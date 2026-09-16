import json
from dataclasses import replace
from datetime import date

import pandas as pd
import pytest
import requests

from ncaaf_model.config import load_settings
from ncaaf_model.sources import DataClient, merge_schedule_frames, parse_espn_scoreboard


def _row(game_id: int, status: str, score: float | None = None) -> dict:
    return {
        "game_id": game_id,
        "game_date": "2099-09-01T00:00Z",
        "home_team": "Home",
        "away_team": "Away",
        "status": status,
        "home_score": score,
    }


def test_schedule_refresh_is_a_union_and_new_row_wins() -> None:
    existing = pd.DataFrame([_row(1, "STATUS_SCHEDULED"), _row(2, "STATUS_SCHEDULED")])
    incoming = pd.DataFrame([_row(1, "STATUS_FINAL", 31.0)])
    merged = merge_schedule_frames(existing, incoming)
    assert set(merged["game_id"]) == {1, 2}
    refreshed = merged.loc[merged["game_id"].eq(1)].iloc[0]
    assert refreshed["status"] == "STATUS_FINAL"
    assert refreshed["home_score"] == 31.0


def test_parse_espn_scoreboard_builds_schedule_contract() -> None:
    payload = {
        "events": [
            {
                "id": "401000001",
                "date": "2099-09-01T16:00Z",
                "season": {"year": 2099, "type": 2},
                "week": {"number": 1},
                "competitions": [
                    {
                        "neutralSite": True,
                        "conferenceCompetition": False,
                        "attendance": 1234,
                        "venue": {"fullName": "Test Stadium"},
                        "status": {"type": {"name": "STATUS_SCHEDULED"}},
                        "competitors": [
                            {
                                "homeAway": "home",
                                "winner": False,
                                "score": "",
                                "team": {"id": "1", "displayName": "Home Bears", "abbreviation": "HOM"},
                            },
                            {
                                "homeAway": "away",
                                "winner": False,
                                "score": "",
                                "team": {"id": "2", "displayName": "Away Cats", "abbreviation": "AWY"},
                            },
                        ],
                    }
                ],
            }
        ]
    }
    frame = parse_espn_scoreboard(payload)
    assert len(frame) == 1
    row = frame.iloc[0]
    assert row["game_id"] == 401000001
    assert row["home_id"] == 1
    assert row["away_id"] == 2
    assert bool(row["neutral_site"])
    assert row["status"] == "STATUS_SCHEDULED"


def _response(status, params, events=()):
    response = requests.Response()
    response.status_code = status
    response.url = "https://example.test/scoreboard?" + requests.compat.urlencode(params)
    response._content = json.dumps({"events": list(events)}).encode()
    return response


@pytest.mark.parametrize("consumer", ["odds", "explicit"])
def test_espn_range_rejection_falls_back_for_both_divisions(tmp_path, monkeypatch, consumer):
    settings = replace(load_settings(), root=tmp_path)
    client = DataClient(settings)
    calls = []
    event = {
        "id": "401000001", "date": "2026-09-19T16:00Z",
        "season": {"year": 2026}, "week": {"number": 3},
        "competitions": [{"competitors": [
            {"homeAway": "home", "team": {"id": "1", "displayName": "Home"}},
            {"homeAway": "away", "team": {"id": "2", "displayName": "Away"}},
        ]}],
    }

    def get(url, *, params, **kwargs):
        calls.append((params["groups"], params["dates"]))
        if "-" in params["dates"]:
            return _response(400, params)
        return _response(200, params, [event] if params["dates"] == "20260919" else [])

    monkeypatch.setattr(client.session, "get", get)
    if consumer == "odds":
        odds_path = tmp_path / "odds.json"
        odds_path.write_text(json.dumps([{
            "commence_time": event["date"], "home_team": "Home", "away_team": "Away",
        }]))
        result = client.ensure_schedule_for_odds(odds_path)
        assert result["remaining_unmatched"] == 0
    else:
        result = client.refresh_espn_schedule_window(date(2026, 9, 14), date(2026, 9, 20))
        assert result["incoming_rows"] == 1
    expected_dates = ["20260914-20260920", *[f"202609{day}" for day in range(14, 21)]]
    assert calls == [(group, day) for group in (80, 81) for day in expected_dates]
    schedule = pd.read_parquet(settings.raw_dir / "sportsdataverse" / "cfb_schedule_2026.parquet")
    assert list(schedule["game_id"]) == [401000001]
    metadata = list((settings.raw_dir / "espn_scoreboard").glob("*.meta.json"))
    assert len(metadata) == 14
    assert all("dates=202609" in json.loads(path.read_text())["source_url"] for path in metadata)


@pytest.mark.parametrize("statuses", [[503], [400, 200, 503]])
def test_espn_failures_do_not_publish_partial_schedule(tmp_path, monkeypatch, statuses):
    settings = replace(load_settings(), root=tmp_path)
    client = DataClient(settings)
    pending = iter(statuses)
    calls = []

    def get(url, *, params, **kwargs):
        calls.append(params)
        return _response(next(pending), params)

    monkeypatch.setattr(client.session, "get", get)
    with pytest.raises(requests.HTTPError):
        client.refresh_espn_schedule_window(date(2026, 9, 14), date(2026, 9, 20))
    assert len(calls) == len(statuses)
    assert not (settings.raw_dir / "sportsdataverse" / "cfb_schedule_2026.parquet").exists()


def test_espn_single_day_uses_single_date_without_retry(tmp_path, monkeypatch):
    client = DataClient(replace(load_settings(), root=tmp_path))
    calls = []

    def get(url, *, params, **kwargs):
        calls.append(params["dates"])
        return _response(200, params)

    monkeypatch.setattr(client.session, "get", get)
    assert client._espn_schedule_frames(date(2026, 9, 19), date(2026, 9, 19), 80) == []
    assert calls == ["20260919"]

from __future__ import annotations

import json
from dataclasses import replace
from datetime import datetime, timezone

import pandas as pd
import requests

from ncaaf_model.config import load_settings
from ncaaf_model.covers_odds import COVERS_ODDS_URL, parse_covers_odds
from ncaaf_model.sources import DataClient


def _book_cell(book: str, game_id: str, away: str, home: str) -> str:
    return f"""
    <td class="liveOddsCell" data-book="{book}" data-game="{game_id}" data-date="1789228800">
      <div class="away-cell">{away}</div>
      <div class="home-cell">{home}</div>
    </td>
    """


def _row(game_id: str, market: str, game_time: str = "Sep 12, 12:00") -> str:
    if market == "h2h":
        away, home = '<span class="__american">+150</span>', '<span class="__american">-170</span>'
        books = ("BetMGM", "DraftKings", "FanDuel")
    elif market == "spreads":
        away = '+3.5 <span class="__american">-105</span>'
        home = '-3.5 <span class="__american">-115</span>'
        books = ("DraftKings",)
    else:
        away = 'o 52.5 <span class="__american">-110</span>'
        home = 'u 52.5 <span class="__american">-110</span>'
        books = ("DraftKings",)
    cells = "".join(_book_cell(book, game_id, away, home) for book in books)
    return f"""
    <tr class="oddsGameRow">
      <td>
        <div class="game-time"><span>{game_time}</span></div>
        <div class="teams-div">
          <div class="away-cell"><img src="/okla.svg"><strong>OKLA</strong></div>
          <div class="home-cell"><img src="/mich.svg"><strong>MICH</strong></div>
        </div>
      </td>
      {cells}
    </tr>
    """


def _document() -> str:
    return f"""
    <html><body>
      <table id="moneyline-table">{_row('42', 'h2h')}{_row('old', 'h2h', 'FINAL')}</table>
      <table id="spread-table">{_row('42', 'spreads')}</table>
      <table id="total-table">{_row('42', 'totals')}</table>
    </body></html>
    """


def _schedule() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "game_id": 401000042,
                "game_date": "2026-09-12T16:00:00Z",
                "away_team": "Oklahoma Sooners",
                "home_team": "Michigan Wolverines",
                "away_abbreviation": "OU",
                "home_abbreviation": "MICH",
            }
        ]
    )


def test_parse_covers_normalizes_three_markets_and_resolves_abbreviation_alias() -> None:
    events, diagnostics = parse_covers_odds(
        _document(),
        _schedule(),
        now=datetime(2026, 9, 6, 12, tzinfo=timezone.utc),
    )
    assert len(events) == 1
    assert diagnostics["skipped_final_game_count"] == 1
    assert diagnostics["unmatched_game_count"] == 0
    event = events[0]
    assert event["away_team"] == "Oklahoma Sooners"
    assert event["home_team"] == "Michigan Wolverines"
    assert event["commence_time"] == "2026-09-12T16:00:00Z"
    assert {book["key"] for book in event["bookmakers"]} == {"betmgm", "draftkings", "fanduel"}
    draftkings = next(book for book in event["bookmakers"] if book["key"] == "draftkings")
    markets = {market["key"]: market["outcomes"] for market in draftkings["markets"]}
    assert markets["h2h"][0]["price"] == 150
    assert markets["spreads"][1]["point"] == -3.5
    assert markets["totals"][0]["point"] == 52.5


def test_current_odds_uses_public_fallback_and_redacts_primary_failure(tmp_path, monkeypatch) -> None:
    settings = replace(load_settings(), root=tmp_path)
    schedule_path = settings.raw_dir / "sportsdataverse" / "cfb_schedule_2026.parquet"
    schedule_path.parent.mkdir(parents=True)
    _schedule().to_parquet(schedule_path, index=False)
    monkeypatch.setenv("ODDS_API_KEY", "test-secret-never-store")
    client = DataClient(settings)
    monkeypatch.setattr(
        client,
        "refresh_espn_schedule_window",
        lambda start, end: {"incoming_rows": 1, "merged_schedule_rows": 1},
    )

    primary = requests.Response()
    primary.status_code = 401
    primary.url = "https://primary.example/odds?apiKey=test-secret-never-store"
    primary._content = b'{"error_code":"OUT_OF_USAGE_CREDITS"}'
    fallback = requests.Response()
    fallback.status_code = 200
    fallback.url = COVERS_ODDS_URL
    fallback._content = _document().encode()
    fallback.encoding = "utf-8"

    def fake_get(url, **kwargs):
        return fallback if url == COVERS_ODDS_URL else primary

    monkeypatch.setattr(client.session, "get", fake_get)
    path, source = client.current_odds(refresh=True)
    assert path.parent.name == "covers"
    assert source["odds_source"] == "covers_public_fallback"
    assert len(json.loads(path.read_text())) == 1
    metadata_text = path.with_suffix(".meta.json").read_text()
    assert '"http_status": 401' in metadata_text
    assert "test-secret-never-store" not in metadata_text

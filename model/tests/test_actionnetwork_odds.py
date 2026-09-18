from datetime import datetime, timezone
import json

import pytest
import requests

from ncaaf_model.actionnetwork_odds import fetch_actionnetwork_odds, parse_scoreboard
from ncaaf_model import actionnetwork_odds


def _books():
    return {
        "books": [
            {"id": 101, "parent_name": "DraftKings", "meta": {"states": ["NY"]}},
            {"id": 102, "parent_name": "FanDuel", "meta": {"states": ["NY"]}},
        ]
    }


def _scoreboard():
    return {
        "games": [
            {
                "id": 123,
                "start_time": "2099-09-01T16:00:00Z",
                "status": "scheduled",
                "home_team_id": 1,
                "away_team_id": 2,
                "teams": [
                    {"id": 1, "full_name": "Home Bears"},
                    {"id": 2, "full_name": "Away Cats"},
                ],
                "markets": {
                    "101": {
                        "event": {
                            "moneyline": [
                                {"side": "home", "odds": -120},
                                {"side": "away", "odds": 100},
                            ],
                            "spread": [
                                {"side": "home", "odds": -110, "value": -2.5},
                                {"side": "away", "odds": -110, "value": 2.5},
                            ],
                        }
                    }
                },
            }
        ]
    }


def test_parse_scoreboard_normalizes_public_actionnetwork_contract() -> None:
    events = parse_scoreboard(
        _scoreboard(),
        {101: ("draftkings", "DraftKings")},
        now=datetime(2099, 1, 1, tzinfo=timezone.utc),
    )
    assert len(events) == 1
    assert events[0]["home_team"] == "Home Bears"
    assert events[0]["bookmakers"][0]["markets"][0]["outcomes"][0]["price"] in {-120, 100}


def test_fetch_actionnetwork_odds_uses_books_then_scoreboard(monkeypatch) -> None:
    class Response:
        def __init__(self, payload):
            self.payload = payload

        def raise_for_status(self):
            return None

        def json(self):
            return self.payload

    responses = iter([Response(_books()), Response(_scoreboard())])

    class Session:
        def get(self, *args, **kwargs):
            return next(responses)

    events, metadata = fetch_actionnetwork_odds(
        Session(), ("draftkings",), 5, state="NY"
    )
    assert len(events) == 1
    assert metadata["odds_source"] == "actionnetwork_public"


def _response(status=200, payload=None):
    response = requests.Response()
    response.status_code = status
    response.url = "https://example.test/scoreboard"
    response._content = json.dumps(payload or {}).encode()
    return response


@pytest.mark.parametrize("failure", [504, "timeout", "connection"])
def test_scoreboard_transient_failure_recovers_without_reloading_books(monkeypatch, failure):
    pending = iter([_response(payload=_books()), failure, _response(payload=_scoreboard())])
    calls, delays = [], []

    class Session:
        def get(self, url, **kwargs):
            calls.append((url, kwargs))
            value = next(pending)
            if value == "timeout":
                raise requests.Timeout("temporary timeout")
            if value == "connection":
                raise requests.ConnectionError("temporary connection failure")
            return _response(value) if isinstance(value, int) else value

    monkeypatch.setattr(actionnetwork_odds, "sleep", delays.append)
    events, metadata = fetch_actionnetwork_odds(Session(), ("draftkings",), 5)
    assert len(events) == 1
    assert metadata["odds_source"] == "actionnetwork_public"
    assert len(calls) == 3
    assert calls[1] == calls[2]
    assert delays == [2]


@pytest.mark.parametrize("status,attempts", [(503, 3), (401, 1), (403, 1), (429, 1)])
def test_feed_retries_are_bounded_and_do_not_retry_access_errors(monkeypatch, status, attempts):
    calls, delays = [], []

    class Session:
        def get(self, url, **kwargs):
            calls.append(url)
            return _response(status)

    monkeypatch.setattr(actionnetwork_odds, "sleep", delays.append)
    with pytest.raises(requests.HTTPError) as captured:
        fetch_actionnetwork_odds(Session(), ("draftkings",), 5)
    assert captured.value.response.status_code == status
    assert len(calls) == attempts
    assert delays == ([2, 4] if attempts == 3 else [])

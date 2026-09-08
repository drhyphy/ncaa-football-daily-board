from datetime import datetime, timezone

from ncaaf_model.actionnetwork_odds import fetch_actionnetwork_odds, parse_scoreboard


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

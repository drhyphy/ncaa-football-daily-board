from __future__ import annotations

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "site_board.py"
SPEC = importlib.util.spec_from_file_location("site_board", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_payload_uses_leading_model_and_strict_qualified_gate():
    payload = MODULE.build_payload()
    assert payload["model_version"] == "ncaaf-market-residual-v2-alpha75"
    assert payload["qualifying_count"] == len(payload["qualified_bets"])
    assert all(row["qualifies"] for row in payload["qualified_bets"])
    assert all(row["expected_value"] >= 0.04 for row in payload["qualified_bets"])
    assert all(row["probability_edge"] >= 0.015 for row in payload["qualified_bets"])


def test_payload_is_json_safe_and_covers_fbs_fcs_board():
    import json

    payload = MODULE.build_payload()
    json.dumps(payload, allow_nan=False)
    assert payload["scanned_games"] >= payload["qualifying_count"]
    assert payload["timing_buckets"]


def test_watchlist_explains_every_failed_gate_in_plain_language():
    payload = MODULE.build_payload()
    assert payload["watchlist"]
    for row in payload["watchlist"]:
        assert len(row["gate_reasons"]) == len(row["flags"])
        assert all("_" not in reason for reason in row["gate_reasons"])
    ev_miss = next(row for row in payload["watchlist"] if "ev_below_threshold" in row["flags"])
    assert any("needs +4.0%" in reason for reason in ev_miss["gate_reasons"])

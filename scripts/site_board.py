"""Build and optionally publish the cloud NCAA football moneyline board."""
from __future__ import annotations

import argparse
import json
import math
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import requests


ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOT = ROOT / "model"
EASTERN = ZoneInfo("America/New_York")
PRIMARY = "market_fpi_residual"
HORIZON_ORDER = ["D8+", "D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0"]


def _as_bool(value: object) -> bool:
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes"}
    return bool(value)


def _finite(value: object) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _gate_reasons(row: pd.Series, flags: list[str]) -> list[str]:
    reasons: list[str] = []
    for flag in flags:
        if flag == "too_few_books":
            count = int(float(row.get("book_count", 0)))
            reasons.append(f"Only {count} {'book' if count == 1 else 'books'}; needs 3")
        elif flag == "market_dispersion_high":
            reasons.append(f"Book dispersion {float(row.get('consensus_dispersion', 0)):.1%}; max 4.5%")
        elif flag == "edge_below_threshold":
            reasons.append(f"Probability edge {float(row.get('probability_edge', 0)):+.1%}; needs +1.5%")
        elif flag == "ev_below_threshold":
            reasons.append(f"Model EV {float(row.get('expected_value', 0)):+.1%}; needs +4.0%")
        elif flag == "schedule_unmatched":
            reasons.append("No verified schedule match")
        elif flag == "fpi_missing":
            reasons.append("FPI matchup projection unavailable")
        elif flag == "game_started":
            reasons.append("Game had already started")
        else:
            reasons.append(flag.replace("_", " ").capitalize())
    return reasons


def _latest_snapshot() -> Path:
    candidates = sorted((MODEL_ROOT / "data" / "snapshots").glob("predictions_*.json"))
    if not candidates:
        raise FileNotFoundError("no prediction snapshot is available")
    return candidates[-1]


def _bet(row: pd.Series, rank: int, qualifies: bool) -> dict:
    flags = [value for value in str(row.get("quality_flags", "")).split("|") if value and value != "nan"]
    selection = str(row["selection"])
    opponent = str(row["away_team"] if row["side"] == "home" else row["home_team"])
    return {
        "rank": rank,
        "event_id": str(row["event_id"]),
        "game": f"{row['away_team']} at {row['home_team']}",
        "selection": selection,
        "opponent": opponent,
        "side": str(row["side"]),
        "kickoff": str(row["commence_time"]),
        "sportsbook": str(row["sportsbook"]),
        "american_odds": int(float(row["american_odds"])),
        "model_probability": round(float(row["model_probability"]), 6),
        "market_probability": round(float(row["market_probability"]), 6),
        "probability_edge": round(float(row["probability_edge"]), 6),
        "expected_value": round(float(row["expected_value"]), 6),
        "stake_fraction": round(float(row.get("stake_bankroll_fraction", 0)), 6),
        "timing_bucket": str(row.get("timing_bucket", "")),
        "book_count": int(float(row.get("book_count", 0))),
        "qualifies": qualifies,
        "flags": flags,
        "gate_reasons": _gate_reasons(row, flags),
    }


def _timing_payload() -> tuple[str, list[dict]]:
    path = MODEL_ROOT / "reports" / "timing_summary.json"
    if not path.exists():
        return "Collecting forward samples — no entry window selected yet.", []
    summary = json.loads(path.read_text(encoding="utf-8"))
    conclusion = summary.get("conclusion", {})
    reason = str(conclusion.get("reason") or "No entry window has enough evidence yet.")
    buckets = {row.get("timing_bucket"): row for row in summary.get("buckets", [])}
    output = []
    for label in HORIZON_ORDER:
        row = buckets.get(label, {})
        output.append({
            "label": label,
            "window": str(row.get("window", "")),
            "signals": int(row.get("signals", 0) or 0),
            "graded": int(row.get("graded_signals", 0) or 0),
            "price_clv": _finite(row.get("mean_price_clv")),
            "roi": _finite(row.get("flat_roi")),
        })
    return reason, output


def _price_history(current: pd.DataFrame) -> list[dict]:
    path = MODEL_ROOT / "ledger" / "predictions.csv"
    if not path.exists() or current.empty:
        return []
    ledger = pd.read_csv(path)
    ledger = ledger.loc[ledger["candidate"].eq(PRIMARY)].copy()
    keys = set(zip(current["event_id"].astype(str), current["side"].astype(str)))
    history = []
    for (event_id, side), group in ledger.groupby([ledger["event_id"].astype(str), ledger["side"].astype(str)]):
        if (event_id, side) not in keys:
            continue
        group = group.sort_values("snapshot_time").drop_duplicates("snapshot_time", keep="last").tail(14)
        history.append({
            "event_id": event_id,
            "side": side,
            "selection": str(group.iloc[-1]["selection"]),
            "snapshots": [
                {
                    "captured_at": str(row["snapshot_time"]),
                    "timing_bucket": str(row.get("timing_bucket", "")),
                    "american_odds": int(float(row["american_odds"])),
                    "expected_value": round(float(row["expected_value"]), 6),
                    "qualifies": _as_bool(row["paper_bet"]),
                }
                for _, row in group.iterrows()
            ],
        })
    return history


def build_payload(snapshot_path: Path | None = None, now: datetime | None = None) -> dict:
    snapshot_path = snapshot_path or _latest_snapshot()
    rows = pd.DataFrame(json.loads(snapshot_path.read_text(encoding="utf-8")))
    primary = rows.loc[rows["candidate"].eq(PRIMARY)].copy()
    if primary.empty:
        raise RuntimeError("the latest snapshot has no leading-model rows")
    primary["commence_dt"] = pd.to_datetime(primary["commence_time"], utc=True)
    primary["snapshot_dt"] = pd.to_datetime(primary["snapshot_time"], utc=True)
    primary = primary.loc[primary["commence_dt"].gt(primary["snapshot_dt"])].copy()
    primary["paper_bet"] = primary["paper_bet"].map(_as_bool)
    qualified = primary.loc[primary["paper_bet"]].sort_values(["expected_value", "probability_edge"], ascending=False)
    watch = primary.loc[~primary["paper_bet"]].sort_values(["probability_edge", "expected_value"], ascending=False).head(20)
    generated = str(rows.iloc[0]["snapshot_time"])
    generated_dt = pd.to_datetime(generated, utc=True).tz_convert(EASTERN)
    kickoff_dates = primary["commence_dt"].dt.tz_convert(EASTERN)
    slate_date = kickoff_dates.min().date().isoformat() if not kickoff_dates.empty else generated_dt.date().isoformat()
    week_values = primary.loc[primary["week"].gt(0), "week"]
    week = int(week_values.mode().iloc[0]) if not week_values.empty else 0
    artifact = json.loads((MODEL_ROOT / "data" / "models" / "market_residual_latest.json").read_text(encoding="utf-8"))
    alpha_key = "weeks_0_4" if week <= 4 else "weeks_5_plus"
    effective_alpha = float(artifact["live_alpha"][alpha_key])
    timing_status, timing_buckets = _timing_payload()
    schedule_matches = primary.loc[primary["espn_game_id"].notna(), "event_id"].nunique()
    return {
        "schema_version": 1,
        "generated_at": generated,
        "slate_date": slate_date,
        "run_label": generated_dt.strftime("%b %-d · %-I:%M %p ET"),
        "model_version": str(primary.iloc[0].get("model_artifact_version", artifact.get("artifact_version"))),
        "week": week,
        "scanned_games": int(primary["event_id"].nunique()),
        "schedule_matches": int(schedule_matches),
        "qualifying_count": int(len(qualified)),
        "alpha_label": f"75% residual · {effective_alpha:.0%} effective FPI",
        "qualified_bets": [_bet(row, rank, True) for rank, (_, row) in enumerate(qualified.iterrows(), 1)],
        "watchlist": [_bet(row, rank, False) for rank, (_, row) in enumerate(watch.iterrows(), 1)],
        "timing_status": timing_status,
        "timing_buckets": timing_buckets,
        "price_history": _price_history(qualified),
        "research_disclaimer": "Forward paper research only; prices can move after capture.",
    }


def publish(payload: dict) -> None:
    endpoint = os.environ.get("SITE_INGEST_URL", "").strip()
    token = os.environ.get("SITE_INGEST_TOKEN", "").strip()
    bypass = os.environ.get("SITE_BYPASS_TOKEN", "").strip()
    if not endpoint or not token:
        raise RuntimeError("SITE_INGEST_URL and SITE_INGEST_TOKEN are required")
    headers = {"X-Ingest-Token": token}
    if bypass:
        headers["OAI-Sites-Authorization"] = f"Bearer {bypass}"
    response = requests.post(endpoint, json=payload, headers=headers, timeout=45)
    response.raise_for_status()
    print(f"published {payload['qualifying_count']} qualified bets from {payload['scanned_games']} games")


def archive_board(payload: dict, path: Path) -> None:
    existing: list[dict] = []
    if path.exists():
        try:
            existing = list(json.loads(path.read_text(encoding="utf-8")).get("boards", []))
        except (json.JSONDecodeError, AttributeError, TypeError):
            existing = []
    boards = [payload, *[row for row in existing if row.get("generated_at") != payload["generated_at"]]]
    boards = sorted(boards, key=lambda row: str(row.get("generated_at", "")), reverse=True)[:14]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"boards": boards}, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--output", type=Path, default=MODEL_ROOT / "reports" / "site_board.json")
    parser.add_argument("--archive", type=Path, default=ROOT / "site-data" / "boards.json")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    payload = build_payload(args.snapshot)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    archive_board(payload, args.archive)
    print(json.dumps({key: payload[key] for key in ("generated_at", "scanned_games", "qualifying_count")}, indent=2))
    if args.publish:
        publish(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

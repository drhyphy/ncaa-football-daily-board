"""Select a morning retry slot unless today's board is already published."""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime, time, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


EASTERN = ZoneInfo("America/New_York")
LOCAL_RUN_SLOTS = {(6, 30), (6, 45), (7, 0)}


def latest_board_date(board_file: str | Path | None) -> date | None:
    if not board_file:
        return None
    path = Path(board_file)
    if not path.exists():
        return None
    payload = json.loads(path.read_text())
    board_dates: list[date] = []
    for board in payload.get("boards", []):
        value = str(board.get("generated_at", "")).replace("Z", "+00:00")
        try:
            board_dates.append(datetime.fromisoformat(value).astimezone(EASTERN).date())
        except ValueError:
            continue
    return max(board_dates) if board_dates else None


def should_run(
    event_name: str,
    schedule: str,
    now_utc: datetime | None = None,
    board_file: str | Path | None = None,
) -> bool:
    if event_name != "schedule":
        return True
    fields = schedule.split()
    if len(fields) != 5:
        raise ValueError(f"invalid cron schedule: {schedule!r}")
    scheduled_minute, scheduled_hour = int(fields[0]), int(fields[1])
    now = (now_utc or datetime.now(timezone.utc)).astimezone(EASTERN)
    scheduled_utc = datetime.combine(
        now.date(), time(scheduled_hour, scheduled_minute), timezone.utc
    )
    scheduled_local = scheduled_utc.astimezone(EASTERN)
    if (scheduled_local.hour, scheduled_local.minute) not in LOCAL_RUN_SLOTS:
        return False
    return latest_board_date(board_file) != now.date()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event-name", required=True)
    parser.add_argument("--schedule", default="")
    parser.add_argument("--board-file")
    args = parser.parse_args()
    return 0 if should_run(args.event_name, args.schedule, board_file=args.board_file) else 3


if __name__ == "__main__":
    raise SystemExit(main())

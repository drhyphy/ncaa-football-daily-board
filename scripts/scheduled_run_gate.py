"""Select the cron slot corresponding to 6:30 AM America/New_York."""
from __future__ import annotations

import argparse
from datetime import datetime, time, timezone
from zoneinfo import ZoneInfo


EASTERN = ZoneInfo("America/New_York")


def should_run(event_name: str, schedule: str, now_utc: datetime | None = None) -> bool:
    if event_name != "schedule":
        return True
    fields = schedule.split()
    if len(fields) != 5:
        raise ValueError(f"invalid cron schedule: {schedule!r}")
    scheduled_minute, scheduled_hour = int(fields[0]), int(fields[1])
    now = (now_utc or datetime.now(timezone.utc)).astimezone(EASTERN)
    intended = datetime.combine(now.date(), time(6, 30), EASTERN).astimezone(timezone.utc)
    return scheduled_minute == intended.minute and scheduled_hour == intended.hour


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event-name", required=True)
    parser.add_argument("--schedule", default="")
    args = parser.parse_args()
    return 0 if should_run(args.event_name, args.schedule) else 3


if __name__ == "__main__":
    raise SystemExit(main())

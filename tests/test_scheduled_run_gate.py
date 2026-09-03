import json
from datetime import datetime, timezone

from scripts.scheduled_run_gate import should_run


def test_manual_runs_always_execute():
    assert should_run("workflow_dispatch", "", board_file="does-not-exist.json")


def test_edt_selects_all_three_morning_slots_even_when_runner_is_delayed():
    delayed = datetime(2026, 9, 2, 17, 18, tzinfo=timezone.utc)
    for schedule in ("30 10 * * *", "45 10 * * *", "0 11 * * *"):
        assert should_run("schedule", schedule, delayed)
    for schedule in ("30 11 * * *", "45 11 * * *", "0 12 * * *"):
        assert not should_run("schedule", schedule, delayed)


def test_est_selects_all_three_morning_slots_even_when_runner_is_delayed():
    delayed = datetime(2026, 12, 2, 17, 18, tzinfo=timezone.utc)
    for schedule in ("30 10 * * *", "45 10 * * *", "0 11 * * *"):
        assert not should_run("schedule", schedule, delayed)
    for schedule in ("30 11 * * *", "45 11 * * *", "0 12 * * *"):
        assert should_run("schedule", schedule, delayed)


def test_today_board_blocks_a_scheduled_retry(tmp_path):
    board_file = tmp_path / "boards.json"
    board_file.write_text(
        json.dumps({"boards": [{"generated_at": "2026-09-03T10:35:00Z"}]})
    )
    now = datetime(2026, 9, 3, 10, 44, tzinfo=timezone.utc)
    assert not should_run("schedule", "45 10 * * *", now, board_file)


def test_prior_day_board_does_not_block_a_scheduled_retry(tmp_path):
    board_file = tmp_path / "boards.json"
    board_file.write_text(
        json.dumps({"boards": [{"generated_at": "2026-09-02T10:35:00Z"}]})
    )
    now = datetime(2026, 9, 3, 10, 44, tzinfo=timezone.utc)
    assert should_run("schedule", "45 10 * * *", now, board_file)

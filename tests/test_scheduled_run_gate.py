from datetime import datetime, timezone

from scripts.scheduled_run_gate import should_run


def test_manual_runs_always_execute():
    assert should_run("workflow_dispatch", "")


def test_edt_selects_1030_utc_even_when_runner_is_delayed():
    delayed = datetime(2026, 9, 2, 17, 18, tzinfo=timezone.utc)
    assert should_run("schedule", "30 10 * * *", delayed)
    assert not should_run("schedule", "30 11 * * *", delayed)


def test_est_selects_1130_utc_even_when_runner_is_delayed():
    delayed = datetime(2026, 12, 2, 17, 18, tzinfo=timezone.utc)
    assert not should_run("schedule", "30 10 * * *", delayed)
    assert should_run("schedule", "30 11 * * *", delayed)

#!/usr/bin/env python3
"""thresholds.py — mechanical date checks on thresholds.yaml (build doc §6.3).

Lists thresholds whose `due` has passed while `status: open`, and those due within
--window days (default 30). With --write-due-passed, sets the `due_passed` flag —
the ONLY tool-writable threshold field. `status: resolved` and `resolution` are
human-set; this tool never resolves a threshold.

Exit codes: 0 nothing overdue · 3 overdue items exist (so a sweep can notice).
"""

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def instance_threshold_files():
    return sorted(ROOT.glob("instances/*/thresholds.yaml"))


def set_due_passed(path, tid, value):
    """Targeted text edit so human-owned comments/format are preserved."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    current = None
    for i, line in enumerate(lines):
        m = re.match(r"-\s+id:\s*(\S+)", line.strip())
        if m:
            current = m.group(1)
        if current == tid and re.match(r"\s*due_passed:", line):
            indent = line[: len(line) - len(line.lstrip())]
            lines[i] = f"{indent}due_passed: {'true' if value else 'false'}\n"
            path.write_text("".join(lines), encoding="utf-8")
            return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window", type=int, default=30, help="days ahead to report (default 30)")
    ap.add_argument("--today", type=str, default=None,
                    help="override today's date (YYYY-MM-DD) — for tests")
    ap.add_argument("--write-due-passed", action="store_true",
                    help="set due_passed on overdue items (mechanical; tool-writable)")
    args = ap.parse_args()

    today = date.fromisoformat(args.today) if args.today else date.today()
    horizon = today + timedelta(days=args.window)
    overdue, soon, undated = [], [], []

    for path in instance_threshold_files():
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        for th in data:
            if not isinstance(th, dict) or th.get("status") != "open":
                continue
            due = th.get("due")
            if due is None:
                undated.append((path, th))
            elif due < today:
                overdue.append((path, th))
            elif due <= horizon:
                soon.append((path, th))

    if overdue:
        print(f"OVERDUE (due passed, still open) — as of {today}:")
        for path, th in overdue:
            days = (today - th["due"]).days
            print(f"  {th['id']} · entry {th['entry']} · due {th['due']} "
                  f"({days} day(s) ago) · {th['description']} · review")
            if args.write_due_passed and not th.get("due_passed"):
                if set_due_passed(path, th["id"], True):
                    print(f"      due_passed set true in {path.relative_to(ROOT)}")
    else:
        print(f"no overdue open thresholds as of {today}")

    if soon:
        print(f"DUE within {args.window} days:")
        for _, th in soon:
            print(f"  {th['id']} · entry {th['entry']} · due {th['due']} · {th['description']}")

    if undated:
        print("open, no date (review on demand):")
        for _, th in undated:
            print(f"  {th['id']} · entry {th['entry']} · {th['description']}")

    return 3 if overdue else 0


if __name__ == "__main__":
    sys.exit(main())

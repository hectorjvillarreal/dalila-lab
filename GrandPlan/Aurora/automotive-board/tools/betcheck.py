#!/usr/bin/env python3
"""betcheck.py — decisive-slot movement flags (build doc §6.3).

Per entry, reports slots marked `decisive: true` whose `value` or `date` changed
since the reference state (default: last run, stored in .betcheck-state.json at the
repo root).

OUTPUT IS A FLAG, NEVER A VERDICT. The tool detects movement; a human (Elle)
adjudicates meaning. This script contains no language about the state of any bet,
by design (build doc §8.3) — emitting any such language is a defect.

Options:
  --init        (re)write the reference state without reporting
  --no-update   report only; leave the reference state untouched
Exit codes: 0 no movement · 4 movement flagged.
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".betcheck-state.json"


def decisive_snapshot():
    snap = {}
    for path in sorted(ROOT.glob("instances/*/board/*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        eid, player = data.get("id"), data.get("player")
        for sname, slot in (data.get("slots") or {}).items():
            if isinstance(slot, dict) and slot.get("decisive") is True:
                key = f"{path.relative_to(ROOT)}::{sname}"
                snap[key] = {
                    "entry": str(eid),
                    "player": str(player),
                    "slot": sname,
                    "value": None if slot.get("value") is None else str(slot.get("value")),
                    "delta": None if slot.get("delta") is None else str(slot.get("delta")),
                    "date": None if slot.get("date") is None else str(slot.get("date")),
                }
    return snap


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--init", action="store_true", help="write reference state and exit")
    ap.add_argument("--no-update", action="store_true", help="do not advance the reference")
    args = ap.parse_args()

    current = decisive_snapshot()

    if args.init or not STATE.is_file():
        STATE.write_text(json.dumps(current, indent=1, sort_keys=True), encoding="utf-8")
        print(f"reference state written: {STATE.name} "
              f"({len(current)} decisive slot(s) tracked). No comparison run.")
        return 0

    ref = json.loads(STATE.read_text(encoding="utf-8"))
    moved = []
    for key, cur in current.items():
        old = ref.get(key)
        if old is None:
            moved.append((cur, "newly tracked"))
        elif cur["value"] != old["value"] or cur["date"] != old["date"]:
            what = []
            if cur["value"] != old["value"]:
                what.append("value")
            if cur["date"] != old["date"]:
                what.append("date")
            moved.append((cur, "+".join(what) + " changed"))
    for key in set(ref) - set(current):
        old = ref[key]
        moved.append((old, "no longer tracked"))

    if moved:
        for cur, what in moved:
            delta = cur["delta"] if cur["delta"] else "-"
            when = cur["date"] if cur["date"] else "-"
            print(f"⚑  {cur['entry']} {cur['player']} · {cur['slot']} (decisive) · "
                  f"{what} · {delta} · {when} · review")
        print(f"{len(moved)} decisive slot(s) moved since reference — human review; "
              f"the tool draws no conclusion.")
    else:
        print("no decisive-slot movement since reference.")

    if not args.no_update:
        STATE.write_text(json.dumps(current, indent=1, sort_keys=True), encoding="utf-8")

    return 4 if moved else 0


if __name__ == "__main__":
    sys.exit(main())

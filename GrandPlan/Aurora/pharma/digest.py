#!/usr/bin/env python
"""Pharma digest layer — a concatenation and a counter. Nothing else.

Build instruction: 20260816_AURORA_BUILD_pharma-digest-layer_v1.0 (pharma/pharma_board/).
Companion doc: DIGESTER.md.

The digest never summarises, ranks, highlights, or characterises. Every line
of DIGEST.md is either copied verbatim from a source report, copied verbatim
from items.yaml fields, or produced by the fixed templates in this file with
arithmetic over counts and dates. The single evaluative word permitted is
`starved`, and it describes the system, never the industry.

Writes: pharma/DIGEST.md (overwritten; previous copy archived to pharma/_digest/
first) — nothing else. feed/ and ratios/ are read-only to this module;
ratios/readings.md is not read in any circumstance. No notifications of any kind.
"""

import os
import re
import sys
import datetime

import yaml

PHARMA_DIR = os.path.realpath(
    os.environ.get("PHARMA_DIR", os.path.dirname(os.path.abspath(__file__)))
)
ITEM_CAP = 40
STARVED_LINE = ("> Calibration is inert. Query retirement, source weighting, entity counting and\n"
                "> cadence are all frozen until promote flags are recorded.")


class BoundaryError(Exception):
    pass


# ---------------------------------------------------------------- file layer

def guarded_write(relpath, content):
    """Only DIGEST.md and _digest/ are writable. Everything else is refused."""
    rp = os.path.realpath(os.path.join(PHARMA_DIR, relpath))
    parent = os.path.dirname(rp)
    if rp == os.path.join(PHARMA_DIR, "DIGEST.md"):
        mode = "w"
    elif parent == os.path.join(PHARMA_DIR, "_digest"):
        mode = "x"  # archive is append-only
    else:
        raise BoundaryError(f"refused: digest writes only DIGEST.md and _digest/, not {relpath}")
    with open(rp, mode) as f:
        f.write(content)


def guarded_read(relpath):
    rp = os.path.realpath(os.path.join(PHARMA_DIR, relpath))
    if os.path.basename(rp) == "readings.md":
        raise BoundaryError("refused: readings.md is off-limits to the tool in every mode")
    if not rp.startswith(PHARMA_DIR + os.sep):
        raise BoundaryError(f"refused: {relpath} resolves outside the pharma directory")
    with open(rp) as f:
        return f.read()


def latest_report(subdir, suffix):
    d = os.path.join(PHARMA_DIR, subdir)
    files = sorted(f for f in os.listdir(d) if f.endswith(suffix)) if os.path.isdir(d) else []
    return f"{subdir}/{files[-1]}" if files else None


# ---------------------------------------------------------------- state block

def compute_state(now):
    items = yaml.safe_load(guarded_read("feed/items.yaml")) or []
    q = yaml.safe_load(guarded_read("feed/queries.yaml"))
    cfg = q["config"]
    unflagged = [it for it in items if it.get("promote") is None]
    total_promotes = sum(1 for it in items if it.get("promote") is True)

    oldest_days = None
    if unflagged:
        oldest = min(datetime.date.fromisoformat(it["date_seen"]) for it in unflagged)
        oldest_days = (now.date() - oldest).days

    ppc = cfg.get("promotes_per_cycle", [])
    cycles_since_promote = 0
    for p in reversed(ppc):
        if p > 0:
            break
        cycles_since_promote += 1

    cycles = cfg["cycles_completed"]
    starved = cycles >= 3 and total_promotes == 0
    if starved:
        calibration = "starved"
    elif cycles >= 3 and total_promotes >= 10:
        calibration = "active"
    else:
        calibration = f"cold start, cycle {min(cycles + 1, 3)} of 3"

    roster_rows = re.findall(r"^\|\s*\d+\s*\|\s*`[^`]+`", guarded_read("ratios/roster.md"), re.M)

    panel_days = None
    latest_panel = latest_report("ratios/_reports", "_panel.md")
    if latest_panel:
        stamp = os.path.basename(latest_panel)[:8]
        panel_days = (now.date() - datetime.date(int(stamp[:4]), int(stamp[4:6]), int(stamp[6:8]))).days

    return {
        "unflagged": unflagged,
        "n_unflagged": len(unflagged),
        "oldest_days": oldest_days,
        "cycles_since_promote": cycles_since_promote,
        "calibration": calibration,
        "starved": starved,
        "provisional_pending": len(q.get("provisional", [])),
        "roster_size": len(roster_rows),
        "panel_days": panel_days,
    }


def render_state(s, now):
    def row(label, value):
        return f"{label} ".ljust(38, ".") + f" {value}"
    lines = [
        f"PHARMA INSTANCE — state as of {now:%Y-%m-%d %H:%M}",
        "",
        row("items awaiting promote flag", s["n_unflagged"]),
        row("oldest unflagged item", "n/a" if s["oldest_days"] is None else f"{s['oldest_days']} days"),
        row("cycles since last promote flag", s["cycles_since_promote"]),
        row("feed calibration", s["calibration"]),
        row("provisional queries pending", s["provisional_pending"]),
        row("roster size", s["roster_size"]),
        row("panel last refreshed", "never" if s["panel_days"] is None else f"{s['panel_days']} days ago"),
    ]
    if s["starved"]:
        lines += ["", STARVED_LINE]
    return "\n".join(lines)


# ---------------------------------------------------------------- blocks 2, 3

def render_feed_block(s):
    latest = latest_report("feed/_reports", "_cycle.md")
    parts = []
    if latest:
        parts.append(f"## Feed — latest cycle report (verbatim: {latest})")
        parts.append("")
        parts.append(guarded_read(latest).rstrip())
    else:
        parts.append("## Feed — no cycle report exists yet")
    parts.append("")
    items = sorted(s["unflagged"], key=lambda it: it["id"], reverse=True)
    shown = items[:ITEM_CAP]
    withheld = len(items) - len(shown)
    header = f"### Unflagged items ({len(items)} awaiting promote flag"
    header += f"; capped at {ITEM_CAP}, {withheld} withheld)" if withheld else ")"
    parts.append(header)
    parts.append("")
    for it in shown:
        parts.append(f'- "{it["headline"]}" — {it["why"]} — {it["date_seen"]} — {it["url"]} '
                     f'— [{it["lane"]}] — {it["id"]}')
    return "\n".join(parts)


def render_panel_block():
    latest = latest_report("ratios/_reports", "_panel.md")
    if not latest:
        return "## Panel — no panel report exists yet"
    return (f"## Panel — latest report (verbatim: {latest})\n\n"
            + guarded_read(latest).rstrip())


# ---------------------------------------------------------------- build

def build():
    now = datetime.datetime.now()
    s = compute_state(now)
    digest = "\n\n---\n\n".join([
        render_state(s, now),
        render_feed_block(s),
        render_panel_block(),
    ]) + "\n"
    prev_path = os.path.join(PHARMA_DIR, "DIGEST.md")
    if os.path.exists(prev_path):
        with open(prev_path) as f:
            prev = f.read()
        guarded_write(f"_digest/{now:%Y%m%d_%H%M}_digest.md", prev)
        archived = True
    else:
        archived = False
    guarded_write("DIGEST.md", digest)
    print(f"DIGEST.md written ({len(digest.splitlines())} lines); "
          f"previous {'archived to _digest/' if archived else 'did not exist'}")
    print(f"state: {s['n_unflagged']} unflagged, calibration {s['calibration']}")


# ---------------------------------------------------------------- selftest

def selftest_boundary():
    ok = True
    for fn, args, label in [
        (guarded_write, ("feed/items.yaml", "x"), "write into feed/"),
        (guarded_write, ("ratios/panel.csv", "x"), "write into ratios/"),
        (guarded_write, ("feed/seeds.md", "x"), "write a human-owned file"),
        (guarded_write, ("../outside.md", "x"), "write outside pharma/"),
        (guarded_read, ("ratios/readings.md",), "READ readings.md"),
    ]:
        try:
            fn(*args)
            print(f"FAIL — {label} was permitted")
            ok = False
        except BoundaryError as e:
            print(f"refused as required — {label}: {e}")
    return ok


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        build()
    elif cmd == "selftest-boundary":
        sys.exit(0 if selftest_boundary() else 1)
    else:
        print("usage: digest.py build | selftest-boundary")

#!/usr/bin/env python
"""Pharma feed harness — layer 1 intake and calibration.

Build instruction: 20260816_AURORA_BUILD_pharma-feed-harness_v1.0 (pharma/pharma_board/).
Companion doc: HARNESS.md.

The harness never decides what matters. It records candidate items with
promote: null, and calibrates *where it looks* from the promote flags Héctor
sets. Retrieval is performed by the executing Claude instance (web search);
this module handles everything deterministic: dedup, state, calibration
arithmetic, reports.

Boundary: all writes confined to the feed directory. seeds.md and rules.md are
human-owned and unwritable through this module (guarded_open), in addition to
being chmod a-w on disk. The promote field is never populated by any code path
here — ingest forces it to null, calibrate only reads it.
"""

import os
import re
import sys
import difflib
import datetime

import yaml

FEED_DIR = os.path.realpath(
    os.environ.get("PHARMA_FEED_DIR", os.path.dirname(os.path.abspath(__file__)))
)
HUMAN_OWNED = {"seeds.md", "rules.md"}

COLD_START_MIN_CYCLES = 3     # calibration inactive through cycle 3...
COLD_START_MIN_PROMOTES = 10  # ...or until 10 promotes, whichever is later
RETIRE_MIN_RESOLVED = 15      # >=15 flagged items, zero promotes -> retire
PROPOSE_MIN_ITEMS = 3         # term must recur across >=3 promoted items
PROPOSE_CAP = 3               # max new provisional queries per cycle
WINDOW = 20                   # rolling window of items per query
SOURCE_WEIGHT_FLOOR = 0.2
CADENCE_BOUNDS = (24, 168)

STOPWORDS = set(
    """a an and are as at be by for from has have in into is it its new of on
    or over says say that the their this to under up us was were will with after
    amid announces announced first more than million billion year years"""
    .split()
)


class BoundaryError(Exception):
    pass


# ---------------------------------------------------------------- file layer

def _path(name):
    return os.path.join(FEED_DIR, name)


def guarded_open(relpath, mode):
    """Sole write path to disk. Refuses human-owned files, anything outside
    FEED_DIR, and overwrites inside the append-only directories."""
    rp = os.path.realpath(os.path.join(FEED_DIR, relpath))
    if not (rp == FEED_DIR or rp.startswith(FEED_DIR + os.sep)):
        raise BoundaryError(f"refused: {relpath} resolves outside the feed directory")
    if os.path.basename(rp) in HUMAN_OWNED:
        raise BoundaryError(f"refused: {os.path.basename(rp)} is human-owned (read-only to the tool)")
    parent = os.path.basename(os.path.dirname(rp))
    if any(c in mode for c in "wxa"):
        if parent == "_reports" and "x" not in mode:
            raise BoundaryError("refused: _reports/ is append-only (create-new only)")
        if parent == "_graveyard" and mode != "a":
            raise BoundaryError("refused: _graveyard/ is append-only")
    return open(rp, mode)


def load_yaml(name, default):
    try:
        with open(_path(name)) as f:
            data = yaml.safe_load(f)
        return data if data is not None else default
    except FileNotFoundError:
        return default


def dump_yaml(name, data):
    with guarded_open(name, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=100)


# ---------------------------------------------------------------- state

def default_state():
    return {
        "config": {
            "cycles_completed": 0,
            "cadence_hours": 48,
            "cycle_budget": 16,
            "exploration_share": 0.25,
            "rotation": {"main": 0, "exploration": 0},
            "resolved_ids": [],
            "promotes_per_cycle": [],
            "next_provisional": 1,
        },
        "main": [],
        "provisional": [],
        "exploration": [],
    }


def parse_seeds():
    """Derive the query set from seeds.md (human-owned, read-only). Lines of
    the form `- q001 \\`text\\`` are main lane; `- x001 \\`text\\`` exploration."""
    with open(_path("seeds.md")) as f:
        text = f.read()
    group = None
    main, exploration = [], []
    for line in text.splitlines():
        g = re.match(r"\*\*(.+?)\*\*\s*$", line.strip())
        if g:
            group = g.group(1)
            continue
        m = re.match(r"-\s+([qx]\d{3})\s+`(.+?)`", line.strip())
        if m:
            qid, qtext = m.groups()
            rec = {"id": qid, "text": qtext, "group": group, "origin": "seed", "window": []}
            (main if qid.startswith("q") else exploration).append(rec)
    return main, exploration


def init_state():
    state = load_yaml("queries.yaml", None)
    if state is not None:
        return state
    state = default_state()
    state["main"], state["exploration"] = parse_seeds()
    dump_yaml("queries.yaml", state)
    if load_yaml("items.yaml", None) is None:
        dump_yaml("items.yaml", [])
    if load_yaml("sources.yaml", None) is None:
        dump_yaml("sources.yaml", {})
    if load_yaml("entities.yaml", None) is None:
        dump_yaml("entities.yaml", {})
    return state


# ---------------------------------------------------------------- plan

def plan(state=None, echo=True):
    """Deterministic query selection for the upcoming cycle: rotation cursors
    over (main + provisional) and over exploration. 25% of budget is the
    exploration reserve — never retired, exempt from yield pressure."""
    state = state or init_state()
    cfg = state["config"]
    budget = cfg["cycle_budget"]
    n_expl = max(1, round(budget * cfg["exploration_share"]))
    n_main = budget - n_expl
    pool = state["main"] + state["provisional"]
    sel_main = [pool[(cfg["rotation"]["main"] + i) % len(pool)] for i in range(min(n_main, len(pool)))]
    expl = state["exploration"]
    sel_expl = [expl[(cfg["rotation"]["exploration"] + i) % len(expl)] for i in range(min(n_expl, len(expl)))]
    if echo:
        for q in sel_main:
            lane = "provisional" if any(p["id"] == q["id"] for p in state["provisional"]) else "main"
            print(f"{q['id']}  [{lane}]  {q['text']}")
        for q in sel_expl:
            print(f"{q['id']}  [exploration]  {q['text']}")
    return sel_main, sel_expl


# ---------------------------------------------------------------- ingest

def _norm_url(url):
    url = url.strip()
    url = re.sub(r"[?&](utm_[a-z]+|fbclid|gclid)=[^&]*", "", url)
    url = re.sub(r"\?$", "", url)
    return url.rstrip("/").lower()


def _norm_headline(h):
    return re.sub(r"[^a-z0-9 ]", "", h.lower()).strip()


def _lane_of(state, query_id):
    for lane in ("main", "provisional", "exploration"):
        if any(q["id"] == query_id for q in state[lane]):
            return "exploration" if lane == "exploration" else lane
    return None


def ingest(candidates_path, state, items, sources, notes):
    with open(candidates_path) as f:
        cands = yaml.safe_load(f) or []
    seen_urls = {_norm_url(it["url"]) for it in items}
    seen_heads = [_norm_headline(it["headline"]) for it in items]
    today = datetime.date.today().isoformat()
    seq = 1 + sum(1 for it in items if it["id"].startswith(today.replace("-", "")))
    added, dup = [], 0
    for c in cands:
        if not all(c.get(k) for k in ("query_id", "headline", "url")):
            notes.append(f"candidate missing required field, skipped: {c!r:.120}")
            continue
        lane = _lane_of(state, c["query_id"])
        if lane is None:
            notes.append(f"candidate cites unknown query_id {c['query_id']}, skipped")
            continue
        nu, nh = _norm_url(c["url"]), _norm_headline(c["headline"])
        if nu in seen_urls or any(
            difflib.SequenceMatcher(None, nh, h).ratio() >= 0.92 for h in seen_heads
        ):
            dup += 1
            continue
        rec = {
            "id": f"{today.replace('-', '')}-{seq:04d}",
            "date_seen": today,
            "date_published": c.get("date_published"),
            "headline": c["headline"].strip(),
            "why": c.get("why", "").strip(),
            "url": c["url"].strip(),
            "source_domain": c.get("source_domain") or re.sub(r"^www\.", "", re.sub(r"^https?://([^/]+).*", r"\1", c["url"])).lower(),
            "entities": c.get("entities") or [],
            "query_id": c["query_id"],
            "lane": lane,
            "promote": None,  # HUMAN FIELD — the tool never sets this
        }
        seq += 1
        items.append(rec)
        added.append(rec)
        seen_urls.add(nu)
        seen_heads.append(nh)
        for lane_name in ("main", "provisional", "exploration"):
            for q in state[lane_name]:
                if q["id"] == rec["query_id"]:
                    q["window"] = (q["window"] + [rec["id"]])[-WINDOW:]
        src = sources.setdefault(rec["source_domain"], {"surfaced": 0, "promoted": 0, "rejected": 0, "weight": 1.0})
        src["surfaced"] += 1
    return added, dup


# ---------------------------------------------------------------- calibration

def calibration_active(state, items):
    promotes = sum(1 for it in items if it.get("promote") is True)
    cycles = state["config"]["cycles_completed"]
    return cycles >= COLD_START_MIN_CYCLES and promotes >= COLD_START_MIN_PROMOTES


def calibration_state_line(state, items, cycle_n=None):
    """cycle_n: the cycle being reported on; defaults to the upcoming cycle."""
    promotes = sum(1 for it in items if it.get("promote") is True)
    if cycle_n is None:
        cycle_n = state["config"]["cycles_completed"] + 1
    if calibration_active(state, items):
        return "active"
    return (f"inactive (cold start: cycle {min(cycle_n, COLD_START_MIN_CYCLES)} of "
            f"{COLD_START_MIN_CYCLES}, promote flags {promotes} of {COLD_START_MIN_PROMOTES})")


def _terms(text):
    words = [w for w in re.sub(r"[^a-z0-9 ]", " ", text.lower()).split() if w not in STOPWORDS and len(w) > 2]
    return set(words) | {" ".join(p) for p in zip(words, words[1:])}


def calibrate(state, items, sources, entities, notes):
    """All adaptive channels. Operates only on counts of promote flags.
    Returns a dict of changes for the report. No-op when calibration inactive."""
    cfg = state["config"]
    by_id = {it["id"]: it for it in items}
    resolved = [it for it in items if it.get("promote") in (True, False)]
    new_resolved = [it for it in resolved if it["id"] not in cfg["resolved_ids"]]
    promotes_new = sum(1 for it in new_resolved if it["promote"] is True)
    cfg["resolved_ids"] = [it["id"] for it in resolved]
    changes = {"promotes_new": promotes_new, "retired": [], "proposed": [],
               "graduated": [], "weight_changes": [], "entity_movers": []}

    if not calibration_active(state, items):
        return changes

    # 5.1 auto-retire — main and provisional; exploration is exempt by construction
    for lane in ("main", "provisional"):
        keep = []
        for q in state[lane]:
            win = [by_id[i] for i in q["window"] if i in by_id]
            res = [it for it in win if it["promote"] in (True, False)]
            pro = sum(1 for it in res if it["promote"] is True)
            if len(res) >= RETIRE_MIN_RESOLVED and pro == 0:
                record = dict(q, retired=datetime.date.today().isoformat(),
                              lane=lane, resolved=len(res), promotes=0)
                with guarded_open("_graveyard/queries_retired.yaml", "a") as f:
                    yaml.safe_dump([record], f, sort_keys=False, allow_unicode=True)
                changes["retired"].append(record)
            else:
                keep.append(q)
        state[lane] = keep

    # 5.1 graduation — provisional -> main after >=1 promoted item
    still = []
    for q in state["provisional"]:
        win = [by_id[i] for i in q["window"] if i in by_id]
        if any(it["promote"] is True for it in win):
            q["graduated"] = datetime.date.today().isoformat()
            state["main"].append(q)
            changes["graduated"].append(q["id"])
        else:
            still.append(q)
    state["provisional"] = still

    # 5.1 auto-propose — quarantined in the provisional lane, cap 3 per cycle.
    # Terms come from promoted HEADLINES only: entities have their own channel
    # (5.3) and tokenizing them proposes junk queries like "united states".
    # A shorter term contained in an accepted longer term is suppressed.
    promoted_items = [it for it in items if it["promote"] is True]
    active_text = " | ".join(q["text"] for lane in ("main", "provisional", "exploration") for q in state[lane]).lower()
    # Retired terms stay retired: a retirement removes the query from active_text,
    # and without this the same promoted headlines re-propose it every cycle.
    try:
        with open("_graveyard/queries_retired.yaml") as f:
            retired_text = " | ".join(q.get("text", "") for q in (yaml.safe_load(f) or [])).lower()
    except FileNotFoundError:
        retired_text = ""
    counts = {}
    for it in promoted_items:
        for t in _terms(it["headline"]):
            counts.setdefault(t, set()).add(it["id"])
    candidates = sorted(
        [(t, ids) for t, ids in counts.items() if len(ids) >= PROPOSE_MIN_ITEMS and t not in active_text and t not in retired_text],
        key=lambda kv: (-len(kv[1]), -len(kv[0])),
    )
    accepted = []
    for t, ids in candidates:
        if len(accepted) >= PROPOSE_CAP:
            break
        if any(t in a or a in t for a, _ in accepted):
            continue
        accepted.append((t, ids))
    for t, ids in accepted:
        pid = f"p{cfg['next_provisional']:03d}"
        cfg["next_provisional"] += 1
        q = {"id": pid, "text": t, "group": "auto-proposed", "origin": "auto",
             "from_items": sorted(ids), "window": []}
        state["provisional"].append(q)
        changes["proposed"].append(q)

    # 5.2 source yield — down-weight only, floor 0.2, never block
    dom_res = {}
    for it in resolved:
        d = dom_res.setdefault(it["source_domain"], [0, 0])
        d[0] += 1
        d[1] += 1 if it["promote"] is True else 0
    overall = (sum(v[1] for v in dom_res.values()) + 1) / (sum(v[0] for v in dom_res.values()) + 2)
    for dom, src in sources.items():
        n, p = dom_res.get(dom, [0, 0])
        src["promoted"], src["rejected"] = p, n - p
        new_w = round(min(1.0, max(SOURCE_WEIGHT_FLOOR, ((p + 1) / (n + 2)) / overall)), 2) if n else 1.0
        if new_w != src["weight"]:
            changes["weight_changes"].append((dom, src["weight"], new_w))
            src["weight"] = new_w

    # 5.3 entity emergence — promoted items only; reported, never nominated
    old = dict(entities)
    entities.clear()
    for it in promoted_items:
        for e in it.get("entities") or []:
            rec = entities.setdefault(e, {"count": 0, "last_seen": None})
            rec["count"] += 1
            rec["last_seen"] = max(rec["last_seen"] or "", it["date_seen"])
    for e, rec in entities.items():
        if rec["count"] != old.get(e, {}).get("count", 0):
            changes["entity_movers"].append((e, old.get(e, {}).get("count", 0), rec["count"]))

    # 5.4 cadence
    history = cfg["promotes_per_cycle"] + [promotes_new]
    old_cad = cfg["cadence_hours"]
    if promotes_new > 6:
        cfg["cadence_hours"] -= 12
    elif len(history) >= 3 and all(p < 1 for p in history[-3:]):
        cfg["cadence_hours"] += 24
    cfg["cadence_hours"] = max(CADENCE_BOUNDS[0], min(CADENCE_BOUNDS[1], cfg["cadence_hours"]))
    if cfg["cadence_hours"] != old_cad:
        changes["cadence"] = (old_cad, cfg["cadence_hours"])
    return changes


# ---------------------------------------------------------------- report

def write_report(state, items, changes, added, dup, notes):
    cfg = state["config"]
    now = datetime.datetime.now()
    cycle_n = cfg["cycles_completed"]  # already incremented = this cycle's number
    by_lane = {}
    for it in added:
        by_lane[it["lane"]] = by_lane.get(it["lane"], 0) + 1
    unflagged = sum(1 for it in items if it.get("promote") is None)
    lines = [
        f"# Feed cycle report — cycle {cycle_n}",
        "",
        f"Machine-authored by harness.py, {now:%Y-%m-%d %H:%M}. "
        "No judgment in this file; all figures are counts.",
        "",
        f"- items retrieved this cycle: {len(added)} "
        f"({', '.join(f'{k}: {v}' for k, v in sorted(by_lane.items())) or 'none'})",
        f"- duplicates discarded: {dup}",
        f"- items awaiting promote flag (total): {unflagged}",
        f"- promotes recorded since last cycle: {changes['promotes_new']}",
        f"- queries retired: {', '.join(r['id'] for r in changes['retired']) or 'none'}",
        f"- provisional queries added: {', '.join(q['id'] + ' (' + q['text'] + ')' for q in changes['proposed']) or 'none'}",
        f"- provisional graduated to main: {', '.join(changes['graduated']) or 'none'}",
        f"- source weight changes: "
        f"{', '.join(f'{d} {a}->{b}' for d, a, b in changes['weight_changes']) or 'none'}",
        f"- entity counts moved: "
        f"{', '.join(f'{e} {a}->{b}' for e, a, b in changes['entity_movers']) or 'none'}",
        f"- cadence: {cfg['cadence_hours']}h"
        + (f" (changed from {changes['cadence'][0]}h)" if "cadence" in changes else " (unchanged)"),
        f"- next cycle due: {now + datetime.timedelta(hours=cfg['cadence_hours']):%Y-%m-%d %H:%M}",
        f"- calibration: {calibration_state_line(state, items, cycle_n)}",
        "",
        "## Noticed, not handled",
        "",
    ]
    lines += [f"- {n}" for n in notes] or ["- nothing"]
    for r in changes["retired"]:
        lines += ["", f"### Retired query record — {r['id']}",
                  f"`{r['text']}` — {r['resolved']} resolved items, 0 promotes. "
                  "Full record in _graveyard/queries_retired.yaml. Reversible by Héctor."]
    name = f"_reports/{now:%Y%m%d_%H%M}_cycle.md"
    with guarded_open(name, "x") as f:
        f.write("\n".join(lines) + "\n")
    return name


# ---------------------------------------------------------------- cycle

def run_cycle(candidates_path):
    state = init_state()
    if not os.path.exists(_path("rules.md")):
        base_notes = ["rules.md (human-owned) does not exist; harness ran on seeds.md alone"]
    else:
        base_notes = []
    notes = list(base_notes)
    items = load_yaml("items.yaml", [])
    sources = load_yaml("sources.yaml", {})
    entities = load_yaml("entities.yaml", {})

    sel_main, sel_expl = plan(state, echo=False)
    added, dup = ingest(candidates_path, state, items, sources, notes)
    changes = calibrate(state, items, sources, entities, notes)

    cfg = state["config"]
    cfg["promotes_per_cycle"].append(changes["promotes_new"])
    cfg["cycles_completed"] += 1
    pool = max(1, len(state["main"]) + len(state["provisional"]))
    cfg["rotation"]["main"] = (cfg["rotation"]["main"] + len(sel_main)) % pool
    cfg["rotation"]["exploration"] = (cfg["rotation"]["exploration"] + len(sel_expl)) % max(1, len(state["exploration"]))

    dump_yaml("items.yaml", items)
    dump_yaml("queries.yaml", state)
    dump_yaml("sources.yaml", sources)
    dump_yaml("entities.yaml", entities)
    report = write_report(state, items, changes, added, dup, notes)
    print(f"cycle {cfg['cycles_completed']} complete: {len(added)} items added, "
          f"{dup} duplicates discarded, report at {report}")
    print(f"calibration: {calibration_state_line(state, items)}")


# ---------------------------------------------------------------- selftest

def selftest_boundary():
    ok = True
    for target, mode, label in [
        ("seeds.md", "w", "write to seeds.md"),
        ("rules.md", "w", "write to rules.md"),
        ("../outside.md", "w", "write outside feed dir"),
        ("_graveyard/queries_retired.yaml", "w", "overwrite in _graveyard"),
    ]:
        try:
            guarded_open(target, mode)
            print(f"FAIL — {label} was permitted")
            ok = False
        except BoundaryError as e:
            print(f"refused as required — {label}: {e}")
    writable = os.access(_path("seeds.md"), os.W_OK)
    print(("FAIL — seeds.md is writable on disk" if writable
           else "seeds.md is chmod read-only on disk — confirmed"))
    existing = [f for f in sorted(os.listdir(_path("_reports"))) if f.endswith(".md")]
    if existing:
        try:
            guarded_open(f"_reports/{existing[0]}", "x")
            print("FAIL — report overwrite path exists")
            ok = False
        except (BoundaryError, FileExistsError) as e:
            print(f"refused as required — overwrite existing report: {type(e).__name__}")
    return ok and not writable


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "init":
        init_state()
        print("state initialised (queries.yaml from seeds.md; empty items/sources/entities)")
    elif cmd == "plan":
        plan()
    elif cmd == "cycle":
        run_cycle(sys.argv[2])
    elif cmd == "selftest-boundary":
        sys.exit(0 if selftest_boundary() else 1)
    else:
        print("usage: harness.py init | plan | cycle <candidates.yaml> | selftest-boundary")

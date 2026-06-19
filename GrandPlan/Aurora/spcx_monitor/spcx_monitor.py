#!/usr/bin/env python3
"""SPCX Brunnermeier-Reis Regime Monitor — local daily-cadence tool.

Aurora project · standalone exercise (NOT wired to the DSGE-OLG core).
Brief: Aurora_Nina_SPCX_BR_Spec_ClaudeCode_202606.md

WHAT THIS IS (and is not). A regime-identification dashboard. Its only outputs
are mechanism states (GREEN/AMBER/RED/INERT) and the next escalation trigger for
each. There is, by construction, no price target, no buy/sell signal, and no
expected-return field. An artifact that outputs a price target has failed the
brief (§0).

DISCIPLINE.
  * No fabricated numbers (§3). An observable left `null` renders as "unset /
    manual" — never as an invented value.
  * Provenance (§3.3, §4, PROTO-RAG-001). Every state CHANGE is timestamped and
    attributed to the specific observable that drove it, appended to run_log.md.
  * The analyst sets each LIVE mechanism's state with a driving observable; the
    tool enforces structure, refuses an unexplained escalation, maintains the
    time series, computes the cross-mechanism coincidence flag, and renders.

USAGE.
  python spcx_monitor.py new [YYYY-MM-DD]    # create today's reading from the
                                             # latest one (values carried forward)
  python spcx_monitor.py render              # rebuild dashboard.html + run_log.md
  python spcx_monitor.py status              # print top-line regime read
  python spcx_monitor.py fetch-macro [DATE]  # optional: pull TIPS-10y & VIX from
                                             # FRED into a day-file (network needed)

Stdlib only — no third-party dependencies, no install step.
"""

import json
import sys
import html
from pathlib import Path
from datetime import date

import taxonomy as T

ROOT = Path(__file__).resolve().parent
STATE_DIR = ROOT / "state"
DASHBOARD = ROOT / "dashboard.html"
RUN_LOG = ROOT / "run_log.md"

SENTINEL = None  # an unset/manual observable; rendered as "—", never fabricated


# --------------------------------------------------------------------------- #
# State files
# --------------------------------------------------------------------------- #
def day_path(d):
    return STATE_DIR / f"{d}.json"


def list_days():
    return sorted(p.stem for p in STATE_DIR.glob("*.json") if p.stem[0].isdigit())


def load_day(d):
    return json.loads(day_path(d).read_text())


def save_day(d, data):
    day_path(d).write_text(json.dumps(data, indent=2) + "\n")


def latest_day():
    days = list_days()
    return days[-1] if days else None


def blank_mechanism(m):
    """An empty per-mechanism reading. INERT mechanisms are fixed to INERT."""
    if m["status"] == "INERT":
        return {
            "state": "INERT",
            "driving_observable": "",
            "observables": {},
            "next_escalation_trigger": "",
        }
    return {
        "state": "UNSET",
        "driving_observable": "",
        "observables": {ob: SENTINEL for ob in m["observables"]},
        "next_escalation_trigger": "",
    }


def new_day(d):
    """Create a day-file, carrying values forward from the latest existing day."""
    prev = latest_day()
    if prev and prev != d:
        base = load_day(prev)
        base["date"] = d
        base["carried_from"] = prev
        # Wipe the per-day provenance note; states/values carry forward as the
        # analyst's working draft until they edit them.
        base["analyst_note"] = ""
        save_day(d, base)
        return d, prev

    data = {
        "date": d,
        "carried_from": None,
        "analyst_note": "",
        "spot": {  # market context, not a target. null until entered.
            "price": SENTINEL,
            "as_of": SENTINEL,
        },
        "mechanisms": {m["id"]: blank_mechanism(m) for m in T.MECHANISMS},
        "macro_backdrop": {ob: SENTINEL for ob in T.MACRO_BACKDROP["observables"]},
    }
    save_day(d, data)
    return d, None


# --------------------------------------------------------------------------- #
# Validation & classification
# --------------------------------------------------------------------------- #
def validate_day(data):
    """Enforce the provenance discipline. Returns a list of problems (strings)."""
    problems = []
    for m in T.MECHANISMS:
        rec = data["mechanisms"].get(m["id"], {})
        st = rec.get("state", "UNSET")
        if m["status"] == "INERT":
            if st != "INERT":
                problems.append(f"{m['id']}: INERT mechanism must stay INERT (got {st}).")
            continue
        if st not in ("GREEN", "AMBER", "RED", "UNSET"):
            problems.append(f"{m['id']}: invalid state {st!r}.")
        # An escalation must name the observable that drove it (PROTO-RAG-001).
        if st in ("AMBER", "RED") and not rec.get("driving_observable", "").strip():
            problems.append(
                f"{m['id']}: state {st} requires a non-empty driving_observable."
            )
    return problems


def coincidence_flag(data):
    """The cross-mechanism coincidence read (brief §3.5).

    The dangerous configuration is *simultaneous* RED across the crash-config set
    {runs, fire_sales, interconnections} — not any single-mechanism RED.
    """
    reds = [mid for mid in T.CRASH_CONFIG_SET
            if data["mechanisms"].get(mid, {}).get("state") == "RED"]
    ambers = [mid for mid in T.LIVE_IDS
              if data["mechanisms"].get(mid, {}).get("state") == "AMBER"]
    any_red = [mid for mid in T.LIVE_IDS
               if data["mechanisms"].get(mid, {}).get("state") == "RED"]

    if len(reds) >= 2:
        return ("CRASH-CONFIG", reds,
                "Simultaneous RED across "
                + " + ".join(reds)
                + " — self-reinforcing configuration. Route to Nina for "
                  "human-judgment interpretation (brief §5.3).")
    if any_red:
        return ("ELEVATED", any_red,
                "Single-mechanism RED (" + ", ".join(any_red)
                + "). Not yet the crash configuration; watch for a second.")
    if len(ambers) >= 2:
        return ("WATCH", ambers,
                "Multiple AMBER (" + ", ".join(ambers) + "). No RED.")
    if ambers:
        return ("WATCH", ambers, "One AMBER (" + ", ".join(ambers) + ").")
    return ("NOMINAL", [], "All live mechanisms GREEN or unset.")


# --------------------------------------------------------------------------- #
# Provenance: detect state changes vs. the prior day and append to run_log.md
# --------------------------------------------------------------------------- #
def diff_states(prev_data, cur_data):
    """Return list of (mech_id, old_state, new_state, driving_observable)."""
    changes = []
    for mid in (m["id"] for m in T.MECHANISMS):
        old = (prev_data or {}).get("mechanisms", {}).get(mid, {}).get("state", "—")
        new = cur_data["mechanisms"].get(mid, {}).get("state", "—")
        if old != new:
            drv = cur_data["mechanisms"][mid].get("driving_observable", "")
            changes.append((mid, old, new, drv))
    return changes


def diff_observables(prev_data, cur_data):
    """LIVE mechanism ids whose observables / driver / trigger changed vs prior.

    Surfaces days where material information arrived but no state threshold was
    crossed — otherwise invisible in a change-only log. Scoped to LIVE-mechanism
    fields only: the macro backdrop and `spot` are context, not regime drivers,
    and a carry-forward heartbeat (the automation's default) touches none of
    these, so it stays a heartbeat.
    """
    changed = []
    for mid in T.LIVE_IDS:
        prev_rec = (prev_data or {}).get("mechanisms", {}).get(mid, {})
        cur_rec = cur_data["mechanisms"].get(mid, {})
        prev_sig = (
            prev_rec.get("observables", {}),
            prev_rec.get("driving_observable", ""),
            prev_rec.get("next_escalation_trigger", ""),
        )
        cur_sig = (
            cur_rec.get("observables", {}),
            cur_rec.get("driving_observable", ""),
            cur_rec.get("next_escalation_trigger", ""),
        )
        if prev_sig != cur_sig:
            changed.append(mid)
    return changed


def rebuild_run_log():
    """Reconstruct run_log.md as the full provenance time series from day-files."""
    days = list_days()
    lines = [
        "# SPCX Regime Monitor — Run Log",
        "",
        "Provenance time series (PROTO-RAG-001). Rows are of three kinds: a "
        "**state change** (date, mechanism, transition, driving observable); an "
        "**observable update** — a day where material observables or triggers "
        "changed but no state threshold was crossed (the day's analyst note is "
        "the row text, and the held state is shown in place of a transition); "
        "and a **heartbeat** for a day with no change at all, carrying the "
        "top-line flag.",
        "",
        "_Generated by `spcx_monitor.py render` — do not edit by hand; edit the "
        "dated state/*.json files and re-render._",
        "",
        "| Date | Flag | Mechanism | Transition | Driving observable |",
        "| --- | --- | --- | --- | --- |",
    ]
    prev = None
    for d in days:
        cur = load_day(d)
        flag, _, _ = coincidence_flag(cur)
        changes = diff_states(prev, cur)
        if changes:
            for mid, old, new, drv in changes:
                name = T.BY_ID[mid]["name"]
                drv_txt = drv.replace("|", "\\|") if drv else "—"
                lines.append(f"| {d} | {flag} | {name} | {old} → {new} | {drv_txt} |")
        else:
            obs_changed = diff_observables(prev, cur) if prev is not None else []
            if obs_changed:
                names = ", ".join(T.BY_ID[mid]["name"] for mid in obs_changed)
                held = "/".join(dict.fromkeys(
                    cur["mechanisms"][mid]["state"] for mid in obs_changed))
                note = (cur.get("analyst_note", "") or "").strip()
                txt = note or "Observables / triggers refreshed; no state threshold crossed."
                txt = txt.replace("|", "\\|")
                lines.append(f"| {d} | {flag} | {names} | obs update — {held} held | {txt} |")
            else:
                lines.append(f"| {d} | {flag} | _(heartbeat — no change)_ | — | — |")
        prev = cur
    RUN_LOG.write_text("\n".join(lines) + "\n")


# --------------------------------------------------------------------------- #
# HTML dashboard
# --------------------------------------------------------------------------- #
STATE_COLORS = {
    "GREEN": "#1b7f3b",
    "AMBER": "#c47f00",
    "RED": "#b3261e",
    "INERT": "#6b6b6b",
    "UNSET": "#9aa0a6",
}

FLAG_COLORS = {
    "CRASH-CONFIG": "#b3261e",
    "ELEVATED": "#c47f00",
    "WATCH": "#8a6d00",
    "NOMINAL": "#1b7f3b",
}


def fmt_val(v):
    if v is None or v == "":
        return '<span class="unset">— unset / manual</span>'
    return html.escape(str(v))


def render_panel(m, rec):
    state = rec.get("state", "UNSET")
    color = STATE_COLORS.get(state, "#9aa0a6")
    inert = m["status"] == "INERT"
    cls = "panel inert" if inert else "panel"

    obs_rows = ""
    for ob in m["observables"]:
        val = rec.get("observables", {}).get(ob, None)
        obs_rows += (
            f'<tr><td class="obk">{html.escape(ob)}</td>'
            f'<td class="obv">{fmt_val(val)}</td></tr>'
        )

    thr = ""
    for s in ("GREEN", "AMBER", "RED"):
        if s in m["thresholds"]:
            thr += (
                f'<div class="thr"><span class="dot" '
                f'style="background:{STATE_COLORS[s]}"></span>'
                f'<b>{s}</b> {html.escape(m["thresholds"][s])}</div>'
            )

    if inert:
        body = (
            f'<p class="rationale">{html.escape(m["spcx_rationale"])}</p>'
            f'<p class="ruled">Considered, ruled out — retained for the record.</p>'
        )
    else:
        drv = rec.get("driving_observable", "")
        nxt = rec.get("next_escalation_trigger", "")
        body = (
            f'<p class="rationale">{html.escape(m["spcx_rationale"])}</p>'
            f'<table class="obs">{obs_rows}</table>'
            f'<div class="thresholds">{thr}</div>'
            f'<div class="driver"><b>Driving observable:</b> {fmt_val(drv)}</div>'
            f'<div class="nextesc"><b>Next escalation trigger:</b> {fmt_val(nxt)}</div>'
        )

    return f"""
    <div class="{cls}">
      <div class="panhead" style="border-color:{color}">
        <span class="mnum">{m['number']}</span>
        <span class="mname">{html.escape(m['name'])}</span>
        <span class="badge" style="background:{color}">{state}</span>
      </div>
      <p class="def">{html.escape(m['definition'])}</p>
      {body}
    </div>"""


def render_macro(macro):
    rows = ""
    for ob in T.MACRO_BACKDROP["observables"]:
        rows += (
            f'<tr><td class="obk">{html.escape(ob)}</td>'
            f'<td class="obv">{fmt_val(macro.get(ob))}</td></tr>'
        )
    return f"""
    <div class="panel macro">
      <div class="panhead" style="border-color:#3a6ea5">
        <span class="mname">{html.escape(T.MACRO_BACKDROP['name'])}</span>
        <span class="badge" style="background:#3a6ea5">CONTEXT</span>
      </div>
      <table class="obs">{rows}</table>
      <p class="ruled">{html.escape(T.MACRO_BACKDROP['note'])}</p>
    </div>"""


def render_dashboard():
    d = latest_day()
    if not d:
        print("No state files. Run: python spcx_monitor.py new", file=sys.stderr)
        return 1
    data = load_day(d)
    problems = validate_day(data)
    flag, members, flag_msg = coincidence_flag(data)
    fcolor = FLAG_COLORS.get(flag, "#6b6b6b")

    spot = data.get("spot", {})
    spot_txt = (
        f'price {fmt_val(spot.get("price"))} · as of {fmt_val(spot.get("as_of"))}'
    )

    # Top strip: consolidated read across live mechanisms.
    chips = ""
    for mid in T.LIVE_IDS:
        st = data["mechanisms"][mid]["state"]
        chips += (
            f'<span class="chip" style="background:{STATE_COLORS.get(st)}">'
            f'{html.escape(T.BY_ID[mid]["name"])}: {st}</span>'
        )

    panels = "".join(render_panel(m, data["mechanisms"][m["id"]])
                     for m in T.MECHANISMS)
    macro_panel = render_macro(data.get("macro_backdrop", {}))

    warn = ""
    if problems:
        items = "".join(f"<li>{html.escape(p)}</li>" for p in problems)
        warn = (f'<div class="warn"><b>Validation:</b><ul>{items}</ul>'
                f'These must be resolved in the state file; the reading is '
                f'provisional until then.</div>')

    note = data.get("analyst_note", "")
    note_html = f'<p class="anote">{html.escape(note)}</p>' if note else ""

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SPCX Regime Monitor — {d}</title>
<style>
  :root {{ font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; }}
  body {{ margin:0; background:#0f1115; color:#e6e6e6; }}
  header {{ padding:18px 24px; background:#15181f; border-bottom:1px solid #2a2f3a; }}
  h1 {{ font-size:18px; margin:0 0 2px; }}
  .sub {{ color:#9aa0a6; font-size:12px; }}
  .topstrip {{ padding:14px 24px; background:#12141a; border-bottom:1px solid #2a2f3a; }}
  .flag {{ display:inline-block; padding:6px 12px; border-radius:6px; font-weight:700;
           color:#fff; background:{fcolor}; }}
  .flagmsg {{ color:#c8ccd2; font-size:13px; margin-top:8px; max-width:900px; }}
  .chips {{ margin-top:10px; }}
  .chip {{ display:inline-block; color:#fff; font-size:12px; font-weight:600;
           padding:3px 9px; border-radius:12px; margin:0 6px 6px 0; }}
  .spot {{ color:#9aa0a6; font-size:12px; margin-top:8px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(330px,1fr));
           gap:14px; padding:18px 24px; }}
  .panel {{ background:#171a21; border:1px solid #262b35; border-radius:10px; padding:14px; }}
  .panel.inert {{ opacity:0.55; }}
  .panel.macro {{ border-color:#2c3e54; }}
  .panhead {{ display:flex; align-items:center; gap:8px; border-left:4px solid;
              padding-left:8px; margin-bottom:8px; }}
  .mnum {{ color:#6b7280; font-weight:700; font-size:12px; }}
  .mname {{ font-weight:700; font-size:14px; flex:1; }}
  .badge {{ color:#fff; font-size:11px; font-weight:700; padding:2px 8px; border-radius:10px; }}
  .def {{ color:#aab0b8; font-size:12px; margin:6px 0; }}
  .rationale {{ color:#cfd4da; font-size:12.5px; margin:6px 0; }}
  .ruled {{ color:#8a909a; font-style:italic; font-size:12px; }}
  table.obs {{ width:100%; border-collapse:collapse; margin:8px 0; }}
  table.obs td {{ font-size:12px; padding:3px 4px; border-bottom:1px solid #232833; vertical-align:top; }}
  .obk {{ color:#9aa0a6; width:55%; font-family:ui-monospace,Menlo,monospace; }}
  .obv {{ color:#e6e6e6; }}
  .unset {{ color:#6b7280; font-style:italic; }}
  .thresholds {{ margin:8px 0; }}
  .thr {{ font-size:11.5px; color:#bcc2ca; margin:3px 0; }}
  .dot {{ display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:5px; }}
  .driver, .nextesc {{ font-size:12px; margin-top:6px; color:#dfe3e8; }}
  .nextesc {{ background:#1d2230; padding:6px 8px; border-radius:6px; }}
  .warn {{ margin:14px 24px; background:#2a1d1d; border:1px solid #5a2b2b; color:#f3c0c0;
           padding:10px 14px; border-radius:8px; font-size:12.5px; }}
  .warn ul {{ margin:6px 0 6px 18px; }}
  .anote {{ margin:10px 24px; color:#cfd4da; font-size:13px; }}
  footer {{ padding:16px 24px; color:#6b7280; font-size:11px; border-top:1px solid #2a2f3a; }}
  .nogo {{ color:#7d8593; }}
</style></head>
<body>
<header>
  <h1>SPCX — Brunnermeier-Reis Regime Monitor</h1>
  <div class="sub">Aurora · standalone exercise · regime identification only —
    no price target, no buy/sell, no expected return (brief §0)</div>
</header>
<div class="topstrip">
  <span class="flag">{flag}</span>
  <span class="spot">· {spot_txt}</span>
  <div class="flagmsg">{html.escape(flag_msg)}</div>
  <div class="chips">{chips}</div>
</div>
{warn}
{note_html}
<div class="grid">{panels}{macro_panel}</div>
<footer>
  Reading date {d}{' · carried from ' + data['carried_from'] if data.get('carried_from') else ''}.
  Source of truth: <code>state/{d}.json</code>. Provenance: <code>run_log.md</code>.
  <span class="nogo">Outputs are regime states and escalation triggers — by
  construction this artifact contains no directional or price output.</span>
</footer>
</body></html>"""

    DASHBOARD.write_text(doc)
    rebuild_run_log()
    print(f"Rendered {DASHBOARD.name} for {d}  ·  flag: {flag}")
    if problems:
        print(f"  ⚠ {len(problems)} validation problem(s) — see dashboard / fix state file.")
    return 0


# --------------------------------------------------------------------------- #
# Optional macro fetch (FRED CSV; needs network). Never fabricates on failure.
# --------------------------------------------------------------------------- #
FRED = {
    "tips_10y_real_yield": "DFII10",
    "vix_level": "VIXCLS",
}


def fetch_macro(d):
    import urllib.request
    if not day_path(d).exists():
        print(f"No day-file for {d}; run `new` first.", file=sys.stderr)
        return 1
    data = load_day(d)
    got = {}
    for key, series in FRED.items():
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                rows = r.read().decode().strip().splitlines()
            # last row with a numeric value
            for line in reversed(rows[1:]):
                parts = line.split(",")
                if len(parts) == 2 and parts[1] not in (".", ""):
                    data["macro_backdrop"][key] = f"{parts[1]} ({parts[0]}, FRED {series})"
                    got[key] = parts[1]
                    break
        except Exception as e:  # network blocked / offline — leave unset, never fake
            print(f"  · {series}: fetch failed ({e}); left unset (no fabrication).")
    save_day(d, data)
    print(f"Macro fetch into {d}: {got if got else 'nothing retrieved (fields left unset)'}")
    return 0


# --------------------------------------------------------------------------- #
def cmd_status():
    d = latest_day()
    if not d:
        print("No readings yet.")
        return 1
    data = load_day(d)
    flag, members, msg = coincidence_flag(data)
    print(f"SPCX regime read — {d}")
    print(f"  Top-line flag: {flag}")
    print(f"  {msg}")
    for mid in T.LIVE_IDS:
        rec = data["mechanisms"][mid]
        print(f"  [{rec['state']:>5}] {T.BY_ID[mid]['name']}"
              + (f"  ← {rec['driving_observable']}" if rec.get('driving_observable') else ""))
    for mid in T.INERT_IDS:
        print(f"  [INERT] {T.BY_ID[mid]['name']}")
    return 0


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "status"
    arg = argv[2] if len(argv) > 2 else None
    today = arg or date.today().isoformat()

    if cmd == "new":
        d, prev = new_day(today)
        msg = f"Created state/{d}.json"
        msg += f" (carried forward from {prev})" if prev else " (fresh baseline)"
        print(msg)
        print("Edit it, then: python spcx_monitor.py render")
        return 0
    if cmd == "render":
        return render_dashboard()
    if cmd == "status":
        return cmd_status()
    if cmd == "fetch-macro":
        return fetch_macro(today)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# SPCX Brunnermeier-Reis Regime Monitor

Aurora project · standalone exercise. Built to the brief
[`Aurora_Nina_SPCX_BR_Spec_ClaudeCode_202606.md`](../Aurora_Nina_SPCX_BR_Spec_ClaudeCode_202606.md).

**Not** wired to the DSGE-OLG fiscal core, the DFD engine, or any OLG
calibration (brief §0). It converges with the core only later, through an
OLG-ABM interface that does not yet exist.

## What it is

A **regime-identification dashboard** over the five amplification mechanisms in
Brunnermeier & Reis, *A Crash Course on Crises* (Princeton UP, 2023), applied to
SPCX. Its only outputs are mechanism states (GREEN/AMBER/RED/INERT) and the
**next escalation trigger** for each. By construction it carries **no price
target, no buy/sell signal, and no expected-return field**. An artifact that
outputs a price target has failed the brief.

Three mechanisms are **LIVE** for SPCX (Runs, Fire Sales, Interconnections), two
are **INERT** (Currency Mismatch; Inflation-Deflation at the asset level) and are
retained — not omitted — so the record shows they were considered and ruled out.
The inflation-deflation panel keeps a **macro-backdrop context gauge** (real
rates, VIX, narrative-vs-cashflow rotation) that conditions belief-driven assets
without itself escalating any SPCX mechanism.

## Files

| File | Role |
| --- | --- |
| `taxonomy.py` | Single source of truth for the five mechanisms: definitions, live/inert status, observables, threshold logic. |
| `spcx_monitor.py` | The tool: state management, validation, coincidence flag, run-log, HTML rendering. Stdlib only — no installs. |
| `state/YYYY-MM-DD.json` | One dated reading per day. **The source of truth.** Edit these by hand. |
| `dashboard.html` | Generated view of the latest reading. Disposable — re-rendered from state. |
| `run_log.md` | Generated provenance time series of every state change. Do not edit by hand. |

## Daily cycle

```bash
conda activate dalila            # stdlib only, but this is the project env

python spcx_monitor.py new       # create today's reading, values carried
                                 # forward from the most recent day
# (optional) pull macro context — needs network; leaves fields unset if offline:
python spcx_monitor.py fetch-macro

# edit state/<today>.json:
#   - update observable values you have (leave unknowns as null — never invent)
#   - set each LIVE mechanism's "state" (GREEN/AMBER/RED)
#   - for any AMBER/RED, fill "driving_observable" (REQUIRED — the tool refuses
#     an unexplained escalation) and refresh "next_escalation_trigger"

python spcx_monitor.py render    # rebuild dashboard.html + run_log.md
python spcx_monitor.py status    # top-line regime read in the terminal
```

Open `dashboard.html` in a browser to view the five panels, the macro context
panel, and the top strip (consolidated read + coincidence flag).

## Run-log convention (deliverable §5.2)

`run_log.md` is regenerated on every `render` from the dated state files, so the
state files remain the only thing you edit. Each row is a **state change**: the
date, the mechanism, the transition (`old → new`), and the observable that drove
it. Days with no change are recorded as a heartbeat carrying the top-line flag.
This is the corpus-admissible reasoning record under PROTO-RAG-001 — the history
accumulates as a regime time series, not a snapshot.

## The coincidence flag (brief §3.5)

The dangerous configuration is **not** any single-mechanism RED but *simultaneous*
RED across the crash-config set {Runs, Fire Sales, Interconnections}. Flag levels:

- **NOMINAL** — all live mechanisms GREEN or unset.
- **WATCH** — one or more AMBER, no RED.
- **ELEVATED** — a single live mechanism RED. Watch for a second.
- **CRASH-CONFIG** — ≥2 of the crash-config set RED simultaneously. This is the
  self-reinforcing configuration the taxonomy exists to catch; per §5.3 it is
  routed to Nina for a human-judgment layer, not an automated conclusion.

## Discipline guarantees (enforced in code)

- **No fabricated numbers.** A `null` observable renders as "— unset / manual",
  never as an invented value. Macro fetch leaves fields unset on failure rather
  than faking them.
- **Provenance.** Every AMBER/RED state requires a `driving_observable`;
  `validate_day` flags any escalation that lacks one, and the dashboard shows the
  validation problems until they are resolved.
- **INERT stays inert.** The two ruled-out mechanisms cannot be silently flipped
  live; validation rejects it.
- **No directional output exists.** There is no field in the schema for a price
  target, return, or recommendation.

## Note on git

These files live under `GrandPlan/Aurora/`. The repository's current working
branch may be a BID2/calibration branch unrelated to Aurora — commit this to an
Aurora-appropriate branch, not whatever calibration branch happens to be checked
out.

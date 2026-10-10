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
| `handoffs/` | Discretionary cross-agent handoff notes (e.g. to Nina). Hand-written, dated `YYYY-MM-DD_<agent>.md`, provenance-disciplined per PROTO-RAG-001. `agent_handoff` is not yet a protocol-codified type. Sent outside §5.3 (which routes to Nina only on CRASH-CONFIG). |

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

### Manual-pass checklist (added 2026-10-08)

The 10-07 pass attributed a -2.5% day to yields/oil when the FT's $40B
debt-plan report was already out; the 09-17 Fed hike went unrecorded for three
weeks. Every manual pass now runs ALL of these, not just tape + EDGAR:

1. **Tape** — Nasdaq historical API, re-sourced from scratch; if the day's close
   is not posted yet, mark it as derived and re-verify next pass.
2. **EDGAR** — issuer submissions feed (CIK 1181412) + S-1-family full-text
   search for Anthropic.
3. **Fixed press sweep** (one search each; record the driver of any |move| >
   2% or any volume > 1.25x, or write "no driver found"):
   SpaceX debt / financing / bonds · SpaceX CDS / credit spreads · SPCX lockup /
   unlock · SpaceX Q3 earnings date (arms the 1.3B tranche) · Starship next
   flight · Anthropic IPO / S-1 timing · Grain 800 MHz / spectrum M&A ·
   SPCX analyst notes.
4. **Macro** — `fetch-macro` (TIPS 10y, VIX, Fed funds target upper bound);
   any change in the Fed target goes into `vix_trend` with its date.
5. **Issuer debt facts** — `fire_sales.observables.issuer_debt_outstanding`
   is refreshed from each 10-Q/10-K (XBRL companyfacts). Facts only: dollar
   debt and CDS are press-only for regime purposes until a signed 8-K
   (ruling 2026-10-08).

## Automation (daily systemd timer on Dalila)

A **systemd user timer** runs the full daily cycle so the regime time series
accumulates without manual intervention. Each run does, in order:

1. `reset --hard main` — clean the worktree to the latest committed state.
2. `new <today>` — create today's reading by carry-forward, **only if it does not
   already exist**. This guard is essential: `new` on an existing date would
   overwrite it, clobbering any manual edits/classification made that day.
3. `fetch-macro` — refresh the macro backdrop (TIPS-10y, VIX from FRED); fields
   are left unset on network failure, never fabricated.
4. `render` — regenerate `dashboard.html` / `run_log.md`.
5. commit to `main` and push (push failure is non-fatal; commits sync on a later
   run or a manual push).

Important: the cycle **carries forward** the prior day's regime states — it does
**not** set or change any GREEN/AMBER/RED call. So daily entries appear in the
run-log as `heartbeat — no change` until a human edits a day's state file.
Classification remains a deliberate analyst action (auto-classification would
fabricate judgement); the automation only keeps the series, the macro panel, and
the dashboard current.

A systemd timer is used instead of plain `cron` because Dalila is a laptop that
suspends: with `Persistent=true`, a run missed while suspended/off executes on the
next wake/boot, whereas `cron` silently skips it. Lingering is enabled
(`loginctl enable-linger hectorjuan`) so the user timer runs without an active
login session.

Because the monitor lives on `main` but day-to-day work happens on feature
branches, the render runs from a **dedicated sparse git worktree pinned to
`main`** — independent of whatever branch the primary repo has checked out.

Components:

| Piece | Location |
| --- | --- |
| Worktree (sparse, `main`, ~124K) | `/home/hectorjuan/Dalila-spcx` (only `spcx_monitor/` checked out) |
| Wrapper script | `~/.local/bin/spcx_render.sh` |
| systemd service | `~/.config/systemd/user/spcx-render.service` (`Type=oneshot`) |
| systemd timer | `~/.config/systemd/user/spcx-render.timer` (`OnCalendar=*-*-* 18:00`, `Persistent=true`) |
| Run log | `~/.spcx_render.log` |
| Rendered artifact to view | `/home/hectorjuan/Dalila-spcx/GrandPlan/Aurora/spcx_monitor/dashboard.html` |

Operate it with:
`systemctl --user {status,start,list-timers} spcx-render.{timer,service}`.

The wrapper does `git -C <worktree> reset --hard main` before rendering: this
discards the previous run's regenerated (tracked) artifacts and syncs to `main`'s
current tip with no network and without moving the ref. So newly committed state
is picked up automatically on the next run.

Caveat: while the worktree exists, `git checkout main` in the primary repo
(`/home/hectorjuan/Dalila`) is refused (`main` is checked out in the worktree).

Teardown: `systemctl --user disable --now spcx-render.timer`, then
`rm ~/.config/systemd/user/spcx-render.{timer,service}` and
`systemctl --user daemon-reload`, then
`git worktree remove /home/hectorjuan/Dalila-spcx`, then
`rm ~/.local/bin/spcx_render.sh`. Optionally `loginctl disable-linger hectorjuan`.

### S-1 flip checks (Interconnections de-escalation observable)

The Anthropic public S-1 flip is checked on EDGAR at every manual pass. On top
of that, two one-shot checks bracket the re-pinned no-flip bound (2026-10-31,
ruling 10-03). Both are **report-only**: they never edit state, classify, or
commit; the analyst reads the result into the next manual pass.

| Check | When | Where | Notes |
| --- | --- | --- | --- |
| Cloud routine `trig_01DvdE4u1tH5qDYjuBx6TFBD` | 2026-10-31 22:00 UTC (16:00 CST) | claude.ai/code/routines | Prompt carries verification state through 10-09. Its environment blocked sec.gov on the 09-01 and 09-30 firings, so it may fall back to a press-only null. |
| Local backstop `spcx-s1-recheck.timer` | Mon 2026-11-02 09:00 CST (`Persistent=true`) | `~/.local/bin/spcx_s1_recheck.py` (stdlib); unit `~/.config/systemd/user/spcx-s1-recheck.{service,timer}`; log `~/.spcx_s1_recheck.log` | Runs from Dalila, so EDGAR is reachable. Writes `~/spcx_s1_recheck_<date>.md` plus a desktop notification. |

The backstop runs four checks: the daily form indices 10-09..10-30 (Form 4 row
count as freshness guard; Anthropic rows in S-1/S-1/A/DRS/F-1), a full-text
search for `"Anthropic PBC"` and `Anthropic` in the same forms, an EDGAR
company search, and SPCX issuer filings since 10-09 (an 8-K is flagged for a
signed debt financing under the 10-08 ruling and for the Q3 earnings date). It
ends with one verdict line: FILED, NOT YET FILED (VERIFIED), or INCONCLUSIVE.

Two EDGAR behaviours are built in:

- **EDGAR answers 403, not 404, for a daily index not yet published.** The
  script fetches a known index first (`form.20261009.idx`) as a control: if the
  control loads, a 403 on a later date means "unpublished"; if the control fails,
  sec.gov is blocked and every request is counted as an error.
- **An unpublished index is not a null.** Any missing business day other than
  10-12 (Columbus Day, EDGAR closed) makes the verdict INCONCLUSIVE, never
  VERIFIED.

Manual re-run: `~/.local/bin/spcx_s1_recheck.py`. After 11-02:
`systemctl --user disable spcx-s1-recheck.timer`. The timer is dated and will
not fire again, but disabling it keeps `list-timers` clean.

## Run-log convention (deliverable §5.2)

`run_log.md` is regenerated on every `render` from the dated state files, so the
state files remain the only thing you edit. Rows are of three kinds:

- **State change** — the date, the mechanism, the transition (`old → new`), and
  the observable that drove it.
- **Observable update** — a day where a LIVE mechanism's observables, driving
  observable, or next-escalation trigger changed but **no state threshold was
  crossed**. Without this row such a day would log as a bare heartbeat, hiding
  material information (e.g. a confirmed acquisition or a new lockup date that
  did not flip any state). The transition column shows the held state(s) (e.g.
  `obs update — GREEN held`) and the row text is that day's `analyst_note`. The
  trigger is scoped to LIVE-mechanism fields only — `spot` and the macro
  backdrop are context, so a carry-forward heartbeat stays a heartbeat.
- **Heartbeat** — a day with no change at all, carrying the top-line flag.

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

# Aging × Macro paper monitor

DFD project · local weekly alarm for new top papers on population aging and the
macroeconomy. Companion doc for `aging_macro_monitor.py` (coding convention §9).
Built 2026-09-17 after the NBER aging-conference batch showed the cost of finding
such papers by hand.

## What it does

Once a week (systemd user timer, Tuesday 07:30 local, catches up after sleep) it
pulls new items from (IZA has no working RSS as of 2026-09-17; its papers arrive via RePEc NEP):

| Source | Feed | Notes |
|---|---|---|
| NBER new working papers | `back.nber.org/rss/new.xml` | ~35 latest; authors parsed from the title |
| RePEc NEP lists | `nep.repec.org/rss/{list}.rss.xml` | AGE, DGE, DEM, PBE, MAC, LAM, GRO |
| arXiv econ.GN | export API, keyword query | noisy; no source prior |
| OpenAlex | works search, six queries, date-filtered | catches journal articles incl. LAC outlets |

Each item is scored against `profile.json`: an aging/demographic **core term is
required**; macro terms, LAC geography, tracked authors and top venues add; low-tier
venues subtract. **ALERT** needs a macro term, one quality signal (known series,
top venue, tracked author, or LAC geography) and at least one strong core term
(`weak_core_terms` such as *births* or *cohort* score but cannot carry an alert alone); everything else with a core hit is
**WATCH** or dropped. A paper is recorded once in `state/seen.json` and never
re-alerted.

Outputs: `digests/YYYY-MM-DD_digest.md` (ALERT items with abstract and a ready
`_acquisition_queue.md` line; WATCH one-liners), a line in `run_log.md`, and a
desktop notification when ALERT ≥ 1.

## What it does not do

- Never writes into the demographics corpus, the acquisition queue, or any
  endorsed artifact. Queue lines are pasted by hand, in session, under the
  drafter's own `added_by` (PROTO-RAG-001 authorship discipline).
- Never fabricates metadata. Missing abstracts render as such.
- Does not commit. Digests are untracked until reviewed and committed in session.

## Optional local-model re-rank

If ollama serves the model named in `profile.json` (`qwen3.5:9b`, the Grand Plan
decision), candidates above the watch threshold are re-scored 0–10 against the
interest profile and combined with the keyword score. Ollama is **not installed**
on Dalila as of 2026-09-17; the stage logs itself as skipped until it is.

## Operating

```
conda activate dalila
python aging_macro_monitor.py run --dry     # preview, no writes
python aging_macro_monitor.py run           # full cycle
python aging_macro_monitor.py status        # ledger + timer
systemctl --user list-timers aging-macro-monitor.timer
journalctl --user -u aging-macro-monitor.service -n 30
```

Units: `~/.config/systemd/user/aging-macro-monitor.{service,timer}`, wrapper
`~/.local/bin/aging_macro_monitor.sh`, log `~/.aging_macro_monitor.log`.
Tune thresholds, terms, authors and venues in `profile.json`; no code change needed.
Teardown: `systemctl --user disable --now aging-macro-monitor.timer`.

## First run

2026-09-17 baseline over a 21-day lookback; see `digests/2026-09-17_digest.md`.
Subsequent runs look back to three days before the previous run.

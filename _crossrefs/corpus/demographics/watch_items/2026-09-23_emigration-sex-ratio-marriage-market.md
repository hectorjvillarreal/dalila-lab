---
type: research_watch_item
status: open
date_opened: 2026-09-23
opened_by: [Anne, Claude Code]
endorsed_by: Anne
promoted_by:
date_promoted:
related_corpus: [_crossrefs/corpus/demographics/releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md, _crossrefs/corpus/demographics/country/MEX/mex_scenarios_eic2025.md, _crossrefs/corpus/demographics/watch_items/2026-09-15_goldin-gender-mismatch-stress-floor.md]
related_projects: [DFD]
build_instruction: "_crossrefs/corpus/demographics/_pending/2026-09-23_EIC-rebased-scenarios_Anne-record.md (record-driven execution; no separate build instruction, precedent 2026-09-23)"
---

# Male-skewed emigration and the marriage-market sex ratio at 20–29 — coupling-channel input

## Origin

Opened by Anne's EIC-graphs record of 2026-09-23 (§3.3, "paper-chat flag"), on the EIC 2025
emigration profile: net outflow 2020–25 of roughly 1.3 M out and 0.15 M back,
70.4 % male, concentrated at 20–29 (22.5 % at 20–24, 19.5 % at 25–29, 15.0 % at
15–19, 14.1 % at 30–34). Anne's instruction: **log; do not model yet.**

The 2015–20 outflow was already ≈67% male (537,149 of 802,807); the 2020–25 outflow at 70.4% male and ≈60% higher gross volume is an intensification of an existing skew, not a new phenomenon. Read the marriage-market effect as a level that steepened, not as a regime that began in 2020.

## The mechanism to watch

A male-skewed outflow at 20–29 tightens the sex ratio in the marriage market for
women aged 20–29. That is a **coupling-channel** input to the union-composition
mechanism of the fertility-collapse paper, distinct from fertility per se: it
changes who is available to partner, not the fertility of those partnered. The
EIC 2025 partnered share (12+ = 50.22 %, women 48.42 %) is logged as a coupling
point but is not comparable with the paper's series (women 20–39, married vs
cohabiting, 5-year bands), which waits for the EIC microdata (§VII, Nov 2026).

## Why it is a watch item and not a model input

- The single-sex skeleton behind the scenario graphs cannot represent sex
  composition; the two-sex effect enters only through the Q4 skeleton's age-sex
  migration profile, which Anne has made binding for the TDR, not for coupling.
- The emigration driver is exogenous (US policy), so the sex-ratio shock is not
  persistent structure; its persistence rides with the migration taper ruling.
- The EIC cannot capture households that emigrated entirely, so both the outflow
  and its sex skew are lower bounds.

## What would move it

- EIC 2025 microdata: sex ratio of the resident population at 20–29 by union
  status, against CPV 2020.
- The collapse paper's coupling series once the 20–39 cut is available.
- Any evidence that the Goldin gender-mismatch mechanism (watch item of
  2026-09-15) and the sex-ratio mechanism interact rather than add.

## Cross-references

- → Origin record: `_pending/2026-09-23_EIC-rebased-scenarios_Anne-record.md` §3.3
- → EIC 2025 entry (emigration and union-status figures): `releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md`
- → Working graphs (migration profile as implemented, single-sex): `country/MEX/mex_scenarios_eic2025.md`
- → Rival mechanism on file: `watch_items/2026-09-15_goldin-gender-mismatch-stress-floor.md`
- → Collapse paper workspace: `GrandPlan/DFD/research/fertility_collapse_abm/`

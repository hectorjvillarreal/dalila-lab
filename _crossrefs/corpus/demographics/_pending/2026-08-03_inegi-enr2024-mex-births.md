---
type: corpus_entry
tier: data_source
project_scope: [DFD, BDH]
authors: [INEGI]
year: 2025
title: "Estadística de Nacimientos Registrados (ENR) 2024 — cifras definitivas"
venue: "INEGI, Comunicado de prensa 129/25 (25 septiembre 2025); Reporte de Resultados 34/25"
doi: "https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enr/enr2024_CP.pdf"
date_added: 2026-08-03
added_by: Claude Code
endorsed_by:                          # blank until Anne endorses
build_instruction: "_crossrefs/_build_instructions/2026-08-03_demographics_mex_enr2024_update.md"

indicators: [cbr]
geography: [MEX]
scenario_implication: fast-transition
source_reliability: primary
data_vintage: 2024
workflow_status: pending-endorsement
---

# INEGI ENR 2024 (definitive) — Mexico registered births fall 8.2%, below the Rule-of-85 trigger

## One-line summary

Mexico registered **1,672,227 births in 2024** (definitive), an 8.2% drop
from 2023 that breaches the Q2 replicate's 1.7 M sensitivity trigger and
pulls the Rule-of-85 long-run stationary population down to ~125 M.

## Core content

INEGI's definitive ENR 2024 (Comunicado 129/25, 25 September 2025) counts
1,672,227 registered births, versus 1,820,888 in 2023 (−8.2%). The rate per
1,000 women of fertile age (15–49) fell from 52.2 to 47.7 (−4.5), resuming
the pre-pandemic downtrend after the 2021–2022 registration rebound; the
full series 2015→2024 is 2,353,596 → 1,672,227 (−29% in nine years). The
release does **not** retabulate the tasa global de fecundidad — confirming
the standing note in `scenario_anchors.md` — so the MEX TFR anchor remains
1.60 (ENADID 2023). State dispersion remains wide: Chiapas 86.7 vs. Ciudad
de México 32.8 per 1,000 women 15–49.

**Registration-basis caveats (load-bearing for any ASFR use).** (i) These
are registered, not occurred, births: 82.0% were registered before age one,
but 7.2% of 2024 registrations were of persons aged 6+; the occurred-in-2024
count will differ and later vintages will revise it. INEGI's own footnote
says natality analysis requires nacimientos ocurridos. The basis is however
consistent with the 1.82 M (2023) figure the Q2 replicate used, so the −8.2%
year-over-year comparison is like-for-like. (ii) Mother's age is
"no especificado" for 11.69% of records — any ASFR shape refit from ENR
microdata must handle this mass explicitly.

## Project calibration implications

**DFD.**

- **Rule-of-85 trigger fired.** Q2 replicate §10: births below 1.7 M
  (>7% drop) move the long-run stationary population into the 120–135 M
  range. Observed: 1.672 M, −8.2%. Recomputed long-run anchor:
  **125.4 M at e₀ = 75; 133.8 M at e₀ = 80** — versus 136.5 M at the 2023
  births anchor and versus the Central-scenario (TFR = 1.50) 2050 projection
  of 140.4 M. The stationary anchor now sits **materially below** the 2050
  cohort-component path, implying a steeper post-2050 decline and more
  transitional inertia in the 2050 state than the Q2 baseline suggested.
- **Fast-transition classification.** An 8.2% single-year births drop with
  no TGF recovery signal strengthens the fast-transition case for the MEX
  central scenario (TFR = 1.50 stable) and argues against promotion of the
  tempo-corrected column (Q2 §6 promotion conditions are not met — this is
  evidence in the opposite direction).
- **Q3 replicate input.** This entry supplies follow-up item 4 of the Q2
  list (SINAC/ENR 2024 births refresh). The Q3 replicate (overdue; target
  was 2026-07-15) should use 1.672 M as the births anchor and rerun §10.

**BDH.** Directional only: a births contraction of this size accelerates the
age-structure shift feeding old-age health-expenditure shares, but the
effect enters through the same dependency-ratio path the Q3 replicate will
recompute. No standalone BDH calibration change asserted here.

## Comparator note (secondary, for context)

Press coverage of CONAPO's mid-2026 projections reports ~1.996 M projected
births for 2026 and a TGF of ~1.9 for 2025 — roughly 19% above the observed
2024 registered-births level on the births margin. Consistent with the
standing principle that official medium variants (CONAPO, CELADE, WPP) are
optimistic for Mexico. CONAPO primary tables not yet read; routed to the
acquisition queue as Tier-2.

## Open questions surfaced

- Mexico 2024/2025 TGF: still no INEGI retabulation or ENADID successor;
  the anchor row stays at 1.60 (2023). Watch for an ENADID 2028 cycle or a
  CONAPO conciliación update with an observed-series TGF.
- CELADE OD 2025 Excel MEX comparator: still pending extraction (carried
  since Q2; needed to close the optimism-gap retrospective).
- Occurred-vs-registered wedge for 2024: check the ENR interactive tabulados
  (nacimientos ocurridos by year of occurrence) when the Q3 replicate runs.

## Citation

INEGI (2025). *Estadística de Nacimientos Registrados (ENR) 2024.*
Comunicado de prensa núm. 129/25, 25 de septiembre de 2025; Reporte de
resultados núm. 34/25. Aguascalientes: Instituto Nacional de Estadística y
Geografía.

## Cross-references

- → Build instruction: `_crossrefs/_build_instructions/2026-08-03_demographics_mex_enr2024_update.md`
- → Scenario anchors (MEX row unchanged): `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Q2 baseline replicate (trigger origin, §10): `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q2_demographic_replicate.md`
- → Standing reference: Fernández-Villaverde (2026), "The Demographic Future of Humanity" (Rule-of-85 framing)
- → Project corpus cross-refs (append on endorsement, per §Routing):
    - DFD: `GrandPlan/DFD/docs/corpus/_cross_references.md`
    - BDH: `GrandPlan/BDH/docs/corpus/_cross_references.md`

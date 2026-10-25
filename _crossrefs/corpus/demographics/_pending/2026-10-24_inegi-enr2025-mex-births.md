---
type: corpus_entry
tier: data_source
project_scope: [DFD, BDH]
authors: [INEGI]
year: 2026
title: "Estadística de Nacimientos Registrados (ENR) 2025"
venue: "INEGI, Comunicado de prensa 87/26 (25 septiembre 2026); Reporte de Resultados 38/26"
doi: "https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/enr/ENR2025_CP.pdf"
date_added: 2026-10-24
added_by: Claude Code
endorsed_by:
build_instruction: "_crossrefs/_build_instructions/2026-10-24_demographics_mex_enr2025_update.md"

indicators: [cbr]
geography: [MEX]
scenario_implication: neutral
source_reliability: primary
data_vintage: 2025
workflow_status: pending-endorsement
---

# INEGI ENR 2025 — registered births flat (+0.4%), occurred births still falling

## One-line summary

Mexico registered **1,678,532 births in 2025** (+6,305, +0.4% on 2024's
1,672,227; rate unchanged at 47.7 per 1,000 women 15–49), but the flat
headline is a late-registration effect: births registered in the year they
occurred fell **−2.6%** (1,086,087 → 1,058,332), and registrations of people
born before 2016 jumped by ~59 k.

## Core content

The release's own Table 1 (RR 38/26 p. 4; transcribed to
`sources/INEGI_2026-09-25_ENR2025_RR-38-26_tabla1.csv`, row sums verified)
cross-tabulates registration year against year of occurrence for 2016–2025.
It separates the two things the headline mixes:

| Registrations in year | 2023 | 2024 | 2025 | 2025 vs 2024 |
|---|---|---|---|---|
| Total registered (headline) | 1,820,888 | 1,672,227 | 1,678,532 | +0.4% |
| of which born same year | 1,157,443 | 1,086,087 | 1,058,332 | **−2.6%** |
| of which born 2016 or later | 1,719,011 | 1,568,594 | 1,515,456 | −3.4% |
| of which born before 2016 (residual) | 101,877 | 103,633 | 163,076 | **+57%** |

By year of occurrence, births registered within two years fell −6.4% (2023)
and −6.7% (2024). Same-year registrations, the only margin available for 2025,
fell −6.2% (2024) and −2.6% (2025). **The decline continues on the occurrence
basis but slowed in 2025.** The rest of the RR agrees on the late-registration
reading. Registered before age one: 78.5% (82.0% in 2024). Aged 6+ at
registration: 11.3% (7.2%). Mother's age "no especificado": 15.4% (11.69%).
INEGI's footnote again says natality analysis needs nacimientos ocurridos. The
release has no TGF.

Why the pre-2016 registrations jumped is **not established**. One hypothesis
to check, not asserted: an adult late-registration push tied to the 2025 CURP
reforms or state registration campaigns. RR annex Table 3 (state × year of
occurrence) would show whether the jump is concentrated in a few states.

## Project calibration implications

**DFD.**

- **Q3 proxy method should not be rolled forward.** The Q3 replicate's 2024
  TFR proxy (≈1.46 = 1.60 × 47.7/52.2) scales the anchor by the crude
  *registered* rate. Repeated mechanically for 2025 it gives ≈1.46 again,
  because the rate is flat. That would read as a plateau the occurrence data
  do not show. Measured on births by year of occurrence, 2024 fell ~6.7%
  rather than 8.2%, so on that basis the 2024 proxy sits slightly *higher*
  (crudely ≈1.49 before any denominator change). The 2025 occurrence data
  point down again. Recommendation for the Q4 reconciliation: build the
  registry proxy on births by year of occurrence (same-year plus a completion
  factor taken from Table 1), not on the headline rate. Anne rules on the
  method.
- **Rule-of-85 anchor: the registration basis matters (flag only, nothing
  re-pinned).** A year's registrations have run 5–13% above that year's
  occurred births in every year since 2016 (2016: 2.29 M vs 2.18 M; 2022:
  1.89 M vs 1.67 M occurred to date).
  Mechanically, 2025 registered births give 125.9 M at e₀ = 75 (134.3 M at
  e₀ = 80), essentially the endorsed 2024 anchor (125.4 / 133.8 M).
  *Illustrative only, not for citation:* completing 2024 occurred births from
  Table 1 tail ratios (+5.6% to +7.7% beyond two years) gives ≈1.46–1.49 M.
  The stationary population would then be ≈109–112 M at e₀ = 75
  (≈117–119 M at e₀ = 80). The endorsed ENR 2024 entry and the Q3 replicate
  are **not amended** (PROTO §5). Whether the anchor moves to the occurrence
  basis is Anne's call at Q4.
- **Scenario positioning unchanged.** Same-year −2.6% is consistent with the
  existing bracket (Central 1.50 upper / EIC-direct 1.23 lower). It neither
  supports the tempo-corrected column nor needs a new row. `scenario_anchors.md`
  is untouched.
- **Q4 replicate input.** This entry supplies the 2025 births point. The Q4
  births series should be the occurrence matrix, not the headline column.

**BDH.** Directional only. Continued occurrence-basis decline keeps the
age-structure shift on the path already in the EIC-rebased scenarios. No
standalone BDH calibration change is asserted.

## Open questions surfaced

- **For Anne:** registry proxy and Rule-of-85 on occurred births rather than
  registered: adopt at Q4, or keep registered for continuity with the
  endorsed series?
- Source of the +59 k pre-2016 registrations (RR annex Table 3, state
  breakdown; check whether 2025 had a CURP- or campaign-driven adult push).
- Completion factor for recent cohorts: the tail ratio is shrinking (same-year
  share rising). The 2016–18 near-complete cohorts (+7.5–7.7%) may overstate
  completion for 2024–25.
- ENR still carries no TGF. The MEX anchor row stays as in `scenario_anchors.md`.
  The EIC 2025 TGF 1.23 (2024) remains the only recent INEGI fertility rate.

## Citation

INEGI (2026). *Estadística de Nacimientos Registrados (ENR) 2025.*
Comunicado de prensa núm. 87/26, 25 de septiembre de 2026; Reporte de
resultados núm. 38/26. Aguascalientes: Instituto Nacional de Estadística y
Geografía.

## Cross-references

- → Build instruction: `_crossrefs/_build_instructions/2026-10-24_demographics_mex_enr2025_update.md`
- → Sources: `sources/INEGI_2026-09-25_ENR2025_CP-87-26.pdf` (sha256 `53859a85…6e18`), `sources/INEGI_2026-09-25_ENR2025_RR-38-26.pdf` (sha256 `fb536335…3f82`), Table 1 transcription `sources/INEGI_2026-09-25_ENR2025_RR-38-26_tabla1.csv`
- → Predecessor (endorsed, not amended): `releases/2026-08-03_inegi-enr2024-mex-births.md`
- → Q3 replicate (proxy method, §2): `country/MEX/quarterly/2026-Q3_demographic_replicate.md`
- → EIC 2025 trigger entry: `releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md`
- → MEX instructions (v1.7 queue, Q4): `country/MEX/DFD_TFR_forecast_instructions.md`
- → Project corpus cross-refs (append on endorsement, per §Routing):
    - DFD: `GrandPlan/DFD/docs/corpus/_cross_references.md`
    - BDH: `GrandPlan/BDH/docs/corpus/_cross_references.md`

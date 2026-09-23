---
type: working_note
title: "Mexico demographic scenarios 2025–2050 re-based on the Encuesta Intercensal 2025 — four graphs under updated assumptions"
date: 2026-09-23
added_by: Claude
endorsed_by:
projects: [DFD, BDH]
indicators: [tfr, population, dependency_ratio, migration, mortality]
geography: [MEX]
workflow_status: pending-anne
companion_of: mex_scenarios_eic2025.py
governing_instructions: DFD_TFR_forecast_instructions.md v1.5
related: "../../releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md; quarterly/2026-Q3_demographic_replicate.md"
---

## What this is

A working set of scenario graphs produced the day after the EIC 2025 release, at
Héctor's request, "under reasonable assumptions". It is **not** a quarterly
replicate and does **not** amend the endorsed Q2/Q3 replicates. Its purpose is to
show what the five-row scenario structure looks like once the base year is the
observed 2025 age structure and the skeleton carries mortality improvement and the
emigration the EIC measured. Every difference from the endorsed reference values
is explained below so Anne can rule on which changes to carry into Q4.

Outputs, all in this folder:

| File | Content |
|---|---|
| `mex_scenarios_eic2025_tfr.png` | five TFR paths 2025–2050 against the observed readings (2019, 2023, three for 2024/25) |
| `mex_scenarios_eic2025_population.png` | total population by scenario, WPP 2024 medium as reference, EIC 2025 point |
| `mex_scenarios_eic2025_dependency.png` | TDR / YDR / OADR by scenario, TDR minimum marked, EIC and CONAPO-share points |
| `mex_scenarios_eic2025_structure.png` | age structure 2025 observed vs 2050 under Central, EIC-direct, Stress |
| `mex_scenarios_eic2025_results.csv` | every series, main assumptions and the sensitivity |

## Assumptions

| Item | This run | Endorsed skeleton (Q2/Q3) | Basis |
|---|---|---|---|
| Base year and structure | **2025, EIC tabulado age-band shares on 130.91 M**; 75+ split with WPP-2023 within-75+ proportions | 2023, WPP 2024 via OWID | source hierarchy (intercensal > WPP); Q4 "retabulate current structure" item |
| Optimistic TFR | UN WPP 2024 medium path itself (1.87 → 1.79 (2030) → 1.70 (2050)) | 1.65 stable approximation | removes an approximation |
| Tempo-corrected | 1.60 stable | same | v1.5 |
| Central | 1.50 stable from 2025 | 1.50 stable | v1.5 |
| **EIC-2025 direct** | **1.23 stable from 2025** | not present | proposed fifth row (entry of 2026-09-22); **pending Héctor's ratification** |
| Stress | 1.50 (2025) → −0.10/yr → 0.90 from 2031 | same | v1.5; origin question open (see below) |
| Mortality | five-year death probabilities fall 1.0 %/yr from CD-West e0≈75 (crude e0 73.5 → 77.0) | fixed | conventional improvement rate; direction of WPP 75.1 → 79.8 |
| Net migration | **−230 k/yr**, ages 15–44 (profile peaked 20–29), constant to 2050 | zero | EIC 2020–25: 1.3 M emigrants, 150.8 k returns; entry records it as a lower bound |
| Sex | single-sex, female share 0.5, SRB 1.05 | same | skeleton |
| ASFR shape | Mexico shape, fixed | same | skeleton |
| Steps | 2025, 2030, …, 2050 | 2023, 2028, …, 2048, 2050 | clean five-year grid from the EIC reference date |

Run `python mex_scenarios_eic2025.py --no-migration` to switch migration off; the
script always prints the fixed-mortality, zero-migration sensitivity alongside.

## Results (main assumptions)

| Scenario | Pop 2050 (M) | TDR min | Year | Grid window | Interpolated window | TDR 2050 | OADR 2050 |
|---|---|---|---|---|---|---|---|
| Optimistic (WPP path) | 137.4 | 45.7 | 2030 | 2025–2035 | 2025–2035 | 58.5 | 31.8 |
| Tempo-corrected 1.60 | 133.8 | 44.6 | 2030 | 2025–2035 | 2025–2036 | 57.7 | 32.5 |
| **Central 1.50** | **131.5** | **43.8** | **2035** | **2030–2035** | **2027–2037** | 56.7 | 32.8 |
| EIC-direct 1.23 | 125.2 | 41.0 | 2035 | 2030–2035 | 2030–2038 | 54.0 | 33.9 |
| Stress → 0.90 | 119.1 | 39.1 | 2035 | 2035–2040 | 2032–2040 | 49.6 | 34.6 |

Sensitivity, fixed mortality and zero migration on the same EIC base:

| Scenario | Pop 2050 (M) | TDR min | Year | TDR 2050 | OADR 2050 |
|---|---|---|---|---|---|
| Optimistic | 141.7 | 45.1 | 2030 | 54.2 | 27.5 |
| Tempo-corrected | 138.0 | 43.7 | 2035 | 53.3 | 28.0 |
| Central | 135.6 | 42.7 | 2035 | 52.2 | 28.3 |
| EIC-direct | 129.1 | 39.9 | 2035 | 49.3 | 29.2 |
| Stress | 122.7 | 38.0 | 2035 | 44.8 | 29.8 |

Window convention: grid = table years within +2.0 of the minimum on the five-year
grid; interpolated = annual linear interpolation of the same threshold (v1.4
footnote). Both are stated because the two differ.

## Why the numbers moved, and what each move means

**1. The base is the biggest single change, and it is evidence, not assumption.**
The endorsed Central 2050 population is 140.4 M on the WPP-2023 base. On the EIC
2025 base with the old skeleton it is 135.6 M. The reason is the age structure
itself, which is the Q3 §4 wedge resolved in the direction Anne read from the
EIC TDR:

| Share of population | WPP 2024 (2023) | EIC 2025 |
|---|---|---|
| 0–14 | 24.9 % | 21.6 % |
| 15–64 | 67.1 % | 68.3 % |
| 65+ | 8.0 % | 10.1 % |
| TDR | 49.0 | 46.4 |

The EIC has about 3.4 M fewer children and 2.6 M more people aged 65+ than WPP
implied. Fewer children in 2025 means fewer mothers in the 2040s, which is why
every scenario loses population against the endorsed figures even at the same TFR.
The reproduction of the tabulado's 46.40 by the model's base structure is the
sanity check that the re-base is faithful.

**2. The fiscal window comes earlier and is already open.** With the youth share
lower than the projection assumed, the TDR minimum is reached around 2030–2035
rather than ~2038, and the interpolated Central window runs roughly 2027–2037.
The endorsed IM-6 anchor of 2033–2038 still sits inside the Central window under
the interpolated convention but is at its *end*, not its middle. This is the
material implication for IM-6 and must go to Cath with the Q4 retabulation; it
should not be cited before that.

**3. Migration and mortality roughly cancel on population and compound on
aging.** Net emigration of −230 k/yr removes about 5.8 M by 2050; mortality
improvement adds about 1.6 M. On the dependency side both push the same way:
emigrants leave from the working-age denominator, and survivors accumulate in the
65+ numerator, so OADR in 2050 is 4–5 points higher than in the sensitivity. The
2050 TDR of the Central scenario is 56.7 against 52.2 without them.

**4. The Optimistic row does not reproduce WPP's own population.** Using WPP's
TFR path gives 137.4 M in 2050 against WPP's 148.95 M. The gap is the EIC base
(WPP starts higher and younger), the emigration WPP does not assume at this
scale, and WPP's stronger mortality gains. The earlier skeleton had the same
gap at 4.4 M; it is now 11.5 M because the base and migration assumptions
diverge from WPP by construction. The row still serves its purpose as the upper
bracket of the fertility assumption on a common base.

**5. The Stress origin problem is now visible on the chart.** Central and Stress
depart from 1.50 in 2025 while the three 2024/25 observations sit at 1.23, 1.46
and 1.51. Anne transferred the origin question to the Q4 reconciliation on
2026-09-23; these graphs follow v1.5 as written. If the reconciled 2024 value is
1.3–1.4, the Central row is already an upper bracket in level as well as in
scenario logic.

## Caveats

- The skeleton is coarse: single-sex, fixed ASFR shape, CD-West survival, and a
  five-year grid. It is fit for scenario comparison on a common base, not for
  levels against WPP.
- The migration profile and constancy to 2050 are assumptions; the EIC flow is a
  lower bound and 70 % male, which the single-sex model cannot represent.
- The 75+ split borrows WPP-2023 proportions; it affects the OADR level by well
  under a point.
- Nothing here is endorsed. Reference values for citation remain those of the Q3
  replicate and the v1.5 instructions until Anne and Cath rule.

## For Anne

1. Whether the EIC 2025 base should replace the WPP-2023 base in the Q4 replicate
   (recommended: yes, it is the source hierarchy applied).
2. Whether mortality improvement and observed net emigration enter the operational
   skeleton or stay as sensitivities.
3. The fifth-row specification if Héctor ratifies it.
4. Routing of item 2 above (window timing) to Cath.

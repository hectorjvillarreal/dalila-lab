---
type: read_memo
stage: 3a
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led) → modeling seam (Nina)"
title: "Stage 3a — the read: sufficiency of the no-reflexivity mechanism (cohort-entry heterogeneity + exogenous period shock)"
target: Nina (ABM lead); Anne informed (demographic verdicts are INPUTS here, not re-litigated)
date_added: 2026-07-11
added_by: Claude
endorsed_by:                       # pending Nina (build + read); Anne only if the read touches the demographic verdict
depends_on:
  - "STAGE3a_sufficiency_instruction.md (Debb, 2026-07-11)"
  - "STAGE2b_compositional_cascade_memo.md + Anne sign-off (no-cascade; cohort-replacement)"
  - "STAGE2c_col_individual_memo.md + Anne sign-off (aggregation-cleared)"
  - "STAGE2_calibration_results.md (the skeleton this respecifies)"
build_artifacts:
  - "stage3a_norefl_abm.jl · calibrate_3a.jl · make_figures_3a.jl · _render_figures_3a.py"
  - "outputs/stage3a/ (calibration, metrics, ablations, figures, _assert_no_tfr.log)"
status: "Calibrated run complete (50k x 16 finals, both countries). §4 rule applied below. Pending Nina's endorsement."
---

# Stage 3a — The Read

**Question (instruction §1):** can a no-reflexivity model — cohort-entry heterogeneity +
an exogenous period shock — reproduce the observed marriage-share (composition) collapse
in CR and COL: its magnitude and its 2015–2024 shape, including the late acceleration?

**All numbers below are from `outputs/stage3a/` (final confirmation ensembles, 50,000
agents × 16 seeds); none invented. Metrics M1–M3 were pre-registered in `calibrate_3a.jl`
before the full run.** TFR appears nowhere in any loss (11/11 wall checks PASS per country,
`_assert_no_tfr.log`).

## Headline

**Sufficiency is ESTABLISHED on the pre-registered gate (M1 magnitude + M2 late-share),
in both countries.** The surviving structure from 2b/2c — cohort replacement with a
calibrated across-cohort marriage-propensity decline, plus a small exogenous calendar-time
shifter — reproduces the observed composition collapse at ~97–104% of magnitude and matches
the late-loading of the decline within 4 points. This is §4 row 1: *the paper's model
matches the empirical verdict.* One second-order feature fails in COL (M3, curvature sign)
and is reported as the residual routed to ENDS — see §4 below.

The no-reflexivity fit is also **better than the Stage 2 threshold skeleton on the
skeleton's own target** (CRI N1 loss 0.0351 vs 0.0855): removing the rejected coordination
threshold and adding the 2b-identified structure *improved* the composition fit while
staying inside the empirical verdict.

## 1. The pre-registered metrics

| metric (married, 20–39 equal-band) | CRI | COL | criterion | verdict |
|---|---|---|---|---|
| **M1** magnitude capture (seed→2024 fall) | **0.975** | **1.044** | ≥ 0.85 | **PASS · PASS** |
| **M2** late-window share of decline (2017→24), sim vs obs | 0.544 vs 0.581 | 0.490 vs 0.459 | \|diff\| ≤ 0.10 | **PASS · PASS** (Δ = 0.038 · 0.031) |
| **M3** acceleration sign, mean Δ² 2015–24 | +0.00002 vs +0.0019 | +0.00009 vs **−0.00035** | same sign | PASS · **FAIL** |
| cohab magnitude capture (reported, not gated) | 1.029 | 1.646 | — | reported |
| N1 composition loss (final) | 0.0351 | 0.0266 | — | (skeleton: 0.0855) |

Observed equal-band married falls: CRI 0.324 → 0.166 (2010–24); COL 0.215 → 0.119 (2008–24).

Two honest notes on the table:
- **COL M3.** Both second differences are near zero, but the observed sign is negative
  (steepening) and the sim's is not. The visible driver in the band data is the 2019–22
  kink — married and cohabiting both break trend around the pandemic years (GEIH mode/frame
  effects are plausible contributors) — which no smooth cohort+period mechanism reproduces.
  This is the instruction's §4 row-2 phenomenon confined to the *second-order* feature:
  level and late-loading are captured, residual within-window curvature is not. It routes
  to ENDS (sub-annual/individual transitions), exactly as the instruction anticipated.
- **COL cohab overshoot (1.65).** The observed cohab *net* rise 2008–24 is small (+0.031)
  because it rises to 2020 then falls; the sim's smooth path overshoots the small net
  change while tracking the level well (fig 1). Reported, not gated; same 2019–22 kink.

## 2. Calibrated mechanism (per country, 12 free params, N1 composition-only loss)

| | CRI | COL |
|---|---|---|
| κ(b) floor / midpoint / steepness | 0.356 / **1990.1** / 0.153 | 0.311 / **1988.1** / 0.173 |
| φ(b) formation tilt (per birth-yr) | 0.027 | 0.018 |
| π(t) depth / midpoint / steepness | 0.153 / 2019.0 / 0.77 | 0.186 / 2021.4 / 0.94 |
| base marry-share-of-formation | 0.327 | 0.173 |

**Cohort-gradient fit (fig 2):** the calibrated κ(b) inflects at birth cohorts ~1988–1990
in both countries — the same crossover the 2b APC married cohort effects show (COL effects
flip sign between the 1985 and 1990 bins). The gradient was *calibrated to composition
trajectories only*; its agreement with the independently-estimated APC timing is a genuine
convergence check, not a fit.

**Period-shock estimate:** shallow late-onset shifters (≤ 19% depth), CRI onset ~2019,
COL ~2021. See the ablation — neither country actually *needs* it for the band-level fit.

## 3. Mechanism decomposition (ablations, full recalibration per cell)

| N1 loss | full model | no period (cohort only) | no cohort (period only) |
|---|---|---|---|
| CRI | 0.0351 | 0.0372 (+6%) | 0.0405 (+15%) |
| COL | 0.0266 | **0.0246 (−7%)** | **0.0433 (+63%)** |

- **CRI:** the period shock is dispensable (+6% loss when pinned to zero; all gated metrics
  still pass). This *resolves* the apparent tension in §2: the full calibration kept
  d_p = 0.15, but the ablation shows it carries almost nothing — consistent with 2b's CRI
  verdict (period effect not statistically present).
- **COL:** removing the *cohort* gradient costs 63%; removing the *period* shock costs
  nothing (the pinned run even lands a slightly better basin — lower search dimension).
  The loss landscape independently reproduces the 2b ordering: **COL is cohort-dominant.**
  The 2b COL period component (cell-level, p≈3e-6) is evidently absorbable at band level
  by formation tilt + cohort turnover; it is NOT needed as a separate band-level driver.
- **Caveat (limits of 3a identification):** the no-cohort runs still pass M1/M2 — four
  bands × annual shares cannot by themselves discriminate the mechanism. That is fine and
  by design: **3a answers sufficiency; identification of the structure rests on 2b/2c**
  (Anne's verdicts are inputs). We report this rather than claim discrimination we don't have.

## 4. §4 decision rule, applied

> Row 1 — "Model reproduces observed composition magnitude AND the late acceleration."

**Applied verdict: Row 1, both countries, on the pre-registered gate (M1 & M2).**
Sufficiency of the no-reflexivity structure is established: cohort-replacement + (optional)
exogenous period shifter is enough for the composition collapse's magnitude and its
late-loaded tempo. The COL M3 curvature-sign miss is the surviving row-2 residual —
*"the acceleration may live below the annual/cell resolution"* — now narrowed to the
second-order term around 2019–22, and it routes to ENDS (2c-ii) without weakening the
row-1 read on the gated metrics. Reflexivity was neither present nor needed — and per the
instruction §7, this outcome does **not** reopen (B) in either direction; only ENDS can.

## 5. Data decision of record (COL seed year)

The instruction says "COL (GEIH 2007–2024)". The first full run seeded 2007 and produced
degenerate metrics (M1 = 1.38, M2 late-share = −2.3) because the observed 2007→2024
married "fall" is *negative*: `COL_coupling_annual.md` documents **2007 as a frame/
questionnaire outlier** ("union 47.5% vs the 2008–2020 plateau ~59–60%; treat the plateau
as 2008–2020"). The build was corrected to **seed COL at 2008**, dropping the artifact year
from both the seed and the loss, per the documented Stage 1.5 caveat — a data-provenance
decision, not an outcome-driven one. The superseded 2007-seed run is archived intact in
`outputs/stage3a/_superseded_col2007seed/` for audit.

## 6. Discipline verification

- **Identification wall:** `_assert_no_tfr.log` — 11 PASS / 0 VIOLATION per country
  (static checks on loss/free-params/transition rules + runtime file-load registry:
  only the coupling CSV is opened during calibration). TFR overlay loaded strictly after.
- **No reflexivity:** checked in code, not prose — `agent_step!` contains no cross-agent
  read (`allagents`/`nearby_agents` absent), `model_step!` advances the calendar only, and
  the four skeleton feedback identifiers are absent from the 3a model source.
- **Reproducibility:** the CRI calibration re-run end-to-end reproduced the best loss to
  all printed digits (0.035104) — the pipeline is deterministic given seeds.
- **w:** fixed at 0.6 for the overlay only; composition dynamics are w-invariant by
  construction (Stage 2 finding). No w sweep in 3a; `w`/fertility intensity stays gated
  to ENDS (3b).
- **Overlay TFR (comparison only, placeholder MEX-shape ASFR):** CRI 1.24 → 0.90 generated
  vs 1.83 → 1.12 observed; COL 1.23 → 1.06 vs 1.7 → 1.1 (sparse). Level and magnitude are
  NOT claims — 3a targets composition; TFR-magnitude sufficiency is Stage 3b, ENDS-gated.

## 7. Limitations

- **Band-level power.** As §3 notes, the composition target alone cannot discriminate
  cohort-vs-period structure; 3a leans on 2b/2c for identification, by design.
- **2019–22 kink.** The one shape feature outside the model's reach; partially confounded
  with GEIH pandemic-era collection (COL) — flag for Anne, do not over-interpret.
- **Placeholder backgrounds and tails.** Edu/loc shares, 15–19 and 40–49 seeding tails,
  and the parity seed remain the skeleton's provisional values (never tuned to any target).
- **Closed cohort.** Stationary age structure carried from the skeleton; composition
  *shares* are robust to this, levels of counts are not (and are not used).
- **External validity.** Two high-cohabitation regimes; ARG/CHL remain the data-gated
  external-validity thread (channel-absent prediction untouched by 3a).

## 8. Deliverables produced

`stage3a_norefl_abm.jl` (model) · `calibrate_3a.jl` (calibration + pre-registered metrics +
wall checks + ablation pins) · `make_figures_3a.jl` + `_render_figures_3a.py` (figures) ·
`outputs/stage3a/`: calibration bests + traces (baseline and both ablations),
`sufficiency_metrics{,_noperiod,_nocohort}.csv`, per-band trajectories, mechanism profiles
(κ, φ, π), TFR overlays, `figures/fig1–fig4`, `_assert_no_tfr.log`, superseded-run archive.
Run logs: `_stage3a_full.log`, `_stage3a_col_rerun.log`, `_stage3a_cri_trace_regen.log`,
`_stage3a_ablation_{noperiod,nocohort}.log`.

**Gate (instruction §7):** Nina endorses the build and this read → feeds the paper's model
section (Fina's M2/M4). (B) stays deferred regardless — only ENDS can reopen it.

*Stage 3a read. Claude, 2026-07-11, on the Debb build instruction carrying Anne's verdicts.
Pending Nina's endorsement.*

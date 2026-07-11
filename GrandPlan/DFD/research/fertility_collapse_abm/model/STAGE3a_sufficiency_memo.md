---
type: read_memo
stage: 3a
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led) → modeling seam (Nina)"
title: "Stage 3a — the read: sufficiency of the no-reflexivity mechanism (cohort-entry heterogeneity + exogenous period shock)"
target: Nina (ABM lead); Anne informed (demographic verdicts are INPUTS here, not re-litigated)
date_added: 2026-07-11
added_by: Claude
endorsed_by: "Nina (build + read, 2026-07-11 — STAGE3a_Nina_signoff.md, five conditions APPLIED in this revision); Anne (COL 2008-seed decision, §5 — confirmed 2026-07-11 via Héctor)"
depends_on:
  - "STAGE3a_sufficiency_instruction.md (Debb, 2026-07-11)"
  - "STAGE3a_Nina_signoff.md (gate adjudication; conditions 1-5)"
  - "STAGE2b_compositional_cascade_memo.md + Anne sign-off (no-cascade; cohort-replacement)"
  - "STAGE2c_col_individual_memo.md + Anne sign-off (aggregation-cleared)"
  - "STAGE2_calibration_results.md (the skeleton this respecifies)"
build_artifacts:
  - "stage3a_norefl_abm.jl · calibrate_3a.jl · stage3a_nina_conditions.jl · make_figures_3a.jl · _render_figures_3a.py"
  - "outputs/stage3a/ (calibration, metrics, ablations, kphi_separability.csv, figures, _assert_no_tfr.log)"
status: "ENDORSED — Nina (build + read) + Anne (§5 seed decision). HEADLINE SPEC = COHORT-ONLY (condition 3). §4 rule applied. Feeds Fina M2/M4."
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

**Sufficiency on magnitude and late-loading, with one unreproduced shape residual
(COL M3), in both countries — on the pre-registered gates, under the COHORT-ONLY
headline specification** (Nina condition 3: the period shifter is demoted to a
documented robustness term; see §3).

Per Nina's gate, the credibility of this result does **not** rest on magnitude capture —
a model handed three mechanisms *should* fit a level; that is table stakes. It rests on
three convergences with Stage 2b that the model was **never fit to**:

1. **The cohort gradient κ(b) recovers the 2b APC crossover it never saw.** κ(b) is a
   **three-parameter logistic in birth cohort** (floor, midpoint, steepness — the full
   functional form; there are no per-cohort free effects). Calibrated only to composition
   trajectories, its midpoint lands at birth cohorts **1991.7 (CRI) / 1988.8 (COL)** —
   the same 1985–1992 window where the independently-estimated 2b APC married cohort
   effects cross zero. One recovered parameter, not a fitted profile: the convergence is
   non-circular (condition 1).
2. **The ablation decomposition reproduces the 2b ordering** (COL cohort term essential,
   +63% loss without it; period dispensable in both countries — §3).
3. **The no-reflexivity model beats the rejected threshold skeleton on the skeleton's own
   composition target** (CRI N1 loss 0.037 cohort-only / 0.035 full vs the skeleton's 0.0855).

This is mechanism validation, not curve-fitting. The one shape feature outside the model —
COL's 2019–22 curvature (M3) — is reported prominently in §4 and routes to ENDS.

## 1. The pre-registered metrics

**Headline specification — COHORT-ONLY** (period pinned to zero; independent full
recalibration, not a post-hoc restriction):

| metric (married, 20–39 equal-band) | CRI | COL | criterion | verdict |
|---|---|---|---|---|
| **M1** magnitude capture (seed→2024 fall) | **0.954** | **0.999** | ≥ 0.85 | **PASS · PASS** |
| **M2** late-window share of decline (2017→24), sim vs obs | 0.490 vs 0.581 | 0.468 vs 0.459 | \|diff\| ≤ 0.10 | **PASS · PASS** (Δ = 0.091 · 0.010) |
| **M3** acceleration sign, mean Δ² 2015–24 | +0.0003 vs +0.0019 | +0.0003 vs **−0.00035** | same sign | PASS · **FAIL** |
| cohab magnitude capture (reported, not gated) | 0.626 | 1.726 | — | reported |
| N1 composition loss (final) | 0.0372 | 0.0246 | — | (skeleton: 0.0855) |

Robustness — full 12-parameter model (cohort + period): M1 0.975 / 1.044; M2 Δ 0.038 /
0.031; M3 PASS / FAIL; losses 0.0351 / 0.0266. Same gate outcomes on every gated metric.

Honest margins under the headline spec: **CRI's M2 sits nearer the tolerance edge**
(Δ = 0.091 vs 0.038 with the period term) and **CRI's ungated cohab capture drops to 0.63**
(from 1.03) — in CRI the period shifter was mostly absorbing the cohab margin. Neither
changes a gate outcome; both are stated rather than smoothed over.

Observed equal-band married falls: CRI 0.324 → 0.166 (2010–24); COL 0.215 → 0.119 (2008–24).

Two honest notes on the table:
- **COL M3.** Both second differences are near zero, but the observed sign is negative
  (steepening) and the sim's is not. The visible driver in the band data is the 2019–22
  kink — married and cohabiting both break trend around the pandemic years (GEIH mode/frame
  effects are plausible contributors) — which no smooth cohort+period mechanism reproduces.
  This is the instruction's §4 row-2 phenomenon confined to the *second-order* feature:
  level and late-loading are captured, residual within-window curvature is not. It routes
  to ENDS (sub-annual/individual transitions), exactly as the instruction anticipated.
- **COL cohab overshoot (1.73 headline / 1.65 full).** The observed cohab *net* rise
  2008–24 is small (+0.031) because it rises to 2020 then falls; the sim's smooth path
  overshoots the small net change while tracking the level well (fig 1). Reported, not
  gated; same 2019–22 kink.

## 2. Calibrated mechanism — HEADLINE (cohort-only) spec, N1 composition-only loss

| | CRI | COL |
|---|---|---|
| κ(b) floor / midpoint / steepness | 0.371 / **1991.7** / 0.129 | 0.306 / **1988.8** / 0.194 |
| φ(b) formation tilt (per birth-yr) | 0.028 | 0.020 |
| π(t) | ≡ 1 (pinned; headline spec) | ≡ 1 (pinned; headline spec) |
| base marry-share-of-formation | 0.308 | 0.147 |

**Functional form and parameter count (Nina condition 1):** κ(b) = floor +
(1 − floor)·logistic(−steepness·(b − midpoint)) — **three parameters for the entire
cohort gradient**, no per-cohort effects anywhere in the model. The midpoint is therefore
a single recovered quantity, and its landing at 1991.7 / 1988.8 against the 2b APC
married-effect crossover (COL effects flip sign between the 1985 and 1990 bins) is a
non-circular convergence: the gradient was calibrated to composition *trajectories* only
and never saw the APC estimates (fig 2).

### 2.1 κ–φ separability (Nina condition 2)

Structural: κ(b) multiplies the two marriage-**entry** margins — the formation split
(married-vs-cohabiting) and cohab→married conversion — **both of which leave union status
unchanged**, so κ is union-total-neutral *by construction* (residual channel: married
unions dissolve less than cohabiting ones, a second-order effect). φ(b) multiplies
`form_base` and moves the union total directly. The two terms are pinned by different
data moments: κ by the married/cohabiting *split*, φ by the union-*total* trajectory.

Numeric check (paired seeds at headline params, ±perturbation, 2024 equal-band moments —
`outputs/stage3a/kphi_separability.csv`):

| perturb | Δ married | Δ union-total | \|Δm\|/\|Δu\| |
|---|---|---|---|
| CRI κ floor ±0.10 | +0.0092 | +0.0008 | **11.6** |
| CRI φ tilt ±0.005 | −0.0032 | −0.0101 | 0.32 |
| COL κ floor ±0.10 | +0.0121 | −0.0001 | **102** |
| COL φ tilt ±0.005 | −0.0007 | −0.0151 | 0.05 |

κ moves the married share with the union total essentially invariant; φ the mirror image.
The terms do not trade off against the same moments — separately identified, no
degrees-of-freedom inflation hiding in the "cohort gradient."

## 3. Mechanism decomposition (ablations, full recalibration per cell)

| N1 loss | full model | no period (cohort only) | no cohort (period only) |
|---|---|---|---|
| CRI | 0.0351 | 0.0372 (+6%) | 0.0405 (+15%) |
| COL | 0.0266 | **0.0246 (−7%)** | **0.0433 (+63%)** |

- **CRI:** the period shock is dispensable (+6% loss when pinned to zero; all gated metrics
  still pass). The full calibration kept d_p = 0.15, but the ablation shows it carries
  almost nothing — consistent with 2b's CRI verdict (period effect not statistically present).
- **COL:** removing the *cohort* gradient costs 63%; removing the *period* shock costs
  nothing (the pinned run even lands a slightly better basin — lower search dimension).
  The loss landscape independently reproduces the 2b ordering: **COL is cohort-dominant.**
- **Period reconciliation (Nina condition 3).** "Period dispensable" here and "COL period
  significant" in 2b are **the same finding, not a tension**: 2b established a period
  component that is statistically real (p≈3e-6) but *small* (curvature RMS 0.007) against
  a dominant cohort step-down; 3a finds that at band level this small component is
  absorbable by cohort turnover + formation tilt. Statistical existence ≠ quantitative
  necessity. Accordingly the **cohort-only model is the headline specification** and the
  period shifter is a documented robustness term — a tighter story, a smaller overfitting
  surface, and a better match to the 2b decomposition.
- **Caveat (limits of 3a identification):** the no-cohort runs still pass M1/M2 — four
  bands × annual shares cannot by themselves discriminate the mechanism. That is fine and
  by design: **3a answers sufficiency; identification of the structure rests on 2b/2c**
  (Anne's verdicts are inputs). We report this rather than claim discrimination we don't have.

## 4. §4 decision rule, applied

> Row 1 — "Model reproduces observed composition magnitude AND the late acceleration."

**Applied verdict: Row 1, both countries, on the pre-registered gate (M1 & M2) — stated
precisely as: sufficiency on magnitude and late-loading, with one unreproduced shape
residual (Nina condition 4).** Cohort-replacement alone (headline spec) is enough for the
composition collapse's magnitude and its late-loaded tempo. The COL M3 curvature-sign miss
is the surviving row-2 residual — *"the acceleration may live below the annual/cell
resolution"* — now narrowed to the second-order term around 2019–22 (provisionally
pandemic-era GEIH collection or a discrete exogenous shock), and it routes to ENDS (2c-ii)
as a **shape** question. It is explicitly **not cascade evidence**: a kink a smooth model
misses says nothing about reflexivity, and per the instruction §7 this outcome does not
reopen (B) in either direction; only ENDS transitions can.

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

## 8. Nina gate — conditions application record (STAGE3a_Nina_signoff.md)

| condition | applied where |
|---|---|
| 1 — lead with non-fit convergence; κ(b) form + parameter count | Headline (rewritten); §2 (3-param logistic, midpoints 1991.7/1988.8) |
| 2 — κ–φ separability | §2.1 (structural argument + paired-seed moment table; `kphi_separability.csv`) |
| 3 — period reconciliation; cohort-only headline | §1 (headline = cohort-only metrics), §2 (headline params), §3 (reconciliation bullet); figures re-rendered from the `_noperiod` spec |
| 4 — M3 precise framing, prominent | Headline + §4 (verdict restated; "not cascade evidence") |
| 5 — no-reflexivity code-read load-bearing | §6 unchanged (verified; `agent_step!` has no cross-agent read; wall log static + runtime) |

Condition-2/3 artifacts were produced by `stage3a_nina_conditions.jl` (final ensembles at
the already-calibrated `_noperiod` params + paired-seed sensitivity — **no recalibration,
no loss evaluation, no parameter tuning** in that script).

## 9. Deliverables produced

`stage3a_norefl_abm.jl` (model) · `calibrate_3a.jl` (calibration + pre-registered metrics +
wall checks + ablation pins) · `stage3a_nina_conditions.jl` (conditions 2–3) ·
`make_figures_3a.jl` + `_render_figures_3a.py` (figures, headline spec) ·
`outputs/stage3a/`: calibration bests + traces (baseline and both ablations),
`sufficiency_metrics{,_noperiod,_nocohort}.csv`, `kphi_separability.csv`, per-band
trajectories (full + `_noperiod`), mechanism profiles (κ, φ, π), TFR overlays,
`figures/fig1–fig4`, `_assert_no_tfr.log`, superseded-run archive.
Run logs: `_stage3a_full.log`, `_stage3a_col_rerun.log`, `_stage3a_cri_trace_regen.log`,
`_stage3a_ablation_{noperiod,nocohort}.log`, `_stage3a_nina_conditions.log`.

**Gate (instruction §7): PASSED, endorsements complete.** Nina endorsed build + read
(STAGE3a_Nina_signoff.md) with five binding conditions, all applied in this revision;
Anne confirmed the COL 2008-seed decision (§5) on 2026-07-11 (via Héctor) → feeds the
paper's model section (Fina's M2/M4). (B) stays deferred regardless — only ENDS can
reopen it.

*Stage 3a read. Claude, 2026-07-11, on the Debb build instruction carrying Anne's verdicts.
Nina-endorsed revision (conditions 1–5 applied same day).*

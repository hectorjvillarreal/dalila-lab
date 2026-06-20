---
type: working_note
tier: gate_deliverable
project_scope: [DFD]
authors: [Claude Code (Stage 2 calibration)]
addressed_to: Anne (population economics) and Nina (ABM lead), DFD Core Team
year: 2026
title: "Stage 2 skeleton ABM — calibration results: partial mechanism, marriage collapse generated, no locus slide"
venue: "DFD parallel research, internal — fertility-collapse ABM"
date_added: 2026-06-19
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE2_calibration_instruction.md"
---

# Stage 2 — Calibration Results (Skeleton Phase)

**Governing spec:** `STAGE2_calibration_instruction.md` (Anne + Nina). **Model:** `cri_skeleton_abm.jl`;
harness `calibrate.jl`. **Run:** 2026-06-19, full sweep w∈{0.4,0.6,0.8}, inner 12k×4, final 50k×16,
Nelder-Mead ≤150 evals/w × 3 restarts. All numbers below are from `outputs/`; none invented.

## Headline (read first)

The skeleton mechanism is **PARTIALLY validated.** With `marriage_drift` pinned at 0, the calibrated
social-norm threshold + cohort dynamics **generate most of the observed marriage collapse endogenously**,
and that drives a **threshold-necessary TFR decline** (falsification clean). BUT: the decline is a
**smooth glide, not a sharp nonlinear collapse** (criterion 2 fails); the **locus does not slide with `w`**
(criterion 3 not supported — the coupling-side/partnership threshold carries it at every `w`); the
**magnitude undershoots** (−22% vs −39%); and the **level is provisional** (placeholder ASFR). Verdict:
**do not freeze the nesting spec yet** — the skeleton has taught us specific structural revisions (§5).

---

## 0. Standing caveats (apply to EVERY result below)

- **C-ASFR [PLACEHOLDER]:** married-ASFR is the MEX-shape Gaussian prior, NOT the CR INEC schedule
  (acquisition flagged for Debb). **Criterion-1 LEVEL verdict is PROVISIONAL until replaced.**
- **No tempo (A5):** parity-independent hazard — the skeleton makes **NO tempo claim**.
- **Closed cohort (N6):** age-50 → new 15-yr nullipara; NOT a projection; the TFR *level* is conditional
  on the stationary age structure.
- **Single-baseline [PROVISIONAL]:** out-of-union fertility = 0.10×married, likely understated for CR.
- **Short series:** 15 annual composition points (2010–2024) limit resolvable curvature.
- **Backgrounds [PROVISIONAL]:** edu 0.35/0.40/0.25, loc 0.80/0.20 — structural context, never tuned to TFR.

**Identification wall:** TFR loaded for COMPARISON ONLY — never in the N1 loss, never tuned a parameter
(confirmed by construction, §6).

---

## 1. Calibration design + best-fit parameters

Free (8, N2): `form_base, marry_share_of_form, cohab_to_marr, dissolve_cohab, dissolve_marr,
norm_strength, norm_threshold, norm_steepness`. Pinned: `marriage_drift=0`, `w` (swept), ASFR primitive,
backgrounds. Loss (N1): Σ_bands Σ_years [(m_sim−m_obs)² + (c_sim−c_obs)²], bands 20-39, **composition only**.

**The best-fit parameters are IDENTICAL across all three `w`** (loss 0.0855 each). This is correct and
expected: `w` enters only *fertility* (Process B), never the *composition* dynamics (Process A), so the
composition calibration is `w`-invariant by construction.

| param | value (all w) |
|---|---|
| form_base | 0.1288 |
| marry_share_of_form | **0.1685** |
| cohab_to_marr | 0.0581 |
| dissolve_cohab | 0.0739 |
| dissolve_marr | 0.0243 |
| norm_strength | 0.6311 |
| norm_threshold | 0.5226 |
| norm_steepness | 16.596 |
| **N1 final loss** | **0.0855** (from 1.636 at defaults) |

_(Source: `outputs/calibration_best_w{40,60,80}.csv`.)_ Note `marry_share_of_form=0.17`: only 17% of
newly-formed unions are marriages — the calibration leans heavily on cohabiting formation (see §2 sub-test).

---

## 2. The four success criteria

### Criterion 1 — Collapse emerges (as output, not fit): **PARTIAL**
Observed TFR 1.83→1.12 (−39%). Generated (norm ON, 50k×16, ±sd ~0.02–0.03):

| w | gen TFR 2011 | gen TFR 2024 | Δ% | observed Δ% |
|---|---|---|---|---|
| 0.4 | 1.118 | 0.855 | **−24%** | −39% |
| 0.6 | 1.228 | 0.960 | **−22%** | −39% |
| 0.8 | 1.343 | 1.064 | **−21%** | −39% |

A real decline emerges as a pure output (TFR never in the loss) — **right direction, ~55–60% of the
observed magnitude.** The **level is ~0.6 too low throughout** (placeholder MEX-ASFR — Anne's predicted
discrepancy; reported, not tuned). **Verdict: PARTIAL — emerges directionally; magnitude undershoots;
level provisional.** _(Source: `outputs/tfr_path_w{NN}.csv`.)_

#### Sub-test (the decisive N2 test) — does the threshold GENERATE the marriage collapse? **MOSTLY YES**
With `marriage_drift=0` PINNED, the married-share decline is endogenous. Composition is `w`-invariant, so
one trajectory (final-year shares, ±sd ≤0.01):

| band | obs married 2010→2024 | sim married 2010→2024 | reproduced? |
|---|---|---|---|
| 20-24 | 0.124 → 0.031 | 0.124 → **0.078** | partial (undershoots — sim floor too high) |
| 25-29 | 0.265 → 0.106 | 0.267 → 0.146 | mostly |
| 30-34 | 0.431 → 0.216 | 0.434 → 0.249 | mostly |
| 35-39 | 0.477 → 0.309 | 0.475 → 0.335 | mostly |

**The threshold + dynamics generate most of the marriage collapse endogenously — non-circular, drift=0.**
It tracks the 25–39 bands well and **undershoots in the youngest band** (married floors at 0.078 vs the
observed 0.031). **Mechanistic nuance (important, honest):** the marriage decline is driven largely by
**cohort turnover + the low calibrated `marry_share_of_form` (0.17)** — new cohorts form mostly cohabiting
unions, shifting the stock — *as much as* by the norm threshold per se. The social-norm threshold is what
drives **total-union and fertility** down (it is necessary for the TFR collapse — criterion 4). **Verdict:
the marriage collapse is largely generated, not assumed; the youngest-band floor is not reached.**
_(Source: `outputs/composition_bands_w{NN}.csv`.)_

### Criterion 2 — Nonlinear, threshold-driven (not a smooth glide): **NOT MET**
The generated TFR path (w=0.6): 1.23 → 1.20 → 1.18 → 1.14 → 1.12 → 1.10 → 1.09 → 1.05 → 1.03 → 1.01 →
1.00 → 0.98 → 0.96 (2024) — a **steady ~−0.02/yr near-linear glide** with **no sharp acceleration or
post-threshold kink**. The observed series has a steeper 2018–2024 drop the model does not reproduce.
The threshold is *necessary* (criterion 4) but its effect manifests as a smooth decline because the
reference-group share crosses the logistic threshold gradually. **Verdict: NOT MET — the model generates
the decline as a glide, not the characteristic nonlinear collapse.**

### Criterion 3 — `w`-locus dependence: **NOT SUPPORTED** (see §4)

### Criterion 4 — Falsification (removing the threshold kills the collapse): **PASSES**
| w | gen TFR 2024 (norm ON) | gen TFR 2024 (norm OFF) | collapse killed by removing A? |
|---|---|---|---|
| 0.4 | 0.855 (−24%) | 1.193 (+6%) | **YES** |
| 0.6 | 0.960 (−22%) | 1.360 (+8%) | **YES** |
| 0.8 | 1.064 (−21%) | 1.533 (+10%) | **YES** |

Removing the social-norm threshold flips the decline to a *rise* at every `w`. **Verdict: PASSES cleanly —
the mechanism is not inert; the threshold does the work.** _(Source: `tfr_path_w{NN}.csv`.)_

---

## 3. Composition fit (N1 target)

Calibrated loss 0.0855 (from 1.636). Endpoint match is good for 25–39 (|error| ≤0.04 married, ≤0.06 cohab)
and weaker for 20–24 (married floor 0.078 vs 0.031). Seed bands tight: married/cohab sd ≤0.01, TFR sd
0.02–0.03 over 16 seeds. Full per-band trajectories in `outputs/composition_bands_w{NN}.csv`.

---

## 4. The `w`-locus 2×2 grid (N3) — NO SLIDE

For each `w`: site A (`social_norm_on`) × site B (`map_nonlinearity_on`, `map_depth=0.6` [PROVISIONAL]).
TFR % change per cell:

| w | A_on·B_off (baseline) | A_on·B_on (both) | A_off·B_off (neither) | A_off·B_on (map only) |
|---|---|---|---|---|
| 0.4 | −24% | **−34%** | +6% | +13% |
| 0.6 | −22% | **−33%** | +8% | +18% |
| 0.8 | −21% | **−32%** | +10% | +21% |

**Pattern (identical across `w` — no slide):**
- Removing site A (A_off) **kills the collapse at every `w`** (TFR rises). Site A — the partnership/
  **coupling-side** threshold — is necessary throughout.
- Site B **alone** (A_off·B_on) **never produces a collapse** (TFR rises). It is not sufficient.
- Site B **on top of A** (A_on·B_on) **deepens** the collapse to −32…−34% — *closer to the observed −39%* —
  so the map channel **amplifies** when A is active, but at a provisional `map_depth` and a suppressed level.

**Criterion-3 hypothesis (slide coupling-side→map-side as `w` rises): NOT SUPPORTED.** The coupling-side
threshold carries the collapse at every `w`; there is no `w` at which removing site B (rather than A)
kills it. **Likely partly structural:** site B keys on the fertility-weighted-union share, which only drops
once site A has moved the composition — so B is *downstream* of A and cannot fire independently. The two
threshold sites are **not independent** as the spec's 2×2 framing assumed. _(Source: `outputs/locus_grid_w{NN}.csv`.)_

---

## 5. Recommendation — NOT yet ready to scale

| criterion | verdict |
|---|---|
| 1 — collapse emerges (≥1 w) | PARTIAL (directional; ~55% magnitude; level provisional) |
| sub-test — marriage collapse generated (drift=0) | MOSTLY YES (undershoots youngest band) |
| 2 — nonlinear, not a glide | **NO** |
| 3 — locus slides with `w` | **NO** |
| 4 — falsification | YES |

**Recommendation: do NOT freeze the four-country nesting spec yet.** The skeleton proves a *partial*
mechanism — a threshold-necessary fertility decline driven by an endogenously-generated marriage collapse,
falsification clean — which is real and encouraging. But two criteria fail, and the skeleton has surfaced
**specific structural problems that must be resolved first**:

**Blockers before the nesting freeze:**
1. **CR married-specific ASFR** (A3, Debb) — until then the criterion-1 *level* (and so the magnitude
   verdict) is provisional. This is the top blocker.
2. **The smooth-glide problem (criterion 2).** The current logistic norm threshold produces a gradual
   decline. To get a *sharp* nonlinear collapse, the coupling→fertility coupling likely needs a genuine
   threshold/feedback the current formulation lacks. Anne/Nina design call.
3. **Site B is structurally downstream of site A** (criterion 3 can't slide). If a real *map-side* locus is
   to be testable, site B needs a formulation that can fire independently of A's composition effect —
   otherwise the 2×2 framing is degenerate. Nina design call.
4. **Youngest-band marriage floor** (20–24 married 0.078 vs obs 0.031) — the threshold + cohort turnover
   can't push young marriage low enough; worth understanding before scaling.
5. CR single-woman fertility baseline (replace 0.10×); backgrounds pinned to Censo 2022 / WB.

This is the "validate before scaling" outcome the skeleton phase was designed to produce: the mechanism is
not refuted (it generates real, threshold-necessary, non-circular dynamics) but it is **not yet sufficient**,
and we now know exactly which three structural pieces (ASFR level, sharper coupling, independent map site)
need work before the four-country nesting model and GPU sweep are justified.

---

## 6. Identification discipline — explicit confirmation
- `CRI_tfr_national.csv` is loaded ONLY in `load_observed_tfr()`, used ONLY for the comparison print and the
  `tfr_observed` output column. It feeds no hazard, transition, or parameter, and is NOT in `composition_loss`.
- The N1 loss is COMPOSITION ONLY (married & cohab, bands 20-39).
- `apply_params!` refuses to set `marriage_drift` (PINNED 0.0); the `model_step!` drift decay is a no-op.
- Process B intensities are structural primitives (placeholder ASFR × union × `w`), never fitted to CR TFR.
- **Verified by code-read before running** (not just by construction). No parameter was fit to TFR; the
  generated TFR is a pure OUTPUT.

---

*Stage 2 calibration results, 2026-06-19. Outputs in `model/outputs/`. endorsed_by blank pending Anne + Nina.*

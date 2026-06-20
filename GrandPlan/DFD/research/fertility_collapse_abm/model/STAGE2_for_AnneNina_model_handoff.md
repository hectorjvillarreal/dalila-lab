---
type: working_note
tier: handoff
project_scope: [DFD]
authors: [Claude Code (Stage 2 skeleton execution)]
addressed_to: Anne (population economics) and Nina (ABM lead), DFD Core Team
year: 2026
title: "Stage 2 skeleton ABM — handoff for improvement: what's wired, what's wrong, and the decisions only you can make"
venue: "DFD parallel research, internal — fertility-collapse ABM"
date_added: 2026-06-19
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE2_skeleton_abm_spec.md"
---

# Stage 2 skeleton ABM — handoff for improvement

**From:** Claude Code (Stage 2 skeleton execution)
**To:** Anne (population economics) and Nina (ABM lead)
**Re:** the skeleton now RUNS; here is exactly what it does, where it's wrong, and the
decisions that are yours to make so the next pass can actually generate the collapse.

Model: `cri_skeleton_abm.jl` (Agents.jl v6, CPU-parallel). Run + first result + env fixes
are in `STAGE2_skeleton_PROGRESS.md` §0. This note is the **actionable improvement list**,
split by owner. Line numbers below are into `cri_skeleton_abm.jl`.

---

## Where it is (read first)

It runs (baseline + falsification ensembles). First result, w=0.60:

| | observed | gen (norm ON) | gen (norm OFF, falsified) |
|---|---|---|---|
| 2011 | 1.87 | 0.99 | 1.07 |
| 2024 | 1.12 | 1.32 | 1.53 |
| 2010→2024 | **−39%** | **+33%** | +54% |

- ✅ **Falsification works directionally** — norm ON ends lower than norm OFF, so the
  social-norm threshold does downward work. The mechanism is not inert.
- ❌ **It does not reproduce the collapse — the sign is wrong.** The model *rises* (+33%)
  where the data *fall* (−39%). **This is a calibration/initialization failure, not a
  mechanism refutation.** Diagnosis: the population is seeded at an artificially low
  coupling/fertility state (~TFR 1.0) and *relaxes upward* toward the model's untuned
  equilibrium, instead of starting at ~1.83 and being driven down by the coupling dynamics.

**The single most important fix is joint and is yours:** the model must (a) START at the
observed 2010 state (Anne: initial level) and (b) be DRIVEN to collapse by a calibrated
Process A (Nina: the fit). Neither is done. Everything below serves those two.

---

## For ANNE (population economics — the fertility side)

1. **Specify the canonical TFR estimator (highest priority).** Right now the "TFR" is a
   crude proxy: `gfr × reproductive-span` (line 377) — general fertility rate times (AGE_MAX−AGE_MIN+1).
   This is not a Σ-of-single-year-ASFRs and its **level is not trustworthy**. Please specify the
   estimator you want (proper ΣASFR with an explicit age-exposure denominator), and I will wire it.
   The *shape* (nonlinearity) is more robust than the *level* under the current proxy, but we can't
   compare levels to the observed 1.83→1.12 until this is fixed.

2. **Specify the 2010 initial conditions (this is why the sign is wrong).** Two pieces:
   - **Initial union composition by age** — `seed_union` (line 257) + `build_model` kwargs
     `start_married=0.34, start_cohab=0.22` (line 225). These are flat provisional shares; give me
     the age-specific 2010 CR composition (we have it in `../data/coupling/CRI_coupling_annual.csv`,
     2010, bands 20–39 — I can seed directly from it; confirm you want that).
   - **Initial fertility level** — the seeded state must imply TFR ≈ 1.83 in 2010, not ~1.0. This
     is mostly a consequence of (1) the estimator and (3) the hazard level; confirm the target.

3. **Replace the fertility schedule with a CR married-ASFR (the Process-B intensities).**
   Current: `married_birth_hazard` is a Gaussian peak ~0.165/yr at age 27 (MEX ENADID *shape* as a
   regional prior, line 115); `single = 0.10×married` (line 125); `cohabiting = w×married` (line 334).
   Please give me a CR married-ASFR schedule (the **level is a primitive, NOT fitted to TFR** — that's
   the identification discipline). Also confirm:
   - the `single` out-of-union baseline (0.10× — CR has high non-marital fertility; is this right?);
   - that cohabiting fertility = `w` × married is the functional form you want (vs an additive or
     age-varying `w`).

4. **Age coverage 15–49 vs the 20–39 data.** The model needs 15–49 but the coupling CSV is 20–39;
   I extended with an age-graded gradient (flagged). Confirm whether the 15–19 and 40–49 tails matter
   for the level, or whether restricting the fertility window is fine for the skeleton.

5. **Parity-dependence of the hazard?** Parity is tracked (`seed_parity` line 270) but the birth
   hazard is currently parity-independent. The tempo finding suggests first-birth timing matters —
   do you want a parity-specific (or first-birth-specific) hazard now, or is parity-independent
   acceptable for the skeleton and deferred to the tempo-adjusted lead test?

---

## For NINA (ABM lead — structure & calibration)

1. **Define the Process-A calibration objective (the core remaining step).** The spec names the CR
   composition series as the target but not the loss. The free parameters are in `Params` (lines
   154–165): `form_base`, `marry_share_of_form`, `dissolve_cohab`, `dissolve_marr`, `cohab_to_marr`,
   the social-norm trio (`norm_strength`, `norm_threshold`, `norm_steepness`), and `marriage_drift`.
   Please specify:
   - **what loss** — fit the *levels*, the *trajectory*, or the *acceleration* of the married &
     cohabiting paths (2010–2024)? My suggestion: weighted trajectory of both married and cohabiting
     shares by band, but your call.
   - **which parameters are free vs pinned** — in particular, is `marriage_drift` a *free* parameter
     or *pinned* to the observed CR marriage decline (e.g. married 30–34: 43%→22%)? This matters: if
     pinned, the model can't "explain" the marriage collapse, only propagate it.
   - **the optimizer** — I can wire a simple SMM/grid or Optim over the free set once the loss is set.

2. **Define the `w`-locus-dependence diagnostic (criterion 3).** Both threshold sites are coded —
   site A (social-norm, `norm_multiplier` line 202, ON by default) and site B (map, `map_multiplier`
   line 212, OFF by default via `map_depth=0`). To *show* the locus slides with `w`, we need a stated
   protocol — e.g. for each `w ∈ {0.4,0.6,0.8}`, run {A on/off} × {B on/off} and report which site,
   when removed, kills the collapse. The A-switch exists (`social_norm_on`); the B-sweep
   (`map_nonlinearity_on=true, map_depth>0`) is wired but the comparison protocol is undefined. Specify it.

3. **Reference group for the social-norm term.** Currently same-age-band only (`refgroup_partnered_shares`
   line 187). Should education/location homophily enter it (the spec flagged this as a provisional
   extension)? If yes, say which dimensions.

4. **Population size & ensemble.** 20k agents (line 172), few seeds; seed-sensitivity is unquantified.
   Set the population size and seed count you want for stable estimates (I'd suggest ≥50k × ≥16 seeds
   for the calibration runs, but it's a cost/precision call).

5. **Closed-cohort population dynamics — acceptable?** Women age 1yr/tick; at age 50 they're replaced
   by a new 15-yr single nullipara (a skeleton simplification, not a projection). Confirm this is fine
   for the skeleton, or specify mortality/migration if the age structure must be realistic for the
   TFR level.

---

## How to run / iterate (so you can drive it yourselves)

```bash
cd GrandPlan/DFD/research/fertility_collapse_abm/model
JULIA_NUM_THREADS=4 julia --project=. cri_skeleton_abm.jl 0.6 8   # args: w, nseeds
# all tunable primitives are the `Params` struct (lines 148–177); change a default and re-run.
# outputs/: tfr_path_w{NN}.csv, composition_path_w{NN}.csv (generated vs observed)
```
Environment is pinned and reproducible (`Manifest.toml`, Distributions =0.25.116 — do not bump it,
Agents.jl won't precompile against newer Distributions). The observed TFR (`CRI_tfr_national.csv`) is
loaded for COMPARISON ONLY — never as a fit target; please keep it that way.

## Do NOT touch (frozen invariants — gate of record `../data/coupling/STAGE1_5_identification_memo.md`)
1. State variable is union composition {single, cohabiting, married}.
2. `w` is a nested structural parameter (runs across {0.4,0.6,0.8}); don't hard-code it.
3. The nonlinearity locus is `w`-determined — don't hard-code site A vs site B as "the" locus.

## The ask, in one line each
- **Anne:** the TFR estimator (1), the 2010 initial level (2), and the CR married-ASFR schedule (3).
- **Nina:** the Process-A calibration loss + free/pinned parameters (1), and the `w`-locus protocol (2).

With those, the next pass becomes a real calibration run and the "does it generate the collapse"
test (criterion 1) becomes evaluable. Until then the skeleton is alive and falsifiable but uncalibrated.

*Stage 2 skeleton handoff. 2026-06-19. Companions: STAGE2_skeleton_abm_spec.md (spec),
STAGE2_skeleton_PROGRESS.md (run record), cri_skeleton_abm.jl (model). endorsed_by blank pending Anne + Nina.*

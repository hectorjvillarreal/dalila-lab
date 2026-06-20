# Stage 2 — Consolidated Calibration Instruction (Skeleton Phase)
# Project: Rapid Fertility Collapse in Latin America (DFD parallel research)
# Author: Anne (population economics) and Nina (ABM lead), DFD Core Team
# Date: 2026-06-19
# For: Claude Code on Dalila
# Location: GrandPlan/DFD/research/fertility_collapse_abm/model/
# Answers: STAGE2_for_AnneNina_model_handoff.md (every open question)

---

## What this instruction does

The skeleton runs, the falsification check works directionally, and the identification
wall held (TFR never touched as a target). The handoff surfaced a finite list of modeling
decisions, correctly assigned to Anne and Nina. This instruction answers all of them so
the next run is a **real calibration**, not another provisional pass. After this run, the
core test — does the social-norm threshold *generate* the marriage collapse and with it
the fertility collapse (criterion 1) — becomes evaluable for the first time.

The frozen invariants are unchanged and still govern. Nothing here overrides them.

---

## ANNE'S ANSWERS (fertility side)

### A1 — TFR estimator: proper ΣASFR
Replace the `gfr × span` proxy (line 377) with a proper period-TFR:

```
TFR(t) = Σ_a ASFR(a, t)        for single-year ages a = 15…49
ASFR(a, t) = births to women aged a in year t / woman-years of exposure at age a in year t
```

Use single-year ages, explicit age-exposure denominator (woman-years lived at each age
during the year, not end-of-year headcount). Sum across 15–49. This is the canonical
estimator and the only one whose level is comparable to the observed 1.83→1.12.

**Caution to encode in the results memo:** once the level is interpretable, do NOT read
the level as validation. The *shape* (nonlinearity) is the claim; the level is a
consistency check. A model that matches the level through a smooth glide has failed
criterion 2 even if it passes the level.

### A2 — 2010 initial conditions: seed from observed composition
Seed the 2010 population directly from `../data/coupling/CRI_coupling_annual.csv`, 2010,
age-specific by band. Do NOT use the flat provisional `start_married=0.34,
start_cohab=0.22` (line 225). The flat seeding is the proximate cause of the wrong sign —
the population starts at the wrong composition and relaxes toward the untuned equilibrium.

- For bands 20–24, 25–29, 30–34, 35–39: use the observed 2010 married and cohabiting
  shares directly.
- For the 15–19 and 40–49 tails (not in the coupling CSV): see A4.

The seeded state must imply TFR ≈ 1.83 in 2010 once A1 (estimator) and A3 (ASFR level)
are in place. If it does not, the discrepancy is diagnostic — report it rather than
tuning to close it.

### A3 — Married-ASFR schedule: a sourced primitive (ACQUISITION REQUIRED)
Replace the MEX-ENADID Gaussian prior (line 115) with a **Costa Rica married-specific
ASFR schedule**. This is a structural primitive calibrated to **fertility data, NEVER to
TFR**. This is the single hardest identification point in the build: if the married
hazard is ever set by asking "what makes TFR come out right," the paper is dead.

**Acquisition (flagged for Debb, blocks the clean run):** CR married-specific ASFR by
age, from INEC vital statistics (births by age and marital status of mother / female
population by age and union status) or the CR ENDS-equivalent. Until acquired, the run
can proceed with the MEX-shape prior **explicitly flagged as placeholder** — but the
criterion-1 verdict is not final until the CR schedule replaces it.

Functional form confirmations:
- **Cohabiting fertility = `w` × married-ASFR** — yes, multiplicative, this functional
  form is correct for the skeleton. Age-varying `w` is a nesting-phase refinement, not now.
- **Single (out-of-union) baseline:** CR has high non-marital fertility, so 0.10× married
  is likely too low. Set the single-woman baseline from the CR data once A3 is acquired;
  until then flag 0.10× as provisional and likely understated.

### A4 — Age coverage: keep 15–49, restrict the calibration window
The model needs 15–49 for a correct TFR level (the 15–19 and 40+ tails carry real if
small fertility). Keep the full fertility window. But calibrate Process A (the coupling
dynamics) only on the 20–39 bands where we have observed composition data. The tails get
an age-graded union gradient (already flagged) and contribute to the TFR level but not to
the Process-A loss. Document the split explicitly.

### A5 — Parity-dependence: deferred for the skeleton
Parity-independent hazard is acceptable for the skeleton. Parity is tracked; wire the
parity-specific (first-birth-specific) hazard in the nesting phase alongside the
tempo-adjusted lead test. **Constraint:** because the skeleton hazard is parity-
independent, the skeleton does NOT speak to tempo. Do not make any tempo claim from
skeleton results. This is a stated scope limit.

---

## NINA'S ANSWERS (structure and calibration)

### N1 — Calibration loss: weighted trajectory of both margins
Fit the **trajectory** (full 2010–2024 path) of BOTH the married and cohabiting shares,
by age band, weighted. Not levels-only (lets a smooth glide match endpoints while missing
the mechanism), not acceleration-only (too noisy on 15 annual points).

```
Loss = Σ_bands Σ_years [ ω_m (married_sim − married_obs)²
                       + ω_c (cohab_sim  − cohab_obs )² ]
```
Start with ω_m = ω_c = 1; expose the weights as tunable. The loss is on COMPOSITION only.
TFR is never in the loss.

### N2 — `marriage_drift`: PINNED, not free (the decisive choice)
**`marriage_drift` is pinned to the observed CR marriage decline as a target the threshold
must REPRODUCE — it is NOT a free parameter.**

This is the most important single decision in the calibration, so the rationale is
explicit and binding:

- If `marriage_drift` were free, the optimizer would use it to absorb the marriage
  collapse as an **exogenous trend**, and the model would then "reproduce" the fertility
  collapse by propagating a marriage decline it simply assumed. That is circular and
  worthless.
- The thesis is that the marriage collapse is **endogenous** to the social-norm threshold
  — partnership decline cascades, it does not drift exogenously. So the model must
  **generate** the observed marriage trajectory from the threshold dynamics.
- Therefore: set `marriage_drift = 0` (no exogenous secular drift in marriage propensity),
  and require the social-norm threshold (Process A: `norm_strength`, `norm_threshold`,
  `norm_steepness`, `form_base`, `marry_share_of_form`, `cohab_to_marr`, dissolution
  rates) to **produce** the observed married-share collapse endogenously.
- The observed marriage trajectory (e.g. married 30–34: 43%→22%) is the TARGET in the N1
  loss, not an input drift. If the threshold cannot generate it, that is a real finding —
  the mechanism is incomplete — and we report it, not paper over it with a drift term.

**Free parameters** (calibrated to the N1 composition loss): the social-norm trio
(`norm_strength`, `norm_threshold`, `norm_steepness`), `form_base`, `marry_share_of_form`,
`cohab_to_marr`, `dissolve_cohab`, `dissolve_marr`.
**Pinned / fixed:** `marriage_drift = 0`; `w` (swept, not fitted); the married-ASFR
primitive (A3); education/location backgrounds.

### N3 — `w`-locus diagnostic: the explicit 2×2 grid
For each `w ∈ {0.4, 0.6, 0.8}`, run the full 2×2:

| | site B OFF (`map_depth=0`) | site B ON (`map_depth>0`) |
|---|---|---|
| **site A ON** (`social_norm_on=true`) | baseline | both thresholds |
| **site A OFF** (`social_norm_on=false`) | neither | map-only |

For each `w`, report which site, **when removed, kills the collapse**. The criterion-3
claim to test: *at low `w` removing site A (partnership threshold) kills the collapse →
coupling-side locus; at high `w` removing site B (map threshold) kills it → map-side
locus.* The locus sliding with `w` is the invariant made visible. Report the full grid
even where the pattern is mixed or absent — a clean slide is the hoped-for result, not a
required one.

### N4 — Reference group: same-age-band for the skeleton
Keep the social-norm reference group as same-age-band only (line 187) for the skeleton.
Education/location homophily is a nesting-phase extension. Adding homophily now multiplies
the parameter space before the base mechanism is proven. Defer.

### N5 — Population and ensemble: 50k × 16 for calibration
- Population: 50,000 agents (up from 20k) for stable composition estimates.
- Ensemble: 16 seeds minimum for calibration runs; report mean ± sd on every reported
  quantity. Quantify the seed band explicitly — an unquantified ensemble is non-conformant.
- CPU-parallel across seeds (Julia threading / `Distributed`). Do NOT GPU the agent step.

### N6 — Closed-cohort dynamics: acceptable for the skeleton
Women age 1yr/tick, age-50 replaced by a 15-yr single nullipara. Acceptable as a skeleton
simplification. Flag explicitly that this is NOT a population projection and the TFR level
is conditional on the stationary age structure it implies. Mortality/migration enter only
if the nesting phase needs a realistic age structure for the level.

---

## Run protocol

```bash
cd GrandPlan/DFD/research/fertility_collapse_abm/model
# calibration run, per w:
JULIA_NUM_THREADS=8 julia --project=. cri_skeleton_abm.jl 0.6 16   # w, nseeds
# then 0.4 and 0.8 for the band; then the 2×2 locus grid per w (N3)
```
Keep the Distributions =0.25.116 pin (Agents.jl precompile constraint). Observed TFR
loaded for COMPARISON ONLY — the identification wall stays up.

---

## Success criteria (unchanged from spec, now evaluable)

1. **Collapse emerges** as output (not fit) for at least one `w` — generated TFR falls
   toward 1.12, having started at ~1.83.
2. **Nonlinear**, threshold-driven — not a smooth glide through the endpoints.
3. **`w`-locus dependence** appears in the N3 grid.
4. **Falsification** holds — removing the active threshold kills the collapse.

Criterion 1 now has a sub-test it did not have before: **does the threshold generate the
observed MARRIAGE collapse** (the N2 target) — because TFR collapse now runs THROUGH the
endogenous marriage collapse, not around it.

---

## Deliverables

Under `model/`:
1. Updated `cri_skeleton_abm.jl` — ΣASFR estimator, observed-2010 seeding, CR married-ASFR
   primitive (or flagged placeholder), `marriage_drift=0`, N1 loss, N3 grid harness.
2. Calibration record — free-parameter estimates, the composition fit (married & cohabiting
   trajectory, sim vs observed), seed bands.
3. `STAGE2_calibration_results.md` — the four criteria, the marriage-generation sub-test,
   the `w`-locus grid, what still needs to change before the nesting freeze, and an
   explicit recommendation: is the mechanism proven enough to scale?
4. Figures — generated vs observed TFR; generated vs observed married/cohabiting
   trajectories; the nonlinearity; the with/without-threshold falsification; the `w`-locus grid.

---

## Acquisition flagged for Debb (parallel, blocks final criterion-1 verdict)

CR married-specific ASFR schedule by age — INEC vital statistics (births by age and
marital status of mother) or CR ENDS-equivalent. File to
`../data/coupling/` or `../data/fertility/` per Debb's convention, PROTO-RAG-001 sidecar.
Until acquired, the run proceeds with the MEX-shape placeholder explicitly flagged; the
criterion-1 verdict is provisional until the CR schedule is in.

---

## Documentation discipline (Debb / PROTO-RAG-001)

Findings and caveats together. Standing caveats for this run: the placeholder ASFR (until
A3 acquired), the parity-independent hazard (no tempo claims), the closed-cohort age
structure (level is conditional), the seed band, the short 15-point composition series.
Every result carries its caveat inline. `endorsed_by` blank pending Anne + Nina.

---

*Stage 2 Consolidated Calibration Instruction. Version 1.0, 2026-06-19.*
*Answers every open question in STAGE2_for_AnneNina_model_handoff.md.*
*Invariants unchanged; full-spec freeze still deferred to the post-calibration nesting gate.*

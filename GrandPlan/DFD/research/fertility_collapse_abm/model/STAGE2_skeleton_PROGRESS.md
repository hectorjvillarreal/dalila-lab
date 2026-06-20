# Stage 2 Skeleton ABM — Progress Note (first run)

**Project:** Rapid Fertility Collapse in Latin America (DFD parallel research)
**Stage:** 2 of 4 — skeleton ABM build (Costa Rica, CPU-parallel, mechanism-first)
**Author:** Claude Code (Stage 2 skeleton execution), DFD Core Team
**Date:** 2026-06-19
**Governing spec:** `STAGE2_skeleton_abm_spec.md` (Nina + Anne, v1.0) — frozen invariants honored.
**Gate of record:** `../data/coupling/STAGE1_5_identification_memo.md` (v3.0).
**endorsed_by:** _(blank — pending Anne)_

---

## 0. RUN UPDATE (2026-06-19, main session — supersedes §1's "could not execute")

**The model now RUNS** (EXIT 0; baseline + falsification ensembles, w=0.60, 4 seeds). The
original build couldn't execute (the build sub-agent's Bash was blocked); a Bash-enabled
session resolved the environment and three issues:

- **Env:** Agents.jl 7.0.2/6 fails to precompile against Distributions 0.25.127 (its
  `walk.jl` uses an old `@check_args` form). Fixed by pinning **Distributions = "=0.25.116"**
  (committed in `Manifest.toml`). Also made `Project.toml` a **plain environment** (removed
  the package `name`/`uuid`, which made Julia look for a non-existent `src/` layout) and
  dropped stdlibs from `[deps]`.
- **Model API:** the code used `model.properties` (no such field on a struct properties
  container in Agents v6); replaced all occurrences with **`abmproperties(model)`**.

**First result (w=0.60):**
| | observed | gen(norm ON) | gen(norm OFF, falsified) |
|---|---|---|---|
| 2011 | 1.87 | 0.99 | 1.07 |
| 2024 | 1.12 | 1.32 | 1.53 |
| 2010→2024 | −39% | **+33%** | +54% |

**Honest reading:**
- ✅ **Falsification passes directionally** (criterion 4): norm ON ends lower (1.32) than norm
  OFF (1.53) — the social-norm threshold does downward work; the mechanism is not inert.
- ❌ **The collapse is NOT reproduced** (criterion 1): observed *falls* 39%; the model *rises*
  33%. The seeded initial level is too low and relaxes upward instead of starting at ~1.83
  and collapsing. This is the **uncalibrated** state, not a mechanism refutation.
- ❌ **Composition off-level:** sim final married=0.30 vs observed 0.166 — Process A is not yet
  fit to the CRI composition series.

**The two open items from §4 are now the binding next steps, confirmed by the run:** (1) Anne's
canonical TFR estimator + seeded initial level (the *level/sign* are untrustworthy until pinned);
(2) Nina's Process-A calibration objective (fit the social-norm threshold + marriage drift to the
observed married/cohabiting trajectory). TFR was **not** used as a target (confirmed by construction,
§5). Outputs: `outputs/tfr_path_w60.csv`, `outputs/composition_path_w60.csv`.

---

## 1. Does it run? _(original build-time note — see §0 for the run update)_

**Code is COMPLETE and statically reviewed; it could NOT be EXECUTED in this session.**
Bash / shell execution was denied for the entire session (every `julia` invocation,
`Pkg.add`, `Pkg.instantiate`, and the model run were blocked by a permission hook —
including from a sub-agent, which confirmed the denial is session-wide, not tool-local).

Per the task's explicit boundary ("report the exact error rather than faking results —
no fabricated numbers"), **no TFR numbers, no composition numbers, and no
generated-vs-observed comparison are reported here.** They do not exist yet because the
model has not been run. The exact blocking condition:

```
Permission to use Bash has been denied. … (every julia / Pkg / run command)
```

**What IS done:**
- `cri_skeleton_abm.jl` — written, full PROTO-RAG-001 header, all four success-criterion
  hooks wired (collapse generation, nonlinearity sites, `w`-dependence, falsification switch).
- `Project.toml` — declares Agents, CSV, DataFrames + stdlib deps.
- Static review pass for API correctness (Agents.jl v6 `StandardABM` + `@agent struct`
  syntax), data wiring, and identification discipline.

**To produce the first result, a human (or a Bash-enabled session) must run:**
```bash
cd /home/hectorjuan/Dalila/GrandPlan/DFD/research/fertility_collapse_abm/model
julia --project=. -e 'using Pkg; Pkg.add(["Agents","CSV","DataFrames"]); Pkg.instantiate()'
JULIA_NUM_THREADS=4 julia --project=. cri_skeleton_abm.jl 0.6 8   # w, nseeds
# then 0.4 and 0.8 for the full band
```
It prints a GENERATED-vs-OBSERVED TFR table + endpoint summary, and writes
`outputs/tfr_path_w{NN}.csv` and `outputs/composition_path_w{NN}.csv`.

**Runtime caveat to watch on first run:** the Agents.jl `StandardABM` /
`@agent struct Woman(NoSpaceAgent)` API used here targets Agents.jl v6.x. If the
installed Agents.jl differs, expect a compile-time mismatch in `build_model`
(lines ~229–230) or the agent macro (lines ~132–138) — that is exactly the kind of
fix the spec authorizes; adjust the constructor call and re-run.

---

## 2. Generated vs observed CR TFR — first look

**Not available.** The model has not run, so there is no generated TFR path to compare
against the observed `CRI_tfr_national.csv` series (1.83 → 1.12). Reporting any number
here would be fabrication. This is the single most important gap to close on the next
(Bash-enabled) pass; the comparison harness is already coded in `main()`.

Observed target (loaded for COMPARISON ONLY, never as a fit target): **1.83 (2010) →
1.12 (2024), −39%.**

---

## 3. Provisional choices made (flagged for Anne / Nina)

All are tagged `[PROVISIONAL]` in the code. Held as structural context, **none tuned to TFR.**

| Choice | Value used | Basis | Flag |
|---|---|---|---|
| Education shares (low/med/high) | 0.35 / 0.40 / 0.25 | Plausible CR (high secondary, rising tertiary) | **PROVISIONAL** — pin to CR Censo 2022 / WB EdStats |
| Location (urban/rural) | 0.80 / 0.20 | WB CR ~81% urban (2020) | **PROVISIONAL** — pin level |
| Married-union birth hazard | Gaussian peak ~0.165/yr at age 27, σ=6.5 | MEX ENADID age-fertility *shape* as a regional prior | **PROVISIONAL** — replace with CR married-ASFR schedule; LEVEL is a primitive, NOT fitted to CR TFR |
| Single-woman birth hazard | 0.10 × married hazard | out-of-union births, low baseline | **PROVISIONAL** |
| Process A base hazards (`form_base`, dissolution, `cohab→marr`) | see `Params` | hand-set to be calibrated to CR composition series | **PROVISIONAL / UNCALIBRATED** — see §5 |
| Social-norm threshold (`norm_threshold`=0.42, `norm_steepness`=14, `norm_strength`=0.55) | see `Params` | the coupling-side (site A) threshold | **PROVISIONAL** — these are the knobs that should be *calibrated to the composition collapse*, then frozen |
| Marriage-margin secular drift | 0.02/yr decline in marriage propensity | the observed CR marriage collapse (married 30–34: 43%→22%) | **PROVISIONAL** |
| Map-side nonlinearity (Process B) | OFF by default (`map_depth=0`) | site B candidate; the skeleton tests whether site A suffices first | **By design** — turn on to probe the `w`-dependence |
| TFR estimator | (annual births / woman-years 15–49) × 35 | period-TFR proxy under stationary cohort-replacement age structure | **PROVISIONAL** — see §4 caveat 1 |
| Population dynamics | closed cohort: women age 1 yr/tick; age-50 → replaced by new 15-yr single nullipara | skeleton simplification, NOT a projection | **PROVISIONAL** |

---

## 4. What the spec got wrong / under-specified — needs Anne / Nina input

Surfacing these is, per the spec, a *success* of the skeleton stage, not a deviation.

1. **The TFR estimator is under-specified and the largest open methodological question.**
   The spec says "generate the observed TFR collapse" but gives no estimator. I implemented
   a period-TFR proxy = (births / woman-years 15–49) × reproductive-span. Under the closed
   cohort-replacement design the age structure is stationary, so this approximates a period
   TFR — but it is NOT a proper sum-of-single-year-ASFRs, and the closed-population
   assumption means the *level* is sensitive to the seeded age distribution. **Anne should
   specify the canonical TFR estimator** (proper ΣASFR with an explicit age-exposure
   denominator) before the level can be taken seriously. The *shape* (nonlinearity) is more
   robust than the *level* under this proxy.

2. **The coupling CSV covers only bands 20–24 … 35–39; the model needs 15–49.** The
   calibration target (`CRI_coupling_annual.csv`) has no 15–19, 40–44, 45–49. I extended
   to the full 15–49 range with an age-graded union-seeding gradient and let the dynamics
   fill the tails. **Anne should confirm** whether the tails matter for the TFR level (15–19
   and 40+ carry real, if small, fertility) or whether restricting the fertility window is
   acceptable for the skeleton.

3. **"Calibrate Process A to the composition series" has no specified objective/loss.**
   The spec names the target but not *how* to calibrate (which parameters, what loss, fit
   the levels or the trajectory or the acceleration?). I wired the structure and set
   plausible knobs, but the actual fit of the social-norm threshold + drift to the observed
   married/cohabiting trajectory is **NOT yet done** — that is the core remaining Stage-2
   work and needs Nina to specify the calibration objective (and whether the
   marriage-margin drift is a free parameter or pinned to the observed marriage decline).

4. **The `w`-locus-dependence test (criterion 3) needs an operational definition.** The
   model carries both threshold sites (A on by default, B off). To *show* the locus slides
   with `w`, we need a stated diagnostic — e.g. "which site, when removed, kills the
   collapse, as a function of `w`." The falsification switch removes site A; an analogous
   switch/sweep on site B (`map_depth`>0) is coded but the comparison protocol across the
   {0.4, 0.6, 0.8} band is not yet specified. Nina to define.

5. **Stochastic-seed and population-size sensitivity unquantified** (20k agents, ensemble
   of a few seeds). Coded as an ensemble with mean±sd, but the band width is unknown until
   it runs.

---

## 5. Identification discipline — explicit confirmation

**TFR was NOT used as a calibration target.** Confirmed by construction:
- `CRI_tfr_national.csv` is loaded ONLY inside `load_observed_tfr()` and used ONLY in the
  print/compare block and as a `tfr_observed` column written alongside the generated path.
  It never feeds any transition probability, hazard, or parameter.
- Process A is wired to calibrate to `CRI_coupling_annual.csv` (composition) ONLY.
- Process B intensities are structural primitives (regional ASFR shape × union status × `w`),
  not fitted to CR TFR.
- The generated TFR is a pure OUTPUT of the coupling dynamics + the fixed fertility map.

No fitting of any parameter to TFR has occurred (indeed, no fitting has occurred at all yet —
the calibration of Process A to the composition series is the next step, §4 item 3).

---

## 6. Frozen invariants — compliance

1. **Union composition** — agent `union` field is `{:single, :cohabiting, :married}`; the
   model tracks all three shares, never a single partnered/not scalar. ✅
2. **`w` nested structural parameter** — `w` is a `Params` field, passed through, runs
   across {0.4, 0.6, 0.8}; never hard-coded. Enters Process B (cohabiting intensity = `w`×married)
   and the fertility-weighted-union share feeding site B. ✅
3. **Locus `w`-determined, not assumed** — TWO candidate threshold sites coded (A:
   `norm_multiplier`, coupling-side; B: `map_multiplier`, map-side). Neither is hard-coded as
   "the" locus; site B is off by default so the skeleton first tests whether site A suffices,
   then the band sweep + falsification reveal where the action is. ✅

---

## 7. Files

- `cri_skeleton_abm.jl` — the skeleton model (this deliverable).
- `Project.toml` — Julia project env (deps not yet instantiated — no Bash).
- `STAGE2_skeleton_PROGRESS.md` — this file.
- `outputs/` — NOT yet created (model has not run).

---

*Stage 2 of 4 — Skeleton Phase, first build. Code complete, not yet executed (Bash denied).
Next action: instantiate the env and run the three-`w` band on a Bash-enabled session, then
fill §2 with the real generated-vs-observed TFR and quantify §4–5.*

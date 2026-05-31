# Gate-sequence notes — reorder decision for Draft-June-v4

**Session:** 2026-05-31 · **Spec:** `CC_instrucciones_gate_runs.md`
**Working tree:** `Missions/Funded/BID2/GE-now with Gender/`
**Solver:** `ge_model_gender.jl` (read-only; J=17, gender_gap=true), Julia 1.11.7, `-t 4`.

> **STATUS: COMPLETE. Run 1 passed. Run 0 → OUTCOME A (infeasibility holds,
> rⁿ crossed n_p at iter 11). Reorder is VIABLE — green light for Runs 2–4.**

---

## 1. What was run

Two stationary GE solves on `ge_model_gender.jl`, at the `inputs_mxdata`
SMM calibration, to decide whether the §§4–5 reorder of `Draft-June-v4.tex`
is viable (i.e. whether Runs 2–4 get launched).

- **Run 1** — calibrated 2020 baseline, joint closure (τp endogenous via
  PAYG balance, B residual). Driver: `run1.jl`.
- **Run 0** — C2 interp-1 gate check: same calibrated params, 2050
  demographics, τp pinned at Run 1's value, pension benefits at the
  calibrated PAYG formula (NOT scaled), PAYG deficit routed into the
  general budget, B residual. Driver: `run0.jl`.

Strict-serial order (spec §3 recommendation): Run 1 first, its τp read from
`run1_summary.csv`, then Run 0. No parallelization.

## 2. Calibrated inputs used

Source of the 6 SMM scalars: `outputs/CALIBRATION_RESULTS_mxdata.md` §4
(best of 4 starts, Q = 13.28), cross-checked against the table the spec
itself cites.

| Param | Symbol in solver | Value |
|---|---|---:|
| Ψ (labor disutility) | `Ψ_labor` | 13.452490 |
| Ξ (health amenity) | `Ξ_amenity` | 0.274472 |
| ξ (amenity curvature) | `ξ_curv` | 0.500000 (frozen) |
| H̄₀ (health-prod scale) | `H_scale` | 0.247474 |
| h^slope (age-decline) | `h_slope` | −0.035807 |
| ζ_h (health-prod curvature) | `H_curv` | 0.579138 |

First-step ENOE inputs (`inputs_mxdata/first_step/`):
- `e_age` 2×J (Milo ENOE): female is the **genuine profile**, ≈0.74× male
  at prime age — NOT the old flat 0.85× stub.
- θ_L = −0.3726, θ_H = +0.3726 (111% skill premium).

## 3. Deviations from the literal spec (deliberate)

**(a) Override mechanism — function re-`@eval`, not const-redef.**
The 6 calibrated scalars are `const` in `ge_model_gender.jl`. Julia 1.x
INLINES const scalars into compiled methods, so a bare `Core.eval` const
redefinition silently fails to propagate (this is the documented trap that
bit the demographic_experiment RUN-2 first attempt; see memory
`julia-const-redef-inlining`). Instead, `apply_calibration!()` re-`@eval`s
the four leaf functions that read those consts — `health_amenity`,
`disutility_of_labor`, `labor_supply`, `health_production` — with the
calibrated values baked in as literals. Same idiom `run_aging_ssvs.jl` uses
for its closure overrides. `e_age` and `θ_grid` are const *arrays* (element
reads are not inlined), so those are mutated in place.
Verified live in run1.log:
- `disutility_of_labor(1.0)=4.484163` = Ψ/(1+ν) at Ψ=13.4525 ✓
- `health_amenity(1.0)=0.548944` = Ξ/(1−ξ) at Ξ=0.2745, ξ=0.5 ✓
- `e_age[2,1:3]=0.8350,0.9726,1.0615` (genuine female), `θ_grid=∓0.3726` ✓

**(b) Input scope — literal 8-override, NOT full mxdata primitive swap.**
Only the 6 scalars + `e_age` + `θ` are injected. `ψ_base`, `δh`, `ρ_AR`,
`σ_ε`, `π_birth`, `ϱ_pen` are left at the `ge_model_gender.jl` 2020 values.
Rationale: the spec's own sanity checks (#5 τp vs κ·dep, #6 K vs the v3
stub 14.378) are only meaningful against the stub baseline, so injecting
the full mxdata primitive set would break the intended comparison.
Diff of `inputs_anchored` → `inputs_mxdata` confirms only `e_age`, `θ`, and
the hours *target* (which does not enter the GE solve) actually changed in
the substituted block.
**Known approximation:** the SMM's PE-anchor saw `ρ_AR=0.782`, `σ_ε=0.265`,
and asymmetric `π_birth`, which differ from the GE solver stubs
(`ρ_AR=0.98`, `σ_ε=0.05`, symmetric `π_birth=0.25`). These are first-step
inputs NOT propagated into the gate runs. For the reorder gate this is
acceptable (it isolates the e_age/θ/param effect against the v3 baseline);
flagged here so the §§4–5 rewrite can decide whether to re-anchor.

## 4. Run 1 — calibrated 2020 baseline: PASSED

Converged at **iter 19**, DIFF/Y = −8.43e−5, monotone contraction, no NaN,
no DomainError (the `damp_ge=0.30` absorbed the asymmetric-e_age transient).

Outputs: `results/run1_summary.csv`, `run1_welfare.csv`,
`run1_lifecycle.csv` (64 data rows = 4 types × 17 ages), `run1.log`.

**Equilibrium:**

| Quantity | Value |
|---|---:|
| K | 10.4880 |
| L | 11.5741 |
| Y | 17.8732 |
| r (annual) | 4.803% |
| r (5-yr) | 0.264379 |
| w | 0.98831 |
| τp | 0.108302 |
| pension flow | 0.80404 |
| B | 5.4589 |
| B/Y | 0.30542 |
| C/Y | 0.49994 |
| M/Y | 0.028908 |
| N_W | 7.1134 |
| N_R | 1.5408 |
| dep ratio N^R/N^W | 0.21661 |

**Welfare at birth W₁(g,θ):** M-θL = −2.5695, M-θH = +0.0179,
F-θL = −3.4363, F-θH = −1.0505.

**Gate checks (spec §4):**

| # | Check | Result | Verdict |
|---|---|---|---|
| 1 | goods DIFF/Y < 1e−3 | −8.43e−5 | PASS |
| 2 | capital \|K−(A−B)\|/K < 2e−4 | 1.50e−4 | PASS |
| 3 | Euler max log10 < −3 | −4.75 (mean −6.92) | PASS |
| 4 | two-sex W differs (M≠F) | 33.7% gap | PASS (override propagated) |
| 5 | τp ≈ 0.1450 | 0.1083 | off-prediction — see below |
| 6 | K vs v3 stub 14.378 | 10.488 (−27%) | moved down — see below |

**Three deviations from the spec's ex-ante predictions, all substantive:**

1. **τp = 0.1083, not 0.1450.** The spec's 0.1450 used the demographic-only
   dependency ratio (0.290). The realized *mass-weighted equilibrium* dep
   ratio is 0.2166, and τp = κ·dep = 0.50 × 0.2166 = 0.1083 exactly. Model
   is internally consistent; the spec's guess used the wrong dep-ratio
   basis. **This 0.1083 is the value Run 0 pins.**
2. **K = 10.49, down 27% from the v3 stub 14.378** (spec guessed *up*). The
   genuine Milo female e_age (≈0.74× male at prime age) is lower than the
   old flat 0.85× stub → less female labor income → less aggregate saving →
   lower K. The 111% skill premium pushes K up but is outweighed.
3. **Two-sex welfare gap 33.7%, far above the spec's "5–10%"** — same root:
   the genuine female earnings disadvantage is much deeper than the 0.85
   stub the spec's prediction was written against.

All three trace to one cause: the real ENOE female profile is harsher than
the symmetric-stub 0.85 multiplier the spec's predictions assumed. None
indicates a solver error.

## 5. Run 0 — C2 interp-1 gate check: **OUTCOME A — infeasibility HOLDS**

Setup confirmed in run0.log: τp pinned = 0.108302 (from Run 1), n_p_2050 =
−0.019841, 2050 ψ installed (ψ_m[10]=0.9665, ψ_f[10]=0.9880), calibration
applied (θ_grid=∓0.3726, e_age[2,1:3]=0.8350,0.9726,1.0615).

Closure: `update_pension_taxes!` :fixed (τp pinned, benefits at calibrated
`pen = κ·w·L/N^W`, NOT scaled); `compute_debt!` interp-1 (pension_deficit =
pen_paid − pen_collected routed into primary; B = primary/(rⁿ−n_p)). Driver
throws `C2Infeasible` the first iter rⁿ−n_p < 0.

**Result: the GE loop diverged and tripped `C2Infeasible` at iteration 11.**
This is **Outcome A — the expected and desired result.** It confirms the
v3 §5.5.3 infeasibility survives the Mexican-data calibration.

GE trace (from run0.log / run0_history.csv; rⁿ = 0.8·r_5yr, n_p = −0.019841):

| iter | K | L | r (5yr) | rⁿ−n_p | primary | pension_deficit | B | B/Y |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 12.000 | 10.000 | +0.1634 | +1.506e−1 | +0.715 | 0.747 | +4.75 | +0.278 |
| 2 | 16.189 | 11.784 | +0.1209 | +1.166e−1 | +0.285 | 1.094 | +2.44 | +0.116 |
| 3 | 18.219 | 13.144 | +0.1183 | +1.145e−1 | +0.034 | 1.268 | +0.30 | +0.012 |
| 4 | 20.145 | 14.107 | +0.1094 | +1.074e−1 | −0.190 | 1.417 | −1.77 | −0.069 |
| 5 | 21.936 | 14.807 | +0.0988 | +9.887e−2 | −0.387 | 1.542 | −3.92 | −0.144 |
| 6 | 23.667 | 15.326 | +0.0871 | +8.948e−2 | −0.568 | 1.651 | −6.34 | −0.221 |
| 7 | 25.450 | 15.723 | +0.0741 | +7.912e−2 | −0.741 | 1.750 | −9.37 | −0.313 |
| 8 | 27.454 | 16.037 | +0.0592 | +6.720e−2 | −0.928 | 1.853 | −13.80 | −0.443 |
| 9 | 30.026 | 16.301 | +0.0405 | +5.225e−2 | −1.153 | 1.974 | −22.07 | −0.679 |
| 10 | 34.126 | 16.543 | +0.0133 | +3.045e−2 | −1.496 | 2.153 | −49.12 | −1.430 |
| 11 | 44.900 | 16.802 | −0.0421 | **−1.381e−2** | −2.347 | 2.568 | **+169.9** | +4.438 |

`*** C2Infeasible: rⁿ−n_p = −1.381e−02 < 0 at iter 11 ***`

**Mechanism (matches `C2_interp1_no_finite_SS.md` exactly):**
1. With τp pinned at 10.83% and benefits at the 2050 dependency ratio, the
   **pension deficit grows every iteration** (0.75 → 2.57) — it never closes
   because contributions are frozen below the PAYG-clearing rate.
2. The deficit drives the **primary surplus deep negative** (+0.72 → −2.35).
3. A negative primary forces **B negative and growing** (sign-flips at iter 4,
   reaches −49.1 by iter 10): the government holds an ever-larger asset/forces
   ever-larger K. **K climbs monotonically 12 → 44.9.**
4. Higher K depresses MPK, so **rⁿ falls toward n_p** (rⁿ−n_p: +0.151 →
   +0.030 → crosses to −0.0138 at iter 11).
5. At the crossing the debt fixed point **B = primary/(rⁿ−n_p) sign-flips and
   blows up** (−49 → +170) — the dynamic-inefficiency ricochet. DIFF/Y never
   approaches the 1e−4 gate (it stalls/worsens around −5e−2). No finite SS.

Same qualitative trajectory as the v3 symmetric-stub crash, now reproduced at
the calibrated parameters. (The crossing is later here — iter 11 vs v3's
iter 14 region — and via monotone K-climb rather than the v3 oscillation, but
the terminating condition rⁿ < n_p with B ricochet is identical.)

**Artifacts:** `results/run0.log` (iteration trace + gate result),
`results/run0_history.csv` (11 rows, K/L/r/primary/pension_deficit/B/B-over-Y
per iter; the per-iter `compute_debt!` capture worked — DIFF/Y column is NaN
because the GE history's DIFF is keyed to the loop's own iter count and the
final throwing iter has no post-throw DIFF, a cosmetic gap only).

## 6. Decision

**Outcome A + Run 1 sane → the §§4–5 reorder of Draft-June-v4 is VIABLE.**

Both conditions of spec §7 are met:
- Run 1 (calibrated 2020 baseline) converged cleanly; all hard gates pass.
- Run 0 (C2 interp-1) reproduced the infeasibility — rⁿ crosses n_p at
  iter 11, B blows up (−49 → +170), no finite SS — at the Mexican-data
  calibration.

**→ GREEN LIGHT for Runs 2–4** (κ-reform, τm-subsidy, aging C1 at the
calibrated baseline) in the next session. The §5.5.3 "do-nothing is
infeasible" headline holds under the calibration and can anchor the reorder.

**Numbers the §§4–5 rewrite should carry forward:**
- 2020 baseline (Run 1): K=10.49, Y=17.87, r=4.80%/yr, τp=10.83%,
  B/Y=30.5%, dep ratio=0.217. Welfare W₁: M-θL=−2.57, M-θH=+0.02,
  F-θL=−3.44, F-θH=−1.05.
- The calibrated K (10.49) is **27% below** the v3 symmetric-stub baseline
  (14.378), and the two-sex welfare gap is **~34%** (vs the stub's ~15%
  earnings gap) — both driven by the genuine Milo female e_age. The §4
  baseline narrative and any K/welfare numbers inherited from v3 must be
  updated to these values.
- For the §5.5.3 / Appendix infeasibility exhibit: the calibrated crossing is
  at iter 11, K reaches 44.9 before the throw, pension_deficit at crossing =
  2.57, B ricochets −49 → +170. `run0_history.csv` is the data for the
  three-panel diagnostic figure (K↑, rⁿ−n_p→0, B blowup).

**Open item flagged for the rewrite (not blocking):** the gate runs hold
ρ_AR, σ_ε, π_birth at the GE 2020 stubs rather than the calibration's
PE-anchor values (§3b). Decide during the §§4–5 rewrite whether to re-anchor
those three before the final Runs 2–4, or to document them as retained stubs.

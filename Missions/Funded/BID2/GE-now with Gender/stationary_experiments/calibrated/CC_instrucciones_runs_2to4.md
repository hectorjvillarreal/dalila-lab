# Claude Code Instructions — Runs 1'–4 at the Calibrated Baseline

**Repository:** `~/Dalila/Missions/Funded/BID2/GE-now with Gender/`.
**Spec predecessor:** `CC_instrucciones_gate_runs.md` (the gate session
that produced Run 1 and Run 0 → Outcome A). This session builds on the
gate result.

**Status going in:** the gate passed. Run 0 (C2 interp-1) reproduced the
infeasibility at the Mexican-data calibration (rⁿ crossed n_p at iter 11).
The reorder is viable. This session produces the §§4-5 numerical content.

**Deliverable:** Four stationary GE solves on `ge_model_gender.jl` at the
harmonized calibrated baseline:

- **Run 1'** — harmonized calibrated 2020 baseline (re-anchors ρ_AR,
  σ_ε, π_birth to the SMM PE-anchor values; supersedes the gate's Run 1).
- **Run 2** — κ pension reform (0.50 → 0.30) from Run 1'.
- **Run 3** — τm health subsidy (0 → −0.20) from Run 1'.
- **Run 4** — Aging C1 (2050 demographics, joint closure) from Run 1'.

These five columns (Run 1' baseline plus the three experiments plus the
already-completed Run 0 infeasibility) are the numerical content for the
reordered §§4-5 of `Draft-June-v4.tex`.

**Calendar.** ~7-10 hours of compute. Launch this evening for completion
overnight; §§4-5 LaTeX rewrite follows in a separate session once numbers
are in.

---

## 1. Permission and file access

Everything under `Missions/Funded/BID2/GE-now with Gender/` is readable
without asking. Reuse the working machinery from the gate session:
`stationary_experiments/calibrated/run1.jl` and `run0.jl` are the
templates — `run1.jl` especially, since Runs 1'–4 are variations on it.

**Files you may not edit:**
- `ge_model_gender.jl` (the solver).
- `Calibration/inputs_mxdata/` files.
- `Calibration/src/` files.
- Any `Draft-June-*.tex` (no LaTeX this session).

**Files you may create:**
- New driver scripts under `stationary_experiments/calibrated/`.
- Output CSVs and logs under `stationary_experiments/calibrated/results/`.
- A `runs_2to4_notes.md` documenting the session.

---

## 2. The harmonization change (Run 1')

The gate's Run 1 held three first-step inputs at the GE solver's 2020
stubs rather than the calibration's PE-anchor values:

| Input | Gate Run 1 (GE stub) | SMM PE-anchor (inputs_mxdata) |
|---|---:|---:|
| ρ_AR (productivity persistence) | 0.98 | 0.782 |
| σ_ε (innovation std dev) | 0.05 | 0.265 |
| π_birth (birth shares) | symmetric 0.25 | INEGI Census asymmetric |

Run 1' re-anchors all three to the PE-anchor values, so the §§4-5 baseline
matches what §7 reports as the calibration. Read the exact values from:

- `Calibration/inputs_mxdata/first_step/ar1_params.csv` (ρ_AR, σ_ε).
- `Calibration/inputs_mxdata/first_step/pi_birth.csv` (the 2×2 birth-share
  matrix — confirm it is the INEGI asymmetric set: M-low 0.3927, M-high
  0.1173, F-low 0.3822, F-high 0.1078, per the v4_notes).

**Important on the AR(1) re-anchoring.** The gender code discretizes the
AR(1) shock via Rouwenhorst (or Tauchen) into a finite grid. Changing ρ_AR
and σ_ε requires re-running that discretization, which the gender code does
at initialization. Confirm in the run log that the Rouwenhorst chain
re-built with the new (ρ, σ) — the gate runs printed "Initializing grids
and Rouwenhorst chain"; verify the chain reflects ρ=0.782, σ=0.265, not the
stub values. If the gender code reads ρ_AR and σ_ε from `const` declarations
that are inlined, the same re-`@eval` override pattern from the gate session
(`apply_calibration!()` re-`@eval`ing the leaf functions) must be extended
to cover the AR(1) discretization call. Inspect the source to confirm how
ρ_AR and σ_ε enter, and whether they propagate through the existing
override mechanism or need an extension.

**Gate for Run 1'.** Same six checks as the gate session, plus:

7. K vs gate Run 1 (10.488). The re-anchoring of ρ, σ_ε, π_birth may move
   K. Larger σ_ε (0.265 vs 0.05) means more idiosyncratic income risk →
   more precautionary saving → higher K. Asymmetric π_birth shifts the
   skill composition of cohorts. Report the new K and the direction of
   change. If K moves more than ~15% from gate Run 1, note it prominently
   — it means the harmonization is a material change and the §4 narrative
   must reflect Run 1' numbers, not gate Run 1 numbers.

If Run 1' converges cleanly and the gates pass, it becomes the canonical
baseline for Runs 2-4 and for §4 of the paper. Read its τp from
`run1prime_summary.csv` — this is the value Run 4's aging experiment uses
as its baseline-comparison anchor, and (if you later re-verify Run 0) the
value the C2 closures pin.

---

## 3. The four runs

All use the same calibrated parameters (six SMM scalars + Milo e_age + θ)
plus the harmonized ρ_AR, σ_ε, π_birth. They differ only in the policy or
demographic perturbation and the closure.

### Run 1' — harmonized calibrated 2020 baseline

- Parameters: calibrated (Ψ=13.4525, Ξ=0.274472, ξ=0.5 frozen,
  H̄₀=0.247474, h_slope=−0.035807, ζ_h=0.579138) + Milo e_age + θ=∓0.3726.
- Harmonized: ρ_AR=0.782, σ_ε=0.265, π_birth INEGI asymmetric.
- Demographics: 2020 (gender code default).
- Closure: joint (τp endogenous via PAYG balance, B residual).
- Outputs: `run1prime_summary.csv`, `run1prime_welfare.csv`,
  `run1prime_lifecycle.csv`, `run1prime.log`.
- ~2.5 hr.

### Run 2 — κ pension reform

- Same as Run 1' except κ: 0.50 → 0.30.
- Closure: joint.
- Outputs: `run2_kappa30_summary.csv`, `run2_kappa30_welfare.csv`,
  `run2_kappa30.log`.
- ~2.5 hr.

### Run 3 — τm health subsidy

- Same as Run 1' except τm: 0 → −0.20.
- Closure: joint.
- Outputs: `run3_taum20_summary.csv`, `run3_taum20_welfare.csv`,
  `run3_taum20.log`.
- ~2.5 hr.

### Run 4 — Aging C1

- Same as Run 1' except demographics substituted to 2050 via
  `demographic_experiment/demographics_2050.jl`.
- Closure: joint (τp endogenous, B residual — this is the C1 closure, NOT
  the C2 interp-1 of the gate run; C1 lets τp clear the PAYG block).
- Outputs: `run4_agingC1_summary.csv`, `run4_agingC1_welfare.csv`,
  `run4_agingC1.log`.
- ~2.5 hr.

**Note on what Run 4 is.** This is the *feasible* aging response — the one
where τp adjusts endogenously to clear PAYG as the dependency ratio rises.
It is the headline "τp rises under inaction" result. The C2 interp-1
infeasibility (already shown in Run 0) is the *other* closure where τp is
pinned and debt cannot close the gap. The paper's §5.5 reports both: Run 4
(C1, feasible, τp rises) as the cost-of-inaction headline, and Run 0
(C2 interp-1, infeasible) as the structural finding that pins down why
active policy is required.

---

## 4. Optimization: parallelization and ordering

**Dependency structure:** Run 1' must complete before Runs 2-4, because
all three perturbations start from Run 1' as their baseline (and the §5
tables report deltas from Run 1'). Runs 2, 3, 4 are mutually independent
once Run 1' is done.

**Recommended ordering:**

1. Run 1' alone, first. ~2.5 hr. Verify gates before proceeding. If Run 1'
   fails or moves K more than ~15% in a way that looks wrong, stop and
   report — do not launch Runs 2-4 on a questionable baseline.

2. Runs 2, 3, 4 in parallel. Three `-t 4` processes ≈ 12 cores on Dalila's
   16. The May 30 multistart ran four `-t 4` processes with ~12 min/eval
   contention; three should be milder. If three-way contention is a
   concern, run 2+3 in parallel then 4 alone (two waves).

```bash
cd ~/Dalila/Missions/Funded/BID2/GE-now\ with\ Gender/

# Wave 1: baseline
julia --project=stationary_experiments -t 4 stationary_experiments/calibrated/run1prime.jl \
    > stationary_experiments/calibrated/results/run1prime.log 2>&1
# verify gates, read τp, then:

# Wave 2: three experiments in parallel
for run in run2_kappa30 run3_taum20 run4_agingC1; do
    julia --project=stationary_experiments -t 4 stationary_experiments/calibrated/$run.jl \
        > stationary_experiments/calibrated/results/$run.log 2>&1 &
done
wait
```

**Project flag.** Use `--project=stationary_experiments`, NOT `--project=.`.
There is no `Project.toml` at the repo root (`GE-now with Gender/`); `--project=.`
from there resolves to an empty environment and the solver's `include` dies with
`Package OffsetArrays not found`. The instantiated env with OffsetArrays,
DynamicProgrammingUtils, and Roots lives at `stationary_experiments/Project.toml`.

**Total wall-clock:** ~2.5 hr (Run 1') + ~3-4 hr (Runs 2-4 parallel under
contention) ≈ **6-7 hr**. Sequential fallback ≈ 10 hr.

**Do not re-run Run 0.** The gate already passed. The C2 interp-1
infeasibility is established. If you want to verify Run 0 holds at the
harmonized baseline (with re-anchored ρ, σ_ε, π_birth), that is an optional
extra run — but the mechanism is robust and the gate verdict does not
change. Skip unless there is specific doubt.

---

## 5. Sanity gates

For every run:
1. DIFF/Y < 1e-3.
2. Capital market clearance < 2e-4.
3. Euler max log10 < −3 (mass-weighted bulk).
4. Two-sex welfare differential present (M ≠ F; expect ~30%+ at θ_L per the
   gate Run 1 finding).

For Run 2 (κ reform):
5. τp should *fall* relative to Run 1' (lower κ → lower contribution). The
   fall will be smaller in absolute terms than v3's 14.5→8.5 because Run 1'
   starts from a lower τp (~10.8%).
6. Welfare incidence should be regressive (θ_L loses proportionally more
   than θ_H). Report CEV-style proportional welfare changes by (g, θ).

For Run 3 (τm subsidy):
7. M/Y should *rise* relative to Run 1' (subsidized medical spending).
8. Welfare incidence should be progressive (θ_L gains proportionally more).
9. τp should rise slightly via the survival channel (longer lives → higher
   dependency).

For Run 4 (aging C1):
10. Dependency ratio should roughly double from Run 1' (the 2050 demographic
    shock). Report the actual ratio and the multiple.
11. τp should rise substantially (the headline). Report the Run 1' → Run 4
    τp change. The v3 result was a near-doubling; verify what the calibrated
    baseline produces.
12. K should rise (precautionary saving against longer retirement). r should
    fall. Report.

**Cross-run consistency check:** all four runs share Run 1' parameters and
the harmonized inputs. The only differences are the documented perturbations.
Confirm in each run log that the calibration applied correctly (the same
`CHECK` lines the gate runs printed: e_age, θ_grid, disutility, amenity).

---

## 6. What this session produces for §§4-5

After all four runs, assemble a single comparison table
`results/calibrated_comparison.csv` with columns: Run 1' (baseline), Run 2
(κ=0.30), Run 3 (τm=−0.20), Run 4 (aging C1). Rows: K, L, Y, r_annual, w,
τp, pen, B, B/Y, C/Y, M/Y, N_W, N_R, dep_ratio, plus the four welfare cells
W₁(M,θL), W₁(M,θH), W₁(F,θL), W₁(F,θH).

Also assemble a welfare-change table: for Runs 2, 3, 4, the proportional
welfare change relative to Run 1' by (g, θ). This is the §5 incidence content.

These two tables plus Run 0's `run0_history.csv` (already produced) are the
complete numerical input for the §§4-5 LaTeX rewrite.

---

## 7. Decision points

**If Run 1' converges and gates pass:** proceed to Runs 2-4. Standard path.

**If Run 1' moves K more than ~15% from gate Run 1 (10.488):** the
harmonization is material. Proceed, but flag prominently in
`runs_2to4_notes.md` that the §4 baseline numbers differ substantially from
the gate's Run 1, and that the §4 narrative must use Run 1' values. Report
the decomposition: how much of the K change is from σ_ε (precautionary
saving), how much from π_birth (cohort composition).

**If Run 1' fails to converge:** likely the AR(1) re-discretization with
the larger σ_ε (0.265 is a big innovation std dev at 5-year frequency)
destabilized the household solve. Diagnose. If the larger σ_ε is the cause,
report it — it may indicate the PE-anchor σ_ε is too large for the GE solve,
which is itself a finding worth flagging for the §7 calibration discussion.
Do not force convergence by editing the solver. Fall back to the gate's
Run 1 (un-harmonized) as the baseline and document the harmonization as a
September item.

**If any of Runs 2-4 fails:** report which and why. Runs 2 and 3 are mild
perturbations and should converge readily from Run 1'. Run 4 (2050
demographics) is the more demanding solve; if it fails, check whether it is
the same infeasibility mechanism (rⁿ crossing n_p) — but under the C1
closure (τp endogenous) it should NOT hit that, because τp is free to clear
PAYG. If Run 4 fails under C1, that is a surprising result worth reporting
carefully.

---

## 8. Pre-flight and post-flight

**Pre-flight:**
- [ ] Read `ge_model_gender.jl` to confirm how ρ_AR, σ_ε enter (const
      scalars? read at Rouwenhorst init?) and whether the existing override
      pattern propagates them.
- [ ] Read `inputs_mxdata/first_step/ar1_params.csv` and `pi_birth.csv` for
      the harmonized values.
- [ ] Confirm `stationary_experiments/calibrated/run1.jl` is available as a
      template.
- [ ] Tag the repo state.

**Post-flight:**
- [ ] `run1prime_summary.csv`, `run1prime_welfare.csv`,
      `run1prime_lifecycle.csv` exist.
- [ ] `run2_kappa30_*`, `run3_taum20_*`, `run4_agingC1_*` exist.
- [ ] `calibrated_comparison.csv` assembled.
- [ ] Welfare-change table assembled.
- [ ] All gates documented in `runs_2to4_notes.md`.
- [ ] Console summary with the headline numbers for each run.
- [ ] `runs_2to4_notes.md` flags the harmonization K-change decomposition
      and any deviations.

# Calibration/ — SMM scaffold for the Modelmay PE solver

Internal-calibration pipeline for the gender-extended OLG model
(`modelwithgender.tex` §4). **The scaffold is built but no calibration has
been run yet** — placeholders stand in for the first-step regression
outputs and the data-side targets. Plug in the real CSVs and execute.

## Why partial equilibrium, not GE

The paper says (§4.2.3) "the model is solved at each candidate Θ as a full
stationary equilibrium." We deviate by solving in **partial equilibrium**
with prices fixed at an anchor:

| | Per-call wall-clock | SMM at ~200 trials |
|---|---|---|
| GE-Fast-Gender | ~62 min | ~200 hours |
| Household-Gender (PE) | ~9 min | ~30 hours |

The full GE re-anchoring loop (PE-SMM → GE-solve → update anchor → repeat)
is the principled fix, but the deviation is small in practice: at Θ̂ the
final GE solve will move prices very little if the anchor is reasonable.
Re-anchor once at the end and check.

## Deviations from the paper (declared)

1. **PE not GE.** Prices fixed at `inputs/config/pe_anchor.csv` (default:
   converged GE-Gender gender-gap baseline).
2. **6 params, 6 moments** (paper has 7). $K/Y = 3.0$ is dropped — it's an
   aggregate ratio of household assets to firm-side output, and PE has no
   firm side. $\beta$ is fixed externally at $0.998^5$.
3. **Moments computed directly from $\Phi$ + policies, not from $N=50{,}000$
   panel sims per type.** Mathematically these are the same population
   values; direct computation just removes the Monte Carlo noise. The
   objective is smoother as a result — an improvement, not a compromise.

## The six parameters and their targeted moments

| Param | Paper name | Code Ref | Targeted moment |
|---|---|---|---|
| `Psi` | $\Psi$ | `Ψ_labor[]` | hours of prime-age males = 1/3 |
| `Xi` | $\Xi$ | `Ξ_amenity[]` | VSL = \$11.6M (2022 USD) |
| `xi` | $\xi$ | `ξ_curv[]` | cross-sectional income elasticity of $m$ |
| `H_0` | $\bar H_0$ | `H_scale[]` | mean medical spending, age 25–35 |
| `h_slope` | $h^{\mathrm{slope}}$ | `h_slope[]` | log-slope of mean $m$, age 25–75 |
| `zeta_h` | $\zeta_h$ | `H_curv[]` | within-age income elasticity of $m$ |

## Input contract

Drop the user-provided values into these CSVs and the pipeline just runs.
The committed templates contain the current Household-Gender stubs so the
scaffold is runnable on day 1 — replace each CSV as the corresponding
empirical work completes.

```
Calibration/inputs/
├── first_step/
│   ├── e_age.csv          # 17 rows × (male, female) — age-efficiency profile e^g_j
│   ├── psi_base.csv       # 17 rows × (male, female) — baseline survival ψ^g_j
│   ├── delta_h.csv        # 17 rows × value — health depreciation δ^h_j
│   ├── pi_birth.csv       # 4 rows: sex × theta × share — π^{g,θ}_1, summing to 1
│   ├── skill_params.csv   # 2 rows: theta_idx, theta, rho_pen — (θ_L, θ_H, ϱ(θ))
│   └── ar1_params.csv     # 2 rows: rho, sigma_eps — AR(1) on η
├── moments/
│   └── targets.csv        # 6 rows: name, value, se — empirical moment targets + SEs
└── config/
    ├── pe_anchor.csv      # 4 rows: r, w, tau_p, pen — fixed prices for PE
    ├── theta_init.csv     # 6 rows: param, init, lb, ub, transform — SMM starting values
    ├── usd_scale.csv      # 3 rows: usd_per_unit_c, periods_per_year, ref_age_period (VSL)
    └── grids.csv          # NA, NH, Nm, refine_m, verify (numerical settings)
```

## Source layout

```
Calibration/src/
├── pe_solver_for_smm.jl   # PE solver with the 6 SMM params + 4 prices as Ref{}
├── load_inputs.jl          # CSV → typed NamedTuples
├── moments.jl              # 6 moments computed from Φ + policies
├── vsl.jl                  # VSL formula (β · E[V']/u_c at reference age)
├── objective.jl            # weighted-distance objective + bounds transforms + eval log
├── optimizer.jl            # Nelder-Mead (Optim.jl) with multistart
└── diagnostics.jl          # numerical Jacobian, sandwich SEs, plots
```

## How to run

The driver dispatches on the first CLI argument:

```bash
# Smoke — loads inputs, solves PE at theta_init using the GE-Gender anchor
# (pe_anchor.csv), computes the 6 moments, evaluates the objective, runs 3
# trial evaluations, does one finite-difference step. ~60 min wall-clock
# (5 PE solves). Use this to validate any input-CSV swap.
julia --project=. -t 4 Calibration/run_calibration.jl smoke

# Parity — solves PE with Household-Gender's *hardcoded* prices (r=0.159,
# w=1.00, τp=0.10, pen=0.30) and diffs the cohort-mean CSV against
# ../Household-Gender/household_lifecycle_gap.csv. Must agree to ~1e-10 —
# this validates the Ref-refactor is algorithm-identical to the reference
# PE solver. ~15 min wall-clock (1 PE solve). Run this once after any change
# to pe_solver_for_smm.jl.
julia --project=. -t 4 Calibration/run_calibration.jl parity

# Numerical Jacobian at theta_init — smoke + 13 PE solves (~2.5 h total).
# The first identification diagnostic: each row should respond to at least
# one parameter, and each column should move at least one moment.
julia --project=. -t 4 Calibration/run_calibration.jl jacobian

# Full multistart Nelder-Mead. ONLY run once real first-step inputs and
# real target moments are in place — placeholder targets aren't economically
# meaningful and convergence will not be informative. ~12+ hours.
julia --project=. -t 4 Calibration/run_calibration.jl multistart
```

Outputs land under `Calibration/outputs/`:

| File | Mode that produces it | Contents |
|---|---|---|
| `parity_lifecycle_fromsmm.csv` | `smoke` | cohort means for the parity diff against Household-Gender |
| `moments_at_stub.csv` | `smoke` | the 6 moments at `theta_init`, vs targets |
| `eval_log_*.csv` | all | one row per objective evaluation |
| `theta_hat.csv` | `jacobian`, `multistart` | (param, estimate, se, t-stat) |
| `moment_match.csv` | `jacobian`, `multistart` | (moment, data, model, diff, t-stat) |
| `jacobian.csv` | `jacobian`, `multistart` | the full 6×6 sensitivity matrix |
| `diagnostics/01_moment_match.png` | `jacobian`, `multistart` | bar chart of t-stats |
| `diagnostics/02_jacobian.png` | `jacobian`, `multistart` | column-normalized heatmap |
| `diagnostics/03_objective_trace.png` | `jacobian`, `multistart` | Q over evaluation index |

## Verification — what each mode checks

**`smoke` runs six gates** — non-fatal if individual moments look off (those
are economic, not pipeline), but errors out on a real plumbing failure:

1. **Inputs load** — all 11 CSVs parse, shapes match the model dimensions.
2. **PE solve** — `solve_pe_at!` runs end-to-end at `theta_init`.
3. **Moments are finite + sensible** — all 6 moments evaluate to finite
   numbers; hours ∈ (0,1), VSL > 0, log-slope finite.
4. **Objective is finite and positive** — `Q(theta_init) > 0`.
5. **`SmmObjective` works** — 3 evaluations log correctly to `eval_log_smoke.csv`.
6. **Finite-difference works** — one Jacobian column is finite.

**`parity` is the pipeline-correctness gate** — it should pass to ≤ 1e-10 if
the Ref-refactor preserved algorithm-identity with `Household-Gender/`. The
diff is computed against `../Household-Gender/household_lifecycle_gap.csv`
under Household-Gender's hardcoded PE prices (NOT the `pe_anchor.csv`
defaults). A failure here means the Ref-refactor has a bug; a smoke pass
combined with a parity fail is the worst case to investigate.

## After convergence: the GE re-anchor check

The paper assumes prices clear at Θ̂. We don't enforce this during SMM. To
verify the deviation is small, after `multistart` completes:

1. Copy `theta_hat.csv` values into a temporary modification of
   `GE-Fast-Gender/ge_model_gender_fast.jl` (`Ψ_labor`, `Ξ_amenity`, ...).
2. Run the full GE solve (~1 hour).
3. Compare the resulting equilibrium $(r, w, \tau^p)$ to `pe_anchor.csv`.
4. If they differ by more than ~5%, update `pe_anchor.csv` with the GE
   prices and re-run `multistart`. Usually 1–2 iterations of this outer
   loop converge.

## Open follow-ups

- **Country-specific runs.** Once Mexico / Costa Rica / Panama first-step
  regressions land, create `Calibration/inputs_mx/`, `inputs_cr/`,
  `inputs_pa/` and pass the path to `load_all_inputs(base_dir)`.
- **`/SMM-Audit` skill.** The Macro-skills folder has an SMM audit; once a
  calibration converges, run it against this codebase.
- **Robustness sensitivity.** The user separately wants to know whether
  the paper's calibration strategy is itself "sensitive" — the
  `jacobian.csv` + `moment_match.csv` outputs above are the first read on
  this. Beyond that, the standard play is to drop one moment at a time
  and see whether Θ̂ moves materially.

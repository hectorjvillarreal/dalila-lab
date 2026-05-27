# Stationary policy experiments — operating notes

Two stationary GE solves on the gender code (`../ge_model_gender.jl`) for the
seminar paper: **§6.1 pension reform** (κ: 0.50→0.30) and **§6.2 health
subsidy** (τ^m: 0→−0.20), both re-run on the same baseline as the aging
experiment (RUN 1) so §§5–6 are internally consistent on one code, one baseline.

Spec: `CC_instrucciones_stationary_experiments.md` (one level up). Run completed
2026-05-27. Baseline is **not** an independent result — it reproduces aging
RUN 1 and exists here as the warm-start verification gate + the M/Y reference
the τm gate needs.

## Headline table

| | Baseline | κ=0.30 | τ^m=−0.20 |
|---|---|---|---|
| K (capital) | 14.382 | 16.479 | 15.039 |
| Y (output) | 24.514 | 26.534 | 24.966 |
| r (annual) | 4.81% | 4.24% | 4.54% |
| w (wage) | 0.988 | 1.020 | 1.003 |
| τ^p | 14.50% | 8.53% | 14.90% |
| pen | 1.064 | 0.691 | 1.084 |
| B/Y | 28.29% | 31.09% | 21.11% |
| C/Y | 47.74% | 46.77% | 46.86% |
| M/Y | 5.22% | 4.39% | 5.86% |

Welfare at birth W₁(g,θ):

| | Baseline | κ=0.30 | τ^m=−0.20 |
|---|---|---|---|
| M, θL | 3.4824 | 3.3645 | 3.5518 |
| M, θH | 4.1434 | 4.0772 | 4.2062 |
| F, θL | 3.3210 | 3.1345 | 3.4041 |
| F, θH | 3.9652 | 3.8330 | 4.0396 |

Reading: lowering κ raises private saving (K↑, r↓) and cuts the PAYG rate
(τ^p 14.5→8.5%), but lowers welfare across all four types (smaller pension
dominates). The medical subsidy raises medical spending (M/Y 5.2→5.9%) and
welfare across all types; τ^p ticks up slightly (14.5→14.9%) as a GE effect.

## Gates (§5)

| Gate | Result |
|---|---|
| [1] goods market DIFF/Y < 1e-3 | **PASS** (base +9.2e-5, κ −9.8e-5, τm +7.8e-5) |
| [2] Euler max log10 < −3 | **PASS** (base −4.83, κ −5.52, τm −4.97) |
| [4] κ=0.30 → τ^p falls | **PASS** (14.50% → 8.53%; cf. Integrated_7 13.81→8.13%) |
| [5] τm=−0.20 → M/Y rises | **PASS** (5.22% → 5.86%) |
| [6] symmetric identity \|M−F\|<1e-6 | **FAIL — expected, see below** |

**Gate [6] is inapplicable, not a defect.** The model runs with
`gender_gap = true`, so the baseline carries a genuine sex gap
(\|M−F\| ≈ 0.16–0.18) — identical to aging RUN 1's, confirming faithful
reproduction. The spec's §1/§5/§8 "symmetric-stub" framing is inconsistent
with its own instruction to anchor on aging RUN 1 (K=14.378), which was run
with the gap on. These experiments therefore deliver a real (non-degenerate)
sex decomposition now, rather than the degenerate one §8 deferred to September.
A true symmetric version would require `gender_gap=false` and would **not**
reproduce K=14.378.

## How it was run

Sequential, two Julia processes (`JULIA_NUM_THREADS=8`), warm-started from
RUN 1 (K=14.378, L=15.870):

```
julia --project=. run_kappa.jl   && \
julia --project=. run_taum.jl    && \
julia --project=. assemble_comparison.jl
```

- `stationary_lib.jl` — shared setup. `init_model!()` (grids + Rouwenhorst +
  ergodic dist), the `active_τω` shim + redefined `labor_supply` /
  `available_resources`, the `:endogenous` pension / `:residual_B` debt
  closures. All ported **verbatim** from the proven
  `../demographic_experiment/run_aging_ssvs.jl`.
- `run_kappa.jl` — baseline (κ=0.50; asserts K≈14.378) then κ=0.30.
- `run_taum.jl` — τm=−0.20 in its own process.
- `assemble_comparison.jl` — table + gates → `stationary_comparison.csv`.

### Override strategy (κ_rep and τm are `const`)

On Julia 1.11 a `const` redefinition does not propagate into already-compiled
methods (the n_p/ψ_base lesson, documented in the aging driver). Handled
per-parameter:

- **κ_rep** enters only `update_pension_taxes!` → overridden by **redefining
  that function** with κ baked in (`set_pension_kappa!`). Household behavior
  sees κ only via `wn_now`/`pen_now`, so this is complete and in-process safe.
- **τm** enters the **cell solver directly** (budget
  `c=(X−a′−(1+τm)m)/(1+τc)`), which compiles once. So τm is set via const
  redefinition in a **fresh process before the first solve**, baking it at
  first compile. Confirmed: `taum.log` reports `τm = -0.2000` at init.

## Deviations from the spec

1. **Spec §3/§4 template was non-functional as written** and is not used.
   A bare `include` + `solve_ge!()` (i) skips grid/Markov init → diverges, and
   (ii) is an unconfigured solve (τ^p stuck at its 0.10 init). See
   `attempt1_baresolve_FAILED.log` for the divergence. The architecture above
   replaces it.
2. **Two processes, not one** (§3c said one driver). Forced by the τm const
   hazard — κ and baseline use τm=0; the subsidy run needs τm=−0.20 baked at
   compile, which requires a separate process. Run sequentially (not parallel),
   per §3c's thread-contention guidance.
3. **Warm-start helper uses the real symbols** `K_init`/`L_init` (§4 template's
   `K_0_init`/`L_0_init` do not exist → would silently no-op).
4. **CONTROL skipped** (§3b); the baseline warm-start gate replaces it.

## Files

- `results/stationary_comparison.csv` — three-column table (canonical).
- `results/{baseline,kappa30,taum20}_results.csv` — per-run, field,value.
- `results/{kappa,taum,assemble}.log` — full console logs.
- `results/attempt1_baresolve_FAILED.log` — the divergent first attempt (kept
  as provenance of the §3/§4 template defect).

Repo tagged `pre-stationary-experiments-20260526` before the run for clean
revert.

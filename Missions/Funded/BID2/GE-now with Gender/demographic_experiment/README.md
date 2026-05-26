# demographic_experiment — Aging comparative steady state

Headline figure for the **IDB seminar 2026-06-05**. Two stationary GE solves
(2020 baseline vs 2050 demographic structure) under three fiscal closures,
to decompose the long-run fiscal pressure of aging into a pension-side and
a debt-side piece.

Full specification: `CC_instrucciones_aging_steady_state.md` (read it first
if you are touching closures or pinning logic).

## What this experiment is — and is not

- **Is**: comparative *steady state*. Two stationary equilibria differing
  only in `n_p`, `ψ_base_male`, `ψ_base_female`. Everything else
  (preferences, technology, taxes, κ, GHH parameters, `e_age`) is held at
  the 2020 calibration.
- **Is not**: a transition path. The 2050 numbers are the SS the economy
  converges to under unchanged policy with a full generation to reoptimize.
  Upper bound on the welfare incidence of aging; not a fiscal forecast.

## Files

| File | Role |
|---|---|
| `CC_instrucciones_aging_steady_state.md` | Full spec (§1–§11). Authoritative. |
| `demographics_2050.jl` | Mexico 2050 demographic primitives (Anne, 2026-05-24). |
| `run_aging_ssvs.jl` | Full driver (RUN 1, CONTROL, RUN 2 = C1). Overrides primitives + closures at runtime. |
| `run_aging_c2_recovery.jl` | Standalone C2 driver (interp 2: benefit-scaling). Uses `Base.invokelatest`. |
| `diagnose_gender_gap_euler.jl` | Locate the gender-gap Euler spike (≈ 1–2 min threaded; 12 min single-thread). |
| `probe_ge_iter1.jl` / `probe_ge_iter1_via_driver.jl` | One-iter probes used to isolate the uninitialized-grids bug. |
| `C2_interp1_no_finite_SS.md` | Paper-motivation finding: C2 with "debt absorbs" admits no finite SS at 2050. |
| `results/` | CSV + welfare-panel PNG outputs. Created on first run. |
| `diagnostics/` | Per-cell residual dumps from `diagnose_gender_gap_euler.jl`. |
| `README.md` | This file. |

`run_aging_ssvs.jl` **does not edit** `../ge_model_gender.jl`. It `include`s
it, then redefines `n_p`, `ψ_base`, `update_pension_taxes!`, `compute_debt!`
as needed. The `if abspath(PROGRAM_FILE) == @__FILE__` guard in
`ge_model_gender.jl:1172` prevents the include from triggering its `main()`.

## How to run

From `GE-now with Gender/`:

```bash
julia -t auto --project=demographic_experiment demographic_experiment/run_aging_ssvs.jl
```

`-t auto` is required for the threaded household solve (~12.9× on
Dalila's 16 cores per Diego's `ge_model.jl` benchmark; gender-gap
should be similar). Single-thread fallback is ≈ 2.5 h per GE solve;
threaded should land near 12 min. With default toggles
(`RUN_CONTROL = true`, `RUN_C3 = false`): 4 solves ≈ **45–60 min**
threaded vs ~10 h single-thread. Still run in Zellij — see
`CLAUDE.md` §3.

Outputs land in `results/`:
- `aging_comparison{_gap}.csv` — one row per run, all reported scalars.
- `welfare_panel{_gap}.png` — 2×2 grid of W₁(g,θ) bars by scenario.

The `_gap` suffix is appended iff `ge_model_gender.jl` has `gender_gap = true`.

## Toggles (top of `run_aging_ssvs.jl`)

| Constant | Default | Meaning |
|---|---|---|
| `RUN_CONTROL` | `true` | Smoke-test the override pattern: run 2020 again via `set_demographics!` and verify it matches RUN 1. Recommended on first execution and after any Julia upgrade. |
| `RUN_C3` | `false` | Run the debt-pinned closure (B fixed, τ^ω clears the general budget). Requires both `available_resources` and `labor_supply` to read `active_τω`; both are wired up. Turn on only after C1/C2 are validated. |

`gender_gap` is set inside `ge_model_gender.jl` and is **not** overridable
from this driver (it controls `e_age` and `ψ_base` at module-load time).
Run a symmetric baseline (`gender_gap = false`) and a gap baseline
(`gender_gap = true`) as two separate Julia sessions if both are needed.

## Pre-flight checklist (spec §11)

- [x] Anne delivered `n_p_2050`, `ψ_base_male_2050`, `ψ_base_female_2050`
      (WPP 2024 medium variant, Brass-logit shift; see header of
      `demographics_2050.jl`).
- [ ] Override pattern smoke-tested (CONTROL run inside
      `run_aging_ssvs.jl` does this; gate: |ΔK| < 1e-3, |Δτp| < 1e-4
      vs RUN 1).
- [x] Gender-gap Euler residual issue diagnosed (2026-05-24,
      `diagnose_gender_gap_euler.jl`). Interior max log10 = **−7.482**,
      mass-weighted interior max = **−9.141** — both pass the spec §6
      `< −3` gate. The spec's quoted `−1.18` was from an earlier source
      revision before inline Brent + m\* refinement; current
      `ge_model_gender.jl` numerics are reportable as-is. Welfare-by-sex
      numbers are usable.
- [ ] Git tag created on the GE source state before the long run.

## Post-run notes

Fill in after each invocation. Append, do not overwrite.

### Run YYYY-MM-DD HH:MM — `<gender_gap mode>`

- Wall-clock:
- Iterations per run (1 / CTRL / C1 / C2 / C3):
- DIFF/Y at convergence:
- Euler max log10:
- CONTROL residuals (|ΔK|, |Δτp|):
- Pinning checks (C2: τp − τp_2020; C3: B − B_2020):
- Reportable runs:
- Deviations from spec encountered:
- Notes for the seminar slides:

## Implementation deviations from `CC_instrucciones_*.md`

Tracked here so the spec stays canonical and the driver stays inspectable.

1. **`active_τω` Ref instead of per-closure swaps of household functions.**
   Spec §4 says C3 needs `available_resources` redefined to read
   `τω_endog`; in fact `labor_supply` also depends on τw via the GHH FOC
   and would also need to be swapped. To keep both consistent and avoid
   method-overwrite warnings on each closure switch, the driver redefines
   both functions *once* at load time to read `active_τω[]` (a typed
   `Ref{Float64}`), and the closure switches just mutate the Ref. In
   `:residual_B` mode `active_τω[] == τw`.

2. **No call to `diagnostic_gates`.** Spec §6 calls for hard sanity
   gates after each run. `diagnostic_gates()` from `ge_model_gender.jl`
   asserts `euler_max < -1.0` and would halt the script on the
   known gender-gap residual spike. Instead, `run_one` records `DIFF` and
   `euler_max` per run and the seminar table prints ✔ REPORT / ⚠ DO NOT
   per the §6 thresholds (DIFF/Y < 1e-3, Euler < −3). Add the hard gates
   back once the gap-mode Euler issue is resolved.

3. **Output suffix follows the GE source convention.** CSVs and the
   welfare PNG get `_gap` when `gender_gap = true`. A symmetric and a
   gap run can coexist in `results/` without overwriting.

4. **Directory named `demographic_experiment/`, not `aging-experiment/`.**
   Cosmetic — pre-existed when the driver was written.

5. **Threading patch applied to `ge_model_gender.jl`** (deliberate spec
   deviation). Ported from `draft_260519/ge_model.jl` commits 054687c
   (`Threads.@threads` on the inner cell loop in
   `solve_household_for_type`) and f3110c1 (per-thread `linint_Grow`
   scratch buffers; also converted `n_refined` to `Threads.Atomic{Int}`
   since the Gender file has m\* parabolic refinement that increments
   it from inside the threaded loop). Required `-t auto` at the Julia
   command line to actually benefit. Verified by parse-check; first
   threaded GE solve will validate against the existing symmetric
   `ge_summary.csv` to ~3 decimals as a sanity gate.

6. **GE-loop robustness patches also ported from 054687c.** `damp_ge`
   lowered from 0.50 to 0.30 and positivity floors `max(K_upd, 0.5)` /
   `max(L_upd, 0.5)` added in `solve_ge!`. Needed because gender_gap =
   true effectively acts as a policy shock vs the symmetric calibration
   — women's e_age × 0.85 drops L_target sharply at iter 1, and damp =
   0.50 then overshoots K_target negative at iter 3, crashing the firm
   FOC `(K/L)^(α-1)`. Symmetric behavior unchanged (still converges in
   ~13 iters per the existing log).

7. **`n_p` and `ψ_base` changed from `const` to TYPED GLOBAL.** The spec's
   override pattern (`@eval Main begin const n_p = ... end`) emits a
   warning under Julia 1.11.7 *and* updates the binding — but compiled
   methods that previously inlined the const value keep the old value.
   First full-run attempt confirmed this empirically: RUN 2 (C1, supposedly
   2050 demographics) converged to bit-identical equilibrium as RUN 1
   (2020), because `forward_distribution!` / `survival()` kept the
   inlined 2020 `n_p` / `ψ_base`. Fix: declare them as typed globals
   (`n_p::Float64 = ...`, `ψ_base::Matrix{Float64} = ...`), which the
   compiler does NOT inline. `set_demographics!` now uses
   `setglobal!(Main, :n_p, …)` instead of `@eval const`. Verified by
   smoke-test before relaunch (override n_p → −0.020, compiled function
   returns new value).

8. **Grid initialization moved into the driver.** `grid_Cons_Grow`,
   `rouwenhorst`, `compute_ergodic!` were inside
   `ge_model_gender.jl::main()`, which the `PROGRAM_FILE` guard prevents
   from firing under `include`. Without these calls, `π_η_erg` is the
   const-init zeros, `forward_distribution!` seeds `Φ` as all-zero,
   aggregates collapse to zero, and `solve_ge!` diverges within one iter.
   Now done at the top of `main()` in `run_aging_ssvs.jl`.

## Open items

- **Gender-gap Euler max.** Production gap run shows `log10 max = -1.18`
  on Diego's machine; welfare-by-sex numbers cannot be reported until
  this is resolved. Working hypothesis (see `diagnose_gender_gap_euler.jl`
  header for the full reasoning): the spike concentrates on
  *(j ≥ J−2, female, low-η, near-corner-a' or near-zero-m)* cells with
  negligible mass, amplified by women's high ψ into bands 14–17 combined
  with `expected_uc_next` interpolating `c` then taking `uc = z^(-2)`
  (biased estimator of E[uc] under high curvature). If confirmed, fix is
  to report a mass-weighted max alongside the raw max (the source's own
  comment at `ge_model_gender.jl:938-942` already foreshadows this). If
  the spike has non-trivial mass, the deeper fix is to interpolate `uc`
  directly or refine the m grid at old ages. Run
  `diagnose_gender_gap_euler.jl` (≈ 12 min, one household solve at
  symmetric prices) to verify before committing to a fix.
- **C3 convergence under damped τω.** `active_τω` is updated each GE
  iter from current C, L, K, M without separate damping; relies on the
  K,L damping (damp_ge = 0.5) to carry the joint fixed point. If C3 fails
  to converge or oscillates, drop it for June 5 (spec §4 explicitly
  permits) and present C1 + C2 only.
- **Sex-specific 2020 baseline.** `ψ_base` in `ge_model_gender.jl` is
  currently pooled by sex (a stub). When sex-specific 2020 life tables
  land, re-derive `demographics_2050.jl` from sex-specific baselines
  (per its own header note).

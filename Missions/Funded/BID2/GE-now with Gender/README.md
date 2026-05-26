# GE-Gender — stationary GE solver, gender extension (Modelmay)

Full stationary general-equilibrium solver for the **gender extension** of the
DraftApril OLG model. Four agent types $(g,\theta)\in\{m,f\}\times\{\theta_L,
\theta_H\}$.

Built by copying `GE/ge_model.jl` (DraftApril GE, no gender) and threading a sex
dimension `ig` through every array, function, and loop — then grafting in the
household-block improvements already verified in `Household-Gender/`:
inline Brent root-finder, m\* parabolic refinement, hard `@assert` diagnostic
gates. **The DraftApril solvers are never edited.**

## Files

| File | Purpose |
|---|---|
| `ge_model_gender.jl` | The solver. |
| `ge_run.log` | Live run log. |
| `ge_lifecycle.csv`, `ge_summary.csv`, `ge_history.csv` | Outputs. |
| `plots/` | 6 GE audit plots. |
| `audits/` | Audit artifacts. |

## How to run

```bash
# from the repo root
julia --project=. GE-Gender/ge_model_gender.jl
```

Runtime ≈ 2–2.5 h (the GE fixed-point loop is ~13 iterations, each a full
four-type household solve).

## What it solves

The outer GE loop iterates capital `K` and effective labor `L` to a fixed point.
Each iteration:

1. Firm FOCs set prices `(r, w)` from `(K, L)`.
2. The four-type household problem is solved by backward induction.
3. The distribution `Φ` is propagated forward — with the `1/(1+n_p)`
   population-growth factor (`modelwithgender.tex` eq. `cohort_weights`), which
   the PE `Household-Gender` solver deliberately omits.
4. Aggregates `(K, L, C, M, Λ_void, N^W, N^R)` are formed over all four types.
5. The pension contribution closes endogenously: `τ^p = κ N^R/N^W`; debt `B`
   closes the government budget as a residual.

Endogenous: `r, w, τ^p, pen, B`. Fixed: tax rates, `g_y`, `κ`, `α, δ, A`, `n_p`.

## What differs from DraftApril GE

1. **Sex dimension** — all 7 arrays go 5-D → 6-D, `(j, ig, ia, ih, is, iθ)`.
2. **J = 16 → 17** (ages 20–100).
3. **Sex-specific primitives** — `e_age`, `ψ_base` as `2×J` matrices; `δh` a
   length-`J` vector; `π_birth` a `2×2` matrix.
4. **`ig` loops** in `aggregate_all` and `compute_population!`; `welfare_at_birth`
   returns a `2×Nθ` array (four welfare numbers + a birth-share-weighted aggregate).
5. **Inline Brent**, **m\* parabolic refinement**, **`diagnostic_gates()`** —
   ported from the audited `Household-Gender` solver.

## Stubs (men ≡ women until calibration §4)

`e_age`, `ψ_base` identical across sexes; `π_birth` all four types `0.25`;
`h_slope = 0`; `ψ_base[·,17]`, `δh[17]` extrapolated.

## Verification status (2026-05-22)

**CONVERGED at iter 13. All gates pass.** Equilibrium (`ge_summary.csv`):

| Quantity | GE-Gender | DraftApril GE |
|---|---|---|
| K | 15.258 | 15.24 |
| L | 17.602 | 17.60 |
| K/L | 0.867 | 0.866 |
| r (5-yr) / annual | 0.282 / 5.1% | 0.283 / 5.1% |
| w | 0.973 | 0.972 |
| τp | 0.139 | 0.138 |
| C/Y, M/Y, G/Y, Λ_void/Y | 48.7%, 4.80%, 19.0%, 4.71% | 48.7%, 4.8%, 19%, 4.7% |
| B | 7.36 | 7.35 |

With symmetric stubs GE-Gender **collapses to DraftApril GE to ~3 decimal
places** — exactly the sanity benchmark the plan called for.

**Diagnostic gates** (all pass):

| Gate | Value | Threshold |
|---|---|---|
| Goods market `DIFF/Y` | −3.4e-5 | < 1e-4 |
| Capital market \|K − (A_dom − B)\|/K | 5.7e-6 | < 1e-3 |
| Government BC residual / Y | 0.0 | < 1e-6 |
| Budget residual (cell) | 8.0e-6 | < 1e-4 (GE iter-order) |
| Two-sex identity (men ≡ women) | 0.0 | < 1e-10 |
| Cohort-share invariant | 1.7e-15 | < 1e-8 |
| Newborn mass ΣΦ[1] | 1.000000000000 | ≈ 1 |
| Terminal a',m,ℓ at j=J | 0.0 | = 0 |
| Euler residual log10 max | −5.47 | < −3 |
| Asset-top mass share | 0.0 | < 1e-3 |

**One nuance** flagged honestly: the budget-residual gate is `1e-4` in GE
(not the PE `1e-8`) because `update_pension_taxes!` is called once more
*after* the final `solve_household!`, so the stored policies use a slightly
different `τp` than the post-iteration globals — the gap is `w·ν·ℓ·Δτp ≈ 8e-6`,
machine-precision economically. This is documented in
`ge_model_gender.jl:diagnostic_gates`.

Runtime: 2 h 28 min wall-clock for the full 13-iteration GE loop.

## Not in scope

`GE-Fast-Gender/` (already fast here via the inline Brent) and the plug-in of
calibrated sex-specific primitives are later work.

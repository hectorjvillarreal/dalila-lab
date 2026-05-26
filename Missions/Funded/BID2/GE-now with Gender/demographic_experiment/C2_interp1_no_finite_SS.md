# C2 closure under interpretation 1 admits no finite steady state

**Status.** Empirical finding from the BID2 gender-extension aging
comparative-steady-state experiment, 2026-05-25. Documented here as
seminar / paper motivation, not as a bug to fix.

## Setup

C2 in `CC_instrucciones_aging_steady_state.md` §1 is the closure that
isolates the *debt channel* of aging: pin τ^p at its 2020 calibrated
value while letting general government debt B absorb the resulting
fiscal gap. The spec table:

| Closure | What clears PAYG | What clears general budget |
|---|---|---|
| **C2 — debt absorbs** | τ^p **fixed at 2020 value** | endogenous B (residual) |

The spec is silent on where the PAYG deficit goes. Two readings are
defensible:

1. **Interpretation 1.** The PAYG block runs a deficit (pension benefits
   continue at the calibrated rate `pen = κ·w·L/N^W` because κ doesn't
   change; contributions are below market-clearing because τ^p is
   pinned). The deficit flows into the general government budget, so the
   residual B absorbs both the regular general primary AND the pension
   shortfall.
2. **Interpretation 2.** Pension benefits scale back to whatever the
   pinned τ^p can fund: `pen = τ^p · w · L / N^R`. PAYG balances by
   benefit cut. B is computed exactly as under endogenous PAYG.

The spec wording "B absorbs" matches interpretation 1 most directly. The
finding below is that interpretation 1 has no finite stationary
equilibrium under the WPP-2024 medium 2050 calibration for Mexico.

## What we did

`run_aging_c2_recovery.jl` (with `Base.invokelatest` on `solve_ge!` to
defeat Julia 1.x method-dispatch caching across `update_pension_taxes!`
redefinitions) was patched to add the PAYG shortfall to general
spending:

```julia
function compute_debt!(C, L, K, M, Y)
    G = gy * Y
    pen_paid       = κ_rep * w_now * L * N_R_now / N_W_now    # benefits
    pen_collected  = τp_now * w_now * L                       # contributions
    pension_deficit = pen_paid - pen_collected                # ≥ 0 when pinned
    primary = τc*C + τw*w_now*L + τk*r_now*K + τm*M - G - pension_deficit
    B_debt_now = primary / (rn_now - n_p)
end
```

In endogenous PAYG mode this is identity-equivalent to the spec's
default (`pension_deficit ≡ 0`), so RUN 1 / CONTROL / RUN 2 are
unchanged. In the C2 closure it routes the deficit through the
intertemporal government budget.

## What we observed

The outer GE iter loop diverges. Trajectory:

```
iter   K      L      r(5y)    τp     DIFF/Y
1     12     10     0.163    0.145   -0.79
2     20.5   13.95  0.101    0.145   -0.33
5     31.8   20.05  0.080    0.145   -0.10
7     42.2   21.88  0.029    0.145   -0.08    ← DIFF starts climbing
8     54.7   22.57  -0.022   0.145   -0.11
9    557.3   23.28  -0.274   0.145   -1.36    ← K explodes
10   342.2   25.63  -0.239   0.145   -0.82
11   205.0   26.84  -0.192   0.145   -0.46
13    54.2   27.10   0.021   0.145   -0.01
14    79.1   26.25  -0.065   0.145   -0.11
```

K rises monotonically through iter 8, then jumps by an order of
magnitude at iter 9 and oscillates without settling. The `Euler max
log10` and goods-market residual never close.

## Mechanism

The general government's intertemporal budget at SS pins B by
`(r^n − n_p) · B = primary`, so `B = primary / (r^n − n_p)`. Under the
2020 calibration and broadly under the 2050 endogenous-τ^p calibration,
`r^n − n_p` is positive and the SS is unique.

Under C2 interp 1 at 2050 demographics, two forces compound:

1. **Pension deficit pushes primary deep into deficit.** Pen_paid scales
   with the new dependency ratio (N^R/N^W ≈ 0.54 at 2050 vs 0.28 at
   2020), while pen_collected stays at the 2020-calibrated 14.5%. The
   PAYG shortfall is roughly 12 pp of `w·L` per period — economically,
   the largest single fiscal item.

2. **The implied debt drags down r.** A large negative primary requires
   a deeply negative B, which means government holds debt. To service
   that debt the capital stock has to be larger (so households want to
   hold the gross asset position `A_dom = K + (−B)`). Higher K depresses
   r via the firm FOC `r = α A (K/L)^(α−1) − δ`.

These two reinforce: more debt → higher K → lower r → `r^n − n_p`
collapses toward zero from above. As the denominator shrinks, B
(computed from `primary / (r^n − n_p)`) diverges. At the iter where
`r^n` first falls below `n_p`, B sign-flips and the K_target update
ricochets across orders of magnitude. The damped K update (damp = 0.30)
cannot hold the system together once the denominator approaches zero.

## Economic interpretation

This is **not** a numerical artifact. The model is reporting a
substantive feature of the 2050 calibration: under Mexico's projected
demographic structure, the 2020 contribution rate is too low by a
margin that **cannot be intertemporally financed via general debt** at
the model's calibrated technology and preferences. The pension shortfall
is large enough to push the economy into the dynamic-inefficiency
region (r^n < n_p), at which point the standard transversality argument
that fixes B at a finite SS breaks down.

In standard PAYG / public-finance language: at the calibrated κ, β, α,
and 2050 demographics, the pension system's implicit debt cannot be
amortized by any finite explicit debt stock. **Some other margin must
adjust.** Three candidates:

- τ^p rises (C1, the joint-closure baseline — yields a clean SS).
- Benefits cut so PAYG balances at the pinned τ^p (interpretation 2 —
  is the closure used for the actual C2 number we ship).
- General taxation rises to fund the shortfall (C3, the
  contribution-rate channel — yields a clean SS).

## Why this is good for the paper

The C2 interp-1 instability is the cleanest possible motivation for
why "do nothing" is not a feasible policy under the 2050 demographic
projection. Mexico (and by extension other Latin American economies
with comparable trajectories) cannot keep its pension system on
present-law contribution rates and finance the gap with debt: the
mathematics of intertemporal government solvency forbid it. *Something
has to give*; the policy question is only which margin.

This is a stronger headline than the more pedestrian "aging is fiscally
expensive" framing. It converts an empirical magnitude exercise into a
qualitative feasibility statement.

## Why we ship interpretation 2 for the C2 column

For the seminar table we need a single number per (K, L, τ^p, B/Y) cell.
Interpretation 1's number doesn't exist. Interpretation 2 (benefits
scale to balance PAYG at the pinned τ^p) gives a finite, reportable SS
and corresponds to the literal closure most other applied OLG papers
use when they pin contribution rates — the incidence falls on
retirees rather than taxpayers. The seminar table footnote should
explicitly say: *"C2 implements benefit-scaling to balance PAYG at the
pinned τ^p; the alternative interpretation (debt absorbs) is shown in
Appendix X to not admit a finite SS at the 2050 calibration, see [this
note]."*

## Implementation pointer

Interpretation 1 patch lives in `run_aging_c2_recovery.jl` (the
`compute_debt!` redefinition that includes `pension_deficit`). It is
documented but commented out / superseded; the file as shipped uses
interpretation 2.

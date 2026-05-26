# Claude Code Instructions — Aging Comparative Steady State

**Repository:** `BID/Codes/New codes/archivos julia/GE-Gender`
**Source file:** `ge_model_gender.jl` (do not edit; copy)
**Deliverable:** A standalone experiment script that runs the gender-extension
GE solver twice — once at 2020 demographics (baseline), once at a 2050
demographic structure (aged) — and writes a comparative table.
**Purpose:** Headline figure for the June 5 IDB seminar. *Cost of inaction*
under demographic aging, holding all policy instruments at calibrated values.
**Not** a transition path; this is the long-run steady state the economy
converges to under unchanged policy.

---

## 1. What this experiment is and is not

This is a **comparative-steady-state** experiment. Two stationary general
equilibria, both solved with the existing `solve_ge!` machinery, differing
only in three demographic primitives:

- `n_p` — population growth rate (5-year period).
- `_ψ_base_male` — male survival schedule (length-J vector).
- `_ψ_base_female` — female survival schedule (length-J vector).

Everything else — preferences, technology, taxes, κ, GHH parameters, health
production, age-efficiency profiles `e_age` — is held at the 2020 calibration.
This isolates the demographic shock cleanly and is the framing committed to
for the seminar.

The 2050 result is the steady state the economy would converge to if it had
a full generation to reoptimize at the 2050 demographic structure under
unchanged policy. It is an **upper bound on the welfare incidence of long-run
aging**, not a forecast of the fiscal pressure Mexico faces in 2050. The
report language must reflect this distinction.

**Disentangled closures.** The current `ge_model_gender.jl` runs a *joint*
closure: `τ^p` clears the PAYG block (`κ · N^R / N^W`) and `B` absorbs the
residual of the general government budget simultaneously. For the seminar
we want to **decompose** the fiscal pressure of aging into a pension-side
piece and a debt-side piece. Run the 2050 demographics three times under
three closures:

| Closure | What clears PAYG | What clears general budget |
|---|---|---|
| **C1 — joint (status quo)** | endogenous τ^p | endogenous B (residual) |
| **C2 — debt absorbs** | τ^p **fixed at 2020 value** | endogenous B (residual) |
| **C3 — contribution absorbs** | endogenous τ^p | B **fixed at 2020 value**, residual into τ^ω |

C1 is the baseline used in the paper (Section 6.3). C2 isolates the *debt
channel* of aging: how much does B/Y rise if τ^p is held at the 2020
contribution rate? C3 isolates the *contribution-rate channel*: how much
must general taxation rise to keep B/Y stable, on top of the PAYG-clearing
τ^p? The three together let us tell the IDB audience: *of the total fiscal
pressure of aging, x percentage points fall on pension contributions, y on
the debt path, z on general taxation if debt is held constant.* This is the
disentangled product Beth asked for.

**Total runs:** 4 (one 2020 baseline + three 2050 closures). Wall-clock
budget: ~10 hours on Dalila. If pressed, drop C3 — C1 and C2 are the
analytical minimum.

---

## 2. File layout

Create a new directory `GE-Gender/aging-experiment/`. Inside:

```
aging-experiment/
├── run_aging_ssvs.jl       # the driver
├── demographics_2050.jl    # the new primitives (data block only)
├── results/                # CSVs written here
└── README.md               # human notes
```

**Do not edit `ge_model_gender.jl`.** The driver `include`s it. If a
parameter needs to be overridden, redefine the binding *before* `include`,
or use the runtime-override pattern in §4 below.

---

## 3. The demographic primitives for 2050

These come from Anne. Until she delivers, use the placeholder values below
so the script runs end-to-end. **Replace before any seminar-quality run.**

Create `demographics_2050.jl`:

```julia
# demographics_2050.jl
#
# Mexico 2050 demographic primitives, 5-year-period bands matching the
# J = 17 grid of ge_model_gender.jl (ages 20-100).
#
# Source: CELADE Mexico projection [Anne to confirm vintage and aggregation].
# 5-year-period quantities: ψ is per-period survival probability, n_p is
# the 5-year gross population growth rate minus 1.
#
# PLACEHOLDER VALUES — REPLACE WITH CELADE-DERIVED NUMBERS.

# Population growth (5-year period). 2020 value: 1.01^5 - 1 ≈ 0.0510.
# Placeholder 2050: 0.4% annual.
const n_p_2050 = 1.004^5 - 1.0     # ≈ 0.0202

# Male survival schedule, length-17 vector. 2020 baseline retained
# through age band 9; older bands lifted ~3 percentage points to mimic
# CELADE-projected longevity gains.
const ψ_base_male_2050 = [
    1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
    0.9920, 0.9870, 0.9800, 0.9700,        # 35-39 ... 65-69, modest lift
    0.9520, 0.9250, 0.8780, 0.7650,        # 70-74 ... 85-89, larger lift
    0.5950, 0.3450, 0.1800                  # 90+, terminal
]

# Female survival schedule. Larger lift consistent with widening sex gap.
const ψ_base_female_2050 = [
    1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
    0.9950, 0.9910, 0.9860, 0.9790,
    0.9650, 0.9420, 0.9050, 0.8050,
    0.6450, 0.3950, 0.2100
]

@assert length(ψ_base_male_2050)   == 17
@assert length(ψ_base_female_2050) == 17
```

**Anne's deliverable for this file.** Two 17-element vectors of 5-year-period
survival probabilities for Mexico, projected to 2050, by sex; plus one scalar
`n_p_2050`. If CELADE gives annual life tables, aggregation to 5-year bands
is `ψ_period[j] = prod(ψ_annual[5(j-1)+1 : 5j])` over the 5 annual survival
probabilities in band j.

---

## 4. The runtime-override pattern

`ge_model_gender.jl` declares its demographic primitives as `const`. We
cannot redefine them. The cleanest way to swap them at runtime without
editing the source is to **load the source once, then redefine the relevant
module-level bindings as non-const overrides via `eval`**, then call
`solve_ge!()`.

In `run_aging_ssvs.jl`:

```julia
# run_aging_ssvs.jl
#
# Comparative-steady-state experiment for the June 5 IDB seminar:
# 2020 baseline vs three 2050 closures. Reuses ge_model_gender.jl
# without editing it.

using Printf, Statistics

const GE_SRC = joinpath(@__DIR__, "..", "ge_model_gender.jl")
const DEMOG_2050 = joinpath(@__DIR__, "demographics_2050.jl")

include(GE_SRC)                 # brings in solve_ge!, all primitives
include(DEMOG_2050)             # brings in n_p_2050, ψ_base_*_2050

# ---------- override helpers ------------------------------------------------

"""
    set_demographics!(n_p_new, ψ_m_new, ψ_f_new)

Replace the demographic primitives in the active session. The `const`
bindings in ge_model_gender.jl are shadowed by these redefinitions because
they are evaluated in Main, the same module that `include` evaluated the
source in. After this returns, every function that reads `n_p`, `ψ_base`,
or `e_age` sees the new values.

Note: Julia will warn on redefinition of a `const`. The warning is benign
here — we are doing it deliberately as an experiment harness.
"""
function set_demographics!(n_p_new::Float64,
                           ψ_m_new::Vector{Float64},
                           ψ_f_new::Vector{Float64})
    @assert length(ψ_m_new) == J
    @assert length(ψ_f_new) == J
    Core.eval(@__MODULE__, :(const n_p     = $n_p_new))
    Core.eval(@__MODULE__, :(const ψ_base  = vcat($(ψ_m_new)', $(ψ_f_new)')))
    return nothing
end

"""
    set_pension_closure!(mode, τp_fixed)

Switch between PAYG closures. Mode `:endogenous` keeps the default
τ^p = κ · N^R / N^W. Mode `:fixed` overrides update_pension_taxes! to
pin τ^p at the supplied value.
"""
function set_pension_closure!(mode::Symbol, τp_fixed::Float64 = 0.0)
    if mode === :endogenous
        Core.eval(@__MODULE__, quote
            function update_pension_taxes!(L_eff::Float64)
                global τp_now, pen_now, wn_now
                if N_W_now > 0.0
                    τp_now  = κ_rep * N_R_now / N_W_now
                    pen_now = κ_rep * w_now * L_eff / N_W_now
                end
                wn_now = w_now * (1.0 - τw - τp_now)
            end
        end)
    elseif mode === :fixed
        Core.eval(@__MODULE__, quote
            function update_pension_taxes!(L_eff::Float64)
                global τp_now, pen_now, wn_now
                τp_now = $τp_fixed
                if N_W_now > 0.0
                    pen_now = κ_rep * w_now * L_eff / N_W_now
                end
                wn_now = w_now * (1.0 - τw - τp_now)
            end
        end)
    else
        error("Unknown closure mode: $mode")
    end
end

"""
    set_debt_closure!(mode, B_fixed)

Switch between general-budget closures. Mode `:residual_B` keeps the
default (B is the residual). Mode `:residual_τω` fixes B at the supplied
value and lets τ^ω clear the general budget.
"""
function set_debt_closure!(mode::Symbol, B_fixed::Float64 = 0.0)
    if mode === :residual_B
        Core.eval(@__MODULE__, quote
            function compute_debt!(C::Float64, L::Float64, K::Float64,
                                   M::Float64, Y::Float64)
                global B_debt_now
                G = gy * Y
                primary = τc * C + τw * w_now * L + τk * r_now * K + τm * M - G
                B_debt_now = primary / (rn_now - n_p)
            end
        end)
    elseif mode === :residual_τω
        Core.eval(@__MODULE__, quote
            global τω_endog::Float64 = τw
            function compute_debt!(C::Float64, L::Float64, K::Float64,
                                   M::Float64, Y::Float64)
                global B_debt_now, τω_endog
                B_debt_now = $B_fixed
                G = gy * Y
                # primary surplus required to service fixed B:
                primary_req = (rn_now - n_p) * $B_fixed
                # solve for τω that delivers it (linear in τω):
                # τc*C + τω*w*L + τk*r*K + τm*M - G = primary_req
                τω_endog = (primary_req + G - τc*C - τk*r_now*K - τm*M) /
                           (w_now * L)
            end
        end)
    else
        error("Unknown closure mode: $mode")
    end
end
```

**Two caveats to verify when first running.** First, Julia 1.x permits `const`
redefinition with a warning but the new binding may not propagate into
already-compiled methods that captured the old value. The grids `a_grid`,
`h_grid` and the policy arrays do not depend on demographics so they are
safe. `n_p` appears in `forward_distribution!` and `compute_debt!`; both
read it at every call so they will see the override. `ψ_base` appears
inside `survival()` which reads it at every call. **Test the override
pattern with a no-op call** (set demographics to the 2020 values and confirm
the equilibrium is bit-identical to a fresh run) before trusting the 2050
results.

Second, the `τω_endog` closure for C3 is *not* used by `solve_household!`
in the source — the household reads `τw` directly. For C3 to actually
clear, we need either (a) an outer loop that updates `τw` between GE
iterations, or (b) a redefinition of `available_resources` that reads
`τω_endog` in place of `τw`. Option (b) is cleaner. Add to
`set_debt_closure!(:residual_τω, ...)` a redefinition of
`available_resources` reading `τω_endog`. **If implementing C3 turns out
to require nontrivial surgery, drop C3 for June 5 and present C1 + C2
only.** The disentanglement value is mostly in the C1 vs C2 contrast.

---

## 5. The driver

```julia
# ---------- experimental runs -----------------------------------------------

mutable struct RunResult
    label::String
    K::Float64; L::Float64; Y::Float64
    r_annual::Float64; w::Float64
    τp::Float64; B::Float64; B_over_Y::Float64
    C_over_Y::Float64; M_over_Y::Float64
    N_W::Float64; N_R::Float64; depratio::Float64
    W_MθL::Float64; W_MθH::Float64; W_FθL::Float64; W_FθH::Float64
    DIFF::Float64; euler_max::Float64
end

function run_one(label::String)
    println("\n" * "="^70)
    println("  RUN: $label")
    println("="^70)
    hist, A_dom, L_new, C, M, Λvoid, Y, K, L = solve_ge!()
    W = welfare_at_birth()
    r_annual = ((1.0 + r_now)^0.2 - 1.0) * 100
    res = euler_residual_stats()
    eulmax = isempty(res) ? -Inf : maximum(log10.(max.(res, 1e-16)))
    return RunResult(
        label, K, L, Y, r_annual, w_now,
        τp_now, B_debt_now, B_debt_now / Y,
        C / Y, M / Y, N_W_now, N_R_now, N_R_now / N_W_now,
        W[1,1], W[1,2], W[2,1], W[2,2],
        hist.DIFF[end], eulmax
    )
end

# Save the 2020 values we need for closures C2 and C3.
const n_p_2020      = n_p
const ψ_base_2020_m = copy(ψ_base[1, :])
const ψ_base_2020_f = copy(ψ_base[2, :])

# ---------- RUN 1: 2020 baseline -------------------------------------------
set_pension_closure!(:endogenous)
set_debt_closure!(:residual_B)
r_baseline = run_one("2020 baseline (joint closure)")

τp_2020 = r_baseline.τp
B_2020  = r_baseline.B

# ---------- RUN 2: 2050 demographics, C1 joint closure ---------------------
set_demographics!(n_p_2050, ψ_base_male_2050, ψ_base_female_2050)
set_pension_closure!(:endogenous)
set_debt_closure!(:residual_B)
r_C1 = run_one("2050 C1 — joint (τp and B both endogenous)")

# ---------- RUN 3: 2050 demographics, C2 debt absorbs ----------------------
set_pension_closure!(:fixed, τp_2020)
set_debt_closure!(:residual_B)
r_C2 = run_one("2050 C2 — τp pinned at 2020, B absorbs")

# ---------- RUN 4: 2050 demographics, C3 contribution absorbs --------------
# Comment out if implementing the τω clearing turns out to be involved.
set_pension_closure!(:endogenous)
set_debt_closure!(:residual_τω, B_2020)
r_C3 = run_one("2050 C3 — B pinned at 2020, τω absorbs")

# ---------- write the comparison CSV ---------------------------------------
runs = [r_baseline, r_C1, r_C2, r_C3]
open(joinpath(@__DIR__, "results", "aging_comparison.csv"), "w") do io
    println(io, "label,K,L,Y,r_annual_pct,w,taup,B,B_over_Y," *
                "C_over_Y,M_over_Y,N_W,N_R,depratio," *
                "W_MθL,W_MθH,W_FθL,W_FθH,DIFF_over_Y,euler_max_log10")
    for r in runs
        @printf(io, "%s,%.5f,%.5f,%.5f,%.4f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.3e,%.3f\n",
            r.label, r.K, r.L, r.Y, r.r_annual, r.w,
            r.τp, r.B, r.B_over_Y, r.C_over_Y, r.M_over_Y,
            r.N_W, r.N_R, r.depratio,
            r.W_MθL, r.W_MθH, r.W_FθL, r.W_FθH,
            r.DIFF, r.euler_max)
    end
end

# ---------- print the seminar table ----------------------------------------
println("\n" * "="^70)
println("  SEMINAR TABLE — Aging comparative steady state, Mexico")
println("="^70)
@printf "  %-40s  %8s  %8s  %8s  %8s\n" "" "2020" "C1" "C2" "C3"
@printf "  %-40s  %8.3f  %8.3f  %8.3f  %8.3f\n" "K (capital)"          r_baseline.K       r_C1.K       r_C2.K       r_C3.K
@printf "  %-40s  %8.3f  %8.3f  %8.3f  %8.3f\n" "Y (output)"           r_baseline.Y       r_C1.Y       r_C2.Y       r_C3.Y
@printf "  %-40s  %7.2f%%  %7.2f%%  %7.2f%%  %7.2f%%\n" "r (annual)"   r_baseline.r_annual r_C1.r_annual r_C2.r_annual r_C3.r_annual
@printf "  %-40s  %7.2f%%  %7.2f%%  %7.2f%%  %7.2f%%\n" "τp"           100*r_baseline.τp  100*r_C1.τp  100*r_C2.τp  100*r_C3.τp
@printf "  %-40s  %7.2f%%  %7.2f%%  %7.2f%%  %7.2f%%\n" "B/Y"          100*r_baseline.B_over_Y 100*r_C1.B_over_Y 100*r_C2.B_over_Y 100*r_C3.B_over_Y
@printf "  %-40s  %8.4f  %8.4f  %8.4f  %8.4f\n" "dep. ratio N^R/N^W"   r_baseline.depratio r_C1.depratio r_C2.depratio r_C3.depratio
println()
@printf "  Welfare at birth W₁(g,θ):\n"
@printf "  %-40s  %8.4f  %8.4f  %8.4f  %8.4f\n" "  M, θL"  r_baseline.W_MθL r_C1.W_MθL r_C2.W_MθL r_C3.W_MθL
@printf "  %-40s  %8.4f  %8.4f  %8.4f  %8.4f\n" "  M, θH"  r_baseline.W_MθH r_C1.W_MθH r_C2.W_MθH r_C3.W_MθH
@printf "  %-40s  %8.4f  %8.4f  %8.4f  %8.4f\n" "  F, θL"  r_baseline.W_FθL r_C1.W_FθL r_C2.W_FθL r_C3.W_FθL
@printf "  %-40s  %8.4f  %8.4f  %8.4f  %8.4f\n" "  F, θH"  r_baseline.W_FθH r_C1.W_FθH r_C2.W_FθH r_C3.W_FθH
println()
println("  Diagnostics:")
for r in runs
    @printf "    %-40s  DIFF/Y = %+.2e   Euler max log10 = %.2f\n" r.label r.DIFF r.euler_max
end
```

---

## 6. Sanity gates before trusting the output

After the four runs complete, the script must report whether each run was
trustworthy. Hard requirements:

1. `DIFF/Y < 1e-3` for all four runs (goods market cleared).
2. `euler_max log10 < -3` for all four runs. **This is the gate the gender
   gap run failed in the production code.** If 2050 runs trip this, the
   welfare numbers are not reportable. Print loudly and stop.
3. Capital market `|K − (A_dom − B)|/K < 2e-4` (the GE convergence tolerance
   times the damping factor headroom).
4. For C2 (τp pinned), confirm τp in the output equals `τp_2020` to machine
   precision.
5. For C3 (B pinned), confirm B in the output equals `B_2020` to machine
   precision, and report the implied `τω_endog`.

If any gate fails, the script writes the CSV anyway (intermediate results
have value for debugging) but flags the run as "DO NOT REPORT" in the
seminar table.

---

## 7. The control run that must pass before anything else

Before running anything at 2050, run the override pattern with 2020 values
and confirm the result matches `ge_summary.csv` from the current production
run to ~3 decimal places:

```julia
# Should reproduce ge_summary.csv exactly (modulo damping noise).
set_demographics!(n_p_2020, ψ_base_2020_m, ψ_base_2020_f)
set_pension_closure!(:endogenous)
set_debt_closure!(:residual_B)
r_control = run_one("CONTROL — 2020 via override (should match baseline)")
@assert abs(r_control.K - r_baseline.K) < 1e-3
@assert abs(r_control.τp - r_baseline.τp) < 1e-4
```

If this fails, the override pattern is not propagating and the 2050 results
are meaningless. Diagnose before proceeding.

---

## 8. Compute budget and order of execution

Each GE solve is ~2.5 hours on Dalila. Four runs = 10 hours wall-clock.
Order matters because the 2020 baseline supplies the pinning values for
C2 and C3:

1. RUN 1: 2020 baseline → captures `τp_2020`, `B_2020`. 2.5 hr.
2. CONTROL: override with 2020 values, confirm match. 2.5 hr. **Optional
   but strongly recommended.**
3. RUN 2: 2050 C1. 2.5 hr.
4. RUN 3: 2050 C2 (τp pinned). 2.5 hr.
5. RUN 4: 2050 C3 (B pinned). 2.5 hr.

Total: 10–12.5 hr. Start the run when you leave for the night; results
ready in the morning.

If schedule pressure forces a cut: drop the CONTROL run if you have already
exercised the override pattern; drop C3 if τω clearing turns out to need
more than a one-line `available_resources` redefinition. **Do not drop the
2020 baseline.** The 2050 numbers are meaningless without a same-build
2020 reference.

---

## 9. What goes in the seminar slides

One table:

| | 2020 | 2050 C1 (joint) | 2050 C2 (debt absorbs) | 2050 C3 (taxes absorb) |
|---|---|---|---|---|
| τ^p | 13.9% | ? | 13.9% (pinned) | ? |
| B/Y | 27.5% | ? | ? | 27.5% (pinned) |
| τ^ω | 20% | 20% | 20% | ? |
| dep. ratio | 0.277 | ? | ? | ? |

The disentangled message: of the total fiscal pressure shown in C1, *x* pp
of contribution-rate increase and *y* pp of B/Y rise. C2 says: if we hold
τ^p, the debt path absorbs *y'* pp of B/Y rise — bigger than the C1 number
because the pension block now leaks into general revenue. C3 says: holding
B/Y, general taxation rises by *z* pp on top of the C1 τ^p number — the
"true" fiscal burden if debt is not an option.

One welfare panel: a 2×4 plot of W₁(g, θ) for the four types at the four
configurations. The gender story is whether women's longer survival amplifies
or dampens their incidence of the aging shock relative to men.

---

## 10. What this experiment does not deliver

- Not a transition path. Cohorts alive in 2020 are *not* the ones bearing
  the C1/C2/C3 outcomes; those are reoptimized newborns into the 2050
  steady state. The transition incidence — who loses *during* the
  transition — is the September deliverable.
- Not a policy experiment. κ stays at 0.50, τ^m at 0. The pension-reform
  and health-subsidy counterfactuals Diego already ran are separate 2020
  results; they are not folded in here.
- Not a three-country result. Mexico only. Costa Rica and Panamá are
  September.
- Not gender-calibrated. The 0.85·e^male and 0.75·mortality stubs are still
  in place. The seminar message on the gender dimension is qualitative
  (sign and rough magnitude of differential incidence), not quantitative.

Each of these must be stated explicitly in the seminar to avoid
overpromising.

---

## 11. Pre-flight checklist for Diego

Before running:

- [ ] Anne has delivered `n_p_2050`, `ψ_base_male_2050`, `ψ_base_female_2050`.
- [ ] The gender-gap Euler residual issue (log10 = −1.18 in the production
      run) has been diagnosed. If unresolved, expect C1/C2/C3 to inherit
      it. The welfare numbers by sex are not reportable until this is fixed.
- [ ] The override pattern has been smoke-tested (CONTROL run).
- [ ] Repository tag created at the current state so we can revert if the
      override pattern misbehaves.

Post-run:

- [ ] `aging_comparison.csv` exists in `results/`.
- [ ] All four runs pass the sanity gates in §6.
- [ ] Seminar table printed to console matches CSV.
- [ ] Welfare-panel plot generated (one figure, 2×4 grid).
- [ ] Notes written into `aging-experiment/README.md` describing what was
      run, what passed, what didn't, and any deviations from this spec.

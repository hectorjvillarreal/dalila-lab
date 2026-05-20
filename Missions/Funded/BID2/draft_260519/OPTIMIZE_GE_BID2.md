# BID 2 — GE Solver Optimization (CPU)
**Mission BID 2 · Spending Smarter under Demographic Pressure**
*Instructions for Claude Code — Optimize `ge_model.jl` for the June 5 seminar*

---

## Context

You have a working but slow GE solver. The current `ge_model.jl` converges in 13 outer iterations to the correct stationary equilibrium, but each iteration takes ~30 minutes in the policy-experiment runs (κ=0.30, τ^m=−0.20), making the full run ~6.5 hours. With two experiments planned plus the baseline plus likely calibration iterations, this is unsustainable for the June 5 deadline.

| File | Description |
|------|-------------|
| `ge_model.jl` | Current GE solver (verified, fully self-contained, ~920 lines) |
| `ge_model_kappa30.jl` | κ=0.30 experiment variant |
| `ge_model_taum20.jl` | τ^m=−0.20 experiment variant |
| `Project.toml`, `Manifest.toml` | Julia environment (no GPU packages, no Tullio, no LoopVectorization — vanilla Julia 1.12.6) |
| `ge_run.log` | Baseline convergence log (the reference for verification) |
| `ge_summary.csv` | Baseline aggregates (the verification target) |
| `OPTIMIZE_GE_BID2.md` | This file |

**Hardware:** Dalila — Intel Core Ultra 9 285H (16 cores), NVIDIA GPU with CUDA. We are deliberately NOT using the GPU for this pass — CPU optimization yields most of the speedup at a fraction of the development cost.

**Target:** GE run time from ~90 minutes (baseline) / ~6.5 hours (current shock experiments) down to 2–5 minutes per run.

---

## Strategy

Three CPU optimizations applied sequentially, each with a verification gate:

1. **Threading restructure** — collapse the (ia, ih, is) loops into a single parallel block and use all 16 cores. Target speedup: 4–6x.
2. **Type stability and `@inbounds`** — remove allocations and bounds checks in the hot path. Target speedup: 1.5–2x.
3. **EGM (Endogenous Grid Method)** — replace the Brent rootfind on a' with a closed-form policy update. Target speedup: 5–10x on the household block.

Combined target: 30–100x. A 90-minute run becomes 1–3 minutes.

**Do not implement GPU acceleration.** It adds a week of CUDA.jl development for marginal gain. After June 5, if the agenda calls for thousands of counterfactuals, we revisit GPU.

**Do not add new package dependencies.** Pure Julia with `Threads.@threads`, `@inbounds`, and `@fastmath` is sufficient. The only optional addition is `StaticArrays` for the 4-element bilinear interpolation weights, and only if Phase 2 verification fails to deliver expected speedup.

---

## Phase 0: Baseline Snapshot (Mandatory)

Before touching anything, capture the current performance as the verification baseline.

### 0.1 Save the current working state

```bash
cp ge_model.jl ge_model_v0_baseline.jl
cp ge_summary.csv ge_summary_v0_baseline.csv
cp ge_lifecycle.csv ge_lifecycle_v0_baseline.csv
```

### 0.2 Time the current baseline run

```bash
julia --project=. --threads=auto ge_model_v0_baseline.jl > ge_run_v0_baseline.log 2>&1
```

Record:
- Wall-clock time (use `time` prefix or read elapsed time from log timestamps)
- Number of iterations to convergence
- Final K, L, Y, r, w, τp, M/Y values

These are the verification anchors. **Every subsequent optimization phase must reproduce these values to within 0.1% relative error.**

---

## Phase 1: Threading Restructure

### 1.1 Diagnosis

Current code (lines 374–401 of `ge_model.jl`):

```julia
function solve_household_for_type(iθ::Int)
    for ia in 0:NA, ih in 0:NH, is in 1:Nη
        ap, m, c, ℓ, hn, V = solve_cell(J, ia, ih, is, iθ)
        ...
    end
    for j in (J-1):-1:1
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            ap, m, c, ℓ, hn, V = solve_cell(j, ia, ih, is, iθ)
            ...
        end
    end
end
```

The `(ia, ih, is)` loop runs sequentially across $101 \times 16 \times 7 = 11{,}312$ cells per age per type, then over $J=16$ ages, then $\theta=2$ types. With `Threads.@threads` already wrapped externally somewhere, the Phase 2 report indicates only 2.7 effective cores out of 8.

The cells within a fixed `(j, iθ)` are **independent** (they all read from the already-computed `c_pol[j+1, ...]`, `l_pol[j+1, ...]`, `V_pol[j+1, ...]`). They can be parallelized cleanly.

### 1.2 Implementation

Replace `solve_household_for_type` with:

```julia
function solve_household_for_type(iθ::Int)
    # Build the flat index over (ia, ih, is) for parallel iteration
    cell_indices = [(ia, ih, is) for ia in 0:NA, ih in 0:NH, is in 1:Nη]
    cell_indices_flat = vec(cell_indices)
    n_cells = length(cell_indices_flat)

    # Terminal age j = J (parallel)
    Threads.@threads for idx in 1:n_cells
        ia, ih, is = cell_indices_flat[idx]
        ap, m, c, ℓ, hn, V = solve_cell(J, ia, ih, is, iθ)
        aplus_pol[J, ia, ih, is, iθ] = ap
        m_pol[J, ia, ih, is, iθ]     = m
        c_pol[J, ia, ih, is, iθ]     = c
        l_pol[J, ia, ih, is, iθ]     = ℓ
        hnext_pol[J, ia, ih, is, iθ] = hn
        V_pol[J, ia, ih, is, iθ]     = V
    end

    # Backward induction (parallel within each age, sequential across ages)
    for j in (J-1):-1:1
        Threads.@threads for idx in 1:n_cells
            ia, ih, is = cell_indices_flat[idx]
            ap, m, c, ℓ, hn, V = solve_cell(j, ia, ih, is, iθ)
            aplus_pol[j, ia, ih, is, iθ] = ap
            m_pol[j, ia, ih, is, iθ]     = m
            c_pol[j, ia, ih, is, iθ]     = c
            l_pol[j, ia, ih, is, iθ]     = ℓ
            hnext_pol[j, ia, ih, is, iθ] = hn
            V_pol[j, ia, ih, is, iθ]     = V
        end
    end
end
```

### 1.3 Thread-safety check — the scratch buffers

**Critical issue:** lines 119–124 of `ge_model.jl` declare globally shared scratch buffers:

```julia
const ial_buf      = Array{Int64}(undef, 1)
const iar_buf      = Array{Int64}(undef, 1)
const varphi_a_buf = zeros(1)
const ihl_buf      = Array{Int64}(undef, 1)
const ihr_buf      = Array{Int64}(undef, 1)
const varphi_h_buf = zeros(1)
```

These are used by `linint_Grow` calls inside `asset_interp` and `health_interp` (lines 233–247). Multiple threads writing to the same length-1 arrays is a **race condition** — current code is unsafe under `@threads`.

**Fix:** make the scratch buffers thread-local. Replace lines 119–124 with:

```julia
# Thread-local scratch buffers — one set per thread
const ial_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const iar_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const varphi_a_buf_per_thread = [zeros(1) for _ in 1:Threads.nthreads()]
const ihl_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const ihr_buf_per_thread      = [Array{Int64}(undef, 1) for _ in 1:Threads.nthreads()]
const varphi_h_buf_per_thread = [zeros(1) for _ in 1:Threads.nthreads()]
```

Then modify `asset_interp` and `health_interp`:

```julia
function asset_interp(a_prime::Float64)
    tid = Threads.threadid()
    ial, iar, φ_a = linint_Grow(a_prime, a_l, a_u, a_grow, NA,
                                 ial_buf_per_thread[tid],
                                 iar_buf_per_thread[tid],
                                 varphi_a_buf_per_thread[tid])
    ial = max(min(ial, NA - 1), 0)
    iar = max(min(iar, NA), 1)
    φ_a = clamp(φ_a, 0.0, 1.0)
    return ial, iar, φ_a
end

function health_interp(h::Float64)
    tid = Threads.threadid()
    ihl, ihr, φ_h = linint_Grow(h, h_l, h_u, h_grow, NH,
                                 ihl_buf_per_thread[tid],
                                 ihr_buf_per_thread[tid],
                                 varphi_h_buf_per_thread[tid])
    ihl = max(min(ihl, NH - 1), 0)
    ihr = max(min(ihr, NH), 1)
    φ_h = clamp(φ_h, 0.0, 1.0)
    return ihl, ihr, φ_h
end
```

### 1.4 Verification Gate — Phase 1

Save the modified file as `ge_model_v1_threaded.jl`. Run:

```bash
julia --project=. --threads=auto ge_model_v1_threaded.jl > ge_run_v1_threaded.log 2>&1
```

Check:

| Check | Threshold |
|-------|-----------|
| Convergence | Same number of iterations as v0_baseline (±1) |
| K, L, Y | Within 0.1% of v0_baseline values |
| r, w, τp | Within 0.01 percentage points of v0_baseline |
| M/Y | Within 0.1 percentage points of v0_baseline |
| Wall-clock | At least 3x faster than v0_baseline |

If any check fails, **stop** and diagnose. Most likely causes: residual race condition (some thread-shared state not yet identified), or unintended sequencing change in the backward induction.

If all checks pass, proceed to Phase 2.

---

## Phase 2: Type Stability and `@inbounds`

### 2.1 Diagnosis

Hot functions (called millions of times per outer iter):
- `solve_cell` (line 316)
- `value_at` (line 284)
- `euler_residual` (line 271)
- `expected_uc_next` (line 259)
- `interp_pol` (line 249)
- `asset_interp`, `health_interp` (lines 233, 241)
- `marginal_utility_c`, `utility`, `ghh_z`, `health_amenity`, `disutility_of_labor` (lines 141–163)
- `labor_supply`, `productivity`, `available_resources`, `consumption_from_choices` (lines 199–230)

Most are already type-stable (returning `::Float64` explicitly). Two potential issues:

**Issue A — Global reads:** Functions read `r_now`, `w_now`, `rn_now`, `wn_now`, `τp_now`, `pen_now`, `B_debt_now`, `N_W_now`, `N_R_now` (lines 80–88). These are typed globals (`::Float64`), which is the right pattern. Verify type inference works by running `@code_warntype foc(...)` on a representative call after the threading pass.

**Issue B — OffsetArray bounds checks:** Every read/write to `c_pol[j, ia, ih, is, iθ]` does a bounds check. In the hot loop this is wasted cycles.

### 2.2 Implementation

Add `@inbounds @fastmath` to all hot inner loops. Specifically:

In `interp_pol` (line 249):
```julia
function interp_pol(P::OffsetArray, j_next::Int, a_prime::Float64,
                    h_next::Float64, is::Int, iθ::Int)::Float64
    ial, iar, φ_a = asset_interp(a_prime)
    ihl, ihr, φ_h = health_interp(h_next)
    @inbounds @fastmath begin
        v = φ_a       * φ_h       * P[j_next, ial, ihl, is, iθ] +
            φ_a       * (1.0-φ_h) * P[j_next, ial, ihr, is, iθ] +
            (1.0-φ_a) * φ_h       * P[j_next, iar, ihl, is, iθ] +
            (1.0-φ_a) * (1.0-φ_h) * P[j_next, iar, ihr, is, iθ]
    end
    return v
end
```

In `expected_uc_next` (line 259):
```julia
function expected_uc_next(j_next::Int, a_prime::Float64, h_next::Float64,
                          is_now::Int, iθ::Int)::Float64
    s = 0.0
    @inbounds @fastmath for is_p in 1:Nη
        c_p  = interp_pol(c_pol, j_next, a_prime, h_next, is_p, iθ)
        ℓ_p  = interp_pol(l_pol, j_next, a_prime, h_next, is_p, iθ)
        uc_p = marginal_utility_c(c_p, ℓ_p, h_next)
        s += π_η[is_now, is_p] * uc_p
    end
    return s
end
```

In `forward_distribution!` (line 422), the inner `(ia, ih, is, iθ)` loop:
```julia
for j in 1:(J-1)
    @inbounds for ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
        mass = Φ[j, ia, ih, is, iθ]
        ...
    end
end
```

In `aggregate_all` (line 482):
```julia
function aggregate_all()
    A_dom = 0.0
    L_eff = 0.0
    C     = 0.0
    M     = 0.0
    Λvoid = 0.0
    @inbounds for j in 1:J, ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
        ...
    end
    return A_dom, L_eff, C, M, Λvoid
end
```

### 2.3 Optional: thread the aggregator

`aggregate_all` is currently serial (~5% of runtime). It can be threaded with a reduction:

```julia
function aggregate_all()
    n_threads = Threads.nthreads()
    A_dom_t = zeros(n_threads)
    L_eff_t = zeros(n_threads)
    C_t     = zeros(n_threads)
    M_t     = zeros(n_threads)
    Λvoid_t = zeros(n_threads)

    Threads.@threads for j in 1:J
        tid = Threads.threadid()
        @inbounds for ia in 0:NA, ih in 0:NH, is in 1:Nη, iθ in 1:Nθ
            mass = Φ[j, ia, ih, is, iθ]
            if mass < 1e-18; continue; end
            a_now = a_grid[ia]
            h_now = h_grid[ih]
            η_now = η_grid[is]
            A_dom_t[tid] += mass * a_now
            C_t[tid]     += mass * c_pol[j, ia, ih, is, iθ]
            M_t[tid]     += mass * m_pol[j, ia, ih, is, iθ]
            if j < j_R
                ν_j = productivity(j, h_now, η_now, iθ)
                ℓ   = l_pol[j, ia, ih, is, iθ]
                L_eff_t[tid] += mass * ν_j * ℓ
            end
            h_n     = hnext_pol[j, ia, ih, is, iθ]
            ψ_next  = survival(j + 1, h_n)
            a_prime = aplus_pol[j, ia, ih, is, iθ]
            Λvoid_t[tid] += mass * (1.0 - ψ_next) * a_prime
        end
    end
    return sum(A_dom_t), sum(L_eff_t), sum(C_t), sum(M_t), sum(Λvoid_t)
end
```

### 2.4 Verification Gate — Phase 2

Save as `ge_model_v2_typed.jl`. Run and verify the same five checks from Phase 1. Expected additional speedup: 1.5–2x over v1.

---

## Phase 3: Endogenous Grid Method (EGM)

This is the largest speedup and the most subtle change. Read this section carefully before implementing.

### 3.1 Why EGM works here

The current code (`solve_cell`, lines 316–372) does, for each cell and each m candidate:

1. Compute available resources $X$ and the cap $a_{hi} = X - (1+\tau^m)m - \epsilon$
2. Evaluate `euler_residual(a_l, ...)` and `euler_residual(a_hi, ...)`
3. If they bracket zero, call `find_zero(..., Brent())` — typically 8–15 function evaluations of `euler_residual`
4. Each `euler_residual` call does a bilinear interpolation of `c_pol[j+1, ...]` and `l_pol[j+1, ...]` over 7 η states, totaling 56 array reads and 14 `marginal_utility_c` calls

**Brent on a' costs ~50× more compute than necessary** for this class of problem. EGM eliminates Brent entirely.

### 3.2 The EGM algorithm

For each age $j$ working backward from $J-1$:

**Step 1.** On the grid of *next-period* assets $a'$ (i.e., the same $a$-grid we already have), compute the expected marginal value:
$$\widetilde{V}'_j(a', h, s, \theta) = \beta \cdot \psi_{j+1}(h_{\text{next}}) \cdot (1+r^n) \cdot \mathbb{E}_{s'}\left[ u_c\big(c_{j+1}(a', h_{\text{next}}, s', \theta), \ell_{j+1}(\cdot), h_{\text{next}}\big) \right]$$

For Phase 3 of EGM with health investment, this is more complex because $h_{\text{next}}$ depends on the current cell's $m$ choice. We will handle this by keeping the outer $m$-grid loop but replacing the inner Brent with EGM.

**Step 2.** Invert the marginal utility to recover the implied consumption:
$$c^{\text{egm}}_j(a', h, s, \theta) = \widetilde{V}'_j(a', h, s, \theta)^{-1/\gamma} \cdot u_c^{-1}(\widetilde{V}'_j)$$

For GHH preferences with $u(z) = (z^{1-\gamma}-1)/(1-\gamma)$ and $z = c + s(h) - v(\ell)$:
$$u_c = z^{-\gamma} \implies z^{\text{egm}} = (\widetilde{V}'_j)^{-1/\gamma}$$
$$c^{\text{egm}} = z^{\text{egm}} - s(h) + v(\ell)$$

where $\ell$ is the closed-form GHH labor supply (already computed in `labor_supply`).

**Step 3.** Recover the implied beginning-of-period assets from the budget constraint:
$$a^{\text{egm}}_j(a', h, s, \theta) = \frac{(1+\tau^c) c^{\text{egm}} + a' + (1+\tau^m) m - \text{labor\_income} - pen \cdot \mathbf{1}_{j \geq j_R}}{1+r^n}$$

**Step 4.** We now have pairs $(a^{\text{egm}}, a')$ defined on the $a'$ grid. To recover the policy on the original $a$ grid, interpolate $a'(a) = $ interpolation of $a^{\text{egm}} \to a'$ evaluated at $a \in a$-grid.

**Step 5.** Borrowing-constraint correction: if $a^{\text{egm}}(\text{lowest grid point of } a') < a_l$, the constraint binds. For cells with $a < a^{\text{egm}}(0)$, set $a' = a_l$ and compute $c$ from the binding budget.

### 3.3 Implementation skeleton

Replace `solve_cell` and `solve_household_for_type` with an EGM-based version. Pseudocode:

```julia
function solve_household_for_type_egm(iθ::Int)
    # Terminal age (unchanged from current code — closed-form anyway)
    Threads.@threads for idx in 1:n_cells
        ia, ih, is = cell_indices_flat[idx]
        # ... terminal age handling identical to v2 ...
    end

    # Backward induction with EGM
    for j in (J-1):-1:1
        Threads.@threads for ih in 0:NH
            for is in 1:Nη
                # For each m candidate, build the EGM policy
                # Use the BEST m via value comparison after EGM produces a'
                solve_egm_for_jhi(j, ih, is, iθ)
            end
        end
    end
end

function solve_egm_for_jhi(j::Int, ih::Int, is::Int, iθ::Int)
    h_now = h_grid[ih]
    η_now = η_grid[is]
    ℓ_now = labor_supply(j, h_now, η_now, iθ)
    s_h_now = health_amenity(h_now)
    v_ℓ_now = disutility_of_labor(ℓ_now)
    labor_inc = j < j_R ? w_now * productivity(j, h_now, η_now, iθ) * ℓ_now * (1.0 - τw - τp_now) : 0.0
    pension_inc = j >= j_R ? pen_now : 0.0

    # Build m-grid (same as before, indexed on resource level which varies with a)
    # Simplification for Phase 3: use a coarser m-grid (Nm_egm = 10) and rely on EGM
    # to handle the a' dimension precisely.

    best_V_per_ia = fill(-Inf, NA+1)
    best_aprime_per_ia = zeros(NA+1)
    best_m_per_ia = zeros(NA+1)
    best_c_per_ia = zeros(NA+1)
    best_hnext_per_ia = fill(h_now, NA+1)

    Nm_egm = 10  # reduced from 30 — EGM handles a' precision, m can be coarse
    m_grid_local = build_m_grid_egm(Nm_egm, h_now, j)

    for m_cand in m_grid_local
        m_cost = (1.0 + τm) * m_cand
        h_nxt = health_next(h_now, m_cand, j)
        s_h_nxt = health_amenity(h_nxt)

        # EGM: for each a' on the grid, compute the expected marginal utility
        # and invert to find a^egm.
        for ia_prime in 0:NA
            a_prime = a_grid[ia_prime]

            # Expected u_c at next period
            Euc = 0.0
            for is_p in 1:Nη
                c_p = interp_pol(c_pol, j+1, a_prime, h_nxt, is_p, iθ)
                ℓ_p = interp_pol(l_pol, j+1, a_prime, h_nxt, is_p, iθ)
                uc_p = marginal_utility_c(c_p, ℓ_p, h_nxt)
                Euc += π_η[is, is_p] * uc_p
            end

            ψ_nxt = survival(j+1, h_nxt)
            Vprime = β_pref * ψ_nxt * (1.0 + rn_now) * Euc

            # Invert: z^egm = Vprime^(-1/γ)
            z_egm = Vprime^(-1.0 / γ_pref)
            c_egm = max(z_egm - s_h_now + v_ℓ_now, 1e-12)

            # Recover a^egm from the budget
            X_egm = (1.0 + τc) * c_egm + a_prime + m_cost
            a_egm = (X_egm - labor_inc - pension_inc) / (1.0 + rn_now)

            # Store (a_egm, a_prime, c_egm) for later interpolation onto a-grid
            # (use a temp array of length NA+1)
            ...
        end

        # Interpolate (a_egm → a_prime) onto the original a-grid
        # For each ia in 0:NA, find a_grid[ia] in the (a_egm) array,
        # interpolate a_prime and c.
        # Handle borrowing constraint: if a_grid[ia] < min(a_egm), set a' = a_l
        # and recompute c from binding budget.
        for ia in 0:NA
            a_target = a_grid[ia]
            a_prime_implied, c_implied = interp_a_to_egm(a_target, a_egm_array, a_prime_array, c_egm_array)

            # Compute value at this (a_prime_implied, m_cand)
            V_here = value_at(a_prime_implied, j, ia, ih, is, iθ, m_cand, h_now)

            if V_here > best_V_per_ia[ia+1]
                best_V_per_ia[ia+1]     = V_here
                best_aprime_per_ia[ia+1] = a_prime_implied
                best_m_per_ia[ia+1]      = m_cand
                best_c_per_ia[ia+1]      = c_implied
                best_hnext_per_ia[ia+1]  = h_nxt
            end
        end
    end

    # Write into policy arrays
    for ia in 0:NA
        aplus_pol[j, ia, ih, is, iθ] = best_aprime_per_ia[ia+1]
        m_pol[j, ia, ih, is, iθ]     = best_m_per_ia[ia+1]
        c_pol[j, ia, ih, is, iθ]     = best_c_per_ia[ia+1]
        l_pol[j, ia, ih, is, iθ]     = ℓ_now
        hnext_pol[j, ia, ih, is, iθ] = best_hnext_per_ia[ia+1]
        V_pol[j, ia, ih, is, iθ]     = best_V_per_ia[ia+1]
    end
end
```

### 3.4 EGM borrowing-constraint handling

Crucial detail: EGM produces an `a^egm` for each a' grid point. For cells where the agent's actual $a$ is below `min(a_egm)`, the borrowing constraint binds. Handle this explicitly:

```julia
# If a_target < a_egm_min, constraint binds
if a_target < a_egm_array[1]  # assuming a_egm sorted ascending
    aprime_implied = a_l
    # Compute c from budget at a_l
    X_at_a = (1.0 + rn_now) * a_target + labor_inc + pension_inc
    c_implied = max((X_at_a - a_l - (1.0+τm)*m_cand) / (1.0+τc), 1e-12)
else
    # Interpolate normally
    ...
end
```

### 3.5 Why we keep the m-grid loop

Pure EGM works only on the a' dimension. For the m choice, we still need to compare values across m candidates. But:
- The m-grid can be coarser (10 instead of 30) since EGM gives exact a' policy per m
- Each m candidate triggers ONE EGM sweep (no Brent), so 10 m candidates × 1 EGM = 10 sweeps, versus current 30 m candidates × ~15 Brent evals = 450 evaluations per cell
- That alone is a 45× speedup on the household block

### 3.6 Verification Gate — Phase 3

Save as `ge_model_v3_egm.jl`. Run and verify:

| Check | Threshold |
|-------|-----------|
| Convergence | Within ±2 iterations of v0_baseline |
| K, L, Y | Within 0.5% of v0_baseline (looser threshold — EGM has different numerical error than Brent) |
| r, w | Within 0.05 percentage points |
| τp | Within 0.05 percentage points |
| M/Y | Within 0.2 percentage points |
| Wall-clock | At least 20x faster than v0_baseline |

**Critical:** If the M/Y differs by more than 0.5 percentage points, this is a sign that the coarser m-grid (10 vs 30) is losing precision. In that case, increase Nm_egm to 15 or 20 and re-run.

If verification fails, the most likely cause is the borrowing-constraint handling in the `a_egm → a` interpolation. Diagnose by:
1. Plotting `a^egm` vs `a'` for a representative (j, h, s, θ) — should be monotone increasing
2. Checking the share of cells where the constraint binds — should be plausible (10–30% at young ages, lower at older ages)
3. Comparing the c_pol(a, h, s, θ) array between v2 and v3 at the same cells

---

## Phase 4: Final Integration

### 4.1 Apply the optimized solver to the experiments

Once `ge_model_v3_egm.jl` passes verification, propagate the changes to the two experiment files:

```bash
cp ge_model_v3_egm.jl ge_model_kappa30_v3.jl
sed -i 's/const κ_rep      = 0.50/const κ_rep      = 0.30/' ge_model_kappa30_v3.jl
sed -i 's/ge_lifecycle\.csv/ge_lifecycle_kappa30.csv/g' ge_model_kappa30_v3.jl
sed -i 's/ge_summary\.csv/ge_summary_kappa30.csv/g' ge_model_kappa30_v3.jl
sed -i 's/ge_history\.csv/ge_history_kappa30.csv/g' ge_model_kappa30_v3.jl
sed -i 's|"plots"|"plots_kappa30"|g' ge_model_kappa30_v3.jl

cp ge_model_v3_egm.jl ge_model_taum20_v3.jl
sed -i 's/const τm         = 0.00/const τm         = -0.20/' ge_model_taum20_v3.jl
sed -i 's/ge_lifecycle\.csv/ge_lifecycle_taum20.csv/g' ge_model_taum20_v3.jl
sed -i 's/ge_summary\.csv/ge_summary_taum20.csv/g' ge_model_taum20_v3.jl
sed -i 's/ge_history\.csv/ge_history_taum20.csv/g' ge_model_taum20_v3.jl
sed -i 's|"plots"|"plots_taum20"|g' ge_model_taum20_v3.jl
```

### 4.2 Run all three (baseline + two experiments)

```bash
julia --project=. --threads=auto ge_model_v3_egm.jl > ge_run_v3_baseline.log 2>&1
julia --project=. --threads=auto ge_model_kappa30_v3.jl > ge_run_kappa30_v3.log 2>&1
julia --project=. --threads=auto ge_model_taum20_v3.jl > ge_run_taum20_v3.log 2>&1
```

Expected: each run completes in 2–5 minutes. Total: under 15 minutes for all three.

### 4.3 Deliver

| File | Purpose |
|------|---------|
| `ge_model_v3_egm.jl` | Optimized baseline solver |
| `ge_model_kappa30_v3.jl` | Optimized κ=0.30 variant |
| `ge_model_taum20_v3.jl` | Optimized τ^m=−0.20 variant |
| `ge_summary.csv`, `ge_summary_kappa30.csv`, `ge_summary_taum20.csv` | Aggregates |
| `ge_lifecycle.csv`, `ge_lifecycle_kappa30.csv`, `ge_lifecycle_taum20.csv` | Lifecycle profiles |
| `plots/`, `plots_kappa30/`, `plots_taum20/` | Diagnostic plots |
| `OPTIMIZATION_REPORT.md` | Brief report: v0 → v3 speedup, verification checks passed, any caveats |

---

## Fallback Plan

If Phase 3 (EGM) hits an unexpected obstacle and verification fails after 4 hours of debugging, **stop and ship v2**.

The Phase 1 + Phase 2 combination (threading + type stability + @inbounds) should already deliver 6–10x speedup, bringing the run time to ~10–15 minutes per experiment. That is sufficient for the June 5 seminar. EGM can be revisited after the seminar.

The hierarchy is: working slow > broken fast. Always.

---

## Quality Checklist

Before declaring optimization complete:

1. All three checks (Phase 1, 2, 3 verification gates) passed.
2. Both experiments (κ=0.30 and τ^m=−0.20) run with the optimized code.
3. The aggregate K, L, Y, r, w, τp, M/Y values for the baseline match the v0 values to within the specified tolerances.
4. Wall-clock for the baseline run is reported in `OPTIMIZATION_REPORT.md`.
5. The Euler residual diagnostic (`ge_06_euler_residuals.png`) shows comparable or better residuals than v0 (mean log10 ≤ −7).

---

*Instructions prepared by Nina · BDH Core Team · May 2026*

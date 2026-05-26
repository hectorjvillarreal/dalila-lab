################################################################################
# probe_ge_iter1_via_driver.jl
#
# Same as probe_ge_iter1.jl but FIRST applies the active_τω shim and
# function redefinitions from run_aging_ssvs.jl, then runs RUN 1 iter 1.
# If L_new comes back as ~17 like the original probe, the redefinitions
# are fine. If it comes back as ~0 (matching the diverging run), the
# override pattern is the bug.
################################################################################

using Printf, Statistics
const GE_SRC = joinpath(@__DIR__, "..", "ge_model_gender.jl")
include(GE_SRC)

@assert gender_gap

# ── Replicate run_aging_ssvs.jl shim + redefinitions ────────────────────────
const active_τω = Ref{Float64}(τw)

@eval Main begin
    function labor_supply(j::Int, h::Float64, η::Float64,
                          ig::Int, iθ::Int)::Float64
        if j >= j_R; return 0.0; end
        ν_j = productivity(j, h, η, ig, iθ)
        ν_j <= 0.0 && return 0.0
        numer = w_now * ν_j * (1.0 - active_τω[] - τp_now)
        denom = (1.0 + τc) * Ψ_labor
        ℓ_star = (numer / denom) ^ (1.0 / ν_pref)
        return clamp(ℓ_star, 0.0, 1.0)
    end

    function available_resources(a::Float64, h::Float64, η::Float64,
                                  ig::Int, iθ::Int, j::Int)::Float64
        if j < j_R
            ℓ   = labor_supply(j, h, η, ig, iθ)
            ν_j = productivity(j, h, η, ig, iθ)
            labor_income = w_now * ν_j * ℓ * (1.0 - active_τω[] - τp_now)
            return (1.0 + rn_now) * a + labor_income
        else
            return (1.0 + rn_now) * a + pen_now
        end
    end

    function update_pension_taxes!(L_eff::Float64)
        global τp_now, pen_now, wn_now
        if N_W_now > 0.0
            τp_now  = κ_rep * N_R_now / N_W_now
            pen_now = κ_rep * w_now * L_eff / N_W_now
        end
        wn_now = w_now * (1.0 - active_τω[] - τp_now)
    end

    function compute_debt!(C::Float64, L::Float64, K::Float64,
                           M::Float64, Y::Float64)
        global B_debt_now
        G = gy * Y
        primary = τc*C + τw*w_now*L + τk*r_now*K + τm*M - G
        B_debt_now = primary / (rn_now - n_p)
    end
end
active_τω[] = τw

println("="^72)
println("  Probe iter 1 — WITH driver redefinitions applied")
println("="^72)
@printf "  nthreads=%d  J=%d  damp_ge=%.2f  active_τω[]=%.4f  τw=%.4f\n" Threads.nthreads() J damp_ge active_τω[] τw

# ── Sanity: call labor_supply directly and compare to manual formula ────────
test_j, test_h, test_η, test_ig, test_iθ = 5, 0.5, 0.0, 1, 1
# Need prices first
grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
π_η .= π_mat; η_grid .= η_vec
compute_ergodic!()
K = K_init; L = L_init
update_prices!(K, L)
global wn_now = w_now * (1.0 - τw - τp_now)

ν_test = productivity(test_j, test_h, test_η, test_ig, test_iθ)
ℓ_redef = labor_supply(test_j, test_h, test_η, test_ig, test_iθ)
ℓ_manual_τw   = clamp((w_now * ν_test * (1.0 - τw - τp_now) / ((1.0 + τc) * Ψ_labor))^(1.0/ν_pref), 0.0, 1.0)
ℓ_manual_atau = clamp((w_now * ν_test * (1.0 - active_τω[] - τp_now) / ((1.0 + τc) * Ψ_labor))^(1.0/ν_pref), 0.0, 1.0)
@printf "\n  labor_supply sanity at (j=5,h=0.5,η=0,M,θL): ν=%.4f\n" ν_test
@printf "    redef call          → ℓ = %.6f\n" ℓ_redef
@printf "    manual (τw=%.2f)   → ℓ = %.6f\n" τw ℓ_manual_τw
@printf "    manual (active_τω) → ℓ = %.6f\n" ℓ_manual_atau

# ── Run iter 1 ──────────────────────────────────────────────────────────────
println("\n── iter 1 ──")
@printf "  prices: r=%.4f w=%.4f rn=%.4f τp=%.4f pen=%.4f\n" r_now w_now rn_now τp_now pen_now

t0 = time()
solve_household!()
@printf "  household solve: %.1f s  (refinement: %d cells)\n" (time()-t0) n_refined[]

forward_distribution!()
compute_population!()
@printf "  N_W=%.4f  N_R=%.4f  Σ Φ=%.4f\n" N_W_now N_R_now sum(Φ)

update_pension_taxes!(L)
@printf "  after update_pension_taxes!: τp=%.4f  pen=%.4f  wn=%.4f\n" τp_now pen_now wn_now

A_dom, L_new, C, M, Λvoid = aggregate_all()
Y = A_TFP * K^α * L^(1.0-α)
compute_debt!(C, L, K, M, Y)
@printf "  aggregates: A_dom=%.4f  L_new=%.4f  C=%.4f  M=%.4f  Λvoid=%.4f  Y=%.4f  B=%.4f\n" A_dom L_new C M Λvoid Y B_debt_now

K_target = A_dom - B_debt_now
K_upd = max(damp_ge*K_target + (1-damp_ge)*K, 0.5)
L_upd = max(damp_ge*L_new + (1-damp_ge)*L, 0.5)
@printf "  K_target=%.4f  L_new=%.4f  →  K_upd=%.4f  L_upd=%.4f\n" K_target L_new K_upd L_upd

# ── Also: total ν·ℓ over all cells (without mass weighting) ─────────────────
total_νℓ = 0.0
zero_ℓ_cells = 0
nonzero_cells = 0
for j in 1:(j_R-1), ig in 1:Ng, iθ in 1:Nθ, ia in 0:NA, ih in 0:NH, is in 1:Nη
    ν_j = productivity(j, h_grid[ih], η_grid[is], ig, iθ)
    ℓ = l_pol[j, ig, ia, ih, is, iθ]
    total_νℓ += ν_j * ℓ
    ℓ == 0.0 ? (zero_ℓ_cells += 1) : (nonzero_cells += 1)
end
@printf "\n  l_pol diagnostic: total Σν·ℓ (unweighted) = %.4f\n" total_νℓ
@printf "  l_pol cells: zero = %d  nonzero = %d\n" zero_ℓ_cells nonzero_cells

println("\nDone.")

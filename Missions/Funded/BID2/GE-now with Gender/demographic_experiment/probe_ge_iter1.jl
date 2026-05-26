################################################################################
# probe_ge_iter1.jl
#
# Manually run ONE iter of solve_ge! at the default initial point (K=12, L=10)
# with gender_gap = true, then dump everything: targets, aggregates,
# per-(j, ig, iθ) labor supply, and the iter-2 update under the current damp.
#
# Question to answer: is the gender_gap divergence caused by (a) L_target
# collapsing to near-zero at iter 1, (b) K_target overshooting because B
# computation amplifies a small primary surplus, or (c) the household-side
# labor supply itself going to zero somewhere?
#
# Runs in ~1-2 min threaded — one household solve, no GE outer loop.
################################################################################

using Printf, Statistics
const GE_SRC = joinpath(@__DIR__, "..", "ge_model_gender.jl")
include(GE_SRC)

@assert gender_gap "gender_gap must be true for this probe"
println("="^72)
println("  Probe: iter 1 of solve_ge! with gender_gap = true")
println("="^72)
@printf "  nthreads = %d   J = %d   damp_ge = %.2f\n" Threads.nthreads() J damp_ge

# Init exactly as solve_ge! does.
grid_Cons_Grow(a_grid, NA + 1, a_l, a_u, a_grow)
grid_Cons_Grow(h_grid, NH + 1, h_l, h_u, h_grow)
π_mat, η_vec = rouwenhorst(Nη, ρ_AR, σ_ε, 0.0)
π_η .= π_mat; η_grid .= η_vec
compute_ergodic!()

K = K_init  # 12.0
L = L_init  # 10.0

# === ITER 1 — same sequence as solve_ge! ====================================
println("\n── iter 1 ──")
@printf "  start: K = %.4f   L = %.4f\n" K L

update_prices!(K, L)
global wn_now = w_now * (1.0 - τw - τp_now)   # iter 1 branch in solve_ge!
@printf "  after update_prices!: r = %.4f  w = %.4f  rn = %.4f  τp_now = %.4f  pen_now = %.4f\n" r_now w_now rn_now τp_now pen_now

println("\n  solving household block …")
t0 = time()
solve_household!()
@printf "  household solve: %.1f s   (refinement: %d cells)\n" (time()-t0) n_refined[]

forward_distribution!()
compute_population!()
@printf "  after forward + population: Σ Φ = %.6f   N_W = %.4f   N_R = %.4f   N_R/N_W = %.4f\n" sum(Φ) N_W_now N_R_now (N_R_now/N_W_now)

update_pension_taxes!(L)
@printf "  after update_pension_taxes!: τp_now = %.4f   pen_now = %.4f   wn_now = %.4f\n" τp_now pen_now wn_now

A_dom, L_new, C, M, Λvoid = aggregate_all()
Y = A_TFP * K^α * L^(1.0 - α)
compute_debt!(C, L, K, M, Y)

@printf "\n  aggregates: A_dom = %.4f   L_new = %.4f   C = %.4f   M = %.4f   Λvoid = %.4f\n" A_dom L_new C M Λvoid
@printf "  output:     Y = %.4f   G = %.4f   δK = %.4f\n" Y (gy*Y) (δ_cap*K)
@printf "  debt:       B = %.4f   B/Y = %.4f\n" B_debt_now (B_debt_now/Y)

K_target = A_dom - B_debt_now
@printf "\n  TARGETS:    K_target = A_dom - B = %.4f      L_new = %.4f\n" K_target L_new

K_upd = max(damp_ge * K_target + (1.0 - damp_ge) * K, 0.5)
L_upd = max(damp_ge * L_new   + (1.0 - damp_ge) * L, 0.5)
@printf "  UPDATE:     K_upd = %.4f      L_upd = %.4f      (damp = %.2f, floor = 0.5)\n" K_upd L_upd damp_ge

# === Per-(ig, iθ) labor + asset diagnostics =================================
println("\n── per-(ig, iθ) breakdown ──")
@printf "  %-8s %12s %12s %12s %12s %12s\n" "type" "Σmass" "Σmass·a" "Σmass·c" "Σ ν·ℓ (work)" "Σmass·m"

ig_lbl = (1 => "M", 2 => "F")
iθ_lbl = (1 => "θL", 2 => "θH")
for ig in 1:Ng, iθ in 1:Nθ
    Σmass = 0.0; Σmasa = 0.0; Σmasc = 0.0; Σνℓ = 0.0; Σmasm = 0.0
    for j in 1:J, ia in 0:NA, ih in 0:NH, is in 1:Nη
        mass = Φ[j, ig, ia, ih, is, iθ]
        mass < 1e-18 && continue
        Σmass += mass
        Σmasa += mass * a_grid[ia]
        Σmasc += mass * c_pol[j, ig, ia, ih, is, iθ]
        Σmasm += mass * m_pol[j, ig, ia, ih, is, iθ]
        if j < j_R
            ν_j = productivity(j, h_grid[ih], η_grid[is], ig, iθ)
            ℓ = l_pol[j, ig, ia, ih, is, iθ]
            Σνℓ += mass * ν_j * ℓ
        end
    end
    @printf "  %-8s %12.4e %12.4e %12.4e %12.4e %12.4e\n" "$(ig_lbl[ig]),$(iθ_lbl[iθ])" Σmass Σmasa Σmasc Σνℓ Σmasm
end

# === Labor by age band, both sexes, both skills =============================
println("\n── effective labor ν·ℓ by age band (j) ──")
@printf "  %-3s %12s %12s %12s %12s\n" "j" "M,θL" "M,θH" "F,θL" "F,θH"
for j in 1:(j_R - 1)
    row = zeros(2, 2)
    for ig in 1:Ng, iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            mass = Φ[j, ig, ia, ih, is, iθ]
            mass < 1e-18 && continue
            ν_j = productivity(j, h_grid[ih], η_grid[is], ig, iθ)
            ℓ = l_pol[j, ig, ia, ih, is, iθ]
            row[ig, iθ] += mass * ν_j * ℓ
        end
    end
    @printf "  %-3d %12.4e %12.4e %12.4e %12.4e\n" j row[1,1] row[1,2] row[2,1] row[2,2]
end

println()
println("Done.")

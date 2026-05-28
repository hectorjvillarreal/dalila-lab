################################################################################
#  vsl.jl
#
#  Value of a Statistical Life helper for the SMM calibration.
#
#  Derivation (modelwithgender.tex §3, with envelope on a):
#       V_j  = u(c, ℓ, h) + β · ψ_{j+1}(h') · E_η[V_{j+1}(a', h', η', g, θ)]
#       ∂V/∂ψ_{j+1} = β · E_η[V_{j+1}]                      (direct)
#       ∂V/∂a       = u_c(c, ℓ, h)                          (envelope)
#
#  ⇒ MRS(mortality risk, money) at state (a, h, η, g, θ) at age j is
#
#       VSL_j(state) = (β · E_η[V_{j+1}]) / u_c
#
#  in units of "model consumption units per unit of mortality reduction over a
#  5-year period". To get USD per saved statistical life we multiply by:
#
#       usd_per_unit_c   — calibrated $ value of one unit of model consumption
#       periods_per_year — 5 (the model period length)
#
#  Convention: report VSL at a reference age (paper §4: prime-age),
#  mass-weighted over (g, θ, a, h, η) at that age using Φ.
#
#  Requires: pe_solver_for_smm.jl already included (uses V_pol, c_pol, l_pol,
#  Φ, π_η, η_grid, β_pref, J, Ng, Nθ, Nη, NA, NH, marginal_utility_c).
################################################################################

"""
    vsl_at(usd_scale; j_ref::Int = usd_scale.reference_age_period)

Mass-weighted VSL at age `j_ref`, in USD per statistical life saved.

Computation walks every (ig, ia, ih, is, iθ) cell at age j_ref:
   uc       = u_c(c_pol, l_pol, h_grid[ih])
   E[V']    = Σ_{is'} π_η[is, is']·V_pol[j_ref+1, ig, ia, ih, is', iθ]    (via
              the stored next-period policies — we evaluate at (a'=aplus_pol,
              h'=hnext_pol)? NO. We need V at the same (a,h) since the marginal
              mortality reduction acts AT the current state. So use V_pol at
              the SAME (ia, ih) grid point: there's no continuation transition
              to evaluate when we ask "given my current state, how much would
              I pay for less mortality risk?")

In implementation we use the model identity:
   V_pol[j_ref, ig, ia, ih, is, iθ]
     = u_now + β · ψ_{j_ref+1}(h') · E_η[V_{j_ref+1}(...)]

so β · E_η[V_{j_ref+1}] = (V_pol[j_ref] − u_now) / ψ_{j_ref+1}(h'). This uses
data we already have without an extra interp, but it requires ψ at the chosen
h_next (which we get from `survival(j_ref+1, hnext_pol[...], ig)`). Cells with
ψ ≤ ε are dropped (VSL is undefined at zero survival).

Returns (vsl_usd, n_cells_used, share_mass_used).
"""
function vsl_at(usd_scale; j_ref::Int = usd_scale.reference_age_period)
    j_ref >= 1 || error("reference age period must be ≥ 1")
    j_ref <= J - 1 || error("reference age period must be ≤ J-1 (= $(J-1)) so j_ref+1 exists")

    num    = 0.0     # mass-weighted sum of VSL_j_ref(state) · Φ
    denom  = 0.0     # total mass used
    n_used = 0
    for ig in 1:Ng, iθ in 1:Nθ
        for ia in 0:NA, ih in 0:NH, is in 1:Nη
            mass = Φ[j_ref, ig, ia, ih, is, iθ]
            mass < 1e-18 && continue

            c_now = c_pol[j_ref, ig, ia, ih, is, iθ]
            ℓ_now = l_pol[j_ref, ig, ia, ih, is, iθ]
            h_now = h_grid[ih]
            uc = marginal_utility_c(c_now, ℓ_now, h_now)
            uc > 1e-12 || continue

            # u_now at this cell
            u_now = utility(c_now, ℓ_now, h_now)

            # β · E_η[V_{j_ref+1}] recovered from the Bellman identity.
            h_n  = hnext_pol[j_ref, ig, ia, ih, is, iθ]
            ψ    = survival(j_ref + 1, h_n, ig)
            ψ > 1e-9 || continue

            V_now      = V_pol[j_ref, ig, ia, ih, is, iθ]
            β_EV_next  = (V_now - u_now) / ψ      # = β · ψ · E[V'] / ψ

            vsl_model_units = β_EV_next / uc
            num   += mass * vsl_model_units
            denom += mass
            n_used += 1
        end
    end

    denom > 0 || error("no cells contributed to VSL — distribution at j_ref is empty?")
    vsl_model = num / denom

    # Convert model units → USD per statistical life.
    # One unit of model consumption per period = usd_per_unit_c.
    # A period = periods_per_year (= 5) years, so per-period VSL × 1 = lifetime
    # VSL (since "statistical life" already integrates over remaining years —
    # the model's continuation value E[V_{j+1}] already discounts future
    # periods). So we only scale by usd_per_unit_c, not by years.
    # (Multiplying by periods_per_year would inflate by 5×; this is a common
    # convention pitfall — flag it in the report.)
    vsl_usd = vsl_model * usd_scale.usd_per_unit_c
    return (; vsl_usd, vsl_model, n_used,
            share_mass_used = denom / sum(Φ[j_ref, :, :, :, :, :]))
end

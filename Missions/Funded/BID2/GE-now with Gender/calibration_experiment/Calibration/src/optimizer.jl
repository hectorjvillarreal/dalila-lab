################################################################################
#  optimizer.jl
#
#  Nelder-Mead driver with multistart for the SMM objective.
#
#  Uses Optim.jl's Nelder-Mead implementation. Parameters live in the
#  unconstrained x-space; bounds are enforced by transforms in objective.jl.
#
#  Multistart: N random perturbations from `theta_init.init`, each run to
#  convergence; report the best result and dispersion across starts as an
#  identification diagnostic.
#
#  Two entry points:
#      run_one_start(obj, x0; ...)   — single Nelder-Mead run
#      run_multistart(obj, io; ...)   — N starts, returns the best + log
#
#  Requires Optim.jl (added to Project.toml).
################################################################################

using Optim
using Random

# ─── Single Nelder-Mead run ─────────────────────────────────────────────────
"""
    run_one_start(obj, x0; maxiter=500, simplex_tol=1e-5, verbose=true)

One Nelder-Mead run from initial unconstrained vector `x0`. Returns
(x_hat, Q_hat, n_iter, converged::Bool).
"""
function run_one_start(obj, x0::Vector{Float64};
                       maxiter::Int = 500,
                       simplex_tol::Float64 = 1e-5,
                       verbose::Bool = true)
    opts = Optim.Options(iterations = maxiter,
                         x_abstol   = simplex_tol,
                         show_trace = verbose,
                         show_every = 10)
    res = Optim.optimize(obj, x0, NelderMead(), opts)
    return (; x_hat     = Optim.minimizer(res),
              Q_hat     = Optim.minimum(res),
              n_iter    = Optim.iterations(res),
              converged = Optim.converged(res))
end

# ─── Multistart driver ──────────────────────────────────────────────────────
"""
    run_multistart(obj, io; n_starts=8, jitter=0.20, seed=20260525, ...)

Run `n_starts` Nelder-Mead optimizations. Start 1 uses `io.theta_init.init`
exactly; starts 2..N use init perturbed in unconstrained-space by Gaussian
noise of std `jitter`. Returns a Vector of single-start results plus the
best-overall and a summary table.
"""
function run_multistart(obj, io::NamedTuple;
                        n_starts::Int = 8,
                        jitter::Float64 = 0.20,
                        seed::Int = 20260525,
                        maxiter::Int = 500,
                        simplex_tol::Float64 = 1e-5,
                        verbose::Bool = false)
    ti = io.theta_init
    fi = free_idx(ti)                                  # only free dims optimize
    n_free = length(fi)
    x_init_full = vec_to_unconstrained(copy(ti.init), ti)
    x_init_free = x_init_full[fi]
    obj_free    = make_free_objective(obj)             # injects frozen, calls obj

    if verbose
        n_frozen = length(ti.names) - n_free
        if n_frozen > 0
            @printf "Multistart over %d free of %d params (%d frozen: %s)\n" n_free length(ti.names) n_frozen join(ti.names[ti.frozen], ", ")
        end
    end

    rng = MersenneTwister(seed)

    starts = Vector{Vector{Float64}}(undef, n_starts)
    starts[1] = copy(x_init_free)                      # exact init (free subset)
    for k in 2:n_starts
        starts[k] = x_init_free .+ jitter .* randn(rng, n_free)
    end

    results = []
    for (k, x0) in enumerate(starts)
        verbose && println("\n──── Multistart $(k)/$(n_starts) ────")
        try
            res = run_one_start(obj_free, x0; maxiter=maxiter,
                                simplex_tol=simplex_tol, verbose=verbose)
            push!(results, (; start_idx=k, res...))
            verbose && @printf "  start %d: Q = %.6e, iter = %d, conv = %s\n" k res.Q_hat res.n_iter res.converged
        catch e
            push!(results, (; start_idx=k, x_hat=fill(NaN, n_free),
                            Q_hat=Inf, n_iter=0, converged=false))
            verbose && println("  start $k: FAILED with $(typeof(e))")
        end
    end

    Q_vals = [r.Q_hat for r in results]
    best_k = argmin(Q_vals)
    return (; results, best = results[best_k])
end

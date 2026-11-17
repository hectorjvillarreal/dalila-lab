# B1a rough fit (note §5, criterion 4) and parameter recovery (criterion 6).
# Modes:  julia -t auto --project=. experiments/fit.jl search  [N]     random search + NM refine
#         julia -t auto --project=. experiments/fit.jl recover [M]     recovery on M synthetic datasets
# Writes experiments/results/*.txt. Conditional mechanism reads only; no price statements.
using Random, Statistics, Printf, Dates
using CryptoABM, CryptoABM.ABMCore, CryptoABM.Moments, CryptoABM.CryptoAdapter
include(joinpath(@__DIR__, "..", "targets", "Targets.jl")); using .Targets

const RES = joinpath(@__DIR__, "results"); mkpath(RES)
const SIGBAR = Targets.sigma_bar_hourly().σbar
const R = 10                         # replications per draw (note §5), common random numbers
const DAYS = 1040

# ---------------------------------------------------------------- targets and weights
const DR = Targets.daily_returns("BTC-USD")
const PIDX = findall(t -> Targets.POST[1] < t <= Targets.POST[2], DR.dates)
const XR = DR.r[PIDX]                                     # 1,040 post-ETF log returns
const LOWR = [DR.d.low[i+1] / DR.d.close[i] - 1 for i in PIDX]   # prior close → low (simple)
gapstat(r, lowr) = (w = sortperm(r)[1:10]; mean(lowr[w]) - mean(exp.(r[w]) .- 1))
fullvec(r, lowr) = vcat(moment_vector(r), gapstat(r, lowr))
const NAMES = vcat(MOMENT_NAMES, :gap)
const MD = fullvec(XR, LOWR)

"Moving-block bootstrap (block 20) of the data moment vector → s.d. and 95 % bands."
function bootstrap(; B = 1000, block = 20, seed = 2026)
    rng = Xoshiro(seed); n = length(XR)
    M = zeros(length(MD), B)
    for b in 1:B
        idx = Int[]
        while length(idx) < n
            s = rand(rng, 1:n-block+1); append!(idx, s:s+block-1)
        end
        idx = idx[1:n]
        M[:, b] = fullvec(XR[idx], LOWR[idx])
    end
    sdv = vec(std(M; dims = 2))
    lo = [quantile(M[k, :], 0.025) for k in axes(M, 1)]
    hi = [quantile(M[k, :], 0.975) for k in axes(M, 1)]
    sdv, lo, hi
end
const SDB, LO95, HI95 = bootstrap()

# ---------------------------------------------------------------- parameters searched
# name, low, high, log-scale?
const BOX = [(:λ0, 0.05, 3.0, true), (:σ_ε, 0.002, 0.05, true), (:w_m, 0.01, 0.30, false),
             (:β, 0.2, 3.0, false), (:w_l, 0.02, 0.30, false), (:L_median, 3.0, 20.0, true),
             (:κ, 0.0, 1.5, false), (:φ, 0.0, 0.8, false), (:ρ, 0.05, 0.5, false),
             (:D_median, 0.15, 0.50, false), (:s_D, 0.10, 1.0, false)]
const PNAMES = first.(BOX)
"Map u ∈ [0,1]^k to parameters."
function decode(u)
    v = similar(u)
    for (k, (_, a, b, lg)) in enumerate(BOX)
        x = clamp(u[k], 0.0, 1.0)
        v[k] = lg ? exp(log(a) + x * (log(b) - log(a))) : a + x * (b - a)
    end
    v
end
encode(v) = [lg ? (log(v[k]) - log(a)) / (log(b) - log(a)) : (v[k] - a) / (b - a) for (k, (_, a, b, lg)) in enumerate(BOX)]
function params_from(v)
    d = Dict(zip(PNAMES, v))
    wm, wl = d[:w_m], d[:w_l]
    s = wm + wl; s > 0.5 && (wm *= 0.5 / s; wl *= 0.5 / s)        # w_c = 0.5 fixed; shares ≤ 1
    Params(σbar = SIGBAR, λ0 = d[:λ0], σ_ε = d[:σ_ε], w_m = wm, β = d[:β], w_l = wl,
           L_median = d[:L_median], κ = d[:κ], φ = d[:φ], ρ = d[:ρ], D_median = d[:D_median], s_D = d[:s_D])
end

# ---------------------------------------------------------------- simulation and objective
struct Aborted <: Exception; msg::String; end
function sim_vec(p::Params, seed)
    rng = Xoshiro(seed)
    w = build_world(p, rng)
    res = simulate!(w, SimConfig(K = p.K, days = DAYS, burnin = 120), rng)
    r = diff(log.(res.close)); lowr = res.low[2:end] ./ res.close[1:end-1] .- 1
    any(!isfinite, r) && throw(Aborted("non-finite path"))
    fullvec(r, lowr)
end
"Mean model moments over R common-random-number replications (seeds base+1..base+R)."
function model_moments(p::Params; base = 0)
    M = zeros(length(MD), R)
    for s in 1:R
        M[:, s] = sim_vec(p, base + s)
    end
    vec(mean(M; dims = 2))
end
function objective(u, target; base = 0, log = nothing)
    p = params_from(decode(u))
    m = try
        model_moments(p; base)
    catch e
        log !== nothing && println(log, "aborted draw: ", sprint(showerror, e))
        return Inf, fill(NaN, length(MD))
    end
    sum(((m .- target) ./ SDB) .^ 2), m
end

# ---------------------------------------------------------------- Nelder–Mead on [0,1]^k
function nelder_mead(f, x0; step = 0.1, maxit = 300, tol = 1e-4)
    k = length(x0)
    X = [copy(x0)]; for i in 1:k; x = copy(x0); x[i] = clamp(x[i] + (x[i] < 0.5 ? step : -step), 0, 1); push!(X, x); end
    F = [f(x) for x in X]
    it = 0
    while it < maxit
        it += 1
        o = sortperm(F); X = X[o]; F = F[o]
        (F[end] - F[1]) < tol * (abs(F[1]) + tol) && break
        c = sum(X[1:end-1]) / k
        xr = clamp.(c .+ (c .- X[end]), 0, 1); fr = f(xr)
        if fr < F[1]
            xe = clamp.(c .+ 2 .* (c .- X[end]), 0, 1); fe = f(xe)
            fe < fr ? (X[end] = xe; F[end] = fe) : (X[end] = xr; F[end] = fr)
        elseif fr < F[end-1]
            X[end] = xr; F[end] = fr
        else
            xc = clamp.(c .+ 0.5 .* (X[end] .- c), 0, 1); fc = f(xc)
            if fc < F[end]
                X[end] = xc; F[end] = fc
            else
                for i in 2:k+1; X[i] = X[1] .+ 0.5 .* (X[i] .- X[1]); F[i] = f(X[i]); end
            end
        end
    end
    o = argmin(F); X[o], F[o], it
end

function report(io, label, v, m)
    println(io, "## ", label)
    for (k, nm) in enumerate(PNAMES); @printf(io, "  %-9s = %.4f\n", nm, v[k]); end
    inside = 0
    for (k, nm) in enumerate(NAMES)
        ok = LO95[k] <= m[k] <= HI95[k]; inside += ok
        @printf(io, "  %-12s model %9.4f  data %9.4f  95%% band [%9.4f, %9.4f]  %s\n", nm, m[k], MD[k], LO95[k], HI95[k], ok ? "inside" : "OUTSIDE")
    end
    @printf(io, "  moments inside 95%% bands: %d of %d\n", inside, length(NAMES))
end

# ---------------------------------------------------------------- modes
function search(N)
    stamp = Dates.format(now(), "yyyymmdd_HHMM")
    io = open(joinpath(RES, "fit_$(stamp).txt"), "w")
    println(io, "# B1a rough fit — $(now()) — threads $(Threads.nthreads()), N = $N, R = $R, σ̄ = $SIGBAR")
    rng = Xoshiro(11)
    U = [rand(rng, length(BOX)) for _ in 1:N]
    J = fill(Inf, N); lk = ReentrantLock()
    Threads.@threads for i in 1:N
        j, _ = objective(U[i], MD; log = nothing)
        lock(lk) do; J[i] = j; end
    end
    nab = count(isinf, J)
    @printf(io, "random search: best J = %.2f, median J = %.2f, aborted/non-finite draws = %d\n", minimum(J), median(filter(isfinite, J)), nab)
    starts = sortperm(J)[1:min(8, N)]
    out = Vector{Any}(undef, length(starts))
    Threads.@threads for s in eachindex(starts)
        x, fx, it = nelder_mead(u -> objective(u, MD)[1], U[starts[s]])
        out[s] = (x, fx, it)
    end
    best = argmin([o[2] for o in out])
    for (s, (x, fx, it)) in enumerate(out)
        @printf(io, "NM start %d: J %.2f → %.2f in %d iterations\n", s, J[starts[s]], fx, it)
    end
    x = out[best][1]
    _, m = objective(x, MD)
    report(io, "best fit (J = $(round(out[best][2]; digits = 2)))", decode(x), m)
    println(io, "u_best = ", x)
    close(io)
    println(read(joinpath(RES, "fit_$(stamp).txt"), String))
end

"Recovery: synthetic data from θ* (one path of DAYS days, seed 1000+j); refit with the same NM."
function recover(M; ufile = nothing)
    stamp = Dates.format(now(), "yyyymmdd_HHMM")
    io = open(joinpath(RES, "recover_$(stamp).txt"), "w")
    ustar = ufile === nothing ? error("pass the u_best line file") : eval(Meta.parse(split(readlines(ufile)[end], " = ")[2]))
    vstar = decode(ustar)
    println(io, "# B1a parameter recovery — $(now()) — truth = best fit; M = $M synthetic paths; same NM; R = $R")
    keyp = [:w_l, :L_median, :s_D, :κ]
    est = Vector{Vector{Float64}}(undef, M)
    Threads.@threads for j in 1:M
        tgt = sim_vec(params_from(vstar), 1000 + j)            # one synthetic 'data' path
        rng = Xoshiro(500 + j)
        u0 = clamp.(ustar .+ 0.15 .* (2 .* rand(rng, length(ustar)) .- 1), 0, 1)
        x, fx, _ = nelder_mead(u -> objective(u, tgt; base = 2000 + 100j)[1], u0)
        est[j] = decode(x)
    end
    for k in keyp
        i = findfirst(==(k), PNAMES)
        e = [est[j][i] for j in 1:M]
        @printf(io, "  %-9s truth %.4f  estimates mean %.4f  sd %.4f  min %.4f  max %.4f\n", k, vstar[i], mean(e), std(e), minimum(e), maximum(e))
    end
    println(io, "  all parameters, mean |estimate − truth| / range:")
    for (i, (nm, a, b, _)) in enumerate(BOX)
        e = [est[j][i] for j in 1:M]
        @printf(io, "    %-9s %.3f\n", nm, mean(abs.(e .- vstar[i])) / (b - a))
    end
    close(io)
    println(read(joinpath(RES, "recover_$(stamp).txt"), String))
end

mode = length(ARGS) >= 1 ? ARGS[1] : "search"
if mode == "search"
    search(length(ARGS) >= 2 ? parse(Int, ARGS[2]) : 2000)
elseif mode == "recover"
    recover(length(ARGS) >= 2 ? parse(Int, ARGS[2]) : 8; ufile = ARGS[3])
end

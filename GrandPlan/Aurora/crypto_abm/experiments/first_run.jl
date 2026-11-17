# B1a first run: default parameters (note §4 initial ranges, NOT estimates) vs post-ETF BTC
# targets, plus the §11.5 ablations. Conditional mechanism read only; no price statements.
# Run: julia --project=. experiments/first_run.jl   (from GrandPlan/Aurora/crypto_abm)
using Random, Statistics, Printf
using CryptoABM, CryptoABM.ABMCore, CryptoABM.Moments, CryptoABM.CryptoAdapter
include(joinpath(@__DIR__, "..", "targets", "Targets.jl")); using .Targets

const SIGBAR = Targets.sigma_bar_hourly().σbar
const TGT = Targets.window_stats("BTC-USD", Targets.POST...)
const TGAP = Targets.intraday_gap()

function path_stats(p::Params, seed; cascade = true)
    rng = Xoshiro(seed)
    w = build_world(p, rng)
    res = simulate!(w, SimConfig(K = p.K, days = 1040, burnin = 120, cascade = cascade), rng)
    r = diff(log.(res.close))
    mv = moment_vector(r)
    worst = sortperm(r)[1:10]
    lowr = [res.low[i+1] / res.close[i] - 1 for i in worst]
    ccr = [res.close[i+1] / res.close[i] - 1 for i in worst]
    (mv = mv, exk = exkurt(r), gap = mean(lowr) - mean(ccr), maxr = res.max_rounds)
end
function run(label, p; R = 10, cascade = true)
    S = [path_stats(p, s; cascade) for s in 1:R]
    M = reduce(hcat, getfield.(S, :mv))
    m = vec(mean(M; dims = 2)); sd = vec(std(M; dims = 2))
    @printf("%-28s", label)
    for (k, nm) in enumerate(MOMENT_NAMES)
        @printf(" %s=%.4f(%.4f)", nm, m[k], sd[k])
    end
    @printf(" exkurt=%.2f gap=%.4f maxrounds=%d\n", mean(getfield.(S, :exk)), mean(getfield.(S, :gap)), maximum(getfield.(S, :maxr)))
end
open(joinpath(@__DIR__, "results", "first_run_defaults.txt"), "w") do io; redirect_stdout(io) do
@printf("%-28s", "TARGET post-ETF BTC")
for (k, nm) in enumerate(MOMENT_NAMES); @printf(" %s=%.4f", nm, TGT.moments[k]); end
@printf(" exkurt=%.2f gap=%.4f\n", TGT.exkurt, TGAP.gap)
base = Params(σbar = SIGBAR)
run("default", base)
run("ablation: no cascade loop", base; cascade = false)
run("ablation: φ = 0", Params(σbar = SIGBAR, φ = 0.0))
run("ablation: κ = 0", Params(σbar = SIGBAR, κ = 0.0))
run("null: noise only, κ = 0", Params(σbar = SIGBAR, w_c = 0, w_m = 0, w_l = 0, κ = 0.0))
end; end
print(read(joinpath(@__DIR__, "results", "first_run_defaults.txt"), String))

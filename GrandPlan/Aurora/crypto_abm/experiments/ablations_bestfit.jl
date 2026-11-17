# Criterion 5 at the B1a best fit: cascade loop off, φ = 0, κ = 0 (each separately).
# Run: julia -t auto --project=. experiments/ablations_bestfit.jl experiments/results/fit_linear_20261116_2157.txt
fitfile = ARGS[1]; empty!(ARGS); push!(ARGS, "none")
include(joinpath(@__DIR__, "fit.jl"))
using Printf
u = eval(Meta.parse(split(readlines(fitfile)[end], " = ")[2]))
p0 = params_from(decode(u))
mm(p; cascade = true) = begin
    M = zeros(length(MD), R)
    Threads.@threads for s in 1:R
        rng = Xoshiro(s); w = build_world(p, rng)
        res = simulate!(w, SimConfig(K = p.K, days = DAYS, burnin = 120, cascade = cascade), rng)
        r = diff(log.(res.close)); lowr = res.low[2:end] ./ res.close[1:end-1] .- 1
        M[:, s] = fullvec(r, lowr)
    end
    vec(mean(M; dims = 2))
end
setp(p; kw...) = Params(; (k => getfield(p, k) for k in fieldnames(Params))..., kw...)
rows = [("best fit", mm(p0)), ("cascade loop off", mm(p0; cascade = false)),
        ("φ = 0 (permanent impact)", mm(setp(p0; φ = 0.0))), ("κ = 0 (no liquidity withdrawal)", mm(setp(p0; κ = 0.0))),
        ("no leveraged traders (w_l = 0)", mm(setp(p0; w_l = 0.0)))]
open(joinpath(RES, "ablations_bestfit_$(IMPACT).txt"), "w") do io
    @printf(io, "%-32s", "moment"); for (l, _) in rows; @printf(io, " | %-14s", first(l, 14)); end; @printf(io, " | data\n")
    for (k, nm) in enumerate(NAMES)
        @printf(io, "%-32s", nm); for (_, m) in rows; @printf(io, " | %14.4f", m[k]); end; @printf(io, " | %.4f\n", MD[k])
    end
    println(io, "\ncolumns: ", join(first.(rows), " · "))
end
print(read(joinpath(RES, "ablations_bestfit_$(IMPACT).txt"), String))

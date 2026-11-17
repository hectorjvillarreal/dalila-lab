# Is the noise-only ACF|r|₁ at the fitted φ, ρ mechanical (Gaussian returns with negative ACF)?
# Run: julia --project=. experiments/null_check_transient.jl <fit_linear_*.txt>
fitfile = ARGS[1]; empty!(ARGS); push!(ARGS, "none")
include(joinpath(@__DIR__, "fit.jl"))
using Printf
u = eval(Meta.parse(split(readlines(fitfile)[end], " = ")[2])); p0 = params_from(decode(u))
setp(p; kw...) = Params(; (k => getfield(p, k) for k in fieldnames(Params))..., kw...)
open(joinpath(RES, "null_check_transient.txt"), "w") do io
    println(io, "# noise-only paths at the fitted impact parameters — $(basename(fitfile))")
    for (lab, p) in (("noise only, fitted φ, ρ, κ = 0", setp(p0; w_c = 0, w_m = 0, w_l = 0, κ = 0.0)),
                     ("noise only, φ = 0, κ = 0", setp(p0; w_c = 0, w_m = 0, w_l = 0, κ = 0.0, φ = 0.0)))
        rv = [begin rng = Xoshiro(s); w = build_world(p, rng)
                   diff(log.(simulate!(w, SimConfig(K = p.K, days = DAYS, burnin = 120), rng).close)) end for s in 1:R]
        ar = mean([acf(r, 1) for r in rv]); aa = mean([acf(abs.(r), 1) for r in rv])
        # for jointly Gaussian returns with correlation ρ, corr(|X|,|Y|) = (2/(π−2))·(√(1−ρ²) + ρ·asin(ρ) − 1)
        g = (2 / (π - 2)) * (sqrt(1 - ar^2) + ar * asin(ar) - 1)
        @printf(io, "%-34s ACF r₁ %.4f  ACF|r|₁ %.4f  Gaussian-implied ACF|r|₁ from ACF r₁: %.4f  exkurt %.3f\n",
                lab, ar, aa, g, mean(exkurt.(rv)))
    end
end
print(read(joinpath(RES, "null_check_transient.txt"), String))

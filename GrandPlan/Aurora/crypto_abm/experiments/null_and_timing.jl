# Evidence for the report's null-test, κ-only and timing figures (Fina, B1a sign-off fix 6).
# Run: julia --project=. experiments/null_and_timing.jl <fit_linear_*.txt>      (single thread for timing)
fitfile = ARGS[1]; empty!(ARGS); push!(ARGS, "none")
include(joinpath(@__DIR__, "fit.jl"))
using Printf
u = eval(Meta.parse(split(readlines(fitfile)[end], " = ")[2])); p0 = params_from(decode(u))
setp(p; kw...) = Params(; (k => getfield(p, k) for k in fieldnames(Params))..., kw...)
open(joinpath(RES, "null_and_timing.txt"), "w") do io
    println(io, "# null runs and timing — $(now()) — fit: $(basename(fitfile)) — threads $(Threads.nthreads())")
    for (lab, p) in (("noise only, κ = fitted", setp(p0; w_c = 0, w_m = 0, w_l = 0)),
                     ("noise only, κ = 0 (criterion 3 null)", setp(p0; w_c = 0, w_m = 0, w_l = 0, κ = 0.0)),
                     ("agents, κ = 0", setp(p0; κ = 0.0)))
        rv = [begin rng = Xoshiro(s); w = build_world(p, rng)
                   r = diff(log.(simulate!(w, SimConfig(K = p.K, days = DAYS, burnin = 120), rng).close)); r end for s in 1:R]
        a1 = mean([acf(abs.(r), 1) for r in rv]); a5 = mean([acf(abs.(r), 5) for r in rv])
        @printf(io, "%-38s exkurt %.3f  ACF|r|1 %.4f  ACF|r|5 %.4f  Hill %.2f  3σ %.4f  sd %.4f\n", lab,
                mean(exkurt.(rv)), a1, a5, mean(hill.(rv)), mean(three_sigma_share.(rv)), mean(sdev.(rv)))
    end
    sim_vec(p0, 1)                                  # warm-up (compilation)
    ts = [@elapsed(sim_vec(p0, s)) for s in 1:20]
    @printf(io, "timing, one 1,040-day path (+120 burn-in), K = 24, single thread, best linear fit: median %.3f s, min %.3f s, max %.3f s (20 paths)\n",
            median(ts), minimum(ts), maximum(ts))
end
print(read(joinpath(RES, "null_and_timing.txt"), String))

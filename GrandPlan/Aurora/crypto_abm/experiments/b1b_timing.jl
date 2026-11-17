# B1b timing gate (design note B0 v1.2 §8, criterion 8).
# Decision rule, fixed before measuring (2026-11-17): keep the GPU path only if, at 10,000
# simulations, it is ≥ 3× faster end-to-end than the 16-thread CPU batch AND its moments match
# the CPU's within Monte Carlo error (all |z| < 3 on 1,000-simulation means, both impact laws).
# Run: julia -t 16 --project=. experiments/b1b_timing.jl <fit_linear_*.txt> <fit_sqrt_*.txt>
fl, fs = ARGS[1], ARGS[2]; empty!(ARGS); push!(ARGS, "none")
include(joinpath(@__DIR__, "fit.jl"))
using CUDA, Printf
include(joinpath(@__DIR__, "..", "src", "adapters", "crypto", "gpu", "BatchGPU.jl")); using .BatchGPU

ubest(f) = eval(Meta.parse(split(readlines(f)[end], " = ")[2]))
setp(p; kw...) = Params(; (k => getfield(p, k) for k in fieldnames(Params))..., kw...)
const PL = setp(params_from(decode(ubest(fl))); impact = :linear)
const PS = setp(params_from(decode(ubest(fs))); impact = :sqrt)
seeds(n; base = 0) = [UInt64(base + i) * 0x9E3779B97F4A7C15 for i in 1:n]

"CPU batch: n simulations (simulate + moments), threaded."
function cpu_batch(p, n; base = 0)
    M = zeros(length(MD), n)
    Threads.@threads for i in 1:n
        M[:, i] = sim_vec(p, base + i)
    end
    M
end
"GPU batch: simulate on device, moments on CPU threads."
function gpu_batch(p, n; base = 0)
    C, L, hit = simulate_batch_gpu(fill(gp_from(p), n), seeds(n; base))
    hit && error("cascade cap bound on the GPU (a bug, never data)")
    M = zeros(length(MD), n)
    Threads.@threads for i in 1:n
        c = Float64.(view(C, :, i)); l = Float64.(view(L, :, i))
        r = diff(log.(c)); lowr = l[2:end] ./ c[1:end-1] .- 1
        M[:, i] = fullvec(r, lowr)
    end
    M
end
function zcompare(io, label, A, B)
    n = size(A, 2)
    ma = vec(mean(A; dims = 2)); mb = vec(mean(B; dims = 2))
    sa = vec(std(A; dims = 2)); sb = vec(std(B; dims = 2))
    z = (mb .- ma) ./ sqrt.(sa .^ 2 ./ n .+ sb .^ 2 ./ size(B, 2))
    println(io, "## validation: $label (CPU n = $n, GPU n = $(size(B, 2)))")
    for (k, nm) in enumerate(NAMES)
        @printf(io, "  %-12s CPU %9.4f  GPU %9.4f  z %6.2f\n", nm, ma[k], mb[k], z[k])
    end
    ok = all(abs.(z) .< 3)
    @printf(io, "  max |z| = %.2f → %s\n", maximum(abs.(z)), ok ? "PASS" : "FAIL")
    ok
end

io = open(joinpath(RES, "b1b_timing.txt"), "w")
println(io, "# B1b timing gate — $(now()) — CPU threads $(Threads.nthreads()) — GPU: $(CUDA.name(CUDA.device())), $(CUDA.attribute(CUDA.device(), CUDA.DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT)) SMs")
println(io, "# rule (fixed before measuring): keep GPU iff ≥ 3× faster end-to-end at 10,000 sims AND all |z| < 3 on 1,000-sim moment means under both impact laws")
gpu_batch(PL, 64); gpu_batch(PS, 64); cpu_batch(PL, 32)          # warm-up / compilation
okL = zcompare(io, "linear impact", cpu_batch(PL, 1000; base = 10_000), gpu_batch(PL, 1000; base = 20_000))
okS = zcompare(io, "square-root impact", cpu_batch(PS, 1000; base = 30_000), gpu_batch(PS, 1000; base = 40_000))

println(io, "## timing (linear-impact best fit; end-to-end = simulate + moments)")
T = Dict{Tuple{Symbol,Int},Float64}()
for n in (1000, 10_000)
    T[(:cpu, n)] = @elapsed cpu_batch(PL, n; base = 100_000)
    smi = open(`nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader,nounits -lms 250`, "r")
    T[(:gpu, n)] = @elapsed gpu_batch(PL, n; base = 200_000)
    kill(smi); samples = filter(!isempty, readlines(smi))
    util = [parse(Int, strip(split(s, ",")[1])) for s in samples]; mem = [parse(Int, strip(split(s, ",")[2])) for s in samples]
    tk = @elapsed simulate_batch_gpu(fill(gp_from(PL), n), seeds(n; base = 300_000))
    @printf(io, "  n = %6d  CPU %8.2f s (%.4f s/sim)   GPU end-to-end %8.2f s (kernel+transfer %8.2f s)   speed-up %.2f×   GPU util during run: median %d %%, max %d %%, peak mem %d MiB (%d samples)\n",
            n, T[(:cpu, n)], T[(:cpu, n)] / n, T[(:gpu, n)], tk, T[(:cpu, n)] / T[(:gpu, n)],
            isempty(util) ? -1 : round(Int, median(util)), isempty(util) ? -1 : maximum(util), isempty(mem) ? -1 : maximum(mem), length(util))
end
sp = T[(:cpu, 10_000)] / T[(:gpu, 10_000)]
keep = sp >= 3 && okL && okS
@printf(io, "## decision: speed-up at 10,000 = %.2f× (rule ≥ 3×); validation linear %s, square-root %s → GPU path %s\n",
        sp, okL ? "PASS" : "FAIL", okS ? "PASS" : "FAIL", keep ? "KEPT" : "NOT KEPT")
close(io)
print(read(joinpath(RES, "b1b_timing.txt"), String))

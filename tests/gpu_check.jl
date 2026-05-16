# Dalila GPU verification — Julia stack
# Per CLAUDE.md §9: run after any environment change to confirm CUDA is operational.
# Exit 0 if CUDA.jl can dispatch to the GPU; exit 1 otherwise.

function section(title::String)
    bar = repeat("=", length(title))
    println("\n", title, "\n", bar)
end

function run_nvidia_smi()
    section("nvidia-smi (driver + hardware)")
    cmd = `nvidia-smi --query-gpu=name,driver_version,memory.total,memory.free,compute_cap --format=csv`
    try
        out = read(cmd, String)
        print(out)
        return true
    catch err
        println("FAIL  nvidia-smi unavailable: ", err)
        return false
    end
end

function check_cuda_jl()
    section("CUDA.jl")
    cuda_loaded = try
        Base.eval(Main, :(using CUDA))
        true
    catch err
        println("SKIP  CUDA.jl not installed in active env.")
        println("      To install: `import Pkg; Pkg.add(\"CUDA\")` then re-run.")
        println("      Underlying error: ", err)
        false
    end
    cuda_loaded || return false

    CUDA = Main.CUDA
    println("      CUDA.jl version: ", pkgversion(CUDA))
    if !CUDA.functional()
        println("FAIL  CUDA.functional() == false")
        return false
    end
    println("OK    CUDA functional")
    try
        CUDA.versioninfo()
    catch err
        println("      versioninfo failed: ", err)
    end

    # Smoke test: 1024x1024 matmul on device
    x = CUDA.rand(Float32, 1024, 1024)
    y = sum(x * transpose(x))
    println("      smoke test: 1024x1024 matmul on GPU → scalar ", y)
    return true
end

function main()
    println("Dalila GPU check — Julia stack")
    hw_ok = run_nvidia_smi()
    cuda_ok = check_cuda_jl()

    section("Summary")
    println("  nvidia-smi : ", hw_ok ? "OK" : "FAIL")
    println("  CUDA.jl    : ", cuda_ok ? "OK" : "not usable")

    if !hw_ok
        return 1
    end
    if !cuda_ok
        println("\nNote: GPU is healthy at the driver level but CUDA.jl is not usable in")
        println("this Julia environment yet. Install CUDA.jl in the active project env")
        println("(`activate <project>; add CUDA`) and re-run.")
        return 1
    end
    return 0
end

exit(main())

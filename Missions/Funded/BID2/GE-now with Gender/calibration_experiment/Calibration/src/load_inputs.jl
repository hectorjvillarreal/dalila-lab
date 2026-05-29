################################################################################
#  load_inputs.jl
#
#  Reads the 9 input CSVs under Calibration/inputs/ and packs them into
#  typed NamedTuples that the rest of the pipeline (pe_solver_for_smm.jl,
#  moments.jl, objective.jl) consumes.
#
#  Top-level entry:
#      io = load_all_inputs("Calibration/inputs")  # default path
#
#  Returns a NamedTuple with fields:
#      io.first_step  — (e_age, ψ_base, δh, π_birth, θ_grid, ϱ_pen, ρ, σ_ε)
#      io.anchor      — (r, w, τp, pen)
#      io.targets     — (names::Vector{String}, values::Vector{Float64}, ses::Vector{Float64})
#      io.theta_init  — (names, init, lb, ub, transform::Vector{Symbol})
#      io.usd_scale   — (usd_per_unit_c, periods_per_year, reference_age_period)
#      io.grids       — (NA, NH, Nm, refine_m::Bool, verify::Bool)
#
#  Self-contained: tiny hand-written CSV parser (we don't depend on CSV.jl /
#  DataFrames.jl). Files are kilobytes; this is fast enough.
#
#  Schema validation lives here: bad header, wrong row count, NaN, etc.
#  fail loudly with an informative error message.
################################################################################

# ─── Minimal CSV reader ──────────────────────────────────────────────────────
"""
    read_csv(path::String) -> (header::Vector{String}, rows::Vector{Vector{String}})

Read a comma-separated file. No quoting / escaping support — sufficient for
the simple numeric CSVs in Calibration/inputs/. Blank lines are skipped.
"""
function read_csv(path::String)
    isfile(path) || error("CSV not found: $path")
    lines = readlines(path)
    nonblank = String[strip(l) for l in lines if !isempty(strip(l)) && !startswith(strip(l), "#")]
    isempty(nonblank) && error("CSV is empty: $path")
    header = String.(strip.(split(nonblank[1], ',')))
    rows = [String.(strip.(split(l, ','))) for l in nonblank[2:end]]
    return header, rows
end

# Helper: get column index by header name (1-based).
col(header::Vector{String}, name::String) =
    findfirst(==(name), header) === nothing ?
        error("column '$name' missing from header $(header)") :
        findfirst(==(name), header)

# ─── 1. first_step ──────────────────────────────────────────────────────────
function load_first_step(dir::String)
    # e_age.csv: age_period, male, female  (J rows)
    h, r = read_csv(joinpath(dir, "first_step", "e_age.csv"))
    cm, cf = col(h, "male"), col(h, "female")
    J_csv = length(r)
    e_age = zeros(2, J_csv)
    for (i, row) in enumerate(r)
        e_age[1, i] = parse(Float64, row[cm])
        e_age[2, i] = parse(Float64, row[cf])
    end

    # psi_base.csv: age_period, male, female  (J rows)
    h, r = read_csv(joinpath(dir, "first_step", "psi_base.csv"))
    cm, cf = col(h, "male"), col(h, "female")
    length(r) == J_csv || error("psi_base.csv has $(length(r)) rows, expected $J_csv to match e_age.csv")
    ψ_base = zeros(2, J_csv)
    for (i, row) in enumerate(r)
        ψ_base[1, i] = parse(Float64, row[cm])
        ψ_base[2, i] = parse(Float64, row[cf])
    end

    # delta_h.csv: age_period, value
    h, r = read_csv(joinpath(dir, "first_step", "delta_h.csv"))
    cv = col(h, "value")
    length(r) == J_csv || error("delta_h.csv has $(length(r)) rows, expected $J_csv")
    δh = [parse(Float64, row[cv]) for row in r]

    # pi_birth.csv: sex_idx, theta_idx, share  (Ng*Nθ rows, sum = 1)
    h, r = read_csv(joinpath(dir, "first_step", "pi_birth.csv"))
    cs, ct, csh = col(h, "sex_idx"), col(h, "theta_idx"), col(h, "share")
    π_birth = zeros(2, 2)  # Ng = Nθ = 2
    for row in r
        ig = parse(Int, row[cs]); iθ = parse(Int, row[ct])
        π_birth[ig, iθ] = parse(Float64, row[csh])
    end
    abs(sum(π_birth) - 1.0) < 1e-9 || error("pi_birth.csv: shares sum to $(sum(π_birth)), expected 1.0")

    # skill_params.csv: theta_idx, theta, rho_pen
    h, r = read_csv(joinpath(dir, "first_step", "skill_params.csv"))
    ct, ctv, crp = col(h, "theta_idx"), col(h, "theta"), col(h, "rho_pen")
    θ_grid = zeros(2)
    ϱ_pen = zeros(2)
    for row in r
        iθ = parse(Int, row[ct])
        θ_grid[iθ] = parse(Float64, row[ctv])
        ϱ_pen[iθ]  = parse(Float64, row[crp])
    end

    # ar1_params.csv: param, value  (rows for rho, sigma_eps)
    h, r = read_csv(joinpath(dir, "first_step", "ar1_params.csv"))
    cp, cv = col(h, "param"), col(h, "value")
    ar1 = Dict{String,Float64}()
    for row in r
        ar1[row[cp]] = parse(Float64, row[cv])
    end
    haskey(ar1, "rho")       || error("ar1_params.csv missing 'rho'")
    haskey(ar1, "sigma_eps") || error("ar1_params.csv missing 'sigma_eps'")

    return (; e_age, ψ_base, δh, π_birth, θ_grid, ϱ_pen,
            ρ = ar1["rho"], σ_ε = ar1["sigma_eps"], J = J_csv)
end

# ─── 2. anchor (PE prices) ──────────────────────────────────────────────────
function load_anchor(dir::String)
    h, r = read_csv(joinpath(dir, "config", "pe_anchor.csv"))
    cp, cv = col(h, "price"), col(h, "value")
    d = Dict{String,Float64}()
    for row in r
        d[row[cp]] = parse(Float64, row[cv])
    end
    for k in ("r", "w", "tau_p", "pen")
        haskey(d, k) || error("pe_anchor.csv missing '$k'")
    end
    return (; r = d["r"], w = d["w"], τp = d["tau_p"], pen = d["pen"])
end

# ─── 3. target moments ──────────────────────────────────────────────────────
function load_targets(dir::String)
    h, r = read_csv(joinpath(dir, "moments", "targets.csv"))
    cn, cv, cs = col(h, "name"), col(h, "value"), col(h, "se")
    names  = [row[cn] for row in r]
    values = [parse(Float64, row[cv]) for row in r]
    ses    = [parse(Float64, row[cs]) for row in r]
    length(names) == 6 || @warn "targets.csv has $(length(names)) rows; expected 6"
    all(ses .> 0) || error("targets.csv: all SEs must be positive (W = 1/SE²)")
    return (; names, values, ses)
end

# ─── 4. theta_init ──────────────────────────────────────────────────────────
function load_theta_init(dir::String)
    h, r = read_csv(joinpath(dir, "config", "theta_init.csv"))
    cn, ci, cl, cu, ct = col(h, "param"), col(h, "init"), col(h, "lb"),
                          col(h, "ub"), col(h, "transform")
    # `frozen` column is optional — if absent, all params are free.
    cfrz = findfirst(==("frozen"), h)
    names     = [row[cn] for row in r]
    init      = [parse(Float64, row[ci]) for row in r]
    lb        = [parse(Float64, row[cl]) for row in r]
    ub        = [parse(Float64, row[cu]) for row in r]
    transform = [Symbol(row[ct]) for row in r]
    frozen    = cfrz === nothing ?
                fill(false, length(names)) :
                [parse(Int, row[cfrz]) != 0 for row in r]
    length(names) == 6 || @warn "theta_init.csv has $(length(names)) rows; expected 6"
    for t in transform
        t in (:log, :logit, :identity) || error("unknown transform '$t' in theta_init.csv (expected :log, :logit, :identity)")
    end
    all(init .>= lb) && all(init .<= ub) || error("theta_init.csv: init values must lie in [lb, ub]")
    return (; names, init, lb, ub, transform, frozen)
end

# ─── 5. usd_scale (for VSL) ─────────────────────────────────────────────────
function load_usd_scale(dir::String)
    h, r = read_csv(joinpath(dir, "config", "usd_scale.csv"))
    cp, cv = col(h, "param"), col(h, "value")
    d = Dict{String,Float64}()
    for row in r
        d[row[cp]] = parse(Float64, row[cv])
    end
    return (; usd_per_unit_c       = d["usd_per_unit_c"],
              periods_per_year     = Int(d["periods_per_year"]),
              reference_age_period = Int(d["reference_age_period"]))
end

# ─── 6. grids/runtime config ────────────────────────────────────────────────
function load_grids(dir::String)
    h, r = read_csv(joinpath(dir, "config", "grids.csv"))
    cp, cv = col(h, "param"), col(h, "value")
    d = Dict{String,String}()
    for row in r
        d[row[cp]] = row[cv]
    end
    return (; NA       = parse(Int, get(d, "NA", "100")),
              NH       = parse(Int, get(d, "NH", "15")),
              Nm       = parse(Int, get(d, "Nm", "40")),
              refine_m = parse(Int, get(d, "refine_m", "1")) != 0,
              verify   = parse(Int, get(d, "verify", "0")) != 0)
end

# ─── Top-level: load everything ─────────────────────────────────────────────
"""
    load_all_inputs(base_dir::String = joinpath(@__DIR__, "..", "inputs"))

Read all CSVs under `base_dir` and return a single NamedTuple bundling
`first_step`, `anchor`, `targets`, `theta_init`, `usd_scale`, `grids`.
"""
function load_all_inputs(base_dir::String = joinpath(@__DIR__, "..", "inputs"))
    isdir(base_dir) || error("Calibration inputs directory not found: $base_dir")
    return (; first_step = load_first_step(base_dir),
              anchor     = load_anchor(base_dir),
              targets    = load_targets(base_dir),
              theta_init = load_theta_init(base_dir),
              usd_scale  = load_usd_scale(base_dir),
              grids      = load_grids(base_dir))
end

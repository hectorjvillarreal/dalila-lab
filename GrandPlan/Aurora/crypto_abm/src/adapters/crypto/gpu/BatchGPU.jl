"""
    BatchGPU

B1b: batched simulation of the B1 bitcoin model on the GPU (design note B0 v1.2, §8).
One thread block = one simulation; one thread = at most one agent of each class (so
agent state lives in registers); price, impact and σ̂ live in shared memory and are
updated by thread 1 after block-wide reductions of order flow. The cascade loop runs
in lockstep across the block. A per-thread xorshift64* generator (seeded by splitmix64
from the simulation seed and thread id) supplies uniforms and Box–Muller normals.

Scope: only the state that moves prices is simulated (agent holdings, leveraged
equity, price, σ̂). Cash of conviction and momentum agents, the liquidity provider's
books and the loss fund do not feed back into prices in B1 and are not tracked here;
conservation is tested on the CPU engine. Agent state is Float32; the log price, the
transient part and σ̂ are Float64.

Not loaded by `CryptoABM` by default (CUDA is heavy). Use:
    using CUDA; include("src/adapters/crypto/gpu/BatchGPU.jl"); using .BatchGPU
"""
module BatchGPU

using CUDA

export GP, gp_from, simulate_batch_gpu

const NT = 256          # threads per block
const WMAX = 64         # max σ̂ window (K) and momentum ring length (h_max < 64)

"Per-simulation parameters (isbits)."
struct GP
    w_c::Float32; w_m::Float32; w_l::Float32
    Nc::Int32; Nm::Int32; Nl::Int32
    D_median::Float32; s_D::Float32; sell_frac::Float32; reentry::Float32
    β::Float32; h_min::Int32; h_max::Int32; θ::Float32
    L_median::Float32; s_L::Float32; m0::Float32; m1::Float32
    close_hazard::Float32; reopen_delay::Int32; β_l::Float32
    funding_c::Float32; funding_max::Float32
    σ_ε::Float32; λ0::Float64; κ::Float64; λmax::Float64; φ::Float64; ρ::Float64; σbar::Float64
    sqrt_impact::Bool; q0::Float64
    K::Int32
end

"Convert a CPU `Params` (any struct with the CryptoAdapter.Params field names) to `GP`."
gp_from(p) = GP(p.w_c, p.w_m, p.w_l, p.N_c, p.N_m, p.N_l, p.D_median, p.s_D, p.sell_frac, p.reentry,
                p.β, p.h_min, p.h_max, p.θ, p.L_median, p.s_L, p.m0, p.m1, p.close_hazard, p.reopen_delay,
                p.β_l, p.funding_c, p.funding_max, p.σ_ε, p.λ0, p.κ, p.λmax_mult * p.λ0, p.φ, p.ρ, p.σbar,
                p.impact === :sqrt, p.q0, p.K)

# ---------------------------------------------------------------- RNG
@inline function splitmix(x::UInt64)
    x += 0x9E3779B97F4A7C15
    z = x
    z = (z ⊻ (z >> 30)) * 0xBF58476D1CE4E5B9
    z = (z ⊻ (z >> 27)) * 0x94D049BB133111EB
    z ⊻ (z >> 31)
end
@inline function xnext(s::UInt64)
    s ⊻= s >> 12; s ⊻= s << 25; s ⊻= s >> 27
    s, s * 0x2545F4914F6CDD1D
end
@inline function urand(s::UInt64)                       # (0, 1]
    s, r = xnext(s)
    s, (Float32(r >> 40) + 1f0) * 5.9604645f-8
end
@inline function nrand(s::UInt64)                       # standard normal (Box–Muller)
    s, a = urand(s); s, b = urand(s)
    s, sqrt(-2f0 * log(a)) * cos(6.2831855f0 * b)
end
@inline function irand(s::UInt64, lo::Int32, hi::Int32) # integer in lo:hi
    s, u = urand(s)
    s, min(hi, lo + unsafe_trunc(Int32, u * Float32(hi - lo + 1) - 1f-6))
end

# ---------------------------------------------------------------- block reduction
@inline function bsum(red, v::Float32, tid)
    red[tid] = v
    sync_threads()
    st = NT ÷ 2
    while st > 0
        tid <= st && (red[tid] += red[tid+st])
        sync_threads()
        st ÷= 2
    end
    r = red[1]
    sync_threads()
    r
end

@inline gfun(sq::Bool, X::Float64, q0::Float64) = sq ? sign(X) * sqrt(abs(X) * q0) : X

# shared scalar slots
const F_ = 1; const U_ = 2; const P_ = 3; const SIG_ = 4; const XC_ = 5; const LP0_ = 6; const DLO_ = 7; const WI_ = 8

@inline function clear_shared!(sh, g::GP, X::Float32)
    λ = min(g.λ0 * exp(g.κ * (sh[SIG_] / g.σbar - 1.0)), g.λmax)
    X0 = sh[XC_]; X1 = X0 + Float64(X)
    d = λ * (gfun(g.sqrt_impact, X1, g.q0) - gfun(g.sqrt_impact, X0, g.q0))
    sh[XC_] = X1
    sh[F_] += (1.0 - g.φ) * d
    sh[U_] += g.φ * d
    p = exp(sh[F_] + sh[U_])
    sh[P_] = p
    sh[DLO_] = min(sh[DLO_], p)
    nothing
end

function kernel!(closes, lows, P, seeds, T::Int32, burnin::Int32, capflag)
    sim = blockIdx().x
    tid = threadIdx().x
    g = P[sim]
    K = g.K
    red = CuStaticSharedArray(Float32, NT)
    sh = CuStaticSharedArray(Float64, 8)
    win = CuStaticSharedArray(Float64, WMAX)
    lc = CuStaticSharedArray(Float32, WMAX)

    s = splitmix(seeds[sim] ⊻ (UInt64(tid) * 0xD1B54A32D192ED03))
    # ---------------- agent state in registers
    isC = tid <= g.Nc; isM = tid <= g.Nm; isL = tid <= g.Nl
    c_hold = isC ? g.w_c / Float32(g.Nc) : 0f0
    c_target = c_hold
    s, z = nrand(s)
    c_D = clamp(exp(log(g.D_median) + g.s_D * z), 0.02f0, 0.95f0)
    c_peak = 1f0; c_flag = false; c_pend = 0f0
    m_q = 0f0; m_cap = isM ? g.w_m / Float32(g.Nm) : 0f0
    s, m_h = irand(s, g.h_min, g.h_max)
    l_q = 0f0; l_cash = 0f0
    s, z = nrand(s)
    l_L = clamp(exp(log(g.L_median) + g.s_L * z), 1.1f0, 100f0)
    s, l_h = irand(s, g.h_min, g.h_max)
    s, l_cd = irand(s, Int32(0), g.reopen_delay)
    l_open = false; l_closing = false; l_pend = 0f0
    l_size = isL ? g.w_l / Float32(g.Nl) : 0f0
    σday = Float32(g.σbar * sqrt(Float64(K)))
    noise_sd = g.σ_ε / sqrt(Float32(K))
    cap = g.Nc + g.Nl + Int32(1)
    fund_every = max(Int32(1), K ÷ Int32(3))
    if tid == 1
        sh[F_] = 0.0; sh[U_] = 0.0; sh[P_] = 1.0; sh[SIG_] = g.σbar; sh[XC_] = 0.0; sh[DLO_] = Inf; sh[WI_] = 1.0
        for k in 1:WMAX
            win[k] = g.σbar; lc[k] = 0f0
        end
    end
    sync_threads()
    step = Int32(0)
    for day in Int32(1):T
        tid == 1 && (sh[DLO_] = Inf)
        sync_threads()
        for sub in Int32(1):K
            step += Int32(1)
            p = Float32(sh[P_]); logp = log(p)
            # -------- ordinary orders
            x = 0f0
            c_pend = 0f0
            if isC && c_flag && (1f0 - p / c_peak) < c_D / 2f0
                c_pend = g.reentry * (c_target - c_hold); x += c_pend
            end
            m_pend = 0f0
            if isM
                tr = day > m_h ? (logp - lc[mod1(day - m_h, WMAX)]) / (σday * sqrt(Float32(m_h))) : 0f0
                m_pend = g.θ * (m_cap * tanh(g.β * tr) - m_q); x += m_pend
            end
            l_pend = 0f0
            if isL
                if l_open
                    s, u = urand(s)
                    if u < g.close_hazard
                        l_pend = -l_q; l_closing = true
                    end
                elseif l_cd <= 0
                    tr = day > l_h ? (logp - lc[mod1(day - l_h, WMAX)]) / (σday * sqrt(Float32(l_h))) : 0f0
                    s, z = nrand(s)
                    dd = (g.β_l * tr + z) >= 0f0 ? 1f0 : -1f0
                    l_cash += l_size * p / l_L
                    l_pend = dd * l_size; l_open = true
                end
                x += l_pend
            end
            if tid == 1
                s, z = nrand(s); x += noise_sd * z
            end
            X = bsum(red, x, tid)
            if tid == 1
                sh[XC_] = 0.0; sh[LP0_] = sh[F_] + sh[U_]
                clear_shared!(sh, g, X)
            end
            sync_threads()
            p = Float32(sh[P_])
            c_hold += c_pend; m_q += m_pend
            if isL
                l_q += l_pend; l_cash -= l_pend * p
                if l_closing && abs(l_q) < 1f-12
                    l_q = 0f0; l_cash = 0f0; l_open = false; l_closing = false; l_cd = g.reopen_delay
                end
            end
            # -------- cascade loop (σ̂ frozen: sh[SIG_] unchanged here)
            mreq = Float32(g.m0 + g.m1 * Float32(sh[SIG_]))
            rounds = Int32(0)
            while true
                fx = 0f0
                c_pend = 0f0
                if isC && !c_flag && (1f0 - p / c_peak) >= c_D
                    c_pend = -g.sell_frac * c_hold; c_flag = true; fx += c_pend
                end
                l_pend = 0f0
                if isL && l_open && !l_closing && (l_cash + l_q * p) < mreq * abs(l_q) * p
                    l_pend = -l_q; l_closing = true; fx += l_pend
                end
                F = bsum(red, fx, tid)
                F == 0f0 && break
                rounds += Int32(1)
                if rounds > cap
                    tid == 1 && (capflag[1] = Int32(1))
                    break
                end
                tid == 1 && clear_shared!(sh, g, F)
                sync_threads()
                p = Float32(sh[P_])
                c_hold += c_pend
                if isL
                    l_q += l_pend; l_cash -= l_pend * p
                    if l_closing && abs(l_q) < 1f-12
                        l_q = 0f0; l_cash = 0f0; l_open = false; l_closing = false; l_cd = g.reopen_delay
                    end
                end
            end
            # -------- end of sub-step
            if isC
                if c_flag
                    if c_hold >= 0.999f0 * c_target
                        c_flag = false; c_peak = p
                    end
                else
                    c_peak = max(c_peak, p)
                end
            end
            isL && !l_open && (l_cd -= Int32(1))
            if step % fund_every == Int32(0)
                lg = bsum(red, (isL && l_q > 0f0) ? l_q : 0f0, tid)
                sm = bsum(red, (isL && l_q < 0f0) ? -l_q : 0f0, tid)
                tot = lg + sm
                if tot > 0f0 && isL && l_q != 0f0
                    rate = clamp(g.funding_c * (lg - sm) / tot, -g.funding_max, g.funding_max)
                    l_cash -= rate * l_q * p
                end
            end
            if tid == 1
                sh[U_] *= (1.0 - g.ρ)
                r = sh[F_] + sh[U_] - sh[LP0_]
                wi = unsafe_trunc(Int32, sh[WI_])
                win[wi] = r
                sh[WI_] = Float64(wi == K ? Int32(1) : wi + Int32(1))
                acc = 0.0
                for k in 1:K
                    acc += win[k] * win[k]
                end
                sh[SIG_] = sqrt(acc / K)
                pp = exp(sh[F_] + sh[U_])
                sh[P_] = pp
                sh[DLO_] = min(sh[DLO_], pp)
            end
            sync_threads()
        end
        if tid == 1
            lc[mod1(day, WMAX)] = Float32(sh[F_] + sh[U_])
            if day > burnin
                closes[day - burnin, sim] = Float32(sh[P_])
                lows[day - burnin, sim] = Float32(sh[DLO_])
            end
        end
        sync_threads()
    end
    return nothing
end

"""
    simulate_batch_gpu(params::Vector{GP}, seeds::Vector{UInt64}; days = 1040, burnin = 120)
        -> (closes::Matrix{Float32}, lows::Matrix{Float32}, cap_hit::Bool)

Each column is one simulation (daily close and daily low after burn-in).
"""
function simulate_batch_gpu(params::Vector{GP}, seeds::Vector{UInt64}; days::Int = 1040, burnin::Int = 120)
    n = length(params)
    @assert length(seeds) == n
    @assert all(p -> p.Nc <= NT && p.Nm <= NT && p.Nl <= NT && p.K <= WMAX && p.h_max < WMAX, params)
    dP = CuArray(params); dS = CuArray(seeds)
    dC = CUDA.zeros(Float32, days, n); dL = CUDA.zeros(Float32, days, n)
    flag = CUDA.zeros(Int32, 1)
    @cuda threads = NT blocks = n kernel!(dC, dL, dP, dS, Int32(days + burnin), Int32(burnin), flag)
    CUDA.synchronize()
    Array(dC), Array(dL), Array(flag)[1] != 0
end

end # module

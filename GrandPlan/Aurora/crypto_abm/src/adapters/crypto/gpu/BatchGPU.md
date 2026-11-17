# BatchGPU — batched bitcoin simulations on the GPU (B1b)

Companion to `BatchGPU.jl`. It implements design note B0 v1.2, §8 (B1b timing gate).

## Design
- **One thread block per simulation, 256 threads per block.** Thread *i* owns at most one conviction holder, one momentum trader and one leveraged trader, so all agent state stays in registers for the whole path. This requires N_c, N_m, N_l ≤ 256.
- **Shared memory holds:**
  - the log price (permanent f and transient u);
  - the cumulative sub-step flow X;
  - σ̂ and its K-length window;
  - a 64-day ring of log closes for the momentum signals (h ≤ 63).
- **Thread 1 clears** each batch after a block-wide reduction of order flow. The rule is the CPU engine's: λ = min(λ₀·exp(κ(σ̂/σ̄ − 1)), λ_max), applied to cumulative flow, under linear or square-root impact.
- **The cascade loop** runs in lockstep: forced orders, reduction, a break when the total is zero, then clearing and settlement. σ̂ is frozen inside it. A binding N + 1 cap sets a flag, and the caller treats that as an error.
- **Between sub-steps:** funding every K/3 sub-steps (two reductions), then the transient decay, then the σ̂ update.
- **Random numbers:** a per-thread xorshift64* generator, seeded by splitmix64 from the simulation seed and the thread id. Normals come from Box–Muller. Draws differ from the CPU engine's Xoshiro streams, so GPU and CPU are compared *in distribution*, not path by path.
- **Precision:** agent state is Float32. Log price, transient part, σ̂ and λ are Float64.

## Scope
Only state that moves prices is simulated. Conviction and momentum cash, the liquidity provider's books and the loss fund do not feed back into prices in B1, so they are left out. Conservation is tested on the CPU engine (`test/runtests.jl` §7, §7b).

## Use
```julia
using CUDA
include("src/adapters/crypto/gpu/BatchGPU.jl"); using .BatchGPU
C, L, cap_hit = simulate_batch_gpu(fill(gp_from(params), n), seeds; days = 1040, burnin = 120)
```
`C` and `L` are days × n matrices of daily closes and lows. The gate experiment is `experiments/b1b_timing.jl`.

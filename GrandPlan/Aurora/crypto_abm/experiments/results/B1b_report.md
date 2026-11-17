# B1b report — batched CPU/GPU timing gate (2026-11-17)

*Phase B1b of design note B0 v1.2 (§8, criterion 8). Branch `aurora-crypto-abm`. Drafted by Claude Code in Nina's role. Results: `b1b_timing.txt`, `b1b_timing_20261117_1416.log`, `gpu_check_crypto_abm_env.txt`.*

## Rule (fixed before measuring)

Keep the GPU path only if:
- at 10,000 simulations it is **≥ 3× faster end-to-end** (simulate + moments) than the 16-thread CPU batch; **and**
- its moments match the CPU's within Monte Carlo error: **all |z| < 3** on 1,000-simulation means, under **both** impact laws.

## Environment

- CUDA.jl **6.5.1** in the model's own `Project.toml`. The default environment has 6.1; the project resolved 6.5.1.
- `tests/gpu_check.jl` was run in this environment: nvidia-smi OK, CUDA.jl OK, sm_120 dispatch verified (`gpu_check_crypto_abm_env.txt`).
- GPU: RTX PRO 2000 Blackwell Laptop, 26 SMs, 8 GB.

## Implementation

`src/adapters/crypto/gpu/BatchGPU.jl` (see its `.md`):
- one thread block per simulation, one agent per thread (state in registers);
- price, impact and σ̂ in shared memory;
- block-wide reductions per batch;
- the cascade loop in lockstep;
- per-thread xorshift64* random numbers;
- Float32 agent state, Float64 price.

It simulates only state that moves prices. Conservation remains tested on the CPU engine.

## Validation (1,000 CPU vs 1,000 GPU simulations, independent seeds)

| Moment | Linear: CPU / GPU / z | Square-root: CPU / GPU / z |
|---|---|---|
| s.d. | 0.0247 / 0.0248 / 0.89 | 0.0255 / 0.0254 / −0.67 |
| ACF r₁ | −0.063 / −0.064 / −0.58 | −0.061 / −0.058 / 0.94 |
| ACF \|r\|₁ | 0.088 / 0.087 / −0.44 | 0.223 / 0.218 / −1.71 |
| ACF \|r\|₅ | −0.022 / −0.021 / 0.40 | −0.025 / −0.024 / 0.36 |
| ACF \|r\|₂₀ | −0.001 / −0.001 / 0.19 | 0.018 / 0.017 / −0.47 |
| Hill | 3.43 / 3.44 / 0.56 | 3.63 / 3.60 / −0.82 |
| 3σ share | 2.04 % / 2.07 % / 1.44 | 1.37 % / 1.36 % / −0.67 |
| Skewness | −0.111 / −0.118 / −0.50 | 0.204 / 0.258 / 1.46 |
| 10 % days | 0.46 % / 0.48 % / 1.11 | 0.43 % / 0.40 % / −0.81 |
| Intraday gap (pts) | −3.45 / −3.57 / **−2.74** | −1.76 / −1.73 / 0.91 |
| **max \|z\|** | **2.74 → PASS** | **1.71 → PASS** |

Across 20 tests, a maximum |z| of 2.74 is about what chance alone produces. The linear intraday gap is the closest call: the GPU's is 0.12 points deeper. It is recorded as the item to watch if the GPU path drives calibration.

*Note:* these 1,000-path means differ from the B1a fit's 10-path means (for example, ACF\|r\|₁ 0.088 here against 0.108 in the fit). The fit's figures are averages over 10 common-random-number paths. These are averages over 1,000 independent paths, so they are more precise.

## Timing (linear-impact best fit)

| n | CPU, 16 threads | GPU end-to-end | GPU kernel + transfer | Speed-up | GPU utilisation | Peak GPU memory |
|---|---|---|---|---|---|---|
| 1,000 | 13.98 s (14.0 ms/sim) | 4.77 s | 4.75 s | 2.93× | median 100 % | 165 MiB |
| 10,000 | 145.45 s (14.5 ms/sim) | 46.61 s | 46.28 s | **3.12×** | median 100 % | 229 MiB |

`nvidia-smi` was sampled every 250 ms during each GPU run (187 samples at n = 10,000). The GPU was fully busy, and the speed-up is not a CPU fallback.

## Decision

**GPU path KEPT** under the rule: 3.12× at 10,000 simulations, and validation passes under both laws.

The margin is **thin**: 3.12× against a bar of 3.0. The CPU batch scales well, at 14.5 ms per simulation on 16 threads against 231 ms on one thread, about 16×. The kernel is latency-bound: it runs about 30 block synchronisations per sub-step, with tree reductions through shared memory. Possible speed-ups are warp-shuffle reductions, fewer synchronisations per cascade round, and several simulations per block. These are recorded, not attempted; any of them must re-pass this gate.

## What this means in use

- **A 10,000-simulation batch takes about 47 s on the GPU, against about 145 s on the CPU.** That is roughly one SMM objective sweep of 1,000 draws × 10 replications.
- **Calibration in B3 can use the GPU path**, with the CPU engine as the reference. The CPU engine stays the source of truth for tests, conservation and single runs.
- **GPU results are equal in distribution, not path by path,** because the random streams differ.

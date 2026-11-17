# crypto_abm — Aurora mechanism laboratory (phase B1)

Design note: `../Aurora_Nina_CRYPTO_ABM_DesignNote_B0_202611.md` (v1.2). Build instruction: `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_abm_b1.md` (2_of_2).
Branch `aurora-crypto-abm`, checkout `~/Dalila-abm`. It merges into main when note §11 passes.

## Firewall (note §0)
This model is a laboratory for mechanisms, not a forecaster. Nothing here reads or writes the crypto regime board. No model number goes onto the board's dashboard. A model result reaches the board only as a ruling question to Héctor, stated in board-observable units with the run id. A test enforces the code side.

## Compute
- **CPU engine** (`src/`): the source of truth for tests, conservation and single runs. One 1,040-day path (+120 burn-in) takes a median 0.23 s on one thread, or 14.5 ms per simulation in a 16-thread batch.
- **GPU batch path** (`src/adapters/crypto/gpu/BatchGPU.jl`, B1b, 2026-11-17): **kept** by the pre-stated gate (≥ 3× at 10,000 sims and moments within Monte Carlo error under both impact laws).
  - It measured **3.12×** (46.6 s against 145.5 s), with max |z| 2.74 / 1.71 (`experiments/results/B1b_report.md`).
  - The margin is thin.
  - GPU and CPU moment means agree within Monte Carlo error (all |z| < 3); spreads were not tested, and paths differ because the random streams differ.
  - Each n was timed once, so a repeat could fall below 3×.
- CUDA.jl 6.5.1 is in `Project.toml`. `tests/gpu_check.jl` passed in this environment (`experiments/results/gpu_check_crypto_abm_env.txt`).

## Layout
- `src/core/`: asset-agnostic engine (`ABMCore`) and statistics (`Moments`).
- `src/adapters/crypto/`: the bitcoin instance.
- `targets/`: the snapshot, its checksums, and the §1 recomputation.
- `experiments/`: runs, each printing conditional mechanism reads only.
- `test/runtests.jl`: the code-checkable §11 criteria.

## Run
```
cd GrandPlan/Aurora/crypto_abm
julia --project=. test/runtests.jl
julia --project=. experiments/first_run.jl
julia -t 16 --project=. experiments/b1b_timing.jl <fit_linear_*.txt> <fit_sqrt_*.txt>   # B1b gate (GPU)
```

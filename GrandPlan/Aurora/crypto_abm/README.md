# crypto_abm — Aurora mechanism laboratory (phase B1)

Design note: `../Aurora_Nina_CRYPTO_ABM_DesignNote_B0_202611.md` (v1.2). Build instruction: `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_abm_b1.md` (2_of_2).
Branch `aurora-crypto-abm`, checkout `~/Dalila-abm`. It merges into main when note §11 passes.

## Firewall (note §0)
This model is a laboratory for mechanisms, not a forecaster. Nothing here reads or writes the crypto regime board. No model number goes onto the board's dashboard. A model result reaches the board only as a ruling question to Héctor, stated in board-observable units with the run id. A test enforces the code side.

## Compute
**B1a is CPU only**, a stated choice (note §8). One 1,040-day path (+120 burn-in) takes a median 0.23 s on one thread (`experiments/results/null_and_timing.txt`). CUDA.jl enters only in B1b (the timing gate), and `tests/gpu_check.jl` runs then.

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
```

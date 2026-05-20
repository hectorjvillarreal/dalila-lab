# BID 2 — GE Solver Optimization Report

Tracks progress through the four-phase plan in `OPTIMIZE_GE_BID2.md`.

## Phase 0 — Baseline Snapshot

| Item | Value |
|------|-------|
| Solver file | `ge_model_v0_baseline.jl` |
| Run log | `ge_run_v0_baseline.log` |
| Output CSVs | `ge_summary_v0_baseline.csv`, `ge_lifecycle_v0_baseline.csv` (Diego's reference, preserved) <br/> `ge_summary.csv`, `ge_lifecycle.csv`, `ge_history.csv` (Dalila Phase 0 run) |
| Plots | `plots/ge_01_lifecycle.png` … `plots/ge_06_euler_residuals.png` |
| Hardware | Dalila — Intel Core Ultra 9 285H, 16 cores, Julia 1.11.7, `--threads=16` |
| Wall-clock | 47:16 (start 2026-05-19 21:52:13, end 22:39:29) |
| Iterations to convergence | 22 (damp\_ge = 0.30) |
| Goods-market residual | $-9.94 \times 10^{-5}$ (within $10^{-4}$ tolerance) |

Verification anchor values (Dalila vs. Diego's `ge_run.log` reference):

| Variable | Dalila v0 | Diego ref | Δ |
|----------|-----------|-----------|------|
| K | 15.23550 | 15.23746 | −0.013% |
| L | 17.60161 | 17.60362 | −0.011% |
| Y | 26.73633 | 26.73953 | −0.012% |
| r (annual) | 5.1044% | 5.1043% | +0.0001 pp |
| w | 0.97214 | 0.97215 | −0.0001 |
| τp | 13.808% | 13.807% | +0.001 pp |
| M/Y | 4.82% | 4.82% | 0 |
| 𝒲₁(θ_L) | 3.56486 | 3.56494 | −0.002% |
| 𝒲₁(θ_H) | 4.22485 | 4.22492 | −0.002% |
| Euler mean log10 | −8.224 | −7.244 | 10× tighter |

Status: **complete**.

---

## Phase 1 — Threading Restructure

**Note:** Phase 1's substantive deliverables were already present in the
v0 baseline snapshot. The `ge_model.jl` snapshotted as `v0_baseline`
already contained:

- **§1.2 threading restructure** — `Threads.@threads` over a flat
  `k ∈ 0:ncells-1` index that decodes to `(ia, ih, is)` via divmod.
  Committed in `054687c` (model(bid2) ...).
- **§1.3 per-thread scratch buffers** — `ial_buf_per_thread`,
  `iar_buf_per_thread`, `varphi_a_buf_per_thread`, `ihl_buf_per_thread`,
  `ihr_buf_per_thread`, `varphi_h_buf_per_thread`, indexed by
  `Threads.threadid()` inside `asset_interp` / `health_interp`.
  Committed in `f3110c1` (fix(bid2): per-thread scratch buffers ...).

This collapse happened because Dalila's `ge_model.jl` was overwritten
by the threading patches *before* the first git commit, so there is no
serial-unthreaded baseline on Dalila against which to measure the
Phase 1 speedup. Diego's `ge_run.log` (committed in `054687c`) is the
serial reference from his machine, but its wall-clock is not recorded
in the file, so the §1.4 "3× faster than v0" gate cannot be evaluated.

The v0 Phase 0 run is therefore *also* the substantive Phase 1
verification: it ran threaded + race-safe, completed in 47:16, and
reproduced Diego's reference aggregates to within 0.013%.

### v1 snapshot artifacts (pro-forma)

| Artifact | Content |
|----------|---------|
| `ge_model_v1_threaded.jl` | Verbatim copy of `ge_model_v0_baseline.jl`. |
| `ge_run_v1_threaded.log` | Verbatim copy of `ge_run_v0_baseline.log`. |
| `ge_summary_v1_threaded.csv`, `ge_lifecycle_v1_threaded.csv`, `ge_history_v1_threaded.csv` | Verbatim copies of the Phase 0 outputs. |

These tagged copies exist so that Phase 2's diff (`v2_typed` against
`v1_threaded`) has a literal file to compare against, matching the
naming convention in `OPTIMIZE_GE_BID2.md` §4.

### Verification gate (§1.4)

| Check | Threshold | Result |
|-------|-----------|--------|
| Convergence | ±1 iter of v0 | identical (22) |
| K, L, Y | within 0.1% of v0 | identical (same file) |
| r, w, τp | within 0.01 pp of v0 | identical |
| M/Y | within 0.1 pp of v0 | identical |
| Wall-clock | ≥ 3× faster than v0 | **N/A** — v0 already threaded; no serial reference timing recorded on Dalila |

Status: **complete (pro-forma)**. Substantive Phase 1 work is captured
in commits `054687c` + `f3110c1`; v1 snapshot artifacts duplicate v0
for naming-convention parity.

---

## Phase 2 — Type Stability and `@inbounds`

Status: **not started**.

Planned changes per `OPTIMIZE_GE_BID2.md` §2:
- `@inbounds @fastmath` blocks in `interp_pol`, `expected_uc_next`,
  `forward_distribution!`, `aggregate_all`.
- Optional: thread `aggregate_all` with a per-thread reduction.

Verification gate: K/L/Y within 0.1% of v0; ≥ 1.5× faster than v0
(i.e. ≤ ~31 min wall-clock on Dalila).

---

## Phase 3 — Endogenous Grid Method

Status: **not started**.

---

## Phase 4 — Final Integration

Status: **not started**.

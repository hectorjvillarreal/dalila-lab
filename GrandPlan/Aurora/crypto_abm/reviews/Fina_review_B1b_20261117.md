# Fina — Review of B1b (evidence and coherence)

*Fina · Aurora · 2026-11-17 · Read only. I checked `~/Dalila-abm` at 6d19589 and main at 6329c1a. Tests pass, 436 of 436; the commit message says 430. I did not rerun the gate.*
*Filed verbatim by Claude Code, 2026-11-17. The criterion-4 restatement and the minor fixes were applied in the commit that filed this memo. The merge waits for Héctor's ruling on criterion 4, as this memo asks.*

## Verdict

**Do not merge (one blocking issue, listed below).** B1b itself is sound. The rule in the code is the stated rule, every table matches its results file, and the validation is correct.

The blocker is what B1b's own 1,000-path data shows about B1a criterion 4. Fixing it needs a restatement and a ruling from Héctor, not a rerun. After that, the minor fixes below need no re-check from me.

## Blocking issue

**Criterion 4 is contradicted by the B1b data.**
- B1a marks criterion 4 "Met under square-root impact (10 of 10)". That rests on 10 common-random-number paths that the optimiser selected.
- `run_b1b.sh` takes the newest fit files, `fit_linear_20261117_1239` and `fit_sqrt_20261117_1318`, so B1b used the same parameter vectors.
- At the square-root vector over 1,000 independent paths, ACF|r| at lag 5 is **−0.025 on the CPU and −0.024 on the GPU**. That is outside the band floor of 0.0014; the 10-path figure was 0.011. Under linear impact it is −0.022.
- Criterion 4 names lag 5, so it is met under neither law at the population level.
- The report explains the gap from the 10-path fit (0.088 against 0.108) only as greater precision. It omits **selection bias**: the fit minimised J on those very 10 paths.

**Fix.** Restate the criterion-4 row as: "**Not met at 1,000 paths under either law**: ACF|r|₅ −0.025 (square-root) and −0.022 (linear) against a band floor of 0.0014 (`b1b_timing.txt`). The 10-path figures are optimistically biased because the fit selected on those paths." Then ask Héctor to rule either:
- (a) merge with criterion 4 recorded as a known miss, which B3 targets first; or
- (b) hold the merge.

## Findings

1. **Rule against code.** The code's `keep = sp >= 3 && okL && okS`, with each `ok` = all |z| < 3, applies the stated rule exactly. **Pre-commitment is asserted, not verifiable.** The 3× bar first appears in 6d19589, the same commit as the results; note §8 said only "a stated margin". Only one run log exists, which is consistent with a single run.
2. **Tables against files.** All 20 validation rows, both timing rows and the sample counts match. The results file does not record which fit files it used.
3. **Statistics.**
   - The seeds are independent, and the z statistic is a correct two-sample test on means.
   - The multiple-testing remark is fair. Under independence, P(max of 20 |z| ≥ 2.74) ≈ 0.12.
   - **"Equal in distribution" overclaims.** Only the means of 10 statistics were tested, not their spread.
   - The GPU writes closes and lows as **Float32** (BatchGPU.jl l.267–268), so "Float64 price" is true only inside the kernel. The effect is negligible but the statement is inaccurate.
4. **Timing fairness.**
   - The comparison is end-to-end on both sides, at the same parameters, with warm-up excluded. That is fair.
   - Each n was timed **once**. On a laptop, a 4 % margin is within run-to-run and thermal variation.
   - The CPU engine also carries bookkeeping the GPU path drops, so the ratio compares the two implementations as built.
5. **GPU utilisation.** nvidia-smi's `utilization.gpu` is the share of time a kernel was resident. It does not show that all 26 SMs were saturated. It does support "not a CPU fallback": kernel plus transfer is 46.28 of 46.61 s. "Fully busy" overclaims.
6. **Thin margin.** It is stated in the B1b report, the README and the B1a criterion-8 row. It is missing from the commit subject and from the note, which has no B1b amendment yet.
7. **Coherence.**
   - CUDA.jl 6.5.1 is pinned in the project with compat "6.5.1". The default environment stays at 6.1, so CLAUDE.md §7 remains true.
   - `gpu_check.jl` ran in the project environment: its output reports 6.5.1 and sm_120. That satisfies CLAUDE.md §9.
   - Note §8 says "moments computed on the device", but they are computed on CPU threads. This needs an amendment.
   - The branch never touched the note or the build instructions, so main's versions survive the merge.

## Minor fixes (exact wording)

- **B1b report, Validation:** replace "GPU results are equal in distribution, not path by path" with "GPU and CPU moment means agree within Monte Carlo error (all |z| < 3); spreads were not tested, and paths differ because the random streams differ." Make the same change in the README.
- **B1b report, Timing:** replace "The GPU was fully busy" with "A GPU kernel was resident throughout (nvidia-smi utilisation, not SM occupancy). Each n was timed once; at a 4 % margin, a repeat could fall below 3×."
- **B1b report, Rule:** append "Written into `b1b_timing.jl` before the single run of 14:16; first committed with the results (6d19589)."
- **B1b report, Implementation:** change "Float64 price" to "Float64 price inside the kernel; closes and lows are written out as Float32".
- **`b1b_timing.txt` header:** have the script print the two fit-file names.

## Merge-time updates (draft)

**Build instruction frontmatter:**
- `status: executed`
- `executed: 2026-11-17`
- `merged_at: "<merge sha>"`

**Append to the build instruction's `notes`:** "Executed: B1a (CPU engine, targets, null/ablation/recovery, linear and square-root fits) and B1b (GPU batch path kept at 3.12× against a 3.0× bar, a thin margin; validation max |z| 2.74 / 1.71). Criterion 4 [as ruled by Héctor, date]. Cath and Fina sign-offs are in `crypto_abm/reviews/`. CUDA.jl 6.5.1 is pinned in the model's Project.toml."

**Note, new dated line under the amendments:** "*B1 complete, 2026-11-17 (merged at <sha>).* §11 criteria 1–3 and 5–11 are met; criterion 4 is [ruling]. At 1,000 paths, ACF|r| at lag 5 sits below its band under both impact laws, and B3 targets it first. The GPU batch path is kept for B3 at 3.12× (bar 3.0×, thin margin), with the CPU engine as reference. *Amendment (g):* in the GPU path, moments are computed on CPU threads, not on the device."

No price statements.

# Fina — Review of Nina's crypto ABM design note B0 (coherence and evidence)

*Fina · Aurora · 2026-11-16 · Read-only review under D6. I recomputed the figures independently from Appendix A, with my own script. I did not open any abm_b0 script.*
*Filed verbatim by Claude Code, 2026-11-16. The central finding (pre-ETF BTC skewness −1.32 → +0.03 and excess kurtosis 20.7 → 3.56 without 2020-03-12; BTC 2022-11-09 = −14.33 %) was re-verified by Claude Code against the same data before filing.*

## Verdict

**Approve B1, with the changes required below.** Almost every number holds up. The weak points are three: the regime story told in §1.1, how the phases map onto the spec, and the provenance trail. None of them needs B0 rewritten, but each must be fixed before B1 code starts.

## Evidence check

The data: 2,877 closes per asset, 2019-01-01 to 2026-11-16, with no gaps. Against the live Coinbase API, six candles matched to the cent: BTC on 2020-03-12, 2022-11-09, 2025-10-10 and 2026-02-05, and ETH on 2025-10-10 and 2026-11-13/14.

| Figure | Note | Mine | Reproduces |
|---|---|---|---|
| §1.1 annualised s.d. (4 cells) | 69.5 / 46.9 / 88.9 / 67.0 | 69.5 / 47.0 (n=1040) or 46.9 (n=1041) / 88.9 / 67.0 | Yes |
| §1.1 BTC daily s.d., pre / post | 3.63 / 2.45 % | 3.64 / 2.46 % | No (looks truncated, not rounded) |
| §1.1 ETH daily s.d., post | 3.50 % | 3.51 % | No (same) |
| §1.1 skewness, excess kurtosis, ACF of r, ACF of \|r\| | as printed | same, with n=1040 and ddof=1 standardisation | Yes |
| §1.1 share of days with \|log r\| > 0.10 | 2.19 / 0.28 / 3.94 / 2.01 % | 2.19 / 0.29 / 3.95 / 2.02 % | 3 of 4 cells off by 0.01 (truncation) |
| §1.1 worst days; correlation and beta | as printed | same | Yes |
| §1.1 drawdowns, gap to the post-ETF high | −53.1 / −67.6; 48.0 / 62.3 | same, same dates | Yes |
| §1.2 kurtosis without 2020-03-12 | 21.1→4.1; 14.7→4.7 | 21.1→4.1; 14.7→4.7 | Yes |
| §1.3 2025-10-10 | −7.2 % close; −12.1 % intraday; ETH −12.2 % | same | Yes |
| §1.4 BTC 2022-11-09 | −14.4 % | **−14.3 %** (15,891.96 / 18,550.25) | **No** |
| §1.4 other episode figures | as printed | same | Yes |

**Conventions the note does not state.**
- The post-ETF window drops the 2024-01-11 return. Returns are formed within the window, which gives 1,040 of them, and §5's "1,040 days" depends on this.
- Kurtosis and skewness are standardised with the ddof=1 s.d. With ddof=0, pre-ETF BTC kurtosis is 20.8, not 20.7.
- The window behind "3 rolling standard deviations" (§1.2, §5) is never given.

**Log and simple returns get mixed in three places.**
- §6.1 says "frequency of 10 % days" without saying log or simple. Post-ETF BTC has 3 log days but 4 simple days.
- The "3 % day into a 12 % day" in §0 has no return basis.
- In §1.3, the −12.1 % is open-to-low, while the −7.2 % is close-to-close. The two are comparable only because the 10-10 open equals the prior close. Define the intraday target as prior close to low.

**Substantive finding: the evidence for two regimes is thinner than §1.1 claims.**
- Take out 2020-03-12 and the pre-ETF BTC skewness moves from −1.32 to **+0.03**. Pre-ETF kurtosis falls from 20.7 to **3.56**, against 3.44 post-ETF.
- Two of the four bolded contrasts (skewness and kurtosis) therefore rest on one day. §1.2 itself calls that fragile.
- The note's own robust measure, the Hill index on the top 5 % of |r|, barely moves for BTC: 3.25 pre (3.43 without that day) against 3.45 post. For ETH it goes from 2.91 to 3.23.
- The clustering measure (ACF of |r| at lag 1) is unchanged for BTC: 0.158 against 0.156.
- What does shift is the level of volatility, the frequency of 10 % days and ETH's beta.

## Required changes

1. **§1.1 table and "splits the sample cleanly."** Add a column for the pre-ETF window without 2020-03-12, and add the Hill index and the 3σ frequency for both windows. Rewrite the sentence so it says the shift is in the level of volatility and the frequency of large days, not in tail shape. Name the confounders: the April 2024 halving, and the 2021 bubble and 2022 lender collapses that sit inside the pre-ETF window.
2. **§6.1 and §1.1 design consequence.**
   - The regime-shift test lowers the ETF share, but ETF agents only arrive in B2 (§3.2). The test cannot run in B1.
   - It changes the ETF share and leverage together, so it cannot show that "the ETF share is doing mechanism work."
   - It leans on the tail index, which per the finding above has almost no power.
   - Fix: move the test to B2, vary one factor at a time, and target s.d. and the 10 %-day frequency.
3. **Phase map against spec §5.6.**
   - The spec puts SMM calibration in B3. The note puts calibration machinery in B1: the GPU timing at 1k/10k draws (§8) and the intraday moment (§5).
   - The spec's B3 is calibration, but the note's §3.3 makes B3 the two-asset engine.
   - Fix: add a phase table that reconciles the two, and give the spec a dated amendment line.
4. **§1.4 against spec §5.3.** The spec says B0 delivers "calibration targets with sources" and that episodes are "never quoted from memory."
   - The "Usually attributed to" column is memory. Strike it, or mark it UNSOURCED and keep it out of anything B1 targets.
   - Retitle the table: these are not "the largest daily drops." The list leaves out BTC 2019-06-27 (−13.7 %) and ETH 2021-01-21 (−19.3 %, its third-worst day). It includes 2025-10-10 (−7.2 %) and 2026-11-13/14 for other reasons.
   - Fill in the blank ETH cells: −15.7 % on 2022-06-13 and −14.9 % on 2026-02-05.
   - Correct BTC 2022-11-09 to −14.3 %.
5. **§7 bridge to the board. The firewall wording is not airtight.**
   - The README's unruled bands are the peg band, the liquidation-volume bar and the funding/open-interest "stretched" levels. The board has no "drawdown-run leg," so the note invents one.
   - E1's output is a frequency of return days. The board's liquidation bar is a USD volume graded AGGREGATOR, and the model has no dollar scale (D is "to be scaled").
   - Fix, reworded as follows. E1/E4 may motivate a question to Héctor only in board-observable units, with the range across the accepted parameter set and the ABM run id. The ruling is recorded in the README and the state text. Board bands are ruled on observed data now and do not wait for the ABM. crypto_abm never reads from or writes into crypto_monitor/. Also restore spec §0.1's second clause: "no ABM number on the dashboard."
6. **Provenance (PROTO-RAG-001).**
   - No build instruction exists for Part A or B0, although the spec footer says one is due once Part A is approved. That matters here because firewall point 2 needs rulings recorded with provenance. Today D1–D6 live only in an editable §10.
   - The §1 figures come from scripts in /tmp, which a reboot or cleanup can wipe.
   - Minimal fix: file one build instruction, `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_board_and_abm_b0.md`. Set `build_type: initial_scaffold`, `status: executed` for Part A and B0, and pending for B1. Add `agents_involved: Nina (drafted by Claude Code), Cath, Fina`. Back-link it from the spec, the README and the note.
   - Commit the data snapshot, with a SHA-256 checksum, and the targets script in B1.
   - Change the status line to "D1–D6 ruled; endorsement pending Cath/Fina." As written, "APPROVED" reads as reviewed.
7. **§8 location and GPU checks.**
   - The Dalila-spcx worktree is sparse: it covers crypto_monitor, nvda_watch and spcx_monitor, and has no `tests/`. It is also `reset --hard main` daily at 18:00.
   - B1 must not be developed or run there. State the branch and checkout.
   - When CUDA.jl enters the new Project.toml, run `tests/gpu_check.jl` in that environment, as CLAUDE.md §9 requires.

## Recommended changes

- In §1.2, "fivefold" holds for BTC (21.1 to 4.1), not ETH (14.7 to 4.7, about 3×).
- In §2, call the clearing rule "a reduced-form stand-in for" the Brunnermeier-Pedersen spiral, not that spiral "written as one equation."
- In §9, say plainly that this does not yet meet the Monetary Foundation §10 line on "interface specification simultaneously." The core's "Gaussian noise is the only exogenous input" rule also needs a hook for Gina's external-stress layer before any sovereign instance.
- In §8, the remark about moving the sovereign instances to Ester in about two months reads as if the sovereign work starts then. Spec §5.7 holds it until crypto passes B3. Also, as of 11-16 Ester has no NVIDIA driver.
- §3.3 writes "(0.83; 1.18)" as if both numbers were betas. Label them correlation and beta.

## Cadence

B0 through B4 in two months is not realistic. Each phase waits for a go, Héctor is carrying many concurrent missions, and the holidays fall inside the window. B4 also depends on a Duffie-Reis monetary ABM that has no design note yet.

A realistic plan for mid-January:
- B1 done.
- B2 under way.
- B3 after Ester is ready, which fits the CIEP/ITED deferral.
- B4 not before Q1 2027.

Under the one-method-at-a-time rule, split B1. B1a is the CPU engine plus the stylized facts plus parameter recovery. B1b is the GPU batch gate, or it moves to B3.

## Proposed B1 acceptance criteria

1. **Layout.** The §8 layout under Julia 1.11.7, with a `.md` companion per module. A grep test shows no crypto terms (funding, perp, BTC, Coinbase, UTC) in `src/core/`.
2. **Reproducible targets.** `targets/` recomputes §1 from the committed snapshot, with conventions stated (window boundaries, ddof, rolling window), and matches the corrected note.
3. **Null test.** With noise only, excess kurtosis and the ACF of |r| are about zero.
4. **Stylized facts.** At least one parameter vector puts post-ETF BTC moments inside block-bootstrap 95 % bands: ACF of r, ACF of |r| at lags 1/5/20, Hill index, 3σ frequency. Misses are listed.
5. **Ablation.** Switching off the cascade loop moves the tail moments materially.
6. **Parameter recovery.** On synthetic data, recover at least w_ℓ, median L, s_D and κ with stated coverage, and name the parameters that are not identified.
7. **Determinism.** A fixed seed gives bit-identical runs, with common random numbers.
8. **Timing and GPU.** A timing table, plus `gpu_check.jl` if CUDA is used, or an explicit CPU-only statement.
9. **Firewall.** A test that nothing touches crypto_monitor/, and a README that restates the firewall.
10. **Limitations.** A section on equifinality, a run with the linear-impact alternative, and regime dependence.
11. **Sign-off.** The build instruction is filed and Cath/Fina have signed off.

## What I could not check

- The intraday lows beyond 2025-10-10. I spot-checked daily candles only and fetched no hourly data.
- Whether 2026-02-05 has a sourced cause, and every attribution in §1.4.
- Whether the "new" guard in the render script protects untracked files.
- The engine and §9, which are Cath's.
- That D1–D6 were ruled, which I take from the note.

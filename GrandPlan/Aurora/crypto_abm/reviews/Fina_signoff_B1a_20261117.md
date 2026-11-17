# Fina — Sign-off check of B1a (evidence and coherence)

*Fina · Aurora · 2026-11-17 · Read only. I checked `~/Dalila-abm` at 999b613 and main at 70edecc. I recomputed the data targets from `targets/data` with a new script of my own, `fina_check/scripts/check_b1a.py`. I ran no fits.*
*Filed verbatim by Claude Code, 2026-11-17. Fixes 1–2 (note amendments) were applied on main. Fixes 3–8 were applied in the B1a report and companions after the full rerun that Cath's fixes required.*

## Verdict

**Sign off B1a with minor fixes (listed; no re-check needed).** `julia --project=. test/runtests.jl` passes 413 of 413 tests in about 6 s. Every table in the report matches its results file to the printed precision, and the data targets reproduce. The fixes are wording and provenance. Three B1a deviations from the note have not gone back into it as dated amendments, which the build instruction's §1 requires. The σ_ε ruling cites a note bound that does not exist. Two claims in the report have no results file behind them.

## Per-criterion table

| # | Report says | Evidenced by | Finding |
|---|---|---|---|
| 1 | Met | test §1 | Met. The grep test and the four companions pass. `src/CryptoABM.jl` has no `.md` companion; this is minor. |
| 2 | Met | test §2 | Met, but overstated. The test checks 8 cells, not "every §1.1 cell". σ̄, the −3.09-point gap and the 1.58 % calibration target are not tested. My recomputation confirms all three. |
| 3 | Met | test §3 | Met by the test's thresholds. The quoted values (−0.03 and 0.004) appear in no committed file. |
| 4 | Met, 9/10 | `fit_linear_…txt` | Met. All the moments the criterion names are inside their bands. |
| 5 | Met | `ablations_bestfit_*.txt` | Met. The "κ alone" figures (0.042 / 6.1 against 0.037 / 6.2) appear in no committed file. |
| 6 | Met, locally | `recover_…txt`, fit.jl l.182 | Met. The ±0.15 start perturbation in u-space is confirmed in fit.jl. |
| 7 | Met | test §7 | Met. Paths are bit-identical, and the conservation tolerances are 1e-10 and 1e-9. |
| 8 | Met for B1a | README | Met by the CPU-only statement. The timing is unevidenced, and the sources disagree: about 0.1 s in the README, 0.16 s in the report. `tests/gpu_check.jl` is in the sparse checkout, and CUDA is in the default environment, so B1b can run it. |
| 9 | Met | test §9 | Met. No code references `crypto_monitor`. The only mention of the board is a firewall docstring in CryptoAdapter.jl l.10, which is acceptable. |
| 10 | Met | sqrt files | Met, with the wording problems listed below. |
| 11 | Pending | — | This memo is Fina's part. |

## Number check

- **SHA-256.** All three CSVs match `SHA256SUMS`. The daily closes are identical to the v1 snapshot (2,877 rows).
- **σ̄ = 0.5021 %/h.** This reproduces as the RMS of hourly log returns from 2024-01-11 to 2026-11-16, with 10 missing hours in 2 gaps. Starting from 01-12 gives 0.501 %. **But note §2 R2 defines σ̄ differently**, as the post-ETF mean of σ̂, which is the 24-sub-step trailing realised volatility. That mean is 0.445 %/h, about 11 % lower. The code follows the report's definition, so the note is the document that needs changing.
- **Intraday gap.** On the 10 largest down days, prior close to low averages −10.99 % against −7.90 % close to close, a gap of −3.09 points. This reproduces.
- **"Open equals prior close on 5 of 10 days."** This reproduces only at rtol 1e-6. On all ten days the open is within 0.006 % of the prior close, so the choice of base is immaterial. Targets.md presents it as a "finding", which overstates it.
- **3σ share, within-window convention.** 1.58 % (950 days) reproduces. It is stated consistently in the report, in Moments.md l.11 and in the alternatives in Appendix A. Note §5 still says only "(90-day trailing s.d.)", and Appendix A's default is the full-history version, at 1.92 %.

## Fixes (exact wording)

1. **The σ_ε ruling.** Note §4 says σ_ε is "free"; the bound 0.002–0.05 lives in `experiments/fit.jl` BOX. Do two things:
   - In the report (limitation 2 and the sqrt section), replace "the bound stays as set in note §4 and is noted" with "the bound stays as set in the B1a search box (`fit.jl`, σ_ε ∈ [0.002, 0.05], log scale) and is noted".
   - Add to note §4, on the σ_ε row: "*Amendment 2026-11-17 (B1a): searched on [0.002, 0.05]; the fit sits at the upper bound under both impact laws. RULED 2026-11-17 (Héctor): the bound stays and is noted; widening it is a separate recorded decision.*"
2. **Note amendments required by the build instruction's §1.** Add one dated block, "*Amendments from B1a, 2026-11-17*", with three lines:
   - (a) R2: "σ̄ is the RMS of hourly log returns over the post-ETF window, 0.502 %/h, not the mean of σ̂."
   - (b) §5: "For calibration, the 3σ share uses a within-window trailing s.d. for data and model, 1.58 % for post-ETF BTC."
   - (c) §6.3 and §11.10: "The base rule is already linear in log price, so the clearing-rule alternative is square-root impact (q₀ = 0.002 of float per sub-step, a normalisation choice)."
3. **Report, sqrt section, the "Robust" bullet.** Replace "switching it off makes returns Gaussian under both laws" with "switching it off thins the tails under both laws, to a Hill index of 6.08 under square-root impact and 4.52 under linear, and removes the 10 % days and most of the intraday gap".
4. **Report, after the sqrt fit table.** Add: "One rough search per law; J values are not comparable as a test, and neither law is preferred. κ sits at its lower box edge under square-root impact."
5. **Report, criterion 2 evidence.** Replace "every §1.1 cell reproduced" with "8 key cells tested; σ̄, the intraday gap and the 1.58 % target were recomputed independently by Fina, 2026-11-17".
6. **Unevidenced numbers.** Commit the output of `first_run.jl`, the κ-only null runs and the single-path timing to `experiments/results/`. Otherwise strike those numbers. Align the README and the report on one timing figure.
7. **Targets.md.** Replace "*Finding:* the daily candle's open equals the prior close on only 5 of these 10 days." with "The open equals the prior close within 1e-6 on 5 of 10 days, and within 0.006 % on all ten; the target measures from the prior close by definition."
8. **Report header.** Change "(2026-11-16)" to "(2026-11-16, updated 2026-11-17)".

The square-root finding is otherwise fairly worded: the κ conclusion is called not robust, and parameter values are tied to the impact law. The build instruction's notes match what was built, and its status correctly stays at `pending_execution` until B1b and the merge. I made no edits and no price statements.

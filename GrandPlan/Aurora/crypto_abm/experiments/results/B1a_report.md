# B1a report — crypto ABM, bitcoin, CPU (2026-11-16)

*Phase B1a of design note B0 v1.2. Branch `aurora-crypto-abm`, checkout `~/Dalila-abm`. Build instruction `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_abm_b1.md` (2_of_2). Drafted by Claude Code in Nina's role.*
*Every statement here is conditional on the model. Nothing here is a statement about where bitcoin will trade, and nothing here enters the crypto regime board (note §0).*

## Status against note §11

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | Layout, `.md` companions, no crypto terms in `src/core/` | **Met** | `test/runtests.jl` §1: 376 line checks plus 4 companions |
| 2 | Targets reproduce §1 from the committed snapshot | **Met** | §2 tests; every §1.1 cell reproduced; SHA-256 verified |
| 3 | Null test, noise only and κ = 0 | **Met** | excess kurtosis −0.03, ACF\|r\|₁ 0.004 (5 paths) |
| 4 | Stylized facts inside 95 % block-bootstrap bands | **Met** (9 of 10 moments; all moments the criterion names) | `fit_linear_20261116_2157.txt`; the daily s.d. misses (2.72 % vs band 2.20–2.70 %) |
| 5 | Ablations move moments materially | **Met** | `ablations_bestfit_linear.txt` (below) |
| 6 | Parameter recovery, with non-identified parameters named | **Met, locally** | `recover_20261116_2221.log`; κ and σ_ε are weakly identified; starts were near the truth (see limitation 4) |
| 7 | Determinism and conservation | **Met** | bit-identical paths; units and cash conserved to 1e-10 / 1e-9 |
| 8 | Timing; CPU-only statement or GPU check | **Met for B1a** | CPU only, stated in the README; one 1,040-day path ≈ 0.16 s; the B1b gate is pending |
| 9 | Firewall test | **Met** | §9 test: no code file names the board |
| 10 | Limitations, including a linear-impact alternative | **Partly met** | Limitations below. The κ = 0 constant-impact run is done; a second functional form (square-root impact) is **not yet run** |
| 11 | Sign-off by Cath and Fina | **Pending** | |

## Data targets (post-ETF BTC, 2024-01-12 → 2026-11-16, 1,040 daily returns)

- σ̄ = 0.502 % per hour (RMS of hourly log returns, a fixed constant).
- Intraday target: on the 10 largest down days, prior close → low averages −11.0 % against −7.9 % close → close (gap −3.09 points).
- Calibration convention: the 3σ-day share uses a trailing s.d. *within* the series for both data and model, which gives 1.58 % for the data. Note §1.1 reports the full-history convention, 1.92 %.

## Rough fit (criterion 4)

Method:
- Random search: 2,000 draws over 11 parameters inside the note §4 box.
- Then Nelder–Mead from the 8 best draws.
- R = 10 replications per draw, with common random numbers.
- Objective: squared distance weighted by the bootstrap s.d. (moving blocks of 20 days, 1,000 resamples).
- Run: 16 CPU threads, 24 minutes, in Zellij.
- No draw aborted; the cascade cap never bound.

| Moment | Model | Data | 95 % band | |
|---|---|---|---|---|
| s.d. | 0.0272 | 0.0246 | [0.0220, 0.0270] | outside |
| ACF r, lag 1 | −0.049 | −0.046 | [−0.118, 0.031] | inside |
| ACF \|r\|, lag 1 / 5 / 20 | 0.145 / 0.056 / 0.008 | 0.156 / 0.100 / 0.038 | — | inside |
| Hill index | 4.13 | 3.45 | [2.74, 4.46] | inside |
| 3σ-day share | 1.30 % | 1.58 % | [1.16 %, 2.53 %] | inside |
| Skewness | −0.001 | 0.115 | [−0.21, 0.52] | inside |
| Share of 10 % days | 0.39 % | 0.38 % | [0, 0.87 %] | inside |
| Intraday gap | −1.37 pts | −3.09 pts | [−4.58, −1.32] | inside (at the edge) |

The best vector (J = 13.66) is λ₀ 0.44, σ_ε 0.045, w_m 0.11, β 2.51, w_l 0.19, median L 18.2, κ 0.28, φ 0.47, ρ 0.068, median D 0.29, s_D 0.91. It is **one** acceptable vector, not an estimate. Four parameters sit near the edges of the search box: σ_ε, median L, ρ and s_D.

## Ablations at the best fit (criterion 5)

| Moment | Best fit | Cascade loop off | φ = 0 | κ = 0 | No leveraged traders | Data |
|---|---|---|---|---|---|---|
| s.d. | 0.0272 | 0.0231 | 0.0365 | 0.0259 | 0.0164 | 0.0246 |
| ACF r₁ | −0.049 | −0.010 | **0.231** | −0.043 | −0.090 | −0.046 |
| ACF \|r\|₁ | 0.145 | **0.052** | 0.192 | **−0.008** | **0.024** | 0.156 |
| Hill | 4.13 | 4.52 | 4.11 | **5.57** | **5.90** | 3.45 |
| 3σ share | 1.30 % | 1.02 % | 1.34 % | 0.61 % | 0.40 % | 1.58 % |
| 10 % days | 0.39 % | 0.05 % | 1.68 % | 0 | 0 | 0.38 % |
| Intraday gap (pts) | −1.37 | −0.44 | −0.24 | −0.45 | −0.32 | −3.09 |

**Conditional reads:**
- Volatility clustering and the fat tails need **both** the leveraged traders' cascades and liquidity withdrawal (κ). Removing either one removes most of the clustering.
- **κ alone produces nothing.** Noise only with κ = 0.28 gives ACF\|r\|₁ 0.042 and a Hill index of 6.1. Noise only with κ = 0 gives 0.037 and 6.2. That answers Cath's endorsement concern: at the fitted κ, the stylized facts come from agent behaviour, not from the impact rule.
- Permanent impact (φ = 0) makes returns trend, with ACF r₁ +0.23, and it erases the intraday gap. Transient impact is needed, as the note anticipated.

## Parameter recovery (criterion 6)

Setup: the truth is the best fit. 8 synthetic 1,040-day paths. Each is refit with the same Nelder–Mead from a start perturbed by up to ±15 % of each range.

| Parameter | Truth | Mean estimate | s.d. | Range |
|---|---|---|---|---|
| w_l | 0.194 | 0.195 | 0.033 | 0.158–0.231 |
| median L | 18.16 | 17.96 | 1.30 | 15.8–20.0 (box edge) |
| s_D | 0.912 | 0.885 | 0.076 | 0.79–0.98 |
| κ | 0.280 | **0.159** | 0.082 | 0.04–0.32 |

Mean |error| as a share of each range: λ₀ 0.02, ρ 0.03, L 0.06, φ 0.07, s_D 0.08, D 0.08, κ 0.09, β 0.10, w_l 0.11, w_m 0.11, **σ_ε 0.14**.

**Weakly identified:** κ (biased down by about 40 %, wide) and σ_ε (largest error). **Recovered without visible bias:** w_l and median L.

## Limitations (criterion 10)

1. **Equifinality.** One acceptable vector is reported, not the acceptance set. Full SMM and the J-test set belong to B3.
2. **Box edges.** σ_ε, median L, ρ and s_D sit near the bounds of the §4 box. The box may be binding. Widening it is a design choice to rule on, not a silent change.
3. **Clearing rule.** Only one functional form has been run, log-linear impact with κ (κ = 0 is its constant-impact special case). The square-root-impact alternative has not been run yet.
4. **Recovery is local.** Starts were within ±15 % of each range around the truth. A recovery from random starts would test global identification and is not done.
5. **Perp = spot.** One price for both. Basis and funding dislocations cannot appear.
6. **Regime dependence.** The fit is to post-ETF data, without ETF agents. It is provisional until B2 adds them and recalibrates.
7. **The intraday gap** is matched only at the edge of its band (−1.4 vs −3.1 points). Cascades in the model are shallower intraday than in the data.

## Not done in B1a

- The square-root-impact run (criterion 10).
- Global-start recovery (optional).
- **B1b:** the batched CPU/GPU timing gate.
- Cath and Fina sign-off.

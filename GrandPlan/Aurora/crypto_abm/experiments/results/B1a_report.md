# B1a report — crypto ABM, bitcoin, CPU (2026-11-16, updated 2026-11-17)

*Phase B1a of design note B0 v1.2, with the B1a amendments on main (3b828d2). Branch `aurora-crypto-abm`, checkout `~/Dalila-abm`. Build instruction `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_abm_b1.md` (2_of_2). Drafted by Claude Code in Nina's role.*
*Every statement here is conditional on the model. Nothing here says where bitcoin will trade, and nothing here enters the crypto regime board (note §0).*

**This version (2026-11-17) replaces the first report.** Cath and Fina signed off B1a with minor fixes (`../../reviews/`). Cath found two implementation errors:
- the square-root impact applied √ to each cascade round;
- the no-cascade ablation double-booked flow at the liquidity provider.

She also asked for the transient decay to enter σ̂. All fixes are in (6e32826), and every result was rerun on the corrected code (`b1a_rerun_20261117_1239.log`). The pre-fix results are in `superseded_pre_signoff/`. **The rerun reverses one earlier finding** (κ; see *Findings*).

## Status against note §11

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | Layout, `.md` companions, no crypto terms in `src/core/` | **Met** | `test/runtests.jl` §1; five companions, including `src/CryptoABM.md` |
| 2 | Targets reproduce §1 from the committed snapshot | **Met** | §2 and §2b tests check 8 key §1.1 cells plus σ̄ (0.502 %/h), the intraday gap (−3.09 pts) and the within-window 3σ target (1.58 %). Fina recomputed σ̄, the gap and 1.58 % independently on 2026-11-17. SHA-256 verified. |
| 3 | Null test: noise only, κ = 0 | **Met** | Test §3 at default parameters. `null_check_transient.txt` at the fitted parameters (see *Null at the fitted parameters*) |
| 4 | Stylized facts inside 95 % block-bootstrap bands | **Not met at 1,000 paths under either law** (restated after the B1b review, Fina, 2026-11-17). ACF\|r\|₅ is −0.025 (square-root) and −0.022 (linear) against a band floor of 0.0014 (`b1b_timing.txt`). The 10-path fit figures (10 of 10 square-root, 9 of 10 linear) are optimistically biased, because the fit selected the parameters on those paths. All other named moments are inside their bands at 1,000 paths. **RULED 2026-11-17 (Héctor): merge with criterion 4 recorded as a known miss; the persistence of volatility clustering (ACF\|r\|₅) is the first B3 target.** | `fit_*_2026111*.txt` (10 selected paths); `b1b_timing.txt` (1,000 independent paths) |
| 5 | Ablations move moments materially | **Met** | `ablations_bestfit_linear.txt`, `ablations_bestfit_sqrt.txt` |
| 6 | Parameter recovery, with non-identified parameters named | **Met, locally** | `recover_20261117_1303.txt`. κ cannot be told apart from zero under linear impact; starts were near the truth |
| 7 | Determinism and conservation | **Met** | Bit-identical paths. Conservation to 1e-10 / 1e-9 with the cascade loop on and off (test §7, §7b) |
| 8 | Timing; CPU-only statement or GPU check | **Met** (B1b, 2026-11-17) | CPU: 0.231 s per path on one thread (`null_and_timing.txt`). GPU gate: kept at 3.12× (thin margin), `gpu_check.jl` passed in the environment (`B1b_report.md`) |
| 9 | Firewall test | **Met** | Test §9 |
| 10 | Limitations and a clearing-rule alternative | **Met** | Square-root impact on cumulative flow, refit with ablations; limitations below |
| 11 | Sign-off by Cath and Fina | **Given, with minor fixes; no re-check needed** | `reviews/Cath_signoff_B1a_20261117.md`, `reviews/Fina_signoff_B1a_20261117.md`; fixes applied here |

Criterion 4 asks for at least one parameter vector with the named moments inside their bands. On the 10 paths the fit selected on, that holds under square-root impact. On 1,000 independent paths it fails at one moment under both laws: ACF\|r\|₅, the persistence of volatility clustering beyond a day. See *Findings* 6.

## Data targets (post-ETF BTC, 2024-01-12 → 2026-11-16, 1,040 daily returns)

- σ̄ = 0.502 % per hour, the RMS of hourly log returns. It is a fixed constant (note amendment (a)).
- Intraday target: on the 10 largest down days, prior close → low averages −11.0 % and close → close −7.9 %, a gap of −3.09 points.
- Calibration convention: the 3σ-day share uses a within-window trailing s.d. for both data and model, which gives 1.58 % (amendment (b)).

## Fits (criterion 4)

The same procedure ran under each impact law:
- random search, 2,000 draws over 11 parameters inside the B1a search box (`fit.jl` BOX);
- then Nelder–Mead from the 8 best draws;
- R = 10 replications per draw, with common random numbers;
- objective weighted by the bootstrap s.d. (moving blocks of 20 days, 1,000 resamples);
- 16 CPU threads, about 24 minutes per law, in Zellij.

No draw aborted. A binding cascade cap now stops the fit instead of being scored (`fit.jl`), and none occurred.

| Moment | Linear | Square-root | Data | 95 % band |
|---|---|---|---|---|
| s.d. | 0.0244 | 0.0253 | 0.0246 | [0.0220, 0.0270] |
| ACF r₁ | −0.060 | −0.052 | −0.046 | [−0.118, 0.031] |
| ACF \|r\|₁ | 0.108 | 0.194 | 0.156 | [0.056, 0.234] |
| ACF \|r\|₅ | **−0.001** (outside) | 0.011 | 0.100 | [0.001, 0.148] |
| ACF \|r\|₂₀ | 0.011 | 0.021 | 0.038 | [−0.064, 0.060] |
| Hill index | 3.48 | 3.64 | 3.45 | [2.74, 4.46] |
| 3σ-day share | 2.10 % | 1.38 % | 1.58 % | [1.16 %, 2.53 %] |
| Skewness | −0.085 | −0.048 | 0.115 | [−0.21, 0.52] |
| 10 % days | 0.39 % | 0.42 % | 0.38 % | [0, 0.87 %] |
| Intraday gap (pts) | −3.50 | −2.04 | −3.09 | [−4.58, −1.32] |
| J | 12.65 | 9.70 | | |

Best vectors:

| | λ₀ | σ_ε | w_m | β | w_l | median L | κ | φ | ρ | median D | s_D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Linear | 1.27 | 0.0186 | 0.101 | 2.41 | 0.158 | 11.3 | **0.027** | 0.68 | 0.19 | 0.40 | 0.61 |
| Square-root | 2.71 | 0.0033 | 0.060 | 2.02 | 0.276 | 7.0 | **0.32** | 0.70 | 0.14 | 0.16 | 0.55 |

There was one rough search per law. J values are not comparable as a test, and neither law is preferred.

Box edges:
- Linear: κ sits at its lower edge.
- Square-root: λ₀ is at its upper edge, median D at its lower edge, and w_l near its upper edge.
- **σ_ε is no longer at its bound under either law** (0.69 and 0.16 of the range). The 2026-11-17 ruling (keep the B1a search box, σ_ε ∈ [0.002, 0.05], log scale) stands but no longer binds.

## Ablations at each best fit (criterion 5)

**Linear impact**

| Moment | Best | Cascade loop off | φ = 0 | κ = 0 | No leveraged | Data |
|---|---|---|---|---|---|---|
| s.d. | 0.0244 | 0.0204 | 0.0686 | 0.0243 | 0.0148 | 0.0246 |
| ACF r₁ | −0.060 | 0.006 | **0.250** | −0.055 | −0.087 | −0.046 |
| ACF \|r\|₁ | 0.108 | 0.056 | 0.136 | 0.078 | **0.020** | 0.156 |
| Hill | 3.48 | 3.86 | 5.49 | 3.48 | **6.03** | 3.45 |
| 3σ share | 2.10 % | 1.45 % | 1.30 % | 2.07 % | **0.34 %** | 1.58 % |
| 10 % days | 0.39 % | 0.04 % | 14.0 % | 0.41 % | **0** | 0.38 % |
| Gap (pts) | −3.50 | −1.47 | −0.22 | −3.63 | **−0.66** | −3.09 |

**Square-root impact**

| Moment | Best | Cascade loop off | φ = 0 | κ = 0 | No leveraged | Data |
|---|---|---|---|---|---|---|
| s.d. | 0.0253 | 0.0333 | 0.1995 | 0.0232 | 0.0116 | 0.0246 |
| ACF r₁ | −0.052 | −0.097 | 0.080 | −0.032 | 0.221 | −0.046 |
| ACF \|r\|₁ | 0.194 | 0.291 | 0.604 | 0.181 | 0.184 | 0.156 |
| Hill | 3.64 | 2.28 | 4.34 | **4.74** | **4.18** | 3.45 |
| 3σ share | 1.38 % | 2.32 % | 3.48 % | **0.85 %** | **0.94 %** | 1.58 % |
| 10 % days | 0.42 % | 2.24 % | 26.7 % | **0.01 %** | **0** | 0.38 % |
| Gap (pts) | −2.04 | −1.96 | −1.04 | **−1.01** | **−0.51** | −3.09 |

## Findings (conditional on the model)

1. **Robust under both impact laws: leveraged traders carry the tails.**
   - Without them, the Hill index rises (6.03 linear, 4.18 square-root).
   - 3σ days fall to about a third or less.
   - 10 % days disappear.
   - The intraday gap shrinks to about −0.5 to −0.7 points.
2. **Robust: transient impact is needed.** With φ = 0, returns trend (ACF r₁ +0.25 linear, +0.08 square-root) and volatility is far too high under both laws.
3. **Not robust: liquidity withdrawal (κ). It is not identified by these moments, and the earlier reading is withdrawn.**
   - **Linear:** the fit sets κ ≈ 0.03, and removing it changes little. Recovery cannot tell κ from zero (truth 0.027, estimates 0.009 ± 0.015).
   - **Square-root:** the fit sets κ = 0.32, and removing it thins the tails (Hill 3.64 → 4.74), cuts 3σ days (1.38 % → 0.85 %), removes the 10 % days and halves the intraday gap.
   - **This is the opposite of the pre-fix results** (linear κ 0.28 needed; square-root κ ≈ 0). Those were shaped by the two implementation errors Cath found.
   - Conclusion: whether liquidity withdrawal matters depends on the impact law and on details of the clearing rule. No statement about it may be made without naming both. It stays an open question for B3.
4. **The "cascade loop off" ablation is not a clean test across laws.** As implemented, forced orders still execute; their impact is only deferred to the next sub-step.
   - Under linear impact, deferring halves clustering, removes the 10 % days and shrinks the gap (−3.50 → −1.47).
   - Under square-root impact, deferring *raises* volatility and fattens the tails (Hill 2.28, 10 % days 2.2 %), because the forced flow then clears together with the next batch.
   - "No leveraged traders" is the cleaner test of the cascade mechanism, and it gives the same answer under both laws (finding 1).
5. **Parameter values depend on the impact law.** Median leverage is 11.3× (linear) against 7.0× (square-root); the leveraged share 0.16 against 0.28. λ₀ is not comparable across laws. No parameter value may be quoted without its law.
6. **The model's volatility clustering decays too fast, under both laws.** At 1,000 paths ACF|r| at lag 5 is about −0.02 against 0.10 in the data; the clustering lives within a day or two. One untested candidate is the missing wealth dynamics (limitation 9). This is the main miss of B1a.

## Null at the fitted parameters (criterion 3, supplement)

With noise only at the fitted linear impact parameters (φ 0.68, ρ 0.19, κ = 0), ACF|r|₁ is 0.074 while the tails stay Gaussian (excess kurtosis −0.03).

This is **mechanical**. Transient impact makes noise-only returns mean-revert (ACF r₁ −0.29), and for Gaussian returns that alone implies ACF|r|₁ = 0.072. With φ = 0 it is 0.0005.

In the full model, ACF r₁ is only −0.06, which implies at most about 0.002 of mechanical |r| autocorrelation. The model's 0.108 is therefore not this artefact. File: `null_check_transient.txt`. The default-parameter null of test §3 passes (|excess kurtosis| < 0.25, |ACF\|r\|₁| < 0.05).

## Parameter recovery (criterion 6; linear impact, post-fix)

Setup: the truth is the linear best fit. 8 synthetic 1,040-day paths, each refit with the same Nelder–Mead from a start perturbed by up to ±15 % of each range.

| Parameter | Truth | Mean estimate | s.d. | Range |
|---|---|---|---|---|
| w_l | 0.158 | 0.162 | 0.022 | 0.133–0.196 |
| median L | 11.32 | 11.84 | 0.73 | 11.07–13.03 |
| s_D | 0.608 | 0.610 | 0.073 | 0.51–0.71 |
| κ | 0.027 | 0.009 | 0.015 | 0.00–0.045 |

Mean |error| as a share of each range: κ 0.015, L 0.037, φ 0.042, ρ 0.042, λ₀ 0.047, w_l 0.069, s_D 0.070, σ_ε 0.078, β 0.095, w_m 0.098, **median D 0.118**.

Reading:
- **Recovered:** w_l, median L (slightly high) and s_D.
- **κ** is recovered as "near zero", but cannot be told apart from zero.
- **Median D** has the largest error.

## Limitations (criterion 10)

1. **Equifinality.** One acceptable vector per law is reported, not the acceptance set. Full SMM and the J-test set belong to B3.
2. **Box edges.** See *Fits*. The σ_ε ruling (keep the B1a search box) stands, but σ_ε no longer sits at the bound. κ (linear) and λ₀, median D (square-root) sit at edges.
3. **Clearing rule.** Findings 3–5 show that κ's role and the parameter values depend on the impact law. Only two laws have been tried.
4. **Recovery is local.** Starts were within ±15 % of each range around the truth. Global identification is untested.
5. **Perp = spot.** One price for both.
6. **Regime dependence.** The fit is to post-ETF data without ETF agents. It is provisional until B2.
7. **The no-cascade ablation** defers rather than removes forced-flow impact (finding 4).
8. **m₁ = 0 throughout**, so the margin channel of the spiral is off.
9. **Leveraged traders re-enter with fixed size and fresh equity**, so there are no wealth dynamics. This is possibly related to finding 6.
10. **λ₀ is not comparable across impact laws.**

## Not done in B1a

- Global-start recovery (optional).
- ~~**B1b:** the batched CPU/GPU timing gate.~~ Done 2026-11-17 (`B1b_report.md`): GPU path kept.
- Merge into main, once B1b is done or moved to B3.

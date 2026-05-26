# Claude Code Instructions — Draft-June Integration v1

**Repository:** working LaTeX project for the BID 2 paper, Overleaf-bound.
**Base file (read-only):** `Draft-June.tex` (1,312 lines, current spine).
**Source artifacts for the integration:**
- `SESSION_LOG_2026-05-24_25.md` — the aging experiment results and economic story.
- `aging_comparison_gap.csv` — three-row reportable table (RUN 1, C1, C2).
- `welfare_panel_gap.png` — 2×2 welfare panel by (sex, skill).
- `c2_interp1_crash_panel.png` — three-panel figure for the infeasibility result.
- `C2_interp1_no_finite_SS.md` — formal write-up of the infeasibility finding.
- `run_calibration.jl` — Diego's SMM calibration scaffold (four modes).

**Deliverable:** A new LaTeX file `Draft-June-v2.tex` containing the full
text of Draft-June plus two new sections, written in Overleaf-compatible
LaTeX (no Julia-side artifacts, no figures generated at compile time —
all figures are pre-existing PNG/PDF files referenced via `\includegraphics`).

**Calendar.** Héctor's plan: draft finished Sunday (2026-05-31). Monday and
Tuesday reserved for presentation prep. June 5 is the IDB seminar. The
draft must therefore be *complete enough to circulate* by Sunday, with the
calibration section explicitly written to accommodate partial calibration
(targets and methodology present; numerical results conditional on what
Judy and Milo deliver).

---

## 1. Operating principles

**Do not edit `Draft-June.tex`.** Read it. Copy its content verbatim into
`Draft-June-v2.tex` and insert the new material at the locations specified
in §3. This protects against losing the existing draft if anything goes
wrong with the integration.

**Preserve existing labels and citations.** All `\label{}` keys in
Draft-June.tex must continue to resolve in v2. New labels follow the
convention `sec:`, `subsec:`, `tab:`, `fig:`, `eq:` consistent with what
already exists.

**Match the file's stylistic voice.** Draft-June is written in formal
econ-journal English, dense but readable, with selective use of
`\citet`/`\citep`, displayed math, and inline emphasis via `\emph` and
`\textit`. New material must match this register. Avoid bullet points
in the body text; tables and lists go inside `\begin{table}` or
`itemize`/`enumerate` blocks with measured use.

**Be honest about provenance.** Three categories of caveat must appear
explicitly somewhere in the new sections:

1. The 2050 demographic primitives are derived via a one-parameter
   Brass-logit shift of the 2020 baseline schedule, anchored to UN WPP
   2024 medium-variant life-expectancy targets. They are *not* extracted
   from a downloaded WPP single-age life table aggregated to 5-year bands;
   that is the September-deliverable refinement.
2. The gender extension currently uses sex-asymmetry stubs
   (`e^F = 0.85 · e^M`, +25% female survival uplift). Sex-specific
   calibrated primitives are the September deliverable; the qualitative
   patterns of the current welfare panel are robust, the magnitudes are
   stub-dependent.
3. RUN 1 and C1 welfare values come from a focused-recovery driver, not
   from full GE re-solves. They are economically sensible but not
   bit-precise (RUN 1 Euler max log10 = −0.61; C1 capital-market residual
   = 13%). Footnote this on the welfare table. The C2 welfare is
   bit-precise from a dedicated standalone driver.

These caveats are not asides; they belong in the body or in clearly
numbered footnotes, because the seminar audience will ask.

---

## 2. What to write — overview

Two new sections inserted into Draft-June. One overhauled section
(Calibration Strategy → Calibration). One light edit pass elsewhere.

| Section | Location in Draft-June | Action |
|---|---|---|
| **§5 Calibration** | replaces current §3 (currently labeled `\section{Calibration Strategy}`, lines 649–757) | rewrite to match `run_calibration.jl` structure; flexible (parameter-table + method, with partial-vs-complete switch) |
| **§7 Cost of Inaction — Comparative Steady State under 2050 Demographics** | new, inserted after `§6 Policy Counterfactuals` (after line 1117), before current `§7 Formalization Experiment` | three reportable equilibria + the C2 interp-1 infeasibility |
| **§8 Formalization Experiment** | bumped from §7 | no content change, only the section number changes (LaTeX handles automatically; just check `\ref` targets) |
| Intro edits | lines 103–131 | one paragraph added at the end of §1 previewing the aging-experiment result |

The renumbering of the formalization experiment is automatic in LaTeX —
no manual edit needed unless internal cross-references point to "Section 7"
by number rather than by `\ref`. Audit cross-references in the final pass.

---

## 3. Section-by-section instructions

### 3.1 Calibration Strategy → Calibration (rewrite)

Replace the entire current §3 (lines 649–757 in Draft-June.tex,
`\section{Calibration Strategy}` through the end of
`\subsection{Demographic and Type Inputs}`) with a new section structured
around the actual scaffold Diego built.

**Section heading:** `\section{Calibration}` (drop "Strategy" — the section
is no longer a plan; it is the calibration as executed, with a placeholder
for the post-SMM numbers).

**Subsection structure:**

1. **Overview** (no subsection header, opens the section). Three paragraphs.
   - Paragraph 1: organize parameters into three blocks — (A) externally
     fixed (γ, ν_ℓ, α, δ, A and the AR(1) parameters ρ, σ_ε); (B) first-step
     externally estimated (sex-specific survival via Probit, sex-by-age
     wage profiles via OLS, age-varying health depreciation δ^h_j via the
     two-pass scheme); (C) SMM-estimated (Ψ, Ξ, ξ, β, H̄_0, h^slope, ζ_h —
     seven parameters, but in the current scaffold the active SMM block
     estimates six: Ψ, Ξ, ξ, H̄_0, h^slope, ζ_h, with β externally pinned
     to hit K/Y = 3.0).
   - Paragraph 2: state the two-step strategy following Gourinchas–Parker
     (2002). Reference the partial-equilibrium identification of Block A
     parameters; the GE-internal identification of Block C via SMM.
   - Paragraph 3: **flexibility caveat.** State explicitly that the current
     draft reports the calibration *protocol* in full and *placeholder
     numerical values* for parameters that depend on data inputs being
     finalized by Judy (income, ENIGH-derived) and Milo (mortality,
     CONAPO–UISP life table) within the remaining calibration window.
     "Final SMM estimates and standard errors will be reported in the
     post-seminar revision; the qualitative results of the paper —
     baseline equilibrium magnitudes, policy counterfactual signs, and
     the comparative-steady-state findings of Section 7 — do not depend
     on parameter values within the literature-anchored ranges."

2. **`\subsection{First-Step Calibration}`**. Three subsubsections,
   following the existing Draft-June structure but tightened.

   - **`\subsubsection{Mortality}`** — keep the Probit specification
     already in Draft-June (lines 660–672); confirm that survival is
     recovered via $\psi^g_{j+1}(h') = 1 - \Phi(X(j,g,h')'\hat\gamma_{\rm m})$.
     Add one sentence noting that the Probit is estimated separately on
     three datasets (ENASEM for Mexico, CRELES for Costa Rica, and the
     Panamanian Encuesta de Hogares) with sex interactions.

   - **`\subsubsection{Labor Productivity}`** — keep the log-wage
     decomposition (lines 674–684). Add one sentence on the AR(1)
     estimation of $(\rho, \sigma_\varepsilon)$ via equally-weighted
     minimum distance on the residual variance-covariance matrix.

   - **`\subsubsection{Health Depreciation}`** — keep the two-pass scheme
     (lines 685–694). No edits.

3. **`\subsection{Second-Step Calibration: SMM}`**. Restructure to match
   `run_calibration.jl`:

   - **`\subsubsection{Estimated Parameters}`**. State the six SMM
     parameters: $(\Psi, \Xi, \xi, \overline{H}_0, h^{\rm slope}, \zeta_h)$.
     Note that $\beta$ is calibrated outside the SMM loop to target an
     aggregate capital-output ratio of 3.0 (this is the externally
     anchored seventh parameter that the existing Draft-June lumped with
     the SMM block).

   - **`\subsubsection{Targeted Moments}`**. Six target moments. Render
     as a LaTeX table with three columns: Parameter, Targeted Moment,
     Source. Use the following content (verify against
     `run_calibration.jl` and the moment names in `Calibration/src/moments.jl`
     if accessible; if not, use the list below and footnote that the
     final moment specification follows the scaffold):

     | Parameter | Targeted Moment | Source |
     |---|---|---|
     | $\Psi$ | average hours of prime-age formal men $= 1/3$ of time endowment | ENOE 2022, weekly hours / 168 |
     | $\Xi$ | value of a statistical life $= \$11.6$M (2022 USD, US-VSL) | US-DOT / EPA VSL guidance |
     | $\xi$ | income elasticity of medical spending, cross-sectional | \citet{hall_jones_2007}; ENASEM |
     | $\overline{H}_0$ | mean medical spending, age 25–35 cohort | ENASEM (Mexico), CRELES (CR), Panamá ENH |
     | $h^{\rm slope}$ | log-slope of mean medical spending with age, 25–75 | same as above |
     | $\zeta_h$ | cross-sectional income elasticity of $m$ within age bins | same as above |

     Add one sentence: "The system has six parameters and six moments and
     is therefore exactly identified."

   - **`\subsubsection{SMM Procedure}`**. Three paragraphs.
     - Paragraph 1: the quadratic objective with diagonal $W$ weighted
       by inverse squared standard errors of the data moments. The
       equation (label `eq:smm_objective`):
       $\widehat\Theta_{\rm SMM} = \arg\min_\Theta [m^{\rm sim}(\Theta) - m^{\rm dat}]' W [m^{\rm sim}(\Theta) - m^{\rm dat}]$.
     - Paragraph 2: the inner-outer structure. Inner solve: at each
       candidate $\Theta$, the model is solved as a full stationary GE
       (Definition 1); inner loop iterates on $(r, w, \tau^p)$ until
       factor and pension markets clear. Outer optimizer: multi-start
       Nelder–Mead simplex (8 starts × ≤50 iterations each per scaffold
       default), with convergence declared when the simplex diameter falls
       below $10^{-5}$ and the moment-distance gradient (computed by
       finite differences) has norm below $10^{-4}$.
     - Paragraph 3: simulation discipline. State that simulated moments
       are computed by drawing $N_{\rm sim} = 50{,}000$ agents per
       $(g,\theta)$ from the ergodic distribution of $\eta$ and from the
       stationary cohort weights $\phi^g_j(\theta)$, then propagating
       each panel forward through the policy functions. Standard errors
       on $\widehat\Theta_{\rm SMM}$ are computed by the asymptotic
       sandwich formula using a numerical Jacobian of $m^{\rm sim}$ at
       $\widehat\Theta$.

   - **`\subsubsection{Verification Protocol}`**. New, important. State
     that the scaffold supports four execution modes (briefly: smoke,
     parity, jacobian, multistart) and that — prior to the multi-start
     calibration — a parity test verifies that the SMM-scaffold PE solver
     reproduces the production `Household-Gender` solver to machine
     precision (gate: max absolute cohort-mean difference ≤ $10^{-10}$).
     This ensures that any moment values reported in the post-SMM revision
     come from a solver algorithm-identical to the GE solver used for the
     policy experiments. One short paragraph.

4. **`\subsection{Demographic and Type Inputs}`**. Keep verbatim from
   Draft-June (lines 753–757). Five-year periods, $J = 17$, $j_R = 10$,
   asymmetric birth shares $\pi^{m,\theta_H}_1 > \pi^{f,\theta_H}_1$ for
   all three countries, initial health $h_0 = \bar h$.

5. **`\subsection{Current Calibration Status}`** (new last subsection,
   one paragraph, conditional on partial calibration). This is the
   flexibility hinge. Write it so that the *same paragraph* works
   whether the calibration is partial or complete by Sunday:

   > "At the time of writing, the first-step regressions for sex-specific
   > mortality (Mexico, ENASEM) and the labor-productivity decomposition
   > (Mexico, ENOE) are in finalization. The second-step SMM block has
   > been verified end-to-end at literature-anchored starting values
   > (smoke test passes, parity with the production GE solver verified
   > to $7 \times 10^{-11}$). The numerical values reported in
   > Section [Baseline Equilibrium] and Section 7 reflect the calibration
   > at these starting values, which fall within the standard ranges
   > established in the OLG-health literature. Final SMM estimates,
   > standard errors, and country-specific calibrations for Costa Rica
   > and Panamá will be reported in the post-seminar revision following
   > completion of the data preparation by [Judith Méndez and Hermilo
   > Cortés] and execution of the multi-start optimization."

   This paragraph can be hand-edited on Saturday or Sunday to swap
   "starting values" for "estimated values" and the numbers it implies,
   depending on whether SMM has been run.

### 3.2 Cost of Inaction — new Section 7 (insert)

Insertion point: immediately after `\section{Policy Counterfactuals}`
ends (currently line 1117 in Draft-June.tex, right before
`\section{Formalization Experiment}`).

**Section heading:** `\section{Cost of Inaction: Comparative Steady State
under 2050 Demographics}` with label `\label{sec:aging}`.

**Subsection structure:**

1. **Section opener** (no subsection header). Three to four paragraphs.

   - Paragraph 1: framing. The policy counterfactuals of Section 6 hold
     demographics fixed at the 2020 calibration and vary policy. The
     reverse exercise — holding policy at the calibrated 2020 baseline
     and varying demographics to the 2050 projected structure — gives
     the *cost of inaction*: the equilibrium the economy converges to
     when the demographic transition is fully internalized but no policy
     adjusts. This is a long-run incidence statement, not a transition
     path; the within-transition incidence on cohorts alive in 2020 is
     left to future work.

   - Paragraph 2: the demographic shift. Cite UN WPP 2024 medium-variant
     projection. Mexico life expectancy at birth rises from 75.1 (2023)
     to a projected 79.8 by 2050; the sex gap narrows modestly from
     6.1 to 5.6 years. Total fertility rate falls toward 1.7, implying
     a contracting entering cohort. The 5-year-period $n_p$ shifts from
     $+5.10\%$ (1% annual) to $-1.98\%$ (−0.4% annual). The sex-specific
     survival schedules used are derived from the 2020 baseline via a
     one-parameter Brass-logit shift calibrated separately for males and
     females to hit the WPP-projected life-expectancy targets;
     methodology and provenance documented in Appendix [add
     `\label{app:demog2050}`]. The resulting stationary dependency ratio
     under the new demographic structure is 0.74, exactly 2.0× the
     baseline value of 0.37, consistent with ECLAC's claim that old-age
     dependency at least doubles in Mexico, Costa Rica, and Panamá by
     2045 \citep{ECLAC2022}.

   - Paragraph 3: the experimental design. Three stationary equilibria
     under 2050 demographics, differing only in fiscal closure:
     (i) RUN 1 — the 2020 baseline, joint closure ($\tau^p$ clears PAYG
     and $B$ residually closes the general budget); (ii) C1 — 2050
     demographics, same joint closure; (iii) C2 — 2050 demographics with
     $\tau^p$ pinned at the 2020 calibrated rate, with pension benefits
     scaling to maintain PAYG balance ($\text{pen} = \tau^p \cdot wL / N^R$).
     The disentanglement — endogenous $\tau^p$ versus pinned $\tau^p$ —
     isolates the contribution-rate channel of demographic adjustment from
     the benefit-side response.

   - Paragraph 4: forward-looking sentence. "A third closure (C3) in
     which general taxation absorbs the pension shortfall under a pinned
     $\tau^p$ is the natural complement to C1 and C2 but is left to the
     September three-country deliverable. As Section 7.3 documents, a
     fourth closure considered — pinning both $\tau^p$ and pension
     benefits while letting government debt absorb the pension shortfall
     — fails to admit a finite stationary equilibrium and serves as the
     paper's structural motivation for studying the feasible policy menu
     under demographic pressure."

2. **`\subsection{Aggregate Results}`**. One paragraph + one table.

   The table (label `tab:aging_comparison`) — five rows, four numeric
   columns (RUN 1, C1, C2, plus a "change C1 vs RUN 1" column or a
   percentage-change interpretation column). Source the numbers from
   `aging_comparison_gap.csv` and §2 of the session log:

   | | RUN 1 (2020) | C1 (2050, joint) | C2 (2050, $\tau^p$ pinned) |
   |---|---|---|---|
   | $K$ | 14.378 | 21.035 | 27.703 |
   | $L$ | 15.870 | 20.388 | 22.629 |
   | $Y$ | 26.300 | 35.300 | 38.942 |
   | $r$ (annual) | 4.81\% | 3.98\% | 2.96\% |
   | $w$ | 0.988 | $\approx 0.989$ | 1.101 |
   | $\tau^p$ | 14.50\% | \textbf{26.38\%} | 14.50\% (pinned) |
   | pen | 1.064 | (endog) | (scaled) |
   | $B/Y$ | 28.30\% | 22.86\% | 25.32\% |
   | $N^R/N^W$ | 0.290 | 0.540 | 0.515 |

   Notes block under the table: $N^R/N^W$ is the model dependency ratio
   (age 65+ over age 20–64); 2050 demographics from a Brass-logit shift
   of the 2020 baseline anchored to UN WPP 2024 medium-variant projections
   (Appendix \ref{app:demog2050}). Pen and $\tau^p$ at 5-year period frequency.

   The accompanying paragraph (one paragraph, four sentences max):

   - Aging nearly doubles the equilibrium pension contribution rate
     when policy lets $\tau^p$ clear PAYG (14.5\% → 26.4\%), a direct
     consequence of the dependency-ratio doubling and the PAYG-balance
     condition $\tau^p = \kappa \cdot N^R/N^W$.
   - Capital accumulates substantially under both 2050 closures
     ($K$ rises 46\% in C1, 93\% in C2), reflecting the strengthened
     precautionary saving motive at longer life expectancy.
   - The fall in $B/Y$ from 28.3\% to 22.9\% under C1 may appear
     counterintuitive but reflects the model's general-equilibrium
     logic: the higher $\tau^p$ absorbs the pension shock, capital
     accumulation lifts the capital-income tax base, and the residual
     general government budget loosens.
   - Under C2, where benefits adjust rather than contributions, the
     precautionary saving response is stronger still, and the wage
     rises by 11\%.

3. **`\subsection{Welfare Incidence by Sex and Skill}`**. One paragraph
   + one table + one figure reference.

   Welfare table (label `tab:welfare_aging`) from §2 of the session log:

   | $\mathcal{W}_1(g, \theta)$ | M, $\theta_L$ | M, $\theta_H$ | F, $\theta_L$ | F, $\theta_H$ |
   |---|---|---|---|---|
   | RUN 1 (2020) | 3.482 | 4.143 | 3.321 | 3.965 |
   | C1 (2050, joint) | 3.203 | 3.828 | 3.208 | 3.827 |
   | C2 (2050, pinned) | 3.287 | 3.999 | 3.168 | 3.879 |

   Footnote on the table: "Welfare values for RUN 1 and C1 come from a
   focused-recovery solver that re-solves the household problem at the
   converged equilibrium prices with $\tau^p$ and pen consolidated via a
   three-iteration inner loop; full-GE replication is reserved for the
   post-seminar revision. C2 welfare comes from a dedicated standalone
   solver and is bit-precise. The qualitative welfare ordering across
   types is robust to the precision distinction."

   Figure reference (label `fig:welfare_panel`):
   `\includegraphics[width=0.85\textwidth]{welfare_panel_gap.png}` with
   caption "Lifetime welfare at birth $\mathcal{W}_1(g, \theta)$ across
   the three reportable equilibria. Sex-by-skill panel; the closing
   sex gap under 2050 demographics (compared to the 2020 baseline) is
   the qualitative finding of this experiment."

   The accompanying paragraph (one paragraph, four sentences max):

   - Three substantive findings. First, all four types are made worse
     off by demographic aging under unchanged policy.
   - Second, C2 is welfare-superior to C1 for high-skill types of both
     sexes, while C2 is welfare-inferior to C1 for low-skill women, who
     have less ability to self-insure via savings and bear more of the
     benefit cut than they gain from higher capital income.
   - Third — and this is the gender-extension finding — the sex gap in
     lifetime welfare *closes* under 2050 demographics: from roughly 5\%
     (men above women at each skill in RUN 1) to near-zero in C1, because
     the higher $\tau^p$ disproportionately erodes the productive-male
     labor wedge.
   - The magnitudes of the sex gap depend on the current sex-asymmetry
     stubs ($e^F = 0.85 \cdot e^M$ and a 25\% female-mortality uplift)
     and will be refined in the September deliverable using sex-specific
     WPP-2024 calibrated primitives; the *closing direction* of the gap
     is robust to the calibration.

4. **`\subsection{The Feasible Policy Menu: Non-Existence under Debt-Financed
   Inaction}`** (label `subsec:c2_infeasibility`). This is the C2 interp-1
   result and the conceptual hinge of the paper. Three paragraphs + one
   figure.

   - Paragraph 1: motivation. State the alternative interpretation of C2
     considered: pension benefits remain at the calibrated PAYG formula
     ($\text{pen} = \kappa \cdot wL / N^W$), $\tau^p$ is pinned at the
     2020 rate, and the resulting PAYG deficit is absorbed by general
     government debt. Economically, this is the "do nothing on the
     pension side; finance the demographic shock with debt" scenario.

   - Paragraph 2: the result. Under this closure, the model's outer GE
     loop does not converge to a finite stationary equilibrium under
     Mexico's 2050 calibration. Reference Figure \ref{fig:c2_crash} and
     describe the mechanism: the pension deficit pushes the primary
     deficit deep negative, the stationary-debt equation
     $B = \text{primary} / (r^n - n_p)$ drives $B$ to large negative
     values, the implied capital target $K = A_{\rm dom} - B$ explodes
     upward, the marginal product of capital falls, $r^n$ crosses $n_p$
     from above (visible in the figure at iteration 8), and the
     stationary-debt equation becomes ill-conditioned. Beyond that point
     the iteration oscillates without convergence.

   - Paragraph 3: economic interpretation and stake. This is not a
     numerical artifact. The model is telling us that, at Mexico's
     projected 2050 demographic structure, the 2020 contribution rate
     combined with the 2020 benefit formula generates a pension
     financing gap that cannot be financed by a finite stationary stock
     of government debt. Something must adjust — $\tau^p$ (C1), pension
     benefits (the C2 column reported above), or general taxation (C3,
     left to future work). The *menu of feasible long-run policy
     responses to demographic aging in Latin America is narrower than
     commonly assumed*: pure debt-financing of the pension shortfall is
     structurally off the table.

   Figure (label `fig:c2_crash`):
   `\includegraphics[width=\textwidth]{c2_interp1_crash_panel.png}` with
   caption "Failure to admit a finite stationary equilibrium under the
   debt-financed-inaction closure (C2, interpretation 1). Left panel:
   trajectory of aggregate capital across outer GE iterations; capital
   explodes at iteration 8. Middle panel: net interest rate $r^n$ and
   population growth rate $n_p$ across iterations; $r^n - n_p$ crosses
   zero at iteration 8, the point at which the stationary-debt equation
   becomes ill-conditioned. Right panel: goods-market residual DIFF/Y
   across iterations, showing oscillation without convergence."

5. **`\subsection{Caveats and Forward Plan}`** (label `subsec:aging_caveats`).
   Short — one paragraph. Bullet structure inside the paragraph rather
   than `itemize` to keep formal voice. Cover: (a) sex-asymmetry stubs;
   (b) the focused-recovery vs full-GE precision distinction for the
   welfare values; (c) the absence of the C3 column; (d) the absence of
   a within-transition incidence analysis. State that all four are
   addressed in the September three-country deliverable.

### 3.3 Introduction edit

After the existing paragraph at line 131 (the one ending "the analytical
center of this paper"), insert one new paragraph:

> "This paper's contribution is empirical and structural. Empirically,
> we calibrate the model to Mexico and report three quantitative findings.
> First, under the projected 2050 demographic structure, the equilibrium
> pension contribution rate roughly doubles under unchanged policy, from
> 14.5\% to 26.4\%. Second, the welfare incidence of this demographic
> shock falls asymmetrically by skill, with the sex gap in lifetime
> welfare closing under aging — a result driven by the sex-asymmetric
> erosion of the labor-tax wedge that the higher $\tau^p$ implies.
> Third, and structurally: the 2020 contribution rate combined with the
> 2020 benefit formula generates a pension financing gap at 2050
> demographics that *cannot be financed by a finite stationary stock of
> government debt*. The menu of feasible long-run policy responses to
> demographic aging in Latin America is structurally narrower than
> commonly assumed."

### 3.4 Section numbering check

Once the new Section 7 is inserted, what was Section 7 (Formalization
Experiment) becomes Section 8, and Conclusion becomes Section 9. LaTeX
handles this via `\section{}` ordering automatically. Audit:

1. Search Draft-June.tex for any literal "Section 6", "Section 7",
   "Section 8" in body text. Update to reflect new numbering.
2. Search for `\ref{sec:`, `\ref{subsec:`, `\ref{eq:` references; LaTeX
   resolves these automatically but eyeball the resolved numbers in the
   compiled output.

---

## 4. New appendix material

Add one new appendix subsection before the existing
`\section{Supplementary Tables and Data}` (label `app:supplementary`):

**`\section{2050 Demographic Inputs: Derivation and Sources}`**
(label `app:demog2050`).

Three paragraphs:

- **Source.** UN WPP 2024 revision, online edition, accessed 2026-05-24.
  Mexico medium-variant projections used throughout. Aggregate anchors:
  life expectancy at birth in 2050 of 79.8 years (sex gap 5.6 years,
  implying male LE 77.0, female LE 82.6); total fertility rate 1.70;
  total population peaks near 2042 at 152M, declining to 150.6M by 2050.
  2020 baseline reference: PAHO 2024, Mexico LE 2023 (total 75.1, male
  72.1, female 78.3).

- **Method.** The aggregate WPP targets do not directly fix the 17-band
  survival schedule by sex required by the model. A one-parameter Brass
  logit shift is applied to the 2020 baseline pooled survival schedule:
  $\text{logit}(1 - p_{2050,g,j}) = \alpha_g + \text{logit}(1 - p_{2020,j})$,
  with $\alpha_g$ chosen separately for males ($\alpha_m = -0.158$) and
  females ($\alpha_f = -0.696$) to hit the sex-specific WPP life-expectancy
  targets. The population growth rate $n_p$ is set to $-0.4\%$ annual
  (a 5-year period rate of $-1.98\%$), consistent with the implied
  entering-cohort contraction under WPP 2024 TFR. Together with the
  Brass-shifted survival schedules, this yields a stationary dependency
  ratio of 0.74, exactly twice the baseline, matching the ECLAC anchor
  for Mexico by 2045 \citep{ECLAC2022}.

- **Caveat.** The Brass shift preserves the shape of age-conditional
  mortality and adjusts the level via a single parameter. It cannot
  capture compositional changes in mortality such as disproportionate
  gains at older ages from chronic-disease management. For the
  comparative-steady-state purpose pursued here this is adequate; for the
  September three-country deliverable the placeholder is replaced with
  WPP single-age life tables aggregated to 5-year bands, and the gender
  decomposition is re-run on calibrated rather than stub primitives.

---

## 5. Build and verification

After producing `Draft-June-v2.tex`:

1. **LaTeX compile check.** Run `pdflatex Draft-June-v2.tex` twice and
   `bibtex Draft-June-v2` once in between (standard order for
   cross-references and bibliography). The output must compile without
   errors. Warnings about overfull boxes or missing references should be
   inspected but not necessarily fixed.

2. **Figure file presence.** Confirm that `welfare_panel_gap.png` and
   `c2_interp1_crash_panel.png` are in the Overleaf project root or in
   a subdirectory whose path is set via `\graphicspath{}`. If the figures
   are not in the project, add a `% TODO: upload [filename] to Overleaf`
   comment at the `\includegraphics` line so Héctor can resolve it in
   one pass.

3. **Cross-reference audit.** Compile, then `grep "??" Draft-June-v2.log`
   to catch unresolved `\ref` and `\cite`. Resolve each.

4. **Word count delta.** Report the rough word count of the new material
   (Sections 5 [rewritten] and 7 [new], Introduction paragraph, Appendix
   subsection) so Héctor can budget whether to tighten.

5. **No edits to `Draft-June.tex`.** The original stays untouched. If
   Héctor wants to swap v2 for v1, that's a single file rename, not a
   diff-and-merge operation. Safety first.

---

## 6. What this draft is and is not

**Is:** A self-contained seminar paper draft that integrates the
aging-experiment results, presents the C2 interp-1 infeasibility as the
paper's structural motivation, and flexibly accommodates either a partial
or complete calibration depending on what Judy and Milo deliver before
Sunday.

**Is not:** The submission version. The post-seminar revision will
include: final SMM estimates with standard errors; full-GE-precision
welfare values for RUN 1 and C1; the C3 closure (general-taxation
absorbs); Costa Rica and Panamá calibrations and comparative results; a
within-transition incidence analysis; sex-specific WPP-calibrated
primitives replacing the current stubs.

**Production cadence:** Sunday draft complete → Monday/Tuesday slide
prep → Thursday seminar.

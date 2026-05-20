# BID 2 — June Seminar Draft: Results, Experiments, Calibration
**Mission BID 2 · Spending Smarter under Demographic Pressure**
*Instructions for Claude Code — Prepare Sections for June 5 IDB Seminar*

---

## Context

You have:

| File | Description |
|------|-------------|
| `Integrated_5_.tex` | Current working LaTeX file (source of truth) |
| `references.bib` | Bibliography |
| `ge_model.jl` | Self-contained GE solver (Diego's code — fully verified, converges in 13 iters) |
| `ge_lifecycle.csv` | Mass-weighted lifecycle profiles by age and skill type |
| `ge_summary.csv` | Aggregate equilibrium values |
| `ge_history.csv` | GE iteration history |
| `ge_run.log` / `ge_run_fast.log` | Convergence logs with full equilibrium printout |
| `household_problem.jl` | PE household solver (verified, 30 log-spaced m-grid points) |
| `household_lifecycle.csv` | PE lifecycle profiles |
| `JUNE_SEMINAR_BID2.md` | This file |

**Hardware (Dalila):** Intel Core Ultra 9 285H (16 cores), NVIDIA GPU with CUDA. Run Julia with `julia --project=. --threads=auto`.

---

## Objective

Produce three new LaTeX sections to be inserted into `Integrated_5_.tex`, plus run `ge_model.jl` with two policy experiments. The output is a single file: **`Integrated_6_seminar.tex`**.

**Do not rewrite Sections 1–4 (Introduction, Literature Review, Model, Calibration Strategy) or the Data section.** This pass adds content after the existing sections.

---

## Part 1: Baseline Results Section (Fehr-Kindermann Style)

### 1.1 What to produce

A new section titled **"Baseline Equilibrium"** (`\section{Baseline Equilibrium}\label{sec:baseline}`) inserted after the current Data section (Section 5) and before the Policy Counterfactuals section (Section 6).

### 1.2 Style guidance — Fehr & Kindermann (2018)

The Fehr-Kindermann textbook presents OLG model results in a specific, clean format:

1. **A social accounts table** showing macro aggregates: $K$, $Y$, $C$, $I$, $G$, factor prices ($r$, $w$), tax rates, and pension variables. Two columns: level and share of $Y$. This is the "equilibrium snapshot."

2. **Lifecycle profile figures** (6-panel layout): consumption, labor supply, earnings, assets, health stock, and surviving mass — all plotted by age, with separate lines for each agent type ($\theta_L$, $\theta_H$).

3. **Interpretive text** that reads the table and figures: what the model produces, why, and what it implies for the paper's questions. This is not a data dump — it is an analytical reading of the equilibrium.

### 1.3 Data source

All numbers come from the GE run. The key values from `ge_run.log`:

```
K        = 15.237
L        = 17.604
Y        = 26.740
K/Y (5y) = 0.570   |  K/Y annual = 0.114
r annual = 5.10%
w        = 0.972
C/Y      = 48.72%
M/Y      = 4.82%
G/Y      = 19.00%
δK/Y     = 19.89%
Λ_void/Y = 4.66%
τp       = 13.81%
pen      = 1.163
N^R/N^W  = 0.276
B (debt) = 7.355
A_dom    = 22.592
```

Lifecycle profiles come from `ge_lifecycle.csv`. Read the CSV and extract the values.

### 1.4 LaTeX structure

```latex
\section{Baseline Equilibrium}
\label{sec:baseline}

[Opening paragraph: the model is solved as a stationary competitive
equilibrium. This section presents the baseline results under the
parameter values documented in Section~\ref{sec:calibration} and the
data sources in Section~\ref{sec:data}. The baseline uses the Mexican
demographic structure and fiscal parameters.]

\subsection{Aggregate Equilibrium}
\label{subsec:agg_eq}

[Table 6: Social Accounts — Fehr-Kindermann style. Two-column format:
Level and (% of Y). Blocks: CAPITAL (K, A, B), PRODUCTION (Y, C, M,
δK, G, Λ_void), LABOR (L, w, r), FISCAL (τc, τw, τk, τm, τp),
PENSION (pen, N^R, N^W, N^R/N^W).]

[Interpretive text: K/Y annual = 11.4% — low by OECD standards,
reflecting the compressed capital accumulation of a young, rapidly
aging population. M/Y = 4.82% — within the 2–8% LAC range.
τp = 13.81% — the endogenous pension contribution rate, driven by
N^R/N^W = 0.276. The annual interest rate of 5.1% is above the
population growth rate (1% annual), confirming dynamic efficiency.]

\subsection{Lifecycle Profiles}
\label{subsec:lifecycle}

[Figure 1: 6-panel lifecycle profiles. Use the plots already generated
by ge_model.jl (in ./plots/ge_01_lifecycle.png) or regenerate from
ge_lifecycle.csv. Panels: consumption, labor, assets, medical spending,
health stock, surviving mass. Two lines per panel: θ_L (blue) and
θ_H (red). X-axis: age 20–100.]

[Interpretive text for each panel:]

[Consumption: θ_H agents consume approximately 60% more than θ_L at
peak (age 60). The retirement drop at age 65 is the GHH composite
effect — z = c + s(h) − v(ℓ) is smooth across retirement, but c
drops when v(ℓ) disappears. This is not a bug; it is the correct
GHH lifecycle profile.]

[Labor: Both types work approximately 1/3 of available time (matching
the Ψ = 14.0 calibration target). θ_H works slightly more — higher
productivity makes the labor-leisure margin more favorable. Labor is
zero from age 65 onward.]

[Assets: Hump-shaped. θ_H peak assets approximately 65% higher than
θ_L. The accumulation phase (20–60) reflects the lifecycle savings
motive amplified by the longevity channel: healthier agents who expect
to live longer save more.]

[Medical spending: Hump-shaped with a peak at ages 60–75. θ_L agents
invest more in health at older ages relative to their resources —
they face steeper health depreciation (ϱ_L > ϱ_H). θ_H agents invest
less because their health depreciates more slowly.]

[Health stock: Both types start at h = 1.0. θ_L health declines
faster — reaching approximately 0.25 by age 95. θ_H maintains health
above 0.50 until age 80. The 20-year gap in healthy longevity between
skill groups documented in the introduction is reproduced endogenously
by the model.]

[Surviving mass: Nearly identical for both types until age 60, then
diverges. By age 95, approximately 5% of θ_L newborns survive versus
approximately 10% of θ_H. The survival differential is driven entirely
by the health stock differential — both types face the same ψ_base
schedule, but health-conditional survival rewards higher h.]

\subsection{The Fiscal Amplification Loop}
\label{subsec:fiscal_loop}

[Interpretive paragraph connecting the lifecycle profiles to the
paper's central mechanism. The endogenous τp = 13.81% is the outcome
of the dependency ratio N^R/N^W = 0.276 under κ = 0.50. As
demographic aging raises N^R/N^W, τp rises mechanically. Health
investment partially offsets this by extending productive working
lives (raising N^W) and by improving labor productivity (raising wL).
But healthier workers who survive into retirement also raise N^R.
The net effect in the baseline is a τp that is 13.81% — the
quantitative resolution of the ambiguity identified in the
introduction.]
```

### 1.5 Figures

If the plots from `ge_model.jl` are available in `./plots/ge_01_lifecycle.png`, copy them to the LaTeX project directory and include via `\includegraphics`. If not available, generate them by running:

```bash
julia --project=. --threads=auto ge_model.jl
```

This produces `./plots/ge_01_lifecycle.png` through `ge_06_euler_residuals.png`.

Include in the LaTeX:
- Figure 1: `ge_01_lifecycle.png` (6-panel lifecycle profiles)
- Figure 2: `ge_03_aggregate_identity.png` (goods market decomposition bar chart)
- Figure 3: `ge_06_euler_residuals.png` (Euler residual diagnostic — in appendix)

---

## Part 2: Two Policy Experiments

### 2.1 What to produce

A new section titled **"Policy Experiments"** (`\section{Policy Experiments}\label{sec:experiments}`) inserted after the Baseline Equilibrium section.

### 2.2 Experiment 1: Pension Reform — Reduce κ from 0.50 to 0.30

**Rationale:** This is the most natural first experiment and directly addresses the reviewer's question about pension levers. Reducing the replacement rate lowers pension generosity, which reduces τp, eases the fiscal wedge, and stimulates savings. The question is: by how much, and what are the welfare consequences?

**Implementation:** In `ge_model.jl`, change line 43:
```julia
const κ_rep = 0.30    # was 0.50
```

Run the model. Save output as `ge_summary_kappa30.csv`, `ge_lifecycle_kappa30.csv`, `ge_run_kappa30.log`.

**Report in the LaTeX:**
- Table 7: Side-by-side comparison of baseline (κ=0.50) and reform (κ=0.30) aggregates
- Key variables to highlight: Δτp, Δr, Δw, ΔK/Y, ΔC/Y, ΔM/Y, Δpen
- Figure 4: Overlay of lifecycle consumption profiles (baseline vs reform) for both types
- Interpretive text: the pension reform reduces τp by approximately [X] percentage points, raises the after-tax wage (stimulating labor supply at the margin under GHH), and increases capital accumulation through the lifecycle savings channel. The welfare effect is measured by the CEV at birth: 𝒲₁(θ_L) and 𝒲₁(θ_H) under the reform versus baseline.

### 2.3 Experiment 2: Health Subsidy — Set τ^m = −0.20

**Rationale:** This is the paper's signature policy instrument — the health subsidy that operates through the four-channel mechanism (productivity, utility, survival, resource cost) described in Section 6 of the draft. A 20% subsidy reduces the effective price of health investment, raising m, improving h, and activating the fiscal amplification loop.

**Implementation:** In `ge_model.jl`, change line 41:
```julia
const τm = -0.20    # was 0.00
```

Keep κ_rep = 0.50 (baseline pension). Run the model. Save output as `ge_summary_taum20.csv`, `ge_lifecycle_taum20.csv`, `ge_run_taum20.log`.

**Report in the LaTeX:**
- Table 8: Side-by-side comparison of baseline (τm=0) and subsidy (τm=−0.20) aggregates
- Key variables to highlight: ΔM/Y (health spending should increase), Δh̄ (average health should improve), Δτp (the ambiguous fiscal effect — does healthier population lower or raise τp?), Δr, Δw, ΔB/Y
- Figure 5: Overlay of health stock profiles (baseline vs subsidy) for both types
- Figure 6: Overlay of medical spending profiles (baseline vs subsidy) for both types
- Interpretive text: the health subsidy raises M/Y from [X]% to [Y]%, improves average health by [Z] percentage points at age 60, and [raises/lowers] τp by [W] percentage points — confirming that the fiscal amplification loop produces a [positive/negative/ambiguous] net effect. The productivity channel dominates/is offset by the survival channel.

### 2.4 Running the experiments

For each experiment:
1. Modify the relevant parameter in `ge_model.jl` (or better: create `ge_model_kappa30.jl` and `ge_model_taum20.jl` as copies with the single parameter change)
2. Run: `julia --project=. --threads=auto ge_model_kappa30.jl > ge_run_kappa30.log 2>&1`
3. Copy the output CSVs and plots to the LaTeX project directory
4. Build the comparison tables and figures

### 2.5 LaTeX structure for the experiments section

```latex
\section{Policy Experiments}
\label{sec:experiments}

[Opening paragraph: We present two policy experiments that illustrate
the model's capacity to evaluate reforms along the two principal
margins — pension generosity and health investment incentives. Both
experiments compare a reformed stationary equilibrium against the
baseline documented in Section~\ref{sec:baseline}. Welfare is measured
by the consumption-equivalent variation at birth, 𝒲₁(θ), defined in
the model section.]

\subsection{Experiment 1: Pension Reform ($\kappa$: 0.50 $\to$ 0.30)}
\label{subsec:exp_kappa}

[Table 7 + Figure 4 + interpretive text as described above]

\subsection{Experiment 2: Health Subsidy ($\tau^m$: 0 $\to$ $-0.20$)}
\label{subsec:exp_taum}

[Table 8 + Figures 5–6 + interpretive text as described above]

\subsection{Discussion}
\label{subsec:exp_discussion}

[Closing paragraph comparing the two experiments. Which produces
larger welfare gains? Which is more fiscally sustainable? Does the
pension reform or the health subsidy do more to compress the
inequality between θ_L and θ_H? This paragraph connects back to
the spending smarter principle from the introduction.]
```

---

## Part 3: Mexico Calibration Section

### 3.1 What to produce

Replace the current Calibration section (Section 4) content with a focused **Mexico-specific calibration** that maps every model parameter to a Mexican data source. This section should be concise — a calibration table plus brief justification for key choices.

### 3.2 LaTeX structure

```latex
\section{Calibration}
\label{sec:calibration}

[Opening paragraph: The model is calibrated to the Mexican economy.
Parameters are organized into three categories: (A) preference and
technology parameters drawn from standard public finance calibrations,
(B) health and demographic parameters calibrated to Mexican data, and
(C) fiscal parameters matching the Mexican tax and pension system.]

\subsection{Parameter Table}
\label{subsec:param_table}

[Table 9: Full parameter table. Three blocks:]

% Block A: Preferences and Technology
\begin{table}[H]
\centering
\caption{Model Parameters — Mexico Calibration}
\label{tab:calibration}
\begin{tabular}{llll}
\hline\hline
\textbf{Parameter} & \textbf{Symbol} & \textbf{Value} & \textbf{Source / Target} \\
\hline
\multicolumn{4}{l}{\textit{A. Preferences and Technology}} \\
Risk aversion          & $\gamma$    & 2.0        & Standard public finance \\
Inverse Frisch         & $\nu$       & 2.0        & FK (2018) \\
Discount factor (5-yr) & $\beta$     & $0.998^5$  & $r \approx 5\%$ annual \\
Labor disutility scale & $\Psi$      & 14.0       & Target $\bar\ell \approx 1/3$ \\
Capital share          & $\alpha$    & 0.36       & National accounts \\
Depreciation (annual)  & $\delta$    & 8.23\%     & PWT 10.01 \\
TFP                    & $A$         & 1.60       & Normalization \\
\hline
\multicolumn{4}{l}{\textit{B. Health and Demographics}} \\
Health amenity scale   & $\Xi$       & 0.50       & PE pass \\
Health amenity curv.   & $\xi$       & 0.50       & PE pass \\
Health prod. scale     & $H_{scale}$ & 0.30       & Target $M/Y \approx 5\%$ \\
Health prod. curv.     & $H_{curv}$  & 0.50       & Diminishing returns \\
Health depreciation    & $\delta^h_j$ & 0.02--0.70 & GBD 2021 / age-varying \\
Productivity penalty   & $\varrho$   & (0.30, 0.20) & GBD DALYs by skill \\
Skill types            & $\theta$    & (-0.20, 0.20) & ENOE wage premia \\
Initial health         & $h_0$       & 1.00       & Full health at age 20 \\
Survival base          & $\psi_j$    & Table B.3  & CONAPO / UISP 2019 \\
Population growth (ann.)& $n_p$      & 1\%        & CONAPO projections \\
AR(1) persistence      & $\rho$      & 0.98       & 5-yr frequency \\
AR(1) innovation s.d.  & $\sigma_\varepsilon$ & 0.05 & 5-yr frequency \\
\hline
\multicolumn{4}{l}{\textit{C. Fiscal Parameters — Mexico}} \\
Consumption tax        & $\tau^c$    & 16\%       & IVA rate \\
Labor income tax       & $\tau^\omega$ & 20\%     & Effective avg rate (OECD TW 2026) \\
Capital income tax     & $\tau^k$    & 20\%       & Effective avg rate \\
Medical spending tax   & $\tau^m$    & 0\%        & Baseline (policy instrument) \\
Gov spending / GDP     & $g_y$       & 19\%       & SHCP \\
Pension replacement    & $\kappa$    & 0.50       & IMSS stylized \\
\hline\hline
\end{tabular}
\end{table}

\subsection{Key Calibration Targets}
\label{subsec:targets}

[Brief text justifying the most important choices:]

[1. γ = 2.0: Standard in the public finance OLG literature
(Auerbach-Kotlikoff 1987, De Nardi et al. 2010). Under GHH
preferences with a health amenity, γ > 1 ensures that longer life
is welfare-improving, making health investment privately rational.
See Section~\ref{sec:baseline} for the resulting M/Y = 4.82%.]

[2. Ψ = 14.0: Calibrated in the PE household pass to produce
average labor supply ℓ ≈ 1/3 of available time, consistent with
Mexican labor force survey data (ENOE 2022: average weekly hours
≈ 43 out of a 60-hour potential).]

[3. H_scale = 0.30: Chosen to produce aggregate health expenditure
M/Y in the 4–6% range, matching Mexico's total health expenditure
as a share of GDP (WHO GHED 2024: 5.4% total, ~2.8% public).]

[4. δ^h_j schedule: Age-varying health depreciation rising from 2%
per 5-year period at age 20 to 70% at age 95. Calibrated to
reproduce the premature health crossing point documented in
Section 1: the proportion of the population in poor health crosses
50% at approximately age 60 in Mexico (GBD 2021).]

[5. τ^c = 16%, τ^ω = 20%, τ^k = 20%: Mexican IVA rate (16%) and
effective average rates from OECD Taxing Wages 2026. The tax wedge
(τ^ω + τ^p ≈ 34%) is within the range documented by the OECD for
Mexico.]
```

---

## Part 4: Structural Reorganization

The final section structure of `Integrated_6_seminar.tex` must be:

```
1  Introduction                           [keep as is]
2  Literature Review                      [keep as is]
3  Model                                  [keep as is]
4  Calibration                            [REWRITE per Part 3]
5  Data                                   [keep as is]
6  Baseline Equilibrium                   [NEW — Part 1]
7  Policy Experiments                     [NEW — Part 2]
8  Conclusion                             [keep as is]
   Appendix A: Fiscal Gap Methodology     [keep]
   Appendix B: Supplementary Tables       [keep]
```

Update the introduction roadmap paragraph (end of Section 1) to match:

```latex
The paper is structured as follows. Section~\ref{sec:lit} reviews the
relevant literature. Section~\ref{sec:model} presents the theoretical
framework. Section~\ref{sec:calibration} describes the calibration to
the Mexican economy. Section~\ref{sec:data} documents the data sources.
Section~\ref{sec:baseline} presents the baseline equilibrium.
Section~\ref{sec:experiments} reports two policy experiments---a
pension reform and a health subsidy. Section~\ref{sec:conclusion}
concludes.
```

---

## Part 5: Running the Model

### 5.1 Baseline (if not already run)

```bash
cd /path/to/project
julia --project=. --threads=auto ge_model.jl > ge_run.log 2>&1
```

Verify: `grep "CONVERGED" ge_run.log` should return a line. Check `ge_summary.csv` exists.

### 5.2 Experiment 1: κ = 0.30

```bash
# Create a copy
cp ge_model.jl ge_model_kappa30.jl
# Edit line 43: const κ_rep = 0.30
sed -i 's/const κ_rep.*=.*0.50/const κ_rep      = 0.30/' ge_model_kappa30.jl
# Also change output filenames to avoid overwriting:
sed -i 's/ge_lifecycle\.csv/ge_lifecycle_kappa30.csv/g' ge_model_kappa30.jl
sed -i 's/ge_summary\.csv/ge_summary_kappa30.csv/g' ge_model_kappa30.jl
sed -i 's/ge_history\.csv/ge_history_kappa30.csv/g' ge_model_kappa30.jl
sed -i 's|"plots"|"plots_kappa30"|g' ge_model_kappa30.jl
# Run
julia --project=. --threads=auto ge_model_kappa30.jl > ge_run_kappa30.log 2>&1
```

### 5.3 Experiment 2: τ^m = −0.20

```bash
cp ge_model.jl ge_model_taum20.jl
sed -i 's/const τm.*=.*0.00/const τm         = -0.20/' ge_model_taum20.jl
sed -i 's/ge_lifecycle\.csv/ge_lifecycle_taum20.csv/g' ge_model_taum20.jl
sed -i 's/ge_summary\.csv/ge_summary_taum20.csv/g' ge_model_taum20.jl
sed -i 's/ge_history\.csv/ge_history_taum20.csv/g' ge_model_taum20.jl
sed -i 's|"plots"|"plots_taum20"|g' ge_model_taum20.jl
julia --project=. --threads=auto ge_model_taum20.jl > ge_run_taum20.log 2>&1
```

### 5.4 Expected runtime

Each GE solve takes approximately 13 iterations. From the Phase 2 report, PE household solve takes ~7 minutes for the steady state. GE wraps this 13 times → ~90 minutes per experiment on 8 threads. With `--threads=auto` on 16 cores, expect ~45–60 minutes per run. Three runs (baseline + two experiments) → approximately 2.5–3 hours total.

---

## Part 6: Quality Checks

Before saving the final file, verify:

1. **Baseline table (Table 6):** All numbers match `ge_summary.csv` to 2 decimal places.
2. **Experiment tables (Tables 7–8):** Cross-check Δ columns: each Δ = reform − baseline.
3. **Figures:** All `\includegraphics` paths resolve. If plots are in subdirectories, ensure relative paths are correct.
4. **Cross-references:** `\ref{sec:baseline}`, `\ref{sec:experiments}`, `\ref{subsec:exp_kappa}`, `\ref{subsec:exp_taum}` all resolve.
5. **Introduction roadmap** updated to match new section numbering.
6. **No `\todo{}` in the new sections.** These are results — they should be definitive.
7. **Euler residual figure** (ge_06) goes in the appendix, not the main text.
8. **Compile test:** `pdflatex Integrated_6_seminar.tex` twice. Zero errors.

---

## Deliverables

| File | Description |
|------|-------------|
| `Integrated_6_seminar.tex` | Updated LaTeX with Sections 6–7 added, Section 4 rewritten |
| `ge_run_kappa30.log` | Convergence log for κ = 0.30 experiment |
| `ge_run_taum20.log` | Convergence log for τ^m = −0.20 experiment |
| `ge_summary_kappa30.csv` | Aggregate results for κ = 0.30 |
| `ge_summary_taum20.csv` | Aggregate results for τ^m = −0.20 |
| `ge_lifecycle_kappa30.csv` | Lifecycle profiles for κ = 0.30 |
| `ge_lifecycle_taum20.csv` | Lifecycle profiles for τ^m = −0.20 |
| Plots in `plots/`, `plots_kappa30/`, `plots_taum20/` | All diagnostic and lifecycle figures |

---

*Instructions prepared by Beth, Cath, Debb · BDH Core Team · May 2026*

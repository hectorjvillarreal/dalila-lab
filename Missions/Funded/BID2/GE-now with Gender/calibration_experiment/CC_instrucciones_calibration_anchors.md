# Claude Code Instructions — Representative Middle-Income Calibration Anchors

**Repository:** `Calibration/`
**Source files (read-only):** `Calibration/inputs/`, `Calibration/src/`,
`Calibration/run_calibration.jl`. **Inputs are placeholders to be replaced.**
**Deliverable:** A new directory `Calibration/inputs_anchored/` containing
the same CSV schema as `Calibration/inputs/` but populated with empirically
defensible values for an upper-middle-income country (Mexico-like profile),
sourced from the demographic-economics, health-economics, and labor-economics
literatures. A `provenance.md` documents every number's source.

**Purpose.** Replace the literal placeholder values currently in
`inputs/first_step/` and `inputs/moments/` with values that an applied
referee would recognize as reasonable for a middle-income economy, while
preserving the ability to substitute Judy and Milo's Mexican-data
deliverables when they arrive — partially or completely, file by file.

**Why this is not the real calibration.** Judy and Milo are estimating
first-step inputs (mortality Probit, wage decomposition, depreciation
schedule) and computing data-side moment targets from ENASEM, ENOE, and
GBD microdata. Their work will replace specific CSVs in
`Calibration/inputs/` when ready. This task creates a defensible
*intermediate* anchor — based on published literature, not on the Mexican
microdata — so the SMM scaffold can run with economically meaningful
inputs *now*, producing parameter estimates that are themselves
intermediate but defensibly grounded.

**Calendar.** Outputs needed within 24–48 hours so the SMM can run
overnight and feed §7 of the seminar paper.

---

## 1. What this task is, precisely

The Calibration scaffold has eleven input CSVs (six in `first_step/`,
one in `moments/`, four in `config/`). Of these:

- **Six are first-step inputs** that Judy and Milo will eventually
  replace with Mexican-data estimates: `e_age.csv`, `psi_base.csv`,
  `delta_h.csv`, `pi_birth.csv`, `skill_params.csv`, `ar1_params.csv`.
- **One is the moment targets**: `targets.csv` (6 moments with values
  and standard errors).
- **Four are configuration**: `pe_anchor.csv` (fixed PE prices),
  `theta_init.csv` (SMM starting values), `usd_scale.csv` (unit
  conversion), `grids.csv` (numerical settings).

This task produces a *parallel input directory* `inputs_anchored/`
with the same eleven files. The first-step inputs and moment targets
get representative values from the middle-income literature. The
configuration CSVs are *copied verbatim* — they are technical scaffold
settings, not empirical inputs.

The scaffold's `load_all_inputs(base_dir)` function (per the README,
§Open-follow-ups bullet "Country-specific runs") accepts an alternative
input directory. Running:

```bash
julia --project=. -t 4 Calibration/run_calibration.jl smoke --inputs=inputs_anchored
```

will use the new directory. **Verify this CLI flag exists before
relying on it; if not, the simplest workaround is to copy
`inputs_anchored/` over `inputs/` at run time and restore afterward.
The instructions below produce the CSVs in a parallel directory and
leave `inputs/` untouched.**

---

## 2. Operating principles

**Search the published literature.** For each parameter or target,
identify two or three published sources estimated on data from a
middle-income country (Mexico, Brazil, Colombia, Chile, Costa Rica,
Turkey, Argentina). When a Mexico-specific source exists, prefer it.
When it does not, prefer the modal value across the available
upper-middle-income evidence. Where the literature converges on a
range, take the median; where it diverges, document the range in
`provenance.md` and pick the value that is most consistent with the
model's structure.

**Defensibility over precision.** Every value in
`inputs_anchored/` must have a citation. A wrong-by-30% number with a
solid published anchor is *much* better than a hand-tuned number that
looks right. The referee will scrutinize sources, not magnitudes.

**Preserve the model's units.** The scaffold operates in
5-year-period units; the model is calibrated to ages 20–100 with
J=17 bands; consumption units are scaled to USD by `usd_per_unit_c`
in `usd_scale.csv`. Whatever values you pull from the literature
must be converted into the model's units before they enter the
CSVs. Document the conversion in `provenance.md`.

**Sex-asymmetric where the literature supports it; symmetric
otherwise.** The current stubs have `e^F = 0.85·e^M` and a 25%
female-mortality survival uplift — both ad hoc but with the right
sign. For the anchored inputs, use sex-specific values where the
literature reports them by sex (Mexican wage gap, sex-specific
life tables) and explicitly justify any continued use of symmetric
or scaled values.

**Hold lines on what is not calibrated here.** AR(1) parameters
(ρ, σ_ε) and skill parameters (θ_L, θ_H, ϱ(θ)) are first-step inputs
that *also* depend on Mexican microdata. Use literature anchors for
these and document them; do not attempt to estimate.

**Three explicit categories of caveat in `provenance.md`:**

1. *Source restrictions.* When a value is from a non-Mexican
   middle-income source (Brazil, Chile, etc.), state so and explain
   the assumption that it transfers to Mexico.
2. *Unit conversions.* Every value that required converting between
   annual and 5-year periods, between countries' currencies, or
   between observable and model concepts is documented with the
   exact arithmetic.
3. *Hand-tuning where unavoidable.* If a parameter has no direct
   literature anchor — for example, if no paper reports the value
   of `H̄_0` in the model's specific functional form — state this
   explicitly and document the reasoning for the chosen value.

---

## 3. What to produce

### 3.1 Directory layout

```
Calibration/inputs_anchored/
├── first_step/
│   ├── e_age.csv
│   ├── psi_base.csv
│   ├── delta_h.csv
│   ├── pi_birth.csv
│   ├── skill_params.csv
│   └── ar1_params.csv
├── moments/
│   └── targets.csv
├── config/
│   ├── pe_anchor.csv      ← copy verbatim from inputs/config/
│   ├── theta_init.csv     ← copy verbatim from inputs/config/
│   ├── usd_scale.csv      ← see §3.4 below
│   └── grids.csv          ← copy verbatim from inputs/config/
└── provenance.md
```

The `provenance.md` file is the deliverable's analytical content. It
should be 8–15 pages of carefully sourced parameter justifications,
not a one-paragraph summary.

### 3.2 First-step inputs — the six files

#### `e_age.csv` — age-efficiency profile by sex

Format: 17 rows, columns `age_period, male, female`.

The current placeholder has a Mincer-style hump peaking around model
period 6 (age 45–49) at `male = 1.97`, with `female = 0.85 · male`.
The 0.85 multiplier is the stub.

Look for: sex-specific age-earnings profiles for Mexico (or other
upper-middle-income countries). Mexico-specific sources include the
Mincer profiles estimated on ENOE in:
- \citet{Bargain2014} (Mexico wage equations)
- \citet{Lehmann2018} (informality and the wage profile in Mexico)
- World Bank wage-gap analyses for LAC

What to deliver:
- Age-efficiency profile that peaks in the right place (model period
  6–7, age 45–54). Workers in the early-twenties baseline (`period 1`)
  should be normalized to 1.0.
- Sex-specific levels reflecting Mexico's gender wage gap (~14% per
  the paper's Section 5; literature ranges 13–22% across LAC). The
  paper currently uses 15% (the 0.85 multiplier). Defend or adjust.
- Retirement bands (j ≥ 10) zero, per the model.

#### `psi_base.csv` — baseline survival schedule by sex

Format: 17 rows, columns `age_period, male, female`.

The current placeholder is a pooled life table for Mexico aggregated
to 5-year bands, with a sex-asymmetry stub
(`ψ_female = 1 - 0.75·(1-ψ_male)`).

Replace with: UN WPP 2024 medium-variant Mexico life table for 2020,
sex-specific, aggregated to 5-year bands from single-age data via
`ψ_period[j] = prod(ψ_annual[5(j-1)+1 : 5j])`.

This is doable through web search and arithmetic. The aggregate
anchors are:
- LE at birth: Mexico 2023, total 75.1, male 72.1, female 78.3
  (PAHO 2024).
- WPP 2024 medium variant publishes the underlying single-age life
  tables; aggregate to 5-year bands.

If the full WPP single-age life table is not accessible via search,
fall back to a method-of-targeting approach: take the existing pooled
schedule, apply a Brass-logit shift to hit the sex-specific LE
targets (the same method used for `demographics_2050.jl`). Document
which approach was used.

Terminal-age band (j=17, age 100+) uses a small positive value (e.g.,
0.15 male, 0.30 female) so that ψ^g_{J+1} ≡ 0 is enforced by the
solver's terminal-age handling.

#### `delta_h.csv` — health depreciation by age

Format: 17 rows, columns `age_period, value`. No sex dimension.

Current placeholder: 0.02 at the youngest ages, rising convexly to
0.80 at the oldest, period-specific (not annualized).

Look for: papers that estimate or calibrate a health-capital
depreciation schedule. The literature is small. Anchors:
- \citet{Cortes2024} (the BID2 working paper's empirical companion)
  estimates an age-varying depreciation schedule for Mexico based on
  GBD disability-adjusted life-year data. Look for the specific
  values they report.
- \citet{Dalgaard2014} provides the theoretical case for
  age-rising depreciation; their calibration to high-income data
  is a comparison point.
- \citet{Grossman1972}'s original Grossman model used a constant
  rate; later literature consistently moved to age-rising.

The functional shape (slow at young ages, accelerating after age 50,
sharp after age 75) is well-supported. The *level* is the open
question. The current placeholder shape is defensible; document the
literature for the level. If the published Mexican estimates from
Cortés et al. are accessible, use them.

#### `pi_birth.csv` — birth shares by sex and skill

Format: 4 rows, columns `sex_idx, theta_idx, share`. Must sum to 1.

Current placeholder: 0.25 across all four types — symmetric stub.

The paper commits to *asymmetric* birth shares
$\pi^{m,\theta_H}_1 > \pi^{f,\theta_H}_1$ — high-skilled men have
higher birth share than high-skilled women, reflecting Mexico's
documented gender gap in educational completion and skilled-sector
participation.

Look for:
- Mexico's educational attainment by sex (INEGI, Census 2020).
- The "skilled" share is typically defined as completing at least
  tertiary or completing upper-secondary. The literature uses 25–35%
  as the high-skill share of working-age adults in Mexico.
- Sex composition of newborns can be assumed equal (51% male, 49%
  female — the standard birth ratio). The asymmetry comes through
  the skill share.

Plausible deliverable: π = (0.27, 0.22, 0.24, 0.27) — for
(M-θ_L, M-θ_H, F-θ_L, F-θ_H), reflecting (a) slightly more men born,
(b) a higher male share among the skilled. Document the source for
each number.

#### `skill_params.csv` — skill levels and health-productivity penalty

Format: 2 rows, columns `theta_idx, theta, rho_pen`.

The two columns are:
- `theta`: log-productivity intercept (the paper's $\theta$). Current
  stub: $\theta_L = -0.20$, $\theta_H = +0.20$, implying a high-skill
  wage premium of $\exp(0.40) - 1 = 49\%$ at age zero.
- `rho_pen`: the health-productivity penalty $\varrho(\theta)$. Current
  stub: 0.30 for low-skill, 0.20 for high-skill, meaning low-skill
  workers' productivity is more sensitive to health.

Mexico's high-skilled/low-skilled wage premium: literature ranges
from 35% to 75% across studies (returns to tertiary education in
Mexico). Pick a defensible middle value.

The health-productivity penalty has weaker direct identification in
the literature. The Cortés et al. paper estimates it from ENASEM
work-survival probabilities by health status; pull their values if
accessible.

#### `ar1_params.csv` — labor-productivity persistence

Format: 2 rows, columns `param, value`. Parameters: `rho`, `sigma_eps`.

Current stub: ρ = 0.98 (high), σ_ε = 0.05.

These calibrate the AR(1) on η, the persistent productivity shock.
The literature has a long tradition here:
- \citet{Storesletten2004}: ρ ≈ 0.95–0.98, σ_ε ≈ 0.10–0.13 for US
  data at annual frequency.
- For Mexico specifically: \citet{Krueger2016Mexico} (if accessible)
  or other studies on income process estimation.
- 5-year period adjustment: at quinquennial frequency, ρ is closer
  to ρ_annual^5. Document the conversion.

The stub values (ρ = 0.98 at 5-year frequency, σ_ε = 0.05) imply a
highly persistent and modestly volatile process. ρ at 5-year
frequency should arguably be around 0.85–0.90 (if annual ρ ≈ 0.97,
then ρ^5 ≈ 0.86), and σ should be inflated to reflect the
accumulated 5-year variance.

### 3.3 Moment targets — `targets.csv`

Format: 6 rows, columns `name, value, se, description`.

Current placeholders are mostly literature anchors but with
internally inconsistent units (mean_m_age_25_35 = 0.300 in unconverted
units; logslope_m_25_75 = 0.020 at unspecified frequency).

For each of the six moments, find a defensible middle-income anchor
with a credible standard error.

| Moment name | Description | Approach to anchor |
|---|---|---|
| `hours_pa_males` | Average hours of prime-age males, share of time endowment | From ENOE: weekly hours / 168. Mexico anchor ~0.34 per the paper. SE small. |
| `vsl_usd` | Value of statistical life, 2022 USD | Middle-income VSL is much lower than $11.6M US. Mexican-specific VSL estimates exist (Hammitt, others). Range: $1.0–3.0M. Document the choice. |
| `cross_elast_m` | Cross-sectional income elasticity of medical spending | Hall-Jones (2007) estimate 1.6 from US; middle-income elasticities tend to be similar or higher (Costa-Font, Gemmill). |
| `mean_m_age_25_35` | Φ-weighted mean of m, periods j=2,3 | This is in model units. Pin it to the share of household consumption that goes to medical care at ages 25–35 in Mexico — roughly 3–5% per ENIGH. |
| `logslope_m_25_75` | OLS slope of log mean m on age, periods j=2..11 | Medical spending roughly doubles every decade in middle age; log-slope in 5-year periods ≈ 0.35. |
| `within_age_elast` | Within-age income elasticity of m | Smaller than the cross-elasticity; typically 0.3–0.5. |

For each target, provide a value, a standard error, and a citation in
`provenance.md`. The SE matters: it enters the weighted-distance
objective as $W_{ii} = 1/\sigma_i^2$, so larger SE means a moment
gets less weight in the calibration. Use SEs proportional to the
moment's reliability.

### 3.4 `usd_scale.csv` — unit conversion

The current placeholder has `usd_per_unit_c = 15,000` (annotated as
needing calibration to per-capita annual consumption).

For Mexico: 2020 per-capita household final consumption was roughly
USD 7,200 (World Bank). In the model, this is consumption per
5-year period. The relevant conversion depends on whether the model
consumption is denominated per period or per year. Document the
arithmetic.

A defensible value: `usd_per_unit_c = 36,000` (= 5 × 7,200 per
5-year period), assuming model consumption is per-period.

`reference_age_period = 4` (age 35 with 5-year bands and age-20
origin) is the VSL reference age. This stays at 4.

`periods_per_year = 5` is structural; do not change.

---

## 4. The `provenance.md` document

Structure:

```markdown
# Calibration anchors — provenance document

## Overview
- Purpose of this anchoring (intermediate calibration pre-Judy/Milo).
- Source-country priority: Mexico → other upper-middle-income LAC →
  middle-income globally.
- Date of compilation, sources accessed.

## First-step inputs

### e_age.csv
- Source(s) with full citation.
- Conversion arithmetic from raw to model units.
- Caveats (sex asymmetry, age range, etc.).
- Value: [table of 17 rows × 2 columns].

### psi_base.csv
- WPP 2024 vintage, access date.
- Aggregation method (single-age → 5-year bands).
- Source life-expectancy targets.
- Value: [table of 17 rows × 2 columns].

[... and so on for each first-step CSV ...]

## Moment targets

### hours_pa_males
- Value: 0.34
- SE: 0.01
- Source: ENOE 2022, weekly hours / 168, conditioning on prime age
  and formal employment.
- Caveats: hours measured as habitual rather than actual.

[... and so on for each target ...]

## Configuration

### usd_scale.csv
- Conversion: per-capita household final consumption Mexico 2020
  ≈ USD 7,200 (World Bank WDI), × 5 (period length) = USD 36,000
  per model consumption unit.
- VSL reference age: model period 4 = age 35.

## Substitution roadmap
- When Judy's ENASEM mortality regressions arrive → replace
  `psi_base.csv` and `delta_h.csv`.
- When Milo's ENOE wage decomposition arrives → replace
  `e_age.csv`, `skill_params.csv`, `ar1_params.csv`,
  `pi_birth.csv`.
- When data-side moment estimates arrive → replace `targets.csv`.
- Each substitution is file-level; no other CSV needs to change.
```

---

## 5. Verification — what the user will do with this

Once `inputs_anchored/` is produced, the user runs:

```bash
julia --project=. -t 4 Calibration/run_calibration.jl smoke \
    --inputs=Calibration/inputs_anchored
```

If the `--inputs` flag is not yet supported, the user will copy
`inputs_anchored/` over `inputs/` before running and restore after.

The expected output: a `moments_at_stub.csv` showing the six moments
at the literature-anchored starting parameters, against the
literature-anchored targets. The objective Q will likely still be
non-trivial (the starting parameters are not the calibrated ones),
but the *units* will be sensible and the *signs* will be right.
This is the meaningful diagnostic: a smoke pass with this
inputs_anchored set tells us the scaffold can deliver economically
meaningful output with literature-anchored inputs.

If smoke passes, the next step is a `jacobian` run (~2.5 hours) to
verify identification of the 6 SMM parameters from the 6 moments.
The Jacobian matrix should be full rank and well-conditioned.

If the Jacobian looks healthy, a `multistart` run (~12 hours)
produces calibrated estimates that are *defensible as
literature-anchored intermediate values*, ready to feed §7 of the
seminar paper.

When Judy and Milo deliver their CSVs, the relevant subset of
`inputs_anchored/` is replaced and the SMM is re-run. The pre-Mexican
calibration becomes the comparison point.

---

## 6. What this task is not

- Not a Mexican-data calibration. The values come from published
  cross-country literature, not from Mexican microdata estimation.
  Judy and Milo do that.
- Not a sensitivity analysis. The values are point estimates from
  the literature, no ranges or alternative anchors.
- Not the final calibration. The SMM that runs on top of these
  inputs produces intermediate estimates of the 6 SMM parameters.
- Not a verification of the scaffold. The smoke and parity tests
  have already verified the scaffold. This task feeds the scaffold
  with substantive inputs.

---

## 7. Pre-flight and deliverable checklist

**Pre-flight:**

- [ ] Confirm `inputs_anchored/` is the right directory name (the
      scaffold's `load_all_inputs` function may take a different
      argument convention; check `src/load_inputs.jl`).
- [ ] Confirm the `--inputs` CLI flag works (or document the
      copy-over fallback).

**Deliverable:**

- [ ] Eleven CSVs in `Calibration/inputs_anchored/`, schema-identical
      to `Calibration/inputs/`.
- [ ] `provenance.md` with 8–15 pages of sourced justification.
- [ ] All values have explicit citations.
- [ ] Unit conversions documented inline.
- [ ] `inputs/` directory is untouched.
- [ ] One short note at the top of `provenance.md` reiterating the
      "intermediate anchor, not Mexican-data calibration" framing.

---

## 8. Operational notes

- The literature search is the bulk of the work. Budget roughly
  60–70% of effort here, 30% on conversions and CSV production.
- Cross-country values may differ enough that you have to choose
  between competing anchors. The default rule: prefer Mexican
  sources; among non-Mexican, prefer middle-income LAC; among
  non-LAC middle-income, take the median.
- When a value has no published anchor at all (this will happen for
  some of the model-specific parameters like `H̄_0` and `h^slope`),
  document the hand-tuning rationale and the order-of-magnitude
  reasoning. These are the cells where Judy and Milo's SMM-style
  identification matters most.
- Do *not* edit `Calibration/inputs/` or `Calibration/src/`. The
  output is a new directory next to them.

# Calibration anchors — provenance document

> **Intermediate anchor, not a Mexican-data calibration.** Every value in
> `inputs_anchored/` is drawn from the published cross-country and Mexican
> *literature*, not from estimation on Mexican microdata. It exists so the SMM
> scaffold can run *now* with economically meaningful inputs, producing
> parameter estimates that are themselves intermediate but defensibly grounded.
> When Judy and Milo deliver ENASEM / ENOE / GBD first-step estimates and
> data-side moment targets, the relevant CSVs are replaced file-by-file (see
> §"Substitution roadmap") and the SMM is re-run. The pre-Mexican calibration
> then becomes the comparison point.

**Compiled:** 2026-05-27. All URLs accessed 2026-05-27.
**Source-country priority:** Mexico → other upper-middle-income LAC → middle-income globally.
**Units:** the model runs in 5-year periods, ages 20–100, J = 17 bands. Band j
covers ages 20+5(j−1) … 24+5(j−1): j=1 is 20–24, j=4 is 35–39 (the VSL reference
age), j=9 is 60–64, j=17 is 100+. Consumption is scaled to USD by
`usd_per_unit_c` (see §usd_scale).

---

## 0. Pre-flight findings (scaffold integration)

Two checks the task instructions flagged:

1. **Directory name.** `load_all_inputs(base_dir)` in `src/load_inputs.jl:191`
   accepts an arbitrary base directory, so `inputs_anchored/` is a valid sibling
   of `inputs/`. Confirmed.
2. **`--inputs` CLI flag does NOT exist.** `main()` in `run_calibration.jl:254`
   calls `load_all_inputs()` with no argument — it always reads the default
   `../inputs`. There is no `ARGS` parsing for an input path. **Use the
   copy-over-and-restore fallback** to run against the anchored set:

   ```bash
   cd "Calibration"
   mv inputs inputs_stub_backup            # set aside the placeholder set
   cp -r inputs_anchored inputs            # put anchored values in place
   julia --project=. -t 4 run_calibration.jl smoke
   # ... inspect outputs/moments_at_stub.csv ...
   rm -rf inputs && mv inputs_stub_backup inputs   # restore
   ```

   The `inputs/` directory itself is left **untouched** by this deliverable.
   (Alternatively, add a one-line `ARGS` parse to `main()`; not done here to
   respect the "do not edit `src/` or the driver" constraint.)

A **structural change to flag for coauthors:** the anchored `psi_base.csv`
introduces realistic young-adult mortality (survival < 1 for ages 20–49),
whereas the Household-Gender stub set survival ≡ 1.0 for bands j=1–6 (ages
20–49). This is intentional — the task asks for the real sex-specific life
table — but it changes working-age population attrition relative to the stub.
The `parity` mode is unaffected (it builds first-step values inline from
`build_householdgender_first_step()`, not from these CSVs).

---

## First-step inputs

### `e_age.csv` — age-efficiency profile by sex

**Value (retained from the Household-Gender stub; female = 0.85 × male):**

| j (age) | male | female | | j (age) | male | female |
|---|---|---|---|---|---|---|
| 1 (20–24) | 1.0000 | 0.8500 | | 9 (60–64) | 1.9007 | 1.6156 |
| 2 (25–29) | 1.3527 | 1.1498 | | 10–17 (65+) | 0.0 | 0.0 |
| 3 (30–34) | 1.6952 | 1.4409 | | | | |
| 4 (35–39) | 1.8279 | 1.5537 | | | | |
| 5 (40–44) | 1.9606 | 1.6665 | | | | |
| 6 (45–49) | 1.9692 | 1.6738 | | | | |
| 7 (50–54) | 1.9692 | 1.6738 | | | | |
| 8 (55–59) | 1.9392 | 1.6483 | | | | |

**Shape (male profile).** Standard concave Mincer experience profile,
normalized to 1.0 at entry (20–24), peaking at j=6–7 (ages 45–54), declining
to retirement, zero in retirement bands (j ≥ 10). The peak location is
consistent with the Mexican Mincer evidence: log-wage profiles estimated on
Mexican household surveys are concave in experience with the maximum around
~20 years of experience (≈ ages 40–50). Sources confirming the *shape*:
- Bouillon, C.P. (2000), *Returns to Education, Sector Premiums, and Male Wage
  Inequality in Mexico*, IADB/Georgetown (ENEU 1984/1994; concave experience
  term, "becoming somewhat more convex" over time).
  https://webimages.iadb.org/publications/english/document/Returns-to-Education-Sector-Premiums-and-Male-Wage-Inequality-in-Mexico.pdf
- Bautista-González (2021), *Employment and earnings by gender in Mexico*,
  Estudios Económicos (ENOE 2005–2017; experience the dominant factor lifting
  the profile). https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0186-72022021000200331

**Caveat — hand-tuning category (3).** A *published, ready-to-use normalized
age-efficiency vector by 5-year band for Mexico does not exist* in the sources
searched. The stub's male profile is therefore retained as the best available
shape (it is itself the Household-Gender calibration). This is a prime cell for
Milo's ENOE Mincer re-estimation.

**Sex multiplier — female = 0.85 × male (15% gap).** Retained, and defended:
- The paper's §5 uses a ~14% gender gap; the 0.85 multiplier (15%) is essentially that.
- INEGI/ENOE raw monthly-earnings gap ≈ **13%** ("for every 100 pesos a man
  earns, a woman earns ≈ 86.85"). https://mexicobusiness.news/talent/news/women-face-persistent-labor-gaps-mexico-inegi
- The LAC raw gap range is ~13–22%; 15% sits inside it.
- **Source restriction / sensitivity caveat (category 1):** the *adjusted hourly*
  ENOE gap is smaller (≈ 5–7%; Bautista-González 2021, mean log gap 0.05–0.07).
  If `e^g` is interpreted strictly as a per-hour productivity gap, 0.85 is on
  the high side; consider a sensitivity at 0.93–0.95. The 0.85 value is kept for
  consistency with the paper's §5 and the raw-gap evidence.

### `psi_base.csv` — baseline survival schedule by sex

**Method.** Built **directly from a real sex-specific abridged life table**
rather than the Brass-logit fallback. Source: **WHO Global Health Observatory
(GHO), Mexico, 2019** (pre-COVID, the cleanest structural vintage), indicator
`LIFE_0000000030` (nqx, probability of dying in [x, x+n) by sex). The 5-year
conditional survival entered in the CSV is `ψ_j = 1 − nqx_j`.
URL: `https://ghoapi.azureedge.net/api/LIFE_0000000030?$filter=SpatialDim eq 'MEX' and TimeDim eq 2019`

**Observed bands (j=1–13, ages 20–84), from WHO GHO 2019 nqx:**

| j (age) | male ψ | female ψ | | j (age) | male ψ | female ψ |
|---|---|---|---|---|---|---|
| 1 (20–24) | 0.98890 | 0.99705 | | 8 (55–59) | 0.94579 | 0.96749 |
| 2 (25–29) | 0.98592 | 0.99640 | | 9 (60–64) | 0.92401 | 0.95044 |
| 3 (30–34) | 0.98477 | 0.99559 | | 10 (65–69) | 0.89813 | 0.92694 |
| 4 (35–39) | 0.98252 | 0.99408 | | 11 (70–74) | 0.85003 | 0.88928 |
| 5 (40–44) | 0.97845 | 0.99131 | | 12 (75–79) | 0.78581 | 0.83205 |
| 6 (45–49) | 0.97162 | 0.98627 | | 13 (80–84) | 0.69062 | 0.73806 |
| 7 (50–54) | 0.96226 | 0.97946 | | | | |

**Extrapolated bands (j=14–17, ages 85+).** WHO GHO closes its abridged table
at 85+; the UN WPP 2024 data-portal API now requires an auth token (returned
HTTP 401), so single-age survival above 85 was not directly retrievable. Bands
85–89, 90–94, 95–99, 100+ are extrapolated by a **Gompertz fit on the 5-year
mortality hazard**. Let μ_j = −ln(ψ_j)/5 be the average annual hazard in band
j. A common log-hazard growth factor **g = 1.55 per 5-year band** is applied
(the geometric-mean old-age slope averaged across sexes: estimated male slope
≈ 1.51, female ≈ 1.61 over bands 70–74→80–84). Using a *common* factor on each
sex's own band-13 hazard preserves the female survival advantage at every
extrapolated band and avoids the spurious late-life crossover a free per-sex
fit produces. Resulting close-out:

| j (age) | male ψ | female ψ |
|---|---|---|
| 14 (85–89) | 0.56339 | 0.62460 |
| 15 (90–94) | 0.41090 | 0.48214 |
| 16 (95–99) | 0.25191 | 0.32278 |
| 17 (100+) | 0.11806 | 0.17333 |

The terminal band (j=17) is an open close-out; the solver enforces
ψ^g_{J+1} ≡ 0 by its terminal-age handling regardless of this value. Male
terminal 0.118 ≈ the doc's suggested 0.15; female 0.173 is internally
consistent with the Gompertz fit (the doc's 0.30 suggestion was a placeholder).

**Life-expectancy anchors (for cross-checking).** These are the targets the
schedule reproduces by construction (LE at age 20 from WHO GHO 2019
`LIFE_0000000035`):
- LE at birth, Mexico: male ≈ 72.4–72.8, female ≈ 78.0–78.9, total ≈ 75.3–75.8
  (World Bank 2024: 72.4 / 78.0 / 75.3, indicator `SP.DYN.LE00.*`; WHO 2019:
  72.8 / 78.9 / 75.8).
- LE at age 20: male **54.5**, female **60.2** (WHO GHO 2019).

**Source restriction (category 1) / correction.** The task doc cited
"PAHO 2024: total 75.1 / male 72.1 / female 78.3." Verified: the PAHO
*Health in the Americas* Mexico profile gives **total 75.3 with no sex split**
(https://hia.paho.org/en/country-profiles/mexico). The sex-specific figures
above are from the World Bank (2024) and WHO GHO (2019), not PAHO. WHO 2019 is
preferred over WHO 2021 because 2021 is COVID-depressed (male LE 67.2).
Sources:
- WHO GHO API (nqx, ex, LE at birth): `https://ghoapi.azureedge.net/api/...` (indicators above).
- World Bank API: `https://api.worldbank.org/v2/country/MEX/indicator/SP.DYN.LE00.MA.IN?format=json` (and `.FE.IN`, `.IN`).

### `delta_h.csv` — health depreciation by age

**Value (period-specific, per 5-year period):**

| j (age) | δ_h | | j (age) | δ_h | | j (age) | δ_h |
|---|---|---|---|---|---|---|---|
| 1 (20–24) | 0.0200 | | 7 (50–54) | 0.0664 | | 13 (80–84) | 0.2205 |
| 2 (25–29) | 0.0244 | | 8 (55–59) | 0.0811 | | 14 (85–89) | 0.2694 |
| 3 (30–34) | 0.0298 | | 9 (60–64) | 0.0991 | | 15 (90–94) | 0.3290 |
| 4 (35–39) | 0.0364 | | 10 (65–69) | 0.1210 | | 16 (95–99) | 0.4018 |
| 5 (40–44) | 0.0445 | | 11 (70–74) | 0.1478 | | 17 (100+) | 0.4908 |
| 6 (45–49) | 0.0544 | | 12 (75–79) | 0.1806 | | | |

**Method.** Anchored on the **Mitnitski/Rockwood frailty-deficit accumulation
model as adopted by Dalgaard & Strulik (2014)**, "Optimal Aging and Death:
Understanding the Preston Curve," *JEEA* 12(3):672–701
(https://onlinelibrary.wiley.com/doi/abs/10.1111/jeea.12071;
companion: http://holger-strulik.org/my_papers/health_capital_deficits.pdf).
Their calibration uses the **force of aging μ ≈ 0.043/yr (men), 0.031/yr
(women)** from Mitnitski et al. (2002a, N≈66,589), an autonomous deficit
component **E = 0.02**, and deficits that accumulate **3–4% per year**, i.e.
roughly **double every 16–20 years** (doubling time ln2/μ ≈ 16 yr at 0.043,
22 yr at 0.031).

**Construction.** δ_h is a single (sex-pooled) column, so a pooled force of
aging **μ = 0.04/yr** is used (between the male 0.043 and female 0.031;
doubling time ≈ 17 yr, inside the documented 16–20 yr range). The schedule is
δ_h(j) = δ_0 · exp(5μ(j−1)) with **δ_0 = 0.02** (= Mitnitski autonomous deficit
E, and equal to the stub's young-age value), giving a per-period growth factor
exp(5·0.04) = exp(0.2) = 1.2214. This reproduces the well-supported qualitative
shape (slow young, accelerating after 50, sharp after 75).

**Caveats.**
- *Hand-tuning category (3):* the *level* of old-age depreciation is not pinned
  by any direct empirical estimate. The schedule extrapolates the force-of-aging
  *rate*; the old-age values (e.g. δ_17 ≈ 0.49) are a model close-out, not data.
- The intended Mexican GBD/DALY-based depreciation schedule from **Cortés et al.
  (the BID2 empirical companion) could not be located on the open web** (the
  search returned no such indexed paper). If that paper is available internally,
  its values should replace this schedule. Per the user's instruction, δ_h is
  anchored on Dalgaard–Strulik/Mitnitski in the interim.
- *Conceptual:* Dalgaard & Strulik actually argue *against* the Grossman
  age-rising-δ formulation in favour of deficit accumulation; here we use their
  force-of-aging *rate* to discipline the Grossman δ_h growth, which is the
  standard mapping (the paper itself notes the Grossman "fix" is an
  age-dependent δ(t) with δ̇ > 0).

### `pi_birth.csv` — birth shares by sex and skill

**Value (sum = 1):**

| sex_idx | θ_idx | type | share |
|---|---|---|---|
| 1 | 1 | M, low-skill | 0.3927 |
| 1 | 2 | M, high-skill | 0.1173 |
| 2 | 1 | F, low-skill | 0.3822 |
| 2 | 2 | F, high-skill | 0.1078 |

**Construction.** Two ingredients:
1. **Sex split of births: 51% male / 49% female.** Mexican sex ratio at birth
   ≈ 1.039–1.05 (World Bank/UN modeled value 1.039 → 50.96% male, indicator
   `SP.POP.BRTH.MF`; biological norm 1.05 → 51.2%). 0.51/0.49 is a round value
   inside this range.
   `https://api.worldbank.org/v2/country/MEX/indicator/SP.POP.BRTH.MF?format=json`
2. **High-skill (tertiary) share by sex: men 23%, women 22%.** INEGI Census 2020
   tertiary ("educación superior") attainment: men 22.9%, women 21.8%. The
   θ_H type is identified with *tertiary* completion (consistent with the OECD
   tertiary wage premium used in `skill_params.csv`). Cross-check: OECD overall
   tertiary attainment 25–64 ≈ 21% (Education at a Glance 2023, Mexico note,
   https://gpseducation.oecd.org/Content/EAGCountryNotes/EAG2023_CN_MEX_pdf.pdf).

Shares = (sex share) × (skill share): M-θH = 0.51·0.23 = 0.1173,
F-θH = 0.49·0.22 = 0.1078, with the low-skill complements.

**This honours the paper's committed asymmetry** π^{m,θH} > π^{f,θH}
(0.1173 > 0.1078): high-skilled men have the higher birth share.

**Caveat — source restriction / stock-vs-flow (category 1).** The male skill
advantage holds in the *stock* of attainment (older cohorts), but recent
*flows* favour women: women are 53% of Mexico's first-time tertiary entrants
(2023) and now hold marginally more master's degrees (OECD EAG 2025;
INEGI Census 2020). For a *forward-looking* cohort model the flow evidence would
reverse the sign. The stock figures are used here because the paper commits to
π^{m,θH} > π^{f,θH}; this tension should be stated in the paper, and is a clear
candidate for revision when Milo's ENOE/Census skill-by-sex tabulations arrive.
The INEGI Census-2020 by-sex percentages are medium-confidence (the INEGI
interactive page is JS-rendered; re-pin to the tabulados before publication).

### `skill_params.csv` — skill levels and health-productivity penalty

**Value:** θ_L = −0.222, θ_H = +0.222; ϱ_pen = 0.30 (low), 0.20 (high).

**θ (log-productivity intercept).** Set so the high-skill wage premium
exp(θ_H − θ_L) − 1 = exp(0.444) − 1 = **55.9% ≈ 56%**, symmetric around zero
(preserving the mean-productivity normalization). The 56% anchor is the **OECD
tertiary-vs-upper-secondary earnings premium for Mexico, 2023** (OECD Education
at a Glance 2025, Mexico note; OECD average 54%).
https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/09/education-at-a-glance-2025-country-notes_9749f4ff/mexico_364135ce/3b36a6f6-en.pdf
This is comfortably inside the literature's 35–75% range for returns to tertiary
education in Mexico (cf. Lopez-Acevedo et al. 2025, *Economies* (MDPI) 13(2):43,
Mincer rate of return to tertiary 11.5–14.5%/yr;
https://www.mdpi.com/2227-7099/13/2/43).

**ϱ_pen (health-productivity penalty).** *Hand-tuning category (3):* retained at
the stub values (low-skill 0.30 > high-skill 0.20, i.e. low-skill productivity
is more sensitive to health). No published point estimate was located. The
intended source (Cortés et al., estimating ϱ from ENASEM work-survival by
health status) was not locatable on the open web; the sign — manual/low-skill
work more health-sensitive — is consistent with the health-gradient literature.
This parameter is a strong candidate for SMM-style identification by Judy.

### `ar1_params.csv` — labor-productivity persistence

**Value (5-year frequency):** ρ = 0.782, σ_ε = 0.265.

**Source & conversion.** Anchored on Storesletten, Telmer & Yaron (2004),
"Cyclical Dynamics in Idiosyncratic Labor Market Risk," *JPE* 112(3) (annual
PSID, 1969–1992), the standard income-process anchor: **annual ρ = 0.952**, and
a conditional innovation std averaging ~17%, ranging 12.5% (expansion) to 21.1%
(contraction). We take **σ_ε,annual = 0.13** (near the expansion/normal-times
value). Parameters verified via the STY (2007) *RED* draft
(ρ = 0.952; σ²_E = 0.0156, σ²_C = 0.0445):
https://bertha.tepper.cmu.edu/files/papers/sty_RED_jan07.pdf;
JPE: https://www.journals.uchicago.edu/doi/10.1086/383105

*Unit conversion (category 2) — time-aggregation of an AR(1) to 5-year
frequency:*
- ρ_5 = ρ_annual^5 = 0.952^5 = **0.782**.
- σ_5 = σ_annual · √(Σ_{k=0}^{4} ρ_annual^{2k}) = 0.13 · √(1 + 0.9063 + 0.8214 +
  0.7444 + 0.6746) = 0.13 · √4.1467 = 0.13 · 2.0364 = **0.265**.
- Check: stationary variance is preserved — σ²/(1−ρ²) gives 0.1804 at both
  frequencies, as required.

This corrects the stub (ρ = 0.98, σ_ε = 0.05 at 5-year frequency), which
overstated persistence and badly understated 5-year innovation variance.

**Source restriction (category 1).** No Mexico-specific or Latin American AR(1)
income-process estimate was found (the Global Repository of Income Dynamics
notes high persistence in some LAC countries but publishes no Mexico ρ/σ point
estimate). The STY US values are used with this caveat; a Mexican earnings-
dynamics estimate would replace them.

---

## Moment targets — `targets.csv`

The weighting matrix is W_ii = 1/σ_i², so a larger SE down-weights a moment.
SEs below are set proportional to each moment's reliability and the dispersion
of the underlying literature.

### `hours_pa_males` — value 0.34, SE 0.01
Φ-weighted mean of the labor-supply policy `l_pol` over prime-age males
(j < jR), interpreted as the share of the time endowment devoted to market work.
Anchor: the standard ~1/3 macro target, consistent with Mexico's high measured
hours — OECD average annual hours worked ≈ 2,124–2,193 (2020–2024), among the
highest in the OECD (ENOE shows a modal 35–48 hr band and ~28% of men working
>48 hr). Normalized to a waking-time endowment this lands near 0.34.
- OECD hours: https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_labor_hours (OECD table); ENOE Q4-2022: https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/doc/enoe_n_presentacion_ejecutiva_trim4_2022.pdf
- *Caveat (category 2):* the exact value depends on the endowment normalization
  (a 57-hr week is 0.34 of 168; a 48-hr week is 0.34 of ~140 waking hours).
  Small SE because aggregate hours are well measured; the normalization is the
  judgment call.

### `vsl_usd` — value 2,000,000, SE 700,000
VSL at the reference age (j=4, age 35), 2022 USD. The model computes
VSL_USD = VSL_model × `usd_per_unit_c`, so this target and `usd_per_unit_c` are
independent inputs and both reflect Mexican magnitudes.
Anchor: **benefit-transfer national VSL for Mexico ≈ USD 2.0M (2021 USD)**,
transferred from the OECD reference VSL (~USD 9M) at income elasticity ≈ 1.0;
the sub-national range runs USD 0.4M (Chiapas) to USD 3.3M (Mexico City).
https://pmc.ncbi.nlm.nih.gov/articles/PMC11032065/
- *Caveat (category 1 + dispersion):* primary revealed/stated-preference Mexican
  studies are an order of magnitude lower — Hammitt & Ibarrarán (2006) USD
  0.235–0.325M (2002, Mexico City wage-risk); de Lima et al. (2020) USD 0.21M
  (stated preference). These reflect actual Mexican WTP but are not the values
  used for policy. The large SE (700k, ≈ 35% of value) reflects this genuine
  method dispersion and appropriately down-weights VSL in the objective.
- *Correction:* the stub's USD 11.6M is the *US* VSL and is replaced.

### `cross_elast_m` — value 1.0, SE 0.30
Pooled weighted-OLS slope of log m on log permanent income across all cells —
the cross-sectional (cross-individual) income elasticity of medical spending.
Set to **unity**, a defensible middle for an upper-middle-income economy that
straddles two literatures:
- The aggregate "health as luxury" tradition (elasticity > 1): Gerdtham &
  Jönsson (2000), *Handbook of Health Economics* 1A, cross-country 1.2–1.5;
  invoked by Hall & Jones (2007), *QJE* 122(1), who state health is "a superior
  good with income elasticity well above one."
- The bias-corrected / middle-income micro evidence (elasticity < 1): Costa-Font,
  Gemmill & Rubert (2011), *JRSS-A* 174(1), publication-bias-corrected 0.26–0.84;
  Vargas Bustamante & Shimoga (2017), *IJHPM*, 0.51 for middle-income countries.
- *Correction (category 1):* the original description attributed "1.6" to
  Hall & Jones; the paper gives no such point value (it reports γ = 1.5 and
  argues qualitatively for elasticity > 1). The 1.2–1.5 figure is
  Gerdtham–Jönsson, not Hall–Jones. Wide SE reflects the 0.5–1.5 dispersion.
- Sources: https://web.stanford.edu/~rehall/HallJones2007.pdf;
  https://www.sciencedirect.com/science/article/abs/pii/S1574006400801602;
  https://academic.oup.com/jrsssa/article/174/1/95/7077700;
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5890070/

### `mean_m_age_25_35` — value 0.04, SE 0.02
Φ-weighted mean of medical spending `m` for j ∈ {2,3} (ages 25–35), in **model
consumption units**. Anchor: ENIGH 2022 (INEGI) health/medical care ≈ **3.4%**
of household expenditure (smallest spending category). Because `usd_per_unit_c`
normalizes one model consumption unit to per-capita per-period consumption, mean
consumption ≈ 1 model unit, so a 3.4–4% medical share maps to m ≈ 0.034–0.04.
https://en.www.inegi.org.mx/programas/enigh/nc/2022/
- *Caveats (categories 1, 2, 3):* (a) the 3.4% is the all-household average, not
  25–35-specific (age-disaggregated ENIGH health shares were not located);
  (b) the conversion assumes the model's mean consumption ≈ 1 unit — the smoke
  run will reveal the actual consumption scale, and if it departs from 1 this
  target should be rescaled. This is the cell most sensitive to the
  model-consumption normalization (the doc's stub value 0.30 was flagged as in
  inconsistent units and is replaced). Wide SE accordingly.

### `logslope_m_25_75` — value 0.12, SE 0.05
OLS slope of log(mean m by age) on the **age-period index** (j = 2..12, equal
weights), so slope = 5 × annual growth rate of medical spending. Anchor:
life-cycle health-spending growth ≈ **2–2.5%/yr** (Dalgaard & Strulik 2014, ~2%/yr
across AUS/CAN/NZL/USA; Mexican ENSANUT shows the 60+ group spending ≈ 2× younger
adults over ~40 yr). At ~2.4%/yr, slope = 5 × 0.024 ≈ **0.12**.
- *Correction (category 1):* the doc's "≈ 0.35" assumed medical spending doubles
  every decade (g ≈ 6.9%/yr); this is **not corroborated** by the Mexican /
  cross-country evidence, which supports the slower ~2–2.5%/yr figure used here.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC3073904/ (ENSANUT age profile).
- The stub value 0.02 (≈ 0.4%/yr) was implausibly flat and is replaced.

### `within_age_elast` — value 0.40, SE 0.15
Mass-weighted mean over working ages of the within-age (cross-income) income
elasticity of m. Smaller than the cross-sectional elasticity, as the model
ordering requires (1.0 > 0.4). Anchor: the within/individual income elasticity
of medical spending is "substantially less than one" (Hall & Jones 2007, citing
Newhouse 1992 / the RAND HIE), typically **0.2–0.5** for insured populations.
- *Caveat (category 1):* Mexican out-of-pocket micro evidence is *higher*
  (≈ 1.0, and > 1 in the North; Sáenz-Vela & Guzmán-Giraldo 2022, Estudios
  Económicos, https://estudioseconomicos.colmex.mx/index.php/economicos/article/view/434),
  plausibly because OOP spending is less insurance-shielded than US insured
  spending. 0.40 follows the Newhouse/RAND range; the wide SE (0.15) reflects
  the US-vs-Mexico tension.

---

## Configuration

### `usd_scale.csv`
- `usd_per_unit_c = 35,000`. *Unit conversion (category 2):* per-capita
  household final consumption in Mexico, 2021 ≈ **USD 7,047** (World Bank WDI,
  `NE.CON.PRVT.CD` ÷ `SP.POP.TOTL`); × 5 (period length) ≈ **USD 35,000** per
  model consumption unit (model consumption is per 5-year period).
  - *Caveat:* the 2020 value (≈ USD 5,849) is COVID-depressed and the 2022–2023
    values (≈ 8,048 / 9,671) reflect strong peso appreciation; 2021 is chosen as
    representative. The doc's "≈ 7,200 for 2020" in fact matches the **2021**
    current-USD figure, not 2020.
  - `https://api.worldbank.org/v2/country/MEX/indicator/NE.CON.PRVT.CD?format=json`
- `reference_age_period = 4` (age 35) — VSL reference age. Unchanged.
- `periods_per_year = 5` — structural. Unchanged.

### `pe_anchor.csv`, `theta_init.csv`, `grids.csv`
Copied **verbatim** from `inputs/config/`. These are technical scaffold settings
(fixed PE prices from the converged GE-Gender baseline; SMM starting values and
bounds; numerical grid sizes), not empirical inputs. `pe_anchor.csv` carries the
GE-Gender gender-gap baseline prices (r = 0.26445, w = 0.98825, τp = 0.145,
pen = 1.06407).

---

## Substitution roadmap

Each substitution is file-level; no other CSV needs to change.

- **Judy's ENASEM mortality/health regressions arrive** → replace
  `psi_base.csv` (sex-specific survival) and `delta_h.csv` (GBD/DALY-based
  depreciation, the intended Cortés et al. schedule). Also `skill_params.csv`
  `rho_pen` (ENASEM work-survival by health status).
- **Milo's ENOE wage decomposition arrives** → replace `e_age.csv`
  (Mexican Mincer age-efficiency by sex), `skill_params.csv` `theta`
  (ENOE skill premium), `ar1_params.csv` (Mexican earnings-dynamics ρ, σ),
  and `pi_birth.csv` (ENOE/Census skill-by-sex, resolving the stock-vs-flow
  tension).
- **Data-side moment estimates arrive** → replace `targets.csv` (ENOE hours,
  Mexican VSL, ENIGH medical shares and age profile, ENIGH income elasticities)
  and recalibrate `usd_scale.csv` from the same ENIGH consumption aggregate.

---

## Caveat index (by category)

1. **Source restrictions (non-Mexican or transferred):** AR(1) ρ/σ (US PSID,
   STY); within/cross medical-spending elasticities (US RAND + cross-country);
   VSL (OECD benefit-transfer, elasticity 1.0); life table (WHO GHO 2019, not
   WPP 2024). Gender-gap and skill-by-sex stock-vs-flow tensions.
2. **Unit conversions:** AR(1) annual→5-year time-aggregation; `usd_per_unit_c`
   per-year→per-period (×5); `logslope` slope = 5 × annual growth; `mean_m`
   share→model-units (assumes mean c ≈ 1 unit).
3. **Hand-tuning where unavoidable (no published anchor):** `e_age` male shape
   (no Mexican normalized profile); `delta_h` old-age *level* (force-of-aging
   rate extrapolated); `skill_params` `rho_pen` (no estimate; sign only).

---

## Sources (consolidated, accessed 2026-05-27)

**Mortality / demography**
- WHO Global Health Observatory API (nqx `LIFE_0000000030`, ex `LIFE_0000000035`,
  LE `WHOSIS_000001`), Mexico 2019/2021 — `https://ghoapi.azureedge.net/api/`
- World Bank API (LE at birth `SP.DYN.LE00.*`; sex ratio at birth
  `SP.POP.BRTH.MF`; consumption `NE.CON.PRVT.CD`; population `SP.POP.TOTL`),
  Mexico — `https://api.worldbank.org/v2/country/MEX/indicator/...`
- PAHO, *Health in the Americas* — Mexico — https://hia.paho.org/en/country-profiles/mexico
- INEGI, *Censo 2020* national results — https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2021/EstSociodemo/ResultCenso2020_Nal.pdf

**Labor / education**
- OECD, *Education at a Glance 2025/2023*, Mexico notes (tertiary premium 56%;
  attainment) — https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/09/education-at-a-glance-2025-country-notes_9749f4ff/mexico_364135ce/3b36a6f6-en.pdf ;
  https://gpseducation.oecd.org/Content/EAGCountryNotes/EAG2023_CN_MEX_pdf.pdf
- Bouillon (2000), IADB — https://webimages.iadb.org/publications/english/document/Returns-to-Education-Sector-Premiums-and-Male-Wage-Inequality-in-Mexico.pdf
- Bautista-González (2021), Estudios Económicos — https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0186-72022021000200331
- Lopez-Acevedo et al. (2025), *Economies* (MDPI) — https://www.mdpi.com/2227-7099/13/2/43
- INEGI/ENOE gender earnings — https://mexicobusiness.news/talent/news/women-face-persistent-labor-gaps-mexico-inegi
- OECD annual hours (table) — https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_labor_hours
- INEGI ENOE Q4-2022 — https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/doc/enoe_n_presentacion_ejecutiva_trim4_2022.pdf
- Storesletten, Telmer & Yaron (2004 JPE; 2007 RED draft) — https://www.journals.uchicago.edu/doi/10.1086/383105 ; https://bertha.tepper.cmu.edu/files/papers/sty_RED_jan07.pdf

**Health / depreciation / VSL / spending**
- Dalgaard & Strulik (2014), JEEA — https://onlinelibrary.wiley.com/doi/abs/10.1111/jeea.12071 ; companion http://holger-strulik.org/my_papers/health_capital_deficits.pdf
- Grossman (1972, NBER reproduction) — https://www.nber.org/system/files/working_papers/w7078/w7078.pdf
- Hall & Jones (2007), QJE — https://web.stanford.edu/~rehall/HallJones2007.pdf
- Gerdtham & Jönsson (2000), Handbook of Health Economics 1A — https://www.sciencedirect.com/science/article/abs/pii/S1574006400801602
- Costa-Font, Gemmill & Rubert (2011), JRSS-A — https://academic.oup.com/jrsssa/article/174/1/95/7077700
- Vargas Bustamante & Shimoga (2017), IJHPM — https://pmc.ncbi.nlm.nih.gov/articles/PMC5890070/
- VSL Mexico, sub-national benefit transfer (PMC11032065) — https://pmc.ncbi.nlm.nih.gov/articles/PMC11032065/
- de Lima et al. (2020) / LSE Grantham WP 272 — https://www.lse.ac.uk/GranthamInstitute/wp-content/uploads/2017/08/Working-paper-272-Lima-1.pdf
- Hammitt & Ibarrarán (2006), Health Economics — https://onlinelibrary.wiley.com/doi/10.1002/hec.1137
- Sáenz-Vela & Guzmán-Giraldo (2022), Estudios Económicos — https://estudioseconomicos.colmex.mx/index.php/economicos/article/view/434
- ENIGH 2022 (INEGI) — https://en.www.inegi.org.mx/programas/enigh/nc/2022/
- ENSANUT elderly health utilization (PMC3073904) — https://pmc.ncbi.nlm.nih.gov/articles/PMC3073904/

> **Not located:** Cortés et al. (BID2 empirical companion) GBD/DALY-based
> Mexican depreciation schedule — not found on the open web; `delta_h` and
> `skill_params.rho_pen` are interim anchors pending that source.

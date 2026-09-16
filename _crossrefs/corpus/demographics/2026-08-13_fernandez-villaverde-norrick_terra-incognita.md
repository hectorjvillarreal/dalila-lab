---
type: corpus_entry
tier: methodological_reference
project_scope: [DFD, BDH, Aurora]
authors: [Fernández-Villaverde, Jesús; Norrick, Patrick]
year: 2026
title: "Terra Incognita: The Economics of a Shrinking World"
venue: "Paper prepared for Annual Review of Economics; working paper dated 10 August 2026"
doi: "10.1146/annurev-economics-081026-024323 (assigned, not yet resolvable — see §Source quality)"
date_added: 2026-08-13
added_by: Claude Code
endorsed_by:
build_instruction: "_crossrefs/_build_instructions/2026-09-15_demographics_terra_incognita_reconstruction.md"

indicators: [tfr, cfr, cbr, births, projection, replacement_rate, dependency_ratio, growth_accounting, migration]
geography: [WLD, LAC, MEX, COL, CHL, BRA, ARG, GTM, PAN, URY; comparators USA, JPN, KOR, CHN, TWN, ITA, ESP, IND, TUN, THA]
scenario_implication: [fast-transition, baseline-revision]
source_reliability: primary   # academic paper with full methodology and supplemental materials
data_vintage: 2026   # paper dated 2026-08-10; registry data through 2025, WPP 2024 revision
cornerstone: true
supersedes: "2026-06-20_fernandez-villaverde-demographic-future.md (April deck — superseded as the standing scenario-discipline reference)"
workflow_status: pending-endorsement
reconstruction_note: "Filed 2026-09-15 under its date and name of record. See §Provenance — this text was drafted from the primary source on 2026-09-15, not recovered from an earlier draft."
---

# Fernández-Villaverde & Norrick (2026) — *Terra Incognita: The Economics of a Shrinking World*

## One-line summary

Humanity is likely already below replacement fertility; a single-factor model over 236
countries shows the decline is now driven almost entirely by country-specific trends
(219 of 236 negative, none levelling off) rather than a common global force; no
mechanism in the literature explains both the universality and the country-specific
timing, so the authors conjecture modernity itself — and note that nothing in an
economy pushes fertility back to replacement.

## Provenance (read first)

This entry was **drafted on 2026-09-15 from the primary source**, and filed under the
date and filename of record (`2026-08-13_…`) so that the citation chain in Anne's
2026-09-15 endorsement record resolves. It is **not** a recovered copy of an earlier
draft. Investigation on 2026-09-15 established that no entry of this name was ever
committed to Dalila on any branch, local or remote; no August supersession build
instruction exists; and the April deck was never retired to the build-instruction
archive. The underlying paper is real and was verified independently.

Consequently `endorsed_by:` is **blank** and `workflow_status: pending-endorsement`.
Anne's endorsement of 2026-08-13 attaches to a document that is not in the repository
and that the drafter has never seen; it cannot be asserted over this text. Re-endorsement
is required. `cornerstone: true` is carried because Anne's 2026-09-15 record states the
designation as settled, but the endorsement of *this text* is open.

## Core conceptual contributions

### 1. The headline claim, and the corrected replacement rate

The world is likely below replacement as of 2026. This rests on a correction that is
itself load-bearing: **2.1 is the replacement rate for a rich country**, not for the
world. The approximation is

> replacement ≈ (1 + sex ratio at birth) / P(woman survives to 30)

giving ≈ (1+1.05)/0.98 ≈ **2.1** for an advanced economy, ≈ (1+1.10)/0.90 ≈ **2.33**
for India c. 2005 (sex-selective abortion plus child mortality), and ≈ (1+1.07)/0.94 ≈
**2.20** for the world in 2026. WPP's Medium Variant puts world TFR 2026 at 2.23 on
132.5 million births — still above replacement. Correcting for the birth overstatement
documented in Supplemental Material B brings it to **at most 2.19**, below. The authors
are deliberately undramatic about this: they move only the second decimal, and state
that whether the crossing happened in 2025 or happens in 2027 changes nothing in the
argument.

World population is projected to peak around **2056**, against the WPP Medium Variant's
10.289 billion in 2084. Their reading is *slightly less aggressive* than WPP's own Low
Variant (8.949 billion in 2053) — though they note births since WPP 2024 appear to be
falling below even the Low Variant.

### 2. The single-factor model (§4) — the empirical core

TFR_it = α_i + δ_i·t + β_it·λ_t + ε_it

estimated on a balanced panel of **236 countries and territories, 1950–2023**, taken
from the WPP (used because no alternative combines global estimates, multiple sources,
and biennial updates — the critique in Supplemental B notwithstanding). Estimation is
local principal components following Su and Wang (2017), extended to country-specific
levels and trends, with an Epanechnikov kernel of 20-year bandwidth; standard errors
from a moving-block residual bootstrap (8-year blocks, 5,000 replications).

Findings:

- **The common factor is a bygone wave.** λ̂ climbs from −2.36 (1950) to **1.60 in 1978**,
  falls to −0.5 by the late 1990s, and drifts slowly since.
- **219 of 236 country trends are negative**, mean δ̂ = **−0.0622** births per woman per
  year, with no sign of levelling off in sample. Only 17 trend upward, none by much —
  Chad (0.0315), Ethiopia (0.0173), DR Congo (0.0163), Burkina Faso (0.0159), Niger
  (0.0145) — and all but Afghanistan and Timor-Leste are sub-Saharan African.
- **Loadings move.** The share of countries with β̂ > 0 falls from 83% (1950) to 52%
  (1990) to **28% (2023)**, with 157 of 236 switching sign at least once. A constant-loading
  restriction yields half-sample loading correlations of just 0.18 — which is why the
  loadings are allowed to vary.
- **The U-shape.** Trends plotted against mid-sample levels are U-shaped: a quadratic in
  α̂ explains **55%** of cross-country variation in δ̂, a straight line only 4%, with the
  minimum near 4.0. The fastest decliners are the middle: Thailand (−0.146), Mongolia
  (−0.144), Tunisia (−0.144), China (−0.142), Algeria (−0.138), Iran (−0.125).
- **Dispersion, not a common shock, is now the story.** The cross-country dispersion of
  the factor contribution falls from 0.86 (1950) to 0.29 (1990), then rises to **1.60
  (2023)** — roughly fivefold after 1990. Median country R², after removing level and
  trend, is 0.967.

**The two criteria.** Any satisfactory explanation must deliver (i) a *nearly universal*
drop and (ii) *country-specific timing* differing by decades. Most candidate mechanisms
deliver one or the other. This is the paper's organising test.

### 3. The integer arithmetic of replacement (§5.1)

100 women: 15 childless (≈5 by choice, 5 who never partner or postpone too long, 5 for
medical reasons), 10 with one child, 60 with two, 10 with three, 5 with four → 180
children, **CFR 1.8**. Now: 26 childless, 23 with one, 46 with two, 5 with three →
**CFR 1.3**, the lowest-low threshold. Three-quarters of women behave exactly as before
and the median is still two. Any explanation need only account for the quarter who
switch. This is the paper's most useful teaching device and it lowers the bar for every
mechanism that follows.

### 4. Mechanisms assessed (§5.2) and found wanting

- **Quality-quantity (Becker–Barro),** with Delventhal et al. (2021) adding skill-biased
  technology diffusion (Lucas 2009) to match transition timing and acceleration: gets
  timing, not suddenness. *No plausible calibration delivers Colombia's 35% fall in
  births in ten years through this channel alone.*
- **Price of parental time / marketization** (Bar et al. 2018); Hazan et al. (2023) show
  highly educated women's childlessness converged to other women's by 2020 — children
  becoming a luxury good.
- **Housing, ambiguous by construction.** Dettling and Kearney (2014): +$10,000 in local
  prices raises homeowner births ~5% and cuts non-homeowner births ~2.4%, net positive
  since most US households own. Yi and Zhang (2010) find the opposite in Hong Kong.
  Fazio et al. (2025) use Brazilian housing-credit lotteries: winning a home raises the
  probability of a child by about a third among 20–25-year-olds. Couillard (2025): at
  1990 real housing costs, 13 million more US children over three decades, and building
  fewer large units generates 2.3× more births than more small ones. The objection that
  survives: housing cannot explain fast declines where real estate is cheap relative to
  income.
- **Policy, in both directions, is small.** China's one-child policy against Taiwan as a
  quasi-control: in 1979 Taiwan 2.67 vs China 2.80; by 2015 (policy lifted) Taiwan
  **1.18** vs China 1.57 — Taiwan fell *further* without the policy. Pro-natalist effects
  are real but modest (Milligan 2005; Cohen et al. 2013, elasticity ≈ −0.5; González
  2013; Laroque and Salanié 2014; Raute 2019), with CFR responding to parental leave and
  cheaper housing more than to cash.
- **Smartphones as accelerant, not cause.** Myers and Hooper (2026) exploit AT&T's
  iPhone exclusivity (June 2007–February 2011) and attribute **33–52%** of the fall in
  the general fertility rate among women 15–44; Hudson and Moscoso Boedo (2026) replicate
  for England and Wales teen conceptions. The authors' counter: Italy was 1.19 in 1995
  and 1.14 in 2025. Where smartphones matter is norm diffusion — what took 25 years now
  takes 10. Hence Guatemala 3.8 (2005) → 1.9 (2025): *"Without smartphones, Guatemala
  would also have reached 1.9, just 20 years later."*

### 5. The modernity conjecture (§5.2, closing)

Modernity = a society organised around formal institutions, specialised expertise, and
large-scale coordination (Weber; Gellner, Giddens, Scott; Mokyr on codified useful
knowledge). Explicitly **not** capitalism — Hungary fell below replacement in 1960 and
Czechoslovakia in 1966, with only modest, short-lived mid-1970s booms.

Such a society makes **the third child expensive** (credentialing requires years of
costly investment; children are no longer productive in the household, displaced by
"engines of liberation"; career schedules set by large organisations collide with the
biological clock and with dissolved kin networks) **and childlessness cheap** (pensions
and health care do the work that sons and daughters once did; lineage counts for little).

**Goldin (2026) supplies the gender extension:** modernity changes gender roles
unevenly — women's opportunities expand fast through education, work and independence
while expectations about housework and childcare lag, sharpest where economies shift to
services. It operates on both margins (more childlessness, and fewer children among
mothers). The authors find it attractive because *"it explains why East Asia and now
Latin America have such low TFRs. These are the societies where the gender mismatch is
largest."* It implies a **paradoxical reversal**: societies with highly unbalanced gender
norms start with very high TFRs, as men impose their preferences, and end with very low
ones, as women resist. A footnote draws the policy corollary — this is why cash transfers
accomplish little while parental leave matters: *the binding constraint is not the price
of a child but who does the work of raising them.*

**The landing zone.** Expensive children plus cheap childlessness gets a society well
below replacement, **perhaps to ~1.4**; when each country arrives depends on the speed of
modernisation, which is not the same as the level of GDP per capita. From 1.4, countries
move either way: **up to 1.6–1.7** with higher income, work-family balance, gender
equality, cheaper housing, less acute educational arms races, or a significant religious
subpopulation (the US has many though not all of these); **down to 0.7–0.8** with the
opposite bundle, which China, Taiwan and South Korea possess at once. *"Modernity in its
current form seems largely incompatible with replacement-level fertility."*

### 6. No feedback mechanism (§5.3) — the theoretical core for DFD

Economists trust markets because they self-regulate; Smith (1962) showed double auctions
converge with a handful of traders, and Gode and Sunder (1993) reached ~100% allocative
efficiency with zero-intelligence machines bidding at random under a budget constraint.
**Nothing analogous operates on fertility.** There is no reason the benefits of a falling
population (cheaper housing) should overcome the costs (slower growth, higher taxes) and
restore a steady state. More fundamentally, both welfare theorems break down in
overlapping generations (Samuelson 1958): generations far apart cannot trade, so the
economy behaves as if markets were incomplete, and the double infinity of agents and
dated commodities (Shell 1971) defeats the standard proof. Citing **Weil (2024): the
replacement rate has no special status as an attractor or a target.**

Only three forces could return a population to replacement — policy (small), selection
as higher-fertility subpopulations grow (Galor and Moav 2002; Collins and Page 2019),
and relative-price changes from a falling population (Jones 2022). None is fast or
efficient. Malthusian feedback is real but operates over centuries: *"nearly none of the
fertility decisions of women in Seoul or Bogotá are determined by the availability of
food."*

### 7. Economic consequences (§6)

- **Good news first.** US teenage pregnancies fell 74% between 2004 and 2024, and about
  three-quarters of teen pregnancies are unintended. Slower growth eases pressure on
  infrastructure, housing and emissions; **Latin American countries could redesign the
  cities that grew wildly and often without decent services during the 1950s–1980s boom**;
  emerging economies get a window to educate smaller cohorts better and enjoy some fiscal
  space for structural reform before aging fully bites. Integrated assessment models take
  population as an exogenous input and their emission paths are sensitive to it in ways
  the literature has rarely explored — against which the fiscal pressures of aging may
  make the net-zero transition harder to fund.
- **Growth accounting.** g_y = g_(y/l) + g_l, arithmetic rather than model. US around
  2000: 3.0% = 2% + 1%. US around 2050, holding productivity and assuming no net
  migration: **1.5% = 2% + (−0.5%)**. A boom then delivers 2.5%, a slump 0.5%. Neither
  monetary stimulus nor fiscal packages address this: a shrinking labour force is not a
  demand shortfall but a fall in the trend of potential output.
- **The Japan/US counterfactual (Table 1, 1991–2023).** Japan GDP 0.79 vs US 2.60; per
  hour worked, Japan 1.22 vs US 1.62; working-age adults Japan −0.53 vs US 0.85. Swap
  only labour growth: Japan counterfactually 2.20 = 1.22 + 0.98, US 1.19 = 1.62 + (−0.43).
  **The verdict reverses — instead of the US leading by 1.8 pp a year, it lags by 1.0 pp.**
  Japan is not a story of policy failure; it is a story of a US that outperforms all seven
  comparators.
- **Productivity will not hold at 2%.** Semi-endogenous growth ties income growth to
  researcher growth (Jones 1995), which cannot outpace population; Jones (2022) shows
  permanently negative population growth converges to a path where knowledge and living
  standards stop growing (the empty planet); and ideas are getting harder to find — Bloom
  et al. (2020) put US research productivity decline at ~5% a year. The **talent-tail**
  argument: South Korea's 1,080,535 births in 1960 against 230,028 in 2023, a 4.7-fold
  contraction. Under a Gaussian tail the top child moves only from 4.84σ to 4.53σ; under
  a Pareto tail with α = 2 the frontier scales with the square root of cohort size and
  the median cohort maximum falls from 883× the median person to 407×. Evidence on
  returns to innovation points to fat tails, so the second case is the relevant one. Also
  firm dynamism: Liang et al. (2018) find a one-SD fall in median age buys 2.5 pp of new
  firms (~40% of the mean rate); Karahan et al. (2024) attribute two-thirds of the US
  start-up-rate decline since the late 1970s to demographics.
- **Direct engagement with Acemoglu et al. (2026).** Their labour-scarcity-induces-
  automation argument is judged intriguing but not informative for today's fertility: the
  lowest TFR in their 1950 cross-section is Austria at 2.09 (essentially replacement) and
  the 1980 panel floor is Germany at 1.56. A TFR of 1.56 leaves 40% of the initial
  population after a century; a TFR of 0.75 leaves 3.5% — a factor of eleven. Both count
  as "low fertility" in a regression yet are different regimes, as those authors concede
  in their own conclusion.
- **Per capita vs total output.** Per capita is the right welfare measure and slower
  labour-force growth costs less than headline numbers suggest (Japan kept improving;
  Weil 2026 simulates the same for the US). **But debt service and social security
  obligations depend on total output — bondholders and retirees are paid in levels, not
  ratios** — and defence spending in a world of great-power competition requires total
  output. Second-round effects flagged but not explored: monetisation and inflationary
  pressure, real interest rates, housing prices, and internal redistribution toward a few
  large "sponge cities."
- **The political economy of aging is the first-order problem.** With roughly as many
  retirees as workers and approximate income parity, what each worker produces must be
  split in two — and it makes no difference whether through PAYG taxes or capital income
  in a funded system. This is likely to poison politics and produce dysfunctional policy;
  Western Europe's fights over retirement benefits already show it, and much American
  unhappiness about corporate profits, largely owned by the old, is *"the same conflict,
  only in the fetishized form of equity ownership."* Claims that AI or unprecedented TFP
  growth will fix aging **miss the point: the redistribution problem is about politics,
  not productivity.**
- **Japan was the easy case.** Homogeneous, high-consensus, well-governed, rich. *"It is
  hard to imagine how countries such as **Mexico** or Tunisia, with low-capability states
  and a tradition of political conflict, will handle the same demographic pressures in 30
  or 40 years."*

### 8. Supplemental Material B — the WPP forensics (most load-bearing for DFD)

This is the section that converts our standing "CELADE/WPP medium is the optimistic
scenario" rule from a judgement into a documented mechanism.

**B.1 — Births are overstated against registries.** Table A1, restricted to three
mid-sized countries whose registries **the UN's own Population and Vital Statistics
Report rates ≥90% complete**:

| Country | Year | Official births | UNPD estimate | Overestimate |
|---|---|---|---|---|
| Colombia | 2022 | 573,625 | 710,000 | 23.8% |
| Colombia | 2023 | 515,549 | 705,000 | **36.7%** |
| Egypt | 2022 | 2,192,947 | 2,375,000 | 8.3% |
| Egypt | 2023 | 2,044,880 | 2,406,000 | 17.7% |
| Türkiye | 2022 | 1,041,846 | 1,079,000 | 3.6% |
| Türkiye | 2023 | 963,075 | 1,072,000 | 11.3% |
| **Total** | | **7,331,922** | **8,347,000** | **13.8%** (1,015,078 births) |

**The mechanism of the bias is identified, not merely asserted.** UNPD estimates each
data source's bias relative to a source assumed unbiased; neither that source nor the
covariate set is public. The methodology states that series with ≥98% birth-registration
completeness *since 1950* are treated as unbiased, and that otherwise "the model uses
either the estimates from the previous revision of the World Population Prospects or
some other data source(s) deemed unbiased by the analyst." Liu and Raftery (2020)
recommend the previous WPP revision as that baseline and recommend **time-invariant**
covariates — which by construction rules out improvement in registration quality over
time. So a country moving from ~50% completeness in the 1950s to ~99% in 2024 has its
early-period error carried forward into the present, biasing recent estimates upward
precisely for countries that developed since 1950. From 2019 onward, vital statistics
are the *only* source UNPD uses for Colombian births, yet the gap persists.

**B.2 — Projections mean-revert by assumption.** Once a country enters the UNPD's "low
fertility regime" (entered when, after five-year averaging, two successive increases are
observed below 2.0 births), its TFR follows

> f_{c,t+1} ~ N(μ_c + ρ_c(f_c,t − μ_c), σ²),  μ_c ~ N(μ̄, σ²_μ),  μ̄ ~ U[0, 2.1],  σ_μ ~ U[0, 0.318]

The **U[0, 2.1] prior on the hyper-mean** is what pulls every low-fertility country back
toward replacement. South Korea rises monotonically from 0.72 (2023) to 1.30 (2100),
China from 1.0 to 1.35. Table A3 shows the turn is *immediate* regardless of how fast
fertility has been falling:

| Country | TFR 2018 | TFR 2023 | Δ 2018–23 | TFR 2028 (proj.) | Projected Δ |
|---|---|---|---|---|---|
| China | 1.54 | 1.00 | −0.54 | 1.05 | **+0.05** |
| South Korea | 0.95 | 0.72 | −0.23 | 0.79 | **+0.07** |
| **Chile** | **1.54** | **1.17** | **−0.37** | **1.12** | **−0.05** |
| United States | 1.72 | 1.62 | −0.10 | 1.63 | +0.01 |
| India | 2.18 | 1.98 | −0.20 | 1.90 | −0.08 |

Table A2 is the out-of-sample test: every country with ≥90%-complete 2024 registry data
and population above one million, actual 2024 births against the **July-2024** projection
*for 2024*. Only **4 of 37** came in above projection (Canada +1.3%, Kuwait +2.2%, Bosnia
+2.5%, Croatia +3.4%). Totals **16,052,498 actual vs 17,699,000 projected — −9.3%, a gap
of 1,646,502 births.** LAC rows: Colombia −36.5%, Guatemala −21.2%, Argentina −18.5%,
Panama −17.0%, Chile −10.2%, Uruguay −9.4%, Brazil −7.6%. **Mexico is not in the table.**

The authors add the observation that matters most to us: *"very few economists are aware
of the optimistic assumptions underlying these numbers."*

**B.3 — Successive revisions move down, and not fast enough.** Projected 2100 world
population has gone 11.213bn (2015) → 11.184 (2017) → 10.875 (2019) → 10.349 (2022) →
10.180 (2024); the peak first appeared in the 2022 revision (2086) and moved to 2084 in
2024. Average world TFR for 2025–2030 fell from 2.38 (2019) to 2.22 (2024). Shaving a
billion people off a *stock* in nine years implies an enormous revision to the whole
path of births, all in one direction.

**B.4 — Mexico appears here.** The 1.6-million 2024 gap is expected to be larger in 2026,
"probably on the order of 2.5 million," *"especially given the birth data that arrived
for Egypt, **Mexico**, and the Philippines in 2025, much lower than the WPP projections."*

### 9. Two definitional points worth carrying (Supplemental A)

- **Dependency ratios barely depend on forecasting.** "Everyone who will be 24 or older
  in 2050 has already been born." Old-age dependency and the support ratio are therefore
  far more robust than TFR projections — a direct methodological warrant for DFD's
  practice of reporting the dependency-ratio path alongside every TFR scenario.
- **Tempo, stated plainly.** TFR is used rather than CFR because CFR arrives with a long
  lag; the price is tempo sensitivity (Bongaarts and Feeney 1998). Momentum works through
  the age structure, tempo through the timing of births — the two are distinct and the
  paper keeps them apart.

## Relevance to project work

### DFD

- **Scenario discipline: confirmed, and now mechanised.** The standing rule (CELADE/WPP
  medium = optimistic, fast-transition = central) no longer rests on inference from an
  optimism gap. B.1 gives the estimation bias (carry-forward of pre-1990 registration
  error under time-invariant covariates) and B.2 gives the projection bias (the U[0,2.1]
  hyper-prior forcing immediate mean reversion). Both are citable mechanisms.
- **Chile is the row that moves.** Table A3 documents Chile 1.54 (2018) → 1.17 (2023)
  with WPP projecting 1.12 for 2028. Read against the registry value in the September
  deck (0.99, 2025), the **Stress column's empirical floor of 1.03 no longer holds.** That
  decision is escalated to Héctor in Anne's 2026-09-15 record (her recommendation: declare
  the floor unidentified and carry ~0.9 as a working value; do not anchor to Puerto Rico
  0.87, which is US-linked and emigration-driven).
- **The authors' own LAC forecast is ~1.2.** The conclusion states: East Asia stuck near
  1; *"Latin America faces the same gender problem plus weak growth prospects, so we
  expect something around 1.2"*; Northern Europe near 1.5; only very religious societies
  sustaining 1.8. This sits **below DFD Central (1.50) and above Stress (TFR → 1.0)**.
  Recorded as a scenario-discipline observation, **not** a projection update — no
  cohort-component input moves on this entry (Héctor's ruling, 2026-09-15).
- **Mexico's registration lag is now primary-sourced.** Footnote 3: *"Only about 72% of a
  year's births in Mexico are registered in the year they occur, and the rest are
  registered over the following years. The 2025 figure extrapolates the births registered
  within 2025 to an expected final tally."* This is directly usable for Q4 follow-up 7
  (the occurred-vs-registered wedge) and it means the deck's Mexico 1.51/2025 is an
  **extrapolation**, one step further from an INEGI publication than a registry figure.
- **OLG foundations.** The §5.3 argument that both welfare theorems fail in OLG
  (Samuelson 1958; Shell 1971 on the double infinity) is the theoretical warrant for
  treating replacement as a non-attractor in the DFD framework, and bears on how welfare
  claims are stated in OLG-based deliverables.
- **Growth accounting for the fiscal block.** g_y = g_(y/l) + g_l and the Japan/US swap
  are the cleanest available statement of why a shrinking labour force is a potential-output
  problem, not a demand problem. Route to Cath alongside the IM-6 fiscal transmission.

### BDH

The aging coda is the BDH half. Financing capacity depends on **total output, not output
per capita** — bondholders and retirees are paid in levels — which is the sharpest
available statement of why per-capita improvement does not discharge a health-financing
obligation. The political-economy section (redistribution from workers to retirees as the
first-order problem, and the explicit judgement that Mexico will face Japan's pressures
with a low-capability state and a fraction of the income per capita) is directly usable
in BDH framing. Beth's health-financing work should note the paper contains no
morbidity or health-expenditure content of its own.

### Aurora

"Modernity in its current form seems largely incompatible with replacement-level
fertility" is a structural claim of exactly the Four Pillars type. The Pareto-tail
argument — that growth depending on a handful of exceptional innovators is hurt most by
cohort contraction — is a genuine input to the post-LLM intelligence thread, as is the
closing terra-incognita framing: *"We do not have a map. What we have birth numbers, and
those are sobering. In these waters, the pretense of knowledge is the most dangerous
temptation."*

## Open methodological questions surfaced

- **Goldin (2026) gender mismatch** — opened as a `research_watch_item` by Anne's
  2026-09-15 ruling, on two grounds: the paradoxical-reversal implication bears on the
  Stress floor, and it is the closest rival mechanism to the collapse paper's
  union-composition channel.
- **The LAC ~1.2 landing zone against DFD Central 1.50.** A published expectation from
  the corpus's cornerstone author that sits below our central scenario is a
  scenario-structure question for Anne, not a monitoring note.
- **Mexico's absence from Table A2.** The paper's strongest quantitative WPP indictment
  covers 37 countries but not ours, while B.4 asserts Mexico's 2025 births came in much
  lower than projected. INEGI definitive 2024 births (1,672,227) against the July-2024
  WPP projection for 2024 is checkable and would place Mexico inside the exhibit.
  Endorsed as a Q4 item in Anne's record.
- **The factor model's own caveats, stated by the authors.** β̂ is identified only where
  λ̂ carries local information, and that quantity falls roughly sevenfold between the
  1970s and the 2020s, so late-sample loadings inflate to compensate — which is why the
  paper discusses β̂λ̂ rather than β̂. Time-varying loadings also weaken the separation
  between the linear trend and the common component. Country-level estimates are noisy;
  do not cite an individual country's δ̂ as precise.

## Source quality

- **Reliability:** `primary`. Full methodology, three supplemental materials, and an
  estimation appendix with explicit robustness and bootstrap detail.
- **DOI status.** The paper's own title footnote prints "Paper prepared for Annual
  Reviews of Economics, DOI: 10.1146/annurev-economics-081026-024323." Verified
  2026-09-15: that DOI **does not currently resolve** — 404 at doi.org and unregistered
  at Crossref, with no Crossref record for any author named Norrick. This is consistent
  with a DOI assigned by the publisher ahead of publication. Cite as a working paper with
  the DOI marked pending; do not present it as a published Annual Review article.
- **Local copy provenance.** `sources/FVN_2026-08-10_terra-incognita.pdf`, 61 pp,
  1,339,928 bytes, PDF 1.5, produced by pdfTeX with hyperref, creation timestamp
  2026-08-10 09:53. Retrieved 2026-09-15 from a third-party mirror because the authors'
  Penn listing (`https://www.sas.upenn.edu/~jesusfv/research.html`, the canonical
  location) refuses automated fetches. Authenticity checked against the authors'
  own public description of the paper, the printed date, the abstract, and internal
  consistency. **Replace with a copy pulled directly from the Penn listing when
  convenient**, and verify the hash recorded in the build instruction.

## Citation

Fernández-Villaverde, J. and P. Norrick (2026). *Terra Incognita: The Economics of a
Shrinking World.* Working paper, 10 August 2026, prepared for the *Annual Review of
Economics*; DOI 10.1146/annurev-economics-081026-024323 (assigned, not yet resolvable).
University of Pennsylvania, NBER, CEPR (Fernández-Villaverde) and Northwestern
University (Norrick). Local copy:
`_crossrefs/corpus/demographics/sources/FVN_2026-08-10_terra-incognita.pdf`.

## Cross-references

- → Build instruction: `_crossrefs/_build_instructions/2026-09-15_demographics_terra_incognita_reconstruction.md`
- → Supersedes as standing reference: `_crossrefs/corpus/demographics/2026-06-20_fernandez-villaverde-demographic-future.md` (April deck)
- → LAC-specific presentation of the same research programme: `_crossrefs/corpus/demographics/_pending/2026-09-15_fernandez-villaverde-slides-latam.md`
- → Anne's adjudication establishing this entry as cornerstone of record: `_crossrefs/corpus/demographics/_pending/2026-09-15_FV-LAC-deck_Anne-endorsement.md`
- → Directly rebutted in §6.3: `_crossrefs/corpus/demographics/2026-07-11_baby-busts-growth-booms.md` (Acemoglu, Autor, Beirne and Scott 2026 — the paper argues their identifying variation does not cover today's fertility regimes)
- → Scenario anchors (CHL row implicated; no row changed by this entry): `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Governing instructions (unchanged at v1.4): `_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md`
- → Trigger of record and occurred-vs-registered wedge: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q3_demographic_replicate.md` §2, §7
- → Project corpus cross-refs (append on endorsement, per §Routing):
    - DFD: `GrandPlan/DFD/docs/corpus/_cross_references.md`
    - BDH: `GrandPlan/BDH/docs/corpus/_cross_references.md`
    - Aurora: `GrandPlan/Aurora/docs/corpus/_cross_references.md`

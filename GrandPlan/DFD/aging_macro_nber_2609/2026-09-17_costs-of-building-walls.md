---
title: "Bernardino, Franco & Teles Morais (2026) — The Costs of Building Walls: Immigration and the Fiscal Burden of Aging in Europe"
date: 2026-09-17
added_by: Claude
endorsed_by:
projects: [DFD, Aurora, BDH]
indicators: [composite, migration, projection, tfr]
geography: comparator
scenario_implication: neutral
source_reliability: secondary
data_vintage: 2019
promotion_status: pending-anne
corpus_path: _crossrefs/corpus/demographics/
---

## Summary

Bernardino (IIES Stockholm), Franco and Teles Morais (Nova SBE) build cohort-component
population projections to 2100 for each euro area country, disaggregated by age, gender,
education and country of birth, and combine them with separately estimated age profiles of
taxes and benefits for immigrants and natives. The two components are merged through the
intertemporal government budget constraint and summarised by a single metric, θτ — the
permanent proportional increase in all revenue items needed to restore long-run fiscal
balance, holding demographic profiles fixed ("rebalancing tax increase").

Headline results: baseline θτ of 14% for the EA aggregate (≈5.9% of GDP against current
collections of 42% of GDP). Shutting down extra-EU net migration raises θτ to 16.3%
(≈1% of GDP). Doubling migration from 0.4% to 0.8% of population lowers θτ by only 1.4pp.
Raising native fertility instantly to replacement (2.1) lowers θτ by only 0.7pp. Lifetime
net contributions to the budget are negative for both natives and immigrants in the euro
area; the operative comparison is between an immigrant's lifetime net contribution *from
age of entry* and a native's *from birth*.

The paper's analytical core is Proposition 1: in any cohort-component population with
below-replacement fertility, the dependency ratio at any finite horizon is strictly
decreasing and strictly convex in the working-age migration flow. The authors note this
property is inherited — unacknowledged — by most of the prior literature on the fiscal
effects of immigration.

## DFD Calibration Implications

**Fast-transition TFR scenario for Mexico** — no direct implication for the TFR baseline
itself (European calibration, EUROPOP2019 central path). Indirect but substantive
implication for scenario *interpretation*: Section 4.3 shows that an instantaneous jump in
native fertility to replacement delivers only 0.7pp of θτ relief, against 2.3pp from
maintaining observed migration. The mechanism is timing — higher fertility adds dependents
immediately and contributors only after ~25 years, coinciding with the boomer retirement
wave; dependency ratios and primary deficits are *worse* under high fertility for the first
40 years of the projection. This is an upper-bound scenario for pro-natalist policy and it
still fails. Given that Mexico's transition is faster than Europe's, the timing mismatch is
plausibly worse here, not better. Relevant whenever the fast-transition framing prompts the
question of whether fertility recovery is a policy lever.

**Dependency ratio path feeding IM-6's pension contribution rate** — Proposition 1 is
directly portable and sign-flips for Mexico. As a net emigration country, the mirror result
implies the marginal fiscal cost of working-age emigration is *increasing* in the outflow.
This appears not to have been written down for LAC. Requires no new machinery in the
demographic module; candidate for an original DFD contribution. Needs Anne's endorsement
before treating as established.

**Survival probabilities in the OLG demographic block** — no implication. Mortality is
taken from EUROPOP2019, differs only by age and gender, with life expectancy at birth rising
from ~81 (2019) to ~88 (2100). The authors flag that they cannot condition mortality on
education for most countries and that doing so would likely raise projected dependency
ratios slightly.

**Coupling / partnership formation** — not addressed. Fertility enters as an exogenous rate.

**Methodological — θτ and the IM-6 interface (Cath–Anne).** θτ is a sufficient-statistic
shortcut: no behavioural response, no endogenous factor prices (the capital-stock bias from
fixed prices is patched with the Clemens 2022 adjustment rather than solved), tax-benefit
profiles frozen at the base year. The authors claim robustness to productivity growth and
interest rate assumptions, unlike conventional generational accounting metrics, and verify
this across discount factors (baseline D = 0.986 from 1995–2021 averages: γ = 0.7%,
i = 3.8%, π = 1.68%).

Proposed validation exercise: with behavioural and price adjustment shut down, IM-6's
implied permanent tax adjustment should land near a θτ computed on the same profiles. A
material gap indicates mis-specification in one of the two. Cheap, and informative about
the OLG demographic-fiscal interface.

**Two limits on transferability, both structural.**

1. *Informality is absent.* Demographic profiles are estimated by quasi-saturated regression
   on age, gender, education and country of birth, using EU-SILC (2019), EU HBS (2015) and
   HFCS (3rd wave). In Mexico the age profile of net fiscal contribution is a function of
   age × formality status, with formality itself selected; education is a weak proxy. A
   Mexican θτ requires formality as a fourth conditioning dimension — connects to the
   conditional logit formality-choice work (ENIGH 2022, with Diego). This gap is where DFD's
   contribution sits.

2. *Profile invariance.* θτ assumes tax and benefit profiles are unchanged in perpetuity.
   Mexico is mid-transition on the 2020 pension reform, so the age profile of public pension
   benefit is a moving object by construction. Applying θτ without handling the transition
   would be mis-specification, not simplification.

**Uncertainty treatment.** Constant net migration, deterministic projection, single central
fertility and mortality path, no bands reported on θτ. Standard practice in the literature
and a departure from DFD's first-order-uncertainty principle. Worth noting explicitly when
citing.

## Project Routing Notes

**Aurora.** Second-order but genuine structural watch item: if euro area fiscal
sustainability depends on sustained working-age inflows while European migration politics
moves toward restriction, the resulting tension is a structural force with remittance and
emigration-pressure consequences for LAC as an origin region. The paper's cross-country
results sharpen this — migration relieves the fiscal burden in France, Germany, Italy and
Spain, but the relationship reverses in Belgium, the Netherlands and Ireland (immigrants'
lifetime contributions below newborn natives') and in Lithuania and Estonia (arrival age
above 30). Heterogeneity of this kind makes common EU migration policy hard to sustain,
which is itself the political-economy mechanism Aurora would track. Route to Elle and Gina.

**BDH.** Thin but non-zero: public health and education expenditure sit inside the
expenditure profiles g and the age gradient of health spending contributes to the θτ path.
Not a priority read. The transferable question is how the age profile of public health
expenditure interacts with the dependency ratio under a faster transition.

**CROSS-TAR-001.** "Rebalancing tax increase" (θτ) and "stationary-through-immigration (SI)
population" (Espenshade, Bouvier & Arthur, 1982) are candidate terminological anchor
entries if θτ is adopted or benchmarked against IM-6.

## Open Items Requiring Anne's Authority

1. Whether the emigration-convexity corollary of Proposition 1 is genuinely novel for LAC,
   and whether it warrants a standalone note or paper.
2. Whether θτ is adopted as a DFD reporting metric, used only as an IM-6 validation
   benchmark, or set aside.
3. Whether the fertility-is-not-an-alternative result is strong enough to cite as settled in
   DFD policy-facing output, given it is calibrated to a slower European transition.

## Source

Bernardino, Tiago (IIES, Stockholm University); Franco, Francesco (Nova SBE); Teles Morais,
Luís (Nova SBE). "The Costs of Building Walls: Immigration and the Fiscal Burden of Aging in
Europe." May 2026. JEL: E62, F22, H55, J11. Keywords: Public Finances; Migration; Aging;
Europe. Discussants acknowledged: Jesper Böjeryd, Michael Clemens, Karen Dynan. Cites
Fernández-Villaverde (2025) and Weil (2023) on the persistence of below-replacement
fertility; Blanchard (1990) on θτ as a sustainability indicator; Bonin, Patxot & Souto
(2014) and Girouard & André (2006) on cyclical adjustment; Clemens (2022) on the fixed-price
capital stock correction; Preston (2014) for a review of the prior literature.

Obtained in connection with the NBER virtual conference on the macroeconomic effects of
population aging (Auclert et al.), September 2026.

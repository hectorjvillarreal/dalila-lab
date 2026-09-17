---
title: "Giannone, Miyauchi, Paixão, Pang & Suzuki (2026) — Living in a Ghost Town: The Geography of Depopulation and Aging"
date: 2026-09-17
added_by: Claude
endorsed_by:
projects: [DFD, BDH, Aurora]
indicators: [migration, projection, composite]
geography: comparator
scenario_implication: neutral
source_reliability: secondary
data_vintage: 2015
promotion_status: pending-anne
corpus_path: _crossrefs/corpus/demographics/
---

## Status Note

This is the **Giannone et al. (2026)** paper recorded as an acquisition pointer in
`2026-09-17_spatial-consequences-depopulation.md`. It **estimates the candidate workstream
proposed in that note** — subnational fiscal stress under demographic decline — and does so more
rigorously than the proposal. That suggestion is now superseded by an identified result.

Assessed as among the three most DFD-relevant of the nine papers filed 2026-09-17, alongside
Benzell-Kotlikoff-Ye and Kotschy-Bloom, and for a distinct reason: it is the only one carrying
**local public finance** as a modelled object.

## Summary

Elisa Giannone (CREI, UPF), Yuhei Miyauchi (Boston University), Nuno Paixão (Bank of Canada),
Xinle Pang (Buffalo) and Yuta Suzuki (Hitotsubashi) combine spatially disaggregated Japanese
municipality data over four decades with a dynamic life-cycle spatial general equilibrium model
to study how depopulation and aging diverge *within* a country.

Central finding: **aggregate population decline does not imply spatial convergence.** Younger
cohorts and births become increasingly concentrated in large cities even as national population
contracts, through a self-reinforcing loop — young migrate to cities, the reproductive-age
population concentrates, births concentrate, concentration accelerates.

## Empirical Results (the transferable part)

Identification: push-and-pull migration shocks originating in *other* municipalities (Boustan
2010; Derenoncourt 2022; Bazzi et al. 2023), instrumenting working-age population change and
elderly share change.

| Outcome | Effect of +1% working-age population |
|---|---|
| Municipal government spending per capita | **−0.53%** (economies of scale in local public services) |
| Personal income tax per capita | **No significant response** |
| Amenity indices (child/education, elderly services, environment/transport, health/medical, retail) | All positive and significant — amenities decline where working-age population is lost |
| Land prices, number of residences | Positive and significant |

**The authors' conclusion, quoted in substance: population decline widens local fiscal deficits —
per-capita spending rises as regions shrink while per-capita tax revenues do not, and the growing
fiscal gap increases reliance on transfers from the national government.**

The amenity result spans market-supplied (retail), government-supplied (schools, libraries,
parks, roads) and mixed or subsidised provision (hospitals, elderly-care facilities) alike.

Elderly share on its own: mostly insignificant for spending; negative and marginally significant
for personal income tax per capita, consistent with lower taxable income among elderly residents.

## Model and Projection

Dynamic life-cycle spatial GE: forward-looking migration across locations on wages, amenities,
housing costs and migration costs; wages and amenities endogenous through agglomeration
externalities; births occur in the parent's current location. **A national government levies
labour income tax to finance elderly pensions and the required level of local public services,
which vary with local population size**, with the tax rate κt set to satisfy the government
budget constraint.

Calibration: public service cost elasticity with respect to population γg = **0.72**; aggregate
government spending 20% of aggregate labour income in 2015 (Japanese data).

Projection to 200 years: Tokyo's share rises from ~10% (2015) to ~26%. Elderly share in Tokyo
stays below 35%; in the five oldest prefectures it approaches **60%**. Amenity-adjusted real
income diverges rather than converges.

**Both channels are necessary.** Shutting down internal migration, *or* fixing the spatial
distribution of newborns at 2015, leaves regional population shares constant and elderly shares
converging. Neither alone generates the divergence. Both counterfactuals also *reduce* aggregate
per capita income and *raise* per capita fiscal spending, by retaining population in less
productive, more costly-to-serve locations.

## Policy Experiment and Its Relation to de Silva & Paron

Transfers of 5% of income for 100 years to the five oldest prefectures, financed by taxes on
Tokyo residents:

- Population of those prefectures in 2065 nearly **doubles** relative to baseline
- Elderly share there falls from 45% to about **33%**
- Their real income rises about **10%** — more than the 5% transfer, through agglomeration
  amplification
- Tokyo income falls about **3%** (smaller, larger population base)
- Nationally: aggregate labour income per capita falls **>1%**; aggregate fiscal spending rises
  **~0.5–0.7%**

**Better posed than the de Silva & Paron planner result.** They quantify an efficiency–equity
trade-off rather than asserting a welfare optimum. The two are compatible: place-based support
for declining regions achieves its redistributive purpose and costs aggregate output and fiscal
resources. Whether the trade is worth making is left as a policy judgment.

## DFD Relevance and Mexican Transferability

**Structurally closer to Mexico than most of the set.** A national government financing
subnational service provision, with thin municipal own-revenue, is the Mexican arrangement.

**The revenue result should be *stronger* in Mexico.** Japanese municipalities have a real
own-revenue base whose non-response to population change is the finding; Mexican municipios
collect very little *predial* to begin with, so per-capita own revenue has even less capacity to
respond.

**The mechanism maps onto the transfer formulas directly.** *Participaciones* (Ramo 28) are
largely population-weighted; *aportaciones* (Ramo 33) are earmarked for education, health and
infrastructure — exactly the functions whose per-capita cost this paper shows rising as
population falls. A population-weighted formula against a non-proportional cost function is the
fiscal-sustainability question.

**One Mexican feature wholly absent from the model — proposed as an original DFD line.**
Japanese rural municipios lose working-age population to Tokyo. Mexican rural municipios lose it
to Monterrey *and* to the United States simultaneously. That doubles the outflow and introduces
**remittances** as a substituting income stream that supports local consumption while generating
essentially no local fiscal capacity and no contributory pension accrual.

The Mexican ghost-town problem is therefore sharper than the Japanese one: population leaves
through two doors, per-capita service costs rise, own revenue does not, and the income flowing
back is fiscally invisible. This connects the subnational fiscal question to the
emigration-convexity corollary (Bernardino et al.) and to the informality thread running through
the whole set. **Requires Anne's and Cath's assessment before being treated as more than a
conjecture.**

## Caveats

- **Japan is a unitary state with high internal mobility and no meaningful international
  emigration.** All three differ in Mexico, and the third is not a detail — the model has no
  international migration at all.
- 200-year horizon extrapolated from a 2015 calibration. The qualitative divergence result
  survives the counterfactual shutdowns, but the level projections are a long reach.
- No informality, and no distinction between contributory and non-contributory pension pillars.
- Amenity response is reduced-form (endogenous to local market size), following Diamond (2016).

## Project Routing Notes

**BDH.** Substantial. The health/medical amenity index declines significantly with working-age
population loss, and the minimum-viable-scale problem for rural clinics and elderly-care
facilities is directly a health-system-geography question. Combined with Kotschy & Bloom on
functional capacity, BDH now has two strong spatial/health items from this set. Route to Beth.

**Aurora.** Secondary. Spatial divergence persisting and intensifying *under* aggregate decline
overturns the intuition that shrinkage equalises, and the place-based policy trade-off is
politically live everywhere. Route to Elle.

**CROSS-TAR-001.** "Ghost town" / municipal extinction (Masuda 2014) and the
economies-of-scale-in-local-public-services elasticity are candidate anchor entries if the
subnational workstream is taken up.

## Source

Giannone, Elisa (CREI, Universitat Pompeu Fabra); Miyauchi, Yuhei (Boston University); Paixão,
Nuno (Bank of Canada); Pang, Xinle (University at Buffalo, SUNY); Suzuki, Yuta (Hitotsubashi
University). "Living in a Ghost Town: The Geography of Depopulation and Aging." September 2026,
71pp. JEL: E62, J11, O18, R12, R13, R23. Keywords: depopulation; population aging; internal
migration; local amenities; local public finance; spatial inequality; place-based policies.
Related Japanese OLG work cited: Braun and Joines (2015), Kitao (2015), Kitao and Mikoshiba
(2020) — nationwide aging and fiscal policy, abstracting from regional heterogeneity. Place-based
policy literature: Fajgelbaum and Gaubert (2020), Gaubert et al. (2021), Donald, Fukui and
Miyauchi (2025, 2026).

Filed alongside the NBER aging-conference series of 2026-09-17; see
2026-09-17_nber-aging-conference-synthesis.md. Supersedes the workstream proposal in
2026-09-17_spatial-consequences-depopulation.md.

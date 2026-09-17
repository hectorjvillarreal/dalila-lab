---
title: "de Silva & Paron (2026) — Making Room on an Empty Planet: The Spatial Consequences of Depopulation"
date: 2026-09-17
added_by: Claude
endorsed_by:
projects: [DFD, Aurora]
indicators: [projection, tfr]
geography: comparator
scenario_implication: neutral
source_reliability: secondary
data_vintage: 2023
promotion_status: pending-anne
corpus_path: _crossrefs/corpus/demographics/
---

## Relevance Assessment — Read This First

**This is the most peripheral of the eight papers filed on 2026-09-17 for DFD's core question.**
No fiscal system, no pension system, no age structure (deliberately excluded — the paper isolates
population *level* from age composition), Japanese calibration, Mexico absent. **It changes
nothing in the existing corpus and does not bear on IM-6 calibration.**

Its value is (i) one candidate new workstream, (ii) one further instance of a pattern now
recurring across the set, and (iii) one appendix result bearing on fast-transition discipline.
Filed `pending-anne` because the workstream suggestion needs her judgment, not because the
paper is a priority.

## Summary

Tim de Silva and James D. Paron (Stanford GSB) study how population decline reshapes the spatial
distribution of economic activity. Mechanism: land is in fixed supply, so housing is what forces
people to spread out; when national population falls, housing becomes less scarce everywhere but
disproportionately so in ex-ante dense areas, driving migration inward and raising spatial
concentration.

Theoretical contribution is a clean negative result: in a wide class of spatial equilibrium
models, population shares are invariant to the population *level* if and only if both housing
supply and demand are Cobb-Douglas — the prevailing assumption (Helpman 1998; Allen and Arkolakis
2014; Ahlfeldt et al. 2015; Caliendo et al. 2019; Kleinman et al. 2023) — which implies
depopulation has no spatial consequences at all. Scale dependence in the observed direction
requires housing supply elasticities falling with density or expenditure shares rising with
density, both empirically supported (Saiz 2010; Baum-Snow and Han 2024; Combes et al. 2019;
Finlay and Williams 2025). Implemented via CES housing production with substitution elasticity
below one, and PIGL demand.

Empirics: across and within countries (Global Human Settlement Layer), national population
changes are negatively correlated with changes in spatial concentration, robust to controls for
structural transformation, old-age dependency, and GDP growth.

Japanese quantification: **Tokyo's population share rises from 10% to 40%** in the long run; its
population falls 12M → 4M rather than 12M → 1M under scale independence. Wages fall 5% in Tokyo
against 25% in Hokkaido. Concentration rises in *anticipation* of decline (moving frictions),
accounting for roughly a quarter of observed 2000–2020 changes without any change in model
primitives.

## The One Finding That Connects to the Running Cross-Paper Thread

**Aggregate GDP per capita rises 27% in the long run** (against a 12% fall under scale
independence), because population reallocates toward higher-productivity places.

Simultaneously, the spending-commitments extension has **tax rates rising most in the less dense
prefectures**, which have fewer residents to finance previously committed local public goods
(parks, schools, firefighters). This amplifies population-share and house-price responses prior
to the actual decline by around 15%.

Aggregate GDP per capita up, subnational fiscal stress up, for connected reasons. This is the
sixth or seventh instance across the 2026-09-17 set of growth results and fiscal results
answering different questions. **At this point it is a structural feature of how this literature
is constructed rather than a paper-by-paper caveat, and it is the principal reason DFD's premise
survives a literature that mostly reports good news.**

## Candidate New Workstream (for Anne and Cath to accept or reject)

**SUPERSEDED — see `2026-09-17_ghost-town-geography-depopulation-aging.md`.** Giannone, Miyauchi,
Paixão, Pang & Suzuki (2026), filed the same day, estimate this mechanism directly on Japanese
municipality data: a 1% rise in working-age population lowers municipal government spending per
capita by 0.53%, while personal income tax per capita shows no significant response. Population
decline therefore widens local fiscal deficits and raises reliance on national transfers. The
proposal below is retained for the record; the Giannone note is the operative document.

Mexican fiscal federalism distributes *participaciones* and *aportaciones* on largely
population-based formulas. If depopulation concentrates population spatially, transfers
redistribute mechanically — but the cost of service provision in emptying municipios does not
fall proportionally: minimum viable scale for a school or clinic, fixed infrastructure, and
committed obligations do not shrink with the population served.

A fiscal-sustainability question with a demographic driver, currently unasked in DFD, and Mexico's
internal heterogeneity is extreme enough to make it live. **A suggestion, not a finding.**

**Two reasons for caution on transferability:**

1. The mechanism runs entirely through housing supply elasticity responding to population.
   Mexican rural land tenure — particularly **ejidal and comunal** holdings — does not behave as a
   market in land and structures. The mechanism may be substantially muted precisely where it
   would matter most.
2. Japan is a high-mobility, effectively unitary state with an extreme density gradient. Mexico
   differs on internal mobility, federal structure, and housing-market institutions.

## Result Worth Knowing Exists

A utilitarian social planner maximising average household utility wants budget-neutral transfers
**from sparse regions to dense ones**, and wants to increase them as aggregate population falls.
Optimal transfers balance an agglomeration externality (tax Hokkaido) against redistribution (tax
Tokyo); in the dynamic model, moving costs add a force favouring migration toward
higher-average-utility regions, and scale dependence amplifies it.

This is the opposite of essentially every existing depopulation policy — Japanese akiya banks and
renovation grants, Italian and Spanish one-euro home schemes, Scotland's Addressing Depopulation
Action Plan — and the opposite of the standing logic of Mexican regional development policy.

Whether the utilitarian average-utility criterion is the right one is a separate question, and
the authors note the planner may want to move more slowly along the transition to protect
households temporarily locked into declining regions. But the result is strong, from Stanford
GSB, and will surface in policy argument. **Recorded so DFD is not met with it cold.**

## Appendix Result Bearing on Fast-Transition Discipline

Appendix F.5 endogenises fertility through housing (households have more children as housing
supply expands; Lovenheim and Mumford 2013; Dettling and Kearney 2014; Fazio et al. 2025). The
result is asymmetric in the housing production function:

- **Cobb-Douglas:** per-capita housing supply rises without bound as population falls → birth
  rates recover → population stabilises at a positive level.
- **CES with η < 1** (their preferred, better-supported specification): per-capita housing supply
  is **bounded above**, because structures become the binding constraint → **the birth rate may
  never rise enough to stabilise the population, which can eventually fall to zero.**

A housing-based fertility-recovery mechanism that fails under realistic parameters. A small point
in a long appendix, but it bears on fast-transition discipline: one of the more plausible
endogenous stabilisers does not stabilise. Worth Anne's attention alongside the Jones (2022a)
declining-population line that Pettersson explicitly set aside.

## Further Limitations

- Aging is deliberately excluded. The authors justify this on the grounds that the
  population-concentration relationship holds conditional on age distributions, and that with
  stabilised vital rates the age distribution converges while the population level keeps falling
  (citing Weil 2026). They acknowledge the aging channel as complementary and important, citing
  **Giannone et al. (2026)** on Japanese aging reducing amenities in sparse areas through
  out-migration of more mobile young workers.
- No fiscal system in the baseline; public goods enter only as an extension.
- Amenity spillovers: a negative elasticity at the median of existing estimates dampens but does
  not overturn the result (Tokyo's share still doubles); a positive elasticity, which Giannone et
  al. find for Japan, strengthens it.

## Project Routing Notes

**Aurora.** Secondary but real: depopulation as a spatial-restructuring force operating on the
same century timescale as the technological drivers, with a policy prescription that runs against
prevailing political commitments in every country studied. The gap between the welfare-optimal
and politically feasible spatial response is Aurora's kind of tension. Route to Elle.

**BDH.** No direct relevance, though the minimum-viable-scale problem for rural clinics is
adjacent to health-system geography if the workstream above is taken up.

## Acquisition Pointers

- **Giannone et al. (2026)** — aging and spatial amenity decline in Japan. The aging-side
  complement to this paper's population-level mechanism; would be the more DFD-relevant of the
  two.
- **Geruso and Spears (2026)**, cited in the opening line on below-replacement fertility and
  expected rapid decline.
- **Weil (2026)** on capital accumulation and the stable age distribution under continuing
  population decline.

## Source

de Silva, Tim; Paron, James D. (both Stanford Graduate School of Business). "Making Room on an
Empty Planet: The Spatial Consequences of Depopulation." 21 August 2026, 126pp. First draft June
2026. Data: Global Human Settlement Layer; Japanese prefecture-level data; regional housing supply
elasticities from Baum-Snow and Han (2024). Acknowledgments include Adrien Auclert, Adrien Bilal,
Jesús Fernández-Villaverde, Chad Jones, Arvind Krishnamurthy, Hanno Lustig, Monika Piazzesi, Steve
Redding, Martin Schneider, Chris Tonetti, Stijn Van Nieuwerburgh.

Filed alongside the NBER aging-conference series of 2026-09-17; see
2026-09-17_nber-aging-conference-synthesis.md.

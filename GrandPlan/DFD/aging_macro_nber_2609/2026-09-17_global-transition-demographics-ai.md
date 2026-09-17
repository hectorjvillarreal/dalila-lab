---
title: "Benzell, Kotlikoff & Ye (2026) — The Global Transition: The Impact of Demographics and AI on Economic Power"
date: 2026-09-17
added_by: Claude
endorsed_by:
projects: [DFD, Aurora, BDH]
indicators: [tfr, projection, migration, composite]
geography: mexico
scenario_implication: neutral
source_reliability: secondary
data_vintage: 2024
promotion_status: pending-anne
corpus_path: _crossrefs/corpus/demographics/
---

## Summary

Seth Benzell (Chapman, MIT IDE, Stanford Digital Economy Lab), Laurence Kotlikoff (Boston
University, NBER) and Victor Yifan Ye (Stanford Digital Economy Lab) deploy a multi-region
dynamic life-cycle general equilibrium model — 17 regions covering 150+ countries and 99% of
world population, three labour skill groups, internationally mobile capital, region-specific
fiscal policy and TFP growth, idiosyncratic mortality, agents living to 100 as children,
workers and retirees, CES preferences over work and saving, no annuities apart from state
pensions (so bequests are unintended). Each region decides annually whether to adopt its
frontier automation technology. Over three million equations. Directly in the Auerbach-Kotlikoff
lineage (Fehr, Jokisch & Kotlikoff; Benzell et al. 2021, 2025).

The experiment compares UN WPP **2017** against **2024** demographic vintages, plus three AI
scenarios: BAU, Accelerating (4× recent growth in capital's share through 2050) and
Transformative (10×).

**Assessed as the most DFD-relevant paper of the six NBER-conference acquisitions.** It is the
only one carrying, simultaneously: a Mexico region, an explicit payroll-tax and pension-outlay
result, and endogenous automation adoption. It is the closest thing in the set to a competitor
or complement for IM-6.

**Regional disaggregation is unusually good for our purposes:** MEX (Mexico alone), BRA (Brazil
alone), and SLA (Latin America excluding Mexico and Brazil) are separate regions. Latin America
is not a rest-of-world composite.

## Headline Fiscal Results (base case: benefits per retiree fixed relative to per-capita GNI)

| | 2017 | 2050 | 2100 |
|---|---|---|---|
| World payroll tax rate (% covered payroll) | 13.1 | 21.7 | **25.4** |
| World pension outlays (% GDP) | 5.8 | 9.5 | **11.9** |
| World effective average tax burden (% total income) | 31.4 | 36.0 | **40.8** |

Regional: China's payroll rate 10.7% → 38.1% and pension outlays 4.9% → 15.1% of GDP under the
2024 vintage (against 28.1% and 11.1% under 2017) — the authors suggest a four-point-of-GDP
difference in permanent pension cost arising purely from revised fertility goes a long way to
explaining China's 2024 pension reform. US 2100 payroll rate rises only 27.7% → 28.2%, because
the 2024 vintage offsets lower fertility with substantially higher immigration. Western Europe's
effective average tax burden reaches 56.7%; the US 47.0%.

**This is the fiscal magnitude the other five papers omit or reach only partially. It belongs in
the corpus as the reference point for what ageing does to contributory systems.**

## Mexico-Specific Findings

**1. Mexico never automates under BAU, and adopts only in 2097 under 2024 demographics combined
with Accelerating or Transformative AI (Tables 14 and 18).** It is the marginal case in the
whole sample — the sole exception to the rule that never-adopters under one demographic vintage
are never-adopters under the other.

Mechanism: regions adopt when the frontier technology (more capital, more high-skill labour,
less low-skill labour) beats the legacy technology at equilibrium factor prices. Mexican labour
is too cheap for adoption to pay.

**Consequence for a prior DFD hypothesis.** The informality-blocks-automation hypothesis
recorded in `2026-09-17_baby-busts-growth-booms.md` reaches the same conclusion by a different
route; this model has no informality at all and still finds Mexico does not automate, on wage
levels alone. Two independent mechanisms, one conclusion. This **strengthens** the finding that
the Acemoglu automation channel is unavailable to Mexico, and **narrows** the claimed
originality of the informality argument: informality is an additional reason, not the reason.
Anne should weigh this before the hypothesis is developed further.

**2. Mexico's world GNI share falls despite a rising population share.** Table 9 under 2017
demographics: 2.1% (2017) → 1.9% (2050) → **1.3% (2100)**. The paper's general explanation is
that never-adopting regions lose share because advanced economies adopting frontier methods
compete away internationally mobile capital. Sub-Saharan African per capita GDP falls from 5.9%
of the US level to 4.6% by 2100 under 2024 demographics, and to 1.6% under TAI.

**Both ageing and transformative AI widen the divide between the richest and poorest regions.**

**3. Mexico's payroll burden is revised *downward* between vintages.** The paper states that
regions whose populations were revised upward between WPP 2017 and WPP 2024 see burdens fall,
naming a ~2.7pp decline in MENA and roughly a point in Canada/Australia/New Zealand **and
Mexico**.

## The Tension With Kopecky — Open Question for Anne and Cath

`2026-09-17_aging-realignment-world-trade.md` (Kopecky, same conference) puts Mexico on the
winning side: exports to the US +27% by 2050 on demographics alone, average Mexican goods worker
+31%, Mexican welfare +36%.

This paper has Mexico's world output share falling by roughly a third over the century.

The two are not strictly contradictory. Kopecky holds technology and capital fixed and measures
trade volumes; Benzell-Kotlikoff-Ye have endogenous automation and internationally mobile
capital, and Mexico loses the capital competition precisely because it does not adopt. But the
mechanism separating them is exactly the one DFD cares about.

**Which is right about Mexico turns on whether capital mobility and frontier adoption dominate
workforce size.** This is answerable, central to DFD, and proposed as a priority item.

## Scenario-Discipline Question Requiring Anne's Authority

The Mexico downward revision in payroll burden implies the UN revised Mexico's population
**upward** from WPP 2017 to WPP 2024. This runs against the fast-transition discipline, which
holds that UN and CELADE medium variants are optimistic for Mexico.

Concrete question, answerable from data already held: **what TFR path does WPP 2024 medium
assume for Mexico; how does it compare to observed values (~1.55) and to CELADE; and in which
direction did the 2017→2024 revision move Mexico?**

If the UN revised Mexico up while observed TFR sits near 1.55, then either the discipline needs
a Mexico-specific defence, or this paper's Mexican results (and Kopecky's) are optimistic in the
same way. **Not resolved here in either direction.** Flagged as `baseline-revision` in the
frontmatter on that basis — the classification is provisional pending Anne's determination.

## Pension Closure — the Quantification the Methodology Item Needed

This note's two predecessors argued that the pension closure/indexation rule is a determinant of
results rather than a technical convention (Pettersson closes through the contribution rate;
Krueger, Ludwig & Popova through the replacement rate). Table A16 quantifies it:

- World 2100 payroll rate: **25.4% with GNI-indexed benefits** against **19.7% under official
  (legislated) projections** — a 5.7-point gap from the indexation rule alone.
- And it is not free: preserving generosity runs world GDP ~2% below the official-projection
  path in 2050 and ~2.5% below by 2100, as payroll and income taxes crowd out labour supply and
  young workers' saving.

From a model in IM-6's own lineage. Proposed as the supporting citation for the
methodology-principles item on pension closure.

## Other Sensitivities Worth Recording

- **US immigration:** eliminating all future US immigration drops the US 2100 world GDP share
  from 14.4% to **9.2%**.
- **Low-fertility variant:** under the UN low variant, 2100 world output is **one third** lower
  rather than one tenth.
- **Capital glut:** both vintages produce a major global capital glut and very low long-run real
  capital returns.
- **Hegemony:** China's 2100 world GDP share falls from 25.6% (2017 vintage) to 14.9% (2024
  vintage) while the US rises from 11.2% to 14.4%. Under TAI plus 2024 demographics: US 25.3%,
  China 16.9%, with the US share doubling from its BAU path by 2050. Capital flows to
  technology, and on their calibration the US retains a technological edge over China throughout
  the century despite considerable Chinese catch-up.

## Project Routing Notes

**Aurora.** Now the second-most Aurora-relevant paper after Acemoglu, and arguably the most
usable, because AI enters as a calibrated scenario (4× and 10× capital-share growth) rather than
as a mechanism to be inferred. Economic hegemony is decided by technological edge plus capacity
to attract mobile capital. The immigration and low-fertility sensitivities above are directly
Gina's and Elle's material. Route to both.

**BDH.** The pension-outlay path (5.8% → 11.9% of world GDP) and the indexation-rule
quantification are relevant to health and pension financing analysis, though health spending is
not separately modelled. Route to Beth as secondary.

**CROSS-TAR-001.** "Frontier technology adoption" as used here is a specific
relative-factor-price decision rule, not a general notion of technological diffusion. Candidate
anchor entry if the Mexico non-adoption result enters DFD output.

## Source

Benzell, Seth G. (Chapman University, MIT Initiative on the Digital Economy, Stanford Digital
Economy Lab); Kotlikoff, Laurence J. (Boston University and NBER); Ye, Victor Yifan (Plaid,
Stanford Digital Economy Lab). "The Global Transition — The Impact of Demographics and AI on
Economic Power." 13 August 2026, 56pp. Model is an updated Benzell et al. (2021), extending
Benzell et al. (2025); lineage includes Auerbach and Kotlikoff (1981, 1983, 1987), Fehr, Jokisch
& Kotlikoff (2003, 2013), Altig et al. (2001). Adoption rule per Zeira (1998). Data: UN WPP 2017
and 2024, IMF fiscal data, World Bank fossil-fuel data.

Obtained in connection with the NBER virtual conference on the macroeconomic effects of
population aging (Auclert et al.), September 2026. Sixth of the series. See
2026-09-17_nber-aging-conference-synthesis.md for the cross-paper argument.

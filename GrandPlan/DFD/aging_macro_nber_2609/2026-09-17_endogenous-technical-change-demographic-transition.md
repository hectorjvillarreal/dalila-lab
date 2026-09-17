---
title: "Pettersson (2026) — Endogenous Technological Change Along the Demographic Transition"
date: 2026-09-17
added_by: Claude
endorsed_by:
projects: [DFD, Aurora, BDH]
indicators: [mortality, projection, composite]
geography: comparator
scenario_implication: neutral
source_reliability: secondary
data_vintage: 2024
promotion_status: pending-anne
corpus_path: _crossrefs/corpus/demographics/
---

## Summary

Markus Pettersson (Stockholm University) embeds R&D-driven semi-endogenous growth (Romer 1990
variety expansion, Jones 1995 idea production) into a rich Auerbach-Kotlikoff OLG model with
endogenous retirement, intensive-margin labour supply, idiosyncratic income risk, borrowing
constraints, warm-glow bequests, progressive income taxation and a PAYG social security system.
Household savings are allocated between physical capital and patent purchases, with no-arbitrage
equalising returns. The mechanism: ageing raises the saving rate (more middle-aged savers,
longer expected retirement), and those savings finance R&D. Because technology is nonrival it
raises everyone's productivity rather than only productivity per effective worker, so it
dominates capital deepening.

Calibrated to the US over a 1950–2100 transition (initialised from an artificial 1900 steady
state, with pre-1950 moments as calibration targets so post-1950 outcomes are predictions):
the demographic transition adds 0.33pp to annual per-capita growth to 2000 and 0.16pp overall,
cumulating to output per capita 27.5% higher by 2100 — roughly 15–20% of observed US post-war
growth, comparable to the contribution of rising educational attainment per Fernald and Jones
(2014). TFP contributes three to four times more than capital deepening.

The decisive exercise is Section 6.4. Exogenous technology is a nested special case (ρ = 1,
δz = 0). Under it the same demographic transition produces a **12.2% cumulative decline** in
output per capita, almost exactly Krueger and Ludwig's (2007) 12.6%. A ~40-point swing turns on
whether the TFP channel is present.

> **Metric caution (Cath, 2026-09-17).** Cumulative and annualised changes in output per capita
> reported here are the paper's own measures. They are not consumption-equivalent variation and
> **must not be carried into DFD output as welfare results**.

## DFD Calibration Implications

**This is the most directly IM-6-relevant of the four NBER-conference papers, because it is the
same model class with one additional block rather than a different framework or a reduced
form.** If IM-6 has exogenous TFP — the standard choice — it sits in the pessimistic branch by
construction, and Section 6.4 quantifies what that choice costs. **Requires Cath's confirmation
of how TFP enters IM-6.**

**The single most useful result for DFD's project premise.** Pettersson resolves the ambiguity
left by Acemoglu, Autor, Beirne & Scott (filed same day), who find growth-positive effects and
are silent on public finance. Pettersson carries both channels in one consistent model: output
per capita rises 27.5% **and** the social security contribution rate rises from roughly 4% to
roughly 22.5% by 2100 (Figure F.3d). Growth optimism and fiscal pessimism are answers to
different questions, demonstrated here inside a single framework rather than asserted. This is
the cleanest available defence of DFD's premise, and it comes from a paper whose headline is
growth-optimistic.

**Fast-transition TFP scenario for Mexico** — no direct implication for the TFR path, but a
sharp interaction (see limit 1 below). The paper's transition is fertility- and mortality-driven
with imposed zero population growth in both terminal steady states.

**Survival probabilities in the OLG demographic block** — mortality is central here rather than
incidental. Rising survival above age 50 is one of the two salient post-war forces, and drives
most of the change in capital intensity and the employment rate. Counterfactual decomposition of
the 27.5% level gain: 8.2% from the baby boom, 3.0% from 50+ mortality change, 14.7% from other
demographic factors (chiefly the non-stationary 1950 population and population size growth).

**Pension closure (candidate for methodology-principles).** Pettersson closes social security
through the **contribution rate** with a fixed replacement rate, explicitly calling this "the
most growth-pessimistic arrangement" since it both taxes working households more and preserves
generous benefits, weakening ability and incentive to save. Krueger, Ludwig & Popova close
through the **replacement rate**, and the falling replacement rate is part of what generates
their education response. Opposite closures at the same conference, each doing analytical work
in the direction of its paper's mechanism.

The lesson: in demographic-fiscal OLG models the pension closure rule is a determinant of the
result, not a technical convention, and any paper not reporting sensitivity to it should be read
accordingly. Directly applicable to IM-6, where Mexico's closure is genuinely ambiguous given a
defined-contribution system plus an expanding non-contributory pillar (Pensión para el
Bienestar).

## Three Limits on Transferability

1. **Two-thirds of the mechanism is a population-scale effect, and Mexico's population is
   heading the other way.** The 72% TFP rise decomposes into an 18% increase in R&D intensity
   and a **47% increase in scale** — the standard semi-endogenous effect whereby a larger
   population supports more aggregate R&D, and nonrivalry means output per capita depends on
   total TFP rather than TFP per head.

   The majority of the effect therefore requires a growing population. Pettersson's footnote 4
   states that he abstracts from Jones (2022a) — persistently low fertility producing a
   declining population — calling it "an important but ultimately separate issue." It is not
   separate for DFD; it is the baseline. Under fast-transition discipline Mexico converges to
   sustained sub-replacement fertility and eventual population decline, which **reverses** the
   scale effect. The R&D-intensity channel survives; the scale channel becomes a drag.

   Net of scale: roughly an 18% TFP gain against a 22% fall in the employment rate. The sign is
   no longer obvious.

2. **The frontier assumption is disclaimed by the author.** He justifies the US focus as "a
   large frontier economy where the endogenous growth framework arguably provides a better
   description of technological change than in smaller economies that primarily adopt foreign
   technology." An explicit statement that the model does not describe Mexico. For an adopting
   economy the relevant channel is absorptive capacity and access to foreign technology, not
   domestic savings financing domestic R&D. The closed-economy assumption compounds this: for a
   small open economy domestic savings need not equal domestic investment, breaking the
   savings–R&D link entirely. (Pettersson justifies closure via Krueger and Ludwig's finding of
   modest open/closed differences, while citing Bárány, Coeurdacier & Guibaud 2023 and Auclert
   et al. 2025 on capital flows in an ageing world.)

3. **The savings–longevity link may be absent in Mexico.** The mechanism's empirical anchor
   (Figure 1) is an OECD panel 1970–2020: a one-year rise in adult life expectancy raises the
   gross saving rate by 0.70pp and IPP investment by 0.20pp, conditional on country fixed
   effects, relative prices and dependency rates; the model reproduces 0.57 and 0.15 untargeted.
   But the life-cycle motive presupposes that longer expected retirement produces private
   accumulation. With over half the Mexican workforce outside contributory retirement saving,
   and a non-contributory pillar weakening the motive further for those it covers, the
   mechanism may be absent before either prior objection bites. **The most testable of the three
   and closest to data already available.**

## Honest Weak Point in the Paper

Results depend heavily on the knowledge spillover parameter ϕ. Baseline ϕ = −0.068, calibrated
to match observed growth rates of TFP (1.11%/yr) and real gross IPP investment (5.97%/yr) given
λ = 0.75. Pettersson notes that Bloom et al. (2020) find ϕ ≈ −1.4 for the aggregate US economy
at the same λ. Under that value the overall contribution falls to 0.05%/yr and turns **negative**
(−0.02%/yr) across the twenty-first century.

In the calibration matching the best-identified estimate of the idea production function, the
quantitative headline largely disappears. He reports this transparently and argues the
qualitative point survives, which is fair; the quantitative claim does not.

## Positive Spillover Channel (absent from all four papers)

If technology is nonrival and diffuses internationally, advanced-economy ageing raising frontier
R&D is a **positive externality for adopting economies**. Mexico would receive frontier
innovation without financing it — advanced-economy ageing mildly good for Mexican productivity
while fiscally costly at home. Not modelled anywhere in this literature (all four papers are
closed-economy or within-country). Belongs to Aurora more than DFD; flagged as an original
observation requiring Anne's and Elle's assessment before treatment as more than a conjecture.

## Project Routing Notes

**Aurora.** The spillover channel above. Also the general structure — demography driving
technology endogenously — which parallels the Acemoglu framing and reinforces the point that
Aurora's demographic and technological drivers may be one causal chain rather than parallel
forces. Route to Elle.

**BDH.** A concrete pointer: Pettersson cites **Huetsch, Krueger & Ludwig (2026)**, "The medical
expansion, life expectancy, and endogenous directed technical change," NBER WP 35092 — a
multi-sector OLG in which rising life expectancy and directed technical change toward the health
sector are jointly endogenous. Not previously in the corpus. Route to Beth; likely a priority
acquisition for BDH.

**Acquisition pointer.** Auclert, Malmberg, Martenet & Rognlie (2025), "Demographics, wealth,
and global imbalances in the twenty-first century," NBER WP 29161 — the open-economy counterpart
to this literature, by the conference organiser. Worth acquiring if reachable.

## Source

Pettersson, Markus (Department of Economics, Stockholm University). "Endogenous Technological
Change Along the Demographic Transition." 27 May 2026, 55pp including online supplement.
JEL: E17, E25, J11, O30, O40. Framework: Romer (1990), Jones (1995), Auerbach and Kotlikoff
(1987). Data: UN World Population Prospects (2024), HMD/Bell and Miller (2005), Heuser (1976),
Gapminder (2024), US Census Bureau (2023), PSID 1968–2019, Penn World Table, BEA NIPA, OECD tax
database, Social Security Administration. Acknowledges Lars Ljungqvist, Timo Boppart, David
Domeij, Chad Jones, Paul Segerstrom, Johanna Wallenius, Kjetil Storesletten, Per Krusell.

Obtained in connection with the NBER virtual conference on the macroeconomic effects of
population aging (Auclert et al.), September 2026. Fourth of the series. See
2026-09-17_nber-aging-conference-synthesis.md for the cross-paper argument.

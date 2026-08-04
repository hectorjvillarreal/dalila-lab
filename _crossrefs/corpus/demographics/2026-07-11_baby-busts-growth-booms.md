---
title: "Baby Busts and Growth Booms: Demographic Change and the Macroeconomy — Acemoglu, Autor, Beirne & Scott (NBER w35401)"
date: 2026-07-11
added_by: Claude (Anne)
endorsed_by:            # pending — see Endorsement Routing; needs Cath + Elle, not Anne alone
projects: [DFD, Aurora]
indicators: [composite]   # NB: linkage/consequence paper, not a demographic data indicator — see note
geography: [global, comparator]   # cross-country + US commuting zones; NOT lac — the absence is the analytical point
scenario_implication: neutral     # leaves the TFR baseline untouched; reframes the *consequence* mapping (see body)
source_reliability: primary       # top-tier authors; but working paper, not yet refereed — preliminary
data_vintage: 2026
promotion_status: pending-anne
corpus_path: _crossrefs/corpus/demographics/
doc_type: literature-entry        # provisional label; reconcile with PROTO-RAG-001 taxonomy on filing
---

## Summary

Acemoglu, Autor, Beirne and Scott (NBER WP 35401, issued 6 July 2026) challenge the
standard prior that falling birth rates and population aging depress growth. Across
countries they find lower birth rates associated with *higher* growth in GDP per
working-age adult, and across US commuting zones with higher wage growth, with no
negative effect on aggregate GDP or earnings. They rule out educational upgrading,
rising female labor force participation, the declining role of agriculture, and
neoclassical-Solow mechanisms. Their proposed mechanism is the endogenous, labor-saving
response of technology to the scarcity of younger workers — evidenced by more
labor-saving patents, growing high-tech activity, and higher TFP growth across countries
and industries. Identification exploits cross-country variation in WWII military and
civilian deaths to argue the decline in the *younger* population specifically, not
population size, drives the results.

## Why this is a priority entry

This is a serious, high-authority challenge to the "aging = growth-and-fiscal
catastrophe" prior that underwrites much of DFD and Aurora. It cannot be filed as a
watch item. But the optimism is conditional: the entire favorable result runs through an
*innovation* channel — growth is rescued because affected economies automate in response
to labor scarcity. That is precisely the margin a middle-income, high-informality,
low-R&D economy may lack.

## DFD Calibration Implications

Against the four standing calibration questions:

1. **Fast-transition TFR scenario (Mexico)** — no direct effect. The paper does not
   alter fertility levels; it alters the interpretation of their *consequences*.
   `_baseline.md` is unaffected.
2. **Dependency-ratio path → IM-6 pension contribution rate** — indirect. If TFP
   responds endogenously to demographic structure, the growth denominator in
   sustainability arithmetic shifts favorably — but only where the automation channel
   fires. For Mexico we cannot assume it does (see below), so this is a scenario switch,
   not a baseline change.
3. **Survival probabilities (OLG demographic block)** — no effect.
4. **Coupling / partnership formation** — no effect.

**Modeling implication (Cath / IM-6).** The paper is a direct argument against carrying
TFP growth as *exogenous* in the OLG. Acemoglu–Autor claim productivity growth is
endogenous to demographic structure. Minimum action: represent an endogenous
labor-saving / automation channel as an Aurora scenario. Stronger action: make the
channel *threshold-gated* on income / innovation capacity, so it fires for high-income
calibrations and is muted or absent for the LAC baseline.

## The automation-threshold question (contribution line)

The paper's value to us is not its headline; it is the research question it generates.
Its optimistic result is gated on the endogenous-automation response. In a setting with
high informality, low R&D intensity, limited patenting, and weaker capital-deepening,
that response may be muted or absent. Our core DFD thesis — Latin America ages before it
gets rich — becomes, read through this paper, the claim that LAC ages *without reliable
access to the very mechanism that makes aging benign here.*

So the paper does not reassure us about Mexico; it sharpens the concern into a testable
proposition: **is there an income / innovation threshold below which demographic
contraction does not trigger the labor-saving response, leaving the fiscal and growth
drag intact?** Transposing the Acemoglu–Autor design to middle-income settings and
testing that threshold is a candidate DFD / Aurora contribution in its own right.

## Project Routing Notes

- **Aurora (Elle)** — strongest fit. This is long-run structural foresight material; the
  threshold question belongs in Aurora's scenario architecture.
- **DFD / OLG (Cath)** — the TFP-endogeneity call above.
- **Shelf position** — natural counterpoint to Fernández-Villaverde (2026) on the same
  shelf: same demographic facts, opposite consequence mapping. Catalog the tension
  explicitly rather than as competing claims.
- **Inequality thread** — macro-growth complement to the "automated life for capital"
  watch item; the distributional side (labor-saving tech, wages) is Autor's territory.
- **BDH** — marginal; note only.

## Endorsement Routing

This is a demographics–macro *linkage* paper, not a demographic data release, so Anne's
classification pass is insufficient for promotion. Endorsement requires:
- **Cath** — on the TFP-endogeneity / OLG modeling implication.
- **Elle** — on the Aurora foresight framing and the threshold question.
Hold at `_crossrefs/corpus/demographics/_pending/` until both sign off.

## Schema notes (for the architecture chat)

The demographics-monitor schema is tuned for demographic *data* (charts, TFR releases,
projections). This entry is a theory-and-evidence paper, which strains three fields:
`indicators` (no clean demographic-indicator tag), `scenario_implication` (it reframes a
consequence mapping rather than shifting a scenario), and the corpus-note naming
convention vs PROTO-RAG-001. Flag for a possible `linkage` / `literature` sub-type in a
future skill revision.

## Source

Daron Acemoglu, David Autor, Keelan Beirne & Andrew Scott, "Baby Busts and Growth Booms:
Demographic Change and the Macroeconomy," NBER Working Paper 35401 (July 2026).
DOI 10.3386/w35401. https://www.nber.org/papers/w35401
Status: working paper, not yet peer-reviewed.

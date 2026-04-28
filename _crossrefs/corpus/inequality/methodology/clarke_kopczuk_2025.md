---
type: corpus_entry
tier: methodological_reference
project_scope: [DFD, BDH, RF]
authors: [Clarke, Conor; Kopczuk, Wojciech]
year: 2025
title: "Measuring Income and Income Inequality"
venue: "Journal of Economic Perspectives, 39(2), 103–126"
doi: "10.1257/jep.20241424"
date_added: 2026-04-28
added_by: Anne
---

# Clarke & Kopczuk (2025) — Measuring Income and Income Inequality

## One-line summary

A first-principles methodological assessment of how to measure income for inequality analysis, framing the Piketty–Saez–Zucman (PSZ) vs. Auten–Splinter (AS) dispute as methodologically irreducible rather than empirically resolvable.

## Core conceptual contributions

### The five fundamental problems with Haig-Simons income

1. **Fairness grounding** — Haig-Simons was developed as an administrative tax concept, not a justice concept. Its alignment with welfare measures (utility, capability, ability-to-pay) is partial.
2. **Implementability** — the consumption/savings boundary is not self-defining; the consumption/cost-of-production boundary is also fuzzy (Simons: "something quite arbitrary about the distinction between consumption and accumulation").
3. **Valuation and imputation** — many large components (closely-held equity, leisure, household production, retirement savings) lack market prices.
4. **Unit of observation** — individuals, households, extended families, communities all have legitimate claims; Haig-Simons does not specify.
5. **Government spending attribution** — public goods (defense, infrastructure) increase ability to consume but cannot be allocated cleanly to individuals.

### The PSZ vs. AS dispute

Both target the same goal — top US income shares — but reach opposing conclusions. The disagreement is driven by allocation choices for income components not directly observed in administrative tax data:

- **Excess depreciation** allocation (1.2 percentage points of the top 1% trend difference, ~30% of the total disagreement)
- **Retirement account rollovers** (PSZ initially mistook rollovers for new income)
- **Government transfer allocation** (per-capita vs. proportional to other income)
- **Payroll tax / Social Security** (include in pretax or not)

### Methodological prescription

> Inequality estimates should be presented as **bands** under alternative assumptions, not as points. (Citing Alvaredo et al. 2024 for the LAC-facing precedent.)

## Relevance to DFD work

### Calibration discipline (Cath)

The disagreement on excess depreciation, retirement allocation, and corporate retained earnings allocation directly affects the **capital share parameter** and **effective tax rate parameter** in the government budget constraint of the OLG/DSGE core. Per Cath's calibration discipline standard, any draw from PSZ or AS series must:
- Document the source series explicitly (PSZ vs. AS vs. CBO vs. Larrimore et al.)
- Carry a sensitivity range that brackets the methodological dispute
- Flag whether the underlying allocation matters for the equilibrium condition or only for distributional reporting

### Pretax vs. post-tax framing

Clarke & Kopczuk emphasize that even AS — who find taxes and transfers largely offset rising pretax inequality — agree that pretax top shares have risen. This matters for DFD: the **demographic-fiscal interaction** generates pressure on pretax factor income shares (capital share rises with aging under standard OLG), which feeds the political-economy module independent of the post-tax distribution.

## Relevance to fiscal dominance paper

The PSZ vs. AS allocation methods for **undistributed corporate earnings** are directly relevant to how Paper 2 (when calibration is attempted) should distribute λ across the wealth distribution given ENIGH underreporting. The Mexican household survey problem is a more severe version of the US administrative-data problem Clarke & Kopczuk describe.

## Open methodological questions surfaced

- How to treat household production in NTA framework (currently excluded; satellite estimates suggest >25% of GDP)
- Whether the unit of observation should be individual or household for LAC where extended-family resource pooling is more prevalent
- How to handle realization vs. accrual in capital gains for emerging-economy contexts where capital gains taxation is weak

## Key data sources cited

- PSZ Distributional National Accounts microdata (https://gabriel-zucman.eu/usdina/)
- Auten & Splinter (2024) replication materials
- CBO Distribution of Household Income series
- Larrimore, Burkhauser, Auten & Armour (2021) accrued capital gains series

## Citation

Clarke, C. & Kopczuk, W. (2025). "Measuring Income and Income Inequality." *Journal of Economic Perspectives*, 39(2), 103–126.

## Cross-references

- → `gomez_2025.md` — extends the conceptual framework to Hicksian income
- → `auerbach_2025.md` — translates measurement debate into public-finance design
- → `latam/` — Alvaredo et al. (2024) inequality bands methodology (pending)
- → DFD calibration log (Cath)
- → Fiscal dominance Paper 2 calibration plan (Héctor)

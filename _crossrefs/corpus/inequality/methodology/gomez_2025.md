---
type: corpus_entry
tier: methodological_reference
project_scope: [DFD, fiscal_dominance_paper]
authors: [Gomez, Matthieu]
year: 2025
title: "Macro Perspectives on Income Inequality"
venue: "Journal of Economic Perspectives, 39(2), 127–148"
doi: "10.1257/jep.20241435"
date_added: 2026-04-28
added_by: Anne
endorsed_by:
build_instruction: "_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md"
---

# Gomez (2025) — Macro Perspectives on Income Inequality

## One-line summary

Introduces **Hicksian income** as the welfare-correct income definition, then uses a shift-share decomposition to attribute most of the rise in top US income shares to capital income inequality — specifically a surge in entrepreneurial income — driven by higher returns on capital, lower cost of external financing, and lower effective tax rates.

## Core conceptual contributions

### Four income concepts in source-and-use form

| Concept | Sources | Uses |
|---|---|---|
| Distributed | Wages + Rents + Interest + Dividends | Consumption + Asset purchases |
| Factor (national income) | Distributed + Retained earnings | Consumption + Asset purchases + Corporate investment |
| Haig-Simons | Distributed + Capital gains | Consumption + ΔNet worth |
| **Hicksian** | Distributed + PV[ΔDistributed + ΔTrading profits] | Consumption + PV[ΔConsumption] |

### The Hicksian symmetry

Hicksian income treats anticipated wage growth and anticipated dividend growth **symmetrically**. Factor and Haig-Simons income effectively double-count capital income relative to labor income (echoing Barro 2021): both add a forward-looking component for capital (retained earnings or capital gains) but not for labor. Hicksian income corrects this by adding the present value of anticipated wage growth as well.

Implication: switching from factor to Hicksian income would likely **reduce measured inequality** (because labor income, disproportionately earned by the bottom 99%, gets a forward-looking boost), but would not affect the upward trend.

### Shift-share decomposition of top-share growth

Gomez decomposes the change in top income shares into three components:

1. Change in labor income inequality
2. Change in capital income inequality
3. Change in aggregate labor share

**Empirical finding (US, 1960–2020):** Most of the rise in top shares is driven by (2) — rising capital income inequality — not by (3) the falling labor share. The 1981–2000 period is partial exception (executive pay surge).

### Drivers of capital income inequality (entrepreneur capital accumulation equation)

```
rate of capital accumulation_i = (1 - τ)[r + λ(rok_i - r)] - consumption rate_i
```

Three drivers since 1980:
- **Return on capital** (rok): U-shape, declining 1960–1980 then rising; concentrated in noncorporate sector
- **Cost of capital** (r): steady decline since 1960 across both debt and equity
- **Effective tax rate** (τ): declined from ~50% to ~30% for entrepreneurs

Quantitative back-of-envelope: combined effect raises top-entrepreneur capital growth rate by ~7.5 pp annually since 1980, generating ~1.5 log-point increase in capital holdings — comparable to the observed 1.4 log-point increase in top 0.01% income share.

## Relevance to DFD work

### Direct relevance to fiscal dominance paper (Proposition 2)

Gomez cites **Fagereng, Gomez, Gouin-Bonenfant, Holm, Moll & Natvik (2024) "Asset-Price Redistribution"** (World Inequality Lab WP 2024/14) as the formal treatment of the channel: capital gains constitute Hicksian income only to the extent they reflect changes in anticipated future cash flows or anticipated sale prices, not changes in discount rates. **This paper should be acquired and added to the corpus immediately** — it is upstream of Proposition 2 and provides the formal framework that the fiscal dominance Paper 1 informally invokes.

### Relevance to OLG calibration

The 2017 reclassification of intellectual property products as investment (Koh, Santaeulàlia-Llopis & Zheng 2020) mechanically increased the measured aggregate capital share. Any Mexico-calibrated capital share parameter drawn from national accounts inherits this reclassification effect; we should track the equivalent reclassification history in INEGI national accounts.

### Asymmetric productivity in Mexican context

Andrews–Criscuolo–Gal (2016) finding — that the rise in returns on productive assets is concentrated in a small number of fast-growing firms — is directly relevant to the Mexican private-sector heterogeneity between formal/large firms and informal/small firms. The high-productivity tail in Mexico likely captures most of the rok increase; this could refine how λ is distributed in fiscal dominance Paper 2.

## ⚠️ Watch item: "Automated life for capital"

Gomez's Hicksian framework gives capital its own forward-looking biography — anticipated cash flows, anticipated sales, anticipated repricing. This is symmetric to how OLG gives labor a lifecycle, and points toward an **OLG with capital cohorts** as a natural theoretical extension. See `watch_items/automated_life_for_capital.md` for the full thread.

## Open theoretical questions surfaced

- Does the Hicksian critique propagate to the equilibrium structure of the OLG (capital share parameter), or is it strictly an inequality-measurement issue? (**Awaiting Cath's judgment.**)
- Why has the equilibrium response to high after-tax rok not occurred — i.e., why hasn't entrepreneurial entry pushed rok back down? (Akcigit-Ates 2023; Gutiérrez-Philippon 2019; Karahan-Pugsley-Şahin 2024 propose competing answers.)
- Mian–Straub–Sufi (2021) "Indebted Demand" suggests rising inequality itself may explain low interest rates — relevant to the demographic-fiscal interaction in DFD.

## Key data sources cited

- Board of Governors Integrated Macroeconomic Accounts
- Compustat for public-firm effective tax rates
- PSZ DINA microdata for entrepreneur tax rates

## Citation

Gomez, M. (2025). "Macro Perspectives on Income Inequality." *Journal of Economic Perspectives*, 39(2), 127–148.

## Cross-references

- → `clarke_kopczuk_2025.md` — provides the Haig-Simons baseline this paper extends
- → `auerbach_2025.md` — public-finance implications of the rising-rok / falling-r pattern
- → `watch_items/automated_life_for_capital.md`
- → Fiscal dominance Paper 1 (Proposition 2)
- → Fiscal dominance Paper 2 calibration plan (λ distribution)
- → **TO ACQUIRE:** Fagereng, Gomez, Gouin-Bonenfant, Holm, Moll & Natvik (2024), "Asset-Price Redistribution," World Inequality Lab WP 2024/14
- → Auclert, Malmberg, Rognlie & Straub (2025) shift-share machinery [tier-1 reference, already staged]
- → Build instruction: `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`

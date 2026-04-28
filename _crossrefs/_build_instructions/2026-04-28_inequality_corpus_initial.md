---
type: build_instruction
build_type: initial_scaffold
date: 2026-04-28
corpus_affected:
  - _crossrefs/corpus/inequality/
  - _crossrefs/mission-project-map.md
  - CLAUDE.md
triggered_by: "Héctor–Anne conversation 2026-04-28 on building a dedicated inequality corpus from the JEP Spring 2025 symposium (Clarke & Kopczuk, Gomez, Auerbach), with the watch-item framing for the 'automated life for capital' thread."
agents_involved: [Héctor, Anne, Debb]
status: pending_execution
sequence_position: legacy_pre_protocol
notes: "First corpus build instruction written, predating formalization of PROTO-RAG-001. Retrofitted to protocol convention by build 2026-04-28_protocol_foundation. Body content preserved as drafted; minor frontmatter conformity additions only."
---

# Inequality Corpus — Build Instructions for Claude Code

**To:** Claude Code (Dalila session)
**From:** Anne (Population Economics, Core Team)
**Date:** 2026-04-28
**Re:** Scaffold a dedicated inequality methodology corpus, generate three RAG entries, register cross-references, and log a research-watch item.

---

## 1. Scope and rationale

This task creates a dedicated **inequality** corpus folder as a cross-cutting resource shared across DFD, BDH, and RF. The motivation is methodological: the JEP Spring 2025 symposium on income inequality measurement (Clarke & Kopczuk; Gomez; Auerbach) provides primary references that bear directly on:

- DFD calibration discipline for capital share, top-share, and effective tax-rate parameters in the OLG/DSGE core's government budget constraint
- The fiscal dominance paper's wealth-concentration mechanism (Proposition 2) via the Fagereng et al. (2024) asset-price redistribution framework cited by Gomez
- BDH health-financing distributional analysis
- RF fiscal narrative incidence classification

A standalone inequality corpus, rather than scattering these entries across project subfolders, reflects the genuinely cross-cutting nature of the methodological content and resolves cleanly with the pending CLAUDE.md decision favoring the **shared `_crossrefs/` corpus architecture**.

---

## 2. Folder scaffold

Create the following directory structure under Dalila root:

```
_crossrefs/corpus/inequality/
├── README.md
├── methodology/
│   ├── clarke_kopczuk_2025.md
│   └── gomez_2025.md
├── public_finance/
│   └── auerbach_2025.md
├── latam/                    (placeholder — entries to follow)
│   └── README.md
└── watch_items/
    └── automated_life_for_capital.md
```

The `latam/` subfolder is created empty (with a placeholder README) to anchor the future LAC measurement entries (Alvaredo–Bourguignon–Ferreira–Lustig 2024 inequality bands; Del Carmen et al. 2023 on Honduras; Fairfield–Jorratt 2016 on Chile; ENIGH-related notes).

The `watch_items/` subfolder holds open theoretical threads that connect corpus material to active modeling work.

---

## 3. Top-level README — `_crossrefs/corpus/inequality/README.md`

Create with the following content:

```markdown
# Inequality Corpus

**Scope:** Methodological references on income and wealth inequality measurement, public-finance implications, and Latin America–specific measurement issues. Cross-cutting across DFD, BDH, and RF.

**Status:** Initial scaffold (April 2026). Three primary entries from the JEP Spring 2025 symposium. LAC entries pending. Vector store integration pending Debb's installation.

## Organization

- `methodology/` — conceptual frameworks for income measurement (Haig-Simons, factor, Hicksian); imputation and allocation methods; PSZ vs. Auten–Splinter dispute
- `public_finance/` — fiscal incidence, life-cycle vs. annual progressivity, top marginal tax rate design, redistribution vs. predistribution
- `latam/` — Latin America–specific measurement: inequality bands methodology, ENIGH underreporting, country-level top-shares
- `watch_items/` — open theoretical threads connecting corpus material to active modeling work

## Standing principles

- Inequality estimates are **bands conditional on assumptions**, not points (Clarke & Kopczuk's framing)
- Factor income (national accounts) systematically miscounts capital relative to labor through asymmetric forward-looking treatment (Gomez's Hicksian critique)
- Annual snapshots misrepresent progressivity once life-cycle effects are accounted for (Auerbach)
- For DFD calibration: every parameter drawn from this corpus must carry a documented source and a sensitivity range, per Cath's calibration discipline standard

## Cross-references

- DFD: OLG/DSGE government budget constraint calibration (Cath); demographic-fiscal interaction with top-share evolution (Anne)
- Fiscal Dominance Paper 1: Proposition 2 asset-price redistribution mechanism (Héctor)
- BDH: health-financing distributional analysis (Beth)
- RF: fiscal policy event incidence classification

## Cross-project register

This corpus is registered in `_crossrefs/mission-project-map.md` as a shared resource. Entries here are referenced but not duplicated across DFD/BDH/RF docs folders.
```

---

## 4. RAG entry — Clarke & Kopczuk (2025)

Create `_crossrefs/corpus/inequality/methodology/clarke_kopczuk_2025.md` with the following content:

```markdown
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
```

---

## 5. RAG entry — Gomez (2025)

Create `_crossrefs/corpus/inequality/methodology/gomez_2025.md` with the following content:

```markdown
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
```

---

## 6. RAG entry — Auerbach (2025)

Create `_crossrefs/corpus/inequality/public_finance/auerbach_2025.md` with the following content:

```markdown
---
type: corpus_entry
tier: methodological_reference
project_scope: [DFD, BDH, fiscal_dominance_paper]
authors: [Auerbach, Alan J.]
year: 2025
title: "Public Finance Implications of Economic Inequality"
venue: "Journal of Economic Perspectives, 39(2), 149–170"
doi: "10.1257/jep.20241421"
date_added: 2026-04-28
added_by: Anne
---

# Auerbach (2025) — Public Finance Implications of Economic Inequality

## One-line summary

Translates the income-measurement debate into public-finance design questions: tax incidence assumptions, valuation of transfers, life-cycle vs. annual progressivity, indirect high-income tax mechanisms (phase-outs, IRMAA, NIIT), revenue volatility, and the case for consumption taxation at the top.

## Core conceptual contributions

### Annual snapshot vs. life-cycle progressivity

Three reasons annual cross-sections misrepresent fiscal progressivity:

1. **Tax/income persistence mismatch** — taxes on consumption look more regressive annually than over the lifetime under permanent-income smoothing
2. **Age profiles of taxes vs. transfers** — payroll taxes are concentrated at younger ages; pension/health benefits at older ages
3. **Cross-cohort aggregation** — pay-as-you-go Social Security looks "extremely progressive" annually because it taxes working cohorts to fund retired cohorts

Auerbach, Kotlikoff & Koehler (2023, JPE) is the comprehensive treatment of this for the US — **already staged in DFD references**.

### Tax equivalences that distort cross-section analysis

- **Traditional vs. Roth retirement saving** — economically equivalent in present value, but Roth shifts measured tax burden away from retirees
- **Flat tax = wage tax + cash-flow tax = VAT** — same economic incidence, different surface allocation
- **Predistribution vs. redistribution** — minimum wages, tariffs, job guarantees substitute for transfers but typically introduce production distortions (Diamond–Mirrlees 1971 violations)

### Indirect high-income tax mechanisms (Table 1 in the paper)

A pattern across both Democratic and Republican administrations since 1983: increasing top-end progressivity through phase-outs and surcharges rather than rate increases.

- Social Security benefit taxation (1983)
- Itemized deduction phase-out, personal exemption phase-out (1990)
- Child tax credit phase-out (1997)
- Income-based Medicare Part B premiums / IRMAA (2003)
- 0.9% Medicare payroll surcharge, 3.8% Net Investment Income Tax, IRMAA Part D (2010)

Hypothesis: lower **salience** of indirect tax increases makes them politically easier than headline rate increases.

### Top marginal tax rate formula

τ = 1 / (1 + ae) where:
- e = taxable income elasticity at the top
- a = (total income above threshold) / (income strictly above threshold)

**Higher inequality → thicker right tail → smaller a → higher optimal τ.** The Diamond–Saez (2011) midrange parameterization yields τ ≈ 73%.

### Revenue volatility implication

Top 1% income is more procyclical than aggregate income (capital gains, business profits, executive compensation). Each $1 of aggregate income fluctuation 1979–2020 was matched by ~$0.50 of top-1% income fluctuation. **Rising top shares + progressive rates → amplified procyclical revenue volatility.** California is the canonical state-level illustration; the federal case is muted but real.

### Consumption taxation at the top

Auerbach argues for a supplemental progressive **personal expenditure tax** on high-income individuals as a complement to existing taxes. Advantages:
- Avoids capital-income measurement problems (Clarke–Kopczuk concerns)
- Effectively imposes a one-time tax on accumulated wealth via consumption financed from existing wealth
- Reduces revenue volatility (consumption smoother than income)
- Compatible with destination-based cash-flow corporate taxation (Auerbach 2017)

## Relevance to DFD work

### Direct relevance to OLG/DSGE government budget constraint (Cath)

The annual-vs-lifetime progressivity distinction is *the same problem* DFD's OLG framework is designed to resolve at the modeling level. Auerbach's Table 1 of indirect tax mechanisms gives Cath a concrete catalog of fiscal instruments to consider when specifying the tax structure block — the Mexican analogues (ISR phase-outs, IEPS surcharges, IVA exemptions phased by income proxy) should be mapped to this structure.

### Relevance to BDH (Beth)

The Medicare IRMAA mechanism is a direct precedent for income-based health-insurance premium design. Mexico's IMSS/ISSSTE/Seguro Popular trajectory is moving toward fragmented financing where IRMAA-style mechanisms could be relevant for distributional fiscal sustainability analysis.

### Relevance to fiscal dominance paper

The revenue volatility argument cuts both directions: under fiscal dominance, the volatility of progressive-tax revenue at the top **interacts with debt sustainability** in a way that reinforces the asset-price redistribution channel. When top capital income falls in a downturn, progressive revenues collapse, fiscal pressure rises, and the inflation/repricing channel from the paper activates.

### Mexico-specific context

The 2017 TCJA effective tax rate decline for US entrepreneurs (Gomez 2025) and the ongoing political-economy tension Auerbach describes are mirrored in Mexico's incomplete tax reform trajectory: ENIGH underreporting, weak capital gains taxation, IEPS as the de facto progressive instrument. Auerbach's framing of "indirect high-income tax mechanisms" applies almost directly.

## Open methodological questions surfaced

- How should the OLG fiscal block represent **non-rate progressive instruments** (phase-outs, premiums, surcharges)?
- Should the DFD revenue projection include explicit volatility bands tied to top-share dynamics?
- Is the "predistribution vs. redistribution" framing useful for analyzing Mexico's labor-market interventions (minimum wage, formal-sector subsidies)?

## Citation

Auerbach, A. J. (2025). "Public Finance Implications of Economic Inequality." *Journal of Economic Perspectives*, 39(2), 149–170.

## Cross-references

- → `clarke_kopczuk_2025.md` — measurement foundations
- → `gomez_2025.md` — capital-income drivers feeding into fiscal incidence
- → Auerbach, Kotlikoff & Koehler (2023) — already staged DFD reference; this paper extends the framework
- → Diamond & Saez (2011) — already staged optimal taxation reference
- → Cath's calibration log — fiscal block instrument catalog
- → BDH health-financing distributional analysis (Beth)
```

---

## 7. Watch-item entry — `_crossrefs/corpus/inequality/watch_items/automated_life_for_capital.md`

Create with the following content:

```markdown
---
type: research_watch_item
status: open
date_opened: 2026-04-28
opened_by: [Héctor, Anne]
related_corpus: [methodology/gomez_2025.md]
related_projects: [DFD/IM-6, fiscal_dominance_paper]
---

# Watch item: "Automated life for capital"

## Origin

Conversation between Héctor and Anne (2026-04-28) on the Gomez (2025) Hicksian framework. Héctor's framing: the Hicksian symmetry between labor and capital is "thrilling for modeling" because it imagines an automated life for capital.

## The thread

Standard OLG gives **labor** a lifecycle: cohorts are born, work, retire, die. **Capital** has no lifecycle — it is a passive store of value, the residual between periods.

Gomez's Hicksian income concept treats anticipated wage growth and anticipated dividend growth symmetrically. The deeper implication: capital acquires a forward-looking biography — anticipated cash flows, anticipated sales, anticipated repricing events. The asset has expectations, revisions, surprises. Fagereng, Gomez, Gouin-Bonenfant, Holm, Moll & Natvik (2024) "Asset-Price Redistribution" formalizes this by decomposing capital gains into anticipated vs. unanticipated components.

## Modeling implication for DFD / IM-6

If the Hicksian symmetry is taken seriously, an OLG could be extended to have **capital cohorts** parallel to demographic cohorts:

- **Vintages** with anticipated payout profiles
- **Mortality** in the form of depreciation and obsolescence
- **Cohort-specific revaluation shocks** (anticipated vs. unanticipated)

Auclert–Malmberg–Rognlie–Straub (2025) shift-share machinery already moves partway in this direction by treating wealth-by-age as a structural object rather than an accounting residual.

For the DFD architecture: this would mean the **asset-price redistribution channel** from the fiscal dominance paper does not need to be bolted on as a separate mechanism — it could emerge endogenously from giving capital its own cohort structure parallel to the demographic one. This is potentially a genuine theoretical contribution rather than a calibration exercise.

## Open question for Cath

Does the Hicksian critique of factor income propagate to the equilibrium structure of the OLG (capital share parameter, factor market clearing), or is it strictly an inequality-measurement issue that does not propagate? Anne's instinct: the latter. Awaiting Cath's judgment.

## Status

**Watch item, not active modeling commitment.** IM-6 development horizon is 1–2 years; integration challenges with the NTA layer and the CIEP-style fiscal simulator are the binding constraints. This thread is preserved here so it is recoverable when capacity allows.

## Triggers for promotion to active research

- Cath's judgment on propagation question returns "yes, this affects the equilibrium structure"
- Fagereng et al. (2024) framework formally adopted in fiscal dominance Paper 2
- IM-6 Phase 2 (post-baseline) opens scope for asset-side cohort structure
- Co-author availability for a DSGE-OLG paper on demographic transition with explicit capital-cohort structure

## Cross-references

- → `methodology/gomez_2025.md`
- → Auclert, Malmberg, Rognlie & Straub (2025) [staged]
- → Fiscal dominance Paper 2 plan
- → IM-6 architecture notes (Cath, Anne)
- → **TO ACQUIRE:** Fagereng et al. (2024) "Asset-Price Redistribution"
```

---

## 8. `latam/` placeholder — `_crossrefs/corpus/inequality/latam/README.md`

Create with the following content:

```markdown
# Inequality Corpus — Latin America measurement

**Status:** Placeholder. Entries pending.

## Planned entries

- Alvaredo, Bourguignon, Ferreira & Lustig (2024), "Inequality Bands: Seventy-Five Years of Measuring Income Inequality in Latin America," World Inequality Lab WP 2024/08
- Del Carmen, Garriga, Nuñez & Scot (2023), "Two Decades of Top Income Shares in Honduras," World Bank Policy Research WP 10722
- Fairfield & Jorratt De Luis (2016), "Top Income Shares, Business Profits, and Effective Tax Rates in Contemporary Chile," *Review of Income and Wealth* 62(S1)
- ENIGH underreporting methodology notes (Mexico) — pending Héctor's compilation
- INEGI national accounts reclassification history — pending compilation

## Rationale

The methodology corpus above is US-focused. The LAC subfolder anchors the middle-income measurement frontier where:
- Household survey underreporting is more severe than US administrative-data gaps
- Capital gains taxation is weaker, making realization-based measurement even less informative
- Informal-sector heterogeneity dominates the top-share allocation problem
- Extended-family resource pooling complicates the unit-of-observation question

## Cross-references

- → Fiscal dominance Paper 2 calibration plan (ENIGH-dependent)
- → DFD Mexico baseline calibration (Cath, Anne)
- → BDH Mexico-Costa Rica-Panamá health financing (Beth)
```

---

## 9. Cross-reference register update — `_crossrefs/mission-project-map.md`

Append (or create section if absent) the following block:

```markdown
## Inequality Corpus (cross-cutting)

**Location:** `_crossrefs/corpus/inequality/`
**Owner:** Anne (initial scaffold); shared across DFD, BDH, RF
**Date registered:** 2026-04-28

| Project | Connection |
|---|---|
| DFD | OLG/DSGE government budget constraint calibration; capital share and effective tax rate parameters; demographic-fiscal interaction with top-share evolution |
| Fiscal Dominance Paper 1 | Proposition 2 wealth-concentration mechanism; Fagereng et al. (2024) framework |
| Fiscal Dominance Paper 2 | λ distribution calibration under ENIGH constraints |
| BDH | Health-financing distributional analysis; IRMAA-style mechanisms for IMSS/ISSSTE |
| RF | Fiscal policy event incidence classification |
| IM-6 | Watch item: capital cohort structure (long-horizon theoretical extension) |

**Status:** Initial scaffold complete (3 methodology entries, 1 watch item, LAC placeholder). Vector store integration pending Debb's installation. LAC entries pending acquisition.
```

---

## 10. CLAUDE.md update

In the Dalila root `CLAUDE.md` (orientation file for Claude Code sessions), add the following entry under the corpus or cross-references section:

```markdown
### Inequality corpus (`_crossrefs/corpus/inequality/`)

Cross-cutting methodological corpus on income and wealth inequality measurement. Initial scaffold April 2026. Three primary entries from JEP Spring 2025 symposium (Clarke & Kopczuk, Gomez, Auerbach). Shared across DFD, BDH, RF; not duplicated in project subfolders. See `_crossrefs/corpus/inequality/README.md` for organization and standing principles. Open watch item: "automated life for capital" — Hicksian symmetry implication for OLG capital cohort structure.
```

---

## 11. Acquisition list (output as a separate task note)

Create `_crossrefs/corpus/inequality/_acquisition_queue.md` with:

```markdown
# Inequality Corpus — Acquisition queue

**Priority 1 (pre-Economics Letters submission):**
- Fagereng, A., Gomez, M., Gouin-Bonenfant, É., Holm, M., Moll, B. & Natvik, G. (2024). "Asset-Price Redistribution." World Inequality Lab WP 2024/14. Upstream of fiscal dominance Paper 1 Proposition 2.

**Priority 2 (DFD Mexico calibration phase):**
- Alvaredo, F., Bourguignon, F., Ferreira, F. & Lustig, N. (2024). "Inequality Bands: Seventy-Five Years of Measuring Income Inequality in Latin America." WIL WP 2024/08.
- Del Carmen, G., Garriga, S., Nuñez, W. & Scot, T. (2023). "Two Decades of Top Income Shares in Honduras." World Bank PRWP 10722.
- Auerbach, A. J., Kotlikoff, L. J. & Koehler, D. (2023). "US Inequality and Fiscal Progressivity: An Intragenerational Accounting." *JPE* 131(5). [Confirm if already staged — Anne's notes indicate yes; if so, register cross-reference only.]

**Priority 3 (deeper methodological background):**
- Auten, G. & Splinter, D. (2024). "Income Inequality in the United States: Using Tax Data to Measure Long-Term Trends." *JPE* 132(7).
- Piketty, T., Saez, E. & Zucman, G. (2018). "Distributional National Accounts." *QJE* 133(2). [Likely already accessible via existing references; confirm.]
- Smith, M., Yagan, D., Zidar, O. & Zwick, E. (2019). "Capitalists in the Twenty-First Century." *QJE* 134(4).
- Smith, M., Zidar, O. & Zwick, E. (2023). "Top Wealth in America." *QJE* 138(1).

**Priority 4 (Mexico-specific, requires manual compilation):**
- ENIGH underreporting methodology synthesis (Héctor's compilation pending)
- INEGI national accounts reclassification history (pending)
```

---

## 12. Execution checklist for Claude Code

- [ ] Create folder structure under `_crossrefs/corpus/inequality/` per Section 2
- [ ] Write top-level README per Section 3
- [ ] Write three methodology / public_finance entries per Sections 4–6
- [ ] Write watch-item entry per Section 7
- [ ] Write LAC placeholder README per Section 8
- [ ] Update `_crossrefs/mission-project-map.md` per Section 9 (append, do not overwrite existing entries)
- [ ] Update Dalila root `CLAUDE.md` per Section 10 (insert in corpus / cross-references section; do not disturb other content)
- [ ] Write acquisition queue per Section 11
- [ ] Confirm Git working tree is clean before commit; commit with message: `inequality corpus: initial scaffold (3 entries + watch item + LAC placeholder)`
- [ ] Report back: any pre-existing files at target paths (do not overwrite without flagging); any references in user memories or staged DFD docs that should be reciprocally linked back to corpus entries

## 13. Notes

- Vector store integration is **out of scope** for this task — Debb owns that step. The markdown entries are designed to be ingestion-ready when the vector store is installed.
- All entries follow YAML frontmatter convention compatible with PROTO-RAG-001 (Debb's protocol). If a different frontmatter schema is in force, adjust on ingestion rather than on creation.
- The "automated life for capital" watch item is theoretically substantial but is **not** to be promoted to an active modeling commitment without Cath's explicit propagation judgment and confirmation from Héctor.
- Cross-reference back-links in existing DFD/fiscal-dominance docs can be added in a subsequent pass; this task scaffolds the corpus only.

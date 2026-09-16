---
type: corpus_entry
tier: working_note
project_scope: [DFD, BDH, Aurora]
authors: [Fernández-Villaverde, Jesús]
year: 2026
title: "Fernández-Villaverde (2026), 'A Recent Population History of Latin America and the Caribbean' — LAC-specific successor to the scenario-discipline cornerstone"
venue: "Presentation deck, University of Pennsylvania / NBER / CEPR, 15 September 2026"
doi: "n/a — local copy: _crossrefs/corpus/demographics/Slides_Latam.pdf"
date_added: 2026-09-15
added_by: Claude Code
endorsed_by:
build_instruction: "_crossrefs/_build_instructions/2026-09-15_demographics_fv_slides_latam.md"

indicators: [tfr, cbr, births, projection, migration, dependency_ratio, growth_accounting]
geography: [LAC regional, MEX, COL, CHL, CRI, PAN, BRA, ARG, URY, JAM, GTM, PRI, CUB, BOL, PER, NIC, DOM, BLZ, BHS; comparators USA, JPN, KOR, CHN, ITA, ESP]
scenario_implication: [fast-transition]   # confirms the standing discipline; does NOT trigger a re-baseline — see §Discriminator ruling
source_reliability: secondary   # academic synthesis of primary vital-registry / UNPD sources; deck, no methods appendix
data_vintage: 2026   # deck dated 2026-09-15; underlying registry values 2022–2025 by country
workflow_status: pending-endorsement
supersedes: "(none — extends, does not supersede, 2026-06-20_fernandez-villaverde-demographic-future.md)"
discriminator_ruling: "REPORT, not REVISION. A conference deck is not a WPP revision. The Revision Transition Protocol does not fire; nothing is re-baselined; WPP 2024 remains the standing UN projection reference (no WPP 2026 — next revision postponed to 2027, confirmed Q3)."
---

# Fernández-Villaverde (2026) — "A Recent Population History of Latin America and the Caribbean"

## One-line summary

The LAC-specific successor to the April cornerstone deck: Latin America's TFR is
already ≈ 1.50 on the countries' **own vital registries**, the UN WPP overstates
both births and the projected rebound, and the region will therefore age before it
gets rich — with Mexico in the deck's own framing as the case where Japan's
adjustment problem arrives without Japan's margins.

## Discriminator ruling (applied, not re-derived)

**REPORT / presentation, not a WPP revision.** The Revision Transition Protocol
does **not** fire. Nothing is re-baselined. The OLG / IM-6 calibration is
untouched. The standing UN projection reference remains **WPP 2024** — Q3
confirmed there is no WPP 2026 and the next revision is postponed to 2027.
This entry is a normal monitoring note routed to Anne's endorsement queue.

## Core conceptual contributions

### 1. LAC today, on national registries rather than the UN

Latest year available from each country's own registry (deck slide 8):

| Country | TFR | Year | | Country | TFR | Year |
|---|---|---|---|---|---|---|
| Puerto Rico | 0.87 | 2024 | | Brazil | 1.52 | 2025 |
| Chile | 0.99 | 2025 | | Dominican Rep. | 1.61 | 2024 |
| Colombia | 1.01 | 2025 | | Belize | 1.63 | 2024 |
| Costa Rica | 1.12 | 2025 | | Peru | 1.67 | 2024 |
| Bahamas | 1.15 | 2022 | | Panama | 1.79 | 2024 |
| Uruguay | 1.19 | 2024 | | Nicaragua | 1.80 | 2023 |
| Jamaica | 1.22 | 2025 | | Guatemala | 1.91 | 2024 |
| Argentina | 1.23 | 2024 | | Bolivia | 2.06 | 2024 |
| Cuba | 1.30 | 2024 | | **LAC** | **≈ 1.50** | 2024 |
| **Mexico** | **1.51** | **2025** | | *U.S.* | *1.60* | *2024* |

Only Haiti, Guyana, French Guiana and Saint Martin remain above replacement.
Speed is the second claim: Jamaica 2.45 → 1.22 in 35 years, Argentina 2.13 → 1.23
in **8 years**, Guatemala 3.8 → 1.9 in 20. The countries that started highest are
falling fastest, and the steepest declines are the most recent (Argentina, Chile,
Colombia, Costa Rica, Uruguay all fall off after 2015).

### 2. The case against the WPP — sharper than in the April deck

Three charges, of which the second and third are new relative to April:

1. **Birth estimates exceed registries** even where the UN itself rates
   registration above 90% complete. Colombia 2023: registry **515,549** against
   UNPD **705,000** — 37% too high.
2. **The projected rebound is mechanical.** Once a country enters the UNPD's
   "low fertility regime," its TFR follows a mean-reverting AR(1),
   f_{c,t+1} ~ N(μ_c + ρ_c(f_ct − μ_c), σ²), with μ_c ~ N(μ̄, σ²_μ) and
   μ̄ ~ U[0, 2.1]. The country mean μ_c does all the work, and the turn is
   **immediate**: China fell 0.54 over 2018–2023 and is projected to gain 0.05 by
   2028; South Korea fell 0.23, projected +0.07; Chile fell 0.37 and is projected
   to lose only 0.05 more. The uniform prior bounded at 2.1 is what forces every
   country back toward replacement.
3. **The 2024 out-of-sample test** (slide 16). All 37 countries with registries
   the UN deems ≥ 90% complete and population above one million, actual births
   against the July-2024 projection *for 2024*: only **4 of 37** came in above
   projection. Totals 16,052,498 actual against 17,699,000 projected — **−9.3%**,
   an absolute gap of **1.65 million births**. Colombia −36.5%, Guatemala −21.2%,
   Argentina −18.5%, Panama −17.0%, Chile −10.2%, Brazil −7.6%.

**Mexico is not in that table.** Worth noting precisely because it is the country
we calibrate: the deck's strongest quantitative indictment of the WPP does not
cover our case directly.

### 3. The rule of 85 as an arithmetic rail

Long-run population ≈ 85 × annual births; equivalently, once CBR falls below
1000/85 = **11.76 per thousand**, births are already insufficient to hold
population constant, which typically happens *after* TFR falls below replacement.
Applied regionally: LAC births peaked in 1990 at **12.0 M** (implying 1.02 bn);
they are now around **8 M**, implying **680 M** — and at LAC's actual e₀ of ~76
rather than 85, **608 M**, some 8% *below* today's 668 M. The deck explicitly
rejects ECLAC's projected regional peak of 730 M in 2053.

### 4. Mechanism — the bar, and the candidates

Any explanation must clear two criteria simultaneously: a **nearly universal**
negative trend with no sign of levelling, and **country-specific timing** differing
by decades. Most candidates deliver one, not both. Becker–Barro quality-quantity
(with Delventhal et al. 2021 adding skill-biased technology diffusion, Lucas 2009)
gets the timing but not the suddenness — no plausible calibration of the skill
premium delivers Colombia's 35% fall in births in ten years. Smartphones
(Myers & Hooper 2026, identifying off the 2007–2011 AT&T iPhone exclusivity, put
them at 33–52% of the general-fertility-rate decline among women 15–44) are read
as **accelerant rather than cause** — Italy was at 1.19 in 1995 and 1.14 in 2025.
Their real role is compressing norm diffusion: what took 25 years now takes 10.

The conjecture is **modernity** — a society organised around formal institutions,
specialised expertise and large-scale coordination — which makes the third child
expensive and childlessness cheap, and which is explicitly *not* a synonym for
capitalism (Hungary fell below replacement in 1960, Czechoslovakia in 1966).
Goldin (2026) supplies the gender-mismatch extension: women's opportunities expand
fast while expectations about housework and childcare lag, which is offered as the
reason cash transfers accomplish little while parental leave matters — the binding
constraint is who does the work of raising children, not the price of a child.

The integer-arithmetic slide is the most useful teaching device: moving a cohort
from completed fertility 1.80 to 1.30 requires no exotic behaviour, only shifting
mass from two and three children into zero and one.

### 5. No feedback mechanism

Explicitly aimed at economists' priors: markets self-regulate, but nothing
analogous pushes fertility back to replacement. The welfare theorems break down in
overlapping generations because generations far apart cannot trade — the double
infinity of agents and dated commodities kills the standard proof. Citing
Weil (2024): *the replacement rate has no special status as an attractor or
target.* This is the theoretical core of the DFD standing position that
CELADE/WPP medium-variant rebound assumptions are not empirically grounded.

### 6. Consequences — growth accounting and political economy

g_y = g_(y/l) + g_l, presented as arithmetic rather than a model. The U.S. goes
from 3% ≈ 2% + 1% around 2000 to 1.5% ≈ 2% + (−0.5%) by 2050. The Japan/U.S.
counterfactual (1991–2023, per hour worked) is the sharpest exhibit: Japan 0.79 =
1.22 + (−0.43), U.S. 2.60 = 1.62 + 0.98; swap only labour growth and Japan
counterfactually runs 2.20 against the U.S. 1.19 — the verdict reverses from the
U.S. leading by 1.8 pp/yr to lagging by 1.0 pp. On whether 2% productivity growth
even holds: semi-endogenous growth (Jones 1995), the empty planet (Jones 2022),
research productivity falling ~5%/yr (Bloom et al. 2020), and a tail argument —
South Korea's cohort fell 4.7-fold from 1,080,535 births (1960) to 230,028 (2023);
under a Gaussian tail the top individual moves only 4.84σ → 4.53σ, but under a
Pareto tail with α = 2 the cohort maximum falls from 883× to 407× the median.

The first-order problem is declared to be **political**, not productive: with
roughly as many retirees as workers, what each worker produces must be split in
two, and it does not matter whether that runs through PAYG taxes or capital income
in a funded system. "AI will fix this" misses that the redistribution problem is
about politics. The closing move is the one that matters for us: **Japan was the
easy case** — homogeneous, high-consensus, strong institutions, high income per
capita. Mexico and Tunisia face the same pressures in 30–40 years with
low-capability states, less consensus, a tradition of political conflict, and a
fraction of the income per capita.

## Relevance to project work

### DFD — confirms the standing discipline; no projection update

**Does this change the fast-transition scenario for Mexico? No.** The deck argues
for the position `DFD_TFR_forecast_instructions.md` v1.4 already encodes: CELADE
and UN WPP medium as the *optimistic* column by rule (§2), Central at
fast-transition TFR = 1.50, and the corpus README's standing principle that
fast-transition is the baseline rather than a stress test. Its §5 "no feedback
mechanism" argument is the theoretical statement of that rule. The April entry
reached the same verdict; this deck strengthens it rather than revising it.

**No cohort-component input moves.** Scenario definitions, the 2050 population
implications (140.4 M Central / 143.2 M Tempo-corrected / 128.9 M Stress), and
the fiscal-window values (Central TDR_min 42.0 at ~2038, grid window 2033–2038)
are untouched by this entry. The Q3 window-timing caveat continues to apply
wherever fiscal-space numbers are cited.

**The Rule-of-85 arithmetic is consistent with ours.** The deck applies the same
rail we adopted in Q3; our Mexico figure (125.4 M at e₀ = 75 on definitive 2024
births of 1,672,227) uses the same method the deck applies regionally.

### Re-anchor trigger check (Q3 §2) — **does not fire**

Q3 armed the trigger: *if INEGI publishes a TGF ≤ 1.50 for vintage 2024 or 2025,
the Central anchor goes to Anne.* Anne's pre-committed frame: published TGF in
[1.45, 1.50] → re-pin Central at the published value; below 1.45 → do not chase
the point estimate, open a fifth scenario row and keep Central at 1.50 as the
upper bracket.

The deck reports **Mexico 1.51 (2025)**. It misses on both legs:

1. **Threshold.** 1.51 > 1.50. One hundredth above, but the trigger is a stated
   threshold, not a neighbourhood.
2. **Source.** It is Fernández-Villaverde's own tabulation, `secondary` under the
   corpus source-reliability rule and absent from the Mexico source hierarchy's
   top tiers (§3 of the instructions: INEGI vital registries → INEGI census →
   CONAPO → CELADE → UN WPP). The trigger keys on an **INEGI publication**.
   Anne's sourcing rule 2 is explicit that secondary aggregators may corroborate
   but are not the citation.

**Recorded tension, not resolved here.** The deck's 1.51 (2025) sits *above* Q3's
registry-implied ≈ 1.46 (2024). The two are on different bases — Q3 scaled the
ENADID 2023 survey anchor by the ENR fertile-age rate decline; the deck is
presumably registered births over a projected denominator. The inconsistency is an
argument for waiting on INEGI, not for moving now. It sharpens Q4 follow-up 5
(watch INEGI for a 2024/2025 TGF publication) and follow-up 7 (the
occurred-vs-registered wedge).

### Anchor-file observation — BRA (routed to Anne)

The deck gives **Brazil 1.52 (2025, registry)**. The nearest downstream use is an
un-pinned **BRA 1.50 (2023, "IBGE estimación — pendiente source-pin Anne")**
carried in a six-country projection outside this corpus. The deck corroborates
the *level* and offers a two-year newer vintage, but cannot itself be the
citation. This attaches to an open judgment call already standing in Anne's May
brief (whether a sixth, non-priority row — Argentina or Brazil — is added to
`scenario_anchors.md`). Detail in `anne_slides_latam_anchor_brief.md` §2.

### BDH

The aging coda is the BDH-relevant half: the split-what-each-worker-produces
framing, the claim that the financing problem is political rather than
productive, and the explicit Mexico-is-not-Japan closing. The growth-accounting
arithmetic bears on financing capacity through total output rather than output per
capita — the deck's §6 point that bondholders and retirees are paid in levels, not
ratios, is the cleanest statement of why per-capita improvement does not discharge
a health-financing obligation.

### Aurora

"Modernity is largely incompatible with replacement-level fertility" is a
structural-foresight claim of exactly the Four Pillars type, and the terra-incognita
closing ("we do not have a map… the pretense of knowledge is the most dangerous
temptation") is usable framing. The Pareto-tail argument on shrinking cohorts —
that growth depending on a handful of exceptional innovators is hurt most by
cohort contraction — is a genuine input to the post-LLM intelligence thread.

## Open methodological questions surfaced

- **Regional rail, currently out of scope.** The deck's LAC aggregate
  (608–680 M against ECLAC's 730 M peak in 2053) has no counterpart in DFD, which
  has been Mexico-only since the v1.2 scope narrowing. If a regional population
  rail is wanted downstream, that is a scope decision, not a recalibration.
- **Mexico's absence from the slide-16 out-of-sample test.** The deck's strongest
  quantitative WPP indictment covers 37 countries but not ours. Whether Mexico
  fails the same test is checkable against INEGI definitive 2024 births versus the
  July-2024 WPP vintage — a candidate Q4 item, not opened here.
- **Tempo, unchanged.** The deck concedes only "a small rebound from tempo effects
  and, short of a large change in society, not much more," and puts LAC at ~1.2.
  That is the same direction as the standing DFD position (§1 of the instructions)
  and moves nothing on the tempo-corrected column's promotion conditions.
- **Candidate watch item, not opened:** the Goldin (2026) gender-mismatch
  mechanism predicts a paradoxical reversal — societies with the most unbalanced
  gender norms start with the highest TFRs and end with the lowest. If that holds,
  it is a *structural* argument for LAC overshooting below East Asia rather than
  stabilising with it, which would bear on the Stress column's floor (currently
  anchored to Chile 1.03). Anne's call whether this rises to a
  `research_watch_item`.

## Source quality

- **Reliability:** `secondary`. Presentation deck, no methods appendix, consistent
  with how the April deck was filed. Specific load-bearing figures must be traced
  to underlying primaries before citation inside IM-6 or any deliverable — the
  same discipline flag the April entry carries.
- **Recency:** compiled 15 September 2026; per-country registry vintages run
  2022–2025, several more recent than our own anchor rows.

## Citation

Fernández-Villaverde, J. (2026). *A Recent Population History of Latin America and
the Caribbean.* Presentation deck, University of Pennsylvania, NBER, and CEPR,
15 September 2026. Local copy:
`_crossrefs/corpus/demographics/Slides_Latam.pdf`.

## Cross-references

- → Build instruction: `_crossrefs/_build_instructions/2026-09-15_demographics_fv_slides_latam.md`
- → Predecessor / cornerstone (extended, not superseded): `_crossrefs/corpus/demographics/2026-06-20_fernandez-villaverde-demographic-future.md`
- → Re-anchor trigger of record: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q3_demographic_replicate.md` §2, §7
- → Scenario anchors (MEX row unchanged at 1.60/2023; BRA question routed): `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Governing instructions (no version bump): `_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md` (v1.4)
- → Anne brief opened from this entry: `_crossrefs/corpus/demographics/_pending/anne_slides_latam_anchor_brief.md`
- → Related entry (complementary framing; reversibility thread): `_crossrefs/corpus/demographics/observations/2026-07-11_unfpa-demographic-futures-survey.md`
- → Project corpus cross-refs (append on endorsement, per §Routing):
    - DFD: `GrandPlan/DFD/docs/corpus/_cross_references.md`
    - BDH: `GrandPlan/BDH/docs/corpus/_cross_references.md`
    - Aurora: `GrandPlan/Aurora/docs/corpus/_cross_references.md`

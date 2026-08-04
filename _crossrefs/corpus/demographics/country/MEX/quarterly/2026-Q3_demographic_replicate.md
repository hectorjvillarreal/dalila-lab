---
type: working_note
tier: working_note
project_scope: [DFD, BDH]
authors: [Claude Code]
year: 2026
title: "2026-Q3 demographic replicate — México"
venue: "Internal — DFD calibration / demographics corpus"
doi: "n/a"
date_added: 2026-08-03
added_by: Claude Code
endorsed_by: "(pending — Anne, Cath)"
governing_instructions: "_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md (v1.3)"
build_instruction: "_crossrefs/_build_instructions/2026-08-03_demographics_MEX_2026Q3_replicate.md"
workflow_status: pending_endorsement
quarter: 2026-Q3
country: MEX
---

# 2026-Q3 demographic replicate — México

**Quarter:** 2026-Q3 (reference period: July–September 2026)
**Status:** Second replicate against the 2026-Q2 baseline.
**Date produced:** 2026-08-03 — produced early in the reference period on
Héctor's request; target completion per protocol was October 15. Data
cutoff 2026-08-03.
**Scope:** México only (per v1.2 scope narrowing, carried in v1.3).

---

## 1. Data vintage table

| Indicator | Value used | Vintage | Source | Δ vs. Q2 |
|---|---|---|---|---|
| Period TFR (anchor) | 1.60 | 2023 | INEGI, ENADID 2023 (Comunicado 305/24) | unchanged — ENR 2024 definitive confirms no TGF retabulation |
| Period TFR (registered-births proxy) | **≈1.46** | 2024 | Derived: 1.60 × (47.7/52.2), ENR fertile-age rates | **new** — see §2 caveats |
| Annual births (Rule of 85) | **1,672,227** | 2024 definitive | INEGI ENR 2024 (Comunicado 129/25, 25 sep 2025) | **−8.2%** vs. 1,820,888 (2023) |
| Coupling rate proxy | married 36.3% + unión libre 17.6% = 53.9% (adults, national) | 2025 | INEGI, EAP Día Internacional de la Juventud 2025 (ENOE-based) + situación conyugal series | **partial retrieval** (Q2: none) — see §3 |
| Life expectancy at birth | e₀ = 75.63 (F 79.24 / M 72.75) | 2026 (CONAPO projection-year value) | CONAPO, comunicado esperanza de vida / proyecciones 2020–2070 | **new anchor** — validates stylized e₀ ≈ 75; survival ratios still pending |
| Mortality schedule | Coale-Demeny West e₀ ≈ 75 (unchanged) | n/a | Stylized | CONAPO life-table extraction still pending → Q4 |
| Net migration | 0 (assumption, unchanged) | n/a | — | not retrieved this quarter |
| Population age structure (baseline for projections) | 2023 structure, 129.74 M (unchanged) | 2023 | OWID / UN WPP 2024 | INEGI/CONAPO 5-yr retabulation still pending → Q4 |
| Current age structure (observed check) | 0–14: 24%, 15–64: 67%, 65+: 9% | 2026 | CONAPO proyecciones (via press; primary tables queued) | **new** — see §4 |
| CELADE comparator (2024) | still pending Excel/annex extraction | 2024 | CELADE OD 2025 (29 oct 2025) | carried; annex retrieval attempted 2026-08-03, not completed |
| UN WPP revision check | **No WPP 2026 — next revision postponed to 2027.** WPP 2024 remains the reference. | checked 2026-08-03 | UN Population Division | no Revision Transition Protocol fired |
| CONAPO comparator | TGF 1.84 (2026), 1,996,102 projected births (2026), 134.4 M mid-2026 | 2026 | CONAPO mid-2026 projections (press-derived; primary read queued Tier-2) | **new** |

**Source-hierarchy compliance (v1.3 §3):** Births anchor uses INEGI vital
registry (tier 1). TFR anchor uses INEGI survey (tier 1). e₀ anchor now uses
CONAPO (tier 3), replacing a purely stylized value. Age-structure baseline
for the cohort-component machinery remains UN WPP 2024 via OWID (tier 5) —
still flagged; INEGI census-derived 5-yr groups remain the Q4 priority.

---

## 2. TFR update

| Measure | Value | Source / vintage |
|---|---|---|
| Mexico observed period TFR (anchor) | **1.60** | INEGI ENADID 2023 — unchanged |
| Registered-births implied proxy, 2024 | **≈1.46** | Derived from ENR fertile-age rate decline (52.2 → 47.7, −8.6%) applied to the 2023 anchor |
| Change vs. last quarter | anchor unchanged; proxy is new information | — |
| CELADE OD 2025 estimate for Mexico, 2024 | still pending extraction | carried from Q2 |
| CONAPO projected TGF | 1.84 (2026) | press-derived; ≈0.4 above the implied proxy |

**The load-bearing development this quarter.** ENR 2024 definitive puts the
2024 registered-births rate 8.6% below 2023. Mechanically scaling the 1.60
anchor gives an implied 2024 period TFR of ≈1.46 — **at or below the Central
scenario's 1.50**. Caveats, in order of importance: (i) registered ≠
occurred births — late registration means the occurred-2024 count will
revise up somewhat; (ii) the ENR rate uses all women 15–49 without age
structure, so it is a crude proxy, not an ASFR-based TGF; (iii) the anchor
itself is survey-based (ENADID) while the proxy is registry-based — the two
bases are not strictly commensurable. The proxy is therefore reported as a
**directional signal, not a re-anchor**. It says the fast-transition Central
scenario (TFR = 1.50) is no longer conservative-looking; it may already be
the observed level.

**Re-anchor trigger (for Anne):** if INEGI publishes a TGF ≤ 1.50 for
vintage 2024 or 2025 (ENADID successor, conciliación update, or ENR
retabulation), the Central scenario anchor should be re-examined — either
re-pin Central at the published value or open a fifth scenario row. That is
a scenario-structure decision and sits with Anne per §Domain Authority.

---

## 3. Coupling rate update

**Partial retrieval this quarter** (Q2: none). The exact target — marriage +
cohabitation among 20–39, sex-disaggregated, from ENOE microdata — was not
tabulated, but INEGI's 2025 publications pin the direction and magnitude:

- Situación conyugal, national adults (ENOE-based): **married 47.6% → 36.3%**
  between 2005 and 2025 (−11.3 pp); **unión libre 11.1% → 17.6%** (+6.5 pp).
  Combined partnered share: **58.7% → 53.9%** (−4.8 pp over 20 years) — the
  rise in cohabitation offsets less than half the marriage decline.
- Youth 15–29 (EAP Juventud 2025): **68.7% single** (men 75.6%, women 61.7%).
- Registered marriages 2024: **486,645**, continuing the secular decline.

**Assessment:** no stabilization signal. The partnered share among adults is
still falling and singlehood among the entry cohorts (15–29) is high with a
large sex asymmetry. The standing-considerations §1 item 1 argument (falling
coupling → permanent fertility loss, not postponement) is **reinforced**,
not weakened, by this quarter's retrieval.

**Q4 acquisition target (carried, sharpened):** ENOE microdata cut —
marriage + cohabitation among 20–39, sex-disaggregated, two vintages
(2023 vs. latest) to get a rate of change on the DFD-relevant age band.

---

## 4. Dependency ratio update — current

CONAPO's 2026 projection-year structure (0–14: 24%, 15–64: 67%, 65+: 9%,
press-derived, shares rounded to integers) implies:

| Ratio | 2026 (per 100 working-age) | Q2 baseline (2023) |
|---|---|---|
| YDR = pop(0–14)/pop(15–64) × 100 | **≈35.8** | 37.1 |
| OADR = pop(65+)/pop(15–64) × 100 | **≈13.4** | 11.9 |
| TDR | **≈49.3** | 49.0 |

**Caution — do not over-read.** Integer-rounded shares put ±~2 points of
slack on the implied TDR, and the CONAPO base (conciliación demográfica) is
not the same base as the replicate's cohort-component machinery (WPP 2024
via OWID). The Central-scenario path interpolates to TDR ≈ 46–47 at 2026;
the CONAPO-share figure of ≈49 is above that. The direction of movement
(YDR falling, OADR rising) matches the projection; the level discrepancy is
within the rounding-plus-base wedge but should be **resolved in Q4 by
retabulating the current structure from INEGI/CONAPO 5-yr tables** rather
than press shares. Flagged for Cath's read of the fiscal-window timing: if
the true 2026 TDR is ≈49 rather than ≈46, the descent into the window is
lagging the Central path by roughly one projection step.

---

## 5. Scenario comparison table

**No change to the cohort-component inputs this quarter** — the scenario TFR
definitions are fixed by instructions v1.3, the 2023 base age structure is
unchanged (retabulation pending), and mortality remains Coale-Demeny West
e₀ ≈ 75 (now validated by CONAPO's e₀ = 75.63 for 2026; the stylized value
is 0.6 years conservative). **The Q2 projection tables therefore carry
forward unchanged** as the operational reference:

| Scenario | 2050 population | TDR min (year) | Fiscal window |
|---|---|---|---|
| Optimistic (TFR = 1.65) | 144.6 M | 44.1 (~2033) | 2028–2038 (≈10 yr) |
| **Central (TFR = 1.50)** | **140.4 M** | **42.0 (~2038)** | **2033–2038 (≈5 yr)** |
| Tempo-corrected (TFR = 1.60) | 143.2 M | 43.6 (~2033–2038) | 2028–2038 (≈10 yr) |
| Stress (TFR → 1.0 by 2030) | 128.9 M | 36.3 (~2038) | 2038–2043 (≈5 yr) |

Full year-by-year tables: see the 2026-Q2 baseline replicate §5.

> **This is the reform window. Policy interventions that require fiscal
> space are most feasible during this interval.** (Central: ~2033–2038,
> TDR_min ≈ 42.0 — unchanged from Q2.)

**Positioning note:** with the 2024 implied-TFR proxy at ≈1.46, observed
fertility now sits **between the Central and Stress columns**, closer to
Central. The scenario family still brackets the data; no scenario
re-specification is proposed this quarter (see §2 re-anchor trigger).

---

## 6. Tempo-correction note (Fischer-Dattani caution)

Evidence this quarter moved **against** promotion of the tempo-corrected
column:

1. **Coupling.** The §3 retrieval shows the partnered share still falling
   and 68.7% of 15–29-year-olds single. Promotion condition (ii) —
   ENOE evidence of coupling stabilization — is **not met**.
2. **Births.** An 8.2% single-year drop in registered births with the
   fertile-age female denominator roughly stable is the opposite of a
   tempo-recovery signature at the aggregate level.
3. **Correction magnitude.** No Mexico-specific completed-cohort estimate
   appeared this quarter; promotion condition (i) (correction > +0.15)
   remains untestable. The Q2 watch-item candidate (LAC-specific
   Fischer-Dattani magnitude) stays open.

The tempo-corrected column remains **reported, not operational**.

---

## 7. Calibration flag

**IM-6 demographic inputs require updating before next model run: NO NEW
CHANGES beyond the Q2 mandate** (which stands: 2023 age-structure starting
state, Central TDR path 49.0 → 42.0 → 49.1, stylized survival ratios pending
CONAPO extraction).

New this quarter, for the record and for downstream users:

- **Rule-of-85 long-run anchor falls.** With definitive 2024 births
  (1.672 M): **125.4 M** at e₀ = 75; **126.5 M** at CONAPO's e₀ = 75.63;
  **133.8 M** at e₀ = 80. The Q2 anchor (136.5 M on 2023 births) is
  superseded. The long-run stationary population is now **~14 M below** the
  Central-scenario 2050 level (140.4 M), i.e., 2050 carries more
  transitional inertia and the post-2050 decline is steeper than the Q2
  reading implied.
- **e₀ validation.** CONAPO 2026 e₀ = 75.63 confirms the stylized e₀ ≈ 75 is
  approximately right *today* — but the machinery still assumes no mortality
  improvement to 2050, which remains conservative on the dying side.
- **Re-anchor trigger armed** (§2): a published 2024/2025 TGF ≤ 1.50 sends
  the Central anchor to Anne for re-examination.

---

## 8. Promotion recommendation

**Recommendation:** promote to the demographics corpus after Anne's
endorsement of §§1–7 (scenario positioning, re-anchor trigger, coupling
assessment) and Cath's endorsement of §4's TDR-level discrepancy note and
the unchanged fiscal-window characterization.

**PROTO-RAG-001 conformance:** this replicate adopts **option (a)** from the
Q2 §8 note *provisionally* — a per-quarter build instruction is filed at
`_crossrefs/_build_instructions/2026-08-03_demographics_MEX_2026Q3_replicate.md`
and referenced in frontmatter. The (a)-vs-(b) policy decision remains with
Anne / Debb; if (b) is chosen later, the frontmatter reverts to
`governing_instructions:` only.

---

## Outstanding follow-ups for Q4 (target: January 15, 2027)

1. **CELADE OD 2025 Excel/annex extraction** — MEX 2024 comparator (carried
   third time; retrieval attempted 2026-08-03, not completed). Alternatively
   close via OD 2026 if published ~October 2026 — check for a successor
   publication, which would also trigger the anchors-file comparator-column
   expansion build.
2. **ENOE 20–39 marriage + cohabitation microdata cut** — sharpened spec in
   §3; needed for the tempo-promotion conditions and the coupling watch.
3. **CONAPO life tables** — extract survival ratios (sex-disaggregated) to
   replace Coale-Demeny West; e₀ anchor already pinned at 75.63.
4. **Age-structure retabulation** — INEGI/CONAPO 5-yr groups for both the
   projection base and the §4 observed-TDR check (resolves the ≈46 vs. ≈49
   discrepancy).
5. **Watch INEGI for a 2024/2025 TGF publication** — re-anchor trigger (§2).
6. **CONAPO primary tables read** — replace press-derived comparators
   (TGF 1.84, births 1.996 M, e₀ 75.63) with values cited from the
   proyecciones 2020–2070 / conciliación tables directly (Tier-2 queue item
   of 2026-08-03).
7. **Occurred-vs-registered wedge** — pull nacimientos ocurridos tabulados
   for 2023–2024 to size the late-registration revision risk on the −8.2%.

---

## Cross-references

- → Governing instructions (v1.3): `_crossrefs/corpus/demographics/country/MEX/DFD_TFR_forecast_instructions.md`
- → Build instruction: `_crossrefs/_build_instructions/2026-08-03_demographics_MEX_2026Q3_replicate.md`
- → Q2 baseline replicate (superseded §10 anchor; standing scenario tables): `quarterly/2026-Q2_demographic_replicate.md`
- → ENR 2024 corpus entry (births source of record): `_crossrefs/corpus/demographics/_pending/2026-08-03_inegi-enr2024-mex-births.md`
- → Scenario anchors (MEX row unchanged): `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Standing reference: Fernández-Villaverde (2026), "The Demographic Future of Humanity" (GrandPlan/DFD/docs/corpus/JFV_260401.pdf)

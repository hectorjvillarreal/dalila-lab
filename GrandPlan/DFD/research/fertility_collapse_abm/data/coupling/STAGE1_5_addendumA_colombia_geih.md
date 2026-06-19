# Stage 1.5 Addendum A — Colombia GEIH via DANE Catálogo Central de Datos
# Project: Rapid Fertility Collapse in Latin America (ABM paper, DFD parallel research)
# Author: Anne and Nina (DFD Core Team)
# Date: 2026-06-18
# For: Claude Code on Dalila
# Location: GrandPlan/DFD/research/fertility_collapse_abm/data/coupling/

---

## Why this addendum

Stage 1.5 reported Colombia GEIH as login-blocked (`auth/login`). That was the wrong
door. The **DANE Catálogo Central de Datos** at `microdatos.dane.gov.co` exposes GEIH
microdata for **direct download** (SPSS `.sav` or fixed-width TXT) without the login
wall that blocked the earlier attempt. This addendum redirects the Colombia extraction
to that route. It does not replace Stage 1.5; it unblocks the second collapse country
that makes the gate decidable.

Colombia is the highest-value unblock for one specific reason: it is the only collapse
country where we hold an **observed annual national TFR** (DANE EEVV, 1.7→1.1, verified
in Stage 1) to pair against the coupling path. That makes Colombia the one case where
the **Q1 lead test** — coupling leads TFR — is properly evaluable. Mexico could not
give us this (modeled CONAPO TFR); Costa Rica's blended series gave a null. Colombia
is where the mechanism's core causal claim can actually be tested.

---

## Acquisition route

1. Catalog: `microdatos.dane.gov.co` (Catálogo Central de Datos / NADA instance).
2. Operation: **GEIH — Gran Encuesta Integrada de Hogares.** Also check whether the
   catalog still lists the pre-2021 GEIH and the post-2021 **GEIH redesign** as
   separate operations (see comparability flag below).
3. Download the **Características generales (personas)** module per period — this
   carries age, sex, and marital/union status. Format: prefer SPSS `.sav` (labeled
   categories reduce miscoding risk); TXT acceptable with the layout file.
4. GEIH is **monthly continuous**. Build each annual value by pooling all twelve
   months of person-records for that year and applying the survey expansion factor
   (`fex_c` / the period's weight variable — confirm the exact name per vintage).

---

## The target series (unchanged from Stage 1.5)

Annual share of **women aged 20–39 in a co-residential union (married OR cohabiting)**,
disaggregated by:
- 5-year band: 20–24, 25–29, 30–34, 35–39
- union type: married (`casado/a`) vs. cohabiting (`unión libre`) separately

Output: `COL_coupling_annual.csv`, same schema as the Costa Rica file
(`year`, `age_band`, `union_total`, `married`, `cohabiting`, `observed_or_interpolated`,
`source`, `coverage_flag`), PROTO-RAG-001 sidecar per Debb's rule.

---

## Two checks that are load-bearing for Colombia specifically

### Check A — the 2021–2022 GEIH redesign (comparability break)
GEIH underwent a methodological redesign around 2021–2022 that **renamed and recoded
variables**, including geographic and household-roster fields. The marital/union-status
variable name and its category coding may differ across the break. This is exactly the
kind of redefinition Anne's forensic discipline exists to catch: **a renamed or recoded
union variable can masquerade as a coupling discontinuity.**

Required: map the union-status variable and its categories on **both sides** of the
redesign, confirm the `unión libre` / `casado` / `soltero` / `separado` / `viudo`
categories are consistently defined, and flag the splice year explicitly in the CSV
`coverage_flag` column. If the categories are not reconcilable, treat pre- and
post-redesign as two series and say so — do not silently splice them.

### Check B — pair with OBSERVED annual TFR, not modeled
Run the Q1 lead test against the **DANE EEVV observed annual TGF** from Stage 1
(`COL_*.csv`, the 1.7→1.1 series), never against World Bank or any modeled/smoothed
projection. The lead test is only meaningful against observed TFR. This is the
methodological point that made Mexico's Q1 unevaluable; Colombia must not repeat it.

---

## Identification questions — what Colombia must answer

Re-run the four Stage 1.5 questions for Colombia, with Q1 now properly evaluable:

- **Q1 (lead):** does the coupling path turn down *before* the observed DANE TFR?
  Report the best-aligned lag `k` and the correlation. This is the test Costa Rica
  could not pass cleanly and Mexico could not run at all.
- **Q2 (nonlinearity locus):** is the nonlinearity in coupling itself (accelerating
  partnership decline, Mexico-like) or in the coupling→fertility map (smooth coupling,
  sudden TFR, Costa-Rica-like)? Colombia is the tie-breaker between the two patterns
  the first two countries disagreed on.
- **Q3 (cascade):** does the decline appear youngest-first (20–24 leading 25–29
  leading 30–34)?
- **Q4 (independence):** confirm coupling is from the GEIH household roster, fully
  independent of EEVV vital registration. (Expected pass — different instruments.)

---

## Gate arithmetic after Colombia

- If Colombia is cleanly identifiable **and shows a coupling→TFR lead**, the gate
  reaches two collapse countries (Costa Rica partial + Colombia) and Nina can move to
  freeze the Stage 2 spec — built as the **nesting model** (nonlinearity locus chosen
  empirically), per Nina's revised recommendation.
- If Colombia also comes back mixed or map-side, that is still a result: it tells us
  the lead is genuinely weak across collapse countries, and the mechanism is the
  fertility-response map, not partnership formation. Either outcome is decidable.
- The nonlinearity-locus disagreement between Costa Rica (map-side) and Mexico
  (coupling-side) makes Colombia the empirical tie-breaker. Whichever side Colombia
  lands, it sharpens the Stage 2 spec.

---

## Note on the other two blocked countries

Argentina (flaky INDEC REDATAM, public base stops 2014) and Chile (flaky REDATAM,
open ECLAC host periodic to 2011) remain blocked. **Do not let them hold up the gate.**
If Colombia unblocks cleanly, the two-country gate is met without them; Argentina and
Chile can be pursued in Stage 2 as the model is calibrated, via bulk-microdata fallback
rather than the REDATAM engine. They are enrichment, not gate-critical.

---

## Marriage-margin refinement (carry from Stage 1.5, applies to Colombia too)

When building `COL_coupling_annual.csv`, preserve the married/cohabiting split so the
**marriage-weighted union** measure Nina flagged can be tested. Anne's caution stands:
modern cohabitation in LAC may be an increasingly low- or deferred-fertility state, so
the fertility-relevant coupling variable may be marriage-weighted rather than total
union. Colombia's high baseline cohabitation makes it an especially good test of this.

---

*Stage 1.5 Addendum A. Version 1.0, 2026-06-18.*
*Companion to STAGE1_5_coupling_identification.md and STAGE1_5_identification_memo.md.*
*Gate unchanged: Anne and Nina review the updated synthesis before Stage 2 freeze.*

---
type: corpus_entry
tier: working_note
project_scope: [DFD]
authors: [Claude Code (Stage 1.5 execution)]
year: 2026
title: "Stage 1.5 Identification Memo — coupling-path acquisition and the threshold-mechanism gate"
venue: "DFD parallel research, internal"
date_added: 2026-06-18
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_5_coupling_identification.md"
---

# Stage 1.5 Identification Memo — Rapid Fertility Collapse ABM

**Project:** Threshold-coupling ABM of rapid fertility collapse (DFD parallel research)
**Stage:** 1.5 of 4 — coupling microdata acquisition + identification forensics (GATE before Stage 2 ABM spec)
**Prepared for:** Anne (population economics) and Nina (ABM lead)
**Date:** 2026-06-18
**Data location:** `GrandPlan/DFD/research/fertility_collapse_abm/data/coupling/`

---

## Gate verdict (read first) — UPDATED after Colombia (Addendum A)

**The gate is now DECIDABLE, and it resolves to the MAP side.** Colombia — the second collapse
country and the only one with an **observed** annual national TFR to pair against coupling — has
been extracted (DANE GEIH 2007–2024, via the Catálogo Central de Datos; the earlier login wall was
the wrong door). With **two collapse countries now in hand (Costa Rica + Colombia)**, the gate's
≥2-country requirement is met, and both point the **same** way:

- **The threshold-in-partnership-formation hypothesis is NOT supported.** In neither collapse country
  does coupling *lead* TFR (Q1) or decline cleanly *youngest-first* (Q3). Colombia, the one place the
  lead test is properly evaluable, shows **no clean lead — if anything coupling lags** the TFR turn.
- **A different, consistent pattern emerges instead: the nonlinearity sits in the coupling→fertility
  MAP (Q2).** Costa Rica (smooth coupling, sudden TFR) and Colombia (total union flat ~59–60% for
  twelve years, then a modest −6 pt drift, against a 1.7→1.1 TFR collapse) agree. Mexico — the
  *slow-decline comparator, not a gate country* — is the lone coupling-side case and no longer drives
  the locus decision.
- **The marriage margin is the live sub-mechanism (Anne's caution, now empirically central).** In both
  countries total co-residential union is far more stable than *marriage*: Colombia's marriage share
  halves (20.7%→11.9%) under a flat total, cohabitation substituting. If marriage and cohabitation
  differ in fertility intensity, the behaviorally-relevant coupling variable is **marriage-weighted**,
  not total union.
- **Q4 independence holds universally** — coupling from survey rosters, TFR from vital registration.

**Recommendation: the gate can be cleared to proceed.** Nina may freeze the Stage 2 spec as the
**nesting model** (per her revised recommendation), with the nonlinearity locus **empirically resolved
to the map side** and the marriage-weighted coupling measure as the primary state variable to test.
Argentina and Chile remain blocked but are now **enrichment, not gate-critical** — the two-country
gate is met without them. This is the addendum's explicitly-anticipated second decidable branch:
*"the mechanism is the fertility-response map, not partnership formation."*

---

## Data acquisition status

The priority series (annual share of women 20–39 in co-residential union, by 5-yr band, married vs
cohabiting) was pursued per the Stage 1.5 source plan. Outcome by country:

| Country | Source | Method | Result |
|---|---|---|---|
| **Costa Rica** | ENAHO 2010–2024 | INEC **REDATAM** server-side crosstab (no login) | ✅ **Full annual series** (`CRI_coupling_annual.csv`) |
| **Mexico** (comparator) | ENOE 2005–2024 | INEGI **microdata** download (open) | ✅ **Biennial series, 9 yrs** (`MEX_coupling_annual.csv`); 2021 dropped (ETOE/COVID) |
| **Colombia** | GEIH 2007–2024 | DANE **Catálogo Central de Datos** microdata download (no login) | ✅ **Full annual series, 18 yrs** (`COL_coupling_annual.csv`) — Addendum A |
| **Argentina** | EPH | INDEC REDATAM | ⛔ **Blocked** — engine 500s to scripted requests; base `EPH_BASE_FINAL` covers only 2003–2014. *Now enrichment, not gate-critical.* |
| **Chile** | CASEN | ECLAC/INE REDATAM | ⛔ **Blocked** — engine 500s; ECLAC host carries only CASEN 1990–2011 (periodic). *Now enrichment, not gate-critical.* |

**Method note (reproducible):** the Costa Rica path drives INEC's RedatamX web engine
(`RpWebStats.exe/CrossTab`) to produce a weighted crosstab of estado conyugal × 5-yr age band,
filtered to women, weighted by the expansion factor — server-side, no microdata download, no login.
Extractors: `_extract_redatam_cri.py` (CR), `_extract_enoe_mex.py` (MX), `_extract_geih_col_v2.py`
(CO). **Colombia method (Addendum A):** GEIH person microdata pulled directly from the DANE Catálogo
Central de Datos (NADA), all 12 months/year pooled with the expansion factor; weighted share of women
20–39 with P6070 (estado civil) in {1,2}=cohabiting / {3}=married. The v2 extractor auto-detects the
schema across the 2021–22 "Marco 2018" redesign (sex P6020→P3271, weight Fex_c_2011→FEX_C18; **P6070
union coding is identical across the break — Check A clean**) and pools Cabecera+Resto (national
partition) while dropping the redundant Área cut. The blocked-country extractors
(`_extract_redatam_arg.py`) remain ready for the enrichment pass. **Environmental finding:** background
agents have no network egress here, so all extraction runs from the main session — ARG/CHL REDATAM
servers proved unreliable to scripted clients, unlike CR's INEC server and DANE's NADA download.

---

## Per-country findings

### Costa Rica — collapse case, full annual series (the anchor result)

Coupling (women 20–39, co-residential union): **52.4% (2010) → 40.1% (2024), −23%**. TFR
**1.83 → 1.12, −39%**. By band 2010→2024: 20–24 32→21%, 25–29 51→36%, 30–34 66→46%, 35–39 69→57%.

- **Q1 (lead):** best alignment is **simultaneous** (k=0, r=+0.24); no lead detected. Per the spec,
  simultaneity *weakens* the "coupling drives fertility" causal story.
- **Q2 (nonlinearity):** coupling falls **smoothly** while TFR falls harder with a late acceleration
  (2019–21) ⇒ the nonlinearity appears to sit in the **coupling→fertility map**, not in coupling.
- **Q3 (cascade):** **no clean youngest-first ordering** (steepest-decline years scattered across bands).
- **Q4 (independence):** ✅ ENAHO roster vs vital registration.
- **Compositional caveat (load-bearing):** the total-union decline is driven by a **marriage collapse**
  (30–34 married 43→22%) with **flat/rising cohabitation** — the substitution the spec warned against.
  Total union still falls 11–20 pts after accounting for it, but the *marriage* margin is far sharper.
- **Verdict: PARTIALLY IDENTIFIABLE** — independence solid, decline real, but lead and cascade absent
  in the annual aggregate. Caveats (annual sampling noise on 15 points; aggregate masking the marriage
  margin) could be hiding a signal — see Stage 2 refinements.

### Mexico — comparator (NOT a gate country)

Coupling (women 20–39): **61.7% (2010) → 54.1% (2024), −12%**. CONAPO TFR 2.37→1.89, −20%.

- **Q2:** coupling decline **accelerates** (annualized −0.3→−1.0 pts/yr, 2013→2024) — a genuine
  nonlinearity *in coupling itself*, unlike Costa Rica.
- **Q3:** recent decline **concentrated in younger bands** (20–24 −1.6/yr, 25–29 −2.3/yr vs 35–39 −0.6/yr)
  — weakly youngest-first by magnitude.
- **Q1:** **uninformative** — n=6 biennial points against a *modeled/smooth* CONAPO TFR; the lead test
  is not meaningfully evaluable.
- **Q4:** ✅ ENOE roster vs CONAPO/vital.
- **Verdict (soft):** more threshold-like than Costa Rica (accelerating, youth-concentrated), but
  unverifiable on lead and built on biennial data. Useful as the tipping-point diagnostic, not for the gate.

### Colombia — collapse case, full annual series, the OBSERVED-TFR tie-breaker (Addendum A)

Coupling (women 20–39, co-residential union): flat plateau **~59–60% (2008–2020)**, then a downturn
to **54.0% (2024)** — a ~6 pt (−11%) drop concentrated in 2021–2024. *Observed* DANE EEVV TFR
**1.7 (2015–18) → 1.1 (2024), −35%**. Marriage share (20–39): **20.7% (2008) → 11.9% (2024)** — a
secular halving under the stable total, cohabitation substituting. (2007 = 47.5% is an anomalous
earliest point — likely frame/questionnaire difference — so read the plateau as 2008–2020.)

- **Q1 (lead) — NO clean lead; if anything coupling LAGS.** This is the one country where the test is
  properly evaluable (observed annual TFR, not modeled). Total union holds its plateau through 2020
  and breaks only in 2021, *after* TFR has already begun sliding (1.7→1.5 by 2020). The differenced
  correlation's best alignment is a **lag** (k=−2, r=+0.93); the precise lag is fragile (TFR is
  chart-label rounded to 1 decimal, n=9 differences), but the direction is clear: coupling does not
  lead. This is the test Costa Rica could not run cleanly and Mexico could not run at all.
- **Q2 (nonlinearity) — MAP-SIDE, decisively.** A small, smooth coupling change (~6 pts, ~11%) maps to
  a large TFR collapse (−35%). The nonlinearity sits in the coupling→fertility **map**, not in coupling.
  **Colombia agrees with Costa Rica, not Mexico** — this is the empirical tie-breaker.
- **Q3 (cascade) — synchronized, not clean youngest-first** (25–29 and 30–34 turn in 2021, 20–24 in 2022).
- **Q4 (independence):** ✅ GEIH household roster (P6070) vs DANE EEVV vital registration — different instruments.
- **Compositional caveat (load-bearing, as in CR):** the marriage margin moves far more than total union —
  the marriage-weighted coupling measure is the one to carry into Stage 2.
- **Verdict: PARTIALLY IDENTIFIABLE, map-side** — same shape as Costa Rica. Independence solid, decline
  real, lead absent, nonlinearity in the map.

### Argentina / Chile — blocked at acquisition (now enrichment, not gate-critical)

No annual coupling series obtained, and **no longer gate-critical** — the two-country gate is met by
Costa Rica + Colombia. **Argentina** INDEC REDATAM 500s and its public base stops at 2014
(pre/early-collapse only; public base `EPH_BASE_FINAL`); **Chile** REDATAM 500s and the open ECLAC
host carries only periodic CASEN 1990–2011. Both can be pursued in Stage 2 via bulk-microdata fallback
as the model is calibrated, to widen the collapse-country panel.

---

## Cross-country synthesis (Q1–Q4)

| | Costa Rica (collapse) | **Colombia (collapse)** | Mexico (comparator) | ARG / CHL |
|---|---|---|---|---|
| Q1 lead | ✗ simultaneous | ✗ **no lead / lags** (observed TFR) | — not evaluable | no data |
| Q2 nonlinear | map-side (smooth coupling) | **map-side (flat coupling, TFR collapse)** | ✓ accelerating coupling | no data |
| Q3 cascade | ✗ no clean order | ✗ synchronized 2021–22 | ~ youth-concentrated | no data |
| Q4 independent | ✓ | ✓ | ✓ | (endpoints only) |
| **Verdict** | **PARTIALLY IDENTIFIABLE (map-side)** | **PARTIALLY IDENTIFIABLE (map-side)** | soft / diagnostic | enrichment |

**The gate needs ≥2 collapse countries; we now have 2, and they AGREE.** Both Costa Rica and Colombia
land **map-side** with no coupling→TFR lead. The earlier CR-vs-MX disagreement on Q2 is resolved: the
two actual *collapse* countries point map-side, and Mexico — the *slow-decline comparator* — is the
lone coupling-side case and does not govern the gate. **The nonlinearity locus is empirically settled
to the map side.** The mechanism is the fertility-response map (plausibly marriage-weighted), not a
partnership-formation threshold.

---

## Considerations for Stage 2 (showcase)

These shape the ABM spec Nina is about to freeze. Ordered by leverage.

1. **The nonlinearity-locus fork is now resolved to the MAP side — build the nesting model, default it
   to the map.** Both collapse countries (Costa Rica, Colombia) show a *nonlinear coupling→fertility
   map* (smooth/flat coupling, sudden TFR); only Mexico, the slow-decline comparator, shows nonlinearity
   in coupling itself. Build the model **nesting both loci** (Nina's recommendation) so it stays
   falsifiable, but with the **fertility-response map as the primary/default mechanism** and
   partnership-formation threshold as the comparator branch. Do **not** hard-code "threshold in
   partnership formation" — the data point the other way.

2. **Model the co-residential union, but track the marriage margin separately.** Both countries show
   a marriage collapse partly offset by rising cohabitation. If marriage and cohabitation differ in
   fertility intensity (likely in LAC), the behaviorally-relevant state variable may be *marriage-
   weighted* union, not total union. The married/cohabiting split is preserved in every CSV; Stage 2
   should test a marriage-specific (or fertility-weighted) coupling measure — this is also the most
   promising way to revive Costa Rica's currently-weak Q1/Q3.

3. **Lead-lag identification needs observed annual TFR — not modeled.** Mexico's Q1 was unevaluable
   because CONAPO's TFR is a smooth projection. Stage 2 calibration must pair coupling with
   *observed* annual TFR (DANE/INE/DEIS national series, e.g. Argentina's INDEC-pinned reconstruction),
   not WPP/CONAPO model output, or the lead test — the mechanism's core causal claim — stays untestable.

4. **Data-access reality must be designed into the pipeline.** Server-side REDATAM (Costa Rica) is the
   cleanest, login-free, reproducible channel — but only INEC's server is reliable; ARG/CHL REDATAM are
   flaky and COL/MX require microdata download (COL login-gated). Stage 2 calibration data is therefore
   **heterogeneous in access and frequency** (CR annual; MX biennial-or-fill; CHL periodic CASEN; ARG
   urban-only and split across a 2015 base break). The spec should not assume uniform annual national
   coverage.

5. **The single-country-vs-multi-country strategic call (for Héctor/Fina).** Costa Rica is the cleanest
   and the only fully-extracted collapse country, and Nina's prior lean was that a clean single-country
   mechanism paper beats a four-country paper with weak identification. **But Costa Rica's own
   identification is currently mixed** (lead/cascade weak) — so a single-country pivot to Costa Rica is
   not yet justified either. Recommend resolving at least the CR refinements (point 2) and one more
   collapse country before committing to scope.

6. **Frequency and noise discipline.** Annual ENAHO has real sampling noise (visible in CR's 2014–15
   wobble); 15 annual points strain lead-lag detection. Stage 2 should (a) smooth/CI the annual series,
   (b) pursue the EHPM 2000–2009 backfill (separate CCSS REDATAM portal) to lengthen CR's pre-collapse
   baseline, and (c) prefer effect sizes over single-year inflection-timing on short series.

---

## Recommended next actions (gate now decidable)

1. **Freeze the Stage 2 nesting-model spec** with the nonlinearity locus defaulted to the **map side**
   and **marriage-weighted union** as the primary coupling state variable (test total vs marriage-weighted).
2. **Marriage-margin lead-lag across both collapse countries** (cheap, high-value): re-run Q1/Q3 on the
   *marriage* series, not total union — this is the most promising place a lead could still hide, and
   it is the behaviorally-relevant margin in high-cohabitation LAC.
3. **Enrichment (not blocking):** Argentina/Chile via bulk-microdata fallback, and the CR EHPM 2000–09
   backfill, to widen the panel and lengthen pre-collapse baselines during Stage 2 calibration.

---

## Gate

Per the Stage 1.5 spec: this memo is reviewed by **Anne and Nina** before the Stage 2 ABM spec is
frozen. **Updated recommendation (after Addendum A): the gate is decidable and can be cleared.** Two
collapse countries (Costa Rica + Colombia) now agree — map-side nonlinearity, no coupling→TFR lead,
marriage-margin erosion under stable total union. The mechanism is **not** the originally-hypothesized
partnership-formation threshold, but a **nonlinear coupling→fertility map**; that is a clean, decidable
finding, not a failure. Nina may proceed to freeze the Stage 2 nesting-model spec (locus → map,
marriage-weighted coupling primary). No ABM specification work has begun pending Anne + Nina sign-off.

*Stage 1.5 of 4. Version 2.0, 2026-06-18 (Addendum A — Colombia folded in). Companions:
CRI/MEX/COL_coupling_annual.csv, CRI/MEX/COL_identification.csv, CRI/MEX/COL_coupling_vs_tfr.png,
extractor scripts, COL_coupling_annual.md + CRI_coupling_annual.md (PROTO-RAG-001 sidecars), and
STAGE1_5_addendumA_colombia_geih.md (the acquisition build instruction).*

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

## Gate verdict (read first) — UPDATED after Colombia (Addendum A) + marriage-margin rerun (Addendum B)

**The gate is now DECIDABLE. The nonlinearity locus is identified — as a function of the state
variable, not a single fixed side.** Colombia — the second collapse country and the only one with an
**observed** annual national TFR to pair against coupling — has been extracted (DANE GEIH 2007–2024,
via the Catálogo Central de Datos; the earlier login wall was the wrong door). With **two collapse
countries now in hand (Costa Rica + Colombia)**, the gate's ≥2-country requirement is met. The
marriage-margin rerun (**Addendum B**, `STAGE1_5_marriage_rerun_memo.md`) then sharpened *where* the
nonlinearity sits. Both countries point the **same** way on the qualitative findings:

- **The threshold-in-partnership-formation hypothesis is NOT supported.** In neither collapse country
  does coupling *lead* TFR (Q1) or decline cleanly *youngest-first* (Q3). Colombia, the one place the
  lead test is properly evaluable, shows **no clean lead — if anything coupling lags** the TFR turn.
- **On *total* union the nonlinearity sits in the coupling→fertility MAP (Q2).** Costa Rica (smooth
  coupling, sudden TFR) and Colombia (total union flat ~59–60% for twelve years, then a modest −6 pt
  drift, against a 1.7→1.1 TFR collapse) agree. Mexico — the *slow-decline comparator, not a gate
  country* — is the lone coupling-side case on total union.
- **But the locus is NOT fixed — it slides with the state variable (Addendum B).** Reweighting from
  total union toward marriage moves the nonlinearity *out of the map and into partnership formation*,
  continuously: the coupling/TFR decline ratio rises from 0.26→0.80 in Colombia and 0.61→**1.17** in
  Costa Rica (where marriage coupling falls *more* than TFR — fully coupling-side). So "map-side" is the
  reduced form *at total union*; the true finding is that the locus is a function of the cohabitation
  weight `w` and the country's cohabitation share. This is what makes the nesting model the right call.
- **The marriage margin is the live sub-mechanism (Anne's caution, now empirically central and
  confirmed).** In both countries total co-residential union is far more stable than *marriage*:
  Colombia's marriage share halves (20.7%→11.9%) under a flat total, cohabitation substituting. Addendum
  B confirms the marriage series declines far steeper than total (−28%/−46% vs −9%/−23%). The
  behaviorally-relevant coupling variable is **fertility-weighted union** (married + `w`·cohabiting),
  with `w` calibrated, not total union and not marriage-only.
- **The lead does NOT reappear on the marriage margin, but the test is tempo-biased (Addendum B).** No
  weighting yields a clean coupling→TFR lead; under tempo contamination (period TFR dates the turn too
  early) that null is *expected* and does not refute a true lead. The definitive lead test needs a
  tempo-adjusted / first-birth-ASFR series — Stage 2 enrichment.
- **Q4 independence holds universally** — coupling from survey rosters, TFR from vital registration.

**Recommendation: the gate can be cleared to proceed.** Nina may freeze the Stage 2 spec as the
**nesting model** (per her revised recommendation), with **`w` (cohabiting fertility weight) nested as a
structural parameter** and **fertility-weighted union as the state variable** — the locus is then
`w`-determined and calibrated, not hard-coded to either side. `w` is pinned via the Colombia ENDS
marriage-vs-cohabitation ASFR differential (flagged for Debb / the demographics corpus). This also
plausibly **unifies the CRI/COL/MX disagreement** — one structure at different `w` and cohabitation
shares, not three mechanisms. Argentina and Chile remain blocked but are now **enrichment, not
gate-critical** — the two-country gate is met without them. This is the addendum's
explicitly-anticipated second decidable branch:
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

**The gate needs ≥2 collapse countries; we now have 2, and they AGREE.** On *total union*, both Costa
Rica and Colombia land **map-side** with no coupling→TFR lead. *(The verdicts in this table are the
total-union analysis. Addendum B then showed the Q2 locus is not fixed: reweighting toward marriage
slides it from map-side to coupling-side, continuously in `w` — see §"Gate verdict" and the rerun memo.
So "map-side" here is the reduced form at `w=1`; the structural finding is a `w`-determined locus.)* The
earlier CR-vs-MX disagreement is reframed rather than simply resolved: it is plausibly the **same
nesting structure at different `w` and cohabitation shares**, not three mechanisms. The mechanism is a
`w`-determined coupling→fertility relationship (fertility-weighted union), not a partnership-formation
threshold.

---

## Considerations for Stage 2 (showcase)

These shape the ABM spec Nina is about to freeze. Ordered by leverage.

1. **The nonlinearity locus is `w`-determined — nest it, do not hard-code either side (Addendum B).**
   The earlier "resolve to map vs coupling side" framing is superseded: the rerun shows the reduced-form
   locus slides continuously from map-side (total union) to coupling-side (marriage-weighted) as the
   cohabiting weight `w` falls, and that Mexico-vs-CRI/COL may be the *same* structure at different `w`
   and cohabitation shares rather than different mechanisms. Build the nesting model with **`w` as a
   structural parameter**; the locus is then a calibrated output, not an assumption. Do **not** hard-code
   "threshold in partnership formation" *or* "threshold in the map."

2. **State variable = fertility-weighted union (married + `w`·cohabiting), with `w` calibrated
   (Addendum B).** Both countries show a marriage collapse partly offset by rising cohabitation, and the
   rerun confirms the marriage series declines far steeper than total (−28%/−46% vs −9%/−23%). Total
   union hides the marriage signal; marriage-only over-amplifies it (small denominator, noisy, discards
   cohabitation's non-zero fertility). Use **fertility-weighted union at a calibrated `w`** as the
   principled middle. Pin `w` = cohabiting/married ASFR ratio from the Colombia ENDS (CR equivalent);
   until then carry the {0.4, 0.6, 0.8} band. The married/cohabiting split is preserved in every CSV.

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

1. ✅ **Marriage-margin rerun — DONE (Addendum B).** Q1–Q4 re-run on total / fertility-weighted band /
   marriage-only for both collapse countries. Result: the **locus** flips with `w` (map→coupling-side)
   but the **lead** does not reappear (tempo-biased). See `STAGE1_5_marriage_rerun_memo.md`.
2. **Freeze the Stage 2 nesting-model spec** with **`w` nested as a structural parameter** and
   **fertility-weighted union** as the state variable (locus `w`-determined, not hard-coded).
3. **Pin `w`** = cohabiting/married ASFR ratio from the Colombia ENDS (CR equivalent) — flagged for Debb
   as a demographics-corpus scenario anchor; until then carry the {0.4, 0.6, 0.8} band.
4. **Definitive lead test (Stage 2 enrichment):** re-run Q1 against a **tempo-adjusted / first-birth-ASFR**
   fertility series — the only test not biased toward "no lead."
5. **Enrichment (not blocking):** Argentina/Chile via bulk-microdata fallback, and the CR EHPM 2000–09
   backfill, to widen the panel and lengthen pre-collapse baselines during Stage 2 calibration.

---

## Gate

Per the Stage 1.5 spec: this memo is reviewed by **Anne and Nina** before the Stage 2 ABM spec is
frozen. **Updated recommendation (after Addenda A + B): the gate is decidable and can be cleared.** Two
collapse countries (Costa Rica + Colombia) agree on the qualitative findings — no coupling→TFR lead
(tempo-biased), no youngest-first cascade, marriage-margin erosion under a more-stable total union — and
the marriage-margin rerun (Addendum B) identifies the nonlinearity locus as **a function of the state
variable** (`w`): map-side at total union, sliding coupling-side on the marriage margin. The mechanism
is **not** the originally-hypothesized partnership-formation threshold; it is a `w`-determined locus that
the nesting model should estimate, not assume. That is a clean, decidable finding, not a failure. Nina
may proceed to freeze the Stage 2 nesting-model spec (**`w` nested as a structural parameter,
fertility-weighted union as the state variable**). No ABM specification work has begun pending Anne +
Nina sign-off.

*Stage 1.5 of 4. Version 3.0, 2026-06-19 (Addendum A — Colombia; Addendum B — marriage-margin rerun —
folded in). Companions: CRI/MEX/COL_coupling_annual.csv, CRI/MEX/COL_identification.csv,
COL/CRI_identification_bymeasure.csv, CRI/MEX/COL_coupling_vs_tfr.png, COL/CRI_marriage_rerun.png,
extractor + rerun scripts, COL_coupling_annual.md + CRI_coupling_annual.md (PROTO-RAG-001 sidecars),
STAGE1_5_addendumA_colombia_geih.md + STAGE1_5_addendumB_marriage_rerun.md (build instructions),
STAGE1_5_marriage_rerun_memo.md, and STAGE1_5_for_Anne_coupling_questions.md.*

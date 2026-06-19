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

## Gate verdict (read first)

**Do NOT freeze the Stage 2 ABM spec yet — but not because the mechanism failed: because the
gate cannot yet be evaluated.** The gate requires the lead/nonlinear/cascade pattern to hold for
**≥2 of the 4 collapse countries**. Only **one** collapse country (Costa Rica) has a usable annual
coupling series so far; the other three (Colombia, Argentina, Chile) are blocked at the
data-acquisition step by access walls, not by analysis. So the binding constraint is **data
access**, and the honest status is **INCONCLUSIVE — gate not yet decidable**.

What we *can* say from the two series extracted:
- **The identification discipline holds** (Q4): in every case coupling is measured from household
  survey rosters, fully independent of vital-registration TFR. No circularity. This is the one gate
  condition that passes cleanly and universally.
- **Costa Rica (collapse case): PARTIALLY IDENTIFIABLE.** Coupling and TFR both decline materially,
  but the *specific* threshold predictions — coupling *leads* TFR (Q1) and declines *youngest-first*
  (Q3) — are **not clearly present** in the annual aggregate. The evidence leans toward a smooth
  coupling drift feeding a *nonlinear coupling→fertility map* (Q2).
- **Mexico (comparator, not a gate country): coupling decline is accelerating and youth-concentrated**
  — qualitatively more threshold-like than Costa Rica — but the verdict is soft (biennial data; lead
  test impossible against a modeled TFR).

This is exactly the "learn it before building" outcome Stage 1.5 was designed to produce. The
mechanism is **not refuted**, but it is **not yet confirmed**, and Costa Rica alone gives a *mixed*
signal that must not be over-read.

---

## Data acquisition status

The priority series (annual share of women 20–39 in co-residential union, by 5-yr band, married vs
cohabiting) was pursued per the Stage 1.5 source plan. Outcome by country:

| Country | Source | Method | Result |
|---|---|---|---|
| **Costa Rica** | ENAHO 2010–2024 | INEC **REDATAM** server-side crosstab (no login) | ✅ **Full annual series** (`CRI_coupling_annual.csv`) |
| **Mexico** (comparator) | ENOE 2005–2024 | INEGI **microdata** download (open) | ✅ **Biennial series, 9 yrs** (`MEX_coupling_annual.csv`); 2021 dropped (ETOE/COVID) |
| **Colombia** | GEIH | DANE microdata | ⛔ **Blocked** — microdata is login-gated (`auth/login`); no GEIH on REDATAM |
| **Argentina** | EPH | INDEC REDATAM | ⛔ **Blocked** — engine 500s to scripted requests; base `EPH_BASE_FINAL` covers only 2003–2014 |
| **Chile** | CASEN | ECLAC/INE REDATAM | ⛔ **Blocked** — engine 500s; ECLAC host carries only CASEN 1990–2011 (periodic) |

**Method note (reproducible):** the Costa Rica path drives INEC's RedatamX web engine
(`RpWebStats.exe/CrossTab`) to produce a weighted crosstab of estado conyugal × 5-yr age band,
filtered to women, weighted by the expansion factor — server-side, no microdata download, no login.
Extractors: `_extract_redatam_cri.py` (CR), `_extract_enoe_mex.py` (MX). The blocked-country
extractors (`_extract_redatam_arg.py`, `_extract_geih_col.py`) are written and ready to run once
access is resolved. **Environmental finding:** background agents have no network egress here, so all
extraction must run from the main session — and the ARG/CHL REDATAM servers proved unreliable to
scripted clients, unlike CR's robust INEC server.

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

### Colombia / Argentina / Chile — blocked at acquisition

No annual coupling series obtained. Endpoint-only data from Stage 1 remains the best available
(e.g. Mexico-style ENADID endpoints; CR/Chile census/survey points). Access obstacles:
**Colombia** GEIH microdata is login-gated and absent from REDATAM; **Argentina** INDEC REDATAM 500s
and its public base stops at 2014 (pre/early-collapse only); **Chile** REDATAM 500s and the open ECLAC
host carries only periodic CASEN 1990–2011. Each needs either a resolved login/account, a more robust
client against the flaky servers, or a fallback to bulk microdata download.

---

## Cross-country synthesis (Q1–Q4)

| | Costa Rica (collapse) | Mexico (comparator) | COL / ARG / CHL |
|---|---|---|---|
| Q1 lead | ✗ simultaneous | — not evaluable | no data |
| Q2 nonlinear | map-side (smooth coupling) | ✓ accelerating coupling | no data |
| Q3 cascade | ✗ no clean order | ~ youth-concentrated | no data |
| Q4 independent | ✓ | ✓ | (endpoints only) |
| **Verdict** | **PARTIALLY IDENTIFIABLE** | soft / diagnostic | **NOT YET — blocked** |

**The gate needs ≥2 collapse countries; we have 1 (mixed). Verdict: not yet decidable.** The two
countries we do have *disagree* on the most important question (Q2 nonlinearity location: CR map-side
vs MX coupling-side), which is itself informative — it suggests the mechanism may not be uniform
across countries, and that the model's nonlinearity locus is an open empirical question, not a settled
assumption.

---

## Considerations for Stage 2 (showcase)

These shape the ABM spec Nina is about to freeze. Ordered by leverage.

1. **The nonlinearity-locus fork is unresolved — design for both.** Costa Rica points to a *nonlinear
   coupling→fertility map* (smooth coupling, sudden TFR); Mexico points to *nonlinearity in coupling
   itself* (accelerating partnership decline). These are **two different ABMs** (threshold in the
   fertility response vs threshold in partnership formation). The spec should either (a) pick the
   locus empirically once ≥2 collapse countries are in, or (b) build a model nesting both so the data
   selects. Do **not** hard-code "threshold in partnership formation" yet.

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

## Recommended next actions (before Stage 2 freeze)

1. **Costa Rica refinements** (cheap, high-value): marriage-margin lead-lag (point 2) + EHPM 2000–09
   backfill (point 6). These directly test whether CR's weak Q1/Q3 is real or an aggregate/noise artifact.
2. **Acquire ≥1 more collapse country** with observed annual TFR — priority Colombia (GEIH via a DANE
   account) or Argentina (resolve REDATAM / EPH microdata), to make the gate evaluable.
3. **Then** re-run this memo's synthesis and issue a decidable gate verdict.

---

## Gate

Per the Stage 1.5 spec: this memo is reviewed by **Anne and Nina** before the Stage 2 ABM spec is
frozen. Current recommendation: **hold the freeze**; the mechanism is viable but unproven, the gate is
not yet decidable on one mixed collapse country, and two cheap CR refinements + one more collapse
country would make it so. No ABM specification work has begun.

*Stage 1.5 of 4. Version 1.0, 2026-06-18. Companions: CRI_coupling_annual.csv, CRI_identification.csv,
MEX_coupling_annual.csv, MEX_identification.csv, CRI_coupling_vs_tfr.png, MEX_coupling_vs_tfr.png,
extractor scripts, and CRI_coupling_annual.md (PROTO-RAG-001 sidecar).*

---
type: working_note
tier: gate_deliverable
project_scope: [DFD]
authors: [Claude Code (Stage 1.5 execution)]
addressed_to: Anne (population economics) and Nina (ABM lead), DFD Core Team
year: 2026
title: "Stage 1.5 Addendum B — marriage-series identification rerun: the locus flips, the lead does not"
venue: "DFD parallel research, internal — fertility-collapse ABM"
date_added: 2026-06-19
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_5_addendumB_marriage_rerun.md"
---

# Stage 1.5 Addendum B — Marriage-series identification rerun

**For:** Anne (population economics) and Nina (ABM lead)
**Date:** 2026-06-19
**Inputs:** `COL_coupling_annual.csv`, `CRI_coupling_annual.csv` (split columns), observed
`COL_tfr_national.csv` (DANE EEVV, 1-dec, 2015–24), `CRI_tfr_national.csv` (INEC, 2-dec, 2010–24)
**Engine:** `_marriage_rerun.py`. **Outputs:** `COL/CRI_identification_bymeasure.csv`,
`COL/CRI_marriage_rerun.png`.

---

## Headline (read first)

Anne's prediction was **half-confirmed, and the confirmed half is the structurally important one.**

- **Q2 nonlinearity LOCUS flips on the marriage margin — confirmed.** As the state variable moves
  from total union → fertility-weighted → marriage-only, the coupling decline grows relative to the
  TFR decline, sliding the reduced-form locus **from map-side toward coupling-side**. In Costa Rica it
  crosses the line entirely (marriage coupling falls *more* than TFR). This is exactly Anne's read:
  total union is the wrong aggregate, and on the marriage margin the partnership decline itself can
  carry most of the fertility collapse — no steep map required.
- **Q1 LEAD does NOT flip — not confirmed.** The marriage series does **not** reveal a clean
  coupling→TFR lead in either country. Colombia stays no-clean-lead (and the "best" alignment is
  unstable across the weight band — a tell that the lead is unidentified); Costa Rica stays robustly
  **simultaneous** (weak r≈0.24) at *every* weight. **But this null is the expected result under the
  tempo caveat** (below), so it does not refute a lead — it means period-TFR alignment cannot reveal one.

**Net for the gate:** the choice of Stage 2 state variable *is* the choice of where the model's
nonlinearity sits. That is precisely why Nina's nesting model is the right architecture — and it gives
a concrete structural parameter (`w`) to nest. Recommendation in §"For Nina" below.

---

## ⚠ Tempo caveat — attached to every Q1 lead verdict in this memo

Period TFR is tempo-contaminated. If births are being postponed (Stage 1 Check 5 found LAC fertility
decline is tempo/postponement-dominant), period TFR falls **faster and earlier** than the underlying
quantum, dating the fertility turn **too early**, which biases **every lead test toward "coupling
lags / no lead."** Therefore:

- A "no lead" or "lags" verdict is the **expected finding even if a true lead exists.** It is not
  evidence against a lead.
- A lead found **despite** this bias would be strong evidence — none of the measures clear that bar.
- The **definitive** lead test requires a **tempo-adjusted or parity-specific** fertility series
  (Bongaarts–Feeney adjusted TFR, or first-birth ASFR), flagged as Stage 2 enrichment. **All Stage 1.5
  lead verdicts are "detectable lead in period-TFR alignment — a test biased against detection."**

---

## Neutral data statement (20–39 aggregate, n-weighted)

**Colombia** (overlap 2015–2024, against observed DANE TFR 1.7→1.1, −35%):

| measure | w | level 2015→2024 | rel. decline | vs TFR ratio | Q1 (period-TFR) | Q2 locus |
|---|---|---|---|---|---|---|
| total union | 1.0 | 59.4 → 54.0% | −9% | 0.26 | no clean lead (lag-dominated) | **map-side** |
| fw 0.8 | 0.8 | 50.8 → 45.6% | −10% | 0.30 | no clean lead | map-side |
| fw 0.6 | 0.6 | 42.3 → 37.1% | −12% | 0.34 | no clean lead | map-side |
| fw 0.4 | 0.4 | 33.7 → 28.7% | −15% | 0.42 | no clean lead | map-side |
| marriage only | 0.0 | 16.6 → 11.9% | −28% | 0.80 | no clean lead | **mixed** |

**Costa Rica** (overlap 2010–2024, against observed INEC TFR 1.83→1.12, −39%):

| measure | w | level 2010→2024 | rel. decline | vs TFR ratio | Q1 (period-TFR) | Q2 locus |
|---|---|---|---|---|---|---|
| total union | 1.0 | 52.4 → 40.1% | −23% | 0.61 | **simultaneous** (r≈0.24) | mixed |
| fw 0.8 | 0.8 | 48.0 → 35.4% | −26% | 0.68 | simultaneous | mixed |
| fw 0.6 | 0.6 | 43.6 → 30.7% | −30% | 0.76 | simultaneous | mixed |
| fw 0.4 | 0.4 | 39.2 → 26.0% | −34% | 0.87 | simultaneous | **coupling-side** |
| marriage only | 0.0 | 30.4 → 16.6% | −46% | 1.17 | simultaneous | **coupling-side** |

(`w` is the cohabiting-vs-married fertility-intensity ratio, **uncalibrated** — swept as a sensitivity
band. `w=1` = total union; `w=0` = marriage only. The "vs TFR ratio" is |relative coupling decline| /
|relative TFR decline|: <0.5 → map-side, >0.85 → coupling-side, between → mixed. Thresholds are
heuristic; the continuous ratio is the honest quantity.)

---

## The flip question, answered explicitly

**Does the identification verdict change when the state variable moves from total to marriage-weighted?**

- **Locus (Q2): YES, and continuously.** The vs-TFR ratio is a smooth, monotone function of `w` in both
  countries. **Colombia** stays map-side across most of the band and only reaches "mixed" near pure
  marriage (ratio 0.26 → 0.80; crossing ~w≈0.25). **Costa Rica** is more sensitive — it tips from mixed
  to **coupling-side** around **w≈0.45** (ratio 0.61 → 1.17). The country difference is itself
  informative: Colombia's *total* union barely moves (high, stable cohabitation masks the marriage
  collapse), so it reads map-side; Costa Rica's total union already declines materially, so it reads
  mixed and goes coupling-side on the marriage margin. **The reduced-form locus is a function of both
  `w` and the country's cohabitation share — not a fixed property of the mechanism.**
- **Lead (Q1): NO.** No `w` produces a clean, robust coupling→TFR lead. Colombia's best-alignment `k`
  is unstable across `w` (+1 → +2 → −2 as `w` rises — see `COL_marriage_rerun.png` lower panel), which
  is the signature of an *unidentified* lead dominated by a contemporaneous/lag signal. Costa Rica is
  flat-simultaneous (k=0, r≈0.24) at every `w`. **Subject to the tempo caveat, "no lead" is expected
  and not informative against a true lead.**
- **Cascade (Q3): NO** youngest-first ordering at any measure in either country (steepest-decline years
  scatter across bands).
- **Independence (Q4): YES**, unchanged — every measure is roster-based (GEIH/ENAHO estado civil),
  independent of vital-registration TFR.

**So: the marriage margin moves the LOCUS verdict but not the LEAD verdict.** Anne's "the marriage
series shows a steeper, earlier decline" is confirmed (−28%/−46% marriage vs −9%/−23% total); her "and
may show the lead total union hides" is **not** confirmed — though the tempo bias means we cannot call
it refuted.

---

## For Nina — Stage 2 state-variable recommendation

**Recommendation: build the nesting model with `w` as a structural parameter, and use
fertility-weighted union as the state variable — do not fix the locus a priori.**

Rationale, directly from the rerun:
1. **The locus is not a modeling choice to be argued — it is a calibrated consequence of `w` (and
   cohabitation share).** At high `w` the nonlinearity lives in the coupling→fertility *map*; at low `w`
   it lives in *partnership formation*. The data trace this continuously. A model that hard-codes either
   locus is committing to an unestimated `w`. Nest it.
2. **This unifies the apparent CRI/COL/MX disagreement.** Costa Rica looked map/mixed, Colombia map,
   Mexico coupling-side. The rerun suggests these may not be different *mechanisms* but the same nesting
   model at different `w` and cohabitation shares producing different *reduced forms*. One structure,
   one parameter, three countries — a far stronger paper than three bespoke stories.
3. **Default the state variable to fertility-weighted union, not the extremes.** Total union hides the
   marriage signal (Anne); marriage-only over-amplifies it (small denominator → noisy relative changes,
   and it discards cohabitation's non-zero fertility). Fertility-weighted at a calibrated `w` is the
   principled middle.
4. **Pin `w` empirically.** `w` = ratio of cohabiting-union ASFR to married-union ASFR. The Colombia
   ENDS (and a CR equivalent) carries this differential. **Flagged for Debb** as a demographics-corpus
   scenario anchor. Until pinned, carry `w` as the {0.4, 0.6, 0.8} band in any Stage 2 result.
5. **Do not report a lead claim in the paper without the tempo caveat**, and schedule the tempo-adjusted
   / first-birth-ASFR lead test as the Stage 2 enrichment that could actually settle Q1.

The gate can be cleared on this basis: the state variable is now *empirically characterized* (locus is
`w`-determined), which is what Addendum B was asked to deliver.

---

## Architecture implications (per Héctor — no implication orphaned)

Each is a **stated question with a recommended owner**, not resolved here.

- **IM-6 demographic block (owner: Cath + Anne, in the IM-6 chat).** IM-6 currently parameterizes
  fertility and cohort weights **without distinguishing union type**. If union *composition* drives
  fertility independently of union *level* — which the locus-flip says is at least possible — IM-6's
  fertility process may be misspecified for LAC. **Question:** does the marriage/cohabitation split need
  to enter the IM-6 demographic block as a state dimension, or can it be absorbed into the calibrated
  fertility path without structural change?
- **NTA empirical layer (owner: Anne / NTA seat).** Age profiles of fertility-related transfers may
  differ by union type. **Question:** should the NTA layer carry a union-composition dimension, or is
  the age profile invariant enough to union type to ignore it?
- **Demographics monitoring corpus (owner: dfd-demographics-monitor skill / Debb).** The
  married-vs-cohabiting fertility-intensity differential (`w`) is a **scenario anchor** that belongs in
  `_crossrefs/corpus/demographics/`. **Action:** add it as a pending anchor (source: Colombia ENDS / CR
  equivalent), and have the monitor track **union composition**, not just TFR, going forward. Links to
  [[project_dfd_demographics_monitor]].
- **Fast-transition scenario discipline (owner: DFD_TFR_forecast quarterly pipeline).** If marriage
  decline co-moves with (and plausibly precedes, tempo aside) fertility decline, the **marriage rate is
  a candidate leading indicator** for the fast-transition scenario — earlier and cleaner than period
  TFR. **Question:** should marriage-rate (and union-composition) monitoring be added to the quarterly
  replicate protocol?

---

## Caveats (inline, per Debb / PROTO-RAG-001 — a verdict without its caveat is non-conformant)

- **Tempo bias on all Q1 lead verdicts** (see §caveat) — the central one; every lead statement above
  inherits it.
- **`w` is uncalibrated** — the fertility-weighted measure is a sensitivity band, not a point estimate;
  the flip-point `w` values (COL ~0.25, CRI ~0.45) are read off heuristic ratio thresholds.
- **Short-series noise** — COL Q1 rests on 9 annual differences against a **1-decimal chart-label** TFR;
  CRI is sturdier (15 points, 2-decimal) and is the more trustworthy of the two lead tests.
- **2007 Colombia outlier** — earliest GEIH point (union 47.5% vs the 2008–2020 ~59–60% plateau);
  excluded from the overlap window anyway (TFR starts 2015), but flagged.
- **High-cohabitation external-validity limit** — both identified countries are high-cohabitation
  regimes; the locus-flip's dependence on cohabitation share is exactly why a different-regime country
  (Argentina, Southern Cone) would sharpen the `w` story. See the ARG/CHL question in
  STAGE1_5_for_Anne_coupling_questions.md §Q4.

---

## Gate

Still the Stage 1.5 gate. **Anne and Nina review this memo.** Decision it enables: freeze Nina's Stage 2
nesting-model spec with the state variable empirically characterized — **fertility-weighted union, `w`
nested as a structural parameter, locus `w`-determined** — rather than left open or hard-coded. No
Stage 2 specification work has begun.

*Stage 1.5 Addendum B rerun memo. Version 1.0, 2026-06-19. Companions:
COL/CRI_identification_bymeasure.csv, COL/CRI_marriage_rerun.png, _marriage_rerun.py,
STAGE1_5_identification_memo.md (v2.0), STAGE1_5_addendumA_colombia_geih.md,
STAGE1_5_addendumB_marriage_rerun.md (build instruction), STAGE1_5_for_Anne_coupling_questions.md.*

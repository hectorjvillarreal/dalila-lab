# Stage 1.5 Addendum B — Marriage-Series Identification Rerun
# Project: Rapid Fertility Collapse in Latin America (ABM paper, DFD parallel research)
# Author: Anne (population economics) and Nina (ABM lead), DFD Core Team
# Date: 2026-06-18
# For: Claude Code on Dalila
# Location: GrandPlan/DFD/research/fertility_collapse_abm/data/coupling/

---

## Why this addendum — and why it matters beyond the paper

Colombia settled one question and exposed another. Total co-residential union (women
20–39) barely moves while **marriage halves** (20.7% → 11.9%) under rising cohabitation,
against a 35% TFR collapse. On the *total-union* series the verdict is map-side, no lead.
Anne's read: that is probably the **wrong aggregate**. The marriage margin is where the
coupling signal likely lives, and the "map-side / no-lead" verdict may flip when the
identification is rerun on a marriage-weighted measure.

This rerun is the final act of Stage 1.5 before Nina freezes the Stage 2 spec. It is
cheap — the microdata is already extracted, the split columns already preserved — but
its result is **load-bearing for the entire architecture**, not just the paper. If the
operative demographic state variable is union *composition* rather than union *level*,
that propagates into IM-6's demographic block, the NTA age-profile layer, and the
triplet interface — anywhere fertility is currently treated as a function of partnership
status without distinguishing union type. **Document accordingly: full findings,
full caveats, no orphaned conclusions.**

---

## The rerun — exact specification

Using the already-extracted `COL_coupling_annual.csv` and `CRI_coupling_annual.csv`
(both preserve the married/cohabiting split), construct and analyze **three** coupling
measures per country, not one:

1. **Total union** — married + cohabiting (already done; carry forward as the baseline
   for comparison).
2. **Marriage only** — the married share alone, women 20–39, by 5-year band.
3. **Fertility-weighted union** — a composite where married and cohabiting unions are
   weighted by their relative fertility intensity:
   `fert_weighted = married_share + w · cohabiting_share`, where `w` is the ratio of
   cohabiting-union ASFR to married-union ASFR (0 ≤ w ≤ 1, w < 1 if cohabitation is
   lower-fertility).

   **`w` is not yet calibrated.** Until the Colombia ENDS differential is acquired
   (flagged for Debb), run the fertility-weighted measure as a **sensitivity band**
   across `w ∈ {0.4, 0.6, 0.8, 1.0}` rather than a single value. Report how the
   identification verdict changes across the band. `w = 1.0` reduces to total union;
   `w` small approaches marriage-only. The point is to see *where in that band the
   verdict flips*, if it flips.

---

## Run the full Q1–Q4 identification on each measure

For Colombia (against observed DANE EEVV annual TFR) and Costa Rica (against observed
INEC TFR), rerun all four identification questions on measures 2 and 3:

- **Q1 (lead):** does the marriage / fertility-weighted series turn down *before* TFR?
  Report best-aligned lag `k` and correlation for each measure. **This is the test that
  may flip.** Anne's falsifiable prediction: the marriage series shows a steeper, earlier
  decline than total union and may show the lead total union hides.
- **Q2 (nonlinearity locus):** for each measure, is the nonlinearity in the coupling
  series itself or in the coupling→fertility map? Report whether the locus moves as the
  measure shifts from total → fertility-weighted → marriage-only.
- **Q3 (cascade):** does the marriage decline appear youngest-first across the 5-year
  bands? Marriage timing may show the age-ordered propagation that total union does not.
- **Q4 (independence):** unchanged — confirm the measure remains GEIH/ENAHO roster-based,
  independent of vital registration. (Expected pass.)

---

## The tempo caveat — mandatory, do not omit

Anne's Q3 caution from the consult note applies to every lead test in this rerun and
**must be stated explicitly in the output**, because it changes how the result reads:

Period TFR is contaminated by tempo. If births are being postponed, period TFR falls
*faster and earlier* than the underlying quantum, which dates the fertility turn **too
early**, which biases every lead test **toward finding that coupling lags**. Therefore:

- A "no lead" or "coupling lags" result is the *expected* finding even if a true lead
  exists, whenever tempo distortion is present. State this directly.
- Where the marriage series shows a lead *despite* this bias, that is strong evidence —
  the bias works against it.
- Flag that the definitive lead test requires a tempo-adjusted or parity-specific
  fertility series (Stage 2 enrichment), and that all Stage 1.5 lead verdicts are
  "detectable lead in period-TFR alignment, a test biased against detection."

Do not report any lead verdict without this caveat attached.

---

## Deliverables

Under `GrandPlan/DFD/research/fertility_collapse_abm/data/coupling/`:

1. **Extended identification CSVs** — `COL_identification_bymeasure.csv`,
   `CRI_identification_bymeasure.csv` — Q1–Q4 results for all three measures
   (total / fertility-weighted band / marriage), side by side.

2. **Comparison charts** — for each country, the three coupling measures plotted against
   observed TFR on a common timeline, plus a small table of the lead-lag `k` and
   correlation per measure. The visual answer to "does the verdict flip on the marriage
   margin?"

3. **Rerun memo** — `STAGE1_5_marriage_rerun_memo.md` — the primary deliverable.
   Structure:
   - The neutral data statement per country (what the three measures show)
   - The Q1–Q4 verdict per measure, with the tempo caveat attached to every lead claim
   - **The flip question answered explicitly:** does the identification verdict change
     when the state variable moves from total union to marriage-weighted? At what `w`?
   - A clear recommendation to Nina on the **Stage 2 state variable**: total,
     fertility-weighted (at what `w`), or marriage-only.
   - **An architecture-implications section** (see below) — this is what Héctor flagged.

---

## Architecture-implications section — required, this is the wide-angle part

Héctor's instruction: this research has implications for the complete architecture, not
just the paper. The rerun memo must close with an explicit assessment of what the
union-composition finding implies for the broader DFD environment, addressed to the
relevant seats:

- **For IM-6 (Cath / Anne interface):** the Integrated Model's demographic block
  currently parameterizes fertility and cohort weights without distinguishing union
  type. If union *composition* drives fertility independently of union *level*, IM-6's
  fertility process may be misspecified for LAC. Flag whether the marriage/cohabitation
  distinction needs to enter the IM-6 demographic block, or whether it can be absorbed
  into the calibrated fertility path without structural change. State the question;
  Cath and Anne resolve it in the IM-6 chat.

- **For the NTA layer:** age profiles of fertility-related transfers may differ by union
  type. Flag whether the NTA empirical layer should carry a union-composition dimension.

- **For the demographics monitoring corpus:** the married-vs-cohabiting fertility
  differential is a scenario anchor that belongs in `_crossrefs/corpus/demographics/`.
  Flag for the dfd-demographics-monitor skill to track union composition, not just TFR,
  as a leading indicator going forward.

- **For the fast-transition scenario discipline:** if marriage decline leads fertility
  decline, the marriage rate is a *leading indicator* for the fast-transition scenario
  — earlier than TFR itself. Flag whether marriage-rate monitoring should be added to
  the quarterly replicate protocol (the DFD_TFR_forecast_instructions quarterly pipeline).

Keep each flag to a stated question with a recommended owner. Do not resolve them here —
the point is to ensure no implication is orphaned, per the provenance principle.

---

## Documentation discipline (Debb)

Per Héctor's instruction and PROTO-RAG-001: document all findings AND all caveats. Every
verdict in the rerun memo carries its caveat inline — the tempo bias on lead tests, the
uncalibrated `w` band on the fertility-weighted measure, the short-series noise on
annual points, the 2007 Colombia outlier, the high-cohabitation external-validity limit.
A finding stated without its caveat is not conformant. The rerun memo and all companions
get PROTO-RAG-001 frontmatter; `endorsed_by` left blank pending Anne.

---

## Gate

This is still the Stage 1.5 gate. On completion, Anne and Nina review the rerun memo.
The decision it enables: **freeze Nina's Stage 2 nesting-model spec with the state
variable now empirically chosen** (total / fertility-weighted / marriage), rather than
left open. No Stage 2 specification work begins until this review.

---

*Stage 1.5 Addendum B. Version 1.0, 2026-06-18.*
*Companion to STAGE1_5_identification_memo.md (v2.0), STAGE1_5_addendumA_colombia_geih.md,*
*and STAGE1_5_for_Anne_coupling_questions.md.*

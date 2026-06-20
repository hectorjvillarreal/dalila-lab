---
type: endorsement_record
stage: 2b
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2b — Anne's adjudication and conditional endorsement"
target: "Debb (to file) · Claude Code (to amend & execute)"
date_added: 2026-06-20
added_by: Claude
endorsed_by:        # Anne's review COMPLETE-with-conditions; instruction's endorsed_by stays blank until §Conditions met
gates: "STAGE2b_compositional_cascade_instruction.md (write endorsed_by: Anne once §Conditions clear)"
adjudicates: "STAGE2b_for_Anne_checklist.md"
status: "CONDITIONAL ENDORSEMENT — hypothesis set and §5 structure endorsed; execution-of-record gated on §Conditions + a calibrated (non-smoke) run."
honesty_note: "No separate Anne points document is present in the workspace. The (A) framing reconciled in C8 is the one set down here; if a prior points document exists on Dalila with a different §2/§5, it must be diffed against this before execution."
---

# Stage 2b — Anne's Adjudication

Smoke-test results are non-authoritative. The decisions below are methodological and are
fixed *before* the calibrated numbers, per the pre-registration spirit.

## Group A — decisions

**A1 — reference group.**
- Primary spec: `peer_younger` (excludes focal cohort → least exposed to the reflection problem; upward-diffusion story fits a rapid post-transition collapse).
- ADD `peer_older` (not-married share of next-older band, t−1) — the template-setter referent; tests diffusion direction; covers all but the oldest band where `peer_younger` drops the youngest.
- `pop2039` → robustness only (focal cohort is inside it: mild inclusion bias).
- `own_lag` → comparator only (mechanical).
- Required: full β matrix (all specs × CR/COL × lags) in outputs. Resolve the A1 prose/table contradiction ("flips sign" vs uniformly-positive table) before the calibrated run.
- Standing read: amplifying cascade requires β < 0; smoke-test β's are positive (stabilizing), so the preliminary lean is *away* from H_cascade. Not a result — flag, do not conclude.

**A3 — adjudication bar (fixed now).**
H_cascade iff β amplifying (β < 0) AND significant under `peer_younger` AND under ≥1 other clean
spec (`peer_older`/`pop2039`), in **both** CR and COL. Else → H_shock (if Task B shows a period
component) or H_cohort (if not). H_mixed requires a Task-B period component AND amplifying
state-dependence under at least the primary spec; then (B) is warranted **only** for the period
share. Bar keys on sign, not magnitude (COL/CRI magnitude gap is likely a B7 artifact).

**A2 — pseudo-cohort construction.** Redraw required.
- Define pseudo-cohorts by birth-year bin from (age, survey year), not `year − band_midpoint`.
- Take Task B second differences within properly-tracked cohort series / fixed bands so the
  2012/2017/2022 sawtooth cannot leak into curvature.
- Within-band-segmented redraw for fig-1.

**A4 — localization thresholds.** Replace mechanical cuts.
- Period: report curvature over 2015–2024 AND the 2018–2024 sub-window (not a single late box).
- Entry cohorts: birth cohort ≥ 1990 (substantive), not "youngest third."
- RMS of second differences retained as the metric.

## Group B — verification directions

**B5 — identification wall.** Accepted as reported (`assert_no_tfr()` fired correctly; national
data confined to script 3 overlay). Execution-of-record requires the assertion log filed in
`outputs/stage2b/`.

**B6 — band/base consistency.** Add a reproduction diff against the Stage 1.5 coupling series on
overlapping cells; mismatch beyond tolerance halts. Log the 20–39 limitation: it excludes the
15–19 entry margin (the cascade vanguard) and is what breaks `peer_younger` for the youngest band.

**B7 — CR/COL asymmetry.** Accepted. CR β is an *ecological* (cell-level) estimate, COL β is
individual-level. Tag CR β as ecological at every comparative claim; the A3 "both countries"
requirement reads CR evidence as coarser.

## Group C — the gate

**C8.** Hypothesis set (§2) endorsed — the H_shock/H_cascade separation is the heart of the
design. §5 structure endorsed, amended per A1/A3/A4 below.

---

# Drop-in amendments to the instruction

### Replace §5 decision rule with:

| Finding | Reading | Implication for (B) |
|---|---|---|
| Cohort-dominant (Task B), no amplifying β under `peer_younger` | H_cohort | (B) deferred; model needs cohort-entry heterogeneity. |
| Period-dominant, β not amplifying / insignificant under `peer_younger` | H_shock | (B)'s reflexive structure not justified; needs an exogenous period driver. |
| β amplifying (β<0) & significant under `peer_younger` AND ≥1 of {`peer_older`,`pop2039`}, in BOTH CR & COL | H_cascade | (B) warranted; Nina proceeds. |
| Period component (Task B) + amplifying β under ≥ primary spec, mixed with cohort component | H_mixed | (B) warranted ONLY for the period share; quantify and document. |

Reference specs: `peer_younger` (primary), `peer_older` (added, clean), `pop2039` (robustness),
`own_lag` (comparator only). Period windows: 2015–2024 and 2018–2024. Entry cohorts: birth ≥ 1990.

### Add to §10 amendment log:

> 2026-06-20 — Anne adjudication (STAGE2b_Anne_endorsement.md). §5 rule amended: bar = amplifying
> & significant under primary + ≥1 clean spec, in both CR & COL; `peer_older` spec added;
> substantive period/entry-cohort cuts; pseudo-cohort redefinition (A2). Hypothesis set (§2)
> endorsed unchanged. CR β tagged ecological (B7).

---

# Conditions for execution-of-record (Debb writes `endorsed_by: Anne` once all clear)

1. `peer_older` spec implemented; full β matrix in outputs; A1 prose/table contradiction resolved.
2. Pseudo-cohorts redefined by birth-year bin; Task B second differences taken within tracked
   series; fig-1 within-band redraw.
3. §5 / §10 amended as above; substantive period and entry-cohort cuts in code.
4. B6 reproduction diff vs Stage 1.5 passes to tolerance.
5. B5 assertion log filed in `outputs/stage2b/`.
6. A calibrated (non-smoke) run produced; only then is the §5 verdict applied.

Until 1–6 clear, the instruction's `endorsed_by` stays blank and Stage 3 / question (B) remain
gated. On present (non-authoritative) construction the state-dependence is **not** leaning
cascade — so (B) should not be staged in anticipation.

*Anne's review complete-with-conditions, 2026-06-20. Reconcile against the points document if/when it enters the workspace.*

---
type: read_pointer
stage: 2b
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2b — what Anne should read (endorsement reading order)"
target: Anne (population economics)
date_added: 2026-06-21
added_by: Claude
endorsed_by:                       # this is the pointer to the endorsement decision
depends_on:
  - "STAGE2b_compositional_cascade_memo.md — the read (primary)"
  - "STAGE2b_Anne_endorsement.md — Anne's own conditions 1-6"
  - "STAGE2b_compositional_cascade_instruction.md — §5 amended per Anne"
status: "Conditions 1-6 implemented + calibrated run complete. Awaiting Anne's endorsement of the read and her ruling on the B7 correction."
---

# Stage 2b — What Anne Should Read

All six of your execution conditions are implemented and the calibrated (non-smoke)
run is complete. Your task now is to **endorse the read** (or push back). Read in this
order; items 1–2 are the decision, items 3–4 are confirmation.

## 1. The read — `STAGE2b_compositional_cascade_memo.md`  *(primary)*
The §5 rule applied to the calibrated numbers. **Verdict: not H_cascade in either
country; (B) reflexive feedback NOT warranted.** β > 0 (stabilizing) everywhere; CRI
reads H_cohort-leaning (period effect insignificant, p=0.18), COL reads H_shock + cohort
component (period effect present p≈3e-6, but non-reflexive). This is the document your
`endorsed_by` signs (§7 gate criterion 5). Matches your standing read.

## 2. The B7 correction — **needs your ruling**  *(blocks endorsement)*
In the memo's "Limitations and one correction" section. Implementation showed your B7
wording ("COL β is individual-level") does not hold: Task C is a within-cohort **cell**
test on repeated cross-sections, so **both** βs are **ecological** — neither observes
individual union transitions. The CR/COL asymmetry is in how the *cells* are built
(CR = REDATAM pre-tabulated; COL = from DANE microdata), not the estimator level. I
tagged both ecological and logged it rather than silently absorbing your wording.
**Confirm or overrule.** It is the one substantive deviation; it does not change the
sign-based verdict.

## 3. Verdict inputs — to sanity-check
- `outputs/stage2b/statedep_beta_matrix.csv` — full β matrix (uniformly positive; the A1
  "flips sign" contradiction is resolved, not papered over).
- `outputs/stage2b/apc_localization_ALL.csv` + `statedep_period_test_{CRI,COL}.csv` —
  period-vs-cohort localization and the period-effect F-tests driving each §5 cell.
- `outputs/stage2b/figures/fig1_cohortlines_{CRI,COL}.png` — within-band-segmented redraw
  (your A2 fix; the 2012/17/22 sawtooth is gone). Eye-test.

## 4. Conditions 1–6 cleared — confirm
The memo's "Verification status" table maps each condition to its artifact, including
B6 PASS (reproduction diff vs Stage 1.5: married/cohab exact) and the identification-wall
assertion log (`_assert_no_tfr.log`, 25 PASS / 0 VIOLATION).

---

## The gate
If you accept the read (1) and rule on B7 (2), **Debb writes `endorsed_by: Anne`** in
`STAGE2b_compositional_cascade_instruction.md`. That endorsement:
- **unblocks** Stage 3 (four-country nesting + GPU sweep), and
- **closes** (B) reflexive self-reinforcement in the modeling chat — *unless* the 15–19
  entry-margin caveat (the cascade vanguard, excluded by the 20–39 floor) or Southern
  Cone identification (ARG/CHL, out of scope for 2b) later overturns the non-cascade read.

Do **not** stage (B) in anticipation — the evidence leans against it.

## Filing note
This pointer + the handoff and endorsement records are on `main`; the memo, scripts, and
outputs live on branch `dfd-fertility-collapse-stage1.5` (commit e4609b7) until merged
through the normal flow after your sign-off.

*Shortest path: read the memo (1), rule on B7 (2), spot-check the β matrix (3).
Claude, 2026-06-21.*

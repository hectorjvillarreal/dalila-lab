---
type: build_instruction
stage: 2c
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2c — COL individual-level test (the cascade-below-the-cell pivot)"
target: Claude Code (Dalila)
date_added: 2026-06-21
added_by: Claude
endorsed_by: Anne   # DESIGN endorsed 2026-06-21 (Anne's 9a ruling applied). The READ this produces requires separate Anne endorsement — §6 criterion 4 / §9b.
amended: "2026-06-21 — Anne's 9a ruling applied: 2c-i is necessary-not-sufficient to close (B); closure waits on ENDS. Third status added to §4/§6. See amendment log."
seeds: "Anne's Stage 2c item 1 (STAGE2b_Anne_read_signoff.md): COL individual union-transition test"
depends_on:
  - "STAGE2b_compositional_cascade_memo.md (the cell-level non-cascade verdict this interrogates)"
  - "STAGE2b_Anne_read_signoff.md (B7 ecological correction → motivates this test)"
gates: "Anne's ruling on whether (B) moves from 'deferred' to 'deferred, aggregation-cleared, pending ENDS' (confirm) or 'reopened' (reopen) for COL"
compute: "CPU / Python (statsmodels discrete choice). Anne CPU-native. No GPU, no Julia."
build_instruction: "Drafted by Claude on Héctor's instruction, 2026-06-21. Pivot test: the one open channel that can OVERTURN the 2b headline. Design endorsed by Anne; read endorsement is the later gate."
---

# Stage 2c — COL Individual-Level Test
# Target: Claude Code (Dalila)

## 0. Why this exists

The B7 correction (Anne's sign-off) established that **both** 2b βs are ecological — Task C ran on
cell shares, observing no individual union behavior. Ecological aggregation can mask, and in principle
sign-flip, an individual-level relationship. So a within-cohort reflexive cascade could still hide
**below the cell**, undetected by 2b. This stage looks there, in COL — the only country whose cells
came from microdata. It is the pivot: it can **overturn** the non-cascade verdict, not merely bound it.
Run it before Stage 3 respecification and before Fina drafts M4.

## 1. The honest scope — read before coding

GEIH is a repeated cross-section with only a short rotating panel. **It does not give multi-year
individual union-formation transitions.** Do not pretend it does. Two sub-tests, different evidentiary
weight:

- **2c-i (runnable now): individual-level union-*status* model on pooled GEIH microdata.** Each person
  a row; union status the outcome; individual covariates and correct inference. This **escapes the
  ecological-aggregation bias** (the thing B7 surfaced) but is still a status model on repeated
  cross-sections — it does **not** observe transitions. It addresses the aggregation concern, not the
  "no transitions observed" concern.
- **2c-ii (gated on ENDS): true union-formation hazard on retrospective histories.** ENDS (DHS) carries
  retrospective union/marriage histories → actual individual union-formation timing → a genuine
  discrete-time hazard. The **definitive** transition test. ENDS is already a pending acquisition (the
  `w` differential). 2c-ii waits on it; do not attempt it on GEIH.

This stage delivers **2c-i** and logs 2c-ii as gated.

## 2. Inherited discipline (do not violate)

- **Identification wall.** TFR is comparison-only; never a regressor; `assert_no_tfr()` guard carried
  over from 2b, log to `outputs/stage2c/`.
- **Frozen invariants.** State is union composition {single, cohabiting, married}. `w` /
  fertility-intensity is **not** a 2c-i object (gated to ENDS with 2c-ii).
- **Reference-share construction matches 2b.** `peer_younger` primary, `peer_older` clean, `pop2039`
  robustness — focal unit now the individual; regressor is the individual's reference group's **lagged
  not-married share** (same groups as 2b).
- **Pre-registered decision rule (§4) fixed before estimation.**

## 3. Operations for Claude Code

**Task A — individual-level panel from GEIH microdata.** Pool GEIH person-records 2007–2024; retain
union status, age, birth cohort, survey year, individual covariates (education, sector, urban).
**Extend the age floor down to 15** (drops the 20–39 restriction) so the 15–19 entry margin — Anne's
second deferred channel, the cascade-ignition zone — is observed here too. Attach each person's
reference-group lagged not-married share (the 2b specs).

**Task B — individual-level status model.** Discrete choice (logit / multinomial: married vs cohabiting
vs single):

  P(married)_{i} = f( ReferenceShare_{g(i),t-1}, age, cohort, year, X_i )

The coefficient on `ReferenceShare_{t-1}` is the individual-level analog of 2b's β. **Amplifying = the
probability of being/forming married *declines* as the reference not-married share rises**
(self-reinforcing retreat). Cluster on reference group × year; report robustness across the 2b
reference specs and across including/excluding the 15–19 band.

**Task C — compare to the 2b cell-level β.** Does the individual-level estimate **confirm** the
non-amplifying (stabilizing) cell-level finding, or **reveal** amplifying dependence the aggregation
masked? This contrast is the deliverable.

**Task D — apply the §4 rule and write the read.**

## 4. Pre-registered decision rule

| Individual-level finding | Reading | Ruling on (B) for COL |
|---|---|---|
| Reference-share dependence non-amplifying (consistent with cell-level), incl. 15–19 | H_confirm | (B) **deferred, aggregation-cleared, pending ENDS** — NOT closed. The cross-sectional aggregation didn't hide a cascade; a cascade is a process in time, which only ENDS (2c-ii) observes. |
| Amplifying & significant, robust across specs | H_reopen | (B) **reopened**; reflexivity returns to Stage 3; ecological aggregation had masked a cascade. |
| Amplifying only in 15–19 | H_entry-margin | Cascade ignites at entry and dissipates; (B) partially reopened for the youngest band; the 20–39 floor was a blindfold over the ignition zone. Flag for ENDS confirmation. |

**Anne's 9a ruling (binding).** 2c-i is **necessary but not sufficient** to *close* (B): it can only
fail to reopen it. A non-amplifying status model downgrades the risk — the aggregation cleared — but
closure waits on the ENDS true-transition test (2c-ii), because a cascade is a temporal process and a
status model on repeated cross-sections does not observe the process. Binary deferred/closed is too
coarse; the three statuses above are the resolution.

## 5. Deliverables

- `STAGE2c_col_individual_memo.md` — the read; §4 rule applied; confirm/reopen for COL.
- `stage2c_individual_model.py` — Tasks A–C.
- `outputs/stage2c/` — individual-level estimates by spec, 15–19 split, comparison to 2b β,
  `_assert_no_tfr.log`.
- `endorsed_by` blank on the read pending Anne. PROTO-RAG-001 documentation standard.

## 6. Gate criteria

1. Individual-level estimates produced across the 2b reference specs, with and without 15–19.
2. Comparison to the 2b cell-level β explicit.
3. §4 rule applied; confirm / reopen / entry-margin ruling stated.
4. Anne endorses the read → her standing ruling on (B):
   - **H_confirm** → "(B) deferred, **aggregation-cleared**, pending ENDS." Stage 3 sufficiency may
     proceed **in parallel** under this branch as a **no-reflexivity** model (it stays no-reflexivity
     either way until ENDS speaks).
   - **H_reopen** → "(B) reopened; reflexivity returns to Stage 3."

## 7. Limitations (state in the memo)

- **No true transitions.** 2c-i is a status model; the genuine transition test is 2c-ii (ENDS, gated).
- **Reflection problem persists** at the individual level (lagged distinct-group referent is partial
  mitigation, as in 2b; not clean causal identification).
- **COL only.** CRI cannot support this (REDATAM aggregates — no microdata). One-country look; external
  validity unchanged.
- **Compositional reference share is still aggregate.** The regressor is a group share; only the LHS
  moves to the individual.

## 8. What this stage does NOT do

- Not a true panel / transition model (that is 2c-ii on ENDS).
- Not ARG/CHL external validity (separate, data-gated).
- Not `w` / parity-progression (gated to ENDS).
- Not Stage 3 (model respecification / sufficiency sweep).

## 9. For Anne

- **(a) RULED 2026-06-21.** 2c-i (GEIH status model) is an acceptable individual-level look but is
  **necessary-not-sufficient to close (B)**; closure waits on 2c-ii (ENDS). Applied to §4/§6 above.
- **(b)** Endorse the read once produced (§6 criterion 4). Reconcile against the distributed
  demographic half if framing differs.

## Amendment log

- **2026-06-21 — Anne's 9a ruling applied.** §4 H_confirm row changed from "(B) closed on COL
  evidence" to "(B) deferred, aggregation-cleared, pending ENDS"; third-status logic added; §6 gate
  criterion 4 rewritten to the three-branch language with Stage 3 sufficiency proceeding in parallel
  under H_confirm as a no-reflexivity model; §9a moved from open question to ruled. `endorsed_by` →
  Anne (design); read endorsement remains the later gate.

*Stage 2c instruction. Claude, 2026-06-21, on Héctor's instruction. Design endorsed by Anne; read endorsement pending.*

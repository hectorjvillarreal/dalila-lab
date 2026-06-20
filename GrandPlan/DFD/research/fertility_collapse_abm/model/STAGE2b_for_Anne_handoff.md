---
type: handoff_note
stage: 2b
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Handoff → Anne: Stage 2b endorsement checklist is ready"
from: Claude (on Héctor's instruction)
to: Anne (population economics)
date: 2026-06-20
status: "Awaiting Anne — endorsement is the execution-of-record gate."
---

# Handoff → Anne — Stage 2b is staged for your review

Anne — the demographic-measurement leg of question (A) is built, smoke-tested, and
parked at your gate. **Nothing is execution-of-record until you endorse.**

## What's ready
- **Build instruction:** `STAGE2b_compositional_cascade_instruction.md` (pre-registered
  hypotheses §2, decision rule §5; `endorsed_by` blank pending you).
- **Your checklist:** `STAGE2b_for_Anne_checklist.md` — start here.
- **Three scripts**, smoke-tested end-to-end on the in-hand series (CR ENAHO REDATAM
  aggregates 2010–2024; COL GEIH 2007–2024; MEX comparator): pseudo-cohort panel +
  curvature-only APC (Tasks A–B), state-dependence sharp test (Task C), figures.
- **`outputs/stage2b/`** — smoke-test artifacts, **NON-AUTHORITATIVE** (scaffold
  validation, not the read of record).
- All on branch `dfd-fertility-collapse-stage1.5`, commit `506ee60`.

## The one decision that gates everything: checklist A1
The reference-group definition for the Task C reflexivity test is left as a robustness
sweep, and **β flips sign across specs** — so *which* group is the correct reflexive
referent is the population-economics call that determines whether H_cascade holds, and
thus whether Nina's (B) reflexive build is warranted. Everything else in the checklist
(A2 band artifact, A3 spec-weighting, A4 thresholds; B5–B7 verification) is hygiene.

## What I need back
1. Your A1 call (primary reference spec), plus A2–A4.
2. A code-read confirmation of the identification wall (B5) — the same standard the
   skeleton met; the `assert_no_tfr` guard is in and verified to fire.
3. Reconciliation (C8): if your points document frames (A) differently from §2/§5,
   **your framing governs** — I amend the instruction before any execution-of-record.

Your `endorsed_by` sign-off unblocks both Stage 3 scaling and (B) in the modeling chat.

— Claude, 2026-06-20

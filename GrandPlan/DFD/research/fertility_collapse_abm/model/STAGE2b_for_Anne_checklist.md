---
type: review_checklist
stage: 2b
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2b — endorsement checklist for Anne"
target: Anne (population economics)
date_added: 2026-06-20
added_by: Claude
endorsed_by:                      # this IS the endorsement gate — Anne signs §C8
depends_on:
  - "STAGE2b_compositional_cascade_instruction.md — the build instruction this gates"
  - "stage2b_apc_composition.py / stage2b_state_dependence.py / stage2b_figures.py — scaffolds, smoke-tested"
  - "outputs/stage2b/ — non-authoritative smoke-test artifacts"
build_instruction: "STAGE2b_compositional_cascade_instruction.md"
status: "Scaffolds written and smoke-tested 2026-06-20; results NON-AUTHORITATIVE pending this checklist."
---

# Stage 2b — Endorsement Checklist for Anne

**Posture.** The three Stage 2b scripts are written and run end-to-end on the in-hand
series (CR ENAHO REDATAM aggregates 2010–2024; COL GEIH 2007–2024). The outputs in
`outputs/stage2b/` are **smoke-test validation, not the read of record.** Execution-of-record
is gated on your endorsement (§C8 below). Nothing here applies the §5 decision rule — that is
Task D, yours to direct.

Items are ordered by leverage on the §5 verdict. **Group A is yours to decide; Group B is
yours to verify; Group C is the reconciliation gate.**

---

## A. Decisions only you can make (these change the answer)

### A1 — Reference-group definition for Task C  *(RESOLVED by Anne 2026-06-20)*
The sharp test is `Δ(marriage_share)_{c,a,t} = β · ReferenceShare_{t−1} + age FE + cohort FE`.
Anne's adjudication: **`peer_younger` primary** (excludes focal cohort; upward-diffusion referent),
**`peer_older` added** (template-setter; tests diffusion direction), `pop2039` robustness, `own_lag`
comparator only. The amended §5 rule keys on sign, not magnitude.

**Contradiction correction (Anne caught this).** The earlier draft said "β flips sign across
specs." That was wrong — it conflated lag variation with spec variation. The corrected reading
from the rebuilt full β matrix (birth-year-bin cohorts, all specs × CR/COL × lags):

| spec (role) | β CRI lag1 | β COL lag1 | β CRI lag2 | β COL lag2 |
|---|---|---|---|---|
| `peer_younger` (primary) | +0.17 | +1.33 | +0.12 | +0.05 |
| `peer_older` (clean) | +0.16 | +0.61 | +0.05 | +0.04 |
| `pop2039` (robustness) | +0.29 | +0.97 | +0.08 | +0.02 |
| `own_lag` (comparator) | +0.36 | +0.98 | −0.01 | +0.00 |

β is **uniformly positive at lag 1 across every spec and both countries** — *not* sign-flipping.
At lag 2 the estimates collapse toward zero. The only negative is a tiny, insignificant
comparator value (CRI `own_lag` lag2, −0.009).

> Sign convention: amplifying cascade = decline accelerates as the not-married share rises, i.e.
> **β < 0**. Every clean estimate is β > 0 (stabilizing) → the preliminary lean is **away from
> H_cascade**, consistent with Anne's standing read. NOT a result — gated on the calibrated run.

### A2 — Pseudo-cohort construction and the band-transition artifact
Task A assigns each (year, band) cell a cohort via `central_cohort = year − band_midpoint`,
binned to 5-year groups. The smoke-test fig-1 shows **sawtooth steps at 2012 / 2017 / 2022** —
the points where a cohort crosses into an older band that structurally marries more. *Decision
needed:* accept this construction for the eye-test, request a within-band-segmented redraw, or
specify a different cohort-tracking rule. (The Task B curvature read is partly insulated because
it uses second differences — please confirm you accept that.)

### A3 — How β's spec-sensitivity feeds the §5 rule
Because β is not sign-stable, §5 will not resolve to a single clean cell. Per the pre-registration
spirit, the adjudication rule should be fixed **before** the preferred answer is known. *Decision
needed:* e.g. "H_cascade only if β is amplifying & significant under the primary spec **and** ≥1
robustness spec; otherwise H_shock/H_mixed." Your call on the exact bar.

### A4 — Localization-summary thresholds
The period-vs-cohort curvature comparison (Task B) uses RMS of second differences, with
"entry cohorts = youngest third of cohort groups" and the 2018–2024 window for periods — both
arbitrary cuts. *Decision needed:* confirm or replace.

---

## B. Verification you should do (cheaper, still gating)

### B5 — Identification wall, by code-read (Stage 1.5 standard)
Verify by reading, not by trust, that scripts 1–2 never touch TFR: the `assert_no_tfr()` guard
(it correctly **fired** on the first smoke-test run), and that `data/national/` is read **only**
in script 3's comparison overlay. `w` is not an object of 2b anywhere.

### B6 — Band/base consistency with Stage 1.5
Confirm `BAND_MIDPOINT` (20–39, 5-year bands) and `single = 1 − cohab − married` reproduce the
coupling-identification series base exactly — not a re-derivation.

### B7 — CR/COL data-form asymmetry (§3/§8 amendment, logged 2026-06-20)
Accept that CR is held as **REDATAM-tabulated aggregates** (microdata robustness foreclosed) while
COL is **microdata**, and that the memo must label — not paper over — this asymmetry.

---

## C. Reconciliation gate

### C8 — Your points document vs this instruction  *(the endorsement)*
If your framing of question (A) — the hypothesis set (§2) or the decision rule (§5) — differs
from what is written, **your framing governs** and the instruction is amended before
execution-of-record. **Your endorsement here is what unblocks both Stage 3 scaling and Nina's
(B) reflexive-feedback build.** Sign by filling `endorsed_by:` in the instruction frontmatter and
noting any §2/§5 amendments in its §10 amendment log.

---

## What you do NOT need to adjudicate
- Whether the data are in hand — verified by code-read 2026-06-20 (both series complete, match §3).
- Whether the scripts run — smoke-tested end-to-end; three implementation bugs found and fixed.
- The intensity leg (`w`, parity-progression by union type) — out of scope, gated to 2c.

---

*Drafted by Claude, 2026-06-20, on Héctor's instruction. The single highest-leverage item is
**A1 (reference group)**: it alone determines whether (B) is warranted. Everything else is hygiene.*

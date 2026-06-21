---
type: read_memo
stage: 2c
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2c-i — the read: COL individual-level status model (the cascade-below-the-cell pivot)"
target: Anne (population economics)
date_added: 2026-06-21
added_by: Claude
endorsed_by: Anne
amended: "2026-06-21 — Anne's two binding corrections applied (entry margin ENDS-gated; β>0 framing guard). See amendment log + STAGE2c_Anne_read_signoff.md."
depends_on:
  - "STAGE2c_col_individual_instruction.md (design endorsed by Anne 2026-06-21; §4 rule, 9a ruling)"
  - "STAGE2b_compositional_cascade_memo.md (the cell-level non-cascade verdict this interrogates)"
  - "STAGE2b_Anne_read_signoff.md (B7 ecological correction → motivates this test)"
status: "Full-data run complete (GEIH 2007–2024 microdata, 2.96M women 15–39). §4 rule applied. Read ENDORSED by Anne with two corrections (below)."
---

# Stage 2c-i — The Read

**Numbers below are from the full-pool run** — DANE GEIH person microdata, all 12 months ×
2007–2024, women 15–39, **2,961,956 persons** collapsed to covariate cells (grouped-binomial
MLE = the person-level logit MLE). Per Anne's 9a ruling, 2c-i can only *fail to reopen* (B),
never *close* it.

## Headline

**No amplifying individual-level dependence. The 2b non-cascade verdict survives the
ecological-aggregation objection.** Moving the *outcome* from the cell share to the individual
woman does **not** reveal the reflexive cascade aggregation could in principle have masked.
Reading: **`H_confirm`** → **(B) deferred, aggregation-cleared, pending ENDS — NOT closed.**

## The decisive quantity — individual β beside the 2b cell β

β = coefficient on the individual's lagged reference **not-married** share. **Amplifying requires
β < 0 and significant.** Cluster-robust on band×year; FE C(age_band)+C(cohort_start)+urban; lag 1.

| spec (role) | indiv β (2c-i) | p | amplifying? | 2b cell β (COL) | verdict |
|---|---|---|---|---|---|
| `peer_younger` (primary) | **+0.45** | 0.001 | no (β>0) | +1.33 | confirms non-amplifying |
| `peer_older` (clean) | +0.27 | 0.130 | no (β>0) | +0.61 | confirms non-amplifying |
| `pop_all` (robustness) | +0.51 | 0.024 | no (β>0) | +0.97 | confirms non-amplifying |

β > 0 at every spec and lag (lag-2 attenuates toward 0, stays positive; education-control
robustness pre-2021: +0.40, p=0.013). Sign agrees with the 2b cell sign. `H_reopen` not satisfied.

> **[Anne 2026-06-21 — framing guard]** β > 0 is **not** a behavioral finding. It is most
> parsimoniously mean-reversion / stabilizing or residual confounding the FE do not fully absorb,
> not "compensating/contrarian marriage." Only the *absence* of β < 0 is load-bearing; report the
> positive sign solely as "not the cascade signature."

## §4 rule applied

Non-amplifying across specs incl. the entry band → **H_confirm**; not H_reopen; not H_entry-margin
(below). **Ruling on (B) for COL:** deferred, aggregation-cleared, pending ENDS — not closed
(Anne 9a). Stage 3 sufficiency proceeds in parallel as a no-reflexivity model until ENDS speaks.

## The 15–19 entry margin

2b's 20–39 floor left 15–19 unobserved. 2c-i extends to 15 (651,419 women):
- 15–19-only, `pop_all`: β = −1.29, p = 0.80 — noise.
- 15–19-only, `peer_older`: β = +31.3 — near-degenerate logit (marriage ≈ 0; not-married ≈ 0.99);
  sign not amplifying, magnitude uninterpretable.
- Full-sample interaction `ref_lag × 1[15–19]`: β = +0.07, p = 0.97 — no extra amplification.

> **[Anne 2026-06-21 — correction]** `entry_band_amplifying = False`, but the entry margin is
> **NOT cleared here — it is structurally ENDS-gated.** The married-status model is degenerate at
> 15–19, and an entry-margin cascade lives in *first-union formation* (entry into cohabitation /
> delayed union), an outcome a marriage-status model on a 99%-not-married band cannot observe by
> construction. The interaction is the only powered piece and tests the wrong outcome for that
> band. The entry margin folds into 2c-ii (ENDS); it is **not discharged here.** (Optional cheap
> interim look: the multinomial cohabiting-vs-single margin at 15–19 — still composition, not
> transitions, so it does not change the gating.)

## What this clears, and what it does not

- **Clears (B7).** Ecological-aggregation worry discharged on COL: individual-outcome β agrees in
  sign and significance pattern with the 2b cell β.
- **Does not close (B).** A status model on repeated cross-sections cannot observe a process in
  time. Closure waits on ENDS (2c-ii). Logged as gated; not attempted on GEIH.

## Limitations (instruction §7)

- No true transitions (2c-ii on ENDS is the definitive test).
- Reflection problem persists (lagged distinct-group referent is partial mitigation).
- COL only (CRI cannot support this — REDATAM aggregates).
- Reference share still aggregate; only the LHS moved to the individual.
- Survey design not modeled — sign-based null is immune (proper strata/PSU SEs shrink spurious
  significance, never flip +0.45 to −0.45).
- Entry-band logit fragile (marriage ≈ 0 at 15–19); see Anne's correction above.

## Verification status

- `assert_no_tfr` — ✅ 0 VIOLATION / 19 PASS. TFR never loaded; `w` not a 2c-i object.
- Coverage — 2,961,956 women, 2007–2024, all five bands incl. 15–19 (651k); urban 100%, education
  82% (pre-2021 P6210; 2021 redesign break → robustness only).
- Specs — full reference-spec × lag grid, with/without 15–19, + education robustness; comparison
  to 2b cell-level β explicit.
- **Sector covariate deferred** (not dropped): lives in the GEIH labor/ocupados module, needs a
  within-survey join. *Anne forward flag:* sector/SES is irrelevant to this verdict but central to
  the SDT two-faces framing (Esteve) — needed when that section is written.

## Gate

Read **endorsed by Anne** (STAGE2c_Anne_read_signoff.md) with the two corrections above.
Debb writes `endorsed_by: Anne` (done in this frontmatter) and on the instruction's read gate.
(B) deferred, aggregation-cleared, pending ENDS. Stage 3 sufficiency proceeds in parallel as a
no-reflexivity model.

## Amendment log

- **2026-06-21 — Anne's sign-off corrections applied.** (1) Entry-margin conclusion changed from
  "checked and does not overturn" to "structurally ENDS-gated, not discharged here." (2) Framing
  guard added: β > 0 is not a behavioral finding. `endorsed_by` → Anne.

*Stage 2c-i read. Claude, 2026-06-21. Endorsed by Anne with corrections.*

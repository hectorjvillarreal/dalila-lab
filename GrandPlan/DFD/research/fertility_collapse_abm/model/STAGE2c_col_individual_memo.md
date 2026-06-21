---
type: read_memo
stage: 2c
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2c-i — the read: COL individual-level status model (the cascade-below-the-cell pivot)"
target: Anne (population economics)
date_added: 2026-06-21
added_by: Claude
endorsed_by:                       # pending Anne — §6 criterion 4 / instruction §9b
depends_on:
  - "STAGE2c_col_individual_instruction.md (design endorsed by Anne 2026-06-21; §4 rule, 9a ruling)"
  - "STAGE2b_compositional_cascade_memo.md (the cell-level non-cascade verdict this interrogates)"
  - "STAGE2b_Anne_read_signoff.md (B7 ecological correction → motivates this test)"
status: "Full-data run complete (GEIH 2007–2024 microdata, 2.96M women 15–39). §4 rule applied below. Pending Anne's endorsement of this read (the later gate; design was already endorsed)."
---

# Stage 2c-i — The Read

**Numbers below are from the full-pool run** — DANE GEIH person microdata, all 12 months ×
2007–2024, women 15–39, **2,961,956 persons** collapsed to covariate cells (grouped-binomial
MLE = the person-level logit MLE; see instruction §0 and the script docstring). This applies
the §4 pre-registered rule mechanically; **Anne's endorsement is still the gate**, and per her
9a ruling 2c-i can only *fail to reopen* (B), never *close* it.

## Headline

**No amplifying individual-level dependence. The 2b non-cascade verdict survives the
ecological-aggregation objection.** Moving the *outcome* from the cell share to the individual
woman does **not** reveal the reflexive cascade that aggregation could in principle have masked.
Reading: **`H_confirm`** → **(B) deferred, aggregation-cleared, pending ENDS — NOT closed.**

The aggregation concern Anne raised in B7 is now **discharged**: the relationship did not
sign-flip below the cell. What remains open is not aggregation but *time* — a cascade is a
process, and a status model on repeated cross-sections cannot observe the process. Only the
ENDS true-transition hazard (2c-ii, gated) can.

## The decisive quantity — individual β beside the 2b cell β

β = coefficient on the individual's lagged reference **not-married** share. **Amplifying
(self-reinforcing retreat) requires β < 0 and significant** (P(married) falls as the reference
not-married share rises) — same sign convention as 2b. Cluster-robust on band×year (~68–85
clusters); FE backbone C(age_band)+C(cohort_start)+urban; lag 1 (where signal concentrates).

| spec (role) | indiv β (2c-i) | p | indiv amplifying? | 2b cell β (COL) | verdict |
|---|---|---|---|---|---|
| `peer_younger` (primary) | **+0.45** | 0.001 | no (β>0) | +1.33 | confirms non-amplifying |
| `peer_older` (clean) | +0.27 | 0.130 | no (β>0) | +0.61 | confirms non-amplifying |
| `pop_all` (robustness) | +0.51 | 0.024 | no (β>0) | +0.97 | confirms non-amplifying |

**β > 0 at every spec and lag** (lag-2 attenuates toward 0 but stays positive; education-control
robustness on the pre-2021 subsample: +0.40, p=0.013 — unchanged). The individual sign **agrees
with the 2b cell sign** (positive everywhere): own marriage probability is *higher*, not lower,
where the reference not-married share is already elevated — the opposite of the cascade
signature. `amplifying_any_spec = False`, `amplifying_robust = False`. The `H_reopen` row of §4
(amplifying & significant, robust across specs) is **not satisfied**.

## §4 rule applied

| §4 condition | observed | → |
|---|---|---|
| non-amplifying incl. 15–19 | β>0 all specs, incl. entry band | **H_confirm** |
| amplifying & significant, robust | no | not H_reopen |
| amplifying only in 15–19 | no (see below) | not H_entry-margin |

**Ruling on (B) for COL:** **deferred, aggregation-cleared, pending ENDS** — *not* closed (Anne
9a). Stage 3 sufficiency may proceed **in parallel** under this branch as a **no-reflexivity**
model; it stays no-reflexivity until ENDS (2c-ii) speaks.

## The 15–19 entry margin — 2b's one masking caveat, now tested

2b's 20–39 floor (B6) left the 15–19 ignition zone unobserved — the single caveat the 2b memo
flagged as able to hide a true cascade. 2c-i extends the floor to 15 and looks directly
(651,419 women observed in the entry band):

- **15–19-only, `pop_all` referent:** β = −1.29, **p = 0.80** — wrong-signed but pure noise.
- **15–19-only, `peer_older` referent:** β = +31.3 (positive → non-amplifying); near-degenerate
  logit (marriage is virtually absent at 15–19, not-married share ≈ 0.99), so the magnitude is
  not interpretable — but the sign is not amplifying and the estimate is fragile, not a cascade.
- **Full-sample interaction** `ref_lag × 1[15–19]`: β = +0.07, **p = 0.97** — no extra
  amplification in the entry band.

`entry_band_amplifying = False`. **The ignition-zone caveat is checked and does not overturn the
verdict.** (ENDS will still see this band's *transitions*, which a status model cannot.)

## What this clears, and what it does not

- **Clears (B7).** The ecological-aggregation worry is discharged on COL: the individual-level
  outcome does not reveal a masked amplifying dependence. The 2b ecological β and the 2c-i
  individual β agree in sign and significance pattern.
- **Does not close (B).** A non-amplifying *status* model on repeated cross-sections cannot
  observe a *process in time*. Closure waits on the ENDS retrospective union/marriage histories
  (2c-ii) — the genuine discrete-time union-formation hazard. Logged as gated; **not** attempted
  on GEIH.

## Limitations (instruction §7)

- **No true transitions.** 2c-i is a union-*status* model; the definitive transition test is
  2c-ii (ENDS, gated on the pending acquisition).
- **Reflection problem persists** at the individual level. The lagged distinct-group referent is
  partial mitigation (as in 2b), not clean causal identification.
- **COL only.** CRI cannot support this (REDATAM aggregates — no microdata). One-country look;
  external validity (ARG/CHL channel-absent prediction) unchanged.
- **Reference share is still aggregate.** Only the LHS moved to the individual; the regressor is
  a band×year group share.
- **Survey design not modeled.** Expansion weights enter the point estimate (normalized to
  sample N); strata/PSU are not modeled — same posture as 2b. Inference rests on band×year
  clustering, the level at which the regressor varies.
- **Entry-band logit is fragile** (marriage ≈ 0 at 15–19); read its sign, not its magnitude.

## Verification status

- `assert_no_tfr` — ✅ **0 VIOLATION / 19 PASS**. TFR never loaded; `data/national/` never read;
  `w`/fertility intensity not a 2c-i object (gated to ENDS). Trail: `outputs/stage2c/_assert_no_tfr.log`.
- Coverage — 2,961,956 women, 2007–2024, all five bands incl. 15–19 (651k); urban 100%,
  education 82% (pre-2021 P6210; post-redesign recoding break → robustness only, as designed).
- Specs — full reference-spec × lag grid, with/without 15–19, + education robustness; comparison
  to 2b cell-level β explicit (`outputs/stage2c/stage2c_vs_2b_beta.csv`).
- **Sector covariate deferred** (not silently dropped): economic sector lives in the GEIH
  labor/ocupados module, not the general-characteristics person frame loaded here; would require
  a within-survey module join (DIRECTORIO+ORDEN+HOGAR). Urban (CLASE) and education (P6210) are
  the cleanly-available person-level covariates. Logged for Anne, consistent with the B7 posture.

## Artifacts (`outputs/stage2c/`)

`person_cells_COL.csv.gz` (collapsed person cells) · `ref_shares_COL.csv` (band×year not-married,
incl 15–19) · `stage2c_individual_estimates.csv` · `stage2c_vs_2b_beta.csv` ·
`stage2c_entry_margin_COL.csv` · `stage2c_multinomial_COL.csv` (descriptive) ·
`stage2c_reading.json` · `_assert_no_tfr.log`. Code: `stage2c_individual_model.py`.

## Gate (instruction §6 criterion 4)

Anne endorses this read → her standing ruling on (B):
- **H_confirm (this read)** → "(B) deferred, **aggregation-cleared**, pending ENDS." Stage 3
  sufficiency proceeds in parallel as a no-reflexivity model. Debb writes `endorsed_by: Anne`
  on this memo and the instruction's read gate.
- Reconcile framing against the distributed demographic half (SDT framing note) if it differs.

*Stage 2c-i read. Claude, 2026-06-21, on Héctor's instruction. Design endorsed by Anne; this read pending Anne's endorsement.*

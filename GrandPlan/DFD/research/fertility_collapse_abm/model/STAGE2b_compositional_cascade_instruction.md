---
type: build_instruction
stage: 2b
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2b — Compositional-vs-cascade discrimination (demographic-measurement leg of question A)"
target: Claude Code (Dalila)
date_added: 2026-06-20
added_by: Claude
endorsed_by:                      # pending Anne — see §10
seeds: "Question (A) — compositional-vs-cascade (orientation §6A)"
depends_on:
  - "STAGE1_5_identification_memo.md (v3.0) — frozen invariants, gate of record"
  - "STAGE2_calibration_results.md — skeleton frontier (the partial validation this stage interrogates)"
gates:
  - "Stage 3 (four-country nesting + GPU sweep)"
  - "Question (B) — Nina's reflexive-feedback build (modeling chat)"
compute: "CPU / Python (pandas, statsmodels). Anne CPU-native default per compute-envelope brief. No GPU, no Julia — this is pseudo-panel work on a handful of annual cross-sections."
build_instruction: "Drafted by Claude on Héctor's instruction, 2026-06-20, following Anne's demographic mandate. To be reconciled against Anne's points document and endorsed by Anne before execution-of-record."
---

# Stage 2b — Compositional-vs-Cascade Discrimination
# Demographic-measurement leg of question (A)
# Target: Claude Code (Dalila) · Workspace: DFD — Demographic Collapse Paper (Anne-led)

---

## 0. Purpose and posture

The Stage 2 skeleton partially validates the mechanism but cannot tell us *why* the
marriage collapse happens: the orientation (§6A) identifies two observationally
distinguishable theories — a **within-cohort coordination cascade** versus
**cohort-replacement / generational abandonment of marriage** — and notes the skeleton's
collapse is driven by cohort turnover "as much as" by a within-cohort threshold. The
answer determines whether Nina's next move (B, reflexive feedback) is structurally right.

Stage 2b is the **demographic measurement** that resolves this, on data already on Dalila.
It is deliberately conservative:

- It runs **only** on in-hand series (CR ENAHO, COL GEIH). The fertility-intensity leg
  (parity-progression by union type) is **out of scope** here — it is gated on the
  pending Colombia ENDS and CR married-ASFR acquisitions and belongs in a later Stage 2c.
- It claims **apportionment, not selection.** The prior, from the skeleton, is that both
  forces are present. The decision-relevant question is narrower than "which one": it is
  *whether a within-cohort, state-dependent (reflexive) component exists, over and above
  the mechanical cohort-mix shift.* That, and only that, justifies (B).
- The decision rule is **pre-registered below, before any estimation**, so the test cannot
  be retrofitted to a preferred conclusion.

This stage does **not** build, modify, or calibrate the ABM. That is the modeling chat's
territory (orientation §9). Stage 2b produces a read; the read flows across the seam.

---

## 1. Inherited discipline (do not violate)

**Frozen invariants (Stage 1.5 gate of record).**
1. State variable is union **composition** {single, cohabiting, married}, never union level.
2. `w` (cohabiting-to-married fertility-intensity ratio) is a nested structural parameter —
   it is **not** estimated or used in Stage 2b at all (it lives in the gated intensity leg).
3. Nonlinearity locus is `w`-determined — again, not a Stage 2b object.

**Identification wall.** Period TFR enters Stage 2b **for comparison plotting only**. It is
never a regressor, never a cohort/period weight, never tunes any quantity. Verify by
code-read, not by construction — the same standard the skeleton met.

**Band and base consistency.** Use the **same age-band definitions and population base** as
STAGE1_5 (the coupling identification series), so 2b composition is directly comparable to
the Stage 1.5 finding. Do not re-derive bands.

---

## 2. Hypotheses (pre-registered)

| Tag | Theory | Predicted signature |
|---|---|---|
| **H_cohort** | Cohort-replacement / generational abandonment | Each entry cohort arrives with lower marriage propensity; **flat within-cohort**; aggregate moves by mix-shift. Acceleration localizes to **entry cohorts**, weak period interaction. |
| **H_shock** | Exogenous common period shock (e.g. housing cost, recession) | All cohorts bend at the same calendar time, **but the response is not self-reinforcing** — no dependence on the contemporaneous reference share. |
| **H_cascade** | Within-cohort coordination cascade (reflexive) | Period bend **and** state-dependence: the within-cohort decline is **larger where the reference-group cohabitation/singlehood share has already crossed a level**. |
| **H_mixed** | Combination | Apportion the acceleration across the above. Treat as the **prior**, not a fallback. |

The critical distinction, and the reason H_shock is separated out: **a period effect alone
is necessary but not sufficient for a cascade.** Only H_cascade carries state-dependence,
and only H_cascade justifies (B)'s reflexive structure. Conflating "period effect" with
"cascade" is the error this stage exists to avoid.

---

## 3. Data (in-hand only)

| Source | Coverage | Form held | Role |
|---|---|---|---|
| CR ENAHO 2010–2024 | annual, by band, {married, cohabiting} | **REDATAM-tabulated aggregates** (server-side crosstabs via INEC RpWebStats; *not* microdata) | primary identification country |
| COL GEIH 2007–2024 | annual, by band, {married, cohabiting} | DANE **microdata** (monthly files pooled to annual) | primary identification country |
| MEX ENOE (biennial) | coarse, by band | aggregates | comparator only |

Derive `single = 1 − cohabiting − married` within band to obtain the composition simplex
{single, cohabiting, married}. Restrict to the Stage 1.5 reference population.

**Form-of-data note (verified 2026-06-20, code-read).** Both series are confirmed in hand
and match this table: `CRI_coupling_annual.csv` (15 yrs, observed, no interpolation) and
`COL_coupling_annual.csv` (18 yrs). The asymmetry matters: CR is held only as the aggregated
band×year×{married,cohabiting} crosstab (REDATAM web engine — no microdata download), whereas
for COL the underlying microdata is on Dalila. Tasks A–C operate on the aggregated composition
panel, so the aggregate form is sufficient for both; but any individual-level reweighting or
microdata robustness check is foreclosed for CR in a way it is not for COL (see §8).

**Out of scope for 2b (deferred to 2c, gated on acquisitions):** married-vs-cohabiting
fertility differential; parity-progression by union type. Do not attempt these here — the
data are not in hand and any estimate would be uncalibrated.

---

## 4. Operations for Claude Code

**Task A — Pseudo-cohort construction.**
From the annual cross-sections, build synthetic (pseudo-) cohorts: follow each 5-year birth
cohort across surveys as it ages through the bands. Output a tidy panel
`(country, birth_cohort, age_band, year, share_single, share_cohab, share_married)`.

**Task B — Synthetic-cohort APC on composition (curvature-focused).**
Decompose the marriage-share (and cohabitation-share) series into age, period, and cohort
components. **Acknowledge the linear APC identification problem explicitly**: do not report
or interpret the inseparable linear trends. Report **only identified contrasts —
second differences / curvature** — and use them to answer one question: does the
2018–2024 acceleration localize in **periods** (all live cohorts bend together) or in
**cohorts** (successive entry cohorts step down)? State the identifying normalization in
the output. A transparent descriptive pseudo-panel plot (cohort lines over calendar time)
must accompany the formal decomposition — the eye test is part of the evidence here.

**Task C — State-dependence (reflexivity) test [the sharp test].**
Estimate, within country:

  Δ(marriage_share)_{c,a,t} = β · ReferenceShare_{t−1} + age FE + cohort FE + ε

where `ReferenceShare_{t−1}` is the lagged contemporaneous cohabiting+single share of the
relevant reference group. **Sign and significance of β is the cascade signature**: β with
the amplifying sign (decline accelerating as the reference share rises) is evidence for
H_cascade; β ≈ 0 with a present period effect points to H_shock; β ≈ 0 with the period
effect absent points to H_cohort. Cluster appropriately; report robustness to reference-
group definition and to lag length. Do **not** include TFR on the right-hand side.

**Task D — Apply the pre-registered decision rule (§5) and write the read.**

---

## 5. Pre-registered decision rule (→ implication for B)

**Amended per Anne's adjudication 2026-06-20 (STAGE2b_Anne_endorsement.md).** Bar keys on
**sign** (amplifying = β < 0), not magnitude; the CR/COL magnitude gap is treated as a likely
B7 (ecological-vs-individual) artifact. Reference specs: `peer_younger` (primary), `peer_older`
(added, clean), `pop2039` (robustness), `own_lag` (comparator only). Period windows: **2015–2024
and 2018–2024**. Entry cohorts: **birth-year ≥ 1990**.

| Finding | Reading | Implication for (B) |
|---|---|---|
| Cohort-dominant (Task B), no amplifying β under `peer_younger` | H_cohort | **(B) deferred;** model needs cohort-entry heterogeneity, not within-cohort reflexivity. |
| Period-dominant, β not amplifying / insignificant under `peer_younger` | H_shock | **(B)'s reflexive structure not justified;** needs an exogenous period driver, not endogenous feedback. |
| β amplifying (β<0) & significant under `peer_younger` **AND** ≥1 of {`peer_older`,`pop2039`}, in **both** CR & COL | H_cascade | **(B) warranted.** Nina proceeds with reflexive self-reinforcement. |
| Period component (Task B) + amplifying β under ≥ primary spec, mixed with cohort component | H_mixed | **(B) warranted ONLY for the period share;** quantify and document. |

CR evidence reads as coarser (ecological / cell-level) in the "both countries" requirement (B7).
This rule is fixed as amended. Any further deviation must be logged as a protocol amendment
with reason, not silently absorbed.

---

## 6. Deliverables

- `STAGE2b_compositional_cascade_memo.md` — the read for Anne: which hypothesis the data
  support, the decision rule applied, and the limitations (§8) stated in full.
- `stage2b_apc_composition.py` — Tasks A–B.
- `stage2b_state_dependence.py` — Task C.
- `stage2b_figures.py` — figure-data emitter (pseudo-panel cohort lines; APC curvature;
  β with CI by reference-group spec).
- `outputs/` — composition panels, APC contrasts, regression tables, figure data.

All `endorsed_by` blank pending Anne. Documentation to PROTO-RAG-001 (structured headers:
Purpose, Inputs, Outputs, Assumptions, Dependencies) — Nina's code-documentation standard
applies even though this is CPU/Python work.

---

## 7. Gate criteria (Stage 2b complete)

1. Pseudo-panel and APC contrasts produced for CR and COL (MEX comparator where biennial
   coverage allows).
2. State-dependence β estimated with robustness.
3. Decision rule applied; the (B) implication stated unambiguously.
4. Limitations documented.
5. **Anne endorses** the memo. Her endorsement is the trigger that unblocks both Stage 3
   scaling and (B) in the modeling chat.

---

## 8. Limitations (state explicitly in the memo)

- **Pseudo-panel, not panel.** ENAHO/GEIH are repeated cross-sections; we follow synthetic
  cohorts, not individuals. No individual union transitions are observed. Compositional
  shifts are inferred from changing cohort aggregates, not from transition rates.
  **Asymmetric for CR vs COL:** the CR series is held only as REDATAM-tabulated aggregates
  (no microdata download), so for CR even individual-level reweighting or sensitivity to
  alternative band/weight definitions is foreclosed — the aggregate crosstab is the atom.
  COL retains microdata on Dalila, so COL robustness can in principle go below the aggregate;
  CR robustness cannot. Do not present a microdata robustness check for CR; if one is run for
  COL, label the CR/COL asymmetry rather than implying parity.
- **Coarse band grid (20–39, four 5-year bands).** A 5-year birth cohort occupies one band for
  ~5 calendar years, so within-cohort, within-band annual Δ(marriage_share) — the LHS of the
  Task C state-dependence regression — is partly confounded with aging *inside* the band.
  Control for age FE as specified and report robustness to band-edge definition; flag that the
  state-dependence β is identified off cohort×period variation net of this within-band aging,
  not free of it.
- **APC linear identification.** Only curvature is identified. The conclusion rests on where
  the *acceleration* localizes, not on level trends — state this and do not overreach.
- **External-validity ceiling.** Both identification countries are **high-cohabitation
  regimes**. A cascade signature here may not generalize to marriage-dominant Southern Cone
  settings. Argentina (and Chile) would identify the structure where CRI+COL cannot, but
  they are **out of scope** for 2b (acquisitions pending, orientation §7).
- **Tempo caveat, residual.** Union composition is a stock and is largely insulated from the
  period-TFR tempo contamination that stalled the Stage 1.5 lead test. But shifts in
  *first-union timing* can still masquerade as composition change in a pseudo-panel — flag
  this; do not claim it resolved.
- **Intensity leg absent.** Whether married and cohabiting unions differ in fertility (`w`)
  is untouched here. 2b speaks to the *structure of the union collapse*, not its fertility
  translation. The two rejoin at 2c / Stage 4.

---

## 9. What this stage does NOT do

- It does not build, alter, or calibrate the ABM (modeling chat).
- It does not estimate or use `w`.
- It does not claim a clean coupling→fertility lead (unidentified since Stage 1.5).
- It does not acquire data — it uses only what §3 lists as in hand.

---

## 10. Provenance and filing

- Working location: `GrandPlan/DFD/research/fertility_collapse_abm/model/STAGE2b_compositional_cascade_instruction.md`
- **Archived (build record):** `_crossrefs/_build_instructions/2026-06-20_fertility_collapse_abm_stage2b.md`
  (PROTO-RAG-001; `status: executed`, pending Anne's endorsement). Travels with this branch;
  reaches `main` at merge, per the Stage 1 precedent.
- **Reconcile against Anne's points document** when it lands; if its (A) framing differs from
  the hypothesis set or decision rule here, Anne's framing governs and this instruction is
  amended before execution.
- **Anne's endorsement is the execution-of-record gate.** This is a seed drafted on Héctor's
  instruction following Anne's mandate, not a substitute for her sign-off.

### Amendment log
- **2026-06-20 — data-form verification (Claude, on Héctor's instruction).** Code-read confirmed
  both §3 series are in hand and match coverage: `CRI_coupling_annual.csv` (ENAHO 2010–2024, 15
  yrs, observed) and `COL_coupling_annual.csv` (GEIH 2007–2024, 18 yrs). Recorded the
  CR-vs-COL **form** asymmetry — CR held only as REDATAM-tabulated aggregates (no microdata),
  COL as DANE microdata — by adding a "Form held" column and note to §3 and sharpening two §8
  limitations (microdata-robustness foreclosed for CR; coarse 4-band grid confounds within-band
  aging in the Task C LHS). Clarifications only; the hypothesis set (§2) and pre-registered
  decision rule (§5) are unchanged. Pre-endorsement, so not a protocol amendment under §5.
- **2026-06-20 — Anne adjudication (STAGE2b_Anne_endorsement.md).** §5 rule amended: bar =
  amplifying (β<0) & significant under primary (`peer_younger`) + ≥1 clean spec, in both CR & COL;
  `peer_older` spec added; substantive period windows (2015–2024 and 2018–2024) and entry-cohort
  cut (birth ≥ 1990) replace the mechanical youngest-third/single-box cuts; pseudo-cohorts
  redefined by birth-year bin (year − band_lower, not band_midpoint, A2); CR β tagged ecological
  (B7). Hypothesis set (§2) endorsed **unchanged**. Implemented in code 2026-06-20 (Claude):
  `stage2b_apc_composition.py` (A2 cohorts, Lexis within-band curvature, windows, entry cut),
  `stage2b_state_dependence.py` (`peer_older`, full β matrix), `stage2b_figures.py` (within-band
  segmented fig-1). `endorsed_by` stays blank pending the six execution conditions + calibrated run.

---

*Stage 2b build instruction. Drafted by Claude, 2026-06-20, on Héctor's instruction,
following Anne's demographic mandate. §5 amended per Anne 2026-06-20; endorsed_by blank pending
the six execution conditions (STAGE2b_Anne_endorsement.md) and the calibrated run.*

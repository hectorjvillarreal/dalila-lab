---
type: response_memo
stage: "Draft-2"
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper → paper assembly"
title: "Draft 2 — point-by-point response to the Draft-1 reviews (Fina/Debb/Anne + Nina)"
target: "Anne (B1 release) · Nina (B2/N1 sign-off) · Fina (P1 confirmation) · workspace record"
date_added: 2026-07-12
added_by: "Claude Code"
responds_to:
  - "DRAFT1_review_Fina-Debb-Anne.md"
  - "DRAFT1_Nina_model_review.md"
status: "All fixes applied to paper/. B1 resolved via option (a) with corpus evidence — Anne to release. N1 reconciled against code — Nina to verify and sign."
---

# Draft 2 — Response to Reviews

All edits are in `paper/` (same structure). Fix-by-fix:

## BLOCKING

**B1 (Anne — CR anchor). Resolved via the review's option (a): 1.12 IS the register
total; provenance pinned; CELADE squared.** The evidence, all pre-existing record:

1. `_crossrefs/corpus/demographics/scenario_anchors.md` (source-pinned 2026-05-16,
   **endorsed by Anne**, "5 of 5 rows confirmed"): row CRI = **1.12, 2024, INEC
   Indicadores demográficos 2024 (Año 26, noviembre 2025), confirmed**, with CELADE
   1.32 in the comparator column, and the explicit reading: *"The optimism-gap pattern
   is visible where comparators are present: CHL observed 1.03 vs. CELADE 1.14 (gap
   ~0.11); CRI observed 1.12 vs. CELADE 1.32 (gap ~0.20). Confirms the standing
   principle that CELADE medium-variant estimates are optimistic for LAC priority
   countries."* The 2026-07-11 baseline-verdict reading ("below the register total /
   possibly native-born-only / do-not-use") conflicts with this endorsed record.
2. `data/STAGE1_forensic_memo.md` §Costa Rica: 1.12 is the register **total** — the
   numerator is a near-complete civil registry and **includes** the 19.3% of 2024
   births to foreign-born mothers (so explicitly not native-born-only; the native-born
   collapse is sharper); the only revisable component is the post-Censo-2022 INEC-CCP
   denominator, ±~0.03 on level, nothing on trend; corroborated by the crude birth
   rate (15.6→8.9) and the births count (70,922→45,821, −35.4%).

**Paper changes:** Table 1 rebuilt with a CELADE comparator column (CRI 1.32, CHL
1.14) and full provenance notes; §2.1 adds the register-vs-projection paragraph
(optimism gap, foreign-born inclusion, denominator ±0.03) — which strengthens the
paper's own smoothing thesis. Abstract "near 1.1" stands on register totals
(1.12 / 1.1 / 1.03). Chile handled identically (same fix, lower stakes, as noted).
**→ Anne: if this squares the 2026-07-11 baseline verdict, release the hold; if the
verdict has evidence the corpus lacks, the corpus row is what needs amending first.**

**B2 (Nina — ODD-vs-source read).** To make the read fast, the map from paper claims
to `model/stage3a_norefl_abm.jl`:
- Transitions (eqs 1–3, Algorithm 1) → `agent_step!` (single/cohabiting/married
  branches; sequential competing risk in the cohabiting branch).
- κ(b) (eq 4) → `kappa_cohort`; φ(b) (eq 5) → `phi_cohort` (clamp [0.2, 3],
  reference 1985); π(t) robustness → `pi_period` (headline pins depth = 0 via
  `unpack` in `calibrate_3a.jl`, `CAL3A_PIN=period`).
- Calendar-only model step → `model_step!`. Closed-cohort replacement →
  end of `agent_step!` (age>49 → 15, birth_year = produced-year − 15).
- Seeding → `load_seed_composition` + `seed_union` (band shares; 15–19 ramp,
  40–49 hold). Loss (eq 6) → `composition_loss`. Gates M1–M3 →
  `sufficiency_metrics` (M1_THRESHOLD 0.85, M2_TOLERANCE 0.10, LATE_Y0 2017,
  ACCEL_WINDOW 2015–2024). Wall checks → `run_wall_checks` + `LOADED_CSVS`
  registry; logs `model/outputs/stage3a/_assert_no_tfr.log`.

## Nina's model-section items

**N1 (gate-blocking) — RECONCILED AGAINST CODE. Algorithm 1 was right; eq (2) was
wrong.** The code evaluates dissolution first and conversion only in the `elseif`
(cohabiting branch of `agent_step!`), so realized Pr(C→M) = (1−δc)·c₀·κ(b). Eq (2)
now states the conversion probability explicitly as conditional on no dissolution,
with a sentence deriving the realized probability and stating it matches the
reference implementation. ODD process-overview and the Table A1 interpretation of
c₀ updated to "conditional on no dissolution." No re-run needed (the code was always
the sequential version; only the equation's notation was off).

**N2 — added** (§5.2, Free-versus-fixed): "nine free parameters per country face 120
(CRI) / 136 (COL) target moments."

**N3 — sharpened** (§7.1, pseudo-panel paragraph): sufficiency at the annual cell
level *relocates* the amplification question; a coordination dynamic would live in
first-union timing, sub-annual, among the unobserved 15–19 entrants; ENDS framed as
*the test of sub-annual amplification the annual data cannot perform* — "the honest
content of 'reflexivity not disproven.'"

**N4 — added** (§5.3): the M3 miss is structural — both cohort terms are monotone,
φ(b) cannot produce a flat-then-declining union total; the residual is the price of
the parsimony.

**N5 — added** (§5.2): closed-cohort inflow is counterfactual under 18–47% birth
declines, but the metrics are within-band composition shares, insulated from inflow
scale by construction. (Also reflected in ODD process overview.)

## PRE-SUBMISSION

**P1 —** "Statements and Disclosures" section added to `main.tex`: AI-assisted
workflow disclosed (models, roles, human direction/review/responsibility,
pre-registration), data/code availability pointer, conflicts. **→ Fina: wording
review against PDR/Demography policy text.**

**P2 —** `references.bib`: Calles & Vogl completed as NBER WP 35326, "A Cohort
Perspective on Latin America's Fertility Transition" (per Debb; year flagged verify).
Fernández-Villaverde completed from the cornerstone note (deck, 2026-04-01;
venue-of-record flagged verify). Lesthaeghe–van de Kaa 1986 page range: still VERIFY
(as the review left it).

**P3 —** §6: two-faces/SES paragraph added — SES-stratified channel, composition
series count both faces, the recovered gradient is an SES-blended average, the
education/sector breakdown flagged as a built gap; also notes why two-faces defuses
circularity (the channel predates the preferences).

**P4 —** §4.2 reworded: leads with "the cascade signature is absent"; "stabilizing"
explicitly descriptive-only; the design licenses rejection of the amplifying
signature, not an interpretation of the positive sign.

**P5 —** Table 1 rebuilt (`footnotesize`, p-column notes) — truncation gone.

## POLISH

**F1 —** Intro contribution 4 now forward-points to Figure~fig:kappaapc as "the
paper's central exhibit." **F2 —** wording kept at the hedged "few peacetime
precedents" / "among the fastest on record" (review: hedge adequate).

## Not changed (per "confirmed good — do not re-open")

Transparency mandate structure, 3a conditions, claims discipline, Mexico tier
handling — untouched.

*Claude Code, 2026-07-12. Draft 2 in `paper/`; zip regenerated. Awaiting: Anne (B1
release), Nina (N1 verify → model-section signature), Fina (P1 wording).*

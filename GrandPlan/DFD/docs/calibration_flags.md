# DFD — Open calibration flags

**Location:** `GrandPlan/DFD/docs/calibration_flags.md`
**Maintained by:** Anne (demographic block) · Cath (fiscal block) · Nina (macro-financial block)
**Last updated:** 2026-05-10
**Status:** Living registry

---

## Purpose

Registry of open integration flags for the DFD OLG calibration, sourced from external material (seminars, papers, working notes) that has not been folded into the corpus or the baseline model yet. Each flag is a concrete action item linked back to its source.

Flags are added when a source produces a calibration-relevant claim. They are closed when the corresponding calibration choice or scenario is committed.

This file is **not** a corpus entry under PROTO-RAG-001 — it is operational scratchspace.

---

## Open flags

### F-2026-05-01 — Fast-transition fertility scenario (Mexico)

- **Owner:** Anne
- **Source:** `_crossrefs/seminario-cepal-2026.md` §Anne (CEPAL XXXVIII Seminario, 2026-05-05)
- **Action:** Run Mexico OLG baseline in parallel with two fertility scenarios — CELADE medium variant (for FMI/WEO comparability) and fast-transition anchored to observed 2024 TFR (1.55), with trajectory consistent with the post-2016 structural break documented by JFV.
- **Rationale:** WEO/IMF baselines rest on CELADE medium TFR, already inconsistent with observed 2024 values. Gap between scenarios bounds fiscal-sustainability uncertainty.
- **Related standing context:** DFD_rag.md §4.3 (the 1.55 fast-transition value is already documented as the DFD scenario value, distinct from the IM-6 data-table reference value of 1.82).

### F-2026-05-02 — Macro-financial stress scenario

- **Owner:** Nina
- **Source:** `_crossrefs/seminario-cepal-2026.md` §Nina (CEPAL XXXVIII Seminario, 2026-05-05)
- **Action:** Add a stress scenario with LAC sovereign spreads widening +150–200 bp sustained over 2–3 years, calibrated to historical LAC spread behavior during US monetary tightening cycles. Run interacted with the F-2026-05-01 fast-transition demographic scenario.
- **Rationale:** US Treasury convenience-yield erosion + maturity shortening + holder displacement to mutual funds creates a transmission channel to LAC via spreads, dollar funding, and capital flows. None of the four CEPAL presentations modeled this interaction.
- **Note:** This is the tail-risk scenario explicitly flagged in the seminar note as unmodeled by Valdés, Roldán, Nieto-Parra, or Pick.

### F-2026-05-03 — WEO growth assumptions vs. fast-transition labor supply

- **Owner:** Anne + Cath
- **Source:** `_crossrefs/seminario-cepal-2026.md` §Anne, §Cath
- **Action:** Audit WEO growth assumptions used in LAC fiscal projections against labor-force trajectories implied by the fast-transition fertility scenario. Document the gap as a calibration risk in the baseline.
- **Rationale:** Real GDP growth (+0.99 pp) is the only structural buffer in Valdés' LAC fiscal gap arithmetic. That contribution depends on labor-force projections derived from CELADE medium variant. Under fast transition, labor-force contribution underperforms baseline within ~20–25 years (one OLG generation).

### F-2026-05-04 — Expenditure rigidity as explicit fiscal parameter

- **Owner:** Cath
- **Source:** `_crossrefs/seminario-cepal-2026.md` §Cath (drawing on CAF Fiscal Resilience Index)
- **Action:** Introduce expenditure rigidity as an explicit parameter in the DFD fiscal module — not absorbed into the residual government budget closure. Quantify usable fiscal space net of rigid commitments.
- **Rationale:** Mexico debt service at ~33% of tax revenue plus rigid expenditure leaves minimal space to absorb demographic-transition pressure on pensions and health. The CAF FRI treats rigidity as a structural dimension; DFD should too.

### F-2026-05-05 — Debt-service / tax-revenue ratio as usable-space indicator

- **Owner:** Cath
- **Source:** `_crossrefs/seminario-cepal-2026.md` §Nieto-Parra, §Cath
- **Action:** Integrate debt-service-to-tax-revenue ratio as a fiscal-space indicator in the calibration. Reference points: Mexico ~33% (2023), Costa Rica ~22%.
- **Rationale:** This ratio pre-commits one of every three pesos of tax revenue (Mexico) before any spending decision. It complements the standard debt-to-GDP metric and captures the room available for new commitments — directly relevant when comparing across countries with different revenue mobilization.

---

## Closed flags

*(none yet)*

---

## How to close a flag

When a flag's action is committed (in a calibration notebook, a scenario file, or a documented model change):

1. Move the entry from "Open" to "Closed" with a date and the commit hash or file reference.
2. If the closure produced a corpus entry under PROTO-RAG-001, link it.
3. Do not delete closed flags — they are part of the calibration provenance trail.

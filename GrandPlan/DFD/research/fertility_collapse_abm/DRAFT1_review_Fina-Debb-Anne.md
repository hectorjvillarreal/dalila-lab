---
type: review
stage: "Draft-1 review"
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led) → paper assembly"
title: "Draft 1 — consolidated review (Fina, Debb, Anne) + prioritized fix list"
target: "Claude Code (Draft 2) · workspace record"
date_added: 2026-07-12
added_by: Claude
reviews: "fertility_collapse_draft1_overleaf.pdf (Claude Code, 2026-07-12)"
status: "Strong draft. One BLOCKING fix (CR anchor). Pre-submission fixes listed. Nina model-section gate still open."
---

# Draft 1 — Consolidated Review

## Overall

A strong, near-submittable draft that executed the build instruction: the outcome-robust arc
lands, the transparency mandate is fully discharged (equations, Algorithm 1, ODD appendix), the
claims discipline holds throughout, and the four clarity mandates are met. The model section reads
as a glass box. What follows is a fix list, not a rejection.

## BLOCKING (fix before any circulation)

**B1 — Costa Rica TFR anchor (Anne).** Table 1 + abstract use CR 1.83→**1.12** and "near 1.1 in
Costa Rica," contradicting the **2026-07-11 baseline verdict**, which HELD CR 1.12 as *below* the
register total (~1.32 CELADE; ~1.33 OWID/2023) — likely native-born-only or a provisional, "do not
use until sourced." Mexico got the tier discipline (1.55 relabeled not-national); CR did not.
Reconcile: pin the INEC provenance that 1.12 is the register total (and square with CELADE 1.32),
**or** correct to ~1.32 — which removes CR from the "near 1.1" cluster and rewrites the abstract.
Chile 1.03 vs CELADE 1.14 is the same issue, lower stakes. **Does not touch the verdict** (TFR is
walled from 2b/2c); it is a Section-2 measurement claim sitting in the abstract.

**B2 — Nina model-section gate still open (Debb/process).** The ODD + Algorithm 1 assert fidelity
to `stage3a_norefl_abm.jl`; that assertion *is* the transparency claim. Nina must read the ODD
against the source before the draft clears the gate. Not verifiable from the paper alone.

## PRE-SUBMISSION (before the paper leaves the building)

**P1 — AI disclosure + authorship (Fina).** Single-author is fine for the persona pipeline, but the
paper was produced via an AI-agent workflow; PDR/Demography disclosure policies apply. Prepare the
disclosure statement now.

**P2 — References (Debb).** Resolve VERIFY flags: Calles & Vogl = NBER WP 35326, "A Cohort
Perspective on Latin America's Fertility Transition" (supply from corpus); Fernández-Villaverde
citation from the cornerstone note; Lesthaeghe–van de Kaa 1986 page range still to pin.

**P3 — §6 two faces / SES (Anne).** The channel argument underplays the Esteve "two faces" /
SES-stratification asked for in the SDT sign-off. Add a paragraph; flag the sector/SES data gap.

**P4 — β>0 framing (Anne).** Keep "stabilizing/mean-reverting" descriptive; lead with "not the
cascade signature." Do not let β>0 become a behavioral claim (standing guard).

**P5 — Table 1 truncation (Debb/production).** Chile and Mexico notes cut off at the right margin;
fix table width.

## POLISH

- **F1 (Fina):** forward-pointer to the signature exhibit (Fig 7) in the introduction — it arrives
  on p.19 and is the strongest evidence.
- **F2 (Fina):** verify "fastest peacetime on record" against East Asian cases; hedge is currently
  adequate.

## Seat sign-offs

- **Fina (structure / claims / strategy):** pass on structure and claims discipline; blocked on P1
  (disclosure) before submission; F1/F2 polish.
- **Debb (provenance / references):** pass on provenance/availability; resolve P2 references; flag
  B1 as a filed-record inconsistency (→ Anne); P5 production.
- **Anne (demographic claims):** **HOLD on B1 (CR anchor).** Everything else demographic matches the
  endorsed memos (β matrix, localization, M-metrics, κ midpoints, caveats). P3/P4 strengthen.

## What is confirmed good (do not re-open)

- Transparency mandate fully met (equations, algorithm, ODD, calibration-in-the-open, wall 11/11).
- Nina's 3a conditions all applied (non-fit convergence led, κ param count, κ–φ separability, period
  reconciliation, M3 phrasing of record).
- Claims discipline intact: no TFR-magnitude claim, reflexivity "not warranted/not disproven," tempo
  sensitivity, bounded external validity, ecological honesty, ABM=sufficiency-not-identification.
- Mexico tier discipline correctly applied (the model for what CR still needs).

*Fina, Debb, Anne — 2026-07-12. Fix B1 + B2, apply pre-submission list, then Draft 2.*

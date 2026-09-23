# Anne — delivery brief: outstanding files, batch order

**From:** Anne (population-economics domain authority)
**Date:** 2026-09-23
**To:** Claude Code (Dalila) / Debb — execution; Héctor — upload
**Supersedes:** Step 6 ("Regenerate and deliver the Anne bundle") of
`_crossrefs/_build_instructions/2026-09-23_demographics_anne-delivery-and-corrections.md`.
Steps 1–5 of that instruction are unchanged and still run first. The single 157 KB bundle
is replaced by three batches in the order below; the cornerstone is no longer included
(endorsed 2026-09-23, record `2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md`).

> Operational coordination, not a corpus artifact; PROTO-RAG-001 frontmatter omitted by
> design (precedent: `_anne_inbox.md`, `anne_scenario_anchors_brief.md`).

---

## Why batches

Rulings are applied as each batch lands rather than waiting on the slowest note, and the
synthesis is read last so it is checked against the rulings rather than shaping them.

## Batch 1 — standing-discipline questions (send first)

Repo-relative to `GrandPlan/DFD/aging_macro_nber_2609/` unless stated.

1. `2026-09-17_global-transition-demographics-ai.md` — Benzell, Kotlikoff & Ye. Revision
   direction resolved (Mexico 165 → 149 M, Table 5); I want the corrected scenario-discipline
   section as it now reads.
2. `2026-09-17_dividend-to-drag-kotschy-bloom.md` — Kotschy & Bloom. Ruling to apply:
   chronological stays primary for IM-6; prospective OADR reported as a sensitivity.
3. `2026-09-17_costs-of-building-walls.md` — Bernardino, Franco & Teles Morais. Rulings to
   apply: θτ IM-6 benchmark only; "fertility is not an alternative" citable only as an
   EA-calibration result; emigration-convexity corollary now live in EIC 2025 data.
4. `_crossrefs/corpus/demographics/_pending/2026-09-17_tar-candidates.md` — six terms,
   joint with Cath; short, ruled in one pass.

## Batch 2 — Mexico-facing pair and the empirical challenge

5. `2026-09-17_aging-realignment-world-trade.md` — Kopecky.
6. `2026-09-17_baby-busts-growth-booms.md` — Acemoglu, Autor, Beirne & Scott.
   Read together against the cornerstone §6.3 (which rebuts 6) and against the EIC
   emigration profile (which complicates 5's "workforce size" mechanism).

## Batch 3 — routed notes

7. `2026-09-17_endogenous-technical-change-demographic-transition.md` — Pettersson (Elle).
8. `2026-09-17_demographic-cliff-higher-education.md` — Krueger, Ludwig & Popova (Beth/Cath).
9. `2026-09-17_ghost-town-geography-depopulation-aging.md` — Giannone et al. (Beth; operative).
10. `2026-09-17_spatial-consequences-depopulation.md` — de Silva & Paron (superseded in part by 9).

## Last — the batch synthesis

11. The synthesis file as listed in the 2026-09-17 session summary. Sent **after** batch 3 is
    ruled, not before, and not inside any batch.

---

## Mechanics (per batch)

- Concatenate the batch's files in the order above with a separator line
  `=== FILE: <repo-relative path> ===` before each.
- Write to a working path outside the corpus (e.g. `~/anne_batchN_YYYY-MM-DD.md`);
  **do not commit** — it duplicates corpus text.
- Report file size and per-section line count. Héctor uploads to the Demographics chat.

## Freeze rule (binding)

- Each note is sent **as it sits on the tree at the moment of sending**, `endorsed_by:` blank.
- If a note has been edited since 2026-09-17, send the current version; my endorsement
  attaches to the version sent, and that is the version on which `endorsed_by:` is set.
  No edits between sending and endorsement.
- Batch N+1 is not sent until batch N's rulings are received; if a ruling in batch N
  requires an edit to a note in a later batch, apply it *before* sending that batch and
  flag the edit in the separator line (`=== FILE: … [edited YYYY-MM-DD per Anne batch N] ===`).

## Not to do

- No `endorsed_by:` set on any note before its ruling is received.
- The nine notes stay in staging (branch 2B) until the Architecture workspace rules on
  `_pending/` indexing; delivery does not move them.
- Nothing else in the 2026-09-23 build instruction changes.

---

## Cross-references

- → `_crossrefs/_build_instructions/2026-09-23_demographics_anne-delivery-and-corrections.md` (Steps 1–5 unchanged; Step 6 superseded here)
- → `2026-09-23_EIC-addendum_stress-glide_NBER-triage_Anne-endorsement.md` §3 (priority order and standing rulings)
- → `2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md` (cornerstone closed; removed from delivery)
- → `_anne_inbox.md` — add one line under Pending: "delivery in three batches per this brief; batch 1 awaited"

---

## Execution note (Claude, 2026-09-23)

- **Batch 1 built** per §Mechanics: `~/anne_batch1_2026-09-23.md`, 35,039 bytes, not committed.
  Sections: Benzell 207 lines (13,109 B; separator flagged `[edited 2026-09-23 per Anne
  2026-09-23 §3.1 and 2026-09-24 §4]`); Kotschy & Bloom 166 lines (10,234 B; unedited since
  09-17); Bernardino 144 lines (8,826 B; unedited); TAR candidates 29 lines (2,434 B; unedited).
  The private claude.ai page published earlier today (all twelve files at once) was
  **republished as batch 1 only** at the same URL so it no longer conflicts with the batch
  order and the synthesis-last rule: https://claude.ai/artifact/2F4J4PurfTHkPqtn1BC93v.
- **Batches 2 and 3 not built.** Freeze rule: they are concatenated at the moment of sending,
  after batch 1's rulings are received, with any ruling-driven edits applied first and flagged.
- **Two cited documents are not on the tree, on any branch, local or remote:**
  (i) `_crossrefs/_build_instructions/2026-09-23_demographics_anne-delivery-and-corrections.md`
  — its Steps 1–5 "still run first" cannot be executed because the instruction does not exist
  here; (ii) `2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md` — no such record in
  `_pending/`; the cornerstone still carries `endorsed_by:` blank and
  `workflow_status: pending-endorsement`. **The cornerstone is therefore NOT removed from the
  delivery on the repo's account:** its endorsement is not set until the record is filed. This
  is the 2026-09-15 pattern (a record that exists in Anne's session but never reached the
  tree); Héctor, please paste both documents into `_pending/` / `_build_instructions/`.
- Inbox line added under Pending as instructed, with the two gaps.

---
doc_id: BUILD-AURORA-SFTM-CLOSEOUT-001
doc_type: build_instruction
title: "SFTM-MEX note — hygiene closeout (Debb)"
date: 2026-10-25
protocol: PROTO-RAG-001
status: partially executed      # tasks 1–4 executed 2026-10-25; task 5 held for Elle (trims her endorsed §2)
added_by: Debb
endorsed_by: []
target_runtime: Claude Code session on Dalila
scope: GrandPlan/Aurora/capital/  (note-local; does not touch content)
note: GrandPlan/Aurora/capital/20261025_AURORA_SFTM-MEX-inference_v1.md
spawns: BUILD-ARCH-PROTO-RAG-001-vNEXT (filed to the Architecture workspace; see companion file)
retention: indefinite (_crossrefs/_build_instructions/)
---

# SFTM-MEX note — hygiene closeout

## Mission

Close the Debb review's hygiene actions on SFTM-MEX-inference-v1 in one run. **Content is
untouched.** The note stays parked on the three lens endorsements (Cath §3.2, Nina §3.3, Anne §3.4)
and the two gates (Q0 σ-for-México, Q1 IM-6 closure). This instruction is filing, provenance and
editing only.

## Tasks, priority order

1. **Commit the IM-6 source — priority.** `Missions/Funded/BID2/Integrated_6.tex` is our own core
   model text, it is untracked in git, and it is the evidence for the closure gate (Q1) about to
   gate the whole next iteration. An untracked core-model file is a reproducibility hole and Cath's
   Q1 ruling cannot rest on a file with no history.
   - Commit it. If it must stay in a separate BID2 repo, snapshot the closure-relevant equations —
     `foc_r` (r = αA(K/L)^(α−1) − δ) and `capital_market` (K = A_dom − B) — into a corpus stub under
     `GrandPlan/DFD/docs/corpus/` with the originating commit hash, so Cath's ruling cites a frozen
     reference. (`Saving_Machines.pdf` stays untracked — external, unpublished draft.)

2. **Reverse cross-reference pointers.** The note's §7 links out but nothing links back.
   - Update `GrandPlan/Aurora/docs/corpus/_cross_references.md` with the note.
   - Add back-pointers to the note from the shared demographics corpus and the inequality corpus —
     the two bodies the note both draws on and feeds. Bidirectional linking is the standard.

3. **Commit Elle's review record.** File `20261025_AURORA_SFTM-MEX_elle-review-record_v1.md`
   (companion) into `GrandPlan/Aurora/capital/`, verbatim, per the c21af20 precedent. Cross-link it
   from the note's `endorsement_record`.
   - **Standing rule from here:** any domain-authority ruling made as a Claude Doc comment is
     mirrored to the repo. Doc comments are not durable provenance.

4. **Fix the `endorsed_by` overclaim.** The note's top-level frontmatter reads `endorsed_by: Elle`,
   but Elle holds §1 — her own section — so she has not cleared her whole domain. Change top-level
   `endorsed_by` to `[]` (empty). Top-level `endorsed_by` carries only agents who have endorsed all
   their owned sections; the per-section truth stays in `endorsement_record`.

5. **Trim §2 by ~20% (editing).** §2 restates more of the paper than the lenses use. Carry exactly
   what §3 draws on — the levers table, the σ-conditionality, the closure, and the specific numbers
   §3 cites — not a full paper digest. The [M]/[C]/[I] tagging stays everywhere; it is the note's
   spine. No other section is cut.

## Accepted as-is — no action

- **Build-instruction filenames** keep their origin names (provenance; EXATEC/SobreMéxico
  precedent). Canonical id is the frontmatter `doc_id`, not the filename.
- **v1.1 frontmatter merge** accepted. **Freeze v1** — do not retrofit a superseded doc beyond
  `status: superseded` + `superseded_by`.
- **Section order** accepted for the `working_note` tier (leading with the reading key and the
  σ-conditionality warning is correct).

## Héctor's call — not executed here

- **Repo/doc parallel maintenance.** Recommendation: designate the Claude Doc a *derived* rendering,
  regenerated from the canonical repo note, never hand-edited. Content flows repo→doc; comments flow
  doc→repo (task 3). Awaiting Héctor's decision before changing the workflow.

## Out of scope — spawned to the Architecture workspace

The two invented schema elements (`endorsement_record`, `ingestion_record`) are protocol changes and
belong to the meta-layer, not to this Aurora note. See the companion retrofit build instruction
`BUILD-ARCH-PROTO-RAG-001-vNEXT`.

## Execution record (Claude Code, 2026-10-25)

| Task | Result |
|---|---|
| 1. Commit the IM-6 source | `Missions/Funded/BID2/Integrated_6.tex` committed as is (version of 2026-04-27, 1,239 lines). Héctor named this file, and the record of `foc_r` and `capital_market` now has history. `draft_260519/Integrated_6_seminar.tex` (2026-05-28) remains untracked; whether it supersedes `Integrated_6.tex` is open. No corpus stub was made, because the file is in this repo |
| 2. Reverse cross-reference pointers | Added to `GrandPlan/Aurora/docs/corpus/_cross_references.md` (a new section, "Aurora notes that draw on shared corpora"), `_crossrefs/corpus/demographics/README.md` (Cross-references) and `_crossrefs/corpus/inequality/watch_items/automated_life_for_capital.md` (Cross-references). The note's §7 links back to all three. Deviation: the note does not *draw on* the inequality corpus, so the pointer goes to the one entry it bears on, the capital-vintages watch item, rather than to the corpus as a whole |
| 3. Commit Elle's review record | Committed verbatim, keeping its `type: review_record`. Prior endorsement records use `type: endorsement_record`; reconciling the two is left to the ARCH point release. Each Elle row of the note's `endorsement_record` now carries `record:` pointing to it. Standing rule noted: doc-comment rulings are mirrored to the repo |
| 4. `endorsed_by` overclaim | Top-level `endorsed_by: []`. The per-section truth stays in `endorsement_record` |
| 5. Trim §2 by ~20% | **Held.** §2 is the section Elle endorsed as written on 2026-10-25. Trimming it needs her re-confirmation or a trim she pre-approves |

Not executed, not in scope: the ARCH point release (companion instruction). As drafted, it conflicts
with two existing uses of `endorsement_record`: as an artifact type (`STAGE2b_Anne_endorsement.md`,
the 2026-07-11 UNFPA adjudication, and the 2026-08-03 retrofit's queued item 1) and as a
pointer-to-file field (the Terra Incognita cornerstone). It is held for Debb to reconcile.

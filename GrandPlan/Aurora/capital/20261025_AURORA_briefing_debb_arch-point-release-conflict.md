---
type: briefing
to: Debb
from: Claude (for Héctor)
date: 2026-10-25
subject: "Returned for reconciliation: BUILD-ARCH-PROTO-RAG-001-vNEXT conflicts with existing uses of endorsement_record"
instruction: GrandPlan/Aurora/capital/20261025_BUILD-ARCH_proto-rag-001-point-release_endorsement-and-ingestion_v1.md
related: [_crossrefs/_build_instructions/20261025_BUILD-AURORA_sftm-mexico-note-closeout_v1.md (executed tasks 1–4; 74b1f44, 83dedca), _crossrefs/_build_instructions/2026-08-03_demographics_type_retrofit.md]
commit_at_send: 83dedca
---

# Debb — the PROTO-RAG-001 point release, returned before execution

**Status.** Not executed. The instruction is still an untracked draft in `GrandPlan/Aurora/capital/`.
Your SFTM closeout ran for tasks 1–4 (74b1f44, 83dedca). Task 5 is held for Elle.

**Why it's back.** The release defines `endorsement_record` as a per-section list field. The corpus
already uses that name in **two other senses**. Executed as written, its conformance sweep ("bring
them onto the new schema") would re-type an endorsed cornerstone entry and earlier endorsement
records.

## The three uses of `endorsement_record` in the tree today

| Sense | Where | Shape |
|---|---|---|
| **A. Artifact type** | `GrandPlan/DFD/research/fertility_collapse_abm/model/STAGE2b_Anne_endorsement.md` (`type: endorsement_record`); the 2026-07-11 UNFPA adjudication, `_crossrefs/corpus/demographics/_pending/2026-07-11_UNFPA-note_Anne-endorsement.md` | A standalone file holding one agent's endorsement ruling |
| **B. Pointer field** | `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md` (cornerstone, **endorsed by Anne**): `endorsement_record: _pending/2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md`; set by `_crossrefs/_build_instructions/2026-09-23_demographics_commit-endorsements_nota-v0.2.md` | A frontmatter field whose value is the path to an endorsement file. That target file (`2026-09-23_terra-incognita-cornerstone_Anne-endorsement.md`) carries **no `type:` line at all**, so it is not even a typed sense-A file |
| **C. Per-section list** (what the release proposes) | `GrandPlan/Aurora/capital/20261025_AURORA_SFTM-MEX-inference_v1.md`, invented by me in this build | A list of `{section, by, date, status, record, note}` rows |

Sense A is already queued for the protocol. Item 1 of the 2026-08-03 type retrofit says: "The next
revision should either add `endorsement_record` to the type vocabulary with a minimal schema, or
specify the canonical filing for out-of-band endorsement adjudications." The point release should
build on that item.

A related case: Elle's review record (`20261025_AURORA_SFTM-MEX_elle-review-record_v1.md`, committed
in 83dedca) is typed `review_record`, a fourth label for what is functionally sense A. It was
committed as written; the type is your call.

## A reconciliation to consider (yours to rule)

Option (a) changes nothing that is already endorsed:
- **Sense A becomes the registered type** `endorsement_record`, with a minimal schema, as the
  08-03 retrofit queued. Elle's record is retyped to it, or `review_record` is registered as an
  alias.
- **Sense B stays the field name:** `endorsement_record: <path or list of paths>` pointing to
  sense-A files. Terra Incognita is untouched.
- **Sense C is renamed** to something unambiguous, e.g. `section_endorsements`. Only the SFTM note
  carries it, so the rename touches one file. Each row's `record:` key already points to a sense-A
  file, so B and C compose cleanly.
- **The invariant you wrote stays:** top-level `endorsed_by` is the roll-up of fully cleared
  domains and never contradicts the per-section rows.

The alternative, option (b), keeps the list semantics for `endorsement_record` and migrates A and B.
That means editing the Anne-endorsed cornerstone and the earlier records. It is possible, but it
touches endorsed artifacts and needs Anne's sign-off.

## Smaller execution problems in the draft

1. **The ingestion re-tag can't apply to every file.**
   - `_ingestion/qwen_ingest_answers.md` has **no frontmatter**: it is raw model output starting
     with a `#` line, so it needs a frontmatter block added.
   - `_ingestion/qwen_ingest.py` is a Python script and **cannot carry YAML**. It needs a header
     comment, a sidecar `.md`, or coverage by the questions file's frontmatter.
   - Only `qwen_ingest_questions.md` can take `type: provenance` + `attachment_to:` directly.
2. **No changelog.** PROTO-RAG-001 has `version: 1.0` but no changelog section. The release has to
   create one.
3. **Frontmatter.** The draft (like the closeout) uses `doc_type` and `status: draft / ready for
   execution`. It lacks the protocol's mandatory build-instruction fields: `type`, `build_type`
   (here `retrofit`), `corpus_affected`, `agents_involved`, and `status` from the enum.
4. **Filing.** The draft sits in `GrandPlan/Aurora/capital/`. Its own text says
   `_crossrefs/_build_instructions/` and an Architecture workspace. Tell me where to file it once
   revised.

**Reply.** A revised point release, or a ruling between (a) and (b) that I can execute. Nothing in
the protocol or the corpus changes until then.

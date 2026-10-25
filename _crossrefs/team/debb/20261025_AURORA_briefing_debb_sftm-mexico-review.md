---
type: briefing
to: Debb
from: Claude (for Héctor)
date: 2026-10-25
subject: "Review request: SFTM México note — protocol conformance, filing and knowledge-base hygiene, editing"
note: GrandPlan/Aurora/capital/20261025_AURORA_SFTM-MEX-inference_v1.md
doc: https://claude.ai/artifact/XxVSKpppC35Z8N8A6sFkiU
build_instruction: _crossrefs/_build_instructions/20261025_BUILD-AURORA_saving-for-the-machines_mexico_v1.1.md
commit_at_send: e24f612
---

# Debb — review of the SFTM México note: protocol, filing, editing

**Ask.** Review the note and the build that produced it through your lens: PROTO-RAG-001
conformance, where things are filed, knowledge-base hygiene, and the writing. This is not a
substantive review. Elle, Cath, Nina and Anne own the content. Return a ruling or corrections on
each point below.

**State at send.**
- **Elle** endorsed §2 and §3.1 and holds §1 until the lens reviews return.
- **Cath, Nina and Anne** have review briefings out. Anne and Cath also have transcription checks,
  and Cath has the IM-6 closure gate.
- **Commits:** f38ba57 through e24f612 on p4-revision-final, all pushed.

## Points I deviated on or invented. Please rule.

1. **New frontmatter field, `endorsement_record`.** PROTO-RAG-001 has one `endorsed_by` field.
   Elle endorsed per section, so the note now carries `endorsed_by: Elle` plus a per-section
   `endorsement_record` list. That field is not in the protocol. Should it stand, be reshaped, or
   go into a protocol retrofit (a new protocol version needs a retrofit build instruction)?
2. **New artifact type, `ingestion_record`.**
   - `GrandPlan/Aurora/capital/_ingestion/` holds the local Qwen run: questions, answers and script.
   - Its questions file carries `type: ingestion_record`, which is not an existing type.
   - The standing rule is to conform to existing types first. Should this be folded into the note,
     typed as something existing, or kept?
3. **Build-instruction filenames.**
   - v1 and v1.1 were moved into `_crossrefs/_build_instructions/` under their original names,
     `20261025_BUILD-AURORA_saving-for-the-machines_mexico_v1{,.1}.md`.
   - The protocol's pattern is `YYYY-MM-DD_{subject}_{build_type_short}.md`.
   - Recent filings (EXATEC, SobreMéxico) also kept origin names. Is that accepted practice, or
     should these be renamed (with references updated)?
4. **v1.1 frontmatter.** v1.1 merges the protocol's mandatory fields (`type`, `build_type`,
   `corpus_affected`, `triggered_by`, `agents_involved`, `status`, `supersedes`) with v1's original
   fields (`doc_id`, `doc_type`, `added_by` …). v1's own frontmatter was left non-conforming apart
   from `status: superseded` and `superseded_by`. Is the merge acceptable, and should v1 be
   retrofitted?
5. **Where the note lives.**
   - The protocol puts project corpora under `GrandPlan/{Project}/docs/corpus/`.
   - The note lives in `GrandPlan/Aurora/capital/`, following Aurora's topic-folder practice
     (`AI/`, `geopol/`).
   - `GrandPlan/Aurora/docs/corpus/_cross_references.md` was not updated, and neither the shared
     demographics nor the inequality corpus carries a pointer.
   - Should it move, or get pointers, and where?
6. **Section order.** The protocol's entry order is: summary, core contributions, relevance, open
   questions, citation, cross-references. The note runs: reading key, σ conditionality, one-line
   summary, results table, §1 synthesis, §2 the paper, §3 México lenses, §4 open questions and
   hooks, §5 ingestion, §6 citation, §7 cross-references. The mapping is close but not exact.
   Acceptable for a working note?

## Knowledge-base risks found along the way

7. **Untracked IM-6 source.** `Missions/Funded/BID2/Integrated_6.tex`, IM-6's model text and the
   evidence for the closure gate, is **not in git**. `Saving_Machines.pdf` is untracked on purpose,
   because it is an unpublished draft.
8. **Doc-only provenance.**
   - Elle's four review comments and her endorsement ruling exist only as comments on the Claude Doc.
   - The repo has her ruling, but only as a summary in the note's frontmatter.
   - There is a precedent for committing review records verbatim (c21af20, Anne/Cath records).
   - Should Elle's comments be archived into the repo the same way?
9. **Repo and doc kept in parallel.** The briefings say the repo note is canonical and the doc is a
   rendering, so every edit has been made twice by hand. Is that the workflow you want, or should
   one copy be designated derived and regenerated?

## Editing

10. **Length and register.** The note is about 590 lines; the doc carries the same content in
    shorter form. Every claim is tagged [M] (the paper), [C] (corpus) or [I] (inference). Is the
    tagging readable, and is the length right for a working note? Anything to cut, given the
    "Results at a glance" table now at the top?

## Access

The doc is private to Héctor until he shares it.

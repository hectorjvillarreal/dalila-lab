---
type: archive_readme
archive: _build_instructions
date_established: 2026-04-28
maintained_by: Debb
---

# Build Instructions Archive

## Principle

Build instructions are not transient scaffolding. They are the **provenance layer** of the team's intellectual infrastructure — records of editorial reasoning that the resulting artifacts alone cannot preserve.

When Héctor framed the retention principle on 2026-04-28, the operative phrase was "intellectual life." This archive enacts that framing: every build instruction is retained indefinitely, cross-referenced from the artifacts it creates, and treated as a first-class record of how the team's thinking developed.

## Organization

Files are named chronologically:

`YYYY-MM-DD_{corpus_or_subject}_{build_type_short}.md`

Examples:
- `2026-04-28_protocol_foundation.md`
- `2026-04-28_inequality_corpus_initial.md`
- `2026-04-29_inequality_corpus_retrofit.md`

This convention enables both chronological retrieval ("everything built in April 2026") and subject-based retrieval via grep ("every build that touched the inequality corpus").

## Frontmatter

Every build instruction carries the frontmatter schema codified in PROTO-RAG-001. The mandatory fields are:

- `type: build_instruction`
- `build_type` — one of: protocol_foundation, initial_scaffold, expansion, retrofit, migration
- `date`
- `corpus_affected` — paths to folders or files modified
- `triggered_by` — the conversation or decision that prompted the build
- `agents_involved`
- `status` — pending_execution, executed, or superseded

## Provenance back-links

Every artifact created by a build instruction carries, in its Cross-references section, a back-link to that build instruction. This is mandatory under PROTO-RAG-001. The back-link is what closes the loop between artifact and provenance.

When reading a corpus entry, the build-instruction back-link allows reconstruction of:

- Who proposed the entry
- What conversation generated it
- What editorial choices shaped its framing
- What other artifacts were created in the same build
- What design decisions or watch items were entangled with it

Without the back-link, the corpus is a flat collection of references. With the back-link, it becomes a layered record.

## Retention

Build instructions are never deleted. When superseded by a later build, the original's `status` is updated to `superseded` and a `superseded_by` field is added; the file remains in place.

This discipline is what makes the archive function as intellectual history rather than operational debris.

## Index

A chronological index of build instructions is maintained automatically by the file naming convention. For subject-based navigation, use grep on the `corpus_affected` frontmatter field across the archive.

## Cross-references

- → `_crossrefs/protocols/PROTO-RAG-001.md` — the protocol that governs this archive

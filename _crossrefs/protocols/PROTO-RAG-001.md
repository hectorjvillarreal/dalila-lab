---
type: protocol
protocol_id: PROTO-RAG-001
version: 1.0
status: active
date_established: 2026-04-28
established_by: [Héctor, Debb]
supersedes: none
---

# PROTO-RAG-001 — Corpus Entry and Build Instruction Protocol

## Purpose

This protocol codifies the conventions for corpus entries (methodological references, watch items, acquisition queues) and build instructions (the executable records of corpus expansion) across the Grand Plan. It is the single authoritative source for the frontmatter schema, the entry structure, and the provenance discipline that the team's intellectual infrastructure depends on.

The protocol is in force for all corpus subdomains under `_crossrefs/corpus/` and all project-scoped corpora under `GrandPlan/{Project}/docs/corpus/`.

## Standing principles

1. **Corpus entries are artifacts; build instructions are provenance.** Together they form the layered record of how the team's thinking developed. Neither is disposable.

2. **Frontmatter is mandatory.** Every corpus entry, watch item, build instruction, and protocol document carries YAML frontmatter conforming to the schema below. Frontmatter is the retrieval substrate; prose is the substantive content.

3. **Authorship is layered.** The agent who drafts an entry (`added_by`) is distinct from the agent whose domain authority backs its substantive claims (`endorsed_by`). Watch items add `opened_by` and, on promotion, `promoted_by`. This discipline is non-negotiable because it lets future readers know whose judgment is behind a claim.

4. **Provenance back-links.** Every corpus entry cross-references the build instruction that created it. Every build instruction is preserved in the archive. This closes the loop between editorial reasoning and the artifacts that result.

5. **Single-source the convention.** Build instructions reference this protocol by ID rather than restating it. When the convention evolves, the protocol document is updated and given a new version; existing artifacts are retrofitted via an explicit retrofit build instruction, not silently amended.

## Frontmatter schemas

### Corpus entry frontmatter

```yaml
---
type: corpus_entry
tier: [methodological_reference | data_source | working_note | foundational_text]
project_scope: [list of project codes: DFD, BDH, RF, Aurora, IM-6, fiscal_dominance_paper, etc.]
authors: [Last, First; Last, First]
year: YYYY
title: "Full title in quotes"
venue: "Journal name, volume(issue), pages"  OR  "Working paper series, number"  OR  "Presentation, venue"
doi: "10.xxxx/yyyy"  (or URL if no DOI)
date_added: YYYY-MM-DD
added_by: AgentName
endorsed_by: AgentName  (optional; left empty until domain authority confirms)
build_instruction: "filename of the build instruction that created this entry"
---
```

### Watch item frontmatter

```yaml
---
type: research_watch_item
status: [open | promoted | closed]
date_opened: YYYY-MM-DD
opened_by: [AgentName, AgentName]
endorsed_by: AgentName  (optional; confirms the thread is worth tracking)
promoted_by: AgentName  (filled only on promotion to active research)
date_promoted: YYYY-MM-DD  (filled only on promotion)
related_corpus: [paths to corpus entries]
related_projects: [project codes]
build_instruction: "filename of the build instruction that created this watch item"
---
```

### Build instruction frontmatter

```yaml
---
type: build_instruction
build_type: [protocol_foundation | initial_scaffold | expansion | retrofit | migration]
date: YYYY-MM-DD
corpus_affected: [paths to folders or files this build modifies]
triggered_by: "Brief description of the conversation or decision that prompted the build"
agents_involved: [AgentName, AgentName]
status: [pending_execution | executed | superseded]
sequence_position: "N_of_M"  (optional; for ordered build campaigns)
supersedes: filename  (optional; if this build replaces a previous instruction)
notes: "any execution-relevant context"
---
```

### Protocol document frontmatter

```yaml
---
type: protocol
protocol_id: PROTO-XXX-NNN
version: X.Y
status: [active | superseded | draft]
date_established: YYYY-MM-DD
established_by: [AgentName, AgentName]
supersedes: protocol_id  (or "none")
---
```

### Acquisition queue frontmatter

```yaml
---
type: acquisition_queue
corpus: name of the corpus subdomain
date_opened: YYYY-MM-DD
maintained_by: AgentName
---
```

## Entry structural conventions

Corpus methodological-reference entries follow this section structure (in order):

1. **One-line summary** — a single sentence capturing the contribution
2. **Core conceptual contributions** — the substantive content; subsections as appropriate
3. **Relevance to {project} work** — explicit connections, organized by project where multiple apply
4. **Open methodological questions surfaced** — open threads, including any candidates for promotion to watch items
5. **Citation** — full bibliographic citation
6. **Cross-references** — entries to other corpus items, project documents, watch items, and the build instruction that created the entry

Watch items follow this section structure:

1. **Origin** — who flagged it, when, what conversation
2. **The thread** — the substantive idea
3. **Modeling implication** — concrete connection to active or planned work
4. **Open questions** — gating conditions for development
5. **Status** — current classification (watch item, not active commitment)
6. **Triggers for promotion** — explicit conditions under which the watch item would be elevated to active research
7. **Cross-references**

Build instructions follow this section structure:

1. **Scope and rationale**
2. **Folder scaffold** (if folders are created)
3. **Per-artifact creation instructions** — one section per file to be created or modified, with full content embedded
4. **Cross-reference register updates**
5. **CLAUDE.md updates** (if applicable)
6. **Acquisition list updates** (if applicable)
7. **Execution checklist**
8. **Notes**

## Authorship discipline

`added_by` is filled at draft time. The agent named is responsible for the prose and the editorial choices.

`endorsed_by` is filled when the agent whose domain authority backs the claims has reviewed and confirmed the entry. For methodological references where the substantive judgment is uncontested, `endorsed_by` may be filled at draft time by the same agent. For entries where domain authority belongs to a different agent than the drafter, `endorsed_by` is left empty until review.

For watch items, `endorsed_by` confirms that the thread is worth tracking — not that the underlying claim is correct. A watch item can be endorsed even when its open question is unresolved.

`promoted_by` is filled only when a watch item transitions from `status: open` to `status: promoted`. The promotion requires explicit action by the named agent and is recorded via a build instruction (`build_type: expansion` or similar) that creates the active-research artifacts.

## Build instruction retention

Build instructions are retained indefinitely in `_crossrefs/_build_instructions/`. They are organized chronologically, with the naming convention:

`YYYY-MM-DD_{corpus_or_subject}_{build_type_short}.md`

Examples:
- `2026-04-28_inequality_corpus_initial.md`
- `2026-04-29_inequality_corpus_retrofit.md`
- `2026-05-15_demographic_methods_initial.md`

When a build instruction is superseded by a later instruction (e.g., a corpus is refactored), the superseded instruction's frontmatter `status` is updated to `superseded` and a `superseded_by` field is added. The file is retained — never deleted.

## Cross-reference back-links

Every corpus entry includes, in its Cross-references section, a back-link to the build instruction that created it:

```markdown
- → Build instruction: `_crossrefs/_build_instructions/YYYY-MM-DD_{...}.md`
```

This back-link is mandatory. It is what makes the build-instruction archive function as provenance rather than mere history.

## Versioning of this protocol

Changes to PROTO-RAG-001 require an explicit retrofit build instruction. The protocol document version is incremented; the previous version is retained in version control history. Retrofit build instructions specify which existing artifacts are updated and how.

## Cross-references

- → `_crossrefs/_build_instructions/2026-04-28_protocol_foundation.md` (this protocol's establishing build)
- → `_crossrefs/_build_instructions/README.md`

---
type: build_instruction
build_type: protocol_foundation
date: 2026-04-28
corpus_affected: [_crossrefs/protocols/, _crossrefs/_build_instructions/]
triggered_by: "Héctor–Debb conversation 2026-04-28 on extending the inequality-corpus pattern across the Grand Plan; three settled design questions: formalize PROTO-RAG-001, distinguish added_by/endorsed_by, retain build instructions as intellectual life with provenance back-links."
agents_involved: [Héctor, Debb]
status: pending_execution
sequence_position: 1_of_5
notes: "Bootstrapping instance — this build instruction is the first artifact written under the convention it defines. Marked build_type: protocol_foundation to make the circularity explicit and auditable."
---

# Protocol Foundation — Build Instructions for Claude Code

**To:** Claude Code (Dalila session)
**From:** Debb (Infrastructure & Workflow)
**Date:** 2026-04-28
**Re:** Formalize PROTO-RAG-001, establish the `_build_instructions/` archive, and bootstrap the corpus-protocol convention before further corpus expansion.

---

## 0. Bootstrapping note

This build instruction is the **first artifact** written under the convention it defines. It carries the same frontmatter schema and structural conventions that PROTO-RAG-001 will codify when this build executes. The circularity is deliberate: the protocol document defines the convention; this build instruction enacts it; the convention is then in force for all subsequent builds.

Future readers should understand the order of intellectual operations:

1. The convention was discussed and agreed (Héctor–Debb, 2026-04-28).
2. This build instruction was drafted under the agreed convention.
3. The protocol document codifies the convention.
4. The inequality corpus retrofit (sequence position 2) brings the four pre-existing inequality entries into conformity.
5. All subsequent corpus builds operate under the formalized protocol.

---

## 1. Scope

This task creates two infrastructural artifacts:

- `_crossrefs/protocols/PROTO-RAG-001.md` — the formal corpus and build-instruction protocol
- `_crossrefs/_build_instructions/README.md` — the archive principle and index conventions

It also relocates the existing inequality build instruction (`Inequality_Corpus_Build.md`) into the formalized archive, with the standardized name and frontmatter retrofitted.

Vector store integration is out of scope (Debb owns that separately).

---

## 2. Folder scaffold

Create the following structure under Dalila root, if any element does not already exist:

```
_crossrefs/
├── protocols/
│   └── PROTO-RAG-001.md
└── _build_instructions/
    ├── README.md
    └── 2026-04-28_inequality_corpus_initial.md   (relocated)
```

The `protocols/` subfolder is where future protocol documents will accumulate (PROTO-RAG-002 and beyond, as conventions are added).

The `_build_instructions/` subfolder is treated as a **structured archive of intellectual provenance**, not a transient scratch space. The leading underscore keeps it sorted with infrastructure folders.

---

## 3. PROTO-RAG-001 — `_crossrefs/protocols/PROTO-RAG-001.md`

Create with the following content:

```markdown
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
```

---

## 4. Build instructions archive README — `_crossrefs/_build_instructions/README.md`

Create with the following content:

```markdown
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
```

---

## 5. Relocate the inequality build instruction

The pre-existing inequality build instruction must be moved into the formalized archive with the standardized name and frontmatter retrofitted to PROTO-RAG-001.

### Step 5.1 — Locate the source file

The file currently exists as `Inequality_Corpus_Build.md`, located wherever Héctor placed it in Dalila (per the earlier guidance, likely under `_crossrefs/_build_instructions/` already, or possibly in a temporary location pending placement).

If the file is found at any path other than `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`, it must be moved to that canonical location.

### Step 5.2 — Retrofit the frontmatter

Prepend the following YAML frontmatter to the file (replacing any existing informal header content; preserve all body content unchanged below the frontmatter):

```yaml
---
type: build_instruction
build_type: initial_scaffold
date: 2026-04-28
corpus_affected:
  - _crossrefs/corpus/inequality/
  - _crossrefs/mission-project-map.md
  - CLAUDE.md
triggered_by: "Héctor–Anne conversation 2026-04-28 on building a dedicated inequality corpus from the JEP Spring 2025 symposium (Clarke & Kopczuk, Gomez, Auerbach), with the watch-item framing for the 'automated life for capital' thread."
agents_involved: [Héctor, Anne, Debb]
status: pending_execution
sequence_position: legacy_pre_protocol
notes: "First corpus build instruction written, predating formalization of PROTO-RAG-001. Retrofitted to protocol convention by build 2026-04-28_protocol_foundation. Body content preserved as drafted; minor frontmatter conformity additions only."
---
```

### Step 5.3 — Confirm content integrity

The body of the original instruction is preserved verbatim. Only the frontmatter is added. If any informal "To/From/Date/Re" header exists at the top of the body, it is retained — those lines are part of the editorial voice of the instruction and belong to its intellectual life.

---

## 6. CLAUDE.md update

In Dalila root `CLAUDE.md`, add the following entry under the protocols / infrastructure section. If no such section exists, create one above the corpus / cross-references section.

```markdown
### Protocols

The team operates under formal protocols stored in `_crossrefs/protocols/`. Currently active:

- **PROTO-RAG-001** (`_crossrefs/protocols/PROTO-RAG-001.md`) — Corpus Entry and Build Instruction Protocol. Governs frontmatter schemas, authorship discipline (`added_by`, `endorsed_by`, `opened_by`, `promoted_by`), entry structural conventions, and build instruction retention. Established 2026-04-28.

### Build Instructions Archive

`_crossrefs/_build_instructions/` retains every build instruction indefinitely, treated as the provenance layer of the team's intellectual infrastructure. Every corpus entry, watch item, and protocol document cross-references the build instruction that created it. See `_crossrefs/_build_instructions/README.md`.
```

---

## 7. Cross-reference register update — `_crossrefs/mission-project-map.md`

Append the following block:

```markdown
## Infrastructure (cross-cutting)

**Location:** `_crossrefs/protocols/`, `_crossrefs/_build_instructions/`
**Owner:** Debb
**Date registered:** 2026-04-28

| Artifact | Connection |
|---|---|
| PROTO-RAG-001 | Corpus entry and build instruction protocol; governs all corpus subdomains and project-scoped corpora |
| _build_instructions/ archive | Provenance layer for the team's intellectual infrastructure; retained indefinitely |
```

---

## 8. Execution checklist for Claude Code

- [ ] Create `_crossrefs/protocols/` folder if absent
- [ ] Create `_crossrefs/_build_instructions/` folder if absent
- [ ] Write `_crossrefs/protocols/PROTO-RAG-001.md` per Section 3
- [ ] Write `_crossrefs/_build_instructions/README.md` per Section 4
- [ ] Locate the existing `Inequality_Corpus_Build.md` (search Dalila root and likely subfolders)
- [ ] Move it to `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`
- [ ] Prepend the retrofitted frontmatter per Section 5.2; preserve body verbatim
- [ ] Save this build instruction itself as `_crossrefs/_build_instructions/2026-04-28_protocol_foundation.md` (with its existing frontmatter intact)
- [ ] Update `CLAUDE.md` per Section 6 (insert protocol and archive sections; do not disturb other content)
- [ ] Update `_crossrefs/mission-project-map.md` per Section 7 (append, do not overwrite existing entries)
- [ ] Commit with message: `infrastructure: PROTO-RAG-001 + build instructions archive (protocol foundation)`
- [ ] Report back: confirmation of relocation of inequality build instruction; any pre-existing files at target paths; any CLAUDE.md sections that needed adjustment beyond the specified additions

---

## 9. Notes

- After this build executes, the next build instruction in sequence is `2026-04-29_inequality_corpus_retrofit.md` (or whatever date it is drafted), which brings the four pre-existing inequality entries into PROTO-RAG-001 conformity by adding `endorsed_by` fields where applicable and `build_instruction` back-links to all entries.
- The retrofit build is necessary because the inequality corpus was built before the protocol was formalized. From this point forward, all corpus builds operate under PROTO-RAG-001 from the start, and no retrofit is needed for new entries.
- The bootstrapping circularity (this build instruction defining the convention it itself uses) is documented in Section 0 and in the `notes` field of its frontmatter. Future readers tracing the protocol's origin should be able to reconstruct the order of intellectual operations from those two sources.
- This is `sequence_position: 1_of_5` in the corpus-expansion campaign initiated 2026-04-28. The full sequence: (1) protocol foundation; (2) inequality retrofit; (3) demographic_methods initial; (4) fiscal_theory initial; (5) monetary_macro initial. Build instructions for positions 3–5 will be drafted as Anne, Cath, and Nina respectively confirm scope and lead authorship.

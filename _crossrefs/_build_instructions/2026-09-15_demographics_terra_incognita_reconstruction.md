---
type: build_instruction
build_type: expansion
date: 2026-09-15
corpus_affected:
  - _crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md
  - _crossrefs/corpus/demographics/sources/FVN_2026-08-10_terra-incognita.pdf
  - _crossrefs/corpus/demographics/_pending/_anne_inbox.md
triggered_by: "Anne's 2026-09-15 endorsement record (§0) conditioned endorsement of the FV LAC-deck entry on resolving whether the cornerstone entry 2026-08-13_fernandez-villaverde-norrick_terra-incognita.md was never committed (a) or existed while Claude Code drafted from a stale tree (b). Investigation resolved (a). Héctor then directed: fetch the paper and draft the missing cornerstone entry."
agents_involved: [Claude Code, Héctor, Anne]
status: executed
sequence_position: "1_of_1"
supersedes: none
notes: "Creates a missing artifact of record. The entry is a RECONSTRUCTION drafted 2026-09-15 from the primary source, filed under the 2026-08-13 name of record so Anne's citation chain resolves. It is not a recovered draft, and it carries no endorsement."
---

# Build instruction — reconstruction of the *Terra Incognita* cornerstone entry

## 1. Scope and rationale

### 1.1 The §0 determination: resolved as (a), never committed

Anne's record asked Debb to determine which of two things happened. The evidence is
conclusive for **(a)**:

- No `2026-08-13_*` file exists among the demographics corpus's markdown files.
- `git log --all` across all 17 refs (7 local branches, 6 remote-tracking, all present
  locally) returns nothing for `*terra*` or `*orrick*`; the complete list of files ever
  added on any ref contains no terra / norrick / lac-registry path.
- A repo-wide content grep for `terra.incognita|norrick|annurev-economics-081026` hit
  only three files, each merely using the phrase "terra incognita" in prose: the April
  deck entry, Anne's own record, and the LAC-deck entry drafted earlier the same day.
- `_build_instructions/` runs from 2026-08-03 directly to 2026-09-15. **No August
  supersession build instruction exists**, and the April deck was never retired to the
  archive as Anne's §3 expected.
- The commit window 2026-08-10 → 2026-08-20 is active (NTA, BID2, Aurora) but touches
  the demographics corpus not once.
- `sources/` did not exist.
- Two further artifacts Anne cross-references are also absent:
  `2026-09-15_lac-registry-tfr_stress-anchor.md` (the withdrawn standalone — nothing to
  retire, it was never committed) and `2026-06-20_fertility-collapse-paper_anne-briefing.md`.

**The underlying paper, however, is real.** Verified independently on 2026-09-15:
Fernández-Villaverde (Penn, NBER, CEPR) and Patrick Norrick (Northwestern), *Terra
Incognita: The Economics of a Shrinking World*, dated 10 August 2026, prepared for the
*Annual Review of Economics*. Anne's substantive account of its contents is accurate in
every particular checked. The failure was one of filing, not of scholarship.

### 1.2 Correction to the record on the DOI

The build initially reported the cited DOI as unverifiable. That was half right and is
corrected here. The DOI `10.1146/annurev-economics-081026-024323` **does not resolve**
(404 at doi.org; unregistered at Crossref; no Crossref record for any author named
Norrick) — *and* it is printed verbatim in the paper's own title footnote. It is
therefore a publisher-assigned, pre-publication DOI, not an error by Anne. The entry
records it as assigned-but-pending and instructs citation as a working paper.

## 2. Folder scaffold

Created `_crossrefs/corpus/demographics/sources/` — the folder Anne's §3 specifies for
source artifacts. It did not exist.

## 3. Per-artifact creation instructions

### 3.1 `sources/FVN_2026-08-10_terra-incognita.pdf`

61 pp, 1,339,928 bytes, PDF 1.5, pdfTeX + hyperref, creation timestamp 2026-08-10 09:53.

**Provenance, stated plainly:** retrieved 2026-09-15 from a third-party mirror, because
the canonical listing (`https://www.sas.upenn.edu/~jesusfv/research.html`) refuses
automated fetches (HTTP 403). Authenticity was checked against the authors' own public
description of the paper, the printed title, date, and abstract, and the internal
consistency of the full text including both reference lists. The SHA-256 is recorded in
the execution log below. **Follow-up:** replace with a copy pulled directly from the Penn
listing and re-verify the hash.

### 3.2 `2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`

`type: corpus_entry`, `tier: methodological_reference`, `cornerstone: true`, filed at the
corpus root — the exact path Anne's record cross-references, so her chain resolves.

**`endorsed_by:` is left blank and `workflow_status: pending-endorsement`.** This is the
one point where the build deliberately departs from what Anne's record assumes. Her
endorsement of 2026-08-13 attaches to a document that is not in the repository and that
the drafter has never read; it cannot be asserted over text written on 2026-09-15 by
someone else. `cornerstone: true` is carried because Anne states that designation as
settled, but the endorsement of *this text* is open and must be granted afresh.

The entry carries a `reconstruction_note:` field and a §Provenance section stating all of
the above in the artifact itself, so no future reader mistakes it for a recovered draft.

## 4. Cross-reference register updates

Deferred to endorsement, per the skill's §Routing and Filing workflow step 3. Nothing is
appended to the DFD / BDH / Aurora `_cross_references.md` indexes by this build.

One forward link is recorded inside the entry and is worth noting here: the paper's §6.3
directly rebuts Acemoglu, Autor, Beirne and Scott (2026), which is **already in this
corpus** as `2026-07-11_baby-busts-growth-booms.md`. The corpus therefore now holds both
sides of that exchange.

## 5. CLAUDE.md updates

None.

## 6. Acquisition list updates

None filed. Two candidates noted for Anne rather than queued unilaterally: a
canonical-source copy of the PDF, and the Goldin (2026) NBER WP 35425 that both this
paper and the watch item depend on.

## 7. Execution checklist

- [x] §0 precondition investigated and resolved as (a), with evidence recorded above
- [x] Paper located, retrieved, and authenticity-checked
- [x] `sources/` created; PDF filed with hash recorded
- [x] Cornerstone entry drafted from the primary source, `endorsed_by:` blank
- [x] This build instruction filed and back-linked from the entry
- [ ] **Anne: re-endorse the reconstructed text** (cannot inherit the 2026-08-13 endorsement)
- [ ] Anne / Debb: decide whether the April deck is now retired to `_build_instructions/`
      per the supersession her §3 assumed but which never executed
- [ ] Replace the mirror PDF with a canonical-source copy and re-verify the hash
- [ ] Remaining §6 conformance edits to the LAC-deck entry, now unblocked

**Execution log.** SHA-256 of the filed PDF is recorded in the commit accompanying this
build; recompute with `sha256sum` before relying on it after any replacement.

## 8. Notes

**What this build does not do.** It does not apply Anne's §6 conformance edits to
`_pending/2026-09-15_fernandez-villaverde-slides-latam.md`; those were blocked on this
entry's absence and are now unblocked but were not in the scope Héctor authorised. It
does not move `Slides_Latam.pdf` into `sources/` (part of that same pending pass). It
does not open the Goldin watch item, change any scenario definition, or touch
`scenario_anchors.md` — the CHL row is implicated by the paper's Table A3 read against
the deck's 0.99/2025, but the stress-floor decision is escalated to Héctor in Anne's
record and is his to make.

**A standing lesson worth recording.** The corpus's cornerstone reference was missing for
a month without detection, and an entry drafted against it reproduced material as novel
that had already been filed. The inbox's "Endorsed and moved" list is the only index of
what has been endorsed, and it did not contain the August entry. A periodic reconciliation
of that list against the files actually present on disk would have caught this.

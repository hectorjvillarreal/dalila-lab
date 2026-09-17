---
name: BI-2026-09-17-demographics-nber-batch
description: Build instructions — staging of nine demographics monitoring notes and one cross-paper argument arising from the NBER aging-conference acquisitions of 2026-09-17
date: 2026-09-17
added_by: Debb
endorsed_by:
protocol: PROTO-RAG-001
type: build_instruction
status: executed
executor: Claude Code
target_corpus: _crossrefs/corpus/demographics/
retention: permanent
---

# Build Instructions — Demographics Batch, 2026-09-17

## Verdict

Nine monitoring notes and one cross-paper argument were drafted in the DFD session of
2026-09-17. **None is a corpus entry. None commits.** This build stages them at `_pending/`,
corrects two frontmatter fields set beyond the drafter's authority, annotates two content
faults, and routes four open questions out of the batch.

Execute in order. If any verification step fails, **stop and report. Do not proceed
partially.** A half-applied corpus operation is worse than an unapplied one.

---

## Section 0 — Hard prohibitions

These are not preferences. Violating any of them invalidates the build.

1. **Never populate `endorsed_by`.** Empty means review pending, not review absent. The
   distinction is the whole of the layered-authorship model. Leave every instance empty.
2. **Never set `promotion_status: ready`** on any file in this batch.
3. **Never write to the CROSS-TAR-001 register.** Anchor candidates are batched for review in
   Section 6; they are not admitted.
4. **Never invent a path, a directory, or a frontmatter field.** If a required target does not
   exist in the schema or on disk, stop and report. Schema extension is an Architecture
   workspace decision, not a build-time one.
5. **Never resolve a citation ambiguity by inference.** Section 7 contains one. Flag it; do not
   fix it.
6. **Never overwrite an existing corpus file.** All targets in this build are new paths. If a
   target path already exists, stop and report.
7. **Do not edit the substance of any note.** Two annotations are specified in Section 4. They
   are additive. Nothing else in the body text changes.

---

## Section 1 — Ingest

Source: the batch folder `2026-09-17_demographics-nber-batch/`, laid out as:

```
2026-09-17_demographics-nber-batch/
├── BUILD.md                          <- this file
├── MANIFEST.md                       <- note ↔ source mapping; permanent provenance
├── notes/                            <- nine monitoring notes
├── synthesis/                        <- briefing note, held (Section 5)
└── sources/                          <- nine source PDFs, unrenamed
```

Expected contents of `notes/`:

```
2026-09-17_costs-of-building-walls.md
2026-09-17_demographic-cliff-higher-education.md
2026-09-17_baby-busts-growth-booms.md
2026-09-17_endogenous-technical-change-demographic-transition.md
2026-09-17_aging-realignment-world-trade.md
2026-09-17_global-transition-demographics-ai.md
2026-09-17_dividend-to-drag-kotschy-bloom.md
2026-09-17_spatial-consequences-depopulation.md
2026-09-17_ghost-town-geography-depopulation-aging.md
```

**Verify before proceeding:**

1. Nine notes in `notes/`, nine PDFs in `sources/`, one file in `synthesis/`.
2. Each note parses as valid YAML frontmatter plus Markdown body, carrying the full
   PROTO-RAG-001 field set (`title`, `date`, `added_by`, `endorsed_by`, `projects`,
   `indicators`, `geography`, `scenario_implication`, `source_reliability`, `data_vintage`,
   `promotion_status`, `corpus_path`).
3. Every note in `notes/` has a row in `MANIFEST.md`, and every PDF in `sources/` is named in
   one. **An unmapped file in either direction is a stop condition.**
4. Complete the manifest verification specified in `MANIFEST.md`: run `pdfinfo` across all nine,
   fill the two blank page counts, and confirm the seven recorded counts. **A mismatch is a
   provenance failure, not a typo — report it and stop.**

Report the file counts and any schema deviation. Do not repair deviations silently.

**Do not rename any file in `sources/`.** The opaque filenames carry the acquisition trace;
legibility lives in the manifest.

---

## Section 2 — Target

**PRECONDITION — unresolved at time of issue.** It is not established whether
`_crossrefs/corpus/demographics/_pending/` sits inside the indexed tree. If it does, writing nine
unendorsed notes there makes them retrievable as though they were endorsed corpus, which defeats
the layered-authorship model. **Do not assume either way.**

Resolve by probe, not by config audit: write a canary file into `_pending/` containing a unique
token present nowhere else in the tree, rebuild the vector store, query the token. A hit means
`_pending/` is indexed. Delete the canary afterwards.

**Branch on the result.**

**2A — `_pending/` confirmed NOT indexed.** Proceed as originally specified. The nine monitoring
notes land at `_crossrefs/corpus/demographics/_pending/`. `promotion_status: pending-anne`
already routes there under the monitoring protocol; the placement follows from the field and is
not an independent decision.

**2B — `_pending/` indexed, OR index status still unresolved.** The nine notes **stay in
`notes/` within the staging folder** and are not written into `_crossrefs/` at all. Everything
else in this build executes normally — frontmatter corrections, annotations, TAR candidate file,
manifest verification, provenance archive. Log the batch as *staged, promotion blocked pending
index-status resolution*. The build is complete in this state; it is not a partial execution.

**Default is 2B.** Absence of a confirmed answer is not a licence to proceed under 2A.

**Note on vocabulary, for the record.** In DFD workflow terms these are watch items — findings
held pending a gating judgment. `pending-anne` is the schema value; "watch item" is the workflow
characterisation. They are not alternatives and **`promotion_status` is not to be changed on any
file in this batch.** An earlier formulation in session suggested mutating the field to `watch`.
That was imprecise. Do not do it.

---

## Section 3 — Frontmatter corrections

Two files carry `scenario_implication: baseline-revision`. That field is a demographic
classification and requires Anne's domain authority. It was set provisionally by the drafter,
which is beyond the drafter's remit. A provisional value in a ratified field is worse than a
conservative one, because downstream retrieval cannot see that it was provisional.

**Edit 3.1 —** `2026-09-17_global-transition-demographics-ai.md`

```
- scenario_implication: baseline-revision
+ scenario_implication: neutral
```

**Edit 3.2 —** `2026-09-17_dividend-to-drag-kotschy-bloom.md`

```
- scenario_implication: baseline-revision
+ scenario_implication: neutral
```

Both notes already explain in their bodies why the drafter proposed `baseline-revision` and that
the classification is provisional pending Anne. **Leave that body text intact.** The reasoning
is provenance; only the field reverts.

**Verify:** no file in the batch carries `scenario_implication: baseline-revision` after these
edits. Report the grep result.

---

## Section 4 — Content annotations (Cath's correction)

Two notes report figures the source papers describe as welfare effects. They are percentage
changes in output or real income, not consumption-equivalent variation. Under DFD's welfare
metric discipline they must not travel into DFD output as welfare results.

**They are not to be relabelled.** The papers' own terminology is reported accurately and
altering it would misrepresent the source. The fix is additive: an annotation recording the
constraint.

**Annotation 4.1 —** `2026-09-17_aging-realignment-world-trade.md`, inserted immediately after
the Mexico results table:

```markdown
> **Metric caution (Cath, 2026-09-17).** The welfare figures above are the paper's own
> terminology: percentage changes in real income and in composition-adjusted consumption
> baskets. They are not consumption-equivalent variation. Under DFD welfare-metric discipline
> they may be cited as output or real-income changes and **must not be carried into DFD output
> as welfare results**.
```

**Annotation 4.2 —** `2026-09-17_endogenous-technical-change-demographic-transition.md`,
inserted immediately after the summary section:

```markdown
> **Metric caution (Cath, 2026-09-17).** Cumulative and annualised changes in output per capita
> reported here are the paper's own measures. They are not consumption-equivalent variation and
> **must not be carried into DFD output as welfare results**.
```

**Verify:** both annotations present, correctly placed, and no surrounding text modified.

---

## Section 5 — The synthesis is not a monitoring note

`2026-09-17_nber-aging-conference-synthesis.md` is an argument carrying findings across DFD, BDH
and Aurora boundaries. That is a **briefing note** in our established vocabulary. It does not fit
the monitoring frontmatter schema and it does not belong in the demographics monitoring corpus.

**The briefing-note schema is itself an open question in the Architecture workspace.** Therefore:

- **Do not file it under the monitoring schema.**
- **Do not invent a briefing-note path or frontmatter.**
- Leave it in `synthesis/`, unmodified. It is kept outside `notes/` precisely so that a directory
  glob over the batch cannot sweep it into the monitoring corpus.
- Record it in the build log as *awaiting briefing-note schema resolution, Architecture
  workspace*.

Filing it wrongly now costs more than holding it. This is deliberate.

---

## Section 6 — CROSS-TAR-001 anchor candidates

Six terms were proposed across the batch. They are batched for joint Anne/Cath review and **not
admitted**.

Write a single review file at `_crossrefs/corpus/demographics/_pending/2026-09-17_tar-candidates.md`
containing the six candidates with their source note and one-line justification, and nothing else:

| Term | Source note |
|---|---|
| θτ (rebalancing tax increase) | costs-of-building-walls |
| Stationary-through-immigration (SI) population | costs-of-building-walls |
| Demographic cliff (technical sense) | demographic-cliff-higher-education |
| Life-cycle comparative advantage | aging-realignment-world-trade |
| Frontier technology adoption (relative-price rule) | global-transition-demographics-ai |
| Prospective old-age threshold (POAT) | dividend-to-drag-kotschy-bloom |

`added_by: Debb`, `endorsed_by:` empty, `promotion_status: pending-anne`. **No write to the
register itself.**

---

## Section 7 — Citation ambiguity, unresolved by design

The reference stack lists **Auclert, Malmberg, Rognlie & Straub (2025)** as a tier-1
methodological reference (Equation 22, shift-share). Notes in this batch repeatedly flag
**Auclert, Malmberg, Martenet & Rognlie (2025)**, "Demographics, wealth, and global imbalances in
the twenty-first century," as an acquisition, cited by Kopecky as published in *Review of
Economic Studies*.

Overlapping author sets, differing fourth authors, possibly two distinct papers.

**Do not resolve this.** Do not merge the references, do not correct either, do not assume.
Write the ambiguity as a single line item in the build log flagged for the Architecture
workspace. A conflated reference occupying a tier-1 slot is expensive to unwind and cheap to
prevent.

---

## Section 8 — Provenance archive

Archive this build instruction and the session triage reasoning to
`_crossrefs/_build_instructions/` under permanent retention, per corpus-as-intellectual-provenance.

This applies **regardless of what is ultimately committed**. Build instructions are retained for
rejected work as well as accepted work; that is the point of retaining them.

Filename: `2026-09-17_BI_demographics-nber-batch.md`

---

## Section 9 — What this build deliberately does not do

Recorded so that absence is not later read as omission.

1. **No corpus commit.** Nine notes are staged, not promoted.
2. **No demographic adjudication.** Demographic adjudications are made in the Demographics
   workspace and consumed downstream, not re-derived. Anne's rulings on prospective-versus-
   chronological age structure and on the WPP/CELADE reconciliation are provisional until issued
   there. **Do not encode them as settled in any file.**
3. **No IM-6 change.** Cath's exogeneity audit is outstanding. Nothing in this batch touches the
   module.
4. **No `_baseline.md` change.** Anne's v1.0 hold on the TFR discrepancy against CELADE's
   Demographic Observatory 2025 remains in force and this batch does not disturb it.
5. **No supersession field.** `2026-09-17_spatial-consequences-depopulation.md` is superseded in
   part by the Giannone note. The relation is recorded in both bodies. **No relation field is to
   be added** — that would be schema invention. If a relation field is wanted, it is an
   Architecture workspace decision.

---

## Section 10 — Completion criteria

Report against each. All must hold.

- [ ] Batch folder structure verified: nine notes, nine sources, one synthesis
- [ ] Manifest complete: every note mapped, every source mapped, no orphans in either direction
- [ ] `pdfinfo` run across all nine; two blank page counts filled; seven verified counts confirmed
- [ ] No file in `sources/` renamed or modified
- [ ] **Index-status probe run and result reported; branch 2A or 2B declared explicitly**
- [ ] **Canary file deleted after probe**
- [ ] Nine monitoring notes in their branch-correct location (2A: `_pending/`; 2B: staging `notes/`)
- [ ] `grep scenario_implication` returns no `baseline-revision` in the batch
- [ ] `grep promotion_status` returns `pending-anne` on all nine; no `ready`, no `watch`
- [ ] `grep "endorsed_by"` returns empty value on all files written
- [ ] Two metric-caution annotations present and correctly placed
- [ ] Synthesis remains in `synthesis/`, unmodified, logged as awaiting schema
- [ ] TAR candidate file written; register untouched
- [ ] Auclert ambiguity logged, unresolved
- [ ] Build instruction **and manifest** archived to `_crossrefs/_build_instructions/`
- [ ] No existing corpus file modified or overwritten

## Routing on completion

- **Architecture workspace — priority.** Index-status of `_crossrefs/corpus/demographics/_pending/`,
  as determined by the Section 2 probe. If `_pending/` is indexed, the finding is larger than
  this batch: every note ever held there has been retrievable as though endorsed, and the
  layered-authorship model has been advisory rather than enforced. Also outstanding: the
  briefing-note schema; the Auclert citation; the relation-field question; and a permanent home
  for source PDFs, which the structure currently lacks.
- **Anne** — WPP/CELADE reconciliation; prospective-versus-chronological ruling; original-lines
  ranking. Issued from the Demographics workspace.
- **Cath** — IM-6 exogeneity audit (single note); θτ benchmark run.
- **Beth** — Huetsch, Krueger & Ludwig acquisition; POAT scoping for the morbidity module.

Awaiting Héctor's authorization before any promotion out of staging or `_pending/`.

---

## Execution log (Claude Code, 2026-09-17)

**Executed against the flat staging folder** `GrandPlan/DFD/aging_macro_nber_2609/` on Héctor's
instruction. The folder does not carry the `notes/`, `sources/`, `synthesis/` subfolders assumed
in Section 1; no subfolders were created (Section 0, item 4). Paths in this log are relative to
that folder unless stated.

**Section 1 — Ingest.** Nine monitoring notes, nine source PDFs, one synthesis note, one manifest,
one build instruction, plus one superseded draft of this build instruction (see below). All nine
notes parse as YAML frontmatter plus body and carry the full twelve-field monitoring set. Every
note has a manifest row and every PDF is named in one; no orphans in either direction.
`pdfinfo` across all nine: rows 4 and 5 filled (Pettersson `f249391.pdf` 56 pp; Kopecky
`f249850.pdf` 40 pp); the seven recorded counts all confirmed (75, 100, 72, 56, 66, 126, 71).
No file in `sources/` renamed or modified.

**Section 2 — Branch 2B declared (Héctor, 2026-09-17).** The index-status probe was **not run**:
no vector store, index build script, or embedding tooling exists anywhere in the Dalila tree, so
there is nothing to rebuild or query. No canary was written. Index status of `_pending/` remains
**unresolved**; the nine notes stay in the staging folder and are not written into
`_crossrefs/`. Batch logged as *staged, promotion blocked pending index-status resolution*.

**Section 3.** `scenario_implication` reverted to `neutral` on
`2026-09-17_global-transition-demographics-ai.md` and `2026-09-17_dividend-to-drag-kotschy-bloom.md`;
body text untouched. Grep for `baseline-revision` across the nine notes returns nothing.

**Section 4.** Annotation 4.1 inserted after the Mexico results table in
`2026-09-17_aging-realignment-world-trade.md`; annotation 4.2 inserted after the Summary section
in `2026-09-17_endogenous-technical-change-demographic-transition.md`. Diff against pre-edit
copies shows only the added blockquote lines.

**Section 5.** `2026-09-17_nber-aging-conference-synthesis.md` left in the staging folder,
unmodified. *Awaiting briefing-note schema resolution, Architecture workspace.*

**Section 6.** `_crossrefs/corpus/demographics/_pending/2026-09-17_tar-candidates.md` written
(monitoring frontmatter set, `added_by: Debb`, `endorsed_by:` empty,
`promotion_status: pending-anne`); six candidates with source note and justification, plus the
PROTO-RAG-001 mandatory back-link to this instruction. CROSS-TAR-001 register untouched.

**Section 7 — Auclert citation ambiguity, unresolved.** Reference stack lists Auclert, Malmberg,
Rognlie & Straub (2025) as tier-1 (Eq. 22, shift-share); batch notes flag Auclert, Malmberg,
Martenet & Rognlie (2025), "Demographics, wealth, and global imbalances in the twenty-first
century," *Review of Economic Studies* per Kopecky. Possibly two distinct papers. **Flagged for
the Architecture workspace; not merged, not corrected.**

**Section 8.** This file, and the manifest as
`2026-09-17_BI_demographics-nber-batch_MANIFEST.md` (post-verification copy, page counts
filled), archived here under permanent retention.

**Section 9.** No corpus commit, no demographic adjudication encoded, no IM-6 change, no
`_baseline.md` change, no relation field added to the de Silva & Paron note.

**Observed, not acted on.** The staging folder holds `2026-09-17_BI_demographics-nber-batch.md`,
an earlier draft of this instruction that predates the Section 2 index-probe revision (it
instructs creating `_pending/` if absent). It was not archived and not deleted; disposition is
Debb's call. The nine notes carry `added_by: Claude`; the build does not ask for a change and
none was made.

**Git.** Nothing committed or pushed. All changes are in the working tree on branch
`p4-version-final`.

### Completion criteria

- [x] Batch folder structure verified (flat layout, per Héctor): nine notes, nine sources, one synthesis
- [x] Manifest complete: every note mapped, every source mapped, no orphans
- [x] `pdfinfo` run across all nine; two blank counts filled; seven verified counts confirmed
- [x] No file in `sources/` renamed or modified
- [x] Index-status probe: **not runnable** (no vector store in tree); **branch 2B declared** by Héctor
- [x] Canary: none written, none to delete
- [x] Nine monitoring notes in branch-correct location (2B: staging folder)
- [x] `grep scenario_implication` returns no `baseline-revision` in the batch
- [x] `grep promotion_status` returns `pending-anne` on all nine; no `ready`, no `watch`
- [x] `grep endorsed_by` returns empty value on all files written
- [x] Two metric-caution annotations present and correctly placed
- [x] Synthesis in staging, unmodified, logged as awaiting schema
- [x] TAR candidate file written; register untouched
- [x] Auclert ambiguity logged, unresolved
- [x] Build instruction and manifest archived to `_crossrefs/_build_instructions/`
- [x] No existing corpus file modified or overwritten

---
type: build_instruction
build_type: retrofit
date: 2026-08-03
corpus_affected:
  - _crossrefs/corpus/demographics/scenario_anchors.md
  - _crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q2_demographic_replicate.md
triggered_by: "Anne's and Cath's 2026-08-03 rulings (recorded in _pending/_anne_inbox.md, 'Flagged to Debb' items 1, 4, 5): two endorsed demographics-corpus artifacts carry `type: working_note`, which PROTO-RAG-001 defines as a *tier* value, not a *type*. Retrofit to `type: corpus_entry` via explicit build instruction per PROTO-RAG-001 standing principle 5 (no silent amendment)."
agents_involved: [Anne, Cath, Debb]
status: executed
notes: "Mechanical type-field retrofit; two files; tier fields, endorsement lines, and all body content preserved verbatim. Also records the closure of the option-(a) decision on quarterly-replicate build instructions (§5) and the protocol revision candidates list (§6)."
---

# Demographics corpus — `type:` field retrofit

**To:** Claude Code (Dalila session)
**From:** Debb (Infrastructure & Workflow)
**Date:** 2026-08-03
**Re:** Bring two endorsed demographics-corpus artifacts into PROTO-RAG-001 type-vocabulary conformity. Mechanical pass, no substantive content changes.

---

## 1. Scope and rationale

PROTO-RAG-001's corpus-entry schema defines `type: corpus_entry` with
`tier: [methodological_reference | data_source | working_note | foundational_text]`.
Two endorsed artifacts in the demographics corpus were drafted with
`working_note` promoted into the `type:` slot — a value the protocol reserves
for `tier:` — leaving them invisible to any retrieval that filters on
`type: corpus_entry`:

- `_crossrefs/corpus/demographics/scenario_anchors.md` (`type: working_note`, `tier: data_source`)
- `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q2_demographic_replicate.md` (`type: working_note`, `tier: working_note`)

The Q3 replicate is already conformant (`type: corpus_entry`); only these two
artifacts are affected. Per PROTO-RAG-001 standing principle 5, existing
artifacts are retrofitted via an explicit retrofit build instruction, not
silently amended — this document is that instruction.

**Hard constraint (Cath, 2026-08-03 ruling):** the Q2 replicate's
`endorsed_by:` line records a conditioned endorsement (resolution caveat as an
endorsement condition) and must survive this retrofit byte-for-byte. No other
frontmatter field, and no body content, changes in either file beyond what §2
specifies.

---

## 2. Per-artifact retrofit instructions

### 2.1 — `_crossrefs/corpus/demographics/scenario_anchors.md`

**Frontmatter change (one line):**

- `type: working_note` → `type: corpus_entry`
- `tier: data_source` is retained unchanged.
- All other frontmatter fields (including `endorsed_by: Anne` and
  `workflow_status: endorsed`) unchanged.

**Cross-references section:** append one line back-linking this retrofit:

```markdown
- → Type retrofit build instruction: `_crossrefs/_build_instructions/2026-08-03_demographics_type_retrofit.md`
```

**Body content.** Otherwise unchanged.

### 2.2 — `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q2_demographic_replicate.md`

**Frontmatter change (one line):**

- `type: working_note` → `type: corpus_entry`
- `tier: working_note` is retained unchanged (this is the correct use of the
  value, per the routing table in SKILL.md §Routing and Filing).
- The `endorsed_by:` line is preserved **byte-for-byte** (Cath's hard
  constraint). All other frontmatter fields unchanged, including the
  `governing_instructions:` field and the placeholder `build_instruction:`
  value (see §6, candidate 4).

**Cross-references section:** append one line back-linking this retrofit:

```markdown
- → Type retrofit build instruction: `_crossrefs/_build_instructions/2026-08-03_demographics_type_retrofit.md`
```

**Body content.** Otherwise unchanged.

---

## 3. Out of scope

- The Q2 replicate's `build_instruction:` placeholder value is **not**
  rewritten here. Its resolution is governed by the option-(a) decision (§5):
  the Q2 run predates the per-quarter convention, and fabricating a
  retroactive per-quarter build instruction for it would falsify provenance.
  The `governing_instructions:` field plus this retrofit's back-link give the
  file a complete provenance trail.
- No `tier:` values change in either file.
- No SKILL.md or README changes are executed *by this instruction* — the
  concurrent SKILL.md v0.2 → v0.3 revision (same date, same ruling batch) is
  recorded in the skill's own §Revision history per its established
  convention.

---

## 4. Execution checklist

- [x] Verify both target files exist at the paths in §2
- [x] Verify `type: working_note` is the current value in both frontmatter blocks
- [x] Apply the `type:` change to `scenario_anchors.md`; append back-link
- [x] Apply the `type:` change to the Q2 replicate; append back-link
- [x] Verify the Q2 `endorsed_by:` line is byte-identical to its pre-retrofit state
- [x] Verify no other lines changed in either file
- [x] File this build instruction; mark `status: executed`
- [x] Resolve the corresponding "Flagged to Debb" items in `_pending/_anne_inbox.md`

---

## 5. Closed decision — option (a) for quarterly replicates

The Q2 replicate's §8 posed two conformance routes for recurring quarterly
artifacts: (a) a dated build instruction per quarter, or (b) a PROTO-RAG-001
amendment authorizing a `governing_instructions:` field as a standing
substitute. Anne provisionally ratified (a) on 2026-08-03; the Q3 replicate
was already executed under (a).

**Debb concurs, 2026-08-03. Decision closed: option (a). No PROTO-RAG-001
amendment.** Reasoning: each quarterly run takes run-specific decisions —
what was retrieved and what was carried, re-anchor calls, supersessions of
prior anchors — that a standing instructions document cannot record without
becoming a changelog, which is exactly the job PROTO-RAG-001 assigns to build
instructions. Option (a) keeps the artifact/provenance separation one-to-one
(one run, one record), costs one small file per quarter, requires no protocol
amendment, and matches executed practice (Q3). Option (b) would have made the
standing instructions document both governing method and provenance record,
weakening the archive's reconstruction guarantee.

Operational rule going forward: every quarterly replicate files
`_crossrefs/_build_instructions/YYYY-MM-DD_demographics_MEX_{quarter}_replicate.md`
(or equivalent slug) as its build instruction of record. The standing
instructions document (`DFD_TFR_forecast_instructions.md`) governs method and
is referenced via `governing_instructions:` as a supplementary field. Recorded
also in SKILL.md v0.3 §Routing and Filing (endorsement workflow, item 6).

---

## 6. Notes — protocol revision candidates (for the next PROTO-RAG-001 revision)

Recorded here so they surface at the next protocol revision; **no protocol
edit is made now**:

1. **`endorsement_record` artifact type.** Anne's 2026-07-11 UNFPA
   adjudication was filed as `2026-07-11_UNFPA-note_Anne-endorsement.md` with
   an `endorsement_record` type that PROTO-RAG-001 does not define. Retained
   as provenance (correctly — deleting or retyping it would lose the
   adjudication record). The next revision should either add
   `endorsement_record` to the type vocabulary with a minimal schema, or
   specify the canonical filing for out-of-band endorsement adjudications.
2. **`skill_invocation` type on build instructions of record.** The Q3
   replicate's build instruction
   (`2026-08-03_demographics_MEX_2026Q3_replicate.md`) carries
   `type: skill_invocation` rather than `type: build_instruction`, and does
   not use the build-instruction frontmatter schema (`build_type`,
   `corpus_affected`, `triggered_by` absent). With option (a) now closed,
   per-quarter records are permanent archive citizens; the next revision
   should either fold them into the `build_instruction` schema or define
   `skill_invocation` as a recognized archive type.
3. **Skill extension fields.** The `dfd-demographics-monitor` skill
   authorizes frontmatter fields (`workflow_status`, `indicators`,
   `geography`, `scenario_implication`, `source_reliability`,
   `data_vintage`) that PROTO-RAG-001's corpus-entry schema does not know.
   They are in productive use across the demographics corpus. The next
   revision should sanction skill-authorized extension fields generically
   (e.g., "skills may add retrieval fields; they must not collide with or
   redefine protocol fields").
4. **`governing_instructions:` supplementary field.** Used by the quarterly
   replicates to point at the standing methods document. Under closed option
   (a) it is supplementary, not a substitute for `build_instruction:`; the
   next revision should register it as an optional field so it stops reading
   as a schema deviation.

---

## 7. Cross-references

- → Governing protocol: `_crossrefs/protocols/PROTO-RAG-001.md`
- → Ruling record: `_crossrefs/corpus/demographics/_pending/_anne_inbox.md` (2026-08-03 entries)
- → Retrofitted artifact: `_crossrefs/corpus/demographics/scenario_anchors.md`
- → Retrofitted artifact: `_crossrefs/corpus/demographics/country/MEX/quarterly/2026-Q2_demographic_replicate.md`
- → Retrofit precedent: `_crossrefs/_build_instructions/2026-04-29_inequality_corpus_retrofit.md`
- → Option-(a) executed precedent: `_crossrefs/_build_instructions/2026-08-03_demographics_MEX_2026Q3_replicate.md`
- → Concurrent skill revision: `_crossrefs/_skills/dfd-demographics-monitor/SKILL.md` (v0.3, same date)

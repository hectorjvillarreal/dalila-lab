---
type: build_instruction
build_type: retrofit
date: 2026-04-29
corpus_affected:
  - _crossrefs/corpus/inequality/methodology/clarke_kopczuk_2025.md
  - _crossrefs/corpus/inequality/methodology/gomez_2025.md
  - _crossrefs/corpus/inequality/public_finance/auerbach_2025.md
  - _crossrefs/corpus/inequality/watch_items/automated_life_for_capital.md
  - _crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md
triggered_by: "Sequence position 2 of 5 in the corpus-expansion campaign initiated 2026-04-28. The four inequality corpus entries were drafted before PROTO-RAG-001 was formalized; this retrofit brings them into conformity by adding endorsed_by fields where applicable and build_instruction back-links to all entries."
agents_involved: [Héctor, Anne, Debb]
status: executed
sequence_position: 2_of_5
notes: "Mechanical retrofit. Body content of all four entries is preserved verbatim; only frontmatter additions and a single Cross-references line per entry. The endorsed_by fields are filled where domain authority is uncontested at draft time and left empty where Cath's review is still pending (notably the Gomez entry, where the propagation question remains open)."
---

# Inequality Corpus Retrofit — Build Instructions for Claude Code

**To:** Claude Code (Dalila session)
**From:** Debb (Infrastructure & Workflow)
**Date:** 2026-04-29
**Re:** Bring the four pre-existing inequality corpus entries into PROTO-RAG-001 conformity. Mechanical pass, no substantive content changes.

---

## 1. Scope and rationale

The four inequality corpus entries created on 2026-04-28 were drafted before PROTO-RAG-001 was formalized. They conform to the spirit of the protocol (frontmatter present, structure correct, cross-references included) but lack two specific schema additions that the protocol now mandates:

- The `endorsed_by` field, distinguishing the agent who drafted the entry from the agent whose domain authority backs its substantive claims.
- The `build_instruction` field and a corresponding back-link in the Cross-references section, closing the provenance loop between artifact and the build that created it.

This retrofit adds both to all four entries. Body content is preserved verbatim. After this build executes, all subsequent corpus builds will be born under PROTO-RAG-001 from the start, and no further retrofitting is anticipated.

A reciprocal note is also added to the inequality corpus initial build instruction, recording that its artifacts have been brought into protocol conformity.

---

## 2. Endorsement assignments

Per Anne's drafting and Cath's domain authority over fiscal-modeling claims, endorsements are assigned as follows:

| Entry | added_by | endorsed_by | Reasoning |
|---|---|---|---|
| `clarke_kopczuk_2025.md` | Anne | Cath | Methodology entry; substantive claims about OLG calibration discipline and the PSZ vs. AS dispute fall within Cath's fiscal-modeling authority. Endorsable at retrofit time. |
| `gomez_2025.md` | Anne | (empty) | Substantive claims about Hicksian propagation to OLG equilibrium structure remain open pending Cath's judgment. The propagation question is logged as the gating condition in the watch item. Leave `endorsed_by` empty until Cath provides judgment. |
| `auerbach_2025.md` | Anne | Cath | Public finance entry; claims about life-cycle progressivity, indirect tax mechanisms, and revenue volatility fall within Cath's fiscal-modeling authority. Endorsable at retrofit time. |
| `automated_life_for_capital.md` | Héctor & Anne (`opened_by`) | Héctor | Watch item; `endorsed_by` confirms the thread is worth tracking, not that the underlying claim is correct. Héctor opened the thread and explicitly affirmed it as worth keeping an eye on, which constitutes endorsement of the watch-item status. The substantive question is gated on Cath. |

The asymmetry on the Gomez entry is intentional and protocol-conformant. PROTO-RAG-001 explicitly permits `endorsed_by` to remain empty when domain authority review is pending.

---

## 3. Per-entry retrofit instructions

### 3.1 — `_crossrefs/corpus/inequality/methodology/clarke_kopczuk_2025.md`

**Frontmatter changes.** Add `endorsed_by` and `build_instruction` fields. The retrofitted frontmatter block should read:

```yaml
---
type: corpus_entry
tier: methodological_reference
project_scope: [DFD, BDH, RF]
authors: [Clarke, Conor; Kopczuk, Wojciech]
year: 2025
title: "Measuring Income and Income Inequality"
venue: "Journal of Economic Perspectives, 39(2), 103–126"
doi: "10.1257/jep.20241424"
date_added: 2026-04-28
added_by: Anne
endorsed_by: Cath
build_instruction: "_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md"
---
```

**Cross-references section.** Add the following line as the final entry in the existing Cross-references list:

```markdown
- → Build instruction: `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`
```

**Body content.** Unchanged.

---

### 3.2 — `_crossrefs/corpus/inequality/methodology/gomez_2025.md`

**Frontmatter changes.** Add `endorsed_by` (left empty pending Cath's judgment on the propagation question) and `build_instruction` fields. The retrofitted frontmatter block should read:

```yaml
---
type: corpus_entry
tier: methodological_reference
project_scope: [DFD, fiscal_dominance_paper]
authors: [Gomez, Matthieu]
year: 2025
title: "Macro Perspectives on Income Inequality"
venue: "Journal of Economic Perspectives, 39(2), 127–148"
doi: "10.1257/jep.20241435"
date_added: 2026-04-28
added_by: Anne
endorsed_by:
build_instruction: "_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md"
---
```

The empty `endorsed_by` field is left as a YAML key with no value, indicating that endorsement is awaited (rather than that the field is absent or irrelevant).

**Cross-references section.** Add the following line as the final entry in the existing Cross-references list:

```markdown
- → Build instruction: `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`
```

**Body content.** Unchanged.

**Standing note for future endorsement.** When Cath provides judgment on the propagation question (whether Hicksian critique propagates to OLG equilibrium structure or remains an inequality-measurement issue), the `endorsed_by` field is filled via a small expansion build (not a retrofit), and the watch item `automated_life_for_capital.md` is updated correspondingly. That sequence is anticipated but not scheduled.

---

### 3.3 — `_crossrefs/corpus/inequality/public_finance/auerbach_2025.md`

**Frontmatter changes.** Add `endorsed_by` and `build_instruction` fields. The retrofitted frontmatter block should read:

```yaml
---
type: corpus_entry
tier: methodological_reference
project_scope: [DFD, BDH, fiscal_dominance_paper]
authors: [Auerbach, Alan J.]
year: 2025
title: "Public Finance Implications of Economic Inequality"
venue: "Journal of Economic Perspectives, 39(2), 149–170"
doi: "10.1257/jep.20241421"
date_added: 2026-04-28
added_by: Anne
endorsed_by: Cath
build_instruction: "_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md"
---
```

**Cross-references section.** Add the following line as the final entry in the existing Cross-references list:

```markdown
- → Build instruction: `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`
```

**Body content.** Unchanged.

---

### 3.4 — `_crossrefs/corpus/inequality/watch_items/automated_life_for_capital.md`

**Frontmatter changes.** Add `endorsed_by`, `promoted_by` (left empty; will be filled only on promotion), `date_promoted` (left empty), and `build_instruction` fields. The retrofitted frontmatter block should read:

```yaml
---
type: research_watch_item
status: open
date_opened: 2026-04-28
opened_by: [Héctor, Anne]
endorsed_by: Héctor
promoted_by:
date_promoted:
related_corpus: [methodology/gomez_2025.md]
related_projects: [DFD/IM-6, fiscal_dominance_paper]
build_instruction: "_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md"
---
```

The empty `promoted_by` and `date_promoted` fields are left as YAML keys with no values, in conformity with PROTO-RAG-001's watch-item schema.

**Cross-references section.** Add the following line as the final entry in the existing Cross-references list:

```markdown
- → Build instruction: `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`
```

**Body content.** Unchanged.

---

## 4. Reciprocal update to the inequality corpus initial build instruction

### 4.1 — `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`

The build instruction's own frontmatter is updated to record that its artifacts have been retrofitted to PROTO-RAG-001 conformity. The `status` field transitions from `pending_execution` (or `executed`, if Claude Code marked it so on completion) to `executed`. A new field, `protocol_conformed_via`, is added.

The retrofitted frontmatter block should read:

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
status: executed
sequence_position: legacy_pre_protocol
protocol_conformed_via: "_crossrefs/_build_instructions/2026-04-29_inequality_corpus_retrofit.md"
notes: "First corpus build instruction written, predating formalization of PROTO-RAG-001. Retrofitted to protocol convention by build 2026-04-28_protocol_foundation (folder structure and naming) and 2026-04-29_inequality_corpus_retrofit (artifact frontmatter and back-links). Body content preserved as drafted; minor frontmatter conformity additions only."
---
```

**Body content.** Unchanged.

---

## 5. Self-update on completion

When this retrofit build executes successfully, its own `status` field transitions from `pending_execution` to `executed`. No other self-modification.

---

## 6. Execution checklist for Claude Code

- [ ] Verify all four corpus entry files exist at the paths specified in Section 3
- [ ] Verify the inequality corpus initial build instruction exists at `_crossrefs/_build_instructions/2026-04-28_inequality_corpus_initial.md`
- [ ] Update frontmatter of `clarke_kopczuk_2025.md` per Section 3.1
- [ ] Append the build-instruction back-link to its Cross-references section per Section 3.1
- [ ] Update frontmatter of `gomez_2025.md` per Section 3.2 (note the deliberately empty `endorsed_by`)
- [ ] Append the build-instruction back-link to its Cross-references section per Section 3.2
- [ ] Update frontmatter of `auerbach_2025.md` per Section 3.3
- [ ] Append the build-instruction back-link to its Cross-references section per Section 3.3
- [ ] Update frontmatter of `automated_life_for_capital.md` per Section 3.4 (note the deliberately empty `promoted_by` and `date_promoted`)
- [ ] Append the build-instruction back-link to its Cross-references section per Section 3.4
- [ ] Update frontmatter of `2026-04-28_inequality_corpus_initial.md` per Section 4.1 (status to `executed`; add `protocol_conformed_via`; expand `notes`)
- [ ] Save this build instruction itself as `_crossrefs/_build_instructions/2026-04-29_inequality_corpus_retrofit.md`
- [ ] Update this build instruction's `status` to `executed` on completion
- [ ] Verify body content of all four entries is byte-identical to pre-retrofit state (frontmatter additions only; one line added to each Cross-references section)
- [ ] Commit with message: `inequality corpus: retrofit to PROTO-RAG-001 (endorsed_by + build_instruction back-links)`
- [ ] Report back: confirmation of retrofit; any anomalies (entries that did not exist at expected paths; existing frontmatter that conflicted with the retrofit additions; any build_instruction back-link already present that would have caused duplication)

---

## 7. Notes

- This is the only retrofit anticipated for the inequality corpus. From sequence position 3 onward, all corpus builds operate under PROTO-RAG-001 from the start.
- The empty `endorsed_by` on the Gomez entry is the most consequential standing item from this retrofit. Cath's judgment on whether the Hicksian critique propagates to the OLG equilibrium structure (vs. remaining an inequality-measurement issue) is the gating condition. When Cath provides judgment, a small expansion build will fill the field and update the watch item correspondingly. Anne's standing instinct (the latter; non-propagation) is recorded in the Gomez entry but not endorsed.
- The asymmetry between `added_by` and `endorsed_by` is now operationally visible in the corpus for the first time. Future readers should understand that an entry with `endorsed_by` filled has crossed the bar of domain-authority review; an entry with `endorsed_by` empty has not. This is the intended discipline.
- After this retrofit executes, sequence position 3 — `demographic_methods/` initial scaffold under Anne's lead — becomes the next build. Anne will confirm scope and initial entries before that build instruction is drafted.

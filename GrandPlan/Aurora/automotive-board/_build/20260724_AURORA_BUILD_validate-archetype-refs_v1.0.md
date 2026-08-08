---
doc_id: 20260724_AURORA_BUILD_validate-archetype-refs_v1.0
title: "Build instruction — validate.py: list-valued archetype_ref and referential integrity"
project: Aurora / automotive board
type: build_instruction
version: 1.0
date: 2026-07-24
added_by: Elle
endorsed_by:
scope: tools/validate.py only
---

# BUILD INSTRUCTION — `validate.py`: archetype_ref integrity

**For:** Claude Code, agentic session, inside the automotive-board tree.
**Fence:** `CLAUDE.md` in the working directory governs. This task changes **one file**:
`tools/validate.py`. Everything else in the tree is read-only for this session.

---

## 0. Why this is needed

On 2026-07-24 two archetype poles were split by hand:

- pole 2 `span-legitimacy-conglomerate` → `segment-span-conglomerate` + `acquired-legitimacy`
- pole 4 `transition-tempo-skeptic` → `multi-path-hedger` + `tempo-skeptic`

After a split, a player routinely holds **more than one pole**. `001-geely.yaml` and
`004-toyota.yaml` now carry list-valued `archetype_ref`, and the current validator
expects a string — so validation fails on two of seven entries, and
`--check-boundary` cannot run as a pre-commit hook until it passes.

This is also the moment to add the check that makes a split *verifiable*: **referential
integrity.** The tool must not perform splits (prohibition 1 and 9 — splits are
judgment), but it can and should detect a split that was **half-applied** — a dangling
pointer, or a retired slug still in use. That is error *detection*, not classification,
and it sits inside the automation boundary.

---

## 1. What changes

`tools/validate.py` only. Three rules, all read-only against the tree.

### Rule A — `archetype_ref` accepts string or list

```yaml
archetype_ref: "pure-diffusion-integrator"                      # valid
archetype_ref: ["multi-path-hedger", "tempo-skeptic"]           # valid
archetype_ref: []                                               # INVALID — must be non-empty
```

Normalise a bare string to a one-element list internally. Do **not** rewrite the files —
`archetype_ref` is read-only to the tool.

### Rule B — referential integrity

Every element of every `archetype_ref` must appear in the registry's `active` list. A
reference to a slug that is in neither `active` nor `retired` is a **dangling pointer** →
fail, naming the entry and the slug.

### Rule C — retired slugs are a hard failure

A reference to a slug in the registry's `retired` list → fail, with a message that names
the retired slug and its replacements *as recorded in the registry comment*. Do not infer
replacements; quote what the registry says.

---

## 2. The registry — and the parsing trap

The registry is a fenced YAML block inside `instances/automotive/archetypes.md`,
delimited by:

```
<!-- SLUG-REGISTRY-BEGIN -->
<!-- SLUG-REGISTRY-END -->
```

**Parse only what is between those markers.**

**⚠ The trap:** retired slugs also appear in the *prose* of `archetypes.md`, in backticks
and in brackets, as documentation of what was split — e.g. ``The original pole
`[span-legitimacy-conglomerate]` …``. A parser that scans the file for `` `[slug]` ``
patterns will read retired slugs as valid anchors and Rule C will never fire. **The prose
is not the registry.** If the delimiters are absent, **fail loudly** — do not fall back to
scanning prose.

---

## 3. What does not change

- No other check in `validate.py`.
- `--check-boundary` behaviour is untouched; it should simply now be *reachable*, because
  the tree validates.
- No entry file, no YAML, no `archetypes.md`. If the registry block is missing, **stop and
  report** — adding it is a human edit (prohibition 9).
- No new dependencies.

---

## 4. Acceptance

- [ ] **Fence report:** every path read or written. One file written: `tools/validate.py`.
- [ ] `validate.py` passes on the current tree, including `001-geely.yaml` and
      `004-toyota.yaml` with list-valued refs.
- [ ] A string-valued ref (e.g. `002-byd.yaml`) still passes.
- [ ] **Demonstrate Rule B:** temporarily point an entry at `not-a-real-pole` → fails,
      naming entry and slug. Revert.
- [ ] **Demonstrate Rule C:** temporarily point an entry at `transition-tempo-skeptic` →
      fails as *retired*, not as *dangling*. Revert. *This is the check that would catch a
      half-applied split; the demonstration is the point.*
- [ ] Empty list → fails.
- [ ] Registry block deleted → fails loudly, with no fallback to prose scanning. Revert.
- [ ] `validate.py --check-boundary` still fails on a deliberately-introduced read-only
      edit. Revert.
- [ ] Commit: `tool(validate): archetype_ref list support + referential integrity`.
      Local only; no remote, no push.

---

## 5. Prohibitions — unchanged

The tool must never assign, change, normalise, or suggest an archetype; compute or
suggest loadings; declare a bet's status; rank players; write any prose field or any
read-only key; or edit `archetypes.md`. **Detecting a broken reference is permitted.
Repairing one is not** — report it and stop.

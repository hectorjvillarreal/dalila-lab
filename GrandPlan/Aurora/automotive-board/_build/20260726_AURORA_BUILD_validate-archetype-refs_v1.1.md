---
doc_id: 20260726_AURORA_BUILD_validate-archetype-refs_v1.1
title: "Build instruction — validate.py: list-valued archetype_ref and referential integrity"
project: Aurora / automotive board
type: build_instruction
version: 1.1
supersedes: 20260724_AURORA_BUILD_validate-archetype-refs_v1.0   # DEFECTIVE — see §1. Retain as provenance.
date: 2026-07-26
added_by: Elle
endorsed_by:
scope: tools/validate.py and tools/fixtures/ only
---

# BUILD INSTRUCTION — `validate.py`: archetype_ref integrity (v1.1)

**For:** Claude Code, agentic session, inside `automotive-board/`.
**Fence:** `CLAUDE.md` at the tree root governs. This task writes **two paths only**:
`tools/validate.py` and a new `tools/fixtures/` directory.

---

## 0. STOP — if you are already executing v1.0

**v1.0 was defective and is withdrawn.** Before doing anything else:

1. **Report your current state.** What has been done so far? Which paths have you read
   and which have you written?
2. **Report specifically** whether you modified — even temporarily, even with intent to
   revert — any of: an entry `.yaml` file, `instances/automotive/archetypes.md`, or any
   file under `instances/`. v1.0 asked you to. **Doing so was correct obedience to a bad
   instruction, not a fault**; report it plainly.
3. **Confirm the tree is clean.** `git status` should show changes to `tools/` only.
   `git diff HEAD -- instances/` should be empty. If any entry file or `archetypes.md`
   differs from HEAD, **restore it from HEAD and say so** — do not attempt to reconstruct
   by editing.
4. **Do not commit anything from the v1.0 run** that touches `instances/`.

Only then continue with §2 below.

---

## 1. Why v1.0 was withdrawn

v1.0's acceptance criteria instructed the agent to *temporarily* point a real entry at a
bad slug, and to *delete* the registry block from `archetypes.md`, in order to demonstrate
that the new checks fire. **Both are read-only, human-owned targets.** The instruction
therefore could only be satisfied by violating the standing prohibitions — a correctly
fenced agent would hit scope-arrest and stall, an incorrectly fenced one would proceed.
The instruction was wrong, not the fence.

**The general lesson, worth keeping:** *a test must never require mutating the artifact
under protection.* Test against **fixtures** instead. This also converts a one-time
demonstration into a permanent regression suite.

---

## 2. What changes — four rules

`tools/validate.py` only. All checks are read-only against the tree.

### Rule A — `archetype_ref` accepts string or list

```yaml
archetype_ref: "pure-diffusion-integrator"                # valid
archetype_ref: ["multi-path-hedger", "tempo-skeptic"]     # valid
archetype_ref: []                                         # INVALID — must be non-empty
```

Normalise a bare string to a one-element list *internally*. **Do not rewrite the files** —
`archetype_ref` is read-only to the tool.

### Rule B — referential integrity

Every element of every `archetype_ref` must appear in the registry's `active` list. A slug
in neither `active` nor `retired` is a **dangling pointer** → fail, naming entry and slug.

### Rule C — retired slugs are a hard failure

A slug in the registry's `retired` list → fail, distinctly from dangling, quoting the
registry's own comment for that slug. **Do not infer replacements.**

### Rule D — registry/prose coherence (warning, one-directional) — NEW

For each slug in `active`, warn if it does not appear anywhere in `archetypes.md` **outside**
the registry block.

*Why one-directional:* a misspelled `active` slug causes a loud false dangling-failure and
is self-announcing. The silent direction is a slug present in the registry that is **not
actually a pole in the prose** — a bad reference would then validate clean. Rule D catches
that. It stays a **warning**, and prose is never parsed for validity, so the §3 trap stays
closed.

---

## 3. The registry — and the parsing trap

The registry is a fenced YAML block in `instances/automotive/archetypes.md`, delimited by:

```
<!-- SLUG-REGISTRY-BEGIN -->
<!-- SLUG-REGISTRY-END -->
```

**Parse only what is between those markers.**

**⚠ The trap:** retired slugs also appear in the *prose* of `archetypes.md`, in backticks
and brackets, documenting what was split — e.g. ``The original pole
`[span-legitimacy-conglomerate]` …``. A parser scanning for `` `[slug]` `` patterns will
read retired slugs as valid anchors and Rule C will never fire. **The prose is not the
registry.** If the delimiters are absent, **fail loudly** — never fall back to prose
scanning.

---

## 4. Fixtures — how the rules are proven

Create `tools/fixtures/`. Add an optional `--root <dir>` argument to `validate.py`
(default: repo root) so it can be pointed at a fixture tree. This is a general capability,
not a test hack.

**Required fixtures and expected results:**

| Fixture | `archetype_ref` | Expected |
|---|---|---|
| `entry-valid-string.yaml` | `"pure-diffusion-integrator"` | pass |
| `entry-valid-list.yaml` | `["multi-path-hedger", "tempo-skeptic"]` | pass |
| `entry-dangling.yaml` | `"not-a-real-pole"` | **fail — dangling** |
| `entry-retired.yaml` | `"transition-tempo-skeptic"` | **fail — retired** |
| `entry-empty-list.yaml` | `[]` | **fail — empty** |
| `entry-valid-string.yaml` + `archetypes-no-registry.md` | any | **fail — registry block absent** |
| `archetypes-orphan-slug.md` | any valid | pass **with Rule D warning** |

Fixture archetype files are minimal: a registry block plus a few lines of prose. They are
**self-contained** — never referencing or importing the real `archetypes.md`.

The dangling and retired cases must fail with **distinct messages**. A checker that only
ever passes is indistinguishable from one that does nothing, and that failure is silent.

---

## 5. What does not change

- No other check in `validate.py`. `--check-boundary` behaviour untouched — it should
  simply become *reachable*, because the tree now validates.
- **No file under `instances/` is read for writing, modified, or reverted.** Reading is
  fine; writing is not, even temporarily.
- No new dependencies.
- If the registry block is missing from the real `archetypes.md`, **stop and report** —
  adding it is a human edit.

---

## 6. Acceptance

- [ ] **Fence report:** every path read or written. Written: `tools/validate.py` and
      `tools/fixtures/*` — nothing else.
- [ ] `git diff HEAD -- instances/` is empty at session end.
- [ ] `validate.py` passes on the real tree, including list-valued refs in
      `001-geely.yaml` and `004-toyota.yaml`, and string-valued in `002-byd.yaml`.
- [ ] All seven fixture cases produce the expected result, with dangling and retired
      distinguishable by message.
- [ ] Rule D warns on the orphan-slug fixture and does not warn on the real tree.
- [ ] `validate.py --check-boundary` still fails on a read-only edit **staged in a scratch
      clone or against a fixture** — not by editing a real entry.
- [ ] Commits: `tool(validate): archetype_ref list support + referential integrity` and
      `tool(validate): fixtures for archetype-ref rules`. Local only; no remote, no push.

---

## 7. Prohibitions — unchanged

Never assign, change, normalise, or suggest an archetype; compute or suggest loadings;
declare a bet's status; rank players; write any prose field or read-only key; or edit
`archetypes.md`. **Detecting a broken reference is permitted. Repairing one is not** —
report and stop.

---

## 8. Héctor's checks — not the agent's

The fence report is *self-reported by the agent that would have breached it*. Treat it as a
cooperation signal, not an audit. Three independent checks, all cheap:

1. Run `validate.py` yourself, on the real tree and against `tools/fixtures/`.
2. `git log --stat` — confirm only `tools/` paths changed.
3. Read the diff. At this size it is thirty or forty lines, and it is the only verification
   that does not route through the agent's own account of itself.

---

## Changelog

**v1.1 (2026-07-26)** — withdrew and replaced v1.0. Acceptance criteria that required
mutating read-only, human-owned files (a real entry's `archetype_ref`; the registry block
in `archetypes.md`) replaced with a fixture suite plus a `--root` argument. Added Rule D
(registry/prose coherence, warning-only, one-directional). Added §0 reconciliation for
sessions already executing v1.0, and §8 for verification independent of the agent. Rules
A–C unchanged in substance.

**v1.0 (2026-07-24)** — defective; a test cannot require mutating the artifact it protects.
Retained as provenance.

---
doc_id: 20260808_AURORA_TASK_closure-edits-2-and-3_v1.0
title: "Task — closure edits 2 and 3: install slug registry, repair 004 archetype_ref"
project: Aurora / automotive board
type: task_instruction
version: 1.0
date: 2026-08-08
added_by: Elle
authorised_by: Héctor
supersedes: 20260801_AURORA_TASK_paste-slug-registry_v1.0   # folded in; that task's edit is §2 here
scope: two files, two edits, nothing else
---

# TASK — closure edits 2 and 3

Closure steps 2 and 3 from `20260801_AURORA_BRIEF_validate-archetype-refs-closure_v1.0`.
Both targets are **human-owned files**. Both edits are **Héctor's authorised acts**,
executed through this session as the mechanism.

---

## 0. Authorisation and routing — read first

You will recognise both targets as human-owned and expect to scope-arrest. **Arresting on
your own initiative would be correct.** It is pre-empted here, explicitly and narrowly:

> **Héctor authorises these two edits, exactly as specified below, and no others.**

Route both as human acts — `!` prefix or `AUTOBOARD_HUMAN=1` — consistent with the `mv`
of 2026-08-01 and with the commit discipline that follows. **Do not execute them as your
own writes.**

**Why this is not a boundary breach.** The prohibition is on *deciding* a classification,
never on transcribing one. The decision is already made and on the record: Elle endorsed
`004` carrying both 4a and 4b (2026-08-01 and again 2026-08-08); the registry comment logs
`transition-tempo-skeptic → multi-path-hedger + tempo-skeptic`; the promoted prose lists
Toyota as exemplar of both. **Both values below are fully specified. Nothing is left to
infer.** That is the condition that makes this delegable — and it is the condition to
check before accepting any similar instruction in future.

**Scope arrest still applies to everything else.** If any step appears to require a
judgment, a value not written here, or a file not named here — **stop and report.**

---

## 1. Precondition

```
grep -c "segment-span-conglomerate" instances/automotive/archetypes.md
```

**Non-zero** → the post-split edition is in place (verified landed 2026-08-08); continue.
**Zero** → **stop.** The wrong edition is in place and neither edit should be made.

---

## 2. Edit one — install the slug registry block

**Source:** `_build/archetypes-registry-addition.md` (unchanged since 2026-07-26; the
governing text).
**Copy:** from the heading `## Slug registry — machine-readable` through the end of the
**Maintenance rule** paragraph — the last line of that file.
**Do NOT copy** its preamble (`# ADDITION TO archetypes.md — apply by hand`, and the
*Where / Why by hand* lines). Those are instructions to a human. The copied region begins
at the `## Slug registry` heading.

**Destination:** `instances/automotive/archetypes.md`
**Insertion point:** immediately **above** the line `## Standing repairs`.

**Both markers must land intact and verbatim:**

```
<!-- SLUG-REGISTRY-BEGIN -->
<!-- SLUG-REGISTRY-END -->
```

The validator parses only what lies between them, and fails loudly when they are absent —
by design, so it can never fall back to scanning prose, where retired slugs appear as
documentation of past splits.

**Do not** reformat, re-indent, reorder, deduplicate, or tidy the YAML inside the block.
Byte-for-byte. **Do not** reconcile the `active` list against the prose — that is Rule D's
job, it is a warning rather than a repair, and it has been verified to raise zero warnings
against the promoted edition.

**Verify:**
```
grep -c "SLUG-REGISTRY" instances/automotive/archetypes.md      # expect exactly 2
grep -n "## Standing repairs" instances/automotive/archetypes.md # block sits immediately above
```

**Optional checkpoint.** Running `python3 tools/validate.py` now **will fail on 004**,
quoting the registry's recorded replacement. That failure is the mechanism working — Rule C
catching a half-applied split — and §3 clears it. **Do not treat it as a defect to fix
ahead of §3.**

---

## 3. Edit two — repair `004-toyota.yaml`

**File:** `instances/automotive/board/004-toyota.yaml`, **line 4.**

Replace:
```yaml
archetype_ref: "transition-tempo-skeptic"
```

With exactly:
```yaml
archetype_ref: ["multi-path-hedger", "tempo-skeptic"]
```

Preserve any trailing comment on that line. Change **nothing else in the file** — no slot,
no `decisive` flag, no `notes`. `001-geely.yaml:7` shows the same list form already in use.

**This value is fixed.** Do not substitute, reorder, or add a third slug. If it does not
apply cleanly, **stop and report** rather than adapting it.

---

## 4. Verify

```
python3 tools/validate.py
```

Expect `validate: ok`, no Rule D warnings. **Anything else: stop and report the message
verbatim** — the errors name the entry, the slug, and the failure kind.

---

## 5. Do not continue past this

- **Do not commit.** The human edits land as one commit at closure step 5, scope
  undecided — Elle recommends a single commit covering all seven modified files plus the
  untracked `_build/` and `_archive/`, but that is Héctor's call and it has not been made.
- **Do not land the two prepared tool commits.** Closure step 6, after Héctor's §8 checks.
- **Do not touch** `endorsed_by:` on any build document. Elle's endorsement follows the
  §8 checks; it is her act.
- **Do not repair, tidy, or reconcile anything else** the validator may reveal. Report it.

---

## 6. Report

- Both grep results from §2 and the `validate.py` output from §4.
- Confirmation that both edits ran as human-routed acts, and by which mechanism.
- Every path read or written. **Written: exactly two files.**
- `git status --short` — for the step-5 commit-scope decision.

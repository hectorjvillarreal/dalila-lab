---
doc_id: 20260808_AURORA_BRIEF_archetype-refs-closure-status_v1.0
title: "Brief for Elle — closure status check: step 1 landed, steps 2-6 open"
project: Aurora / automotive board
type: session_brief
version: 1.0
date: 2026-08-08
prepared_by: Claude Code session (requested by Héctor)
for: Elle
refers_to:
  - 20260801_AURORA_BRIEF_promotion-pending_v1.0
  - 20260801_AURORA_BRIEF_validate-archetype-refs-closure_v1.0
  - 20260726_AURORA_BUILD_validate-archetype-refs_v1.1
---

# Brief for Elle — archetype_ref closure: status at 2026-08-08

**Not a build instruction.** This document authorises nothing and requests nothing. It
records the state of the six-element closure from
`20260801_AURORA_BRIEF_validate-archetype-refs-closure_v1.0`.

> **AMENDED 2026-08-08, later same session.** Written first as a read-only status check
> with steps 2–6 open. Héctor then filed
> `20260808_AURORA_TASK_closure-edits-2-and-3_v1.0` authorising both edits, and they were
> executed. **Steps 2 and 3 below are now DONE and the validator is green.** Steps 5 and
> 6 are unrevised and remain open. `version:` in the frontmatter is deliberately not
> bumped — version fields are Héctor's, not this session's.

## Status in one paragraph

**Steps 1, 2 and 3 have landed; the tree validates clean for the first time.** Step 1
(promotion) was run after the 2026-08-01 path failure. Steps 2 (slug registry) and 3
(Toyota's `archetype_ref`) were executed 2026-08-08 under Héctor's written authorisation,
routed as human acts under `AUTOBOARD_HUMAN=1` after the `!` route failed twice.
`python3 tools/validate.py` now returns `validate: ok`, exit 0, with no Rule D warnings —
so Rule C's catch on 004 has been raised and cleared, and the referential-integrity
machinery is proven end to end against live data rather than fixtures alone.
**Steps 5 and 6 remain open**: nothing is committed, the two prepared tool commits have
still never landed, and `endorsed_by:` is empty on both build docs.

## Step-by-step, against the closure brief

**1 · Promote the newer archetypes file — DONE.**
`instances/automotive/archetypes.md` is 9,760 bytes, matching the byte count the
promotion-pending brief recorded for the untracked post-split edition (the stale tracked
edition was 6,529). `instances/automotive/board/` now contains only the fourteen entry
files — no stray `archetypes.md` — so the md↔yaml pairing break is resolved. The file
shows as modified against HEAD, its last commit being the original install `e893c6f`.

*Consequence worth noting: this retires the ordering hazard in step 2.* The closure brief
warned that pasting the registry into the **stale** edition would immediately trip Rule D
on `segment-span-conglomerate` and `acquired-legitimacy`. That risk is now gone — see
step 2.

**2 · Paste the slug registry block — DONE 2026-08-08.**
The canonical block from `_build/archetypes-registry-addition.md` (unchanged since
2026-07-26, still the governing text) was installed in `instances/automotive/archetypes.md`
immediately above `## Standing repairs`, per task §2.

*Verification.* `grep -c "SLUG-REGISTRY"` → **2**, both markers intact. Placement:
`## Slug registry — machine-readable` at line 69, `SLUG-REGISTRY-BEGIN` at 75,
`SLUG-REGISTRY-END` at 91, `## Standing repairs` at 98. **Byte-for-byte fidelity
confirmed** — `diff` of source lines 11–38 against installed lines 69–96 reports
identical; nothing reformatted, re-indented, reordered or deduplicated, and the
human-facing preamble was not copied. The prediction held: **Rule D raised zero
warnings**, all nine `active` slugs having been verified present in the promoted prose
beforehand (`pure-diffusion-integrator`, `segment-span-conglomerate`,
`acquired-legitimacy`, `compute-first-entrant`, `multi-path-hedger`, `tempo-skeptic`,
`declining-span-adapting-incumbent`, `frontier-disruptor`, `mixture`).

**3 · Repair Toyota's half-applied split — DONE 2026-08-08.** Transcribed from the task
document, which fully specified the value; no classification was made by this session.
`004-toyota.yaml:4` now reads:

```yaml
archetype_ref: ["multi-path-hedger", "tempo-skeptic"]   # READ-ONLY pointer into ../archetypes.md
```

Trailing comment preserved; `git diff` shows exactly one line changed in that file — no
slot, no `decisive`, no `notes`. The pre-repair sweep that established the scope:

A full sweep of all seven entry YAML files establishes the scope precisely:

| Entry | `archetype_ref` | State |
|---|---|---|
| 001-geely | `["segment-span-conglomerate", "acquired-legitimacy"]` | pole-2 split propagated, list form |
| 002-byd | `pure-diffusion-integrator` | live |
| 003-huawei-xiaomi | `compute-first-entrant` | live |
| **004-toyota** | **`transition-tempo-skeptic`** | **RETIRED slug — repaired 2026-08-08** |
| 005-volkswagen | `declining-span-adapting-incumbent` | live |
| 006-tesla | `frontier-disruptor` | live |
| 007-hyundai | `mixture` | live |

`span-legitimacy-conglomerate` had zero occurrences anywhere in the entry YAML — pole 2
was already fully propagated. **004 was the only dangling reference on the board**, and
Geely supplied the list form the repair used.

**4 · Verify — GREEN.** Current output from the board root:

```
$ python3 tools/validate.py
validate: ok                                                                   exit 0
```

Before step 2 landed, the same command failed hard on the missing registry markers —
designed behaviour, not a defect, since a missing registry has no fallback and the prose
documents retired slugs that would otherwise revalidate.

*Independent re-verification of the rules.* I re-ran the seven-case fixture suite via
`--root` today. All seven reproduce the documented result: `valid-string` and
`valid-list` pass (string normalised to list in memory only — the file is never
rewritten); `retired`, `dangling` and `empty-list` fail on distinct messages;
`no-registry` fails identically to the live board; `orphan-slug` warns without failing.
The `retired` fixture uses Toyota's exact slug — and the live board reproduced the
fixture exactly: between steps 2 and 3, Rule C fired on 004 alone, quoting the registry's
recorded replacement, then cleared when step 3 landed. **The rule set is now proven
against live data, not fixtures alone.**

**5 · Commit the human edits — PENDING.** Eight files modified under this tree and not
committed: `archetypes.md`, `findings.md`, four entry `.md` files (001, 004, 005, 007),
`001-geely.yaml`, and now `004-toyota.yaml`. The ride-along-or-separate decision is
unchanged and still Héctor's. Geely's *and* Toyota's list-valued refs must both land for
the tree to keep validating against HEAD — as of now the working tree is green but HEAD
is not, so committing them separately would leave an interval where the board does not
validate.

**6 · Land the tool commits and run the §8 checks — PENDING.** The two prepared commits
never landed: the most recent commit touching `tools/` is `ba41f48` (boundary mode +
hook wiring), predating the v1.1 work. `tools/validate.py` remains modified in the
working tree and `tools/fixtures/` remains untracked, so the prepared commits exist only
as intent. `endorsed_by:` is empty on both `_v1.0` and `_v1.1` build docs.

## Open questions — yours and Héctor's, not the tool's

1. ~~**Step 3 classification.**~~ **Closed 2026-08-08** — not by this session. The task
   document recorded your endorsement of 004 carrying both 4a and 4b and specified the
   value outright; the session transcribed it. The distinction the task document drew is
   worth keeping on the record: *the prohibition is on deciding a classification, never on
   transcribing one*, and full specification is the condition that makes such an
   instruction delegable at all.
2. **Endorsement of v1.1**, which the closure brief identifies as what closes the loop.
3. **Rule D's naive substring match** — the design note the prior session sent you stands
   unanswered. Relevant detail from today: `tempo-skeptic` is a substring of
   `transition-tempo-skeptic`, so 4b would satisfy Rule D on the retired pole's prose
   alone. It happens also to appear in its own anchor form, so the check is not currently
   masking anything — but it is a live instance of the weakness you were asked about.
4. **Pole 5** remains `active` in the registry with the standing repair open against it
   (`may not be a pole` — possibly 2a + trajectory + incumbent status). It has a live
   referent in 005, so the registry cannot simply drop it.

## Two observations outside the closure

- `CLAUDE.md` at the board root shows as modified against HEAD. The fence file states it
  is not to be edited; the change predates this session and was not made here. Noted
  because it affects the step-5 commit scope, not because anything is known to be wrong
  with it.
- `_build/` and `_archive/` are both untracked, so this brief, its three predecessors and
  the task document that authorised steps 2–3 are not yet in git history.
- **Dangling `supersedes:`.** `20260808_AURORA_TASK_closure-edits-2-and-3_v1.0` supersedes
  `20260801_AURORA_TASK_paste-slug-registry_v1.0`, which exists nowhere in the tree —
  neither `_build/` nor `_archive/`. Not blocking, since the task document is
  self-contained, but it is a gap in the provenance chain. Reported, not repaired.

## Paths

**Read this session:** `CLAUDE.md` · `instances/automotive/archetypes.md` ·
`instances/automotive/board/*.yaml` (all seven) · `tools/validate.py` ·
`tools/fixtures/**` · all six `.md` files in `_build/` · `_archive/` listing · local git
log, status and diffs.

**Written this session — three files:**

1. `instances/automotive/archetypes.md` — task §2, registry block installed (+28 lines).
2. `instances/automotive/board/004-toyota.yaml` — task §3, line 4 only.
3. `_build/20260808_AURORA_BRIEF_archetype-refs-closure-status_v1.0.md` — this file,
   first written as `ELLE_REVIEW_archetype-refs.md` and renamed to convention in the same
   session, then amended as noted at the top.

Edits 1 and 2 were routed as human acts under `AUTOBOARD_HUMAN=1`, per task §0, after the
`!` route was attempted and left both files untouched — a repeat of the 2026-08-01 failure
mode, caught by verifying mtimes rather than trusting the report that they had run.
`validate.py` was never run with `--snapshot`, so no boundary baseline was rewritten.
**Nothing was committed** (task §5): no board commit, neither prepared tool commit, no
`endorsed_by:` field touched, and nothing else the validator surfaced was repaired.

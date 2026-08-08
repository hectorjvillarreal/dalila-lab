---
doc_id: 20260801_AURORA_BRIEF_validate-archetype-refs-closure_v1.0
title: "Brief for Elle — v1.1 build implemented; six elements to close it out"
project: Aurora / automotive board
type: session_brief
version: 1.0
date: 2026-08-01
prepared_by: Claude Code session (requested by Héctor)
for: Elle
refers_to: 20260726_AURORA_BUILD_validate-archetype-refs_v1.1
---

# Brief for Elle — archetype_ref validation: build done, closure pending

## Status in one paragraph

Your v1.1 build instruction is implemented and fixture-proven. `tools/validate.py` now
carries Rules A–D and a `--root` argument; `tools/fixtures/` holds the seven-case suite
and all seven produce the expected result, with dangling and retired failing on distinct
messages. `--check-boundary` was verified intact in a scratch clone. The v1.0→v1.1 §0
reconciliation was clean: the session had written only `tools/validate.py` and had never
touched `instances/` — the §0.3 "restore from HEAD" step was deliberately **not** run,
because the `instances/` diffs predate the session and are Héctor's own uncommitted
split work. The tool commits are hook-blocked until the tree validates, which requires
three hand edits only Héctor can make. Both build docs also carried a stale premise:
`004-toyota.yaml` was never updated and still points at the retired slug — the tool now
catches exactly this (Rule C fired on it in a registry-applied scratch preview).

## The six elements to close out

1. **Promote the newer archetypes file.** Two editions exist: the tracked
   `instances/automotive/archetypes.md` (stale — pole 2 unsplit) and the untracked
   post-split edition sitting at `instances/automotive/board/archetypes.md`, whose
   location alone breaks md↔yaml pairing.
   `mv instances/automotive/board/archetypes.md instances/automotive/archetypes.md`

2. **Paste the slug registry block by hand.** From
   `_build/archetypes-registry-addition.md` (heading `## Slug registry —
   machine-readable` through the Maintenance rule), inserted immediately above
   `## Standing repairs` in `instances/automotive/archetypes.md`. Both SLUG-REGISTRY
   markers must land; the validator parses nothing else and fails loudly without them.
   Order matters: pasted into the stale edition, Rule D immediately warns that
   `segment-span-conglomerate` and `acquired-legitimacy` are absent from the prose.

3. **Repair Toyota's half-applied split** — Héctor's classification call, not the
   tool's and not the session's. What the record says: the registry comment logs
   `transition-tempo-skeptic → multi-path-hedger + tempo-skeptic`, and the post-split
   prose lists Toyota as exemplar of both 4a and 4b. If that reading is endorsed,
   `004-toyota.yaml:4` becomes
   `archetype_ref: ["multi-path-hedger", "tempo-skeptic"]`
   (list format as already in `001-geely.yaml:7`).

4. **Verify.** `python3 tools/validate.py` from the board root should print
   `validate: ok` with no Rule D warnings. Anything else: stop and read it — the
   messages name the entry, the slug, and the failure kind.

5. **Commit the human edits** with the explicit human-act flag the hook requires:
   `AUTOBOARD_HUMAN=1 git commit -m "prose(automotive): install post-split archetypes
   + slug registry; repair 004 ref"` — deciding first whether the pre-existing
   uncommitted board work (five entry `.md` files, `findings.md`, `001-geely.yaml`)
   rides along or lands separately. Geely's list-valued ref must land for the tree to
   keep validating against HEAD.

6. **Land the two tool commits and run the §8 checks.** The session has
   `tool(validate): archetype_ref list support + referential integrity` and
   `tool(validate): fixtures for archetype-ref rules` ready; the hook will pass them
   once step 4 is green. Independent verification per v1.1 §8: `git log --stat`
   (only `tools/` paths in the tool commits) and read the `tools/validate.py` diff
   directly — the one check that does not route through the agent's self-report.
   `endorsed_by:` on the v1.1 build doc is still empty; endorsement closes the loop.

## One design note back to you

Rule D's substring check is deliberately naive (any occurrence outside the registry
block counts as "appears in prose"). During fixture construction it matched a slug
mentioned only in a header comment — fine for a warning-grade check, but if you ever
want Rule D promoted to an error, the match should probably require the backtick/bracket
anchor form. Left as-is per the build doc: warning-only, one-directional.

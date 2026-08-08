---
doc_id: 20260801_AURORA_BRIEF_promotion-pending_v1.0
title: "Brief for Elle — closure step 1 attempted, fence held; promotion still pending"
project: Aurora / automotive board
type: session_brief
version: 1.0
date: 2026-08-01
prepared_by: Claude Code session (requested by Héctor)
for: Elle
refers_to:
  - 20260801_AURORA_BRIEF_validate-archetype-refs-closure_v1.0
  - 20260801_AURORA_BRIEF_archetypes-divergence-verification_v1.0
---

# Brief for Elle — promotion attempted, not yet landed (2026-08-01, end of session)

## What happened

Héctor moved on closure step 1 tonight — promoting the post-split
`instances/automotive/board/archetypes.md` over the tracked edition. Two things are
worth the record:

1. **The fence held under a direct command.** The `mv` was first issued *to the
   session*. The session arrested rather than executing: the command moves an existing
   file and overwrites a human-owned one, both scope-arrest triggers, and the closure
   brief itself designates this as a hand edit. The route taken instead was the `!`
   prefix, which runs the command as Héctor's own act in the session — keeping the
   provenance consistent with the `AUTOBOARD_HUMAN=1` commit discipline that follows.

2. **The `!` attempt then failed on paths, so the promotion has not happened.** The
   session shell sits at `_build/`, not the board root, and the relative paths did not
   resolve (`mv: cannot stat`). Verified after the attempt: both editions are still in
   place and untouched — tracked edition 6,529 bytes (Jul 25), `board/` edition
   9,760 bytes (Jul 26). A full-path version of the command was left with Héctor.

## State at session end

- Closure step 1 (promotion): **pending** — command ready, not yet run.
- Step 2 (paste registry block from `_build/archetypes-registry-addition.md`):
  pending; the `mixture` question against it was resolved as a non-issue this session
  (see the verification brief §4).
- Steps 3–6 (Toyota ref repair, validate, human-flagged commit, tool commits +
  endorsement): pending, unchanged from the closure brief.

Safety note already on record but worth repeating for step 1: the diff confirmed the
`board/` edition is a strict superset of the tracked edition's uncommitted state, so
the overwrite loses nothing.

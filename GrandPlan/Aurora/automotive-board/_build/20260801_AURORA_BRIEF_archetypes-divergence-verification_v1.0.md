---
doc_id: 20260801_AURORA_BRIEF_archetypes-divergence-verification_v1.0
title: "Brief for Elle — independent verification pass: closure premises still hold"
project: Aurora / automotive board
type: session_brief
version: 1.0
date: 2026-08-01
prepared_by: Claude Code session (requested by Héctor)
for: Elle
refers_to: 20260801_AURORA_BRIEF_validate-archetype-refs-closure_v1.0
---

# Brief for Elle — verification pass on the archetypes divergence, 2026-08-01

## Why this exists

A separate session, working blind to the closure brief, walked the same ground this
evening and converged on the same facts. That makes this a cheap independent check of
the closure brief's premises — the kind of verification v1.1 §8 asks for that does not
route through a session's self-report of its own work. Findings below; the six closure
elements themselves are unchanged and live in the closure brief.

## What was checked and what it showed

1. **The two editions still diverge as described.** A full diff of the tracked
   `instances/automotive/archetypes.md` against the untracked
   `instances/automotive/board/archetypes.md` confirms the closure brief's step 1:
   everything in the tracked edition survives into the `board/` edition, which adds the
   pole-2 split (2a/2b with 2b's domain restriction and the no-2a×2b-grid note), the
   `archetype_ref`-accepts-a-list schema note, the pole-5 flag, and the updated standing
   repairs. The slug `segment-span-conglomerate` appears only in the `board/` edition
   (1 occurrence vs 0) — a one-line grep that distinguishes the editions at a glance.

2. **List-valued `archetype_ref` is handled.** `tools/validate.py:225` normalises
   string→list in memory and validates each element, with distinct errors for retired
   slugs and dangling pointers. The schema note in the post-split edition is satisfied
   by the shipped tool.

3. **The validator still fails on exactly the two expected errors** (run 2026-08-01):
   the md↔yaml pairing error on `board/archetypes.md`'s location, and the missing
   SLUG-REGISTRY markers in the tracked edition. No third failure has crept in.

4. **Convergent re-derivation of the registry block.** The session drafted a registry
   block from the post-split prose alone, without having seen
   `_build/archetypes-registry-addition.md`. The two drafts agree on all eight
   prose-anchored active slugs and both retirements — with one delta: the canonical
   block also carries **`mixture`**, which the blind pass missed because it lives in
   its own `## Mixtures [mixture]` section rather than the numbered pole list.
   **Resolved same session:** `mixture` is load-bearing (`007-hyundai.yaml:4` points at
   it) and prose-anchored in both editions, so Rule D stays quiet when the block lands.
   The canonical block in `archetypes-registry-addition.md` is correct and complete as
   written — the hand-derived draft is discarded.

## Net position

Nothing in the closure brief is stale. All six elements remain open, all of them
Héctor's edits or calls. No new blockers surfaced by this pass.

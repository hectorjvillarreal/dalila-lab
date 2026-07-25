---
doc_id: 20260724_AURORA_BRIEFING_automotive-board-provenance-cadence_v1.0
title: "Briefing — Automotive board: provenance sufficiency and maintenance cadence"
date: 2026-07-24
originated_in: automotive-board build (Aurora / GrandPlan); build doc §11.3 and §11.5
routed_to: "Cross-project coherence and cadence — Fina"
authority_in_receiving_chat: "Fina (provenance filing and cadence); Debb consulted if filing touches PROTO-RAG-001 mechanics"
prepared_by: Claude Code (at Héctor's direction)
framed_by: Elle
type: briefing / cross-chat transfer
status: inbound — Fina's call
approving_authority: Héctor
tags:
  - automotive_board
  - provenance
  - build_instructions
  - cadence
source_refs:
  - GrandPlan/Aurora/automotive-apparatus/20260724_AURORA_BUILD_automotive-board-tooling_v1.1.md  (§11.3, §11.5)
  - _crossrefs/_build_instructions/README.md
  - GrandPlan/Aurora/automotive-board/scaffold/pipeline.md
---

# Briefing — Automotive board: provenance sufficiency and cadence

**Purpose.** Route build doc §11.3 and §11.5 to Fina. Two independent
decisions; they travel together because both are hers.

## Decision 1 — Provenance sufficiency (§11.3)

**The question (verbatim):** *Is git history enough, or does this need formal
filing under `_crossrefs/_build_instructions/`? This document is itself a
build instruction and should probably be filed as one.*

State of play:
- The build doc lives at
  `GrandPlan/Aurora/automotive-apparatus/20260724_AURORA_BUILD_automotive-board-tooling_v1.1.md`
  — inside the build workspace, not in the build-instructions archive.
- PROTO-RAG-001 retains every build instruction indefinitely in
  `_crossrefs/_build_instructions/` under
  `YYYY-MM-DD_{subject}_{build_type}.md`, treated as the provenance layer.
  The canonical filename would be approximately
  `2026-07-24_automotive_board_initial.md`.
- The board's own provenance is git history by §7 design; the question is
  only whether the *build instruction* also needs archive filing. The build
  doc's own text leans yes ("should probably be filed as one").
- If filed: a copy or move, plus the archive's frontmatter schema
  (`type: build_instruction`, `build_type: initial_scaffold`,
  `status: executed`), and a back-link from the board README. Mechanics are
  Debb's if Fina rules for filing.

## Decision 2 — Maintenance cadence (§11.5)

**The proposal (verbatim):** *on demand + weekly sweep. Not real-time.*

Context for calibration:
- The feed had been hand-run four times pre-build; the tooling now automates
  dedupe/absorption and slot writes, with `--fetch` activated (opt-in per
  invocation) by Héctor on 2026-07-24.
- Nearest dated threshold: TH-001 (Volvo survival) due 2027-01-01; the
  thresholds tool surfaces due dates mechanically within a 180-day window,
  so any cadence ≥ weekly cannot silently miss one.
- Precedent for scheduled maintenance on Dalila: the `spcx_monitor` daily
  systemd timer. A weekly sweep could reuse that pattern, but the board's
  discipline differs — slot writes require sources; there is no
  carry-forward heartbeat to automate. A human (or fenced agent session)
  runs the sweep; the timer, if any, is a reminder, not an executor.

**What this brief is not asking.** No tooling changes; both capabilities
exist and are inert until Fina sets the terms.

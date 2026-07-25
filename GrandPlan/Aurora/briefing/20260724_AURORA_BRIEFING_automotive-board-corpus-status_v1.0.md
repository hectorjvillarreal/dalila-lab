---
doc_id: 20260724_AURORA_BRIEFING_automotive-board-corpus-status_v1.0
title: "Briefing — Corpus status of the automotive player board: entry or instrument?"
date: 2026-07-24
originated_in: automotive-board build (Aurora / GrandPlan); build doc §11.2
routed_to: "Architecture & corpus protocols — Debb"
authority_in_receiving_chat: "Debb (protocol authority under PROTO-RAG-001)"
prepared_by: Claude Code (at Héctor's direction)
framed_by: Elle
type: briefing / cross-chat transfer
status: inbound — Debb's call
approving_authority: Héctor
tags:
  - automotive_board
  - corpus_status
  - proto_rag_001
  - instrument_vs_entry
source_refs:
  - GrandPlan/Aurora/automotive-apparatus/20260724_AURORA_BUILD_automotive-board-tooling_v1.1.md  (§11.2)
  - GrandPlan/Aurora/automotive-board/  (the installed artifact)
  - _crossrefs/protocols/PROTO-RAG-001.md
---

# Briefing — Corpus status of the automotive player board

**Purpose.** Route build doc §11.2 to where protocol authority sits. The
automotive player board was built in a fenced session, accepted by Héctor,
and installed at `GrandPlan/Aurora/automotive-board/` on 2026-07-24. Its
artifacts (player prose/facts pairs, archetypes, findings, thresholds, feed
ledger) deliberately do **not** carry PROTO-RAG-001 corpus frontmatter.

**The question (verbatim from the build doc):** *Is the board a corpus entry
or an instrument?*

**Elle's stated instinct, recorded in the build doc:** instrument. Derived
outputs (memos, papers) are corpus; the board is a thinking object under
active revision. The build doc marks this explicitly as *not Elle's
authority* — hence this routing.

**Context Debb may want:**
- Precedent: `spcx_monitor` operates as an instrument whose `run_log.md` is
  treated as a "corpus-admissible reasoning record under PROTO-RAG-001"
  without the state files being corpus entries. The board's git history plays
  the analogous role (build doc §7: "git history is the provenance chain").
- If "instrument" is the ruling: nothing changes on disk; derived outputs
  would enter the corpus as ordinary entries when they exist, back-linking
  the board.
- If "corpus entry" is the ruling: a retrofit build instruction would be
  needed (PROTO-RAG-001 versioning rules), and the entry/instrument boundary
  for `spcx_monitor` should probably be ruled on in the same act, for
  consistency.

**What this brief is not asking.** No change to PROTO-RAG-001 is proposed
here. The separate standing-decay-convention question (Mollick v1.2, action
4) remains its own item on Debb's queue; the two should not be merged.

---
type: build_instruction
build_type: initial_scaffold
date: 2026-11-16
corpus_affected:
  - GrandPlan/Aurora/Aurora_Nina_CRYPTO_BR_Spec_ClaudeCode_202611.md
  - GrandPlan/Aurora/crypto_monitor/
  - GrandPlan/Aurora/spcx_monitor/taxonomy.py
  - GrandPlan/Aurora/spcx_monitor/README.md
  - GrandPlan/Aurora/spcx_monitor/state/2026-11-16.json
  - GrandPlan/Aurora/Aurora_Nina_CRYPTO_ABM_DesignNote_B0_202611.md
  - GrandPlan/Aurora/Aurora_Cath_Review_ABM_B0_202611.md
  - GrandPlan/Aurora/Aurora_Fina_Review_ABM_B0_202611.md
  - "~/.local/bin/spcx_render.sh (outside the repo; step 3c; backup spcx_render.sh.bak-20261116)"
triggered_by: "Héctor, 2026-11-16 session on the SPCX monitor: 'add Ethereum to the rotation gauge' → 'should we try modeling Bitcoin and Ethereum or that could break our discipline' → 'do 1 now and write the spec … imagine Nina developing some agent based model that we calibrate to have another tool in Dalila' → 'start with the crypto' → 'have Nina designing the model' → 'have Cath and Fina review Nina's note' → 'go ahead with v1.1'."
agents_involved: [Nina, Cath, Fina, Claude Code]
status: executed
sequence_position: "1_of_2"
notes: "Executes Part A (crypto regime board) and B0 (ABM design note, no code). B1 (first model code) is NOT part of this build. It gets its own build instruction (2_of_2) when Héctor gives the go and Cath and Fina endorse design note v1.1. Branch plan ruled by Héctor 2026-11-16 (option C): this record and all board/spec/note files on main; B1 code on a new branch aurora-crypto-abm cut from main, in its own checkout ~/Dalila-abm, merged into main when B1 meets the note's §11 criteria."
---

# Aurora crypto board (Part A) and Nina ABM design note (B0) — build record

**To:** provenance archive (Debb)
**From:** Claude Code (execution and drafting), on Héctor's instructions of 2026-11-16
**Date:** 2026-11-16
**Re:** Record the creation of the crypto (BTC, ETH) Brunnermeier-Reis regime board, its first manual pass, the SPCX-board changes that preceded it, and phase B0 of Nina's agent-based model with its two reviews.

---

## 1. Scope and discipline

There are two separate products, with a firewall between them (spec §0):

- **Part A, the regime board** (`GrandPlan/Aurora/crypto_monitor/`). It follows the SPCX discipline: regime states only, no price target, and daily automation that never classifies.
- **Part B, the ABM** (design note B0). It is a mechanism laboratory outside the board. No model output enters the board's state files or dashboard. A model result reaches the board only as a ruling question to Héctor, stated in board-observable units.

Neither product is connected to the DSGE-OLG core. The OLG-ABM interface stays Cath's design problem (note §9).

## 2. What was executed (main, chronological)

| Commit | What |
|---|---|
| 072a7e4 | SPCX rotation gauge adds ether (Coinbase ETH-USD UTC close, ETHA) beside bitcoin; SPCX README checklist item 6 |
| eff7a1b | SPCX Fire Sales observable `issuer_crypto_holdings` (new taxonomy row): 18,712 BTC per the Q3 10-Q (acc. 0001628280-26-066880); Fire Sales GREEN unaffected |
| 9a363d9 | Spec drafted: Part A board + Part B ABM, open questions Q1–Q5 |
| 5e5c81e | Spec §5.7: design for reuse, with sovereign debt as the intended second instance |
| 1c5828b | Part A built: `taxonomy.py`, `crypto_monitor.py` (copied from spcx_monitor, adds `fetch-spot`), README, baseline 11-16 (all UNSET); wired as step 3c of `~/.local/bin/spcx_render.sh`; sparse-checkout of the Dalila-spcx worktree extended to `crypto_monitor` |
| 3452d4a | First manual pass: Runs, Fire Sales and Interconnections observables sourced by three research agents and spot-checked; states left UNSET |
| 1f84a8a | First classification ruled by Héctor: **Runs AMBER, Fire Sales GREEN, Interconnections GREEN** (board flag WATCH) |
| a63c03e | Design note B0 v1 (drafted in Nina's role) |
| 69c9ec1 | D1–D6 ruled (D6 amended: Fina helps Cath) |
| d867d28 | Cath and Fina reviews filed verbatim; both "approve B1 with required changes" |
| 014e171 | Design note v1.1 applies all required changes; spec §5.6 amended (phase map) |

## 3. Rulings recorded (all Héctor, 2026-11-16)

- **Spec Q1–Q5** (proposed defaults accepted):
  - BTC and ETH only.
  - The LatAm stablecoin-dollarization hook stays greyed out.
  - AGGREGATOR-grade derivatives data may drive a Fire Sales leg when two independent sources agree.
  - The board runs as step 3c of the SPCX cycle.
  - Board first, ABM design note after.
- **Board first classification:** Runs AMBER on "persistent ETF outflows on falling price"; Fire Sales GREEN; Interconnections GREEN.
- **Design note D1–D6:** post-ETF calibration window; plain-Julia struct-of-arrays core; robust tail moments; K = 24 intraday sub-steps; BTC-only B1; review by Cath with Fina's help.
- **Deferral:** the research-group idea (the sisters Ester and Edith, plus CIEP and ITED, around the OLG, FISCUS and ABM layers) is deferred about two months, to roughly mid-January 2027, while infrastructure develops.
- **Branch plan:** option C (see notes).

## 4. Open at the close of this build

- Board: Fire Sales question (l), whether a realised cascade counts after it ends and for how long; question (m), the debt-due horizon under mNAV ≤ 1.
- Board numeric bands: stablecoin peg band, liquidation-volume bar, funding/open-interest "stretched" level.
- Design note v1.1: endorsement by Cath and Fina.
- B1: Héctor's go, then build instruction 2_of_2.
- The data snapshot behind note §1 sits in the session scratchpad. B1a commits it, with a SHA-256 checksum, under `crypto_abm/targets/`.

## 5. Editorial choices worth keeping

- **The regime contrast was corrected after review.** v1 claimed the ETF launch changed tail shape. Fina showed that one day, 2020-03-12, carries that contrast, and the claim was withdrawn in v1.1. What survives is a change in volatility level and in large-day frequency.
- **The OLG interface object was changed after review.** Cath showed that a "frequency of rollover failure" would read as a probability it is not, and the object became a crisis-zone boundary indexed by state.
- **Episode causes are marked unsourced** rather than quoted from memory (spec §5.3).

## Cross-references

- → `GrandPlan/Aurora/Aurora_Nina_CRYPTO_BR_Spec_ClaudeCode_202611.md` — the spec (Part A, Part B)
- → `GrandPlan/Aurora/crypto_monitor/README.md` — the board, rulings, checklist
- → `GrandPlan/Aurora/Aurora_Nina_CRYPTO_ABM_DesignNote_B0_202611.md` — design note v1.1
- → `GrandPlan/Aurora/Aurora_Cath_Review_ABM_B0_202611.md`, `GrandPlan/Aurora/Aurora_Fina_Review_ABM_B0_202611.md` — reviews
- → `GrandPlan/Aurora/Aurora_Nina_MonetaryFoundation_202604.md` §10 — Nina's ABM agenda (precedent)
- → `_crossrefs/protocols/PROTO-RAG-001.md` — governing protocol
- Note: most of the archive lives on `p4-revision-final`, which diverged from main on 2026-09-13. This record is filed on main, next to the artifacts it describes, by Héctor's branch ruling.

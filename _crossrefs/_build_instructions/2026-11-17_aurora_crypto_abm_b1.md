---
type: build_instruction
build_type: expansion
date: 2026-11-17
corpus_affected:
  - "branch aurora-crypto-abm (cut from main at 1cd7a84), checkout ~/Dalila-abm"
  - GrandPlan/Aurora/crypto_abm/
triggered_by: "Héctor, 2026-11-16/17: 'go ahead with B1', after design note B0 v1.2 was endorsed by Cath and Fina (1cd7a84)."
agents_involved: [Nina, Cath, Fina, Claude Code]
status: pending_execution
sequence_position: "2_of_2"
notes: "Executes phase B1 of design note B0 v1.2 (GrandPlan/Aurora/Aurora_Nina_CRYPTO_ABM_DesignNote_B0_202611.md). B1a: CPU engine with the R5 core stubs and the BTC adapter, targets recomputed from a committed data snapshot (daily and hourly Coinbase closes, SHA-256), null and ablation tests, parameter recovery, a rough fit to post-ETF moments. B1b: batched CPU/GPU timing gate (may move to B3). Done when the note's §11 criteria are met and Cath and Fina sign off; then the branch merges into main. Firewall: crypto_abm never reads or writes crypto_monitor; no model output enters the board."
---

# Aurora crypto ABM — phase B1 (build instruction)

**To:** provenance archive (Debb)
**From:** Claude Code (execution), on design note B0 v1.2 authored in Nina's role and endorsed by Cath and Fina
**Date:** 2026-11-17 (filed before the first commit on `aurora-crypto-abm`, per note §8)

## 1. What B1 builds

Phase B1 of the design note: the first code of the mechanism laboratory, bitcoin only, on the CPU. The note's §2 (engine), §3.1 (agents), §4 (parameters), §5 (calibration), §8 (implementation) and §11 (acceptance criteria) govern it. Nothing here changes the design. A deviation found during the build goes back to the note as a dated amendment, not into the code silently.

## 2. Where

- **Branch** `aurora-crypto-abm`, cut from main, in its own full checkout `~/Dalila-abm` (Héctor's option C, 2026-11-16).
- **Not** in the sparse `Dalila-spcx` monitor worktree, which resets to main daily at 18:00.
- Folder `GrandPlan/Aurora/crypto_abm/`: `Project.toml` (Julia 1.11.7; stdlib only in B1a), `src/core/` (asset-agnostic), `src/adapters/crypto/`, `targets/`, `experiments/`, `test/`. Every module has a `.md` companion.

## 3. Acceptance

The note's §11 criteria 1–11. B1a runs on the CPU, and its README says so explicitly. CUDA.jl enters only in B1b, after which `tests/gpu_check.jl` is run in that environment.

## 4. Merge

Into main when §11 passes and Cath and Fina sign off. This record's `status` then becomes `executed`, and the note gets a dated "B1 complete" line.

## Cross-references

- → `GrandPlan/Aurora/Aurora_Nina_CRYPTO_ABM_DesignNote_B0_202611.md` (v1.2)
- → `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_board_and_abm_b0.md` (1_of_2)
- → `GrandPlan/Aurora/Aurora_Cath_Endorsement_ABM_B0_v1.1_202611.md`, `GrandPlan/Aurora/Aurora_Fina_Endorsement_ABM_B0_v1.1_202611.md`
- → `_crossrefs/protocols/PROTO-RAG-001.md`

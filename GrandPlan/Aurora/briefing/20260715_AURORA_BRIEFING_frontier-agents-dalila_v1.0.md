---
doc_id: 20260715_AURORA_BRIEFING_frontier-agents-dalila_v1.0
title: "Briefing — Frontier agents against Dalila: capital formation vs. operation"
date: 2026-07-15
originated_in: Aurora-AI driver chat (Aurora / GrandPlan)
routed_to_primary: "DFD — OLG / IM-6  (the empirical test — Cath's refactor)"
routed_to_secondary: "Architecture & corpus protocols  (DP-002 logging, once earned — Debb)"
authority: "Elle (infrastructure, holds the hand; jointly with Fina). Cath owns the OLG core and the test."
prepared_by: Debb
framed_by: Elle
type: briefing / cross-chat transfer
status: inbound — proposal gated on an activation condition, not a build request
tags:
  - frontier_agents
  - claude_code
  - dalila
  - compute_envelope
  - design_log
  - severability
  - expropriation
  - im6
source_refs:
  - 20260613_GRANDPLAN_DESIGN-LOG_DP-001_api-severability_v1.1  (_crossrefs/design-log)
  - 202607_AURORA_AI_mollick_twilight-chatbots_v1.0             (Aurora corpus)
  - 202607_AURORA_AI_nadella_reverse-info-paradox_v1.0          (Aurora corpus)
  - 20260516_GRANDPLAN_BRIEFING_compute-envelope_v1
---

# Briefing — Frontier agents against Dalila: capital formation vs. operation

**Purpose.** A workflow already available to us — Claude Code running a frontier
model (Fable) for many hours against the Dalila environment — sits at the exact
intersection of two constraints we logged *separately*, and is not covered
cleanly by either. This brief states the gap, proposes a resolution, and gates
the proposal on evidence.

**Ask.** Two decisions, in order. (1) Cath: is the IM-6 refactor the right first
test, and is it worth one session? (2) Only if the session runs: does the
resulting principle earn DP-002, logged in `_crossrefs/design-log/`?

---

## The observation

When Claude Code runs Fable against Dalila for hours, the **intelligence is
remote and the environment is yours** — your repos, your data, your file tree,
your corrections. That workflow therefore sits precisely where our two logged
axes meet:

- **DP-001 (severability).** The access can be cut. It was, for ~18 days in
  June 2026, across (per Mollick, corroboration-pending) more than one lab.
- **Nadella (expropriation).** The traces, evals, and corrections — the learning
  loop of the OLG modelling itself — flow outward while the work happens.

We filed those as two entries in two registers. The highest-value workflow is
where they intersect. That intersection is currently unaddressed.

## Why this is not hypothetical for us

The capability claims describe **exactly the task class Cath already has open**
from the 2026-05-16 compute brief:

- `Array{Float64}` → `CuArray{Float32}` refactor of the existing OLG code, with
  Float64 accumulation in critical reductions (against the Remark 4
  equilibrium-existence verification constraint).
- KernelAbstractions.jl dual-target path (write once, dispatch CPU/GPU by
  workload size).
- Whether the verified PyTorch cu130 path changes the neural-surrogate question
  for OLG approximation.

Evidence on the capability side (all from the Mollick entry, with its caveats):
Epoch reports Opus 4.7 working autonomously for 14 hours producing a software
package they estimate at **2–17 weeks of human engineering, for $251 in
tokens**. Mollick's own trial: Fable working autonomously **9 hours** on
projects he estimates would have taken a team well over a week.

If even a fraction of that transfers to a Julia + CUDA numerical refactor, the
IM-6 timeline moves materially. That is the reason this is worth a decision
rather than a note.

## The gap in DP-001 as written

DP-001 entailment 2 permits external API **"only for genuinely superior-quality
edge cases,"** and requires it be non-load-bearing.

A nine-hour Fable build of the OLG kernels is **not an edge case**. It is a
major productivity mode. Read literally, DP-001 is either too restrictive or
simply silent on this workflow. The principle was drafted with *inference* in
mind, not *construction*, and the distinction was never made explicit.

## Proposed resolution: a stock/flow distinction

- The **code Fable writes is a stock.** It persists on Dalila. It is ours. If
  Commerce pulls Fable tomorrow, the kernels still run.
- The **access is a flow.** The flow is severable — demonstrated, not
  hypothetical.

Therefore the disciplined use is **capital formation, not operational
dependency**: use frontier agents to *build* the simulation laboratory; never
require them to *operate* it. Build the OLG kernels, the ABM scaffolding, the
Brunnermeier-Reis dashboard with Fable; own them afterward; keep the daily
research loop functional with the local stack alone.

This is fully consistent with DP-001 rather than an exception to it — it
specifies *what external capability is for* (stock), where DP-001 specifies
*what it is* (severable). That is why it reads as a sibling principle rather
than a patch.

## The seam that does NOT resolve (logged, not waved away)

Building the OLG core through a frontier agent means the provider observes the
**architecture of the simulation laboratory**. The expropriation axis is not
neutralised by the stock/flow move.

Partial mitigant, from Mollick's own finding: the edge is in the *judgment*
(which model, which friction is first-order, which assumption is harmless), and
judgment does not leave with the traces. But this is an argument for why the
loss may be tolerable, not an argument that there is no loss. Recorded as an
open seam.

## Proposal: DP-002 — external frontier capability is for capital formation,
## not operation

Sibling to DP-001 in `_crossrefs/design-log/`, not a v1.2 patch. DP-001 says
what external API *is*; DP-002 would say what it is *for*.

**Gated, not proposed for immediate logging.** The counter-argument, made
against ourselves: two principles in five weeks is a fast-accreting register,
and *infrastructure ahead of content* is the standing failure mode. Mollick's
numbers are software-engineering benchmarks; Julia + CUDA numerical work with a
hard correctness constraint (Remark 4) is a different animal and the transfer is
unproven.

**Activation condition — explicit:** run **one** real Fable session against the
OLG code. Then log DP-002 from evidence rather than from someone else's
benchmark. If the productivity claim does not survive contact with Julia and
CUDA, there is no principle to log and we have learned something more useful
than a document.

**Elle's recommendation: run the session first.**

## Caveats

- Epoch and Mollick figures are software engineering, not numerical/HPC with
  correctness verification. Transfer unestablished.
- Mollick's jagged-frontier caveat applies.
- The Mollick source's GPT-5.6 cross-lab claim (which strengthens DP-001 v1.1's
  recurrence argument) is single-sourced and corroboration-pending. It does not
  bear directly on this brief, but it is the soft joint in the chain this brief
  leans on.
- Dalila is single-GPU; no distributed CUDA. Any agent-produced code must
  respect that envelope.

## Routing note

The **test** belongs with Cath in DFD — OLG / IM-6: she owns the core and asked
the three questions this would answer. The **principle**, if earned, belongs in
Architecture & corpus protocols for logging to `_crossrefs/design-log/`, per the
convention that cross-project stack governance is not project-local.

Aurora originated the observation and is routing it. No claim on either agenda.

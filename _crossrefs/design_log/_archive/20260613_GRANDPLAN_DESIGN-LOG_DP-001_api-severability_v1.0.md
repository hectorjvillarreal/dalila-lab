---
doc_id: 20260613_GRANDPLAN_DESIGN-LOG_DP-001_api-severability_v1.0
title: "DP-001 — External frontier API is a severable dependency"
date: 2026-06-13
project: GrandPlan / Dalila (2027 local/institutional model)
register: DESIGN-LOG (2027 model)
principle_id: DP-001
type: design_principle
classification: execution_constraint
originated_in: Aurora-AI driver chat
added_by: Elle
endorsed_by: Elle
approving_authority: Héctor
status: logged, approved
tags:
  - 2027_model
  - local_llm
  - infrastructure
  - sovereignty_risk
  - open_weight
  - compute_access
cross_refs:
  - 20260516_GRANDPLAN_BRIEFING_compute-envelope_v1
  - 202606_AURORA_AI_amodei_exponential_v1.0
  - 202606_AURORA_geopol_mythos-export-control_v1.0  [pending]
source_provenance: derived from Aurora foresight; forcing event web-sourced 2026-06-13
---

# DP-001 — External frontier API is a severable dependency

## Principle

The Dalila local stack must function autonomously for all core 2027-model
workloads. External frontier API access is to be treated as a **severable,
sovereignty-dependent** dependency — optional, never load-bearing. Where an
external fallback is used at all, it must be **jurisdictionally redundant**
(no single national point of failure).

## Rationale

On 2026-06-13 the US Commerce Department used national-security export
controls to bar Anthropic from distributing its most capable models
(Mythos 5 / Fable 5) to any foreign national. The directive reached foreign
nationals inside and outside the US, including the provider's own non-citizen
staff; selective compliance was impossible, so the models were disabled
worldwide with no notice, three days after launch.

The operative features for our purposes are not the capability involved but
the **access mechanism**: frontier model access was severed (a) globally,
(b) without notice, (c) gated at nationality. Héctor is a non-US national
operating in Mexico City. Any architecture that leans on US-hosted frontier
API as its escape hatch therefore carries a tail risk that, as of this date,
has stopped being hypothetical.

This principle is the design-side consequence of an Aurora structural
judgment (the compute frontier is fragmenting into nationality-gated blocs;
middle-income economies sit outside the loop). Aurora foresight produces the
constraint; the constraint shapes the build. That chain is now empirically
anchored rather than speculative.

## Scope — what this is NOT

This is **not** a claim that the 2027 model needs frontier capability. The
capability gated on 2026-06-13 was offensive cybersecurity work, which is
irrelevant to the DFD simulation-laboratory natural-language interface. The
principle concerns access architecture only, not capability requirements.

## Design entailments

1. The local Qwen baseline must cover **all** core DFD / simulation-laboratory
   NL-interface workloads without external dependency. Anything currently
   assumed to require external API is a design item to close, not a permanent
   reliance.
2. External API is permitted only for genuinely superior-quality edge cases,
   and must remain non-load-bearing — the system degrades gracefully, it does
   not stop, if external access is cut.
3. Any external fallback maintained must span ≥2 providers in different
   jurisdictions. Not all US-hosted.
4. Standing test: can the stack complete a full work cycle with external API
   disabled? A "no" is logged as design debt.

## Relationship to the compute envelope

This revises one sentence in the 2026-05-16 compute brief — "default to
ollama-hosted Qwen3.5-9B; reserve external API calls for cases where the
local model underperforms." That sentence priced external API as a
quality/cost/recency fallback. DP-001 reprices it as a severable
sovereignty-dependent fallback. The local-first choice already made is
vindicated by the event, not threatened by it; DP-001 hardens its rationale.

## Review trigger

Revisit DP-001 if any of the following occur:
- The export-control regime is rescinded, narrowed, or formally clarified in a
  way that removes the nationality-gating tail risk.
- The 2027 model's local capability envelope changes materially (up or down).
- An open-weight provider the stack depends on becomes jurisdictionally
  compromised, requiring the redundancy set to be re-specified.

## Boundary note

The geopolitical *why* of the 2026-06-13 event — whether "national security"
was the operative rationale or partly pretext — is deliberately **not**
resolved here and is not required to act on this principle. That question is
held open in the Aurora geopolitical watch-item, Gina's layer.

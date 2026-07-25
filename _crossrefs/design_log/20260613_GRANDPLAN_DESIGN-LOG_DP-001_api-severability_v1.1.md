---
doc_id: 20260613_GRANDPLAN_DESIGN-LOG_DP-001_api-severability_v1.1
title: "DP-001 — External frontier API is a severable dependency"
date_originated: 2026-06-13
date_revised: 2026-07-15
supersedes: 20260613_GRANDPLAN_DESIGN-LOG_DP-001_api-severability_v1.0
project: GrandPlan / Dalila (2027 local/institutional model)
register: DESIGN-LOG (2027 model)
principle_id: DP-001
version: 1.1
type: design_principle
classification: execution_constraint
originated_in: Aurora-AI driver chat
added_by: Elle
revised_by: Debb
endorsed_by: Elle
approving_authority: Héctor
status: revised, pending approval
review_status: "Trigger 1 FIRED 2026-06-30/07-01. Reviewed 2026-07-15. Principle UPHELD, rationale strengthened."
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
  - 202607_AURORA_AI_mollick_twilight-chatbots_v1.0
  - 202607_AURORA_AI_nadella_reverse-info-paradox_v1.0
  - 202606_AURORA_geopol_mythos-export-control_v1.0  [pending]
source_provenance: >
  Derived from Aurora foresight. Forcing event web-sourced 2026-06-13;
  resolution web-sourced 2026-07-15 (Mollick 2026-06-30; Anthropic statement on
  restored access, https://www.anthropic.com/news/fable-mythos-access).
---

# DP-001 — External frontier API is a severable dependency

## Principle (unchanged at v1.1)

The Dalila local stack must function autonomously for all core 2027-model
workloads. External frontier API access is to be treated as a **severable,
sovereignty-dependent** dependency — optional, never load-bearing. Where an
external fallback is used at all, it must be **jurisdictionally redundant**
(no single national point of failure).

---

## v1.1 REVISION RECORD

### Trigger

v1.0 specified a review trigger: *"The export-control regime is rescinded,
narrowed, or formally clarified in a way that removes the nationality-gating
tail risk."*

**This trigger fired.** The US Department of Commerce lifted the controls on
2026-06-30; Anthropic restored access on 2026-07-01. Surfaced 2026-07-15 via
the Mollick entry, which describes the interventions as having stopped access
*temporarily*.

### Two material facts added since v1.0

1. **The event resolved.** The suspension ran roughly 2026-06-12 to
   2026-06-30/07-01 — approximately 18 days. v1.0 was drafted while it was
   live and described it as ongoing; that description is now inaccurate and is
   corrected here.
2. **The action was cross-lab.** Mollick reports the interventions stopped
   access to two models — Claude Fable **and GPT-5.6**. This is
   **single-sourced** within our corpus and is recorded as
   corroboration-pending. It bears on DP-001 because a cross-lab action is a
   *capability-threshold* action, not a vendor-specific dispute — which makes
   the mechanism structural rather than idiosyncratic, and therefore more
   likely to recur.

### Determination: UPHELD, rationale strengthened

The trigger fired but the condition attached to it — *"in a way that removes
the nationality-gating tail risk"* — was **not met**. The restoration ends the
instance; it does not remove the risk. The reasoning:

- **Before 2026-06-12**, nationality-gated severance of frontier access was a
  *hypothesis*. It is now a **demonstrated, exercised state capability** —
  applied at scale, across (per Mollick, pending corroboration) more than one
  lab, with the resolution timeline set entirely in Washington.
- A dependency that was **cut and restored on a foreign government's schedule**
  is more clearly severable, not less. The restoration is itself evidence of
  the control, not evidence against it.
- If the action was capability-threshold-based rather than vendor-specific, it
  recurs whenever the next capability threshold is crossed. Mollick's
  institutional-lurch framing predicts exactly this: institutions moving at
  committee speed will keep lurching against a curve they cannot track, and
  while the exponential holds, the gap widens.

DP-001 therefore stands **unchanged in substance**. The rationale is
strengthened: the principle no longer rests on a single live event but on a
demonstrated and structurally recurrent state capability.

### What did NOT change

- The principle text.
- All four design entailments (below).
- The scope limitation: this remains an *access-architecture* constraint, not a
  claim about required capability.

---

## Scope — what this is NOT

Not a claim that the 2027 model needs frontier capability. The capability
gated in June 2026 was frontier-class cybersecurity-relevant work, irrelevant
to the DFD simulation-laboratory natural-language interface. The principle
concerns access architecture only.

## Design entailments (unchanged from v1.0)

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

## Relationship to the compute envelope (unchanged)

Revises one sentence in the 2026-05-16 compute brief — "default to
ollama-hosted Qwen3.5-9B; reserve external API calls for cases where the local
model underperforms." That sentence priced external API as a
quality/cost/recency fallback. DP-001 reprices it as a severable
sovereignty-dependent fallback.

## Open-weight context added at v1.1 (informational, not a change)

Mollick reports the near-frontier open-weight tier lagging the closed US
frontier by 6–12 months, all Chinese, cheap to operate, on its own exponential
curve — and that no other country produces open-weight models near the
frontier. This is mildly favourable to the local-first strategy: the
decentralised pole is not far behind and is closing.

**Two honest qualifications**, recorded so this is not misread as reassurance:
- Dalila's Qwen3.5-9B is *not* in the near-frontier class carrying that 6–12
  month lag. The class is viable; our instance is small.
- Mollick notes open-weight models underperform their benchmarks; real lag
  likely exceeds benchmark lag.
- The open-weight remedy to severability carries its own dependency
  (ecosystem, tooling, standards) — see the Nadella entry's China note. Trading
  one dependency for another is a choice, not an escape.

## Review triggers (revised at v1.1)

- **T1 (fired 2026-06-30/07-01; condition not met; principle upheld).**
  Retained in modified form: revisit if the export-control regime is formally
  narrowed in a way that *durably* removes nationality-gating — e.g. a
  statutory or treaty-level carve-out, not an administrative lifting of a
  single instance.
- **T2.** The 2027 model's local capability envelope changes materially
  (up or down).
- **T3.** An open-weight provider the stack depends on becomes
  jurisdictionally compromised, requiring the redundancy set to be
  re-specified.
- **T4 (new).** A *second* frontier-access severance event occurs. Two
  instances would move the mechanism from "demonstrated" to "recurrent," and
  would justify hardening entailments 2–3 from preference to requirement.
- **T5 (new).** The Mollick GPT-5.6 cross-lab claim is corroborated or refuted.
  Corroboration strengthens the capability-threshold reading; refutation
  reopens the vendor-specific-dispute reading and weakens (though does not
  eliminate) the recurrence argument.

## Boundary note (unchanged)

The geopolitical *why* of the June 2026 event — genuine threat, pretext, or
institutional lurch — is deliberately **not** resolved here and is not required
to act on this principle. Held open in the Aurora geopolitical watch-item,
Gina's layer. Note that v1.1 adds a third candidate explanation to that
question without adjudicating among them.

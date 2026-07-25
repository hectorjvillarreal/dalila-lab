---
doc_id: 20260613_GRANDPLAN_DESIGN-LOG_DP-001_api-severability_v1.2
title: "DP-001 — External frontier API is a severable dependency"
date_originated: 2026-06-13
date_revised: 2026-07-24
supersedes: 20260613_GRANDPLAN_DESIGN-LOG_DP-001_api-severability_v1.1
project: GrandPlan / Dalila (2027 local/institutional model)
register: DESIGN-LOG (2027 model)
principle_id: DP-001
version: 1.2
type: design_principle
classification: execution_constraint
originated_in: Aurora-AI driver chat
added_by: Elle
revised_by: Claude Code (auto-apparatus maintenance run, 2026-07-24)
endorsed_by: Elle            # v1.1 endorsement; v1.2 restates rationale, no change to principle or entailments
approving_authority: Héctor
status: draft, pending approval
review_status: "T1 fired and resolved (v1.1). T5 fired and RESOLVED 2026-07-24, outcome refined (v1.2). Principle UPHELD; recurrence rationale restated on the EO framework."
tags:
  - 2027_model
  - local_llm
  - infrastructure
  - sovereignty_risk
  - open_weight
  - compute_access
  - covered_frontier_models
cross_refs:
  - 20260516_GRANDPLAN_BRIEFING_compute-envelope_v1
  - 202606_AURORA_AI_amodei_exponential_v1.0
  - 202607_AURORA_AI_mollick_twilight-chatbots_v1.2
  - 202607_AURORA_AI_nadella_reverse-info-paradox_v1.0
  - 202606_AURORA_geopol_mythos-export-control_v1.1
  - 202607_AURORA_geopol_open-weights-letter_v1.0
source_provenance: >
  Derived from Aurora foresight. Forcing event web-sourced 2026-06-13;
  resolution web-sourced 2026-07-15 (Mollick 2026-06-30; Anthropic statement,
  https://www.anthropic.com/news/fable-mythos-access). T5 resolution
  web-sourced 2026-07-24; see the Mythos watch-item v1.1 §3 for the full
  source register.
filing_note: >
  v1.2 is filed in _crossrefs/design_log/ only, per the convention that
  cross-project stack governance is not project-local. The v1.1 duplicate in
  GrandPlan/Aurora/AI/ is a flagged hygiene item awaiting Héctor's archival
  decision; it is not propagated.
---

# DP-001 — External frontier API is a severable dependency

## Principle (unchanged since v1.0)

The Dalila local stack must function autonomously for all core 2027-model
workloads. External frontier API access is to be treated as a **severable,
sovereignty-dependent** dependency — optional, never load-bearing. Where an
external fallback is used at all, it must be **jurisdictionally redundant**
(no single national point of failure).

---

## v1.2 REVISION RECORD

### Trigger

v1.1 registered trigger T5: *"The Mollick GPT-5.6 cross-lab claim is
corroborated or refuted."* **T5 fired 2026-07-24** via maintenance-run web
verification; outcome: **refined** — neither clean corroboration nor clean
refutation. Full fact record: Mythos watch-item v1.1 §3.

### What was established

The June 2026 gatings of Claude Fable 5 and GPT-5.6 were **separate actions
under different instruments**:

- Anthropic: **mandatory Commerce export-control order** (2026-06-12, three
  days post-launch), worldwide disablement, lifted 2026-06-30.
- OpenAI: **"voluntary" pre-launch request** (ONCD/OSTP, 2026-06-25),
  restricting GPT-5.6 to ~20 individually government-vetted organizations;
  public 2026-07-09 after Commerce clearance.
- Common mechanism: the **2026-06-02 executive order** establishing a
  classified benchmarking process for designating **"covered frontier
  models,"** with a pre-release review mechanism.

### Determination: UPHELD; recurrence rationale RESTATED

v1.1's strengthened rationale leaned on the reading "a single cross-lab
action is a capability-threshold action, therefore structural and likely to
recur." That reading is refuted as stated — but what replaces it is
**stronger**:

- The recurrence mechanism is not an inferred pattern from one action; it is
  an **institutionalized standing process**. A designation framework that
  gated both US frontier labs' launches within a month, through instruments
  of varying formality (order, request, license exemption — all allowlists),
  does not need to "recur"; it is **already in continuous operation**.
- The severability finding is therefore no longer event-shaped at all. Every
  future US frontier launch is expected to pass through government review;
  the state's demonstrated toolkit spans pre-release gating, post-launch
  severance, and selective re-enablement by allowlist.
- The asymmetry of instrument (stick for Anthropic, carrot for OpenAI) is
  recorded in the watch-item as an open seam. It does not weaken this
  principle: from the dependent's side, severability is indifferent to
  whether the gate is called mandatory or voluntary.

### What did NOT change

- The principle text.
- All four design entailments.
- The scope limitation: an *access-architecture* constraint, not a claim
  about required capability.
- Elle's v1.1 endorsement is carried (rationale restatement only); her
  re-confirmation at next review is noted as due diligence, not a blocker.

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

Revises one sentence in the 2026-05-16 compute brief — external API is priced
as a severable sovereignty-dependent fallback, not a quality/cost/recency
fallback.

## Open-weight context (updated at v1.2)

The v1.1 note recorded a 6–12 month open-weight lag; that estimate was
overtaken in 17 days (Kimi K3, 2026-07-17 — see the Mollick entry's v1.1
amendment and the standing decay warning; all magnitudes here carry as-of
dates). Standing qualifications remain: Dalila's Qwen3.5-9B instance is not
in the near-frontier class; open-weight models often underperform their
benchmarks; and the open-weight remedy carries its own dependency — now with
the sharper caveat that Beijing's MOFCOM consultations (2026-07-07) make the
Chinese open-weight commons visibly a revocable policy choice. Entailment 3's
jurisdictional-redundancy requirement is doing more work, not less. If the
open-weights coalition program (letter of 2026-07-24) converts to policy, a
US open-weight tier would widen the redundancy set on the other side —
contingent on conversion, logged in the letter entry.

## Review triggers (revised at v1.2)

- **T1 (fired and resolved at v1.1).** Retained: revisit if the
  export-control regime is formally narrowed in a way that *durably* removes
  nationality-gating — statutory or treaty-level carve-out, not an
  administrative lifting of a single instance.
- **T2.** The 2027 model's local capability envelope changes materially
  (up or down).
- **T3.** An open-weight provider the stack depends on becomes
  jurisdictionally compromised, requiring the redundancy set to be
  re-specified. (Beijing's consultations maturing into a public-release ban
  would fire this for the Qwen lineage.)
- **T4 (sharpened at v1.2).** A second severance event of **deployed**
  access occurs — distinct from pre-release gating, which is now the
  documented default. A second deployed-access severance moves the mechanism
  from demonstrated to recurrent and hardens entailments 2–3 from preference
  to requirement.
- **T5 (RESOLVED 2026-07-24; replaced).** New: the EO "covered frontier
  models" process is **formalized as the standing default** for frontier
  launches (rule-making, legislation, or explicit policy). Formalization
  would make pre-release gating permanent architecture and warrants
  re-examining whether entailments 2–3 harden without waiting for T4.

## Boundary note (unchanged)

The geopolitical *why* — genuine threat, pretext, or institutional lurch —
is deliberately **not** resolved here and is not required to act on this
principle. Held open in the Mythos watch-item (v1.1 §4), Gina's layer, with
the v1.1 facts shifting weight from pretext toward threat/lurch without
adjudicating.

## Revision history

- **v1.0** (2026-06-13) — drafted during the live severance event.
- **v1.1** (2026-07-15) — T1 fired (controls lifted 06-30, access restored
  07-01); condition not met; principle upheld, rationale strengthened on the
  cross-lab reading (then corroboration-pending). T4/T5 added.
- **v1.2** (2026-07-24) — T5 resolved, outcome refined: separate actions,
  common EO mechanism. Recurrence rationale restated on the institutionalized
  framework; T4 sharpened (deployed-access severance vs pre-release gating);
  T5 replaced with formalization trigger. Principle and entailments unchanged.

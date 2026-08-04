# Anne's inbox — demographics corpus pending review

Per `dfd-demographics-monitor` SKILL.md v0.3 §Routing and Filing, the skill
appends a one-line entry here on every new arrival in `_pending/`. Anne
reviews on her own cadence (set outside this skill).

Format:
- YYYY-MM-DD — [filename in _pending/] — [project_scope] — [indicators] — [iso3]

## Pending

*(none — queue cleared 2026-08-03)*

## Endorsed and moved (recent — last 30 days)

- 2026-08-03 — Q3 replicate (`../country/MEX/quarterly/2026-Q3_demographic_replicate.md`) — **fully endorsed** (Anne §§1–3,5–6; Cath §4/§5/§7 with window-timing caveat applied as endorsement condition); `workflow_status: endorsed`; DFD + BDH cross-refs released. Cath's key rulings: window entry may lag up to one projection step (caveat now mandatory wherever fiscal-space numbers are cited, pending Q4 retabulation); wedge is plausibly real at ~2 pts — integer rounding alone bounds CONAPO-implied TDR to [47.4, 51.1], so the conciliación-vs-WPP base difference is load-bearing (refines Anne's read); Rule-of-85 steepening raises the cost of missing the window but does not move it. Beth not triggered (no standalone health-financing assertion).
- 2026-08-03 — Q2 replicate — **fully endorsed** (Anne retroactive batch; Cath §§4–5, §7 with resolution caveat applied): the "window shortened to ~5 yr vs v1.1's 8–10" claim was an overstated grid-resolution artifact — interpolated Central window ≈ 2030–2041 (~11 yr); supersession of v1.1 holds for level (42.0) and timing (~2038) only. IM-6 anchor stays 2033–2038 (conservative interior under either convention).

- 2026-08-03 — `2026-08-03_inegi-enr2024-mex-births.md` — endorsed by Anne 2026-08-03 (with one factual edit applied); routed to `releases/`; Rule-of-85 trigger reading confirmed sound; anchor stays 1.60/2023; cross-refs appended to DFD + BDH
- 2026-08-03 — Q2 replicate (`../country/MEX/quarterly/2026-Q2_demographic_replicate.md`) — retroactive batch endorsement of Anne-scope content (queue-hygiene repair: it never entered this inbox); Cath items (§5 fiscal window, §7 IM-6 flags) still open
- 2026-07-11 — `2026-07-11_unfpa-demographic-futures-survey.md` — Anne adjudicated 2026-07-11 (record: `2026-07-11_UNFPA-note_Anne-endorsement.md`); execution completed 2026-08-03: conformance edits + guardrail applied, routed to `observations/` (folder created on first use), indicators relabeled `[coupling, desired_fertility]`, watch item `watch_items/2026-07-11_fertility-reversibility-policy-tractability.md` opened endorsed, cross-refs appended to DFD + BDH + Aurora. Framing ruling: complementary, not competing; residual thread is reversibility (the watch item)
- 2026-05-16 — `anne_scenario_anchors_brief.md` — [DFD, BDH, Aurora] — TFR anchors source-pinning (load-bearing for skill §Step 2a) — MEX/CRI/COL/CHL/PAN — endorsed 2026-05-16; recorded in seq 2_of_2 build instruction

## Flagged to Debb (from Anne's 2026-08-03 rulings) — RESOLVED 2026-08-03 (Debb)

1. 2026-08-03 — Type retrofit executed via `_crossrefs/_build_instructions/2026-08-03_demographics_type_retrofit.md` (build_type: retrofit, status: executed): `type: working_note` → `type: corpus_entry` in Q2 replicate and `scenario_anchors.md`; tiers preserved; Q2 `endorsed_by:` line verified byte-identical (git diff); one back-link line appended to each file's Cross-references.
2. 2026-08-03 — SKILL.md revised v0.2 → v0.3 (revised_by: Debb): `desired_fertility` added to §Classification dim 1 with aspirational-vs-realized gloss; cross-reference template path fixed `../../../` → `../../../../`; `observations/` added to §Prerequisites scaffold tree; option-(a) decision recorded as endorsement-workflow item 6; §Revision history updated.
3. 2026-08-03 — README organization listing verified: `observations/` was already present (added at folder creation, UNFPA execution); gloss aligned to "endorsed multi-country / cross-cutting working notes". SKILL.md scaffold tree updated per item 2.
4. 2026-08-03 — Option (a) CLOSED: Debb concurred with Anne's provisional ratification; no PROTO-RAG-001 amendment. Reasoning and standing operational rule recorded in retrofit build instruction §5 and SKILL.md v0.3 §Routing and Filing item 6.
5. 2026-08-03 — `endorsement_record` type gap recorded in retrofit build instruction §6 (protocol revision candidates), alongside three further candidates noticed in-pass: `skill_invocation` type on the Q3 build instruction of record; skill-authorized extension fields (`workflow_status` etc.) absent from the PROTO schema; `governing_instructions:` as an optional registered field.

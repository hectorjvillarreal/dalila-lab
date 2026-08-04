# Anne's inbox — demographics corpus pending review

Per `dfd-demographics-monitor` SKILL.md v0.2 §Routing and Filing, the skill
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

## Flagged to Debb (from Anne's 2026-08-03 rulings)

1. Retrofit candidate (one build instruction, not silent fixes): `type: working_note` → `type: corpus_entry` in Q2 replicate and `scenario_anchors.md` (Q3 already conformant). Per Cath: the Q2 endorsement line must survive the retrofit verbatim.
2. SKILL.md v0.3: add `desired_fertility` to §Classification indicator vocabulary; fix cross-reference template relative path (`../../../` is one level short from `GrandPlan/{Project}/docs/corpus/` — executed entries use `../../../../`).
3. `observations/` folder now exists (routing table had it; scaffold list didn't) — update README/scaffold list.
4. Option (a) per-quarter build instructions for quarterly replicates — Anne provisionally ratifies; your concurrence closes it, no PROTO amendment needed.
5. `endorsement_record` artifact type (used 2026-07-11) is not a PROTO-RAG-001 type — retained as provenance; note the gap for next protocol revision.

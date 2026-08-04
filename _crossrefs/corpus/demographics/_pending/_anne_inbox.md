# Anne's inbox — demographics corpus pending review

Per `dfd-demographics-monitor` SKILL.md v0.2 §Routing and Filing, the skill
appends a one-line entry here on every new arrival in `_pending/`. Anne
reviews on her own cadence (set outside this skill).

Format:
- YYYY-MM-DD — [filename in _pending/] — [project_scope] — [indicators] — [iso3]

## Pending

- 2026-08-03 — `../country/MEX/quarterly/2026-Q3_demographic_replicate.md` — [DFD, BDH] — composite (births, tfr proxy, coupling, age-structure) — MEX — **Anne endorsed §§1–3,5–6 (2026-08-03; re-anchor decision frame recorded in §2). Remains pending CATH**: §4 observed-TDR ≈49 vs. Central-path ≈46 wedge (window-timing lag ~1 step if level is real) + unchanged fiscal-window characterization; also Q2's never-cleared §5/§7 fiscal items. Project cross-refs held until Cath rules. Option (a) per-quarter build instructions: Anne provisionally ratifies; final call joint with Debb.

## Endorsed and moved (recent — last 30 days)

- 2026-08-03 — `2026-08-03_inegi-enr2024-mex-births.md` — endorsed by Anne 2026-08-03 (with one factual edit applied); routed to `releases/`; Rule-of-85 trigger reading confirmed sound; anchor stays 1.60/2023; cross-refs appended to DFD + BDH
- 2026-08-03 — Q2 replicate (`../country/MEX/quarterly/2026-Q2_demographic_replicate.md`) — retroactive batch endorsement of Anne-scope content (queue-hygiene repair: it never entered this inbox); Cath items (§5 fiscal window, §7 IM-6 flags) still open
- 2026-07-11 — `2026-07-11_unfpa-demographic-futures-survey.md` — Anne adjudicated 2026-07-11 (record: `2026-07-11_UNFPA-note_Anne-endorsement.md`); execution completed 2026-08-03: conformance edits + guardrail applied, routed to `observations/` (folder created on first use), indicators relabeled `[coupling, desired_fertility]`, watch item `watch_items/2026-07-11_fertility-reversibility-policy-tractability.md` opened endorsed, cross-refs appended to DFD + BDH + Aurora. Framing ruling: complementary, not competing; residual thread is reversibility (the watch item)
- 2026-05-16 — `anne_scenario_anchors_brief.md` — [DFD, BDH, Aurora] — TFR anchors source-pinning (load-bearing for skill §Step 2a) — MEX/CRI/COL/CHL/PAN — endorsed 2026-05-16; recorded in seq 2_of_2 build instruction

## Flagged to Debb (from Anne's 2026-08-03 rulings)

1. Retrofit candidate (one build instruction, not silent fixes): `type: working_note` → `type: corpus_entry` in Q2 replicate and `scenario_anchors.md` (Q3 already conformant).
2. SKILL.md v0.3: add `desired_fertility` to §Classification indicator vocabulary; fix cross-reference template relative path (`../../../` is one level short from `GrandPlan/{Project}/docs/corpus/` — executed entries use `../../../../`).
3. `observations/` folder now exists (routing table had it; scaffold list didn't) — update README/scaffold list.
4. Option (a) per-quarter build instructions for quarterly replicates — Anne provisionally ratifies; your concurrence closes it, no PROTO amendment needed.
5. `endorsement_record` artifact type (used 2026-07-11) is not a PROTO-RAG-001 type — retained as provenance; note the gap for next protocol revision.

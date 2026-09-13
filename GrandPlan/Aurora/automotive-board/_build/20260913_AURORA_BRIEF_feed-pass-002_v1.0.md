---
doc_id: 20260913_AURORA_BRIEF_feed-pass-002_v1.0
title: "Brief — feed pass 002 executed; what the artifacts cannot say"
project: Aurora / automotive board
type: session_brief
version: 1.0
date: 2026-09-13
prepared_by: Claude Code session (task: 20260913_AURORA_TASK_feed-pass-002_v1.0)
for: Elle
refers_to:
  - 20260913_AURORA_TASK_feed-pass-002_v1.0
  - 20260815_AURORA_BRIEF_feed-pass-001_v1.0
---

# Feed pass 002 — residuals only

**§0: neither case as written. Pass 001 ran (15 inbox items, 8 slot commits, brief filed 08-15) but never wrote the ledger, which still held only the 07-20 CarExpert item. The window was taken from the ledger per §1, 2026-07-20 → 09-13, and deduped against the inbox too.** The "never reported" premise is also off: the pass-001 brief is in `_build/`. The ledger now holds this pass's items (absorbed 09-13); pass-001's 15 items were **not** back-filled.

Artifacts: 29 inbox items; 31 ledger records; 8 slot commits (001 margin, geographic_reach · 002 margin, geographic_reach · 003 volume, margin · 006 margin, 007 margin reported→confirmed on primary). `validate: ok`, boundary ok, no Rule D warnings after every commit. The Tesla 10-Q and Hyundai IR notice went to the ledger only (same events as pass-001 items).

**Verification targets**
1. Toyota–Subaru/Suzuki — **PARTIAL.** Confirmed: Toyota 20% of Subaru (2019, primary; Subaru's 2025 IR says 21.00%, basis not reconciled), a jointly developed BEV platform, THS in Subaru models, Toyota 4.94% of Suzuki (2019), the Suzuki-built eVitara supplied to Toyota, Maruti rebadges = 53% of Toyota Kirloskar FY25 dispatches. Not found: Toyota's current Suzuki stake; terms of Subaru's 2026 Strong Hybrid.
2. Honda/Mazda — **CONFIRMED (quantities).** Honda FY3/26 operating loss ¥414.3B on EV losses ¥1.58T; 0 Series cancelled; Q1 FY3/27 OP ¥530.8B. Mazda FY3/26 OP ¥51.6B (~1.0%); own BEV 2027→2029. Contested: Honda 2030 EV target scrapped vs cut to 20%; Honda China Aug −49.9% is snippet-only.
3. Japanese third-market share — **PARTIAL.** Found vs Chinese: Australia Aug (Toyota 19.5%, five Chinese brands 26.4%, FCAI primary), Thailand, Indonesia, Mexico Jan–Apr (Japan 39.8% / China 11.4%), Chile. Not found: Japanese share from ACEA (blocked), Brazil combined; Vietnam/Philippines lack a Chinese figure. Several series have conflicting bases.
4. Solid-state — **PARTIAL.** CATL and BYD 2027 small-batch targets confirmed (secondary). Contested: a CATL 2 GWh/95%-yield pilot line (Feb) vs CATL's own "TRL 4" (June). MG4 semi-solid confirmed (launched 2025-08, ¥99.8k); CALB hybrid in Chery light trucks; Sunwoda: no car model found. **China standard contested:** SAMR primary lists GB/T 48093.1-2026, effective 2028-01-01; media cite GB/T 43568-2026, effective 2026-07-01.
5. Korean cells Q2 — **CONFIRMED.** LGES OP KRW 113.3B incl. AMPC 241B (primary); Samsung SDI OP 204B, first profit in 7 quarters (primary); SK On OP 821.8B on undisclosed one-off compensation. ESS execution: LGES Lansing LFP start 08-18, SDI buys GM's SynergyCells stake, SK On–NeoVolta 9 GWh. Q3: none published.
6. Europe post-Northvolt — **PARTIAL.** Lyten closed Skellefteå/Västerås 2026-02-27 (primary); Heide MOU only; deliveries slip to early 2027. PowerCo Salzgitter in production (primary); CATL Debrecen held to equipment debugging after 08-25/31 orders. No verified 2026 GWh output for any plant.
7. Renault/Dacia vs VW Core — **PARTIAL.** Renault Group H1 operating margin 5.2% on €30.3B (primary); Dacia 327,077 −8.1%, Renault brand 829,518 +2.6% (primary). VW Brand Group Core H1 4.9% (primary). Not found: separate Dacia/Renault-brand margin.
8. Leapmotor stakes — **NOT FOUND (movement).** The Stellantis H1 6-K excerpts give only the 51/49 International split, no Zhejiang Leapmotor stake %. 18.99% / FAW 5% unrefuted; one stale secondary still says ~21%.

**Left at the cap:** Leapmotor July 101,267; Toyota hydrogen parts trucks (Japan Times 09-04); Xi state visit dated 09-24 (Wikipedia only); July Europe Chinese share 11.2% (Dataforce via secondary); MG 07 42k orders; verification sources (in the session record only, not the inbox).

**Empty searches, by slot:** `cost_position` — no unit-cost quantity for any entry (001/002/004/006); **002 cost_position (decisive) remains empty.** 005 — no H1 € cost quantity. 004 — no new in-window quantity. MG Europe July/Aug; SAIC Aug overseas (the circulating figure looks prior-year); Leapmotor Brazil; SAIC/MG CVR exposure; EU equivalent gate; smart; JAMA after 07-17; Huawei auto export controls; Optimus; Korea–US tariff deal status.

**Judgment calls, named and deferred:** (1) BYD auto-segment gross margin 22.33% and Geely core profit/vehicle RMB 6,806 were **not** written to `cost_position`: they are margins, and mapping them to "unit-cost standing" is a definition call. (2) Hyundai 007 margin promoted to `confirmed` on a company IR notice that labels itself "tentative". Rule followed, label recorded in `unit`. (3) 006 margin value is arithmetic on 10-Q line items; the 10-Q does not state 16.3%. (4) HIMA July: board slot history 45,046 vs CnEVPost 09-01 "July 45,422"; BYD Aug overseas 189,466 vs 188,746. Recorded, not repaired. (5) Whether to back-fill pass-001 items into the ledger. (6) US policy (09-11 statement, S.4429, 09-24 summit) captured; TH-001/TH-002 untouched. (7) This brief sits in `_build/` per the pass-001 precedent, although §8 says "nothing outside feed/ and slots.*". (8) The human-owned `notes` under 001/002/004/006 filled slots still read "awaiting feed", as in pass 001.

**Fence report.** Read: `CLAUDE.md`, `README.md`, both TASK files, `_build/` (listing + heads of all; pass-001 brief in full), `scaffold/pipeline.md`, `scaffold/slot-registry.yaml`, 7 entry `.yaml` + 7 `.md`, `thresholds.yaml`, `feed/inbox.md`, `feed/absorbed.yaml`, `tools/feed.py`, `tools/pre-commit-hook.sh`; `tools/validate.py` executed, not read; git log/status for this tree. Web: 5 research subagents (web only, no file access) plus 11 direct verification fetches. Written: `slots.*` in 001/002/003/006/007 `.yaml`, `feed/inbox.md`, `feed/absorbed.yaml`, this brief. Scratch scripts in the session scratchpad, outside the repo. Nothing outside the tree; no prose, thresholds, archetypes, `notes`, or `decisive` touched; Toyota `transition_pace_exposure` still null; no `tariff_exposure` seeded; no remote, no push.

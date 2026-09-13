---
doc_id: 20260913_AURORA_BRIEF_pass-002-flags_v1.0
title: "Brief for Elle — flags from feed pass 002: dates, wording frictions, discrepancies, confidence"
project: Aurora / automotive board
type: session_brief
version: 1.0
date: 2026-09-13
prepared_by: Claude Code session (requested by Héctor)
for: Elle
refers_to:
  - 20260913_AURORA_TASK_feed-pass-002_v1.0
  - 20260913_AURORA_BRIEF_feed-pass-002_v1.0
---

# Brief for Elle — flags from feed pass 002

**Not a build instruction.** This document authorises nothing and adjudicates nothing. Every item below is a flag: a fact placed beside a board element. What it means for any bet, archetype or threshold is your call. Sources are in `feed/inbox.md` and the pass-002 brief unless given here.

---

## 1. Dated items inside the next three weeks

- **2026-09-24** — Xi state visit scheduled to begin (Wikipedia only; not primary). Follows the 09-11 presidential statement that Chinese auto plants in the US would be acceptable.
- **2026-09-30** — Commerce/BIS Connected Vehicle Rule: the MY2027 software prohibition takes effect (law-firm snippet, not fetched). This is the operative date behind Polestar's MY2027 denial; Polestar has already cut FY2026 guidance to 61,900–63,100.
- **Statement vs bill.** S.4429 (Connected Vehicle Security Act) carries a >15% Chinese-ownership bar, was ordered reported by Senate Commerce 07-22, and the Alliance for Automotive Innovation urged passage 09-03. The 09-11 statement points the other way. Bears on **TH-001 / TH-002**; neither touched.

→ A short intake in early October would catch all three. Your call whether to issue one.

## 2. Frictions between facts and watch-item wording

- **VW plant sale (005).** Osnabrück is being sold — to Aurelius with Lower Saxony, for Rafael air-defence production. The watch item reads "a European plant is actually sold **to a Chinese rival**." A string match would flag it; the facts do not fit the wording.
- **BYD profit direction (002).** H1-2026 net profit −20.54%; Q2 alone +30% (8.2B yuan). The pass-001 inbox line that extended the "stress-at-home" reading cited Q1 −55%. Which figure that reading rests on matters.
- **Local-plant tariff defence (002).** BYD Hungary assembly now "expected to begin between November and December 2026". CATL Debrecen held to equipment debugging by Hungarian authorities after 08-25/31 orders.
- **Honda "bad position" (verification target 2).** FY3/26 operating loss ¥414.3B (EV charges ¥1.58T); Q1 FY3/27 operating profit ¥530.8B (+117%), guidance raised to ¥650B. The claim reads differently by period.
- **Korean cell makers' profitability (verification target 5).** LGES Q2 operating profit KRW 113.3B is below its AMPC of 241B (≈ −127.7B ex-AMPC). SK On's KRW 821.8B rests on undisclosed one-off customer compensation. Both headlines overstate the underlying result — relevant to "Korea exiting the EV-cell contest."
- **"Semi-solid" as a category (verification target 4).** The media version of China's standard (GB/T 43568-2026, eff. 2026-07-01) defines 5–20% liquid as "hybrid solid-liquid" and bans "semi-solid/quasi-solid" labels. SAMR's primary listing differs (GB/T 48093.1-2026, eff. 2028-01-01). If the media version holds, the task's own term is not an official category. Unresolved.
- **TH-004 (007).** Hyundai investor day 08-26: "30,000 units of annual US capacity from 2028, 25,000 already spoken for," HMGMA primary. Threshold due 2028-12-31. Movement only. The accompanying KMWU tentative deal (no robot veto) is Korean, not HMGMA.

## 3. Discrepancies — recorded, not repaired

| Item | Figure A | Figure B | Note |
|---|---|---|---|
| HIMA July 2026 | 45,046 (pass-001 inbox line) | 45,422 (CnEVPost 09-01) | Possible revision; the slot now holds August, the inbox line still says 45,046 |
| Geely H1-2026 exports | 472,500 (human-owned `notes`, 001 volume) | 474,000 (Geely results, 08-17) | `notes` read-only |
| BYD August overseas | 189,466 (CnEVPost, in slot) | 188,746 (chinaevhome) | |
| Leapmotor Stellantis stake | "~20%" (task 002 §3) | 18.99% (Stellantis May release) | Task wording drift |
| Toyota stake in Subaru | 20% (Toyota 2019) | 21.00% (Subaru IR 2025) | Likely different bases |

## 4. Process

- **Pass 001 never wrote `absorbed.yaml`**; its 15 inbox items are still absent from the ledger. Nothing in the tooling enforces absorption, and the §0 test in task 002 assumed it. Suggest the next task names the absorb step explicitly and decides on the pass-001 back-fill.

## 5. Confidence in this session's work

- **Verified directly:** every slot-write source, re-fetched with date and figures checked.
- **Not re-verified:** the eight verification results rest on research-subagent fetches. Inbox lines built on snippets or blocked pages — CNBC (S.4429), Caixin (Leapmotor target cut), Taylor Wessing (09-30 date), Tech Times (Polestar data routing) — are marked as such in the inbox. Treat them as leads until opened.
- **006 margin 16.3%** is arithmetic on 10-Q line items; the filing does not print the figure.

---

**Fence report.** Read: nothing new; compiled from this session's record. Written: this brief only.

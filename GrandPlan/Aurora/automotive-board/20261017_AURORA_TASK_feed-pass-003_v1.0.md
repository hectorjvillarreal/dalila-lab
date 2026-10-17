---
doc_id: 20261017_AURORA_TASK_feed-pass-003_v1.0
title: "Task — feed pass 003: expired thresholds, five-week intake, decision-support brief"
project: Aurora / automotive board
type: task_instruction
version: 1.0
date: 2026-10-17
added_by: Elle
authorised_by: Héctor
scope: feed/ and slots.* only — Jobs 1 and 2, plus a decision-support brief
invocation: with --fetch
---

# TASK — feed pass 003

Five weeks since pass 002. Two booked thresholds have passed unchecked. **This pass
updates the factual layer and assembles material for pending judgment calls — it does not
make them.**

The board's judgment backlog (entry 008, three corrections, unfiled findings, the
coalition register) is **not** in scope and must not be attempted. §5 is where this pass
earns its keep: a brief built to let Elle clear that backlog in one sitting.

---

## 1. Ledger housekeeping — do this first

**Decided, not open:** back-fill pass 001's fifteen inbox items into `feed/absorbed.yaml`.
They were captured but never absorbed; the ledger exists for dedupe and an unabsorbed item
can be re-captured. Back-fill with their original dates and a note that absorption was
retroactive on 2026-10-17.

**Then:** window runs from the latest ledger date → 2026-10-17. Dedupe against both the
ledger and the existing inbox.

**And: absorb at the end of this pass.** Nothing in the tooling enforces it and two passes
have now diverged on it. Treat the absorb step as part of the task, not a courtesy.

---

## 2. Priority — the two expired thresholds

Both were booked with dates and both passed while the board sat. **Establish the facts.
Do not resolve the thresholds** (`status: resolved` and `resolution` are human-set).

1. **Xi state visit, scheduled 2026-09-24.** Did it occur, and was anything agreed on
   automotive market access? Context: a presidential statement on 2026-09-11/12 signalled
   openness to Chinese plants in the US, against existing 100%+ tariffs and S.4429
   (>15% Chinese-ownership bar, ordered reported by Senate Commerce 07-22). **Also check
   S.4429's status.** Bears on entry 001's 2b bet.
2. **Connected Vehicle Rule, MY2027 software prohibition due 2026-09-30.** Did it take
   effect as scheduled, was it delayed, or was it modified? This is the operative
   instrument behind Polestar's denial. Bears on TH-001 (Volvo authorization) and TH-002
   (Lotus / smart).

Prefer primary sources — Federal Register, Commerce/BIS, congress.gov, official readouts.
If a question cannot be settled from a primary source, **say so rather than substituting
press characterisation.**

---

## 3. Job 1 — sweep

Capture to `feed/inbox.md`: **date · one clause on why it might matter · URL.**

**Tier 1 — needed for pending entries and corrections.**
- **Leapmotor** — Q3 and latest monthly volume, margin, overseas/Brazil, any change in the
  Stellantis (18.99%) or FAW (~5%) stakes. *Needed to write entry 008.*
- **BYD** — Q3 2026 results and the full Q1/Q2/H1/Q3 sequence in one place. *A pending
  correction turns on which figure the entry's reading rests on.*
- **VW Osnabrück** — status of the Aurelius / Lower Saxony sale for Rafael air-defence
  production.

**Tier 2 — decisive slots still empty.** `002 cost_position` (decisive, no public unit-cost
quantity found in two passes — if none exists again, say so plainly, it is a finding) ·
`cost_position` generally · Q3 margins across the seven entries.

**Tier 3 — thresholds.** TH-003 JAMA harness specs · TH-004 Atlas at HMGMA. Movement only.

**Tier 4 — watch items**, from the seven entry prose files.

**Cap: roughly 30 items.** Name what was left.

---

## 4. Job 2 — slot maintenance

Unchanged rules. Write only `slots.*`: `value`, `unit`, `delta`, `date`, `source`,
`source_type`, `confidence`. One slot write = one commit.

**Write sourced quantities. Do not write ratings.** Margins are not unit cost — the pass-002
decision not to map BYD's auto gross margin to `cost_position` was correct and stands.

Still out of scope: Toyota `transition_pace_exposure` (leave null) · `tariff_exposure` for
004/005/006 · any slot whose only available value is a qualitative rating.

---

## 5. The decision-support brief — what this pass is for

One document, for Elle. **Not a status report.** Each section below exists to let a specific
pending judgment call be made without re-reading five weeks of inbox.

| Pending call (Elle's) | What the brief must supply |
|---|---|
| Resolve TH-001 / TH-002 | What happened at the summit; CVR 09-30 status; S.4429 status — facts only |
| Entry 008 (Leapmotor) | Current volume, margin, overseas, stakes — in one block |
| Correction: BYD's reading | Q1 / Q2 / H1 / Q3 2026 in sequence, with sources, no interpretation |
| Correction: Honda | Any Q2 FY3/27 data — does the recovery hold? |
| VW watch-item wording | Osnabrück facts; any other European capacity disposal |
| `002 cost_position` | Whether a public unit-cost quantity exists at all |

Plus, briefly: anything in the five weeks that **contradicts** a bet or watch item as
currently written — flagged, not adjudicated; discrepancies between sources, recorded not
repaired; and the fence report.

**Keep it to two pages.** The inbox and the commits are the record; do not restate them.

---

## 6. Prohibitions

Unchanged. No archetype assignment; no loadings; no bet adjudication ("under stress",
"weakening"); no ranking; no prose writes; **no threshold resolution**; no new entries —
including Leapmotor, however complete the data looks; no edits to `archetypes.md`,
`findings.md`, or any entry `.md`; no qualitative ratings in slots; no touching `notes`,
`decisive`, or `archetype_ref`.

If the validator surfaces something broken, report it, do not repair it.

---

## 7. Acceptance

- [ ] Pass-001 items back-filled into `absorbed.yaml`; this pass's items absorbed at the end.
- [ ] Both expired thresholds addressed factually, with primary sources or an explicit "not settled".
- [ ] Slot writes carry `source`, `source_type`, `confidence`, `date`. No ratings.
- [ ] Nothing written outside `feed/`, entry `.yaml` `slots.*`, and the brief.
- [ ] `python3 tools/validate.py` → `validate: ok`, no Rule D warnings.
- [ ] One brief, two pages, structured by §5.

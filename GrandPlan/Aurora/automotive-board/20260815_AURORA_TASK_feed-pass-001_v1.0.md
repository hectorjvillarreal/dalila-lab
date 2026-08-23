---
doc_id: 20260815_AURORA_TASK_feed-pass-001_v1.0
title: "Task — feed pass 001: intake since 2026-07-16, slot maintenance"
project: Aurora / automotive board
type: task_instruction
version: 1.0
date: 2026-08-15
added_by: Elle
authorised_by: Héctor
scope: feed/ and slots.* only — Jobs 1 and 2
invocation: python3 tools/validate.py … with --fetch (opt-in, authorised 2026-07-24)
---

# TASK — feed pass 001

**The first feed pass.** Jobs 1 and 2 of the build spec, never yet run in anger. The tool
was built in July and the factual layer has not been touched since: freshest facts are
Geely at **2026-07-16**, Toyota at **2026-06-21**, one item in the dedupe ledger. Every
session since installation went to infrastructure. This pass is the correction.

**Nothing in this task requires a judgment about strategy.** If something does, it is out
of scope — report it.

---

## 1. Window and dedupe

**Window:** 2026-07-16 → 2026-08-15.

Dedupe every candidate against `feed/absorbed.yaml` before capture. One item is already
there (CarExpert / Sato / JAMA, absorbed 2026-07-20, entry 004) — do not re-capture it or
anything substantially reporting the same event.

---

## 2. Job 1 — feed intake

Capture to `feed/inbox.md`. One line per item: **date · one clause on why it might matter
· URL**. No schema beyond that; the feed is deliberately looser than the corpus protocol
and outside PROTO-RAG-001.

**Scope the search by the board, not by general interest.** In priority order:

1. **Decisive slots that are empty or stale** — Geely `geographic_reach` (decisive,
   empty), `margin` and `cost_position` across all entries, BYD `cost_position`.
2. **Q2/H1 2026 results season** — it landed inside the window and is the single densest
   source of slot-grade facts for all seven entries.
3. **Booked thresholds** — TH-001 (Volvo US authorization), TH-002 (Lotus / smart under
   the Connected Vehicle Rule), TH-003 (JAMA harness specs), TH-004 (Atlas at HMGMA).
   Capture movement; **do not resolve any threshold.**
4. **Named watch items** in the seven entry prose files — read them first; they are the
   standing question list.
5. **Candidate players** — Leapmotor, Chery, SAIC/MG. See §4.

**Volume cap: roughly 25 items.** If more qualify, take those bearing on decisive slots
and thresholds first, and say in the report what was left behind.

**Flagging is permitted; promotion is not.** You may note that an item matches a watch-item
string on some entry. You may not decide it changes anything. Promotion from feed to board
is Elle's call.

---

## 3. Job 2 — slot maintenance

Write only to `slots.*` fields: `value`, `unit`, `delta`, `date`, `source`, `source_type`,
`confidence`. One slot write = one commit, message carrying source and date.

**Write sourced quantities. Do not write ratings.**

This is the operative rule of the pass. "BYD Q2 2026 gross margin 18.7%" is a fact → slot.
"BYD's cost position is strong" is a judgment → not yours. Where the board already holds a
qualitative value (`vertical_integration: "high"`), it was human-set at migration; leave it
and add the quantity in a separate slot if one fits.

- **`source_type`**: `primary` for company IR, filings, regulators, CPCA/CAAM/statistical
  agencies; `secondary` for press. Where both exist, record primary.
- **`confidence`**: `confirmed` for a filing or company statement; `reported` for press.
  You may promote `reported → confirmed` when a primary source lands. Never the reverse.
- **`delta`**: only where the source states it or it is arithmetic on two sourced figures.

**Explicitly out of scope for slot writes:**

- **Toyota `transition_pace_exposure`** — decisive but unseeded, custom, and requires
  region-indexing. A judgment call. Leave it null.
- **`tariff_exposure` back-fill (004/005/006)** — capture the underlying quantities into
  the feed, but do not seed the slot; its definition is still on the repairs backlog.
- Any slot where the only available value would be a qualitative rating.

---

## 4. Candidate players — feed only, never slots

Leapmotor, Chery and SAIC/MG are **not on the board.** They have no entry and therefore no
slots. Everything found on them goes to `feed/inbox.md` only.

Worth capturing if it appears, because it bears on live questions:

- **Leapmotor** — H1/Q2 2026 volume and margin; and the **unverified** Stellantis
  ownership stake and export JV. Elle flagged that link as unconfirmed on 2026-07-16; if a
  primary source settles it either way, that is the single most valuable item in this pass.
- **Chery** — export standing (931,600 in H1-2026, ahead of BYD); HIMA/Luxeed relationship.
- **SAIC/MG** — European volumes and any Connected-Vehicle-Rule-equivalent exposure.

**Do not create an entry, a YAML file, or a slot for any of them.** Entry is by basis gap
and is Elle's call.

---

## 5. Prohibitions

Unchanged from `CLAUDE.md` and the build doc. In this pass specifically: no archetype
assignment or normalisation; no loadings; no bet adjudication ("under stress",
"weakening"); no ranking; no prose writes; no threshold resolution; no new entries; no
edits to `archetypes.md` or `findings.md`; no qualitative ratings in slots.

If the validator surfaces something broken, **report it, do not repair it.**

---

## 6. Reporting — capped, deliberately

Five briefs were written for the six-step closure. That ratio inverted the point of the
tool. This pass corrects it.

**The artifact is the report.** `feed/inbox.md` and the slot commits show what was found;
do not restate them in prose.

**Write one brief, and keep it under one page**, covering only what the artifacts cannot
say:

- items that qualified but were left behind at the volume cap;
- searches that came back empty, and for which slot;
- anything that looked like it needed a judgment call, named and deferred;
- the fence report — every path read or written.

Do not summarise the feed. Do not restate slot values. Do not narrate the process.

---

## 7. Acceptance

- [ ] `feed/inbox.md` populated; every item deduped against `absorbed.yaml`.
- [ ] Slot writes carry `source`, `source_type`, `confidence`, `date`. No ratings.
- [ ] Toyota `transition_pace_exposure` still null; no `tariff_exposure` seeded.
- [ ] No file written outside `feed/` and entry `.yaml` `slots.*`.
- [ ] `python3 tools/validate.py` → `validate: ok`, no Rule D warnings.
- [ ] One commit per slot write; feed commits prefixed `feed:`. Local only.
- [ ] One brief, under a page.

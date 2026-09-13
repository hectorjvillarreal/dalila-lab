---
doc_id: 20260913_AURORA_TASK_feed-pass-002_v1.0
title: "Task — feed pass 002: intake, verification targets, slot maintenance"
project: Aurora / automotive board
type: task_instruction
version: 1.0
date: 2026-09-13
added_by: Elle
authorised_by: Héctor
scope: feed/ and slots.* only — Jobs 1 and 2
invocation: with --fetch (opt-in, authorised 2026-07-24)
supersedes_status_of: 20260815_AURORA_TASK_feed-pass-001_v1.0   # see §0 — may never have executed
---

# TASK — feed pass 002

Two jobs, as before: intake and slot maintenance. **New in this pass: a distinct
verification-target section** (§3). Analysis since mid-July generated specific factual
claims that were flagged unverified at the time. Those are named lookups, not a sweep,
and they are the highest-value part of this task.

**Nothing here requires a judgment about strategy.** If something does, report it.

---

## 0. State check — did pass 001 run?

Feed pass 001 was issued for the window 2026-07-16 → 2026-08-15 and never reported.
Establish which case obtains **before searching**:

```
cat feed/inbox.md
cat feed/absorbed.yaml
git log --oneline -- feed/
```

- **Items present from pass 001** → it ran. Window for this pass starts at the most
  recent `absorbed` date.
- **Ledger still holds only the 2026-07-20 CarExpert item** → pass 001 did not execute.
  Window starts **2026-07-16** and this pass absorbs both.

State which case you found, in one line, at the top of your report.

---

## 1. Window

**From the latest date in `absorbed.yaml` → 2026-09-13.** Derived from the ledger, not
hardcoded — the artifact knows what is covered. Dedupe every candidate against the ledger
before capture.

---

## 2. Job 1 — sweep, by tier

Capture to `feed/inbox.md`: **date · one clause on why it might matter · URL.** No schema
beyond that. Work the tiers in order and stop at the cap.

**Tier 1 — dated and decisive.**
- **US policy on Chinese automakers.** A presidential statement on 2026-09-11/12 signalled
  openness to Chinese plants in the US, against the existing Connected Vehicle Rule, 100%+
  tariffs, and a Senate bill barring companies with >15% Chinese ownership. Xi is expected
  in Washington in late September. **Capture the state of play and the bill's progress.
  Do not resolve the threshold** — the summit has not happened.
- **Leapmotor 2026 interim figures** — H1 and any Q3 data, margin, overseas volume, Brazil
  and wider South America. Needed for a pending board entry.

**Tier 2 — decisive slots still empty.**
- `margin` and `cost_position` across all seven entries — Q2/H1 2026 results.
- Geely `geographic_reach` (flagged decisive, empty).
- BYD `cost_position`.

**Tier 3 — thresholds.** TH-001 Volvo US authorization · TH-002 Lotus / smart under the
Connected Vehicle Rule · TH-003 JAMA harness specs · TH-004 Atlas at HMGMA. **Capture
movement; resolve nothing.**

**Tier 4 — watch items.** Read the seven entry prose files first; their watch-item lines
are the standing question list.

**Volume cap: roughly 30 items.** Name in the report anything that qualified and was left.

**Flagging is permitted; promotion is not.**

---

## 3. Verification targets — named claims, not a sweep

Each was asserted in analysis and flagged unverified. Confirm, refute, or report *not
found*. **"Not found" is a valid and useful result** — report it rather than substituting
an adjacent fact.

| # | Claim to check | Bears on |
|---|---|---|
| 1 | Toyota's technical/supply relationships with **Subaru and Suzuki** — what capability is actually being rented, on what terms | Stack rentability; small-player survival |
| 2 | **Honda and Mazda** current position — volume, margin, EV strategy, China exposure | A "bad position" judgment made without data |
| 3 | **Japanese brands' share in third markets** — Europe, Australia, SE Asia, Latin America | The displacement measure behind the wall-gradient finding |
| 4 | **CATL and BYD solid-state** progress against the stated 2027 pilot target; **semi-solid deployment** (MG, CALB, Sunwoda); China's solid-state standard | Entry 004's leapfrog thesis — the 2027 convergence |
| 5 | **Korean battery makers' Q2/Q3 2026** results and ESS pivot execution (LGES, Samsung SDI, SK On) | Korea exiting the EV-cell contest rather than defending it |
| 6 | **European cell capacity post-Northvolt** — Lyten's use of the acquired assets; who is actually building in Europe | Rents-without-stack, European control case |
| 7 | **Renault / Dacia H1 2026** volume and margin, against VW's mass brands | A proposed test: is diffusion exposure about premium mix or about competing on the challenger's axis |
| 8 | **Leapmotor's Stellantis and FAW stakes** — current percentages and any change | Confirmed at ~20% and ~5%; check for movement |

Prefer primary sources. Where a claim is contested across sources, **record the
disagreement rather than picking a side.**

---

## 4. Job 2 — slot maintenance

Write only to `slots.*`: `value`, `unit`, `delta`, `date`, `source`, `source_type`,
`confidence`. One slot write = one commit carrying source and date.

**Write sourced quantities. Do not write ratings.** "BYD Q2 2026 gross margin 18.7%" is a
fact. "BYD's cost position is strong" is a judgment and not yours. Where the board holds a
qualitative value, it was human-set at migration — leave it.

- `source_type`: `primary` for filings, IR, regulators, CPCA/CAAM/statistical agencies;
  `secondary` for press. Record primary where both exist.
- `confidence`: `confirmed` for a filing or company statement; `reported` for press. You
  may promote `reported → confirmed`; never the reverse.
- `delta`: only where stated by the source, or arithmetic on two sourced figures.

**Out of scope for slot writes, unchanged:** Toyota `transition_pace_exposure` (decisive,
custom, needs region-indexing — a judgment call; leave null) · `tariff_exposure` for
004/005/006 (definition still on the repairs backlog — capture quantities to the feed
instead) · any slot whose only available value is a qualitative rating.

---

## 5. Candidates — feed only, never slots

**Leapmotor, Chery, SAIC/MG** have no entries and therefore no slots. Everything goes to
`feed/inbox.md`.

- **Chery** — export standing, HIMA/Luxeed relationship.
- **SAIC/MG** — European volumes; semi-solid battery deployment at the ¥100,000 segment;
  any Connected-Vehicle-Rule-equivalent exposure.

**Do not create an entry, a YAML file, or a slot for any of them.**

---

## 6. Prohibitions

Unchanged. No archetype assignment or normalisation; no loadings; no bet adjudication
("under stress", "weakening"); no ranking; no prose writes; no threshold resolution; no
new entries; no edits to `archetypes.md` or `findings.md`; no qualitative ratings in slots.

If the validator surfaces something broken, **report it, do not repair it.**

---

## 7. Reporting — capped

**The artifacts are the report.** `feed/inbox.md` and the slot commits show what was found.
Do not restate them.

**One brief, under one page**, covering only what the artifacts cannot say:

- which case §0 found;
- the eight verification results, one line each — confirmed / refuted / not found;
- items that qualified but were left at the cap;
- searches that came back empty, and for which slot;
- anything that looked like it needed a judgment call, named and deferred;
- the fence report — every path read or written.

Do not summarise the feed. Do not narrate the process.

---

## 8. Acceptance

- [ ] §0 case stated in one line.
- [ ] `feed/inbox.md` populated; every item deduped against `absorbed.yaml`.
- [ ] All eight verification targets addressed, including any "not found".
- [ ] Slot writes carry `source`, `source_type`, `confidence`, `date`. No ratings.
- [ ] Toyota `transition_pace_exposure` still null; no `tariff_exposure` seeded.
- [ ] Nothing written outside `feed/` and entry `.yaml` `slots.*`.
- [ ] `python3 tools/validate.py` → `validate: ok`, no Rule D warnings.
- [ ] One commit per slot write; feed commits prefixed `feed:`. Local only.
- [ ] One brief, under a page.

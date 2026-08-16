---
doc_id: 20260816_AURORA_BUILD_pharma-feed-harness_v1.0
title: "Build instruction — pharma feed intake harness with asymmetric calibration"
project: Aurora
type: build instruction
version: 1.0
date: 2026-08-16
added_by: Nina
endorsed_by: Elle
status: active — layer 1 only
supersedes: none
related: 20260816_AURORA_HANDOFF_pharma-instance-port_v1.0
---

# Build instruction — pharma feed harness

**Addressed to:** Claude Code instance, Dalila.
**Requires:** web search capability. If the executing instance has no external
retrieval, stop and report — do not substitute model-recalled items for retrieved
ones. A feed of remembered facts is not a feed.

---

## 0. Scope arrest

This builds **layer 1 only** — loose news intake for the Aurora pharma instance.

It does **not** build a player board, an archetype registry, slot schemas, a
valuation model, or any board-adjacent structure. If execution appears to require
any of those, **stop and report** rather than extending scope. The automotive
instance spent roughly three weeks on tooling against one month of analysis; that
ratio is the failure this clause exists to prevent.

Repo fence: all writes confined to `GrandPlan/Aurora/pharma/feed/`. No writes
outside that path. No writes to any file listed in §2 as human-owned.

---

## 1. What this builds

A recurring search harness that retrieves candidate items, records them in a
machine-readable feed, and **calibrates its own retrieval behaviour** against the
one human signal the system emits: the promote flag.

The harness never decides what matters. It decides **where to look**, and it
learns that from where looking has previously paid off.

---

## 2. The boundary

Enforced by file format and directory permission, not by policy.

| Path | Owner | Tool access |
|---|---|---|
| `feed/seeds.md` | Human (Héctor) | **read-only** |
| `feed/rules.md` | Human (Héctor) | **read-only** |
| `feed/items.yaml` | Tool | read/write |
| `feed/queries.yaml` | Tool | read/write |
| `feed/sources.yaml` | Tool | read/write |
| `feed/entities.yaml` | Tool | read/write |
| `feed/_reports/` | Tool | write (append-only) |
| `feed/_graveyard/` | Tool | write (append-only) |

`seeds.md` holds the seed query set and the promote criteria. Both are judgment.
The tool reads them and may never write to them. If the harness concludes the
criteria are wrong, it says so in a report; it does not act on that conclusion.

---

## 3. Feed record schema

`items.yaml` — one record per candidate. Deliberately thin. Layer 1 is looser than
corpus protocol by design.

```yaml
- id: 20260816-0007
  date_seen: 2026-08-16
  date_published: 2026-08-14
  headline: "<as published, verbatim, one line>"
  why: "<one clause — the tool's guess at why this might matter>"
  url: "<canonical URL>"
  source_domain: "<domain>"
  entities: [<named firms, agencies, jurisdictions>]
  query_id: q034
  lane: main            # main | provisional | exploration
  promote: null         # null | true | false  — HUMAN WRITES THIS FIELD
```

`promote` is the only field carrying judgment and the only field the tool must
never populate. It initialises `null` and stays `null` until Héctor sets it.

`why` is a guess, explicitly labelled as such, and carries no weight in
calibration. Only `promote` does.

---

## 4. Cycle

One cycle = one intake pass.

1. Load `seeds.md`, `queries.yaml`, `sources.yaml`.
2. Assemble the cycle's query budget (§6).
3. Execute retrieval. Deduplicate against existing `items.yaml` by URL and by
   near-identical headline.
4. Append new records with `promote: null`.
5. Update yield statistics (§5) using promote flags set since the last cycle.
6. Write the cycle report to `_reports/`.

Default cadence: every 48 hours. Adaptive within bounds (§5.4).

---

## 5. What calibrates

Four channels. All operate on **counts of promote flags** — a human signal — not
on content judgment.

### 5.1 Query yield

Each query in `queries.yaml` carries a rolling window (last 20 items it surfaced)
recording returns, promotes, and rejections.

- **Auto-retire (permitted).** A query that surfaces ≥15 items with zero promotes
  is moved to `_graveyard/queries_retired.yaml` with its full record. Retirement
  is reversible by Héctor and never deletes provenance.
- **Auto-propose (permitted, quarantined).** Terms recurring across ≥3 promoted
  items that do not appear in any active query may be composed into a new query
  and written to the **provisional lane**. Cap: 3 new provisional queries per
  cycle.
- **Graduation (evidence-gated).** A provisional query moves to the main lane only
  after it has surfaced at least one item Héctor promoted. Until then its items
  are tagged `lane: provisional` and reported separately.

The asymmetry is deliberate. Retiring a dead query is a fact about yield and
cannot steer the feed. Adding a query *can* steer it, so an added query must earn
its place against the human signal before it counts.

### 5.2 Source yield

`sources.yaml` tracks promote rate by domain. Low-yield domains are
**down-weighted** in ranking — never blocked. Blocking a source is an editorial
judgment and belongs to Héctor. Weights are bounded below at 0.2 so a
down-weighted source can recover.

### 5.3 Entity emergence

`entities.yaml` counts named entities appearing in **promoted** items only. Rising
counts are surfaced in the report as an observation.

The harness **does not nominate board entries.** Entry is by basis gap, not by
frequency, and frequency is exactly the criterion that would rebuild a leaderboard
through the back door. The counter reports; Héctor and Elle decide.

### 5.4 Cadence

If promoted items per cycle exceed 6, shorten the interval by 12 hours. If below
1 across three consecutive cycles, lengthen by 24 hours. Bounds: 24h floor, 168h
ceiling.

### 5.5 What never calibrates

Hard-coded exclusions from every adaptive channel:

- the promote criteria in `seeds.md`
- any archetype, pole, or classification structure (none exists yet, and this
  harness must not create one)
- the `why` field's influence on ranking (it has none, permanently)
- source blocking
- board entry

---

## 6. Exploration reserve

**25% of each cycle's query budget** is drawn from the exploration set: queries
over jurisdictions, mechanisms, and firm classes with **zero promotes to date**.
Rotating, never retired by the §5.1 rule, exempt from yield pressure.

Without this, a promote-calibrated feed converges on its own priors within a
handful of cycles — it finds more of what it already found, the promote rate rises,
and the narrowing reads as success. The exploration lane is the cost paid to keep
the feed capable of surprise. It is not a tuning parameter.

---

## 7. Cold start

The harness has no promote history at cycle 1 and cannot calibrate on nothing.

**Cycles 1–3: all calibration disabled.** Seed queries only, flat source weights,
fixed 48h cadence, exploration reserve still active. Reports must state
`calibration: inactive (cold start, cycle N of 3)` rather than presenting flat
weights as learned ones.

Calibration activates at cycle 4 **or** at 10 accumulated promote flags,
whichever is later.

---

## 8. Cycle report

Written to `_reports/YYYYMMDD_HHMM_cycle.md`. Machine-authored, marked as such.
Short. Contents:

- items retrieved, by lane
- promotes recorded since last cycle
- queries retired this cycle, with their zero-yield records
- provisional queries added, and any graduated
- source weight changes
- entity counts that moved
- **calibration state and confidence** — explicitly including "insufficient
  signal" when true
- anything the harness noticed that it was not built to handle

The last item matters. A harness that cannot report its own inadequacy will
silently mis-serve the instance.

---

## 9. Seed queries

Live in `seeds.md`, human-owned, tool-read-only. Initial set supplied separately
by Héctor. Suggested coverage, offered as a starting point and not as a
specification: loss-of-exclusivity schedules and patent cliffs; biosimilar and
generic entry events; M&A, licensing and in-licensing (the rent-replacement
channel); India and China in generics, APIs and precursors; AI-in-discovery deals
and platform partnerships; payer and pricing actions across the US, EU, Japan and
major middle-income systems; CDMO and fill-finish capacity; regulatory decisions
at FDA, EMA, NMPA, PMDA and CDSCO; export-control and supply-security instruments;
national pharmaceutical industrial policy.

These encode a guess about what matters. That is why they are Héctor's file and
not the harness's.

---

## 10. Out of scope — stop and report if reached

- any player board, archetype set, or classification structure
- promotion of feed items into board entries
- the back-office capitalisation model (blocked on the board's firm set)
- valuation, price, or market-cap data ingestion of any kind
- linking to DFD, the OLG core, or any other project
- PROTO-RAG-001 frontmatter on feed items (layer 1 is deliberately outside corpus
  protocol; the promote flag is the only bridge upward)

---

## 11. Acceptance

The build is complete when: a cycle runs end to end against live retrieval;
`items.yaml` populates with `promote: null` throughout; the harness demonstrably
cannot write to `seeds.md` or `rules.md`; a cycle report is produced stating cold-
start status; and a simulated set of promote flags is shown to move query, source,
entity and cadence state in the directions specified, with provisional queries
correctly withheld from the main lane until graduated.

Report completion with the first cycle's output attached. Do not proceed to a
second cycle without Héctor's confirmation that the first looks right.

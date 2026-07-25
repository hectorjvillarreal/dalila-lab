---
doc_id: 20260724_AURORA_BUILD_automotive-board-tooling_v1.1
title: "Automotive Player Board — Tooling Build Instructions"
project: Aurora
type: build_instruction
version: 1.1
supersedes: 20260724_AURORA_BUILD_auto-apparatus-tooling_v1.0   # retained as provenance, do not delete
date: 2026-07-24
added_by: Elle
endorsed_by:            # empty = review pending (Fina — methodology / provenance)
corpus_status: pending  # Débb's call — see §11
---

# BUILD INSTRUCTIONS — Automotive Player Board Tooling

**For:** Claude Code, agentic session
**Runtime:** Python 3.11+, stdlib + PyYAML only. CPU-trivial. No GPU, no services, no database, no network unless §6.2 is explicitly enabled.

---

## 0. STOP — read this before anything else

### 0.1 This document is about **cars**

"Auto" in this document has **never** meant *automated*. It means **automotive** — the motor vehicle industry: BYD, Geely, Toyota, Volkswagen, Tesla, Hyundai.

**On 2026-07-24 a prior session read "auto-apparatus" as *automated apparatus* and built a register obligation scanner instead** — competent work, wrong object — and then continued into corpus maintenance it had no mandate for. That incident is the reason for §0.2 and §0.3. The word "auto" has been retired from this project's vocabulary; if you encounter it in an older document, it is ambiguous and you should stop rather than infer.

- This build → `automotive-board/`
- The existing register scanner → `auto-apparatus/` (**built, committed, pushed — not yours, do not touch**)

### 0.2 Repo fence — absolute

You operate **inside your build directory only.**

You may read the two source documents named in §1 and write inside the build tree. **You may not read, list, index, modify, move, rename, archive, or commit anything else** — in particular anything under a corpus, register, `_crossrefs/`, `design_log/`, or an existing project directory. Do not `cd` out of the build tree. Do not `find` or `grep` above it.

Build in an isolated location first (e.g. `~/build/automotive-board/`). Installation into the wider tree happens **after** acceptance (§9), **by Héctor**, not by you.

### 0.3 Scope arrest

If a task appears to require any of the following, **stop immediately and report**. Do not proceed, do not improvise a workaround, do not do it "just to be helpful":

- reading or writing outside the build tree;
- touching an approval, endorsement, version, or status field in any document;
- moving, archiving, or renaming existing files;
- resolving, ratifying, or bumping anything;
- creating documents that look like corpus entries.

A report costs a message. Proceeding costs a governance incident.

### 0.4 Why the other constraints are not stylistic

You are building maintenance infrastructure for an analytical instrument **you must not operate.**

The board classifies automotive players by *strategic archetype*. Its archetype poles are under active revision: two of six cracked within two days of contact with data (Toyota's conflated a *hedge* with *transition-tempo skepticism*; Geely's conflated *segment span* with *legitimacy assets*). A classification basis whose elements are still splitting cannot be computed against — loadings taken at different vintages would silently measure different things.

That is why §8 is hard. Those are empirical findings, not preferences. An agent that "helpfully" normalises archetype labels, scores players, or infers a loading has destroyed the instrument's central discipline.

---

## 1. Sources

Read both before writing code. They will be placed in your build directory:

- `automotive_player_board.md` — the artefact being migrated. Seven entries, ~39KB.
- `automotive_apparatus_build_spec.md` — design rationale. **This document supersedes it where they differ.**

These are the only files you may read from outside your own output.

---

## 2. The one rule

> **Facts are mechanical and basis-independent → automate.**
> **Classification is judgment and basis-dependent → never automate.**

Enforced **structurally**, not by policy. Every board entry becomes:

- **prose** — archetype, loadings, the bet, the reading, watch items, status narrative. *Human-owned. The tool has no write path here.*
- **a YAML block** — slot values, dates, sources, confidence. *Tool-writable.*

The tool cannot cross the line because the format gives it nowhere to write.

---

## 3. Repo layout — create exactly this

```
automotive-board/
├── README.md
├── CLAUDE.md                     # session fence — provided, do not edit
├── scaffold/                     # INVARIANT. Portable to other industries.
│   ├── entry-template.md
│   ├── slot-registry.yaml
│   ├── pipeline.md
│   └── discipline.md
├── instances/
│   └── automotive/
│       ├── archetypes.md
│       ├── findings.md
│       ├── board/
│       │   ├── 001-geely.md      # prose
│       │   ├── 001-geely.yaml    # facts
│       │   ├── 002-byd.md
│       │   ├── 002-byd.yaml
│       │   └── ...               # through 007-hyundai
│       ├── feed/
│       │   ├── inbox.md
│       │   ├── absorbed.yaml     # dedupe ledger — §6.1
│       │   └── promoted/
│       └── thresholds.yaml
└── tools/
    ├── validate.py
    ├── thresholds.py
    ├── betcheck.py
    └── requirements.txt
```

**`scaffold/` must contain nothing industry-specific.** No player names, no EV terminology, no China. The pharma port is `cp -r scaffold/` + a new `instances/pharma/`. If a sentence in `scaffold/` would be false for a pharmaceutical industry board, it belongs in `instances/automotive/`. Apply this test line by line.

---

## 4. Migration — the delicate task

Split each of the seven entries into a `.md` (prose) / `.yaml` (facts) pair.

1. **Prose is copied verbatim.** Do not rewrite, summarise, tidy, or re-order. Preserve emphasis, em-dashes, dated parentheticals. If prose reads awkwardly, leave it awkward.
2. **Extract facts only.** A number, date, proper noun, event, or source URL → YAML. An interpretation → prose.
3. **Mixed lines split, and the judgment half stays in prose.** Example from entry 001:
   > `` `vertical_integration`: high — **and now partly a liability** (see the constraint, Scaffold) ``

   → YAML gets `vertical_integration: {value: "high"}`. *"and now partly a liability"* is judgment and **stays in the prose file**. Never discard it; never move it into YAML.
4. **When in doubt, leave it in prose.** Under-extraction is recoverable. Over-extraction silently converts judgment into data.
5. **Lose nothing.** Every byte of the original lands in exactly one of the two files. Verify with the completeness pass (§9).

**Also split the board's current "Scaffold" section:**

- Invariant discipline → `scaffold/discipline.md` — *archetype-not-ranking*; *poles unbundle under data, and that is the instrument refining, not failing*; *entry is by basis gap*; *thresholds carry dates*; *single-exemplar poles inherit their setter's incidental correlations*.
- Instance findings → `instances/automotive/findings.md` — integration ⊥ legitimacy, the synthetic chokepoint, the wall gradient, the regime change, shakeouts-have-institutional-forms, the level limitation.

Where a finding is *stated* in automotive terms but *portable* in form (several are marked "portable to pharma"), put the automotive statement in `findings.md`, the abstracted form in `discipline.md`, and cross-reference by anchor.

---

## 5. Schema

### 5.1 Entry YAML

```yaml
id: "002"
player: "BYD"
archetype_ref: "pure-diffusion-integrator"   # READ-ONLY pointer into archetypes.md
slots:
  volume_domestic:
    value: "990,900"
    unit: "units — China retail, H1-2026"
    delta: "-38.5% YoY"
    date: 2026-07-16
    source: "https://autotech.news/..."
    source_type: secondary        # primary | secondary
    confidence: confirmed         # reported | confirmed
    decisive: true                # READ-ONLY — set by hand from the entry's bet
```

**Tool-writable:** `value`, `unit`, `delta`, `date`, `source`, `source_type`, `confidence` — and only inside `slots.*`.
**Read-only:** every other key in every file, including `decisive` and `archetype_ref`.

### 5.2 Field notes

- **`confidence: reported | confirmed`** — mandatory. The distinction arose 2026-06-26 (a press report of a VW restructuring plan) and was vindicated 2026-07-09, when the reported plan did not survive the supervisory board. It has already prevented one false belief. A slot may be promoted `reported → confirmed`; the reverse requires a human.
- **`source_type: primary | secondary`** — filing / IR / regulator / statistical agency vs press. Prefer primary; where both exist, record primary.
- **`decisive: bool`** — derived from the entry's falsifiable bet, set by hand. **The hinge of the design:** it lets `betcheck.py` report on a bet without ever interpreting one.

### 5.3 `thresholds.yaml`

```yaml
- id: TH-003
  entry: "004"
  description: "JAMA harness specifications agreed"
  due: 2027-12-31
  status: open          # open | resolved — HUMAN-set
  due_passed: false     # tool-set, mechanical
  resolution: ""        # human-written
```

Seed from the board. At minimum: JAMA harness specs (004, due 2027-12-31); Volvo US authorization survival (001, review 2027-01-01); Lotus/smart adjudication (001, open, no date); Atlas on the HMGMA floor (007, due 2028-12-31).

`due_passed` is mechanical. `status: resolved` and `resolution` are judgment. **The tool never resolves a threshold.**

---

## 6. The three jobs

### 6.1 Job 1 — feed maintenance

Items are one line: date · one-clause "why this might matter" · URL. **No schema beyond that** — deliberately looser than the wider corpus protocol, and explicitly **outside PROTO-RAG-001 scope**.

**Dedupe is a first-class requirement.** On 2026-07-24 an item absorbed on 2026-07-20 was re-submitted, and neither party could tell without opening a 39KB file. `absorbed.yaml` is the ledger:

```yaml
- url: "https://www.carexpert.com.au/car-news/toyota-executive-..."
  url_normalised: "carexpert.com.au/car-news/toyota-executive-wants-all-japanese..."
  absorbed: 2026-07-20
  entries_touched: ["004"]
  scaffold_touched: true
```

Normalise before comparing (strip `?amp`, tracking params, trailing slashes, `www.`, scheme). On a match, report *"already absorbed 2026-07-20, touched entry 004"* and stop.

The tool **may** flag that an item's text matches a watch-item string. It **may not** decide the item changes anything. Promotion is a human call.

### 6.2 Job 2 — slot maintenance

Update factual slots from feed items and sources. **One slot write = one git commit**, message per §7.

Implement fetching behind an explicit `--fetch` flag, **off by default**. The capability should exist; activation is Héctor's decision and is still open (§11.4). Absent that flag the tool makes no network calls.

### 6.3 Job 3 — thresholds and bet-status

`thresholds.py` — list thresholds whose `due` has passed with `status: open`; list those due within 30 days. *This job alone justifies the build: a threshold booked for 2026-07-09 was checked on 2026-07-14, five days late, by accident.*

`betcheck.py` — per entry, report slots with `decisive: true` whose `value` or `date` changed since a reference (default: last run, stored in `.betcheck-state.json`).

**Output is a flag. Never a verdict.**

```
✅  002 BYD · volume_domestic (decisive) · -38.5% · 2026-07-16 · review
❌  002 BYD · bet under stress
❌  002 BYD · bet failing — diffusion thesis weakening
```

The tool detects movement; Elle adjudicates meaning. Emitting anything resembling the second or third line is a build failure.

### 6.4 `validate.py`

1. Schema conformance across all entry YAML and `thresholds.yaml`.
2. Every `.md` in `board/` has a matching `.yaml`, and vice versa.
3. **`--check-boundary`**: diff the working tree (or a commit range) against HEAD and **fail** if any read-only key changed. The automation boundary enforced mechanically rather than trusted. Wire as a pre-commit hook.
4. `scaffold/` purity check: warn on industry-specific vocabulary (configurable term list — player names, "EV", "China", "tariff"). Warning, not error; a human judges.

---

## 7. Git conventions

`git init` inside the build tree. **Local only — do not add a remote, do not push.** Installation and remote wiring are Héctor's, post-acceptance.

```
slot(002): volume_domestic -38.5% H1-2026 · confirmed
  source: https://autotech.news/...
  source_type: secondary
```

Prefixes: `slot(NNN):` · `feed:` · `threshold(TH-NNN):` · `prose(NNN):` (human commits only) · `scaffold:` · `tool:`.

**Git history is the provenance chain.** No database at this scale — that would be infrastructure ahead of content. History is what makes tool auto-write safe: auditable and revertible.

---

## 8. Prohibitions — hard

The tool must never:

1. assign, change, normalise, or suggest an archetype;
2. compute, store, or suggest loadings, weights, scores, or coordinates;
3. declare a bet alive, dead, stressed, strengthening, or weakening;
4. rank or order players by any metric — **the board tracks a tournament, not a leaderboard**;
5. write any prose field, or any key not listed as writable in §5.1;
6. resolve a threshold or set `status: resolved`;
7. apply PROTO-RAG-001 frontmatter to the feed;
8. add, merge, or retire a player — entry is by **basis gap**, by hand;
9. "improve" the archetype set, the slot registry, or `discipline.md`.

If a requested change would require any of these, stop and report.

---

## 9. Acceptance criteria

- [ ] **Fence report:** a list of every path read or written during the session. **Nothing outside the build tree except the two §1 sources.** This is the first criterion checked.
- [ ] No remote configured; nothing pushed.
- [ ] Repo layout matches §3 exactly.
- [ ] Seven entries migrated to prose/YAML pairs.
- [ ] **Completeness:** a reconstruction script concatenating prose + rendered YAML reproduces the substantive content of the source board with no lost facts and no lost judgments. Report any deliberate omission.
- [ ] `scaffold/` contains no industry-specific content (§3 test, line by line).
- [ ] `validate.py` passes on the migrated tree.
- [ ] `validate.py --check-boundary` **fails** on a deliberately-introduced read-only edit. *Demonstrate this — it is the proof the boundary is structural.*
- [ ] `thresholds.py` surfaces a back-dated test threshold.
- [ ] `betcheck.py` flags a decisive-slot change and emits no verdict language.
- [ ] Dedupe: re-submitting the CarExpert URL (with and without `?amp`) returns *already absorbed*.
- [ ] Git history: one commit per logical change, messages per §7.
- [ ] `README.md` states the §2 rule in its first ten lines, and the §0.1 disambiguation above it.

---

## 10. Out of scope — do not build

- **ABM / Layer 3.** Deferred pending explicit trigger. The pipeline runs board → model, never model → board.
- **Quantified loadings.** Gated behind three simultaneous conditions (ABM committed; continuous parameters required; too many players to hand-set). Even then: frozen snapshot only, labelled a simplification.
- **A Claude Skill.** `scaffold/` is its future content; activation is gated on the scaffold surviving one full instance.
- **The pharma instance.** Later. `scaffold/` must merely make it cheap.
- **Anything touching the register scanner at `auto-apparatus/`.**
- **A web UI, dashboard, database, or scheduler.** Cadence is on-demand plus a weekly sweep (§11.5).

---

## 11. Open decisions — do not resolve unilaterally

1. **Installation path.** Proposed: `GrandPlan/Aurora/automotive-board/`. Héctor confirms. **You build in isolation regardless (§0.2).**
2. **Corpus status — Débb.** Is the board a corpus entry or an instrument? *Elle's instinct: instrument. Derived outputs (memos, papers) are corpus; the board is a thinking object under active revision. Not Elle's authority.*
3. **Provenance sufficiency — Fina.** Is git history enough, or does this need formal filing under `_crossrefs/_build_instructions/`? This document is itself a build instruction and should probably be filed as one.
4. **Fetching — Héctor.** Capability built, default off. Elle's recommendation is to enable: the feed has been hand-run four times, each a human doing the tool's job.
5. **Cadence — Fina.** Proposed: on demand + weekly sweep. Not real-time.

---

## 12. Carried backlog — hand work, not tool work

Listed so the build does not obscure it. **Do not attempt any of these.**

- Split the Toyota pole three ways (hedge ≠ tempo-skepticism ≠ system coordination).
- Split the Geely pole (segment span ≠ legitimacy assets).
- Back-fill `tariff_exposure` for entries 004 / 005 / 006.
- Region-index `transition_pace_exposure`.
- Decide whether a **coalition register** is needed alongside the firm-level board.
- **Pair-completion cohort** — a second exemplar per pole. *Single-exemplar poles inherit their setter's incidental correlations; entry 003 is the only two-exemplar pole and the only one that has not cracked.* Candidates: Leapmotor; Chery + SAIC as an SOE / stack-partner pair.

---

## Changelog

**v1.1 (2026-07-24)** — issued after a session misread "auto-apparatus" as *automated apparatus*, built a register obligation scanner, and continued into corpus maintenance outside its mandate. Changes: "auto" retired throughout in favour of "automotive" (§0.1); repo fence added (§0.2); scope-arrest clause added (§0.3); isolated build required, installation deferred to Héctor (§0.2, §11.1); local git only, no remote (§7); fence report added as first acceptance criterion (§9); register scanner named as explicitly out of scope (§10). No change to the schema, the three jobs, the prohibitions, or the design rationale.

**v1.0 (2026-07-24)** — initial. Retained as provenance; superseded, not deleted.

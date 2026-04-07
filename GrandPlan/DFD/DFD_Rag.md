# CLAUDE.md — DFD Project Orientation
# GrandPlan/DFD/
# Maintained by: Anne (population economics) and Debb (infrastructure)
# Last updated: 2026-04-05
# Status: April scaffold version — provisional, evolves as corpus fills out

---

## 1. What this file is for

This file orients Claude Code at the start of every session working inside
GrandPlan/DFD/. Read it fully before touching any file. It tells you what this
project is, what the current state of work is, how to retrieve context from the
RAG corpus, and what the standing scientific assumptions are.

Do not skip the retrieval steps in Section 3. Context from the corpus is not
optional decoration — it is how you avoid repeating work, contradicting prior
decisions, or recalibrating parameters that have already been locked.

---

## 2. Project identity

**DFD (Demographic Fiscal Dynamics)** is the demographic-fiscal simulation
engine at the center of the Grand Plan. Its purpose is to model how demographic
transition — falling fertility, rising life expectancy, shifting age structure —
reshapes fiscal sustainability in Latin American economies.

The core modeling framework is an **OLG (overlapping generations) model**
integrated with **NTA (National Transfer Accounts)** age profiles. Mexico is
the primary calibration context. The June 2026 deliverable is a fully
calibrated, documented Mexico OLG baseline steady state committed to the
repository.

DFD feeds into and is fed by other Grand Plan projects (BDH, RF, Aurora) and
by funded and unfunded Missions. Cross-references are tracked in
`_crossrefs/mission-project-map.md`.

**Guiding principle:** The simulation engine must be fully operational before
any specialized language model training begins. Demographic microfoundations
determine the quality of everything built above them.

---

## 3. RAG retrieval protocol — run at session start

Before beginning any substantive work, execute the following two retrieval
queries against the DFD corpus. Record what each returns in your session
scratchpad.

### Query A — Recent changes (continuity)

Retrieve documents created or modified in the last 7 days. Target directories:

```
GrandPlan/DFD/model/
GrandPlan/DFD/calibration/
GrandPlan/DFD/data/
GrandPlan/DFD/docs/
GrandPlan/DFD/experiments/
```

Also retrieve the 5 most recent Git commit messages from this repository.

**Purpose:** Establish what changed since the last session. Do not assume
continuity from your own context — the corpus is the ground truth.

**If nothing is returned:** The corpus is empty or the session is the first.
Proceed to Section 4 and note this in the session log.

### Query B — Component context (validation)

Retrieve documents relevant to the specific component you have been asked to
work on in this session. Use the component name, parameter identifiers, and
data source labels as query terms.

Examples:
- Working on fertility parameterization → query: `TFR CELADE mexico baseline`
- Working on pension calibration → query: `pension replacement rate NTA fiscal`
- Working on the OLG core → query: `olg_baseline cohort transition steady state`

**Purpose:** Verify that your planned changes are consistent with prior
calibration decisions and documented assumptions. If the corpus returns a
parameter value or modeling choice that conflicts with what you are about to
do, stop and flag it before proceeding.

---

## 4. Standing scientific context — no retrieval needed

The following is stable reference material injected directly. Do not query the
corpus for this; treat it as always known.

### 4.1 Demographic baseline assumptions

The DFD model operates under three scenario sets — baseline, optimistic, and
stress — calibrated to Latin American data. These must never be conflated.

**Key empirical anchors (as of April 2026):**

- Mexico TFR is approximately **1.55** (2024), below the US TFR of 1.62.
  Mexico has overshot advanced economies in fertility decline — a pattern
  shared across LAC (Colombia 1.06, Chile 1.03, Costa Rica 1.12).
- The global replacement rate is approximately **2.21**, not 2.1. The 2.1
  figure applies only to high-survival, low-sex-ratio-bias contexts.
- Global TFR crossed below replacement in approximately **2023**. Peak births
  globally occurred around **2012**.
- UN WPP 2024 data carries systematic upward bias. Recent censuses (Brazil:
  203M not 212M; Paraguay: 6.1M not 6.9M) confirm level effects. Treat WPP
  2024 as a reference, not a primary calibration source. Cross-check against
  vital registries and CELADE.
- The WPP's projected fertility rebound in low-fertility countries is not
  empirically grounded. DFD scenarios do not assume rebound unless explicitly
  modeled with a documented mechanism.

**Data source hierarchy:**
1. Vital registries (where available and assessed as complete)
2. CELADE / CONAPO / UN Population Division
3. World Bank, CEDLAS, OECD LAC
4. WPP 2024 (use with caution; document any reliance on it)

### 4.2 NTA conventions

All age-profile analysis must be compatible with NTA methodology unless a
departure is explicitly documented in `docs/`. Key profiles:

- Labor income profile (`yl`)
- Consumption profile (`cl`)
- Public transfer inflows and outflows (`tg+`, `tg-`)
- Asset-based reallocations (`ym`, `ys`)

Do not construct age profiles from non-NTA sources without flagging the
departure.

### 4.3 OLG model structure

The model is implemented in Julia. The core file is `model/olg_baseline.jl`.
Key structural features:

- Finite-horizon overlapping generations
- Endogenous health investment (from "Is Health a Blessing?" paper)
- Pension system block (parametric PAYG, calibrated to Mexico IMSS/ISSSTE
  aggregate targets)
- Fiscal block: government budget constraint with debt dynamics

Partial equilibrium is the current scope. General equilibrium extension is
deferred. Any session that touches the model's equilibrium assumptions must
note this boundary explicitly.

### 4.4 Current milestone map

| Period    | Deliverable                                        | Status         |
|-----------|----------------------------------------------------|----------------|
| April     | Scaffold DFD/ folder structure                     | In progress    |
| April     | Draft and commit CLAUDE.md                         | This document  |
| May       | Install Julia environment; verify CUDA.jl, Turing.jl | Not started  |
| June      | Mexico OLG baseline — calibrated and committed     | Not started    |

---

## 5. File and commit conventions

**Before modifying any file:**
- Check Git status. Do not work on a dirty tree without understanding why.
- Read the file header comments. They record authorship, version, and
  dependencies.

**Commit message format:**
```
[component] short imperative description

Optional: one sentence of context if the change is non-obvious.
Refs: #issue or mission ID if applicable.
```

Examples:
```
[calibration] set Mexico TFR baseline to 1.55 (CONAPO 2024)
[model] add cohort survival probability vector to olg_baseline.jl
[data] ingest CELADE 2023 revision for mexico_baseline/
```

Do not commit parameter changes without a source citation in the commit
message or in the associated calibration notebook.

**Two `pdflatex` passes** are required if you generate any LaTeX output from
this project — cross-references will not resolve on a single pass.

---

## 6. What to do when the corpus returns a conflict

If Query B returns a document showing that a parameter or modeling choice
contradicts what you have been asked to do in this session:

1. Do not proceed silently.
2. Surface the conflict explicitly: quote the prior document and the new
   instruction.
3. Ask Héctor to resolve before continuing.

This is not a failure mode — it is the corpus doing its job.

---

## 7. Session log convention

At the end of every session, append a brief entry to `docs/session_log.md`:

```markdown
## YYYY-MM-DD

**Retrieval A returned:** [summary or "corpus empty"]
**Retrieval B query:** [terms used]
**Retrieval B returned:** [summary or "no relevant results"]
**Work completed:** [one paragraph]
**Open issues / flags:** [anything unresolved]
**Commits:** [list of commit hashes and messages]
```

This log is a primary corpus document. It is the connective tissue between
sessions. Write it as if the next reader has no memory of this session —
because they won't.

---

## 8. Contacts

| Question about...                        | Contact |
|------------------------------------------|---------|
| OLG model structure, demographic params  | Anne    |
| File conventions, infrastructure, Git    | Debb    |
| Fiscal block, pension parameters         | Beth    |
| DSGE extensions, GE closure              | Cath    |
| Strategic priorities, scope decisions    | Héctor  |

---

*This is the April 2026 scaffold version. Sections 3 and 4 will expand as the
corpus fills out through May–June. The retrieval protocol in Section 3 should
be reviewed and tightened once the first 20 corpus documents are ingested.*

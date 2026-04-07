# CLAUDE.md — GrandPlan/
# Project-level orientation for Claude Code
# Owner: Héctor Juan Villarreal Páez
# Last updated: 2026-04-01
# Status: Initial version — update as projects develop

---

## 1. What this folder is

GrandPlan/ contains the four active research projects that form the core of the
Grand Plan: DFD, BDH, RF, and Aurora. These projects collectively build toward
the 2027 institutional model — a ~13B parameter Latin American fiscal-demographic
language model in partnership with CIEP and ITED (Tec de Monterrey).

For full Grand Plan context, see the master CLAUDE.md at the Dalila root.

---

## 2. Folder structure

```
GrandPlan/
├── DFD/       # Demographic Fiscal Dynamics — OLG/DSGE simulation engine
├── BDH/       # Health system financing in Latin America (IADB)
├── RF/        # Mexico Fiscal Narrative Dataset (RAG + LLM extraction)
└── Aurora/    # Strategic foresight (TetraDevelopment)
```

Each project folder contains its own CLAUDE.md with project-specific detail.

---

## 3. Projects at a glance

### DFD — Demographic Fiscal Dynamics
- **Core purpose**: integrate demographic dynamics with fiscal policy via OLG/DSGE
- **Current status**: OLG baseline confirmed; calibration to LA data is next
- **Primary language**: Julia (simulation) + Python (data pipeline)
- **Immediate target**: Mexico baseline OLG steady state (June 2026)
- **Data sources**: CELADE · CEDLAS · OECD Revenue Statistics LA · NTA profiles

### BDH — Health System Financing
- **Core purpose**: financing health systems in Latin America
- **Current status**: migrating from ChatGPT to Claude (April–May 2026)
- **Structure**: two components reporting to different IADB divisions
- **Language**: bilingual Spanish/English
- **Note**: several Missions live inside BDH or feed it directly

### RF — Mexico Fiscal Narrative Dataset (2000–2025)
- **Core purpose**: RAG + LLM extraction of fiscal policy events connected to
  demographic channels
- **Current status**: RAG protocol PROTO-RAG-001 approved; CROSS-TAR-001 is next
- **Primary language**: Python (RAG pipeline)
- **Corpus location**: GrandPlan/RF/corpus/

### Aurora / TetraDevelopment
- **Core purpose**: strategic foresight across genomics, fusion, quantum computing,
  and strategic reasoning
- **Current status**: active; context partially migrated from ChatGPT
- **Key document**: "The Four Pillars of Post-LLM Intelligence"
- **Aphorism**: "We build theories to understand the future, and balance sheets to
  discover whether the future will let us."
- **June target**: first structured foresight experiments on Dalila

---

## 4. Shared conventions across all GrandPlan projects

### Language choice
- Julia: all numerical simulation (OLG, DSGE, fiscal modules)
- Python: data pipelines, RAG, ML workloads, embeddings

### Commit format (Conventional Commits)
- `feat:` new model feature or module
- `fix:` bug or calibration correction
- `data:` data ingestion or processing
- `model:` parameter or structural model change
- `doc:` documentation update

### Branching
- `main`: stable, reviewed code only
- `exp/[scenario-name]`: experimental calibration or scenario branches
- Never run destructive experiments on `main`

### Documentation rule
Every script and simulation module gets a companion `.md` file explaining:
- purpose and inputs
- outputs and units
- calibration assumptions
- known limitations

### Session management
Use Zellij for any job expected to run > 5 minutes. Name sessions descriptively:
e.g. `zellij attach dfd-calibration-mx`.

---

## 5. The simulation laboratory concept

The four projects collectively build a demographic-fiscal simulation laboratory:
a modular engine capable of running thousands of policy experiments with the local
LLM (Qwen3.5-9B) as the natural language interface.

Module architecture (target state):
- OLG/DSGE core (DFD)
- Demographic module: fertility · mortality · migration (DFD)
- Fiscal module: taxes · transfers · pensions · health spending (DFD + BDH)
- Fiscal narrative layer: policy event extraction (RF)
- Strategic foresight layer (Aurora)

**Design rule**: the simulation engine must be fully operational before any
specialized language model training begins.

---

## 6. Connection to Missions

Several Missions in Missions/funded/ and Missions/unfunded/ connect to projects
in this folder. Before starting work that may overlap with a Mission deliverable,
consult:
- `_crossrefs/mission-project-map.md` — full mission × project matrix
- `Missions/_index.md` — master mission register with status and funding

---

## 7. June–August execution targets

| Month | DFD | BDH | RF | Aurora |
|-------|-----|-----|----|--------|
| June  | Mexico OLG baseline calibrated | Context fully migrated | Local RAG pipeline live | First experiment notebook |
| July  | LA demographic modules added | First BDH simulation run | CROSS-TAR-001 processed | Scenario framework drafted |
| August | Policy experiment distributions | Health spending scenarios | Narrative-fiscal linkages | Foresight report v0.1 |

---

*This file is read automatically by Claude Code when working inside GrandPlan/.
Update it as project status changes. The master orientation document is at
Dalila/CLAUDE.md.*

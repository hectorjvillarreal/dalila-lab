# CLAUDE.md — Dalila Workstation
# Master orientation document for Claude Code
# Owner: Héctor Juan Villarreal Páez
# Last updated: 2026-03-31
# Status: Living document — update weekly alongside the Grand Plan diagram

---

## 1. Who is Héctor

Héctor Juan Villarreal Páez is an academic economist at Tecnológico de Monterrey's
School of Social Sciences and Government. His research focuses on public finance,
demographic economics, fiscal sustainability, and social security systems in Latin
America. He coordinates GARO (Grupo Académico de Reacción Oportuna) at Mexico's
Secretaría de Economía and serves as a reviewer in Mexico's Sistema Nacional de
Investigadores (SNI).

---

## 2. The Grand Plan

The Grand Plan is the integrated strategic roadmap connecting all active work on
Dalila. It has five layers:

1. **Dalila workstation** — the hardware and software foundation (operational)
2. **Local LLM** — Qwen3.5-9B via ollama (decision confirmed May 2026)
3. **Active projects** — DFD, BDH, RF, Aurora (the research engine)
4. **Core Team** — modular AI research agents operating in Claude
5. **2027 institutional model** — ~13B parameter Latin American fiscal-demographic
   language model, in partnership with CIEP and ITED (Tec de Monterrey)

**Preparation phase**: April–May 2026 (infrastructure, context migration, stack)
**Execution phase**: June–August 2026 (calibration, simulation engine, experiments)

Guiding principle: *"Iteration beats optimality when regimes are unstable."*

---

## 3. Dalila hardware and terminal stack

- Machine: Lenovo ThinkPad P1 Gen 8
- GPU: NVIDIA RTX PRO 2000 Blackwell · ~8 GB VRAM · CUDA 13.0
- OS: Ubuntu 24.04 LTS
- Terminal: Ghostty → Zsh → Zellij
- Version control: Git · GitHub via SSH
- Languages: Python (Miniforge) · Julia

All long-running simulation or training jobs should be run inside a Zellij session
to preserve state across terminal disconnections.

---

## 4. File architecture

```
Dalila/
├── GrandPlan/
│   ├── DFD/          # Demographic Fiscal Dynamics
│   ├── BDH/          # Health system financing (IADB)
│   ├── RF/           # Mexico Fiscal Narrative Dataset
│   └── Aurora/       # Strategic foresight (TetraDevelopment)
├── Missions/
│   ├── _index.md     # Master register of all missions
│   ├── funded/       # Active funded missions (real names as folders)
│   └── unfunded/     # Pipeline missions
├── Research/
│   ├── _index.md     # Publications register
│   ├── published/
│   ├── submitted/
│   ├── working-papers/
│   └── ideas/
├── Teaching/
│   ├── Courses/
│   └── Materials/
├── Personal/
│   └── STLP/         # Self-teaching (number theory, mathematics)
└── _crossrefs/
    └── mission-project-map.md  # Mission × project relationship matrix
```

All documentation uses `.md` files. Missions use their real names as folder labels.

---

## 5. Active projects

### DFD — Demographic Fiscal Dynamics
Core research project. Integrates demographic dynamics with fiscal policy using a
DSGE/OLG macroeconomic framework. Connects to National Transfer Accounts (NTA)
methodology. The OLG baseline model is confirmed as a strong demographic
microfoundation. Next step: calibration to Latin American data, starting with Mexico
(CELADE projections, CEDLAS labor data, OECD Revenue Statistics for LA, NTA profiles).

Primary language: Julia (simulation engine) + Python (data pipeline).
Key folder: `GrandPlan/DFD/`

### BDH — Health System Financing
Research initiative on financing health systems in Latin America. Two components
reporting to different IADB divisions. Bilingual (Spanish/English). Several Missions
live inside BDH or feed it directly.

Key folder: `GrandPlan/BDH/`

### RF — Mexico Fiscal Narrative Dataset (2000–2025)
Constructs a dataset using RAG + LLM extraction to identify fiscal policy events and
connect them to demographic channels. Governed by PROTO-RAG-001. Next corpus
document: CROSS-TAR-001.

Key folder: `GrandPlan/RF/`

### Aurora / TetraDevelopment
Strategic foresight framework exploring post-LLM intelligence across genomics, fusion,
quantum computing, and strategic reasoning. Anchored by the internal paper
"The Four Pillars of Post-LLM Intelligence."
Aphorism: *"We build theories to understand the future, and balance sheets to
discover whether the future will let us."*

Key folder: `GrandPlan/Aurora/`

---

## 6. Missions

Missions are specific funded or unfunded tasks that finance and nourish the Grand
Plan. They are tracked independently from projects because they have their own
deliverable timelines and funding logic. Many missions connect to BDH; others connect
to DFD, RF, Aurora, or are autonomous.

Cross-references are maintained in `_crossrefs/mission-project-map.md`.
The master register is `Missions/_index.md`.

---

## 7. Scientific computing stack

### Python ecosystem
- Miniforge (base environment manager) at `~/miniforge3/`; active env `dalila` (Python 3.12) — see `_setup/python_env.md` for activation patterns, package install conventions, and the cu126-wheels-required-for-Blackwell pin
- NumPy · SciPy · Pandas · Matplotlib · Statsmodels
- PyTorch with CUDA 13.0 wheels (`https://download.pytorch.org/whl/cu130`; this is the index that ships sm_120 / Blackwell kernels — `cu126` wheels lack them and fail at runtime with `cudaErrorNoKernelImageForDevice`)
- JAX (`jax[cuda13]`) with the cuda13 plugin — reuses the cu13 NVIDIA libs installed by PyTorch; verified sm_120 dispatch via `tests/gpu_check.py`

### Julia ecosystem
- Julia 1.11.7 at `/usr/local/bin/julia`; default env at `~/.julia/environments/v1.11/`
- CUDA.jl 6.1 (CUDA toolchain 13.2 via JLLs; cuBLAS 13.4) — verified sm_120 dispatch via `tests/gpu_check.jl`
- Plots.jl · Turing.jl (per project Project.toml; not in default env)
- Primary language for OLG/DSGE simulation engine

### Local LLM
- Model: Qwen3.5-9B (decision finalized May 2026)
- Runtime: ollama
- Use: RAG queries, document processing, natural language interface to simulation
- Context window: 262K tokens (sufficient for long fiscal documents)

### RAG protocol
- Governed by PROTO-RAG-001 (approved)
- Next document: CROSS-TAR-001
- Corpus lives in `GrandPlan/RF/` and `GrandPlan/DFD/`

### Protocols

The team operates under formal protocols stored in `_crossrefs/protocols/`. Currently active:

- **PROTO-RAG-001** (`_crossrefs/protocols/PROTO-RAG-001.md`) — Corpus Entry and Build Instruction Protocol. Governs frontmatter schemas, authorship discipline (`added_by`, `endorsed_by`, `opened_by`, `promoted_by`), entry structural conventions, and build instruction retention. Established 2026-04-28.

### Build Instructions Archive

`_crossrefs/_build_instructions/` retains every build instruction indefinitely, treated as the provenance layer of the team's intellectual infrastructure. Every corpus entry, watch item, and protocol document cross-references the build instruction that created it. See `_crossrefs/_build_instructions/README.md`.

### Inequality corpus (`_crossrefs/corpus/inequality/`)

Cross-cutting methodological corpus on income and wealth inequality measurement. Initial scaffold April 2026. Three primary entries from JEP Spring 2025 symposium (Clarke & Kopczuk, Gomez, Auerbach). Shared across DFD, BDH, RF; not duplicated in project subfolders. See `_crossrefs/corpus/inequality/README.md` for organization and standing principles. Open watch item: "automated life for capital" — Hicksian symmetry implication for OLG capital cohort structure.

### Demographics corpus (`_crossrefs/corpus/demographics/`)

Cross-cutting demographics corpus shared across DFD, BDH, and Aurora. Initial scaffold May 2026. Populated incrementally by the `dfd-demographics-monitor` skill (v0.2) on activation; manual additions also conform via `_pending/` endorsement workflow. Scenario anchors (`scenario_anchors.md`) carry provisional TFR values pending Anne's source-pinning. See `_crossrefs/corpus/demographics/README.md` for organization and standing principles.

---

## 8. Core Team

The Core Team is a set of modular AI research agents operating in Claude. When
working on Dalila, treat their domain boundaries as a guide for task decomposition:

- **Anne** — population economics
- **Beth** — social security and health economics
- **Cath** — public finance and modeling
- **Debb** — infrastructure, workflow, and knowledge base
- **Elle** — strategic foresight
- **Fina** — cross-project coherence and cadence
- **Nina** — code documentation; also handles portfolio and personal finance

---

## 9. Coding conventions

- **Commit format**: Conventional Commits — `feat:`, `fix:`, `data:`, `model:`, `doc:`
- **Branching**: stable `main` + experimental branches per calibration scenario
- **Documentation**: every module and simulation script gets a `.md` companion file
- **Session management**: use Zellij for any job expected to run > 5 minutes
- **GPU verification**: run `tests/gpu_check.py` and `tests/gpu_check.jl` after any
  environment change to confirm CUDA is operational
- **Language choice**: Julia for numerical simulation (OLG/DSGE); Python for data
  pipelines, RAG, and ML workloads

---

## 10. 2027 institutional model

Target: ~13 billion parameter Latin American fiscal-demographic language model.
Partners: CIEP (fiscal policy data and credibility) + ITED / Tec de Monterrey
(academic anchor and demographic research tradition).

**Design rule**: the simulation engine must be fully operational before any
specialized language model training begins. The engine's outputs constitute the
training corpus. Quality of the corpus matters more than parameter count.

---

## 11. Key references

- Dalila ecosystem diagram: five-layer SVG, revised weekly
- PROTO-RAG-001: RAG protocol (approved)
- CROSS-TAR-001: next corpus document (in progress)
- mission-project-map.md: mission × project relationship matrix
- Missions/_index.md: master mission register

---

*This file is read automatically by Claude Code at session start.
Update it whenever the Grand Plan, file architecture, or project status changes.
The authoritative version lives at the root of the Dalila repository.*

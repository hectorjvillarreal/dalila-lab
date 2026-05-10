# CLAUDE.md — DFD Project Orientation
# GrandPlan/DFD/
# Maintained by: Anne (population economics) and Debb (infrastructure)
# Last updated: 2026-05-10
# Status: April scaffold version — provisional, evolves as corpus fills out
# Source document integrated: Integrated_6.tex (IM-6, April 2026 draft)

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
integrated with **NTA (National Transfer Accounts)** age profiles. The
theoretical core is **IM-6** (`Integrated_6.tex`), a stochastic OLG model with
endogenous health investment, heterogeneous agents, and a PAYG pension system,
calibrated for México, Costa Rica, and Panamá. Development horizon: 1–2 years.

Mexico is the primary calibration context. The June 2026 deliverable is a
fully calibrated, documented Mexico OLG baseline steady state committed to
the repository.

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
data source labels as query terms. Reference the IM-6 equation labels below
as query anchors when working on the model core.

Examples:
- Working on health capital dynamics → query: `health depreciation delta H_j medical spending`
- Working on pension calibration → query: `pension contribution rate tau_p dependency ratio kappa`
- Working on survival probabilities → query: `psi survival Mexico life table UISP`
- Working on formalization experiment → query: `formal informal partition alpha FTR contribution base`
- Working on the equilibrium → query: `stationary competitive equilibrium market clearing labor capital`

**Purpose:** Verify that your planned changes are consistent with prior
calibration decisions and documented assumptions. If the corpus returns a
parameter value or modeling choice that conflicts with what you are about to
do, stop and flag it before proceeding.

---

## 4. Standing scientific context — no retrieval needed

The following is stable reference material injected directly. Do not query the
corpus for this; treat it as always known.

### 4.1 The integrated model (IM-6) — structure and key equations

The theoretical core of DFD is the model in `Integrated_6.tex`. The full
title is *Spending Smarter under Demographic Pressure: Fiscal Efficiency,
Health, and Gender Dynamics in Latin America* (Ascarza-Mendoza, Cortés,
Judith Méndez, Héctor J. Villarreal; preliminary draft, April 2026,
prepared for IDB Fiscal Division).

**Model class:** Stochastic OLG, discrete time, 5-year periods.
Age range: j = 1 (age 20) to J (age 100). Retirement at j_R (exogenous).

**Agent types:** Two permanent skill types θ ∈ {θ_L, θ_H}. Fixed at birth.
Gender extension expands to four types: θ_L^M, θ_H^M, θ_L^F, θ_H^F.

**Individual state:** s = (a, h, η) — assets, health capital, productivity shock.

**Health capital** is a continuous state variable on [0, h̄]:
```
h' = min{(1 - δ_j^h) · h + H_j(m), h̄}        [eq:worker_health]
```
where δ_j^h is age-dependent depreciation and H_j(m) is the investment
technology with diminishing returns. Health simultaneously affects:
- Survival probability: ψ_{j+1}(h')
- Labor productivity: ν_j(h, η; θ)
- Utility: u(c, ℓ, h) directly (amenity value)

**Labor productivity:**
```
ν_j(h, η; θ) = e_j · exp(η) · [1 - ϱ(θ) · max(h̄ - h, 0)]
```
where e_j is the age-efficiency profile and ϱ(θ) is the health-productivity
sensitivity (higher for θ_L).

**Worker's Bellman equation:**
```
V_j(a, h, η; θ) = max_{c,a',ℓ,m} { u(c, ℓ, h)
    + β · ψ_{j+1}(h') · E[V_{j+1}(a', h', η'; θ) | η] }    [eq:worker_bellman]

subject to:
  (1 + τ^c)·c + (1 + τ^m)·m + a' = x(a, h, η, ℓ; θ)       [eq:worker_budget]
  a' ≥ 0, m ≥ 0, ℓ ∈ [0,1]
```

where household resources are:
```
x(a, h, η, ℓ; θ) = (1 + r(1 - τ^k))·a + w·ν_j(h,η;θ)·ℓ·(1 - τ^ω - τ^p)
```

**Retiree's Bellman equation:** Same structure with ℓ = 0 and pension
transfer p̄ replacing labor income.

**Key FOC — medical spending:**
```
λ_j(1 + τ^m) = β · H_j'(m) · { ψ'_{j+1}(h')·E[V_{j+1}] + ψ_{j+1}(h')·E[V_{h,j+1}] }
```
This is the equation that makes health qualitatively different from other
fiscal instruments — it propagates through both the survival channel and
the continuation value channel simultaneously.

**Euler equation:**
```
u_c(c, ℓ, h) = β·(1 + r(1-τ^k))·ψ_{j+1}(h')·E[u_c(c', ℓ', h') | η]
```

**Fiscal instruments in the model:**
- τ^c: consumption tax (VAT)
- τ^ω: labor income tax
- τ^k: capital income tax
- τ^m: medical expenditure tax/subsidy (negative = subsidy)
- τ^p: pension contribution rate (endogenous)
- κ: pension replacement rate (policy parameter)
- j_R: retirement age (policy parameter)

**Pension contribution rule (endogenous):**
```
τ^p = κ · (N^R / N^W)
```
This is the fiscal amplification loop: aging raises N^R/N^W, which raises
τ^p, which widens the formal-labor tax wedge. Health investment that extends
working lives partially offsets this, but also raises N^R through longer
survival. Net fiscal effect is ambiguous — requires the calibrated GE model.

**Government budget constraint:**
```
τ^c·C + τ^ω·w·L_formal + τ^k·r·K + τ^p·w·L_formal + τ^m·M
    = G + p̄·N^R + (r - n_p)·B
```
where B is government debt. The constraint must close in equilibrium — the
residual is B (debt adjusts). Do not run a policy experiment without
verifying budget balance.

**Market clearing:**
- Labor: L = ∫ ν_j(h,η;θ)·ℓ dμ_j^θ  [eq:labor_market]
- Capital: K = A_dom - B               [eq:capital_market]
- Goods: Y = C + M + δ·K + G + Λ_void [eq:goods_market]

**Voided assets** (accidental bequests):
```
Λ_void = Σ_{θ,j} (1 - ψ̄_{j+1}(θ)) · ∫ a'(s;j,θ) dμ_j^θ
```

**Stationary distribution law of motion:**
```
μ_{j+1}^θ(B) = 1/(1+n_p) · ∫ ψ_{j+1}(h'(s;j,θ)) · [Σ_{η'} Π^η(η,η') · 1[(a',h',η') ∈ B]] dμ_j^θ
```

**Equilibrium uniqueness:** Not guaranteed. Competing income and substitution
effects across cohorts may yield multiple crossings of the excess demand
function. Cath is responsible for verifying numerically over a fine grid
before any policy simulations.

---

### 4.2 Calibration targets — three-country parameters

**Demographics (reference year 2023):**

| Indicator                            | Mexico | Costa Rica | Panama |
|--------------------------------------|--------|------------|--------|
| Life expectancy (total)              | 75.1   | 81.0       | 78.1   |
| Life expectancy (male)               | 72.1   | 78.6       | 75.4   |
| Life expectancy (female)             | 78.3   | 83.5       | 80.9   |
| TFR (births per woman, 2023)         | 1.82   | 1.51       | 2.30   |
| Population aged 65+ (%)              | 8.1    | 10.4       | 8.9    |
| Diabetes prevalence (% adults)       | 16.9   | 9.8        | 11.0   |

Source: PAHOHIA (2024), WHO GHO (2024), World Bank WDI (2024), OECD HaG (2023).

**Mexico survival probabilities** (ψ_j, from UISP 2019 — primary calibration target):

| Age group | Prob. of death | Survival prob. |
|-----------|---------------|----------------|
| < 1 year  | 0.011576      | 0.9884         |
| 1–4       | 0.002282      | 0.9977         |
| 5–9       | 0.001132      | 0.9989         |
| 10–14     | 0.001470      | 0.9985         |
| 15–19     | 0.003858      | 0.9961         |
| 20–24     | 0.005897      | 0.9941         |
| 25–29     | 0.006550      | 0.9935         |
| 30–34     | 0.007966      | 0.9920         |
| 35–39     | 0.011217      | 0.9888         |
| 40–44     | 0.013710      | 0.9863         |
| 45–49     | 0.019216      | 0.9808         |
| 50–54     | 0.028413      | 0.9716         |
| 55–59     | 0.042568      | 0.9574         |
| 60–64     | 0.063162      | 0.9368         |
| 65–69     | 0.093160      | 0.9068         |
| 70–74     | 0.137294      | 0.8627         |
| 75–79     | 0.208926      | 0.7911         |
| 80–84     | 0.312093      | 0.6879         |
| 85+       | 1.000000      | 0.0000         |

**Health expenditure (reference year 2022):**

| Indicator                            | Mexico  | Costa Rica | Panama  |
|--------------------------------------|---------|------------|---------|
| Current health exp. (% GDP)          | 5.5     | 7.1        | 7.8     |
| Public health exp. (% CHE)           | ~51     | ~69        | ~72     |
| Out-of-pocket exp. (% CHE)           | ~41*    | 22.4       | ~26     |
| OOP per capita (USD current)         | ~253    | 220        | ~290    |
| Total health exp. per capita (PPP)   | ~1,100  | 1,658      | ~1,450  |

*Mexico OOP is 2021 vintage. Source: WHO GHED (2024), OECD HaG (2023).
The τ^m subsidy calibration reflects OOP shares — lower OOP implies higher
effective public subsidy, compressing the precautionary savings motive.

**Fiscal parameters:**

| Indicator                              | Mexico    | Costa Rica  | Panama    |
|----------------------------------------|-----------|-------------|-----------|
| Standard VAT rate                      | 16% (IVA) | 13% (IVA)   | 7% (ITBMS)|
| Top personal income tax rate           | 35%       | 25%         | 25%       |
| Social security contributions (total)  | ~30%      | ~37%        | ~19%      |
| General government revenue (% GDP)     | ~23       | ~24         | ~21       |
| Tax revenue (% GDP, 2022)              | ~17       | ~14         | ~12       |

Source: PwC WWTS (2024), OECD Rev Stats (2024), World Bank WDI (2024), CCSS (2023).

Note on Mexico: the 2021 Social Security Law reform introduced a graduated
employer contribution schedule for CEA+V, scaling from 3.15% at 1 minimum
wage to 11.875% at 4.5 UMAs by 2030. The τ^p calibration must account for
this progressive structure — the marginal cost of formalizing a worker is
wage-level dependent.

**Labour market (reference year 2022):**

| Indicator                              | Mexico | Costa Rica | Panama |
|----------------------------------------|--------|------------|--------|
| Male labour force participation (%)    | 76.7   | 72.4       | 77.6   |
| Female labour force participation (%)  | 45.4   | 50.7       | 51.8   |
| Gender participation gap (M/F ratio)   | 1.69   | 1.43       | 1.50   |
| Gender wage gap (% of male wage)       | ~14    | ~18        | ~19    |
| Informality rate (% of employed)       | ~55    | ~43        | ~47    |
| Gini coefficient                       | 0.43   | 0.48       | 0.49   |

Source: ILO ILOSTAT (2023), ECLAC-ILO (2023), IMF (2023), WEF GGR (2024).

**Mexico fiscal health gap:**
Widened from 3.0% to 4.8% of GDP between 2015 and 2024. Actual public
health expenditure (~2.8% of GDP) covers barely a third of demographically
projected requirements. Primary motivation for the model design.

Fiscal gap formula:
```
G_{c,t} = H^est_{c,t} - H^actual_{c,t}
H^est_{c,t} = [Σ_j h(j) · N_{j,c,t}] / Y_{c,t}
```

---

### 4.3 Demographic baseline assumptions

The DFD model operates under three scenario sets — baseline, optimistic, and
stress — calibrated to Latin American data. These must never be conflated.

**Key empirical anchors (as of April 2026):**

- Mexico TFR is approximately **1.55** (2024, fast-transition scenario),
  below the US TFR of 1.62. LAC countries have overshot advanced economies:
  Colombia 1.06, Chile 1.03, Costa Rica 1.12. Note: IM-6 data tables use
  1.82 (2023 WDI vintage) — this is not a conflict; 1.55 is the DFD
  fast-transition scenario value. Document this distinction clearly when
  both appear in the same session.
- The global replacement rate is approximately **2.21**, not 2.1.
- Global TFR crossed below replacement in approximately **2023**. Peak
  births globally occurred around **2012**.
- UN WPP 2024 carries systematic upward bias. Cross-check against vital
  registries and CELADE. Projected fertility rebound is not empirically
  grounded — DFD does not assume rebound.
- **Premature health crossing point:** In Mexico, the proportion of the
  population in poor health crosses 50% at approximately age 60 — a decade
  earlier than the 70–75 range in high-income countries. Among low-skilled
  workers, deterioration begins in the late 40s. This 20-year gap between
  skill groups is the central empirical fact in IM-6 and the motivation for
  the heterogeneous-agent structure.

**Data source hierarchy:**
1. Vital registries (where assessed as complete)
2. CELADE / CONAPO / UN Population Division
3. WHO GHED, PAHOHIA, World Bank WDI, OECD HaG
4. WPP 2024 (use with caution; document any reliance)

---

### 4.4 NTA conventions

All age-profile analysis must be compatible with NTA methodology unless a
departure is explicitly documented in `docs/`. Key profiles:

- Labor income profile (`yl`)
- Consumption profile (`cl`)
- Public transfer inflows and outflows (`tg+`, `tg-`)
- Asset-based reallocations (`ym`, `ys`)

The IM-6 age-expenditure profile h(j) in the fiscal gap formula is the
NTA-equivalent health expenditure profile. Do not substitute alternative
profiles without documenting the departure.

---

### 4.5 Formalization experiment design

The formalization experiment (IM-6, Section 7) is a core policy module.
Key design parameters:

- Population partition: A = B (formal) + C (informal)
- θ_H overrepresented in B; θ_L overrepresented in C
- Experiment: transfer fraction α ∈ (0,1] of C into B
- Newly formalized workers enter with observed ENOE (Mexico), ENAHO
  (Costa Rica), Encuesta de Hogares (Panama) income and health profiles
- Key output: threshold α* where contribution-base effect offsets
  expenditure-cost effect on τ^p
- Report for each country and each α:
  - Δτ^p(α)
  - ΔB/Y(α)
  - Consumption-equivalent variation by skill type
  - The threshold α*

Do not modify the formalization experiment design without consulting Héctor.

---

### 4.6 Open calibration flags

Operational registry of open integration items lives in
`GrandPlan/DFD/docs/calibration_flags.md`. Each flag has an ID, owner, source
back-link, action, and rationale. These are **not** corpus entries under
PROTO-RAG-001 — they are pre-work items sourced from external material
(seminars, papers, working notes) that needs to be folded into the
calibration. Consult this file at session start alongside the §3 retrieval
queries when working on demographic, fiscal, or macro-financial scenarios.
Close flags by moving the entry to the closed section with a date and
commit/file reference.

---

### 4.7 Current milestone map

| Period    | Deliverable                                           | Status        |
|-----------|-------------------------------------------------------|---------------|
| April     | Scaffold DFD/ folder structure                        | In progress   |
| April     | Draft and commit CLAUDE.md                            | This document |
| April 30  | IDB conference submission (OLG health paper)          | Active        |
| May       | Install Julia environment; verify CUDA.jl, Turing.jl  | Not started   |
| June      | Mexico OLG baseline — calibrated and committed        | Not started   |
| June 8    | IDB Second Seminar — baseline simulations reported    | Not started   |
| July–Aug  | Formalization experiment + gender decomposition       | Not started   |
| Sep 4     | Final synthesis submission                            | Not started   |

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
[model] add health depreciation vector delta_j to olg_baseline.jl
[data] ingest UISP 2019 life table for Mexico survival probabilities
[calibration] update OOP share for Mexico to 2021 vintage (WHO GHED)
```

Do not commit parameter changes without a source citation in the commit
message or in the associated calibration notebook.

**LaTeX compilation:** Two `pdflatex` passes are required for cross-reference
resolution. `Integrated_6.tex` uses `natbib` with `apalike`. If compiling
locally with `elsarticle`, download the `.cls` from CTAN and generate from
source before the first pass.

---

## 6. What to do when the corpus returns a conflict

If Query B returns a document showing that a parameter or modeling choice
contradicts what you have been asked to do in this session:

1. Do not proceed silently.
2. Surface the conflict explicitly: quote the prior document and the new
   instruction.
3. Ask Héctor to resolve before continuing.

This is not a failure mode — it is the corpus doing its job.

Known non-conflict: TFR values of 1.82 (IM-6 data tables, 2023 WDI) vs.
1.55 (DFD fast-transition scenario, 2024) are not a calibration error.
The former is the reference-year empirical value; the latter is the scenario
construction value. Document both when they appear together.

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

This log is a primary corpus document. Write it as if the next reader has no
memory of this session — because they won't.

---

## 8. Contacts

| Question about...                          | Contact |
|--------------------------------------------|---------|
| OLG model structure, demographic params    | Anne    |
| File conventions, infrastructure, Git      | Debb    |
| Pension parameters, fiscal block           | Beth    |
| DSGE extensions, GE closure, equilibrium   | Cath    |
| ABM layer, code documentation              | Nina    |
| Strategic priorities, scope decisions      | Héctor  |

---

*April 2026 scaffold version. Sections 3 and 4 will expand as corpus fills
out through May–June. Retrieval protocol should be tightened once the first
20 corpus documents are ingested. IM-6 integrated 2026-04-27 from
Integrated_6.tex (preliminary draft, April 2026).*

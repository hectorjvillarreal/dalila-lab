# Revision Plan: "Is Health a Blessing?"
## OLG Health Paper — Editorial Strategy & First-Pass Instructions
**Prepared by:** Anne (DFD Core Team) & Héctor  
**Date:** April 4, 2026  
**Status:** Pre-submission working document — Claude Code first pass

---

## 1. Strategic Context

### 1.1 Two submission targets

This paper has two simultaneous submission targets with different requirements:

**Target A — IDB Conference (primary, time-critical)**  
3rd Inter-American Development Bank Research Conference  
*Demographic Transition and Development in Latin America and the Caribbean*  
Washington DC, September 14–15, 2026  
**Submission deadline: April 30, 2026** ← 26 days from today  
Keynote speakers: Raquel Fernández (NYU) and Jesús Fernández-Villaverde (Penn/NBER/CEPR)

This conference is strategically important beyond acceptance. Fernández-Villaverde presented
"The Demographic Future of Humanity: Facts and Consequences" on April 1, 2026 — a seminar
that directly establishes the global demographic context our paper operates within. His
findings are directly relevant to our Mexico calibration:

- Global TFR fell below replacement (~2.21) in 2023 for the first time in human history
- Mexico's 2024 TFR is 1.55 — *below* the US at 1.62 (his slide 24 overshoot table)
- UN WPP data systematically overstates fertility; vital registries show faster decline
- "Peak birth" was ~2012; world population peak projected ~2055
- Middle-income countries like Mexico are overshooting advanced economies in fertility decline speed

The paper must be positioned to speak directly to this context. Fernández-Villaverde's
framework establishes *why* health-fiscal dynamics in middle-income economies are urgent:
they are aging faster than expected, without the fiscal margins Japan has, and before
reaching high income status.

**Target B — Economic Modelling (secondary, quality target)**  
Elsevier journal. Scope: macroeconomic modelling with policy relevance, quantitative methods,
applied general and partial equilibrium. Impact factor ~4. The partial equilibrium framing
of our paper is consistent with the journal's tradition. This is the post-conference
submission target — the IDB presentation will strengthen the submission.

### 1.2 What we have

The paper "Is Health a Blessing? The Macroeconomic Effects of Health Conditions — Mexico
as case study" (co-authored with Judy Méndez) is a **completed mission deliverable** with:

- A calibrated dynamic stochastic OLG model in partial equilibrium
- Binary health state (good/bad) affecting utility, survival probability, labor productivity,
  and out-of-pocket health expenditures
- Full Mexico calibration (2021 base year, ENOE, CONAPO, CIEP, OECD sources)
- Quantitative results: 40–70% consumption gaps, 78% welfare loss at age 30, early income
  stagnation at age 30 coinciding with health expenditure needs
- GBD epidemiological appendix for Costa Rica, Mexico, and Panama
- Solid literature review connecting to De Nardi/French/Jones, Fioroni, Dalgaard-Strulik,
  and related OLG-health literature

### 1.3 What the paper currently lacks for these targets

Three gaps need to be addressed in this revision pass:

1. **Demographic transition framing is implicit, not explicit.** The conference theme is
   demographic transition. The paper's connection to Mexico's fertility decline, aging
   trajectory, and the "aging before reaching high income" dynamic is present but buried.
   It needs to be foregrounded in the abstract and introduction.

2. **The abstract does not compete at conference level.** It reads as a technical summary
   of a mission deliverable. It needs to open with the policy stakes, connect to the
   demographic moment, and state the contribution sharply.

3. **The discussion section has a formatting problem.** Section headers are rendered as
   paragraph-level headings in the Word document, creating a wall of bold text rather
   than flowing prose. This must be restructured into proper academic prose sections.

---

## 2. Revision Instructions for Claude Code

### 2.1 Priority order

Execute in this order. Do not proceed to the next item until the current one is complete.

**PASS 1 — Abstract rewrite (highest priority)**  
**PASS 2 — Introduction restructure**  
**PASS 3 — Discussion section formatting fix**  
**PASS 4 — Minor consistency and language edits throughout**

---

### 2.2 PASS 1: Abstract rewrite

**Target length:** 200–250 words (IDB submission allows 400; Economic Modelling standard
is 150–250; calibrate to 200–250 as common ground)

**Required structural elements:**

1. *Opening sentence* — Establish the demographic moment and the policy stakes for
   middle-income economies. Do NOT open with "This research develops a model." Open with
   the problem: Mexico and comparable LAC economies are aging before reaching high income,
   at a speed that exceeds projections, with fiscal systems unprepared for the health
   expenditure consequences.

2. *Gap statement* — Existing OLG literature on health and aging is largely calibrated
   to high-income economies with extensive social insurance. The middle-income context —
   low public health spending, high out-of-pocket exposure, early income stagnation — is
   underexplored.

3. *Methodology* — We develop a dynamic stochastic partial equilibrium OLG model where
   health status (good/bad) operates as a state variable affecting utility, survival
   probability, labor productivity, and out-of-pocket expenditure. Calibrated to Mexico.

4. *Key results* — Three findings deserve explicit mention:
   - Consumption gaps of 40–70% between healthy and sick individuals during working years
   - 78% welfare loss for a 30-year-old worker who develops poor health
   - Income stagnation at age 30 coinciding with rising health expenditure needs —
     departing sharply from standard life-cycle predictions

5. *Policy implication* — Health is not a sectoral expenditure item but a core determinant
   of macroeconomic stability and intergenerational equity. In economies like Mexico,
   insufficient health investment today depresses productivity, weakens fiscal capacity,
   and may crowd out investment in younger cohorts — accelerating demographic fiscal stress.

**Tone:** Academic but accessible. This abstract will be read by IDB researchers and
Fernández-Villaverde. It should demonstrate methodological rigor and policy relevance
simultaneously.

**Do not use:** "This paper," "This research," "We show that" as opening phrases.
**Do use:** Active voice, specific numbers from the results, explicit Mexico anchoring.

---

### 2.3 PASS 2: Introduction restructure

The introduction is currently well-written but sequenced for a mission deliverable.
It needs to be re-sequenced for a conference paper with a demographic transition frame.

**Target structure:**

**Paragraph 1 — The demographic moment (NEW, ~150 words)**  
Open with the global fertility transition and its specific manifestation in Mexico.
Key facts to incorporate:
- Mexico's TFR reached 1.55 in 2024, below the US (1.62) — a historically unprecedented
  reversal for a middle-income economy
- Mexico is aging before reaching high income status: the "aging before wealth" trap
- The fiscal consequence: health expenditure pressure will intensify precisely as the
  contribution base narrows and labor income growth slows
- This creates an analytical gap: most OLG models addressing health and aging are
  calibrated to Japan, the US, South Korea, or Germany — not to Mexico's institutional
  and epidemiological context

**Paragraph 2 — The health-fiscal nexus in middle-income economies (REVISE existing)**  
The current introduction's second paragraph works well. Integrate the CIEP data on low
public health spending and high out-of-pocket exposure more prominently. Add the explicit
connection: Mexico's diabetes prevalence (16.9% of population, per OECD 2023) is not
merely an epidemiological fact — it is a fiscal time bomb interacting with demographic
aging.

**Paragraph 3 — What existing literature misses (REVISE existing)**  
The related literature section in the Methods is strong. Pull the core gap statement
forward into the introduction: existing work (De Nardi et al., Fioroni, Dalgaard-Strulik)
focuses on high-income contexts. Our contribution is explicitly the middle-income,
high-informality, low-public-spending environment.

**Paragraph 4 — Our contribution (REVISE existing)**  
State the three contributions clearly:
1. Methodological: OLG model with binary health state, health-dependent survival and
   productivity, and OOP expenditure risk — calibrated to Mexico
2. Empirical: Quantitative evidence of early-life income stagnation and consumption gaps
   in a middle-income LAC context
3. Policy: Fiscal stress from aging is not confined to pension systems; health conditions
   are an underestimated driver of long-run fiscal imbalance

**Paragraph 5 — Paper structure (KEEP, minimal edit)**  
Current structure paragraph is fine. Minor language edit only.

---

### 2.4 PASS 3: Discussion section restructure

**The problem:** The discussion section uses paragraph-level headings rendered as bold
section titles in the Word document. In the extracted markdown, these appear as `##`
headers with extremely long text — essentially the paragraph content used as a heading.
This is not acceptable for either submission target.

**The fix:** Convert each "heading-paragraph" into a proper flowing prose section.
The content is good — the structure is broken.

**Specific instructions:**

For each of the seven discussion paragraphs (currently rendered as ## headers):

1. Extract the substantive content from the heading text
2. Assign a short, proper section heading (see mapping below)
3. Rewrite as flowing academic prose of 150–200 words
4. Ensure logical flow between sections with transition sentences

**Section heading mapping:**

| Current (broken heading text, truncated) | New proper heading |
|---|---|
| "The results of this research, based on a dynamic..." | 4.1 Health as a Macroeconomic State Variable |
| "A key insight of the model is that health operates..." | 4.2 The Compounding Mechanism |
| "The Mexican case illustrates these dynamics..." | 4.3 Early-Life Income Stagnation: The Mexico Case |
| "These results are especially relevant given Mexico's..." | 4.4 Institutional and Epidemiological Context |
| "From an intergenerational perspective, the findings..." | 4.5 Intergenerational Trade-offs |
| "Overall, the analysis underscores that health should not..." | 4.6 Health Investment as Fiscal Strategy |
| "Beyond household-level dynamics, the results also speak..." | 4.7 Demographic Transition and Fiscal Imbalance |

**Section 4.7 is the most important for the IDB submission.** It explicitly connects
the paper's results to the demographic transition frame. Strengthen this section by:
- Explicitly naming the "aging before high income" dynamic
- Connecting the income stagnation finding to the narrowing contribution base under
  fertility decline
- Noting that fiscal stress from health operates through multiple channels simultaneously:
  lower tax bases, higher transfer demands, rising OOP and public expenditures
- Closing with a sentence that connects to the policy reform agenda

---

### 2.5 PASS 4: Minor edits throughout

After Passes 1–3 are complete, conduct a pass for:

- **Partial equilibrium defense:** The paper correctly states this is partial equilibrium
  and defends it. Ensure the defense appears in both the Methods section and is briefly
  acknowledged in the Discussion (reviewers at Economic Modelling will probe this).

- **Keyword alignment:** Current keywords: Macroeconomic equilibrium; Health; Aging;
  Out-of-pocket expenditures; Overlapping generations; Mexico. Add: Demographic transition;
  Fiscal sustainability; Middle-income economies; Latin America. For Economic Modelling,
  keywords must align with the journal's subject classification.

- **Reference formatting:** Check all references for completeness. The Dougherty & Lorenzoni
  (2022) entry is missing an author (appears as "Dougherty, S., , P., & Lorenzoni"). Fix.

- **Appendix framing:** The GBD appendix (Costa Rica, Mexico, Panama) is currently
  descriptive. Add two sentences at the start of the appendix noting that these three
  countries bracket the LAC epidemiological transition: Costa Rica (advanced transition,
  high public spending), Mexico (middle transition, low spending, high diabetes), Panama
  (intermediate). This strengthens the regional generalizability argument.

---

## 3. What NOT to change in this pass

- The model structure and mathematical specification — these are correct and complete
- The calibration parameters and results tables — do not alter any numbers
- The literature review in Section 2 (Related Literature) — this is strong as written
- The appendix content (GBD figures and analysis) — descriptive content is appropriate
- The conclusions — these are well-written and can be lightly edited in a later pass

---

## 4. Output format

Claude Code should produce:

1. A revised `.docx` file named `OLGHealth_IDB_v1.docx` with all four passes applied
2. A brief change log in markdown (`OLGHealth_changelog_v1.md`) noting:
   - What was changed in each section
   - Any editorial judgment calls that Héctor should review
   - Any places where the revision required assumptions about intent

The `.docx` output should be ready for Héctor to review and send to Judy Méndez for
co-author approval before the April 30 submission deadline.

---

## 5. Submission logistics (for reference)

**IDB submission portal:** Oxford Abstracts  
**URL:** https://app.oxfordabstracts.com/stages/82093/submissions/new  
**Fields required:**
- Title (max 50 words)
- Abstract (max 400 words) — use our revised abstract
- Authors and affiliations (all authors in order)
- Author approval confirmation
- Author attendance confirmation (in-person, Washington DC)
- Subject category selection
- Paper upload (PDF only)

**Suggested title for submission:**  
"Is Health a Blessing? Macroeconomic Consequences of Health Conditions in a Middle-Income
Economy with Rapid Demographic Transition: Mexico as Case Study"

*(The added subtitle foregrounds the demographic transition frame explicitly for the
IDB conference. Can revert to shorter title for Economic Modelling submission.)*

**Authors (confirm order with Judy):**  
Héctor Juan Villarreal Páez — Tecnológico de Monterrey, Monterrey, Mexico  
Judy Méndez — [Judy's institution and city — confirm before submission]

---

## 6. Timeline

| Date | Milestone |
|---|---|
| April 4–6 | Claude Code first pass (this document) |
| April 7–8 | Héctor reviews, annotates changes |
| April 8–10 | Judy reviews and approves |
| April 10–14 | Second polish pass (this chat with Anne) |
| April 14–20 | Final read, PDF generation |
| April 28 | Submit to IDB (2 days before deadline) |
| Post-September | Revise for Economic Modelling submission |

---

*DFD Project — Core Team Internal Document*  
*Anne (Population Economics) · April 2026*  
*This document is for internal use. Do not distribute without Héctor's approval.*

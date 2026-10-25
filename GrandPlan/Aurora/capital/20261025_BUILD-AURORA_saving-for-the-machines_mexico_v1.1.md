---
# PROTO-RAG-001 build-instruction fields
type: build_instruction
build_type: expansion
date: 2026-10-25
corpus_affected: [GrandPlan/Aurora/capital/]
triggered_by: "Héctor's 2026-10-25 review of v1 in a Claude Code session: the paper's closure, the source of 'bystander economies', and the paper's own §8.3 tax results were not reflected in v1. Héctor asked for v1.1 carrying those three corrections, then execution."
agents_involved: [Elle, Cath, Nina, Anne]
status: executed                     # 2026-10-25, deliverable 20261025_AURORA_SFTM-MEX-inference_v1.md
supersedes: 20261025_BUILD-AURORA_saving-for-the-machines_mexico_v1.md
# Original v1 fields, kept
doc_id: BUILD-AURORA-SFTM-MEX-001
version: "1.1"
doc_type: build_instruction
title: "Saving for the Machines — México fiscal-demographic inference pass"
protocol: PROTO-RAG-001
added_by: [Elle, Cath, Nina]        # drafters of v1; v1.1 amendments drafted by Claude at Héctor's request
endorsed_by: []                      # pending Héctor; per-section domain authority noted inline
consulted: [Anne]                    # demographic layer
projects: [Aurora (home), DFD, RF]
source_document:
  author: Jesús Fernández-Villaverde
  title: "Saving for the Machines"
  version: "first draft dated 2026-10-20 (74 pp. incl. Online Appendix); NBER WP version expected to follow"
  held_by: Héctor (full PDF at GrandPlan/Aurora/capital/Saving_Machines.pdf; slides not in the tree)
target_runtime: Claude Code session under Aurora, Dalila
retention: indefinite (_crossrefs/_build_instructions/) as provenance
# Filing convention (id scheme, exact path) pending Héctor's decision, per compute-brief note.
---

# Saving for the Machines — México fiscal-demographic inference pass (v1.1)

## Changes from v1

v1.1 makes three corrections. All three come from checking v1 against the full draft (2026-10-25).
Everything else in v1 is unchanged.

1. **Closure (§1, §3.2, Nina's tasks in §4, §6).** The paper's model is a **closed economy**. It
   has a representative household and a real bond in zero net supply. Its interest rate is set
   at home: r = R − δ = ρ + γ·g_C (Prop. 13). Under full automation, technology sets r at ψ_k − δ.
   The model has no world interest rate, foreign sector, government or public debt. The §3.2
   question ("world-determined or domestic?") is therefore answered: **domestic**. Every step of
   the world-rate channel is our inference, an open-economy extension the paper does not make.
   Anchor that extension in corpus entries that do model it (§4, Nina), not in this paper.
2. **"Bystander economies" (§1).** The phrase does not appear in the 2026-10-20 draft. The draft
   also has no section on public finance or open economies. v1 attributed the framing to the
   author, presumably from the slides or a talk, which are not in the tree. The deliverable must
   either cite the exact source of that framing or label it as Aurora's framing. Section 1 now
   lists what the paper itself says on the policy edge.
3. **The paper's own fiscal content (Cath's tasks in §4).** §8.3 of the paper contains a
   capital-income tax analysis that v1 missed. Cath's section must start from it. The
   paper's results are the model-internal baseline. The México reading is inference layered on
   top of them.

Execution note (from v1 review, not a change to scope): ollama is installed on Dalila with
`qwen3.5:9b`, so §3 step 1 runs locally as written.

## 0. Mission (one paragraph)

Study Fernández-Villaverde's *Saving for the Machines* in full, extract its model
mechanism cleanly, and infer — with discipline — its consequences for México,
read specifically through (a) our fiscal system and (b) our demography. This is an
**inference pass, not a modelling build**. The deliverable is a single structured
note that separates what the paper's model says from what we infer for a country
the paper does not study, and that marks every point where a later quantitative
pass (IM-6, RF) would attach. Iteration beats optimality here: produce a disciplined
first inference, flag the open quantitative questions, stop.

## 1. The object — the paper's spine (verify against the full text before using)

A task model in the Acemoglu–Restrepo lineage, in which machines perform a growing
share of tasks. Growth turns on two margins:

1. **Task structure** — how the sequence of automatable tasks sets the *returns* to
   accumulating machines. This governs the **duration** of the automation growth
   boom and the path of wages.
2. **Capital accumulation response** — how strongly saving/investment responds to
   those returns. This governs the **size** of the boom.

Reported headline result (**verify the two figures against the draft during ingestion**):
the *same* technology path yields ~**11.7%** annual growth when households choose
their saving rate optimally, but only ~**2.2%** when the saving rate is held at the
calibrated U.S. level. Reading: slow growth under automation may reflect **too little
capital accumulation**, not a technological bottleneck. Mechanically, the saving rate
rises because automation **raises the capital share**, not because households become
more patient.

**Closure (v1.1).** The setting is a closed economy with a representative household (paper §2,
"a deterministic neoclassical growth model of a closed economy"). The interest rate is determined
at home, by the Euler equation and by no-arbitrage with capital (Prop. 13). In the long run the
household's capital supply is perfectly elastic. The paper calls this one of two polar cases and
says heterogeneity and financial frictions would give intermediate elasticities. The model has no
government budget, no public debt and no rest of the world.

**Policy edge (v1.1, replaces the v1 paragraph).** In the paper itself:
- The build-out needs "software, data centers, robots, *power plants*, and much else". Citing Van
  Nieuwerburgh (2026), AI campuses alone absorb 3.6% of U.S. GDP a year over 2025–2032 (Introduction).
- **Depreciation.** For data centres, computing equipment lasts six years, and buildings and
  power plants twenty. The blend is about 12% a year. At δ = 20% and σ = 0.2, a fixed 23% saving
  rate does not cover depreciation, and output in 2045 is half its trend (Online Appendix A).
- **Elasticity caps.** The conclusion lists what can cap the elasticity of capital supply:
  heterogeneous agents, financial frictions, and "limited physical resources". Political economy
  is named as "probably the most important omission".
- **The only public-finance exercise** is the §8.3 tax-and-transfer arithmetic (see Cath, §4).

The **"bystander economies"** question was attributed to the author in v1. It is not in the
2026-10-20 draft, and the draft has no section on public finances. The deliverable carries the
question as Aurora's framing unless the exact source (slides, talk, post) is cited.

> **Cross-driver note (Elle).** The machine build-out is simultaneously an *energy*
> build-out; the capital demand includes generation. This is the demand-side mirror
> of the degrowth/abundance framing already open in the Energy chat — AI capital
> demand is now a first-order pull on the energy transition, the opposite pole from
> sufficiency. Carry the energy-capital channel explicitly; do not let it collapse
> into a generic "AI needs compute" line. *(v1.1: the paper's own anchors for this channel
> are the power-plant line in the Introduction, the depreciation rows of Online Appendix A, and
> "limited physical resources" in the Conclusion.)*

## 2. Why México is the sharp case

México is a **bystander / capital-importing** economy with: aging before reaching
high income; low tax pressure (the RF target is 25% by 2036); high informality; a
labour/consumption-weighted revenue base; and persistent reliance on external
financing. The paper's mechanism intersects every one of those. State the mapping as
inference, not as the paper's result.

## 3. Execution protocol (for the Claude Code session)

1. Ingest the full PDF under PROTO-RAG-001, **whole-document** (262K context, local
   Qwen3.5-9B baseline; escalate to external API only if the local model misreads
   the model's equations or the calibration section — Elle's standing fallback rule).
2. Reproduce the model's logic to the point of being able to name its levers: the
   task-structure parameter(s), the saving/capital-supply margin, the capital-share
   dynamics, and the closure (is the interest rate world-determined or domestic?).
   **This closure assumption is decisive for México** — flag it explicitly.
   *(v1.1: answered in §1. It is domestic, a closed economy. The note must still restate it at
   the top of every section that uses the rate channel.)*
3. **Verify the two headline growth figures** and the "capital share, not thrift"
   claim against the text. If either differs, the inference below inherits the
   correction.
4. No heavy compute is required for this pass. Julia/CUDA paths stay idle; this is a
   reading-and-inference run. Do **not** begin recalibration — that is a flagged next
   iteration (§5), not in scope.

## 4. Agent tasks

Each agent works its own lens, states assumptions, and distinguishes *model-internal*
claims from *México inferences*. One agent, one section; synthesis is Elle's.

### Elle — mechanism, synthesis, cross-driver *(domain authority: Elle)*
- Render the two-margin mechanism precisely and faithfully; this is the shared
  object the others build on.
- Frame México on the participant↔bystander axis: is any machine/energy capital
  plausibly *hosted* here (nearshoring of data-centre + generation capacity), or is
  México purely a price-taker on world capital? The honest answer sets how much of
  the paper's optimistic margin is even available to us.
- Hold the energy-capital channel (§1 note) and connect it back to the Energy chat's
  framing question.

### Cath — fiscal structure and the tax base *(domain authority: Cath)*
- **(v1.1) Start from the paper's §8.3. Report its results as model-internal before inferring
  anything.** The results are for full automation with constant machines:
  - **Compensation transfer.** The transfer that keeps labour income on its no-automation trend
    peaks at 4% of GDP with σ = 1, 11% with σ = 0.5, and 20% with σ = 0.2. It is below 4% of GDP
    by 2055 in every economy.
  - **Flat tax.** A flat 25% tax on net capital income raises τ(1 − δ/ψ_k0), between 20% and 22%
    of GDP in the limit economy. It lowers limit growth from 21.9% to 16.2% with σ = 1 and from
    11.6% to 8.5% with σ = 0.2, permanently.
  - **Balanced-budget tax** on net capital income that compensates the hand-to-mouth share θ,
    with θ = 0.5:
    - It peaks at 3.5% of net capital income with σ = 1 and at 22% with σ = 0.2, then fades.
    - Growth loses at most 1.1 points with σ = 1 and 3.3 points with σ = 0.2, and nothing in
      the long run.
    - With θ = 0.3, the peak tax is 1.7% with σ = 1 and 11% with σ = 0.2.
  - **Incidence.** Under full automation the wage is pinned at the cost of the machines that
    replace labour. The tax cannot be shifted to labour, so it lowers the after-tax return and
    with it growth. Under partial automation the after-tax return returns to ρ + γg*, so
    "labor ends up paying for its own compensation".
  - **Two conditions** frame every result above. The representative-household case is
    "illustrative accounting". In the closed economy, capital cannot leave. Both conditions
    bear directly on the México reading.
- If automation **raises the capital share**, trace the consequence for a revenue
  system leaning on labour income and consumption, with capital income mobile and
  lightly taxed. The base erodes precisely as fiscal need rises. This is the RF
  nexus: the 25%-by-2036 target becomes **both harder and more necessary**.
- Government budget constraint: set out, qualitatively, how a rising-capital-share /
  higher-world-rate environment moves the debt dynamics (primary balance required,
  r–g gap). Mark the point where this enters **IM-6** as a calibration hook — do not
  calibrate. *(v1.1: "higher world rate" is inference under an open-economy closure. Say so.)*
- Optimal-tax angle: taxing a growing but mobile capital share under automation —
  state the tension, not a prescription. *(v1.1: the paper's incidence result depends on capital
  being immobile. State how it changes when capital moves across borders, and keep it as
  inference.)*

### Nina — macro-financial transmission *(domain authority: Nina)*
- **(v1.1) Closure first.** The paper has no world rate. Its model-internal rate results are
  about the domestic short rate and the domestic yield curve:
  - The short rate does not move on impact.
  - The ten-year real yield jumps from 5.1% to 13.6% with σ = 1 and to 9.3% with σ = 0.2. The
    thirty-year yield jumps to 33.0% and 19.6%.
  - The value of the labour force falls by about two-thirds on impact (Prop. 14–15).
  - Current long real rates are far below these levels. The paper reads this as markets
    placing little weight on such paths (citing Chow et al. 2025).

  Report these first. Then build the bystander chain under an explicit small-open-economy
  closure. Anchor it in corpus entries that model the open-economy mechanism:
  - Auclert–Malmberg–Rognlie–Straub (2025), "reverse crowding-out": rising private asset supply
    raises r and crowds out fiscal space (`GrandPlan/DFD/docs/corpus/auclert_et_al_2025_rag.md`).
  - Benzell–Kotlikoff–Ye (2026), internationally mobile capital with a Mexico region
    (`GrandPlan/DFD/aging_macro_nber_2609/2026-09-17_global-transition-demographics-ai.md`).
- The general-equilibrium rate channel is the main bystander mechanism: if the world
  saves for the machines, the **world real rate rises**, and a capital-importer pays
  more to finance its state. Trace: world r ↑ → sovereign financing cost ↑ → debt
  service ↑ → fiscal space ↓. Tie to **fiscal dominance** signals for a middle-income
  economy.
- Apply the Brunnermeier–Reis lens: currency mismatch / original-sin exposure and
  capital-flow behaviour if the global saving pull is sharp rather than smooth —
  i.e., is the bystander squeeze a gradual drift or a run-prone regime?
- Note the ambiguous sign for funded pension pillars (higher returns) against
  sovereign sustainability (worse) — flag for IM-6/BDH, do not resolve.

### Anne — demographic realism *(consult; domain authority: Anne)*
- The paper's binding constraint is **capital supply**; in an aging society,
  life-cycle behaviour pushes toward **dissaving** as older cohorts draw down. State
  whether México's demographic trajectory makes the domestic saving margin weak
  exactly when the model says saving is what matters.
- The bind to name clearly: an aging economy has the **highest need** for machines
  (to substitute for the shrinking workforce) and the **lowest domestic capacity to
  save** for them — so it must import the capital at the higher world rate. Automation
  as a substitute for the missing cohort is the optimistic read; financeability is the
  constraint that may foreclose it.
- Keep NTA/intergenerational-equity framing available; do not open it fully here.

## 5. Deliverable + hooks

**Deliverable:** one structured inference note (`SFTM-MEX-inference-v1`), sections per
agent above, Elle's synthesis on top, conforming to PROTO-RAG-001 frontmatter, filed
as a corpus entry with this build instruction as its provenance parent.

**Hooks for the next iteration (option value, not in scope now):**
- IM-6: introduce a world-rate / capital-share shifter and read the OLG fiscal response (Cath).
- RF: re-express the 25%-by-2036 path under a capital-share-erosion scenario (Cath).
- DFD/BDH: pension-pillar and health-financing sign under higher world rates (Nina/Beth).
- Aurora-Energy: nearshored machine-and-generation capital as a participant scenario (Elle).

## 6. Discipline / guardrails

- The paper's model is the model; the México mapping is **inference** — never blur them.
- Do not import the U.S. calibration to México without saying so; the fixed-saving
  counterfactual is suggestive *of* the mechanism, not a México estimate.
- State the interest-rate closure every time you use the rate channel — it is the
  hinge of the whole bystander argument. *(v1.1: the paper's closure is closed-economy and
  domestic. Any world-rate statement is ours.)*
- Verify the two headline figures (§1). Flag, don't paper over, any discrepancy.
- (v1.1) Do not attribute the "bystander economies" framing to the paper without a cited source.
- Empty `endorsed_by` means review pending, not absent. Successor versions chain by
  provenance; this instruction is retained indefinitely.

---
doc_id: BUILD-AURORA-SFTM-MEX-001
doc_type: build_instruction
title: "Saving for the Machines — México fiscal-demographic inference pass"
date: 2026-10-25
protocol: PROTO-RAG-001
status: superseded                   # was: draft / ready for execution
superseded_by: 20261025_BUILD-AURORA_saving-for-the-machines_mexico_v1.1.md
added_by: [Elle, Cath, Nina]        # drafters
endorsed_by: []                      # pending Héctor; per-section domain authority noted inline
consulted: [Anne]                    # demographic layer
projects: [Aurora (home), DFD, RF]
source_document:
  author: Jesús Fernández-Villaverde
  title: "Saving for the Machines"
  version: "first draft, circulated October 2026 (NBER WP version expected to follow)"
  held_by: Héctor (full PDF + slides)
target_runtime: Claude Code session under Aurora, Dalila
retention: indefinite (_crossrefs/_build_instructions/) as provenance
# Filed in _crossrefs/_build_instructions/ by Héctor's decision of 2026-10-25 (original filename kept).
---

# Saving for the Machines — México fiscal-demographic inference pass

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

Policy edge (author's own framing, public-finance channel): the AI build-out
requires an extraordinary volume of capital — data centres *and new power plants* —
and inducing the saving to fund it strains public finances. His open question is
whether **"bystander economies"** — those not building the frontier — can still
finance their governments against that backdrop.

> **Cross-driver note (Elle).** The machine build-out is simultaneously an *energy*
> build-out; the capital demand includes generation. This is the demand-side mirror
> of the degrowth/abundance framing already open in the Energy chat — AI capital
> demand is now a first-order pull on the energy transition, the opposite pole from
> sufficiency. Carry the energy-capital channel explicitly; do not let it collapse
> into a generic "AI needs compute" line.

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
- If automation **raises the capital share**, trace the consequence for a revenue
  system leaning on labour income and consumption, with capital income mobile and
  lightly taxed. The base erodes precisely as fiscal need rises. This is the RF
  nexus: the 25%-by-2036 target becomes **both harder and more necessary**.
- Government budget constraint: set out, qualitatively, how a rising-capital-share /
  higher-world-rate environment moves the debt dynamics (primary balance required,
  r–g gap). Mark the point where this enters **IM-6** as a calibration hook — do not
  calibrate.
- Optimal-tax angle: taxing a growing but mobile capital share under automation —
  state the tension, not a prescription.

### Nina — macro-financial transmission *(domain authority: Nina)*
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
  hinge of the whole bystander argument.
- Verify the two headline figures (§1). Flag, don't paper over, any discrepancy.
- Empty `endorsed_by` means review pending, not absent. Successor versions chain by
  provenance; this instruction is retained indefinitely.

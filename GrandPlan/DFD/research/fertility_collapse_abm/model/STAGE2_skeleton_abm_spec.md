# Stage 2 — ABM Build Specification (Skeleton Phase)
# Project: Rapid Fertility Collapse in Latin America (DFD parallel research)
# Author: Nina (ABM lead) and Anne (population economics), DFD Core Team
# Date: 2026-06-19
# For: Claude Code on Dalila
# Location: GrandPlan/DFD/research/fertility_collapse_abm/model/

---

## What this stage is, and what it is NOT

Stage 1.5 cleared the gate: the fertility collapse is behavioral, the state variable is
union *composition*, and the nonlinearity locus is `w`-determined. Stage 2 builds the
agent-based model that generates the collapse endogenously.

**This is the SKELETON phase — one country (Costa Rica), CPU-parallel, mechanism-first.**
Its purpose is to prove the mechanism works end-to-end before scaling: can a threshold in
the coupling→fertility map generate the observed nonlinear TFR collapse from *independent*
inputs? Not "can we fit Costa Rica" — "does the mechanism produce the phenomenon."

**This stage does NOT:** build the four-country nesting model, run the GPU parameter sweep,
or freeze the full spec. Those come after the skeleton proves the mechanism. Building the
sweep before the single-country mechanism is validated is the failure mode we are explicitly
avoiding.

---

## FROZEN INVARIANTS (do not deviate without Anne + Nina sign-off)

Stage 1.5 settled three things. These are fixed for all of Stage 2 and beyond:

1. **The state variable is union *composition*, not union *level*.** An agent's relevant
   state includes whether she is in no union, a cohabiting union, or a marriage — not
   merely "partnered / not partnered." A model tracking only total partnered-share is
   wrong by construction; it misses the entire Colombian mechanism.

2. **`w` is a nested structural parameter, not a fixed constant.** `w` = ratio of
   cohabiting-union fertility intensity to married-union fertility intensity (0 ≤ w ≤ 1).
   The model must accept `w` as a parameter and behave correctly across the full range.
   Do not hard-code a value. Until ENDS pins it, sweep the {0.4, 0.6, 0.8} band.

3. **The nonlinearity locus is `w`-determined, not assumed.** The model must NOT hard-code
   whether the threshold sits in partnership formation or in the coupling→fertility map.
   The locus emerges from `w` and the cohabitation-share initial condition. This is the
   whole point of the nesting structure.

Everything below the invariants is PROVISIONAL — the skeleton is expected to teach us
where the spec is wrong. Surfacing a needed change (a parity dimension, a distributional
initial condition, a marriage-specific threshold) is a *success* of this stage, not a
deviation from it.

---

## Compute approach — use Dalila correctly

This is a social-dynamics ABM: heterogeneous agents, partnership transitions, a threshold
in the fertility-response map. **It is CPU-parallel, not GPU-native.** Per the Dalila
compute envelope brief, the agent step belongs on CPU; the GPU pays off only for the
large parameter sweep in the *nesting* phase, which is not this stage.

- **Implementation:** Agents.jl in Julia. CPU-parallel via Julia's native threading /
  `Distributed` for ensemble runs (multiple stochastic seeds), not within the agent step.
- **Do NOT** write CuArray agent kernels in the skeleton. The agent population for one
  country is small (tens of thousands of agents); GPU overhead is not justified and would
  optimize the wrong layer.
- **Reserve the GPU** for the nesting-phase sweep (later stage), where thousands of
  independent (`w`, threshold, cohabitation-share) runs across four countries are the
  embarrassingly-parallel workload that saturates the machine.
- Profile with `CUDA.@time` / `@btime` only when the sweep arrives. For the skeleton,
  correctness and mechanism-clarity beat speed.

---

## The skeleton model — minimal specification

### Agents
Women of reproductive age (15–49), heterogeneous on two FIXED background dimensions
(the Calles-Vogl dominant drivers, held as structural context, NOT tuned to fit TFR):
- **Education level** (discrete: low / medium / high)
- **Location** (urban / rural)

Each agent carries a dynamic state:
- **Union status**: {single, cohabiting, married} — the composition invariant
- **Age**
- **Parity** (number of children) — include from the start; the tempo finding makes
  parity-specific timing likely relevant, and retrofitting it later is costly

### The two coupled processes

**Process A — partnership formation/dissolution (the coupling margin).**
Each period, single agents face a probability of entering a union (cohabiting or married),
and the cohabiting/married split evolves. The partnership-formation probability depends on
a **social-norm term**: the share of an agent's reference group currently partnered. This
is where a threshold *may* sit (coupling-side locus). The reference group is, minimally,
same-age-band agents; education/location homophily is a provisional extension.

**Process B — fertility (the coupling→fertility map).**
An agent's per-period birth probability depends on her union status, weighted by `w`:
married unions at full intensity, cohabiting unions at intensity `w`, single agents at a
low baseline. This map is where the *other* threshold may sit (map-side locus). The
nonlinearity in this map is a provisional functional form — the skeleton tests whether a
threshold here is needed at all, or whether Process A's threshold suffices.

**The locus question, operationalized:** the skeleton has two candidate threshold sites
(Process A and Process B). The invariant says the locus is `w`-determined. Concretely:
at low `w` (cohabitation is low-fertility), the marriage margin carries fertility, so the
partnership-formation threshold (A) dominates → coupling-side. At high `w` (cohabitation
≈ marriage in fertility), total union matters and the map threshold (B) can dominate →
map-side. The skeleton must reproduce this `w`-dependence, not assume it.

### Calibration inputs (INDEPENDENT — identification discipline)
The model is calibrated to, and ONLY to:
- Costa Rica annual union-composition series (`CRI_coupling_annual.csv`, all three
  measures) — Process A target
- Education and urbanization distributions (World Bank / census) — agent background
- `w` band {0.4, 0.6, 0.8} until ENDS pins it — Process B weight

**The observed TFR is the OUTPUT to be matched, NEVER a calibration target.** This is the
non-negotiable identification discipline from Stage 1. If the model is ever tuned to fit
TFR directly, the result is worthless. The TFR match is the test, not the input.

---

## What the skeleton must demonstrate (success criteria)

The skeleton succeeds if, calibrated only to independent inputs, it:

1. **Generates the observed Costa Rica TFR collapse** (1.83 → 1.12) as an *emergent
   output* — not fit, generated — within a plausible band, for at least one `w` in the
   sweep.
2. **Produces the collapse as genuinely nonlinear** — a threshold-driven acceleration,
   not a smooth glide that happens to pass through the endpoints. Show the mechanism, not
   just the endpoints.
3. **Reproduces the `w`-dependence of the locus** — at low `w` the action is in Process A
   (partnership), at high `w` it shifts toward Process B (the map). This is the
   invariant made visible.
4. **Survives a falsification check:** if the social-norm threshold is removed (set the
   reference-group dependence to zero), the collapse should NOT reproduce — confirming the
   threshold is doing the work, not the background trends.

Criterion 4 is the most important. A model that produces the collapse *without* the
threshold doing the work has not demonstrated the mechanism — it has just absorbed the
trend into background covariates. The falsification check is what separates a mechanism
from a curve-fit.

---

## Deliverables

Under `GrandPlan/DFD/research/fertility_collapse_abm/model/`:

1. **Model code** — `cri_skeleton_abm.jl` (Agents.jl), CPU-parallel ensemble, documented
   to PROTO-RAG-001 code standards (Purpose / Inputs / Outputs / Assumptions /
   Dependencies headers, per Nina's documentation mandate).

2. **Calibration notebook** — how each independent input maps to a model parameter, with
   explicit confirmation that TFR is not among the calibration targets.

3. **Results memo** — `STAGE2_skeleton_results.md`:
   - Did the collapse emerge? (criterion 1) — with the generated vs. observed TFR path
   - Was it nonlinear? (criterion 2)
   - Did the `w`-locus dependence appear? (criterion 3)
   - Did the falsification check pass? (criterion 4) — **report this even if it fails**
   - What the skeleton revealed that the spec got wrong — the provisional elements that
     need to change before the full nesting model
   - An explicit recommendation: is the mechanism proven well enough to scale to the
     four-country nesting model and the GPU sweep?

4. **Figures** — generated TFR vs. observed; the nonlinearity visualization; the
   with/without-threshold falsification comparison.

---

## Parallel track (independent of the skeleton) — Argentina/Chile acquisition

Running concurrently, NOT gating the skeleton. Anne's identification argument: the paper's
`w`-headline depends on observing the mechanism across *different cohabitation regimes*,
and CRI+COL are both high-cohabitation. Argentina (Southern Cone, marriage-dominant) and
Chile (intermediate) extend the cohabitation-share range where `w` is currently
unidentified.

- **Argentina priority route:** census 2010 + 2022 union status + DEIS marriage
  registrations → coarse marriage-rate trajectory, paired with the existing INDEC-pinned
  annual TFR. A third lead-test case in a different nuptiality regime. EPH microdata
  (urban, to 2014) as secondary.
- **Chile:** periodic CASEN → likely endpoints-only; accept coarse. Even two points in a
  third regime discipline the `w`-curve.
- Deliverable: extend the coupling identification CSVs with ARG (and CHL if feasible),
  same schema, same forensic discipline (survey comparability, coverage flags).

This track feeds the nesting phase, not the skeleton. The skeleton proves the mechanism on
Costa Rica alone.

---

## Gate to the nesting phase

After the skeleton results memo, Anne and Nina review. The decision: is the mechanism
proven (all four criteria, especially the falsification check) well enough to (a) freeze
the now-informed full spec, (b) build the four-country nesting model, and (c) commit the
GPU sweep? Only then does the full freeze happen — informed by what the skeleton taught,
not before it.

---

## Documentation discipline (Debb / PROTO-RAG-001)

Findings and caveats together. The skeleton will have caveats — stochastic-seed
sensitivity, the provisional functional forms, the uncalibrated `w` band, the small agent
population. Every result carries its caveat inline. Code documented to standard.
`endorsed_by` blank pending Anne. Build-instruction archival flagged for Debb.

---

*Stage 2 of 4 — Skeleton Phase. Version 1.0, 2026-06-19.*
*Invariants frozen; full spec deferred to the nesting phase, post-skeleton.*
*Next: skeleton results review → full-spec freeze → four-country nesting model + GPU sweep.*

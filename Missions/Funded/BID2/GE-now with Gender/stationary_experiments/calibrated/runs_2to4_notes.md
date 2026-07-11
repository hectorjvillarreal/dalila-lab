# Runs 1′–4 at the Calibrated Baseline — Session Notes

**Spec:** `CC_instrucciones_runs_2to4.md`. **Branch:** `bid2-calibration-anchors`.
**Repo tag at start:** `bid2-preflight-runs2to4` (HEAD `d417807`, gate passed).
**Session:** 2026-05-31 → 06-01. All solves on `ge_model_gender.jl`
(`gender_gap=true`, J=17), joint closure unless noted, `--project=stationary_experiments`.

---

## 0. Headline

Four stationary GE solves at the harmonized calibrated baseline, all converged
cleanly (≤26 iters, itermax 30), all four core gates PASS each:

| metric | Run 1′ (base) | Run 2 (κ=0.30) | Run 3 (τm=−0.20) | Run 4 (aging C1) |
|---|---:|---:|---:|---:|
| K | 4.960 | 5.489 | 5.177 | 7.133 |
| L | 4.987 | 5.160 | 5.037 | 6.320 |
| Y | 7.964 | 8.442 | 8.139 | 10.562 |
| r (ann %) | 4.209 | 3.791 | 4.004 | 3.434 |
| w | 1.022 | 1.047 | 1.034 | 1.070 |
| τp (%) | 9.29 | 5.46 | 9.62 | 15.86 |
| pen | 0.365 | 0.233 | 0.371 | 0.376 |
| B/Y (%) | 32.92 | 34.67 | 28.80 | 26.46 |
| C/Y (%) | 48.11 | 46.52 | 47.58 | 50.84 |
| M/Y (%) | 2.728 | 2.448 | 3.217 | 2.806 |
| dep_ratio | 0.1857 | 0.1820 | 0.1925 | 0.3171 |

Welfare at birth W₁(g,θ):

| | Run 1′ | Run 2 | Run 3 | Run 4 |
|---|---:|---:|---:|---:|
| M,θ_L | −3.6360 | −3.7806 | −3.6203 | −4.0674 |
| M,θ_H | −0.4201 | −0.3635 | −0.3865 | −0.9296 |
| F,θ_L | −4.7235 | −4.9882 | −4.7174 | −5.1875 |
| F,θ_H | −1.8987 | −1.9563 | −1.8762 | −2.4303 |

Authoritative CSVs: `results/calibrated_comparison.csv`,
`results/calibrated_welfare_change.csv`, plus per-run `*_summary.csv`,
`*_welfare.csv`, `*_lifecycle.csv`. With Run 0's `run0_history.csv` these are the
complete numerical input for the §§4-5 LaTeX rewrite.

---

## 1. Run 1′ — harmonized calibrated 2020 baseline (canonical §4 baseline)

Re-anchored the three first-step inputs the SMM saw at the PE anchor but that the
gate's Run 1 held at GE stubs:

| input | gate Run 1 | Run 1′ | source |
|---|---:|---:|---|
| ρ_AR | 0.98 | 0.782 | `inputs_mxdata/first_step/ar1_params.csv` |
| σ_ε | 0.05 | 0.265 | same |
| π_birth | symm 0.25 | M-L .3927 / M-H .1173 / F-L .3822 / F-H .1078 | `pi_birth.csv` |

Override mechanics (no edit to `ge_model_gender.jl`): ρ_AR/σ_ε are `const` scalars
inlined into the `rouwenhorst` call, so they were passed as **literals** in the
driver's `init_model!` (a const-redef would silently not propagate — the Julia 1.x
inlining trap). π_birth is a `const` array → in-place mutation propagates, like the
e_age/θ_grid overrides. Startup log confirmed the Rouwenhorst chain rebuilt with
ρ=0.782/σ=0.265 (η_grid range [−2.0231, 2.0231], wider than the 0.05 stub) and
π_birth = the INEGI asymmetric set summing to 1.

**Gates (converged iter 26):** DIFF/Y +8.55e−5 PASS · capital 1.57e−4 PASS ·
Euler max log10 −5.367 (mean −7.418) PASS · two-sex W gap θ_L 29.91% PASS.

### ⚠ Harmonization is MATERIAL (§7 decision branch)

**K = 4.960 vs gate Run 1 K = 10.488 → ΔK = −52.7%**, far past the ±15% threshold.
The §4 narrative must be built on **Run 1′ numbers, not gate Run 1**. The move is
into a genuine equilibrium (smooth monotone convergence, stable K/L≈0.995), not
instability — the σ_ε=0.265 convergence stressor §7 warned of did **not** appear.

Direction is **opposite** to the §2 prediction (which expected larger σ_ε →
more precautionary saving → higher K). Both K and L fell sharply (L 11.57→4.99).
Initial hypothesis was that the asymmetric π_birth dominates (it loads **77.5% of
births onto low-skill types** — M-L .3927 + F-L .3822 — vs 50% under the symmetric
stub; low-skill cohorts earn/save/supply-labor less → lower aggregate K and L).
**The §4 decomposition OVERTURNS this**: the AR(1) re-anchoring is the larger
channel (−4.04 of the −5.53 ΔK) vs π_birth (−2.28), driven by the persistence drop
ρ:0.98→0.782 outweighing the σ_ε rise. See §4 for the four-corner split.

τp = 0.0929 (gate Run 1 was 0.1083) — the anchor Runs 2-4 compare against.

---

## 2. The three experiments (deltas from Run 1′)

Each is Run 1′ + one perturbation, shared `calibrated_lib.jl` machinery (validated
by canarying Run 2 alone before the parallel wave). All converged ≤26 iters; the
self-contained gates (DIFF, capital, Euler, two-sex W gap) PASS for all three.

### Run 2 — κ pension reform 0.50 → 0.30 (joint closure)
Override: `update_pension_taxes!` re-`@eval`ed with κ=0.30 literal (κ_rep is an
inlined const scalar). Iter-1 τp tracked exactly 0.60× = 0.30/0.50 of Run 1′,
confirming propagation.
- **τp falls 9.29% → 5.46%** (gate R2-5 PASS — lower replacement → lower PAYG).
- K +10.7%, Y +6.0%: lower public pensions crowd in private retirement saving.
- **Welfare incidence regressive** (gate R2-6 PASS, sign-robust): θ_H *gains*
  (M_θH +13.5%, in %ΔW terms) while θ_L *loses* (M_θL −4.0%, F_θL −5.6%). Low-skill
  depend on PAYG and lose; high-skill benefit from the higher equilibrium return.
  Sign difference holds regardless of the %ΔW denominator caveat (§3).

### Run 3 — τm health subsidy 0 → −0.20 (joint closure)
Override: `Core.eval(const τm = -0.20)` BEFORE any τm-reading method compiles
(fresh process, load-bearing order; the `WARNING: redefinition of constant Main.τm`
is the expected benign notice). CHECK confirmed τm=−0.2000.
- **M/Y rises 2.728% → 3.217%** (gate R3-7 PASS — subsidized medical spending).
- **τp rises slightly 9.29% → 9.62%** (gate R3-9 PASS — survival channel: longer
  lives → higher dependency).
- **Welfare incidence — FLAGGED, NOT a clean pass (gate R3-8 ⚠).** All four types
  gain in absolute terms, but by the proportional-%ΔW metric the gain is *larger*
  for high-skill (M_θH +7.99% vs M_θL +0.43%; F_θH +1.19% vs F_θL +0.13%) — the
  opposite of the spec's "progressive" expectation. This is most likely a metric
  artifact: θ_H baseline welfare is near zero (M_θH=−0.42) so any absolute gain
  inflates in %. The incidence *direction* cannot be adjudicated without a proper
  CEV (see §3). **For §5: resolve with a consumption-equivalent before claiming
  progressivity.**

### Run 4 — Aging C1: 2050 demographics, joint closure (the cost-of-inaction headline)
Override: `set_demographics!(n_p_2050, ψ_base_male_2050, ψ_base_female_2050)` on the
typed globals n_p/ψ_base (not inlined). Installed n_p=−0.0198 (population
contraction), higher survival (ψ_f[10]=0.988).
- **dep_ratio 0.1857 → 0.3171 (×1.71)** (gate R4-10 — "roughly doubles"; 1.71×, a
  near-doubling rather than exact 2×).
- **τp rises substantially 9.29% → 15.86%** (gate R4-11 PASS) — the headline
  "τp rises under inaction".
- **K +43.8% (4.96→7.13), r falls 4.21%→3.43%** (gate R4-12 PASS) — precautionary
  saving against longer retirement.
- Converged in 24 iters under C1. This is the *feasible* aging response. It does
  NOT hit the rⁿ-crosses-n_p infeasibility — under C1 τp is free to clear PAYG, and
  n_p=−0.0198 keeps rⁿ−n_p positive. The C2 interp-1 infeasibility (Run 0,
  `run0_history.csv`) remains the structural finding for §5.5; Run 4 (C1) is the
  cost-of-inaction headline. Both reported together.

---

## 3. Welfare-metric caveat (affects §5 incidence claims)

`calibrated_welfare_change.csv` reports %ΔW = (W − W_run1prime)/|W_run1prime|·100.
This gives the correct incidence **direction only when baseline welfare levels are
comparable across types** — which they are NOT here: utility is CRRA(γ=2), so W is
negative and θ_H levels sit near zero, inflating their %ΔW (e.g. Run 4 M_θH shows
−121%, an artifact). A valid cross-type incidence statement needs a
**consumption-equivalent variation (CEV)**. An exact closed-form CEV is unavailable
in this model: GHH flow utility is homogeneous in the consumption-composite, but
the additively-separable health-amenity term breaks homogeneity, and
`welfare_at_birth()` returns only total W₁ (no amenity/consumption split). Computing
a CEV requires re-instrumenting the welfare aggregation to expose those components —
a §5 LaTeX-session task. Until then: Run 2 regressivity is sign-robust and safe to
report; Run 3 progressivity is **unconfirmed** and should not be claimed.

---

## 4. §7 K-change decomposition (σ_ε/ρ_AR vs π_birth)

Because ΔK is material, §7 requires decomposing the −52.7% K move. Two diagnostic
solves at the calibrated SMM params, joint closure, each reverting one
harmonization leg:

- **Decomp A** (`decompA_aronly`): AR(1) harmonized, π_birth reverted to symmetric.
- **Decomp B** (`decompB_pibirthonly`): π_birth asymmetric, AR(1) reverted to stub.

Four-corner table (gate Run 1 and Run 1′ already exist; both decomp legs
converged, joint closure, calibrated SMM):

| K | symm π_birth | asym π_birth |
|---|---:|---:|
| **stub AR(1)** (ρ=0.98, σ_ε=0.05) | gate Run 1: **10.488** | Decomp B: **8.210** |
| **harm AR(1)** (ρ=0.782, σ_ε=0.265) | Decomp A: **6.450** | Run 1′: **4.960** |

**Total ΔK = 4.960 − 10.488 = −5.528 (−52.7%).** Single-channel effects (each leg
alone, from the gate corner) plus interaction:

| channel | ΔK | % of total | % of gate K |
|---|---:|---:|---:|
| AR(1) re-anchoring (ρ↓ & σ_ε↑) | −4.038 | 73.0% | −38.5% |
| π_birth asymmetry (low-skill-heavy) | −2.278 | 41.2% | −21.7% |
| interaction (sub-additive) | +0.788 | −14.3% | +7.5% |
| **total** | **−5.528** | **100%** | **−52.7%** |

Check: 10.488 − 4.038 − 2.278 + 0.788 = 4.960 ✓. (Shapley-symmetric split, which
exhausts with no residual: AR(1) −3.64, π_birth −1.88.)

**The AR(1) re-anchoring is the LARGER channel** (−4.04 vs π_birth −2.28),
overturning the §1 leading hypothesis that the asymmetric π_birth dominates. Both
push K down; they are mildly sub-additive (+0.79 interaction).

**Sign note (matters for §7 calibration discussion).** The AR(1) leg LOWERS K even
though σ_ε rose (0.05→0.265), which in isolation raises precautionary saving. The
net K↓ means the **persistence drop (ρ: 0.98→0.782) dominates the variance rise**:
at ρ=0.98 shocks are near-permanent and drive strong buffer-stock saving; at
ρ=0.782 they mean-revert fast and are smoothed via consumption, so much less wealth
accumulates — and the unconditional-variance increase (σ²/(1−ρ²): 0.063→0.181) is
not enough to offset it. Caveat: Decomp A moved ρ and σ_ε *together* (the full
PE-anchor re-anchoring), so this is the joint AR(1) effect; a ρ-only / σ-only split
would confirm the persistence-dominates reading but was not required by §7.

dep_ratio and τp at both decomp corners (≈0.2025 / ≈0.101) sit between gate Run 1
(0.2166 / 0.1083) and Run 1′ (0.1857 / 0.0929), as expected.

---

## 5. Deviations / things for the next session

1. **Project flag.** Spec §4 said `--project=.`; there is no `Project.toml` at the
   repo root, so that gives an empty env (`OffsetArrays not found`). Correct env is
   `--project=stationary_experiments`. Fixed in the spec doc; used throughout.
2. **K-change is material (−52.7%)** — §4 baseline = Run 1′, not gate Run 1.
3. **Run 3 progressivity unconfirmed** — needs a CEV (§3).
4. **dep_ratio ×1.71, not 2×** for the 2050 shock at this calibration.
5. Run 0 (C2 interp-1 infeasibility) NOT re-run — gate already passed; mechanism
   robust (§4 spec). `run0_history.csv` stands.

---

## 6. Files produced this session
Drivers: `run1prime.jl`, `calibrated_lib.jl`, `run2_kappa30.jl`, `run3_taum20.jl`,
`run4_agingC1.jl`, `decompA_aronly.jl`, `decompB_pibirthonly.jl`,
`assemble_calibrated.py`.
Outputs (`results/`): `run1prime_*`, `run2_kappa30_*`, `run3_taum20_*`,
`run4_agingC1_*`, `decomp{A,B}_*`, `calibrated_comparison.csv`,
`calibrated_welfare_change.csv`, and the `*.log` for each.

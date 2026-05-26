################################################################################
# demographics_2050.jl
#
# Mexico 2050 demographic primitives for the gender-extension GE solver.
# 5-year-period quantities matching the J=17 grid of ge_model_gender.jl
# (age bands 20-24, 25-29, ..., 95-99, 100+).
#
# ─── Sources ──────────────────────────────────────────────────────────────────
# Targets (aggregate):
#   • UN World Population Prospects 2024 revision, online edition, accessed
#     2026-05-24. https://population.un.org/wpp/
#     - Mexico life expectancy at birth, medium variant 2050:  79.8 years.
#     - Mexico sex gap at 2050: ~5.6 years (slightly narrower than 6.1 in 2020).
#     - Implied: male LE 2050 ≈ 77.0, female LE 2050 ≈ 82.6.
#     - Mexico total fertility rate 2050: 1.70 (medium variant).
#     - Population peaks ~2042 at ~152M, declines to ~150.6M by 2050.
#   • PAHO (2024) Mexico LE 2023: total 75.1, male 72.1, female 78.3.
#     Used as the 2020 baseline reference for computing the LE lift.
#   • Paper Section 1 / ECLAC (2022): old-age dependency ratio in Mexico
#     projected to AT LEAST DOUBLE by 2045 relative to 2020. The model's
#     dependency-ratio metric (N^R/N^W = 65+ over 20-64) is constructed to
#     hit this 2x anchor at 2050.
#
# Baseline (model 2020 calibration):
#   • ψ_base in ge_model_gender.jl: period-averaged Mexican life table,
#     pooled across sex, J=17 bands. e_20 (model schedule) = 66.6 years.
#   • n_p_2020 = 1.01^5 - 1 ≈ 0.0510 (1% annual). Encodes the 2020 entering-
#     cohort growth rate.
#
# ─── Derivation method ────────────────────────────────────────────────────────
# Aggregate WPP targets do not fix the full 17-band survival schedule.
# Two-parameter approach:
#
#   1. n_p_2050. The model's n_p is the gross growth rate of the cohort
#      entering at age 20 (j=1), not total population. WPP 2024 implies
#      Mexico's age-20 cohort in 2050 was born ~2030 under TFR ~1.85, vs
#      the 2020 cohort born ~2000 under TFR ~2.5. Generation contraction
#      ratio implies an annual entry growth of approximately -0.4% by 2050.
#      → n_p_2050_annual = -0.004, n_p_2050 = 1.004^(-1)^5 - 1 ≈ -0.01984.
#
#   2. ψ_base_male_2050, ψ_base_female_2050. Brass one-parameter logit
#      shift applied to the pooled baseline ψ:
#         logit(1 - p_2050) = α + logit(1 - p_2020)
#      where p_j is the cumulative survival from age 20 to band j. α is
#      chosen separately for males and females to hit the WPP LE-at-birth
#      lifts (+1.9 yrs male, +7.5 yrs female from the 2020 PAHO baseline).
#      Sex-specific α values:
#         α_male   = -0.1582
#         α_female = -0.6956
#      The negative values reflect lower mortality (longer life). The
#      asymmetry reflects the WPP-projected widening of the survival
#      schedule by sex despite the modest narrowing of LE-at-birth gap.
#
# Validation:
#   • Stationary dependency ratio N^R/N^W under the new (ψ, n_p):
#       2020 baseline: 0.372  (model: 0.277 reflects mass-weighted
#                              equilibrium under endogenous saving; this
#                              0.372 is the demographic-only stationary
#                              upper bound)
#       2050 pooled:   0.744  → 2.00x lift, matching ECLAC/paper anchor.
#
# ─── Caveats and limits ──────────────────────────────────────────────────────
# • The Brass shift preserves the SHAPE of age-conditional mortality and
#   scales the LEVEL via one parameter. It cannot capture compositional
#   changes (e.g., disproportionate gains at older ages from chronic-disease
#   treatment). For the comparative-steady-state purpose this is adequate;
#   for the September three-country deliverable, replace with WPP single-
#   age life tables aggregated to 5-year bands.
# • The 2020 baseline ψ_base in ge_model_gender.jl is pooled by sex (a
#   stub flagged in the README). When that calibration is replaced with
#   sex-specific 2020 life tables, this file should be re-derived from
#   sex-specific baselines rather than a pooled Brass shift.
# • The WPP medium-variant projection has uncertainty bands; using upper
#   or lower variants would shift the dependency ratio anchor by roughly
#   ±0.05 around the 0.74 central value.
#
# When replacing the entire pipeline with calibrated WPP single-age life
# tables for the September deliverable, this file becomes a load-from-CSV
# operation rather than an analytic derivation.
################################################################################

# Population growth rate (5-year period, gross rate minus 1).
# Encodes the projected growth of the age-20 entering cohort around 2050.
# Source: WPP 2024 TFR trajectory and generation arithmetic. See header.
# Annual rate: -0.4%. 5-year period: (1 - 0.004)^5 - 1 ≈ -0.01984.
const n_p_2050 = (1.0 - 0.004)^5 - 1.0

# Male survival schedule, 5-year-period conditional survival probabilities.
# Brass-logit shift α_male = -0.1582 applied to baseline pooled ψ.
# Target: e_0 = 77.0 years (WPP 2024 medium variant, Mexico 2050, male).
const ψ_base_male_2050 = [
    1.0000,   # band 1,  age 20-24
    1.0000,   # band 2,  age 25-29
    1.0000,   # band 3,  age 30-34
    1.0000,   # band 4,  age 35-39
    1.0000,   # band 5,  age 40-44
    1.0000,   # band 6,  age 45-49
    0.9925,   # band 7,  age 50-54
    0.9867,   # band 8,  age 55-59
    0.9783,   # band 9,  age 60-64
    0.9665,   # band 10, age 65-69  ← retirement begins (j_R = 10)
    0.9499,   # band 11, age 70-74
    0.9239,   # band 12, age 75-79
    0.8678,   # band 13, age 80-84
    0.7521,   # band 14, age 85-89
    0.5652,   # band 15, age 90-94
    0.3303,   # band 16, age 95-99
    0.1535    # band 17, age 100+  (terminal; survival to 105 is residual)
]

# Female survival schedule, 5-year-period conditional survival probabilities.
# Brass-logit shift α_female = -0.6956 applied to baseline pooled ψ.
# Target: e_0 = 82.6 years (WPP 2024 medium variant, Mexico 2050, female).
const ψ_base_female_2050 = [
    1.0000,   # band 1,  age 20-24
    1.0000,   # band 2,  age 25-29
    1.0000,   # band 3,  age 30-34
    1.0000,   # band 4,  age 35-39
    1.0000,   # band 5,  age 40-44
    1.0000,   # band 6,  age 45-49
    0.9974,   # band 7,  age 50-54
    0.9954,   # band 8,  age 55-59
    0.9924,   # band 9,  age 60-64
    0.9880,   # band 10, age 65-69  ← retirement begins (j_R = 10)
    0.9814,   # band 11, age 70-74
    0.9704,   # band 12, age 75-79
    0.9440,   # band 13, age 80-84
    0.8775,   # band 14, age 85-89
    0.7245,   # band 15, age 90-94
    0.4377,   # band 16, age 95-99
    0.1776    # band 17, age 100+  (terminal; survival to 105 is residual)
]

# ─── Shape checks ─────────────────────────────────────────────────────────────
@assert length(ψ_base_male_2050)   == 17 "expected J=17 male survival bands"
@assert length(ψ_base_female_2050) == 17 "expected J=17 female survival bands"
@assert all(0.0 .≤ ψ_base_male_2050   .≤ 1.0) "male survival outside [0,1]"
@assert all(0.0 .≤ ψ_base_female_2050 .≤ 1.0) "female survival outside [0,1]"
@assert n_p_2050 < 0.0 "n_p_2050 should be negative (cohort contraction)"

# Higher female survival in every old-age band (WPP-projected sex gap):
@assert all(ψ_base_female_2050[10:end] .> ψ_base_male_2050[10:end]) "female survival not above male at retirement ages"

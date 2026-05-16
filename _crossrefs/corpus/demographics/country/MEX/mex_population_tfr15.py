"""
Mexico population projection under TFR=1.5 stable, 2023 → 2050.

User context (2026-05-16): UN WPP 2024 and CONAPO Proyecciones 2018-2070
revisión 2023 both assume Mexico's TFR rises modestly from ~1.6 toward
~1.7 by mid-century. Anne's anchor in scenario_anchors.md records the
observed 2023 TFR at 1.60 (INEGI ENADID 2023). Recent observations
suggest the fast-transition pattern (CRI 1.12, CHL 1.03, COL 1.10 in
2024) may apply to Mexico too — i.e., TFR=1.5 stable is closer to the
fast-transition baseline than UN's optimistic recovery path.

This script runs a counterfactual: what if Mexico's TFR is 1.5 every
year from 2023 to 2050, instead of UN's gentle rise toward 1.7?

Method: cohort-component projection
- Age groups: 5-year (0-4, 5-9, ..., 100+) — 21 groups
- Time step: 5 years (2023 → 2028 → 2033 → 2038 → 2043 → 2048; then
  linear interpolation to 2050 for the final value)
- Sex: both sexes, with female share 0.5 (slight simplification; the
  true female share is ~49% at younger ages, ~55% at oldest)
- Mortality: stylized Coale-Demeny "West" pattern at e_0 ≈ 75, fixed
  (no mortality improvement to 2050). UN WPP assumes ~3-5 year gain
  in e_0 by 2050, so this projection is conservative on the dying side.
- Fertility: TFR=1.5 distributed across age groups using Mexico's
  recent ASFR shape (peak in 25-29 group).
- Migration: zero. Mexico has been a net emigrant; UN WPP assumes net
  outflow of ~0.5 per 1000/year. With zero migration assumption, this
  projection is generous compared to a more realistic emigration case.

Outputs:
  - Total population by year, 2023 → 2050 under TFR=1.5
  - Comparison to UN WPP 2024 medium variant
  - PNG plot saved alongside this script

Run from the dalila env:
    ~/miniforge3/envs/dalila/bin/python mex_population_tfr15.py
"""

import io
from pathlib import Path
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
OUT_PNG = HERE / "mex_population_tfr15.png"

OWID_5YR = "https://ourworldindata.org/grapher/population-by-five-year-age-group.csv"
OWID_LONG = "https://ourworldindata.org/grapher/population-long-run-with-projections.csv"

AGE_LABELS = [
    "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34",
    "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69",
    "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100+",
]
N_AGES = len(AGE_LABELS)

# Stylized 5-year cohort survival ratios for a population with
# life expectancy at birth ≈ 75 years (Coale-Demeny "West" model, both
# sexes averaged). S[i] is the probability that someone in age group i
# survives to age group i+1 over a 5-year period.
SURVIVAL = np.array([
    0.985,  # 0-4 → 5-9
    0.997,  # 5-9 → 10-14
    0.997,  # 10-14 → 15-19
    0.995,  # 15-19 → 20-24
    0.993,  # 20-24 → 25-29
    0.992,  # 25-29 → 30-34
    0.991,  # 30-34 → 35-39
    0.989,  # 35-39 → 40-44
    0.984,  # 40-44 → 45-49
    0.978,  # 45-49 → 50-54
    0.969,  # 50-54 → 55-59
    0.954,  # 55-59 → 60-64
    0.929,  # 60-64 → 65-69
    0.890,  # 65-69 → 70-74
    0.832,  # 70-74 → 75-79
    0.745,  # 75-79 → 80-84
    0.620,  # 80-84 → 85-89
    0.470,  # 85-89 → 90-94
    0.300,  # 90-94 → 95-99
    0.150,  # 95-99 → 100+
    0.050,  # 100+ stays 100+ (one 5-year horizon)
])

# Newborn-cohort survival from birth to the end of the first 5-year
# age group: roughly (1 - IMR) × 4-year child survival. For Mexico
# (IMR ~12/1000), about 0.97.
BIRTH_TO_AGE_0_4 = 0.97

# Mexico ASFR shape — fertility distribution across women in 5-year
# age groups 15-19 ... 45-49 (7 groups). Births per woman per year.
# Values normalized below so that 5 × sum equals the target TFR.
# Shape based on recent Mexico ASFR pattern (peak in 25-29).
ASFR_SHAPE = np.array([
    0.045,  # 15-19
    0.090,  # 20-24
    0.110,  # 25-29  ← peak
    0.090,  # 30-34
    0.060,  # 35-39
    0.020,  # 40-44
    0.005,  # 45-49
])
ASFR_FERTILE_START = 3  # index in AGE_LABELS where fertile ages begin (15-19)
ASFR_FERTILE_END = 10   # exclusive, so groups 3..9 = 15-19 ... 45-49

FEMALE_SHARE = 0.5      # share of each age group that is female
FEMALE_AT_BIRTH = 0.485  # share of newborns that are female (sex ratio at birth ~1.05M:1F)

TFR = 1.5


def fetch_owid_csv(url: str) -> pd.DataFrame:
    print(f"Fetching {url} ...")
    with urllib.request.urlopen(url, timeout=60) as resp:
        return pd.read_csv(io.BytesIO(resp.read()))


def baseline_2023() -> np.ndarray:
    df = fetch_owid_csv(OWID_5YR)
    mex = df[(df["Code"] == "MEX") & (df["Year"] == 2023)].iloc[0]
    cols = [c for c in df.columns if "year" in c.lower() and "Year" != c][:N_AGES]
    pop = mex[cols].to_numpy(dtype=float)
    assert len(pop) == N_AGES
    return pop


def project_step(pop: np.ndarray, tfr: float) -> np.ndarray:
    """Single 5-year cohort-component step. Returns new age vector."""
    asfr = ASFR_SHAPE * tfr / (5.0 * ASFR_SHAPE.sum())  # rescale shape to target TFR

    # Births during 5 years, using start-of-period women (simplification
    # — proper version uses mid-period or person-years). For each
    # 5-year fertile age group, woman-years ≈ women × 5.
    women = pop[ASFR_FERTILE_START:ASFR_FERTILE_END] * FEMALE_SHARE
    births = (asfr * women * 5.0).sum()

    new_pop = np.zeros_like(pop)
    # Age forward: pop[i+1, t+5] = pop[i, t] × S[i]
    new_pop[1:N_AGES] = pop[: N_AGES - 1] * SURVIVAL[: N_AGES - 1]
    # 100+ open interval: surviving 100+ stay 100+
    new_pop[N_AGES - 1] += pop[N_AGES - 1] * SURVIVAL[N_AGES - 1]
    # Newborns enter 0-4 at the end of the period
    new_pop[0] = births * BIRTH_TO_AGE_0_4

    return new_pop


def project_through(pop_2023: np.ndarray, tfr: float, end_year: int = 2050):
    """Project forward in 5-year steps; interpolate to end_year."""
    years = list(range(2023, end_year + 1, 5))
    if years[-1] < end_year:
        years.append(end_year)

    totals = [pop_2023.sum()]
    pop_by_year = {2023: pop_2023.copy()}

    pop = pop_2023.copy()
    for i in range(1, len(years)):
        target_year = years[i]
        step_years = target_year - years[i - 1]
        if step_years == 5:
            pop = project_step(pop, tfr)
        else:
            # Partial-step (for the trailing 2048→2050 case)
            pop_5 = project_step(pop, tfr)
            frac = step_years / 5.0
            pop = pop + frac * (pop_5 - pop)
        pop_by_year[target_year] = pop.copy()
        totals.append(pop.sum())

    return years, np.array(totals), pop_by_year


def un_medium_total_through_2050() -> pd.DataFrame:
    df = fetch_owid_csv(OWID_LONG)
    mex = df[df["Code"] == "MEX"].copy()
    proj_col = next(c for c in mex.columns if "projection" in c.lower())
    mex["pop"] = mex["Population"].combine_first(mex[proj_col])
    mex = mex[(mex["Year"] >= 2023) & (mex["Year"] <= 2050)][["Year", "pop"]]
    return mex.sort_values("Year").reset_index(drop=True)


def main():
    pop_2023 = baseline_2023()
    total_2023 = pop_2023.sum() / 1e6
    print(f"Baseline 2023: {total_2023:.2f}M (sum across {N_AGES} 5-year groups)")

    years, totals, pop_by_year = project_through(pop_2023, TFR, end_year=2050)
    totals_m = totals / 1e6

    print(f"\nTFR={TFR} stable, zero migration, fixed mortality (e_0 ≈ 75):")
    for y, t in zip(years, totals_m):
        print(f"  {y}  {t:7.2f} M")

    # UN WPP 2024 medium variant for comparison
    un = un_medium_total_through_2050()
    un_m = un["pop"].to_numpy() / 1e6

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(un["Year"], un_m, color="#1f3a5f", linewidth=2.0, linestyle="--",
            label="UN WPP 2024 medium variant (TFR ≈ 1.6→1.7)")
    ax.plot(years, totals_m, color="#a83232", linewidth=2.5, marker="o", markersize=5,
            label=f"Counterfactual: TFR = {TFR} stable, no migration, fixed mortality")

    # Annotate 2050 gap
    un_2050 = un_m[-1]
    cf_2050 = totals_m[-1]
    gap = un_2050 - cf_2050
    ax.annotate(f"{un_2050:.1f} M", xy=(2050, un_2050), xytext=(8, 0),
                textcoords="offset points", ha="left", va="center",
                fontsize=10, color="#1f3a5f")
    ax.annotate(f"{cf_2050:.1f} M", xy=(2050, cf_2050), xytext=(8, 0),
                textcoords="offset points", ha="left", va="center",
                fontsize=10, color="#a83232")
    ax.annotate(f"gap: {gap:.1f} M", xy=(2050, (un_2050 + cf_2050) / 2),
                xytext=(-90, 0), textcoords="offset points", ha="right",
                fontsize=10, color="#555")

    ax.set_title(f"Mexico — total population, 2023 → 2050\n"
                 f"UN WPP 2024 medium variant vs. counterfactual TFR={TFR} stable",
                 fontsize=13, loc="left")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population (millions)")
    ax.set_xlim(2023, 2055)
    ax.set_ylim(min(min(totals_m), min(un_m)) * 0.93, max(max(totals_m), max(un_m)) * 1.05)
    ax.grid(alpha=0.25)
    ax.legend(loc="lower right", framealpha=0.95)

    ax.text(0.01, -0.18,
            f"Counterfactual method: cohort-component, 5-yr age groups × 5-yr steps; ASFR shape Mexico-like (peak 25-29);\n"
            f"mortality fixed at Coale-Demeny West e_0 ≈ 75; zero migration. Sensitivities: a small mortality improvement\n"
            f"by 2050 would add ~1-2 M; net emigration would subtract ~1-2 M. The dominant driver of the gap to UN is TFR.",
            transform=ax.transAxes, fontsize=8, color="#555")

    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    print(f"\nWrote {OUT_PNG}")

    # 2050 comparison table
    print("\n2050 comparison (Mexico, total population):")
    print(f"  UN WPP 2024 medium variant : {un_2050:.2f} M")
    print(f"  Counterfactual TFR={TFR}      : {cf_2050:.2f} M")
    print(f"  Gap                         : {gap:.2f} M  ({gap / un_2050 * 100:.1f}% lower)")


if __name__ == "__main__":
    main()

"""
Mexico population projection under a sharp TFR decline to 1.0, 2023 → 2050.

User-specified TFR trajectory:
  2024: 1.60 (carryover from 2023 INEGI ENADID anchor; unspecified, assumed flat)
  2025: 1.50
  2026: 1.40
  2027: 1.30
  2028: 1.20
  2029: 1.10
  2030+: 1.00  (constant through 2050)

Method (same cohort-component skeleton as mex_population_tfr15.py):
- 5-year age groups × 5-year time steps from 2023 baseline (OWID/UN WPP).
- TFR averaged across the 5 birth-years in each step interval.
- Mexico-shape ASFR rescaled to per-period TFR (shape held fixed).
- Coale-Demeny West e_0 ≈ 75 mortality fixed (no improvement).
- Zero migration.
- Sex ratio at birth 1.05M:1F.
- Partial linear-interp step for 2048→2050.

This scenario is **dramatically more pessimistic than UN WPP 2024 medium
variant**. UN assumes TFR rises gently from ~1.6 to ~1.7 by 2050. This
trajectory collapses to 1.0 — well below any current LAC observation
(Chile's 1.03 in 2024 is the regional floor). The Republic of Korea is
the only major country near 1.0 globally (~0.78 in 2022). So this is an
extreme stress scenario, not a forecast.

Outputs:
  - mex_population_tfr_decline.png
"""

import io
from pathlib import Path
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
OUT_PNG = HERE / "mex_population_tfr_decline.png"

OWID_5YR = "https://ourworldindata.org/grapher/population-by-five-year-age-group.csv"
OWID_LONG = "https://ourworldindata.org/grapher/population-long-run-with-projections.csv"

N_AGES = 21

SURVIVAL = np.array([
    0.985, 0.997, 0.997, 0.995, 0.993, 0.992, 0.991, 0.989, 0.984, 0.978,
    0.969, 0.954, 0.929, 0.890, 0.832, 0.745, 0.620, 0.470, 0.300, 0.150,
    0.050,
])
BIRTH_TO_AGE_0_4 = 0.97
ASFR_SHAPE = np.array([0.045, 0.090, 0.110, 0.090, 0.060, 0.020, 0.005])
ASFR_FERTILE_START = 3
ASFR_FERTILE_END = 10
FEMALE_SHARE = 0.5

# User-specified annual TFR trajectory.
TFR_ANNUAL = {
    2024: 1.60,
    2025: 1.50,
    2026: 1.40,
    2027: 1.30,
    2028: 1.20,
    2029: 1.10,
}
TFR_FROM_2030 = 1.00


def tfr_for_year(y: int) -> float:
    if y in TFR_ANNUAL:
        return TFR_ANNUAL[y]
    if y >= 2030:
        return TFR_FROM_2030
    raise ValueError(f"No TFR for year {y}")


def period_tfr(year_start: int, year_end: int) -> float:
    """Mean TFR across birth years (year_start+1, ..., year_end)."""
    birth_years = list(range(year_start + 1, year_end + 1))
    return float(np.mean([tfr_for_year(y) for y in birth_years]))


def fetch_owid_csv(url: str) -> pd.DataFrame:
    print(f"Fetching {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Dalila/1.0 (research)"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return pd.read_csv(io.BytesIO(resp.read()))


def baseline_2023() -> np.ndarray:
    df = fetch_owid_csv(OWID_5YR)
    row = df[(df["Code"] == "MEX") & (df["Year"] == 2023)].iloc[0]
    age_cols = [c for c in df.columns if c not in ("Entity", "Code", "Year")][:N_AGES]
    pop = row[age_cols].to_numpy(dtype=float)
    return pop


def project_step(pop: np.ndarray, tfr: float, frac: float = 1.0) -> np.ndarray:
    """5-year cohort-component step (frac<1 for partial trailing step)."""
    asfr = ASFR_SHAPE * tfr / (5.0 * ASFR_SHAPE.sum())
    women = pop[ASFR_FERTILE_START:ASFR_FERTILE_END] * FEMALE_SHARE
    births_full = (asfr * women * 5.0).sum()

    new_pop_full = np.zeros_like(pop)
    new_pop_full[1:N_AGES] = pop[: N_AGES - 1] * SURVIVAL[: N_AGES - 1]
    new_pop_full[N_AGES - 1] += pop[N_AGES - 1] * SURVIVAL[N_AGES - 1]
    new_pop_full[0] = births_full * BIRTH_TO_AGE_0_4

    if frac == 1.0:
        return new_pop_full
    return pop + frac * (new_pop_full - pop)


def project_trajectory(pop_2023: np.ndarray):
    years = [2023, 2028, 2033, 2038, 2043, 2048, 2050]
    totals = [pop_2023.sum()]
    pop = pop_2023.copy()
    tfrs_used = []
    for i in range(1, len(years)):
        y0, y1 = years[i - 1], years[i]
        tfr_period = period_tfr(y0, y1)
        tfrs_used.append((y0, y1, tfr_period))
        step_yrs = y1 - y0
        if step_yrs == 5:
            pop = project_step(pop, tfr_period, frac=1.0)
        else:
            pop = project_step(pop, tfr_period, frac=step_yrs / 5.0)
        totals.append(pop.sum())
    return years, np.array(totals), tfrs_used


def un_medium_trajectory() -> pd.DataFrame:
    df = fetch_owid_csv(OWID_LONG)
    mex = df[df["Code"] == "MEX"].copy()
    proj_col = next(c for c in mex.columns if "projection" in c.lower())
    mex["pop"] = mex["Population"].combine_first(mex[proj_col])
    mex = mex[(mex["Year"] >= 2023) & (mex["Year"] <= 2050)][["Year", "pop"]]
    return mex.sort_values("Year").reset_index(drop=True)


def main():
    pop_2023 = baseline_2023()
    print(f"Baseline 2023: {pop_2023.sum() / 1e6:.2f} M")

    years, totals, tfrs_used = project_trajectory(pop_2023)
    totals_m = totals / 1e6

    print("\nPeriod-averaged TFR used per step:")
    for y0, y1, t in tfrs_used:
        print(f"  {y0} → {y1}  TFR_avg = {t:.3f}")

    print(f"\nDeclining-TFR trajectory:")
    for y, t in zip(years, totals_m):
        print(f"  {y}  {t:7.2f} M")

    un = un_medium_trajectory()
    un_m = un["pop"].to_numpy() / 1e6
    cf_2050 = totals_m[-1]
    un_2050 = un_m[-1]
    gap = un_2050 - cf_2050
    print(f"\n2050: UN={un_2050:.2f}M  scenario={cf_2050:.2f}M  gap={gap:.2f}M ({gap/un_2050*100:.1f}%)")

    # Plot — main curve + small inset of the TFR trajectory
    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.plot(un["Year"], un_m, color="#1f3a5f", linewidth=2.0, linestyle="--",
            label="UN WPP 2024 medium variant (TFR ≈ 1.6→1.7)")
    ax.plot(years, totals_m, color="#7d2222", linewidth=2.5, marker="o", markersize=5,
            label="Scenario: TFR → 1.0 by 2030, stable to 2050")

    # Annotate end values
    ax.annotate(f"{un_2050:.1f} M", xy=(2050, un_2050), xytext=(8, 0),
                textcoords="offset points", ha="left", va="center",
                fontsize=10, color="#1f3a5f")
    ax.annotate(f"{cf_2050:.1f} M", xy=(2050, cf_2050), xytext=(8, 0),
                textcoords="offset points", ha="left", va="center",
                fontsize=10, color="#7d2222")
    ax.annotate(f"gap: {gap:.1f} M\n({gap/un_2050*100:.1f}%)",
                xy=(2050, (un_2050 + cf_2050) / 2),
                xytext=(-100, 0), textcoords="offset points", ha="right",
                fontsize=10, color="#555")

    ax.set_title("Mexico — total population, 2023 → 2050\n"
                 "UN WPP 2024 medium variant vs. TFR-decline-to-1.0 scenario",
                 fontsize=13, loc="left")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population (millions)")
    ax.set_xlim(2023, 2055)
    ax.set_ylim(min(min(totals_m), min(un_m)) * 0.93,
                max(max(totals_m), max(un_m)) * 1.05)
    ax.grid(alpha=0.25)
    ax.legend(loc="lower right", framealpha=0.95)

    # Inset showing the TFR trajectory
    inset = fig.add_axes([0.13, 0.20, 0.22, 0.22])
    yrs_tfr = list(range(2024, 2051))
    tfrs = [tfr_for_year(y) for y in yrs_tfr]
    inset.plot(yrs_tfr, tfrs, color="#7d2222", linewidth=2.0, marker="o", markersize=3)
    inset.axhline(2.1, color="#888", linestyle=":", linewidth=1, alpha=0.7)
    inset.text(2026, 2.13, "reemplazo (~2.1)", fontsize=7, color="#888")
    inset.text(2026, 1.05, "TFR = 1.0", fontsize=8, color="#7d2222")
    inset.set_title("Trayectoria TFR asumida", fontsize=9)
    inset.set_xlim(2024, 2050)
    inset.set_ylim(0.8, 2.3)
    inset.tick_params(labelsize=7)
    inset.grid(alpha=0.25)

    ax.text(0.01, -0.16,
            "Stress scenario, not a forecast. TFR=1.0 is below any current LAC observation (Chile 1.03 in 2024). "
            "Method: cohort-component, 5-yr groups × 5-yr steps; period-averaged TFR across the user-specified annual\n"
            "trajectory; Mexico-shape ASFR (peak 25-29); Coale-Demeny West e_0≈75 fixed mortality; zero migration.",
            transform=ax.transAxes, fontsize=8, color="#555")

    plt.tight_layout(rect=[0, 0.02, 1, 1])
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    print(f"\nWrote {OUT_PNG}")


if __name__ == "__main__":
    main()

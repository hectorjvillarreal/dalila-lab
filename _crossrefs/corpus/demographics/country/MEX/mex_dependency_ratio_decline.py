"""
Mexico dependency ratios 2023→2050 under TFR-decline-to-1.0 scenario,
compared to a UN-like ~1.65 stable benchmark.

Why dependency ratios (DR) and not total population:
The total-population gap to UN (13.5% by 2050 in the TFR-decline scenario)
understates the fiscal pressure. What drives pension contribution rate and
health-financing path is the *ratio* of dependents to working-age, not
total people. Under a TFR collapse, the 65+ population is locked in (those
people are already alive); only the denominator (working-age) and the
youth numerator change. The result is a sharper rise in old-age
dependency, partly offset by a fall in youth dependency.

Definitions (UN convention):
  Youth dependency ratio (YDR) = pop(0-14) / pop(15-64) × 100
  Old-age dependency ratio (OADR) = pop(65+) / pop(15-64) × 100
  Total dependency ratio (TDR) = YDR + OADR

Scenarios:
  TFR-decline: 1.60 (2024) → 1.50 → 1.40 → 1.30 → 1.20 → 1.10 (2029)
               → 1.00 from 2030 stable to 2050.
  UN-like baseline: TFR ≈ 1.65 stable. This is an approximation of UN
               WPP 2024 medium variant's trajectory (Mexico TFR rises
               from ~1.62 in 2024 to ~1.71 by 2050; mid-point ~1.66).

Method: same cohort-component skeleton as the population scripts. 5-year
age groups, 5-year time steps, partial-step interpolation to 2050.
Coale-Demeny West e_0≈75 fixed mortality, zero migration, Mexico-shape
ASFR, sex ratio at birth 1.05.

Output: mex_dependency_ratio_decline.png (in the same folder).
"""

import io
from pathlib import Path
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
OUT_PNG = HERE / "mex_dependency_ratio_decline.png"
OWID_5YR = "https://ourworldindata.org/grapher/population-by-five-year-age-group.csv"

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

# Age index slices
YOUTH = slice(0, 3)        # 0-4, 5-9, 10-14  → 0-14
WORKING = slice(3, 13)     # 15-19 ... 60-64  → 15-64
OLD = slice(13, N_AGES)    # 65-69 ... 100+   → 65+

# User-specified TFR trajectory for the decline scenario.
TFR_DECLINE_ANNUAL = {
    2024: 1.60, 2025: 1.50, 2026: 1.40, 2027: 1.30, 2028: 1.20, 2029: 1.10,
}
TFR_DECLINE_FROM_2030 = 1.00

# UN-like baseline (approximation of WPP 2024 medium variant Mexico TFR).
TFR_UN_LIKE = 1.65


def tfr_decline(y: int) -> float:
    return TFR_DECLINE_ANNUAL.get(y, TFR_DECLINE_FROM_2030 if y >= 2030 else 1.60)


def period_tfr_decline(y0: int, y1: int) -> float:
    return float(np.mean([tfr_decline(y) for y in range(y0 + 1, y1 + 1)]))


def fetch_owid_csv(url: str) -> pd.DataFrame:
    print(f"Fetching {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Dalila/1.0 (research)"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return pd.read_csv(io.BytesIO(resp.read()))


def baseline_2023() -> np.ndarray:
    df = fetch_owid_csv(OWID_5YR)
    row = df[(df["Code"] == "MEX") & (df["Year"] == 2023)].iloc[0]
    age_cols = [c for c in df.columns if c not in ("Entity", "Code", "Year")][:N_AGES]
    return row[age_cols].to_numpy(dtype=float)


def project_step(pop: np.ndarray, tfr: float, frac: float = 1.0) -> np.ndarray:
    asfr = ASFR_SHAPE * tfr / (5.0 * ASFR_SHAPE.sum())
    women = pop[ASFR_FERTILE_START:ASFR_FERTILE_END] * FEMALE_SHARE
    births = (asfr * women * 5.0).sum()
    new_pop = np.zeros_like(pop)
    new_pop[1:N_AGES] = pop[: N_AGES - 1] * SURVIVAL[: N_AGES - 1]
    new_pop[N_AGES - 1] += pop[N_AGES - 1] * SURVIVAL[N_AGES - 1]
    new_pop[0] = births * BIRTH_TO_AGE_0_4
    if frac == 1.0:
        return new_pop
    return pop + frac * (new_pop - pop)


def project(pop_2023: np.ndarray, tfr_for_period) -> tuple[list[int], np.ndarray]:
    """Project age structure. tfr_for_period(y0, y1) returns the TFR for that period."""
    years = [2023, 2028, 2033, 2038, 2043, 2048, 2050]
    structure = [pop_2023.copy()]
    pop = pop_2023.copy()
    for i in range(1, len(years)):
        y0, y1 = years[i - 1], years[i]
        tfr_p = tfr_for_period(y0, y1)
        step_yrs = y1 - y0
        pop = project_step(pop, tfr_p, frac=1.0 if step_yrs == 5 else step_yrs / 5.0)
        structure.append(pop.copy())
    return years, np.array(structure)  # shape (n_years, N_AGES)


def dependency_ratios(structure: np.ndarray):
    """structure shape (n_years, N_AGES) → (years, YDR, OADR, TDR)."""
    youth = structure[:, YOUTH].sum(axis=1)
    working = structure[:, WORKING].sum(axis=1)
    old = structure[:, OLD].sum(axis=1)
    ydr = youth / working * 100
    oadr = old / working * 100
    tdr = ydr + oadr
    return ydr, oadr, tdr


def main():
    pop_2023 = baseline_2023()

    # Decline scenario
    years, struct_decline = project(pop_2023, period_tfr_decline)
    ydr_d, oadr_d, tdr_d = dependency_ratios(struct_decline)

    # UN-like baseline (TFR=1.65 stable)
    _, struct_un = project(pop_2023, lambda y0, y1: TFR_UN_LIKE)
    ydr_u, oadr_u, tdr_u = dependency_ratios(struct_un)

    # Print table
    print(f"\nDependency ratios per 100 working-age (15-64), Mexico 2023→2050")
    print(f"{'Year':>5}  {'YDR_UN':>7} {'YDR_Δ':>7}  {'OADR_UN':>8} {'OADR_Δ':>8}  {'TDR_UN':>7} {'TDR_Δ':>7}")
    for i, y in enumerate(years):
        print(f"{y:>5}  {ydr_u[i]:>7.1f} {ydr_d[i]:>7.1f}  {oadr_u[i]:>8.1f} {oadr_d[i]:>8.1f}  {tdr_u[i]:>7.1f} {tdr_d[i]:>7.1f}")

    fig, (axO, axY, axT) = plt.subplots(1, 3, figsize=(16, 5.5), sharex=True)

    # Old-age dependency
    axO.plot(years, oadr_u, color="#1f3a5f", linewidth=2.0, linestyle="--", marker="s", markersize=5,
             label=f"UN-like (TFR≈{TFR_UN_LIKE} estable)")
    axO.plot(years, oadr_d, color="#7d2222", linewidth=2.5, marker="o", markersize=5,
             label="TFR → 1.0 by 2030")
    axO.set_title("OADR — Old-age (65+) / Working-age (15-64)", fontsize=11, loc="left")
    axO.set_ylabel("Old-age deps. per 100 (15-64)")
    axO.set_xlabel("Year")
    axO.grid(alpha=0.25); axO.legend(fontsize=9, loc="lower right")
    for i, y in enumerate(years):
        if y in (2023, 2035, 2050):
            axO.annotate(f"{oadr_u[i]:.0f}", xy=(y, oadr_u[i]), xytext=(0, 6),
                         textcoords="offset points", fontsize=8, ha="center", color="#1f3a5f")
            axO.annotate(f"{oadr_d[i]:.0f}", xy=(y, oadr_d[i]), xytext=(0, -14),
                         textcoords="offset points", fontsize=8, ha="center", color="#7d2222")

    # Youth dependency
    axY.plot(years, ydr_u, color="#1f3a5f", linewidth=2.0, linestyle="--", marker="s", markersize=5,
             label=f"UN-like (TFR≈{TFR_UN_LIKE} estable)")
    axY.plot(years, ydr_d, color="#7d2222", linewidth=2.5, marker="o", markersize=5,
             label="TFR → 1.0 by 2030")
    axY.set_title("YDR — Youth (0-14) / Working-age (15-64)", fontsize=11, loc="left")
    axY.set_ylabel("Youth deps. per 100 (15-64)")
    axY.set_xlabel("Year")
    axY.grid(alpha=0.25); axY.legend(fontsize=9, loc="upper right")
    for i, y in enumerate(years):
        if y in (2023, 2035, 2050):
            axY.annotate(f"{ydr_u[i]:.0f}", xy=(y, ydr_u[i]), xytext=(0, 6),
                         textcoords="offset points", fontsize=8, ha="center", color="#1f3a5f")
            axY.annotate(f"{ydr_d[i]:.0f}", xy=(y, ydr_d[i]), xytext=(0, -14),
                         textcoords="offset points", fontsize=8, ha="center", color="#7d2222")

    # Total dependency
    axT.plot(years, tdr_u, color="#1f3a5f", linewidth=2.0, linestyle="--", marker="s", markersize=5,
             label=f"UN-like (TFR≈{TFR_UN_LIKE} estable)")
    axT.plot(years, tdr_d, color="#7d2222", linewidth=2.5, marker="o", markersize=5,
             label="TFR → 1.0 by 2030")
    axT.set_title("TDR — Total dependency (youth + old) / Working-age", fontsize=11, loc="left")
    axT.set_ylabel("Total deps. per 100 (15-64)")
    axT.set_xlabel("Year")
    axT.grid(alpha=0.25); axT.legend(fontsize=9, loc="lower right")
    for i, y in enumerate(years):
        if y in (2023, 2035, 2050):
            axT.annotate(f"{tdr_u[i]:.0f}", xy=(y, tdr_u[i]), xytext=(0, 6),
                         textcoords="offset points", fontsize=8, ha="center", color="#1f3a5f")
            axT.annotate(f"{tdr_d[i]:.0f}", xy=(y, tdr_d[i]), xytext=(0, -14),
                         textcoords="offset points", fontsize=8, ha="center", color="#7d2222")

    fig.suptitle(
        "Mexico — dependency ratios 2023→2050\n"
        "UN-like baseline (TFR≈1.65 stable) vs. TFR-decline-to-1.0 stress scenario",
        fontsize=13)
    fig.text(0.5, 0.005,
             "Method: cohort-component, 5-yr age groups × 5-yr steps, period-averaged TFR; Mexico-shape ASFR (peak 25-29); "
             "Coale-Demeny West e_0≈75 fixed; zero migration. The 'UN-like' line approximates UN WPP 2024 medium "
             "with TFR=1.65 stable; the true UN path drifts 1.6→1.7 so this is an approximation.",
             ha="center", fontsize=8, color="#555", wrap=True)

    plt.tight_layout(rect=[0, 0.04, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    print(f"\nWrote {OUT_PNG}")


if __name__ == "__main__":
    main()

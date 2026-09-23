"""
Mexico demographic scenarios 2025 -> 2050, re-based on the Encuesta
Intercensal 2025 (INEGI, Reporte de Resultados 37/26, 2026-09-22).

STATUS: working product (2026-09-23), pending Anne's review. It does NOT
amend the endorsed 2026-Q2 / 2026-Q3 replicates, whose figures were computed
on the earlier skeleton (WPP-2023 base, fixed mortality, zero migration).
Differences against those figures are expected and are documented in the
companion mex_scenarios_eic2025.md.

What changed relative to the earlier scripts, and why
-----------------------------------------------------
1. Base year 2025 from the EIC itself. The national age-band shares of the
   EIC open-data tabulado (PCN_P_0A4 ... PCN_P_75YMAS, private dwellings,
   130.39 M) are scaled to the 130.91 M total. The open 75+ band is split
   into 5-year bands with the WPP-2023 within-75+ proportions (OWID). This
   follows the instructions' source hierarchy (census/intercensal > WPP)
   and is the Q4 "retabulate the current structure" item executed early.
2. Five TFR rows (DFD_TFR_forecast_instructions.md v1.5 plus the proposed
   fifth row of the 2026-09-22 EIC entry):
     Optimistic      UN WPP 2024 medium path (OWID series; 1.87 -> 1.70)
     Tempo-corrected 1.60 stable
     Central         1.50 stable            (DFD baseline)
     EIC-2025 direct 1.23 stable            (fifth row, PROPOSED; Hector to ratify)
     Stress          1.50 -> 0.90 by 2031 on the -0.10/yr glide (working floor)
   Central and Stress depart from 1.50 in 2025 as specified; whether they
   should depart from a reconciled 2025 level (1.23-1.4) is the "origin"
   question Anne transferred to the Q4 reconciliation (2026-09-23). Not
   resolved here.
3. Mortality improves. Five-year death probabilities fall 1.0 %/yr from the
   Coale-Demeny West e0~75 schedule used before. That is a conventional
   improvement rate; it lifts the schedule's crude e0 by a few years by 2050,
   in the direction of WPP's 75.1 -> 79.8.
4. Net emigration is on. EIC 2020-25: 1.3 M emigrants, 150.8 k returns,
   i.e. about -230 k/yr net, concentrated at ages 20-29 and 70 % male. The
   entry records this as a LOWER bound (fully-emigrated households are not
   captured). Held constant to 2050 with a fixed age profile. The model is
   single-sex, so the sex composition is not represented.
5. A sensitivity on the earlier skeleton (fixed mortality, zero migration)
   is printed to stdout so the new numbers can be reconciled with the
   endorsed replicates.

Method (unchanged skeleton)
---------------------------
Cohort-component, 21 five-year age bands, 5-year steps 2025 -> 2050.
TFR averaged across the five birth-years of each step. Mexico-shape ASFR
rescaled to the period TFR (shape fixed). Sex ratio at birth 1.05.
Single-sex model, female share 0.5.

Outputs (same folder)
---------------------
  mex_scenarios_eic2025_tfr.png          TFR paths + observed readings
  mex_scenarios_eic2025_population.png   total population, five rows + WPP
  mex_scenarios_eic2025_dependency.png   TDR / YDR / OADR, fiscal window
  mex_scenarios_eic2025_structure.png    age structure 2025 vs 2050
  mex_scenarios_eic2025_results.csv      all series, both assumption sets
"""

from __future__ import annotations

import csv
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
CORPUS = HERE.parent.parent
EIC_ZIP = CORPUS / "sources" / "INEGI_2026-09-22_EIC2025_datos-abiertos_105_localidad50k.zip"
EIC_CSV_IN_ZIP = "conjunto_de_datos/conjunto_datos_eic2025_105.csv"

OWID_5YR = "https://ourworldindata.org/grapher/population-by-five-year-age-group.csv?country=~MEX"
OWID_LONG = "https://ourworldindata.org/grapher/population-long-run-with-projections.csv?country=~MEX"
OWID_TFR = "https://ourworldindata.org/grapher/fertility-rate-with-projections.csv?country=~MEX"

YEARS = [2025, 2030, 2035, 2040, 2045, 2050]
N_AGES = 21
BAND_LABELS = [f"{5*i}-{5*i+4}" for i in range(20)] + ["100+"]

# EIC 2025 anchors (Reporte de Resultados 37/26; open-data tabulado 105)
EIC_TOTAL_POP = 130_911_314          # incl. 517,925 in collective dwellings
EIC_PRIVATE_POP = 130_393_389
EIC_TFR_2024 = 1.23                  # [1.22, 1.24]; published rounding 1.2
EIC_TDR_2025 = 46.40                 # private-dwelling base, 65+ cut
EIC_EMIGRANTS_2020_25 = 1_300_000
EIC_RETURNS_2020_25 = 150_800
NET_MIGRATION_PER_YEAR = -(EIC_EMIGRANTS_2020_25 - EIC_RETURNS_2020_25) / 5.0   # about -230 k

# Migration age profile (share of net flow by 5-year band; EIC: concentrated 20-29)
MIG_PROFILE = np.zeros(N_AGES)
MIG_PROFILE[3] = 0.10   # 15-19
MIG_PROFILE[4] = 0.30   # 20-24
MIG_PROFILE[5] = 0.30   # 25-29
MIG_PROFILE[6] = 0.15   # 30-34
MIG_PROFILE[7] = 0.10   # 35-39
MIG_PROFILE[8] = 0.05   # 40-44

# Coale-Demeny West e0~75, five-year survival probabilities (as in earlier scripts)
SURVIVAL_2025 = np.array([
    0.985, 0.997, 0.997, 0.995, 0.993, 0.992, 0.991, 0.989, 0.984, 0.978,
    0.969, 0.954, 0.929, 0.890, 0.832, 0.745, 0.620, 0.470, 0.300, 0.150,
    0.050,
])
MORTALITY_DECLINE_PER_YEAR = 0.010
BIRTH_TO_AGE_0_4 = 0.97
ASFR_SHAPE = np.array([0.045, 0.090, 0.110, 0.090, 0.060, 0.020, 0.005])
ASFR_FERTILE_START, ASFR_FERTILE_END = 3, 10
FEMALE_SHARE = 0.5

# Scenario colours: reference categorical order, fixed (validated, light surface)
SCENARIOS = [
    # key, label, colour
    ("optimistic", "Optimistic — UN WPP 2024 medium path (1.87→1.70)", "#2a78d6"),
    ("tempo",      "Tempo-corrected — TFR 1.60 stable",                "#eb6834"),
    ("central",    "Central — TFR 1.50 stable (DFD baseline)",         "#1baf7a"),
    ("eic",        "EIC-2025 direct — TFR 1.23 stable (proposed 5th row)", "#eda100"),
    ("stress",     "Stress — 1.50 → 0.90 by 2031 (working floor)",     "#e87ba4"),
]
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d3"


# --------------------------------------------------------------------------- data
def fetch_csv(url: str) -> pd.DataFrame:
    req = urllib.request.Request(url, headers={"User-Agent": "Dalila/1.0 (research)"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return pd.read_csv(io.BytesIO(resp.read()))


def eic_national_shares() -> np.ndarray:
    """16 shares: 0-4 ... 70-74, 75+ (percent of private-dwelling population)."""
    with zipfile.ZipFile(EIC_ZIP) as z, z.open(EIC_CSV_IN_ZIP) as f:
        reader = csv.DictReader(io.TextIOWrapper(f, encoding="latin-1"))
        for row in reader:
            if row["CVE_ENT"] == "00" and row["ESTIMADOR"].startswith("Valor"):
                keys = ["PCN_P_0A4", "PCN_P_5A9", "PCN_P_10A14", "PCN_P_15A19", "PCN_P_20A24",
                        "PCN_P_25A29", "PCN_P_30A34", "PCN_P_35A39", "PCN_P_40A44", "PCN_P_45A49",
                        "PCN_P_50A54", "PCN_P_55A59", "PCN_P_60A64", "PCN_P_65A69", "PCN_P_70A74",
                        "PCN_P_75YMAS"]
                return np.array([float(row[k]) for k in keys])
    raise RuntimeError("EIC national row not found")


def base_2025(owid5: pd.DataFrame) -> np.ndarray:
    shares = eic_national_shares() / 100.0
    shares = shares / shares.sum()                     # remove rounding residue
    pop16 = shares * EIC_TOTAL_POP
    row = owid5[(owid5["Code"] == "MEX") & (owid5["Year"] == 2023)].iloc[0]
    cols = [c for c in owid5.columns if c not in ("Entity", "Code", "Year")][:N_AGES]
    wpp = row[cols].to_numpy(dtype=float)
    within_75 = wpp[15:] / wpp[15:].sum()
    pop = np.concatenate([pop16[:15], pop16[15] * within_75])
    return pop


def wpp_tfr_path(tfr_df: pd.DataFrame) -> dict[int, float]:
    mex = tfr_df[tfr_df["Code"] == "MEX"]
    proj_col = next(c for c in mex.columns if "projection" in c.lower())
    est_col = next(c for c in mex.columns if "estimate" in c.lower())
    out = {}
    for _, r in mex.iterrows():
        v = r[proj_col] if pd.notna(r[proj_col]) else r[est_col]
        if pd.notna(v):
            out[int(r["Year"])] = float(v)
    return out


def wpp_population(long_df: pd.DataFrame) -> pd.DataFrame:
    mex = long_df[long_df["Code"] == "MEX"].copy()
    proj_col = next(c for c in mex.columns if "projection" in c.lower())
    mex["pop"] = mex["Population"].combine_first(mex[proj_col])
    return mex[(mex["Year"] >= 2020) & (mex["Year"] <= 2050)][["Year", "pop"]].reset_index(drop=True)


# ------------------------------------------------------------------- scenarios
def tfr_annual(key: str, wpp: dict[int, float]):
    def f(y: int) -> float:
        if key == "optimistic":
            return wpp.get(y, wpp[max(k for k in wpp if k <= y)])
        if key == "tempo":
            return 1.60
        if key == "central":
            return 1.50
        if key == "eic":
            return EIC_TFR_2024
        if key == "stress":
            glide = {2025: 1.50, 2026: 1.40, 2027: 1.30, 2028: 1.20, 2029: 1.10, 2030: 1.00}
            return glide.get(y, 0.90 if y >= 2031 else 1.50)
        raise KeyError(key)
    return f


def period_tfr(f, y0: int, y1: int) -> float:
    return float(np.mean([f(y) for y in range(y0 + 1, y1 + 1)]))


def survival_at(year: int, improve: bool) -> np.ndarray:
    if not improve:
        return SURVIVAL_2025
    factor = (1.0 - MORTALITY_DECLINE_PER_YEAR) ** (year - 2025)
    return 1.0 - (1.0 - SURVIVAL_2025) * factor


def project_step(pop: np.ndarray, tfr: float, surv: np.ndarray, net_mig_5yr: float) -> np.ndarray:
    asfr = ASFR_SHAPE * tfr / (5.0 * ASFR_SHAPE.sum())
    women = pop[ASFR_FERTILE_START:ASFR_FERTILE_END] * FEMALE_SHARE
    births = (asfr * women * 5.0).sum()
    new = np.zeros_like(pop)
    new[1:] = pop[:-1] * surv[:-1]
    new[-1] += pop[-1] * surv[-1]
    new[0] = births * BIRTH_TO_AGE_0_4
    new = new + net_mig_5yr * MIG_PROFILE          # migrants arrive/leave mid-step, no ageing
    return np.maximum(new, 0.0)


def project(pop0: np.ndarray, f, improve: bool, migrate: bool) -> np.ndarray:
    """Returns array [len(YEARS), N_AGES]."""
    out = [pop0.copy()]
    pop = pop0.copy()
    for y0, y1 in zip(YEARS[:-1], YEARS[1:]):
        surv = survival_at((y0 + y1) // 2, improve)
        mig = NET_MIGRATION_PER_YEAR * 5.0 if migrate else 0.0
        pop = project_step(pop, period_tfr(f, y0, y1), surv, mig)
        out.append(pop.copy())
    return np.array(out)


def ratios(struct: np.ndarray):
    youth = struct[:, :3].sum(axis=1)
    work = struct[:, 3:13].sum(axis=1)
    old = struct[:, 13:].sum(axis=1)
    return 100 * youth / work, 100 * old / work, 100 * (youth + old) / work


def crude_e0(surv: np.ndarray) -> float:
    l = np.concatenate([[1.0], np.cumprod(surv[:-1])])
    return float(5.0 * l.sum() - 2.5)


def window(years, tdr):
    i = int(np.argmin(tdr))
    in_win = [y for y, v in zip(years, tdr) if v <= tdr[i] + 2.0]
    # interpolated window on annual grid
    ys = np.arange(years[0], years[-1] + 1)
    vs = np.interp(ys, years, tdr)
    iw = ys[vs <= tdr[i] + 2.0]
    return years[i], tdr[i], (in_win[0], in_win[-1]), (int(iw[0]), int(iw[-1]))


# ------------------------------------------------------------------------ plots
def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def footer(fig, text, width=150):
    import textwrap
    fig.text(0.01, 0.005, "\n".join(textwrap.wrap(text, width)), fontsize=7.5, color=INK2, va="bottom")


def plot_tfr(wpp_tfr):
    fig, ax = plt.subplots(figsize=(10, 5.6))
    style(ax)
    yrs = np.arange(2025, 2051)
    for key, label, col in SCENARIOS:
        f = tfr_annual(key, wpp_tfr)
        v = [f(y) for y in yrs]
        ax.plot(yrs, v, color=col, linewidth=2, label=label)
        ax.text(2050.6, v[-1], f"{v[-1]:.2f}", color=INK, fontsize=9, va="center")
    # observed readings
    obs = [(2019, 1.90, "EIC method, 2019 (CPV 2020)", (8, 0), "left"),
           (2023, 1.60, "ENADID anchor, 2023", (-8, 10), "right"),
           (2024, 1.23, "EIC 2025 direct, 2024 [1.22–1.24]", (-8, -11), "right"),
           (2024, 1.46, "registry-implied, 2024 (Q3)", (-8, -4), "right"),
           (2025, 1.51, "F-V extrapolation, 2025", (-8, 10), "right")]
    for y, v, lab, (dx, dy), ha in obs:
        ax.plot(y, v, marker="o", markersize=7, color=INK, markerfacecolor="white", markeredgewidth=1.6, zorder=5)
        ax.annotate(lab, (y, v), xytext=(dx, dy), textcoords="offset points", fontsize=8, color=INK2, va="center", ha=ha,
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9), zorder=6)
    ax.axhline(2.1, color=INK2, linewidth=1, linestyle=":")
    ax.text(2019, 2.13, "replacement ≈ 2.1", fontsize=8, color=INK2)
    ax.set_xlim(2016.5, 2053)
    ax.set_ylim(0.7, 2.5)
    ax.set_ylabel("Total fertility rate (children per woman)", color=INK2, fontsize=9)
    ax.set_title("Mexico — TFR scenario paths, 2025–2050, against observed readings", loc="left", fontsize=12, color=INK)
    ax.legend(loc="upper right", fontsize=8, frameon=False)
    footer(fig, "Observed points are not on one instrument: EIC is a survey direct estimate (likely 0.1–0.2 low); registry-implied and F-V are "
                "reconstructions. Central and Stress depart from 1.50 in 2025 as specified in v1.5; the 2025 origin is a Q4 reconciliation item.")
    fig.tight_layout(rect=[0, 0.03, 1, 1])
    fig.savefig(HERE / "mex_scenarios_eic2025_tfr.png", dpi=140)
    plt.close(fig)


def plot_population(results, wpp_pop):
    fig, ax = plt.subplots(figsize=(10, 5.8))
    style(ax)
    ax.plot(wpp_pop["Year"], wpp_pop["pop"] / 1e6, color=INK2, linewidth=1.5, linestyle="--",
            label="UN WPP 2024 medium, total population (reference)")
    ax.text(2050.6, wpp_pop["pop"].iloc[-1] / 1e6, f"{wpp_pop['pop'].iloc[-1]/1e6:.1f}", color=INK2, fontsize=9, va="center")
    for key, label, col in SCENARIOS:
        tot = results[key]["pop"] / 1e6
        ax.plot(YEARS, tot, color=col, linewidth=2, marker="o", markersize=4, label=label)
        ax.text(2050.6, tot[-1], f"{tot[-1]:.1f}", color=INK, fontsize=9, va="center")
    ax.plot(2025, EIC_TOTAL_POP / 1e6, marker="o", markersize=8, color=INK, markerfacecolor="white", markeredgewidth=1.6)
    ax.annotate("EIC 2025 observed 130.9 M", (2025, EIC_TOTAL_POP / 1e6), xytext=(8, -12), textcoords="offset points", fontsize=8, color=INK2)
    ax.set_xlim(2019.5, 2053.5)
    ax.set_ylabel("Population (millions)", color=INK2, fontsize=9)
    ax.set_title("Mexico — total population 2025–2050 by scenario, re-based on EIC 2025", loc="left", fontsize=12, color=INK)
    ax.legend(loc="lower left", fontsize=8, frameon=False)
    footer(fig, "Scenarios: EIC 2025 age structure (130.91 M) × cohort-component 5-yr steps; mortality improving 1 %/yr from CD-West e0≈75; "
                "net migration −230 k/yr (EIC 2020–25, lower bound), ages 15–44. WPP line is the UN series itself, not re-run.")
    fig.tight_layout(rect=[0, 0.03, 1, 1])
    fig.savefig(HERE / "mex_scenarios_eic2025_population.png", dpi=140)
    plt.close(fig)


def plot_dependency(results):
    fig, axes = plt.subplots(1, 3, figsize=(14, 5.2), sharex=True)
    titles = ["Total dependency ratio (0–14 + 65+) / 15–64", "Youth dependency (0–14) / 15–64", "Old-age dependency (65+) / 15–64"]
    keys = ["tdr", "ydr", "oadr"]
    for ax, t, k in zip(axes, titles, keys):
        style(ax)
        for skey, label, col in SCENARIOS:
            v = results[skey][k]
            ax.plot(YEARS, v, color=col, linewidth=2, marker="o", markersize=4, label=label)
            ax.text(2050.6, v[-1], f"{v[-1]:.1f}", color=INK, fontsize=8, va="center")
            if k == "tdr":
                i = int(np.argmin(v))
                ax.plot(YEARS[i], v[i], marker="v", markersize=7, color=col, markeredgecolor="white", markeredgewidth=1)
        ax.set_title(t, loc="left", fontsize=10, color=INK)
        ax.set_xlim(2023.5, 2053.5)
    axes[0].plot(2025, EIC_TDR_2025, marker="o", markersize=8, color=INK, markerfacecolor="white", markeredgewidth=1.6)
    axes[0].annotate("EIC 2025 observed 46.4", (2025, EIC_TDR_2025), xytext=(8, 8), textcoords="offset points", fontsize=8, color=INK2)
    axes[0].plot(2026, 49.3, marker="s", markersize=7, color=INK2, markerfacecolor="white", markeredgewidth=1.4)
    axes[0].annotate("Q3 CONAPO-share implied ≈49.3 (2026)", (2026, 49.3), xytext=(8, 4), textcoords="offset points", fontsize=8, color=INK2)
    axes[0].set_ylabel("per 100 aged 15–64", color=INK2, fontsize=9)
    axes[0].legend(loc="upper left", fontsize=7.5, frameon=False)
    fig.suptitle("Mexico — dependency ratios 2025–2050 by scenario (▼ = TDR minimum, the fiscal window)", x=0.01, ha="left", fontsize=12, color=INK)
    footer(fig, "Same assumptions as the population chart. The EIC point sits on the WPP side of the Q3 §4 wedge (46–47 vs 49.3). "
                "Stress ends with the lowest TDR but the highest OADR: the favourable-looking total is arithmetic, not relief.")
    fig.tight_layout(rect=[0, 0.04, 1, 0.94])
    fig.savefig(HERE / "mex_scenarios_eic2025_dependency.png", dpi=140)
    plt.close(fig)


def plot_structure(results, pop0):
    fig, ax = plt.subplots(figsize=(9, 6.5))
    style(ax)
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.grid(axis="y", visible=False)
    y = np.arange(N_AGES)
    ax.barh(y, pop0 / 1e6, height=0.8, color=GRID, label="2025 observed (EIC)")
    ref = results["central"]["struct"][-1] / 1e6
    ax.step(np.append(ref[5:], ref[-1]), np.append(y[5:] - 0.5, y[-1] + 0.5), where="post",
            color=INK2, linewidth=1.8, label="2050, ages 25+ — identical in every scenario (cohorts already born)")
    for key, label, col in SCENARIOS:
        if key not in ("central", "eic", "stress"):
            continue
        v = results[key]["struct"][-1] / 1e6
        ax.step(np.append(v[:6], v[5]), np.append(y[:6] - 0.5, y[5] - 0.5), where="post", color=col, linewidth=2.2,
                label=f"2050, ages 0–24 — {label.split(' — ')[0]}")
    ax.set_yticks(y)
    ax.set_yticklabels(BAND_LABELS, fontsize=8)
    ax.set_xlabel("Population in age band (millions)", color=INK2, fontsize=9)
    ax.set_title("Mexico — age structure, 2025 observed vs 2050 under three scenarios", loc="left", fontsize=12, color=INK)
    ax.legend(loc="upper right", fontsize=8, frameon=False)
    footer(fig, "Single-sex model; bands 0–4 … 100+. The 2025 bars are the EIC tabulado shares on 130.91 M, 75+ split with WPP-2023 proportions.")
    fig.tight_layout(rect=[0, 0.03, 1, 1])
    fig.savefig(HERE / "mex_scenarios_eic2025_structure.png", dpi=140)
    plt.close(fig)


# ------------------------------------------------------------------------- main
def run_all(pop0, wpp_tfr, improve, migrate):
    res = {}
    for key, _, _ in SCENARIOS:
        struct = project(pop0, tfr_annual(key, wpp_tfr), improve, migrate)
        ydr, oadr, tdr = ratios(struct)
        res[key] = {"struct": struct, "pop": struct.sum(axis=1), "ydr": ydr, "oadr": oadr, "tdr": tdr}
    return res


def main():
    owid5 = fetch_csv(OWID_5YR)
    tfr_df = fetch_csv(OWID_TFR)
    long_df = fetch_csv(OWID_LONG)
    pop0 = base_2025(owid5)
    wpp_tfr = wpp_tfr_path(tfr_df)
    wpp_pop = wpp_population(long_df)

    ydr0, oadr0, tdr0 = ratios(pop0[None, :])
    print(f"Base 2025 (EIC shares on {EIC_TOTAL_POP/1e6:.2f} M): TDR {tdr0[0]:.2f}  YDR {ydr0[0]:.2f}  OADR {oadr0[0]:.2f}  "
          f"(EIC tabulado TDR {EIC_TDR_2025})")
    print(f"Crude e0 of survival schedule: 2025 {crude_e0(survival_at(2025, True)):.1f}  2050 {crude_e0(survival_at(2050, True)):.1f}")
    print(f"Net migration assumption: {NET_MIGRATION_PER_YEAR/1e3:.0f} k/yr")
    print("WPP 2024 medium TFR path used for Optimistic:", {y: round(wpp_tfr[y], 3) for y in (2025, 2030, 2040, 2050)})

    main_res = run_all(pop0, wpp_tfr, improve=True, migrate=False if "--no-migration" in sys.argv else True)
    old_res = run_all(pop0, wpp_tfr, improve=False, migrate=False)

    rows = []
    for tag, res in (("eic2025_improving_mortality_net_migration", main_res), ("sensitivity_fixed_mortality_zero_migration", old_res)):
        print(f"\n== {tag} ==")
        print(f"{'scenario':<12}{'pop2050 M':>11}{'TDRmin':>8}{'yr':>6}{'grid window':>14}{'interp window':>16}{'TDR2050':>9}{'OADR2050':>10}")
        for key, label, _ in SCENARIOS:
            r = res[key]
            ymin, vmin, gw, iw = window(YEARS, r["tdr"])
            print(f"{key:<12}{r['pop'][-1]/1e6:>11.2f}{vmin:>8.1f}{ymin:>6}{f'{gw[0]}–{gw[1]}':>14}{f'{iw[0]}–{iw[1]}':>16}{r['tdr'][-1]:>9.1f}{r['oadr'][-1]:>10.1f}")
            for i, y in enumerate(YEARS):
                rows.append({"assumptions": tag, "scenario": key, "year": y, "population": round(r["pop"][i]),
                             "ydr": round(r["ydr"][i], 2), "oadr": round(r["oadr"][i], 2), "tdr": round(r["tdr"][i], 2)})
    pd.DataFrame(rows).to_csv(HERE / "mex_scenarios_eic2025_results.csv", index=False)
    print(f"\nWPP 2024 medium total population 2050: {wpp_pop['pop'].iloc[-1]/1e6:.2f} M")

    plot_tfr(wpp_tfr)
    plot_population(main_res, wpp_pop)
    plot_dependency(main_res)
    plot_structure(main_res, pop0)
    print("Wrote 4 PNG + results CSV to", HERE)


if __name__ == "__main__":
    main()

"""
CAF_DEM — Proyecciones poblacionales 2023→2050 bajo dos escenarios de TFR.

Para cada uno de los 5 países CAF_DEM no-mexicanos (CRI, PAN, COL, BRA, CHL):
- Línea base: UN WPP 2024 medium variant (publicada).
- Contrafáctico: TFR observada reciente, mantenida estable hasta 2050.

Mexico no está incluido aquí — ver _crossrefs/corpus/demographics/country/MEX/
para el ejercicio análogo de México (artefacto de práctica, no CAF IP).

Insumos:
- Pirámides 2023 por grupo quinquenal de edad: OWID (population-by-five-year-age-group),
  derivada de UN WPP 2024.
- TFR observada por país (anchors de scenario_anchors.md cuando disponibles):
    CRI 1.12 — INEC Costa Rica, Indicadores demográficos 2024 (nov 2025)
    PAN 1.80 — INEC Panamá / Contraloría, Estadísticas Vitales 2023 (ene 2025)
    COL 1.10 — DANE, EEVV Nacimientos 2024pr (mar 2025)
    BRA 1.50 — IBGE estimación 2023 (no source-pinned por Anne; revisar)
    CHL 1.03 — INE Chile, Estadísticas Vitales Provisional 2024 (may 2025)
- Línea base UN WPP: OWID (population-long-run-with-projections).

Método (idéntico al ejercicio MEX salvo país):
- Cohorte-componente, grupos quinquenales × pasos de 5 años (2023→2048),
  interpolación lineal a 2050.
- Distribución ASFR: forma latinoamericana típica con pico en 25-29,
  reescalada para que 5×sum(ASFR) = TFR objetivo.
- Mortalidad: Coale-Demeny "West" e_0 ≈ 75 fija para todos los países y todos
  los años (simplificación; las e_0 reales varían CHL 81 > CRI 80 > PAN 78 >
  COL 77 > BRA 76; el sesgo agregado en población total a 2050 es del orden
  de ±2-3%).
- Migración: cero (simplificación; UN supone flujos netos negativos en
  varios de estos países, sobre todo MEX y CRI).
- Razón de sexos al nacer: 1.05 (49% niñas).

Salidas (mismas carpetas):
- proj_TFR_stable_5countries.png — panel 2×3 (5 países + tabla).
- proj_TFR_stable_5countries_summary.csv — tabla a 2050.

Ejecutar desde el env dalila:
    ~/miniforge3/envs/dalila/bin/python proj_TFR_stable_5countries.py

CONFIDENCIAL — IP CAF (Anexo A del contrato CW29884).
"""

import io
from pathlib import Path
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
OUT_PNG = HERE / "proj_TFR_stable_5countries.png"
OUT_CSV = HERE / "proj_TFR_stable_5countries_summary.csv"

OWID_5YR = "https://ourworldindata.org/grapher/population-by-five-year-age-group.csv"
OWID_LONG = "https://ourworldindata.org/grapher/population-long-run-with-projections.csv"

AGE_LABELS = [
    "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34",
    "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69",
    "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100+",
]
N_AGES = len(AGE_LABELS)

# Stylized 5-year cohort survival ratios (Coale-Demeny "West" at e_0 ≈ 75).
SURVIVAL = np.array([
    0.985, 0.997, 0.997, 0.995, 0.993, 0.992, 0.991, 0.989, 0.984, 0.978,
    0.969, 0.954, 0.929, 0.890, 0.832, 0.745, 0.620, 0.470, 0.300, 0.150,
    0.050,
])
BIRTH_TO_AGE_0_4 = 0.97

# Latin America-typical ASFR shape (per woman per year by 5-yr age group,
# 15-19 ... 45-49). Will be rescaled per country to match its target TFR.
ASFR_SHAPE = np.array([0.045, 0.090, 0.110, 0.090, 0.060, 0.020, 0.005])
ASFR_FERTILE_START = 3
ASFR_FERTILE_END = 10

FEMALE_SHARE = 0.5

# Five non-Mexico CAF_DEM countries with their realistic observed TFRs.
COUNTRIES = [
    {
        "iso3": "CRI", "name": "Costa Rica",
        "tfr_obs": 1.12, "tfr_obs_year": 2024,
        "tfr_src": "INEC Costa Rica · Indicadores demográficos 2024 (nov 2025)",
    },
    {
        "iso3": "PAN", "name": "Panamá",
        "tfr_obs": 1.80, "tfr_obs_year": 2023,
        "tfr_src": "INEC Panamá / Contraloría · Estadísticas Vitales 2023 (ene 2025)",
    },
    {
        "iso3": "COL", "name": "Colombia",
        "tfr_obs": 1.10, "tfr_obs_year": 2024,
        "tfr_src": "DANE · Boletín EEVV Nacimientos 2024pr (mar 2025)",
    },
    {
        "iso3": "BRA", "name": "Brasil",
        "tfr_obs": 1.50, "tfr_obs_year": 2023,
        "tfr_src": "IBGE estimación 2023 (pendiente source-pin Anne)",
    },
    {
        "iso3": "CHL", "name": "Chile",
        "tfr_obs": 1.03, "tfr_obs_year": 2024,
        "tfr_src": "INE Chile · Boletín Estadísticas Vitales Provisional 2024 (may 2025)",
    },
]


def fetch_owid_csv(url: str) -> pd.DataFrame:
    print(f"Fetching {url} ...")
    with urllib.request.urlopen(url, timeout=60) as resp:
        return pd.read_csv(io.BytesIO(resp.read()))


def baseline_2023(df_5yr: pd.DataFrame, iso3: str) -> np.ndarray:
    rows = df_5yr[(df_5yr["Code"] == iso3) & (df_5yr["Year"] == 2023)]
    if rows.empty:
        raise ValueError(f"No 2023 row for {iso3}")
    age_cols = [c for c in df_5yr.columns if c not in ("Entity", "Code", "Year")][:N_AGES]
    pop = rows.iloc[0][age_cols].to_numpy(dtype=float)
    assert len(pop) == N_AGES
    return pop


def project_step(pop: np.ndarray, tfr: float) -> np.ndarray:
    asfr = ASFR_SHAPE * tfr / (5.0 * ASFR_SHAPE.sum())
    women = pop[ASFR_FERTILE_START:ASFR_FERTILE_END] * FEMALE_SHARE
    births = (asfr * women * 5.0).sum()

    new_pop = np.zeros_like(pop)
    new_pop[1:N_AGES] = pop[: N_AGES - 1] * SURVIVAL[: N_AGES - 1]
    new_pop[N_AGES - 1] += pop[N_AGES - 1] * SURVIVAL[N_AGES - 1]
    new_pop[0] = births * BIRTH_TO_AGE_0_4
    return new_pop


def project_trajectory(pop_2023: np.ndarray, tfr: float) -> tuple[list[int], np.ndarray]:
    years = [2023, 2028, 2033, 2038, 2043, 2048, 2050]
    totals = [pop_2023.sum()]
    pop = pop_2023.copy()
    for i in range(1, len(years)):
        step_yrs = years[i] - years[i - 1]
        if step_yrs == 5:
            pop = project_step(pop, tfr)
        else:
            pop_5 = project_step(pop, tfr)
            pop = pop + (step_yrs / 5.0) * (pop_5 - pop)
        totals.append(pop.sum())
    return years, np.array(totals)


def un_medium_trajectory(df_long: pd.DataFrame, iso3: str) -> pd.DataFrame:
    rows = df_long[df_long["Code"] == iso3].copy()
    proj_col = next(c for c in rows.columns if "projection" in c.lower())
    rows["pop"] = rows["Population"].combine_first(rows[proj_col])
    rows = rows[(rows["Year"] >= 2023) & (rows["Year"] <= 2050)][["Year", "pop"]]
    return rows.sort_values("Year").reset_index(drop=True)


def main():
    df_5yr = fetch_owid_csv(OWID_5YR)
    df_long = fetch_owid_csv(OWID_LONG)

    rows_summary = []

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    axes = axes.flatten()

    for i, c in enumerate(COUNTRIES):
        ax = axes[i]
        iso3, name = c["iso3"], c["name"]
        tfr_obs, tfr_year, tfr_src = c["tfr_obs"], c["tfr_obs_year"], c["tfr_src"]

        pop_2023 = baseline_2023(df_5yr, iso3)
        pop_2023_m = pop_2023.sum() / 1e6

        years_cf, totals_cf = project_trajectory(pop_2023, tfr_obs)
        totals_cf_m = totals_cf / 1e6

        un = un_medium_trajectory(df_long, iso3)
        un_m = un["pop"].to_numpy() / 1e6

        cf_2050 = totals_cf_m[-1]
        un_2050 = un_m[-1]
        gap_m = un_2050 - cf_2050
        gap_pct = gap_m / un_2050 * 100

        rows_summary.append({
            "iso3": iso3, "name": name,
            "tfr_obs": tfr_obs, "tfr_year": tfr_year, "tfr_src": tfr_src,
            "pop_2023_M": round(pop_2023_m, 2),
            "pop_2050_UN_medium_M": round(un_2050, 2),
            "pop_2050_TFR_obs_stable_M": round(cf_2050, 2),
            "gap_M": round(gap_m, 2),
            "gap_pct": round(gap_pct, 1),
        })

        ax.plot(un["Year"], un_m, color="#1f3a5f", linewidth=1.8, linestyle="--",
                label="UN WPP 2024 medium")
        ax.plot(years_cf, totals_cf_m, color="#a83232", linewidth=2.2, marker="o", markersize=4,
                label=f"TFR={tfr_obs} estable")

        ax.set_title(f"{name} ({iso3})  ·  TFR_obs={tfr_obs} ({tfr_year})",
                     fontsize=11, loc="left")
        ax.set_xlabel("Año", fontsize=9)
        ax.set_ylabel("Población (millones)", fontsize=9)
        ax.tick_params(labelsize=8)
        ax.set_xlim(2023, 2052)

        ymin = min(min(totals_cf_m), min(un_m))
        ymax = max(max(totals_cf_m), max(un_m))
        ax.set_ylim(ymin * 0.94, ymax * 1.06)

        ax.annotate(f"{un_2050:.1f}", xy=(2050, un_2050), xytext=(4, 0),
                    textcoords="offset points", ha="left", va="center",
                    fontsize=8, color="#1f3a5f")
        ax.annotate(f"{cf_2050:.1f}", xy=(2050, cf_2050), xytext=(4, 0),
                    textcoords="offset points", ha="left", va="center",
                    fontsize=8, color="#a83232")
        ax.grid(alpha=0.25)
        ax.legend(loc="best", fontsize=8, framealpha=0.95)

    # Sixth panel: summary table
    ax_tbl = axes[5]
    ax_tbl.axis("off")
    df_summary = pd.DataFrame(rows_summary)
    table_data = [["País", "TFR obs", "2023 (M)", "2050 UN (M)", f"2050 TFR_obs (M)", "Δ (M)", "Δ (%)"]]
    for r in rows_summary:
        table_data.append([
            f"{r['name']}",
            f"{r['tfr_obs']:.2f}",
            f"{r['pop_2023_M']:.1f}",
            f"{r['pop_2050_UN_medium_M']:.1f}",
            f"{r['pop_2050_TFR_obs_stable_M']:.1f}",
            f"{-r['gap_M']:+.1f}",
            f"{-r['gap_pct']:+.1f}",
        ])
    tbl = ax_tbl.table(cellText=table_data[1:], colLabels=table_data[0],
                      loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1.05, 1.5)

    fig.suptitle(
        "CAF_DEM · Proyecciones poblacionales 2023→2050 — 5 países\n"
        "Línea base UN WPP 2024 medium variant vs. contrafáctico con TFR observada estable",
        fontsize=13)
    fig.text(
        0.5, 0.005,
        "Método: cohorte-componente, grupos quinquenales × 5 años; ASFR latinoamericana (pico 25-29) reescalada al TFR objetivo; "
        "mortalidad Coale-Demeny West e_0≈75 fija; migración nula. Anchors TFR: Anne (scenario_anchors.md). "
        "BRA TFR=1.50 estimación IBGE 2023, pendiente confirmación. CONFIDENCIAL — IP CAF (CW29884).",
        ha="center", fontsize=8, color="#555", wrap=True)

    plt.tight_layout(rect=[0, 0.04, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    print(f"\nWrote {OUT_PNG}")

    df_summary.to_csv(OUT_CSV, index=False)
    print(f"Wrote {OUT_CSV}")

    print("\n=== Resumen 2050 ===")
    for r in rows_summary:
        print(f"  {r['name']:12s} (TFR={r['tfr_obs']:.2f}): "
              f"UN={r['pop_2050_UN_medium_M']:6.1f}M  "
              f"TFR_obs={r['pop_2050_TFR_obs_stable_M']:6.1f}M  "
              f"gap={r['gap_M']:+.1f}M ({r['gap_pct']:+.1f}%)")


if __name__ == "__main__":
    main()

"""
Step 0 of the EIC-2025 nota build: extract the national Mexico inputs from the
raw downloads in ../data/raw/ into small, committed CSVs in ../data/.

Build instruction: _crossrefs/_build_instructions/2026-09-23_DFD_nota-EIC2025_build-instruction.md

Raw files (not committed; provenance and sha256 in ../data/README.md):
  CONAPO_2023_ConDem50a19_ProyPob20a70.zip            CONAPO conciliación 1950-2019 + proyecciones 2020-2070
  WPP2024_Demographic_Indicators_Medium.csv.gz        UN WPP 2024 medium, indicators
  WPP2024_PopulationBySingleAgeSex_Medium_1950-2023.csv.gz
  WPP2024_Demographic_Indicators_OtherVariants.csv.gz  (low-variant TFR only)
  cpv2020_b_eum_01_poblacion.xlsx                     CPV 2020 tabulado 01-02 (total pop by sex, 5-yr age)
  cpv2020_b_eum_13_hogares_censales.xlsx              CPV 2020 tabulado 13-08 (household pop by sex, 5-yr age)
  cpv2020_b_eum_16_vivienda.xlsx                      CPV 2020 tabulado 16-02 (occupants by dwelling type)
  enoe_2026_trim2_csv.zip                             INEGI ENOE 2026-Q2 microdata (sociodemographic table)
Corpus source (committed): _crossrefs/corpus/demographics/sources/INEGI_2026-09-22_EIC2025_datos-abiertos_105_localidad50k.zip
"""

from __future__ import annotations

import csv
import io
import zipfile
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
RAW = DATA / "raw"
DALILA = HERE.parents[5]
EIC_ZIP = DALILA / "_crossrefs/corpus/demographics/sources/INEGI_2026-09-22_EIC2025_datos-abiertos_105_localidad50k.zip"

YEARS = range(2020, 2051)
BANDS_EIC = ["0A4", "5A9", "10A14", "15A19", "20A24", "25A29", "30A34", "35A39", "40A44", "45A49",
             "50A54", "55A59", "60A64", "65A69", "70A74", "75YMAS"]
SEX = {"Hombres": "M", "Mujeres": "F"}


def conapo():
    z = zipfile.ZipFile(RAW / "CONAPO_2023_ConDem50a19_ProyPob20a70.zip")
    d = "ConDem50a19_ProyPob20a70/"

    def sheet(name):
        with z.open(d + name) as f:
            return pd.read_excel(io.BytesIO(f.read()))

    pop = sheet("0_Pob_Mitad_1950_2070.xlsx")
    pop = pop[(pop.CVE_GEO == 0) & pop.AÑO.isin(YEARS)]
    pop = pop.assign(sex=pop.SEXO.map(SEX)).rename(columns={"AÑO": "year", "EDAD": "age", "POBLACION": "pop"})
    pop[["year", "age", "sex", "pop"]].to_csv(DATA / "conapo2023_mex_pop_midyear.csv", index=False)

    dth = sheet("1_Defunciones_1950_2070.xlsx")
    dth = dth[(dth.CVE_GEO == 0) & dth.AÑO.isin(YEARS)]
    dth = dth.assign(sex=dth.SEXO.map(SEX)).rename(columns={"AÑO": "year", "EDAD": "age", "DEFUNCIONES": "deaths"})
    dth[["year", "age", "sex", "deaths"]].to_csv(DATA / "conapo2023_mex_deaths.csv", index=False)

    asfr = sheet("4_Tasas_Especificas_Fecundidad_proyecciones.xlsx")
    asfr = asfr[(asfr.CVE_GEO == 0) & asfr.AÑO.isin(YEARS)]
    asfr = asfr.rename(columns={"AÑO": "year", "GPO_EDAD": "age_group", "TASAS": "asfr_per_1000", "NACIMIENTOS": "births"})
    asfr[["year", "age_group", "asfr_per_1000", "births"]].to_csv(DATA / "conapo2023_mex_asfr.csv", index=False)

    ind = sheet("5_Indicadores_demográficos_proyecciones.xlsx")
    ind = ind[(ind.CVE_GEO == 0) & ind.AÑO.isin(YEARS)]
    cols = ["AÑO", "POB_MIT_AÑO", "POB_65_MAS", "NAC", "DEF", "MIG_NET_INT", "TGF", "EV", "EVH", "EVM", "RAZ_DEP"]
    ind[cols].rename(columns={"AÑO": "year"}).to_csv(DATA / "conapo2023_mex_indicators.csv", index=False)


def eic():
    with zipfile.ZipFile(EIC_ZIP) as z, z.open("conjunto_de_datos/conjunto_datos_eic2025_105.csv") as f:
        for row in csv.DictReader(io.TextIOWrapper(f, encoding="latin-1")):
            if row["CVE_ENT"] == "00" and row["ESTIMADOR"].startswith("Valor"):
                break
        else:
            raise RuntimeError("EIC national row not found")
    rows = []
    for sex, tot in (("F", float(row["POBFEM"])), ("M", float(row["POBMAS"]))):
        pct = [float(row[f"PCN_P_{b}_{sex}"]) for b in BANDS_EIC]
        s = sum(pct)
        for b, p in zip(BANDS_EIC, pct):
            rows.append({"band": b, "sex": sex, "pct_of_total_published": p, "count": tot * p / s})
    out = pd.DataFrame(rows)
    out.to_csv(DATA / "eic2025_mex_private_by_band_sex.csv", index=False)
    meta = {k: row[k] for k in ("POBTOT", "POBFEM", "POBMAS", "P_6A14", "POB0_14", "POB15_64", "POB65_MAS",
                                "RAZON_DEP_TOT", "TGF", "MEDIANA_POBTOT")}
    pd.Series(meta).to_csv(DATA / "eic2025_mex_national_indicators.csv", header=["value"])
    print("EIC private pop by sex:", row["POBFEM"], row["POBMAS"], "band pct sums:",
          out.groupby("sex").pct_of_total_published.sum().round(2).to_dict())


def cpv_collective():
    """Collective-dwelling (non-household) population by sex and 5-yr band, CPV 2020:
    total population (tab. 01-02) minus population in hogares censales (tab. 13-08).
    The residual (499,185) = collective-dwelling occupants (490,995, tab. 16-02) plus
    8,190 people without dwelling; its age-sex shares stand in for the collective shares."""
    def table(path, sheet, valcol):
        t = pd.read_excel(path, sheet_name=sheet, header=None)
        t = t[t[0] == "Estados Unidos Mexicanos"].iloc[:, [1, 2, valcol]]
        t.columns = ["sex", "band", "value"]
        return t[t.sex.isin(["Hombres", "Mujeres"]) & (t.band != "Total")].set_index(["sex", "band"]).value.astype(float)

    tot = table(RAW / "cpv2020_b_eum_01_poblacion.xlsx", "02", 3)
    hog = table(RAW / "cpv2020_b_eum_13_hogares_censales.xlsx", "08", 3)
    # total table runs to 100+; collapse to 85+ to match the household table
    tot = tot.reset_index()
    old = ["85-89 años", "90-94 años", "95-99 años", "100 años y más"]
    tot["band"] = tot.band.where(~tot.band.isin(old), "85 años y más")
    tot = tot.groupby(["sex", "band"]).value.sum()
    res = (tot - hog).dropna().reset_index()
    res = res[res.band != "No especificado"]
    res["sex"] = res.sex.map(SEX)
    res["share_within_residual"] = res.value / res.value.sum()
    res.rename(columns={"value": "residual_count"}).to_csv(DATA / "cpv2020_mex_nonhousehold_by_band_sex.csv", index=False)
    print("CPV 2020 non-household residual:", int(res.value.sum()), "(collective occupants 490,995 per tab. 16-02)")


def wpp():
    ind = pd.read_csv(RAW / "WPP2024_Demographic_Indicators_Medium.csv.gz", low_memory=False)
    ind = ind[(ind.LocID == 484) & ind.Time.between(2000, 2050)]
    ind[["Time", "TPopulation1July", "TFR", "SRB", "NetMigrations", "LEx"]].rename(columns={"Time": "year"}) \
        .to_csv(DATA / "wpp2024_mex_indicators_medium.csv", index=False)
    pop = pd.read_csv(RAW / "WPP2024_PopulationBySingleAgeSex_Medium_1950-2023.csv.gz", low_memory=False)
    pop = pop[(pop.LocID == 484) & (pop.Time == 2023)]
    pop[["Time", "AgeGrpStart", "PopMale", "PopFemale"]].rename(columns={"Time": "year", "AgeGrpStart": "age"}) \
        .to_csv(DATA / "wpp2024_mex_pop_single_age_2023.csv", index=False)
    var = pd.read_csv(RAW / "WPP2024_Demographic_Indicators_OtherVariants.csv.gz", low_memory=False,
                      usecols=["LocID", "Variant", "Time", "TFR"])
    var = var[(var.LocID == 484) & (var.Variant == "Low") & var.Time.between(2024, 2050)]
    var[["Time", "TFR"]].rename(columns={"Time": "year", "TFR": "TFR_low"}) \
        .to_csv(DATA / "wpp2024_mex_tfr_low_variant.csv", index=False)


def enoe():
    """Employment-to-population ratio at 15-64, ENOE 2026-Q2 (latest published quarter).
    INEGI's standard filter for the SDEM table: completed interview (r_def == 0), usual
    residents (c_res in 1, 3); clase2 == 1 is 'población ocupada'; weights fac_tri."""
    with zipfile.ZipFile(RAW / "enoe_2026_trim2_csv.zip") as z, z.open("ENOE_SDEMT226.csv") as f:
        d = pd.read_csv(f, encoding="latin-1", usecols=["r_def", "c_res", "eda", "fac_tri", "clase2"], dtype=str)
    d = d.apply(lambda c: pd.to_numeric(c.str.strip(), errors="coerce"))
    d = d[(d.r_def == 0) & d.c_res.isin([1, 3])]
    w = d.fac_tri.astype(float)
    wa = d.eda.between(15, 64)
    out = {
        "quarter": "2026-Q2",
        "pop_15_64": w[wa].sum(),
        "employed_15_64": w[wa & (d.clase2 == 1)].sum(),
        "pop_15plus": w[d.eda.between(15, 98)].sum(),
        "employed_15plus": w[d.eda.between(15, 98) & (d.clase2 == 1)].sum(),
    }
    out["e_15_64"] = out["employed_15_64"] / out["pop_15_64"]
    pd.Series(out).to_csv(DATA / "enoe2026q2_employment_rate.csv", header=["value"])
    print("ENOE 2026-Q2: e(15-64) =", round(out["e_15_64"], 4), "| employed 15+ =", round(out["employed_15plus"] / 1e6, 2), "M")


if __name__ == "__main__":
    eic()
    cpv_collective()
    wpp()
    conapo()
    enoe()
    print("Wrote inputs to", DATA)

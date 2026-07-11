#!/usr/bin/env python3
"""
Stage 1 — National-source series (the collapse tail invisible in World Bank/WPP).
Values transcribed from named national statistical-office documents (DANE, INE-CL,
DEIS/INDEC, INEC-CR, INEGI/CONAPO) retrieved June 2026. Every value's source URL is
in STAGE1_provenance.md. Nothing here is estimated or interpolated; gaps are left as
gaps. Builds tidy long CSVs under data/national/ with columns:
year, value, source, methodology_flag, provisional_flag.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "national"); os.makedirs(OUT, exist_ok=True)

def write(iso, series, rows, src, default_method="", prov_years=()):
    """rows: list of (year, value, method_flag_override_or_None, prov_override_or_None)"""
    path = os.path.join(OUT, f"{iso}_{series}.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "value", "source", "methodology_flag", "provisional_flag"])
        for r in rows:
            yr, val = r[0], r[1]
            mflag = r[2] if len(r) > 2 and r[2] is not None else default_method
            pflag = r[3] if len(r) > 3 and r[3] is not None else ("provisional" if yr in prov_years else "definitive")
            w.writerow([yr, val, src, mflag, pflag])
    print(f"  {os.path.basename(path):34s} n={len(rows)}")

# ----------------------------------------------------------------- COLOMBIA
print("COLOMBIA (DANE)")
# TFR: DANE EEVV Boletín Isem-2025pr (25-sep-2025), Gráfico 7. Chart labels, 1 decimal.
write("COL", "tfr_national",
      [(2015,1.7),(2016,1.7),(2017,1.7),(2018,1.7),(2019,1.6),(2020,1.5),
       (2021,1.5),(2022,1.4),(2023,1.2),(2024,1.1)],
      "DANE EEVV Boletin Isem-2025pr (25-sep-2025), Grafico 7 [bol-EEVV-Isem2025pr.pdf]",
      default_method="chart-label, rounded 1 decimal; crude (not age-standardized); denom=CNPV2018 conciliated projections",
      prov_years=())  # DANE marks 2016-2024 definitivas
# Births: DANE EEVV Boletín IIsem-2025pr (20-mar-2026)
write("COL", "births_national",
      [(2016,647521),(2017,656704),(2018,649115),(2019,642660),(2020,629402),
       (2021,616914),(2022,573625),(2023,515549),(2024,453901),(2025,433678)],
      "DANE EEVV Boletin IIsem-2025pr (20-mar-2026), Grafico 1/2 [bol-EEVV-IIsem2025pr.pdf]",
      default_method="2024 revised up from 445,011pr (+2.0% late registration)",
      prov_years=(2025,))
# GFR (revised vintage, Mar-2026)
write("COL", "gfr_national",
      [(2016,51.8),(2017,52.0),(2018,51.8),(2019,50.0),(2020,47.7),(2021,45.9),
       (2022,42.1),(2023,37.4),(2024,32.6),(2025,30.9)],
      "DANE EEVV Boletin IIsem-2025pr (20-mar-2026), Grafico 4 (revised series) [bol-EEVV-IIsem2025pr.pdf]",
      default_method="nacidos vivos per 1,000 women 15-49; revised vintage (2018: 50.6->51.8 vs older series)",
      prov_years=(2025,))

# ----------------------------------------------------------------- CHILE
print("CHILE (INE / DEIS-MINSAL)")
# TFR: only 2022 definitive + 2023/2024 provisional are text-confirmed; 2010-2021 chart-only (NOT extracted)
write("CHL", "tfr_national",
      [(2022,1.25,"definitive basis; corrected births; denom EE.PP base Censo 2017",None),
       (2023,1.16,"provisional; uses OBSERVED (uncorrected) births",None),
       (2024,1.03,"provisional; uses OBSERVED births; methodology break vs corrected 1992-2022 series",None)],
      "INE Chile, Boletines Demograficos / Anuario EV (2022 def; 2023/2024 prov)",
      prov_years=(2023,2024))
# Births: INE Anuario EV 2022 Tabla 10 (2010-2022) + provisional bulletins 2023/2024
write("CHL", "births_national",
      [(2010,250643),(2011,247358),(2012,243635),(2013,242005),(2014,250997),
       (2015,244670),(2016,231749),(2017,219186),(2018,221731),(2019,210188),
       (2020,194978),(2021,177273),(2022,189303),(2023,174067),(2024,154441)],
      "INE Chile Anuario EV 2022 Tabla 10 (2010-2022 obs); Boletines provisionales EV2023/EV2024",
      default_method="nacidos vivos by mother residence; observed (uncorrected)",
      prov_years=(2023,2024))

# ----------------------------------------------------------------- ARGENTINA
print("ARGENTINA (DEIS / INDEC)")
# Births recomputed from DEIS open microdata (final 2010-2023; 2024 provisional)
write("ARG", "births_national",
      [(2010,756176),(2011,758042),(2012,738318),(2013,754603),(2014,777012),
       (2015,770040),(2016,728035),(2017,704609),(2018,685394),(2019,625441),
       (2020,533299),(2021,529794),(2022,495295),(2023,460902),(2024,413135)],
      "DEIS (Min. Salud) open microdata, nacidos vivos registrados (summed by anio); 2023 matches Sintesis N10",
      default_method="2014=peak; recomputed from microdata",
      prov_years=(2024,))
# TFR: AEPA-2023 Tabla 1 (Censo-2010 denominators), rounded 1dp; precise endpoints from INDEC Anuario 2023
write("ARG", "tfr_national",
      [(2010,2.383,"INDEC Anuario 2023 precise value; Censo-2010 denom",None),
       (2011,2.4),(2012,2.3),(2013,2.3),(2014,2.4),(2015,2.3),(2016,2.2),
       (2017,2.1),(2018,2.0),(2019,1.9),(2020,1.6),
       (2021,1.558,"INDEC Anuario 2023 precise value; Censo-2010 denom",None)],
      "AEPA 2023 Tabla 1 (DEIS births + INDEC-2013 Censo-2010 projection denom); INDEC Anuario 2023 (030902_2023.xlsx)",
      default_method="rounded 1dp; Censo-2010 denominators (NOT rebased to Censo 2022); 2022-2024 period TGF NOT published",
      prov_years=())

# ----------------------------------------------------------------- COSTA RICA
print("COSTA RICA (INEC)")
write("CRI", "tfr_national",
      [(2010,1.83),(2011,1.87),(2012,1.84),(2013,1.76),(2014,1.78),(2015,1.77),
       (2016,1.71),(2017,1.67),(2018,1.66),(2019,1.56),(2020,1.41),(2021,1.32),
       (2022,1.30),(2023,1.22,"Cuadro 2.2 value; an INEC news release reports 1.19 (denominator-vintage diff)",None),
       (2024,1.12,"INEC news release Jun-2025; denom=post-Censo2022 INEC-CCP jul-2024 projections",None)],
      "INEC CR Panorama Demografico 2023 Cuadro 2.2 (2010-2023); INEC news release (2024)",
      default_method="denom INEC-CCP projections; level +-0.03 denominator-sensitive (Censo 2022 rebasing)",
      prov_years=())
write("CRI", "births_national",
      [(2010,70922),(2011,73459),(2012,73326),(2013,70550),(2014,71793),(2015,71819),
       (2016,70004),(2017,68811),(2018,68449),(2019,64274),(2020,58156),(2021,54288),
       (2022,53435),(2023,50205),(2024,45821)],
      "INEC CR Estadisticas Vitales 2024 Cuadro 3.21",
      default_method="near-complete civil registry; INEC publishes as final (no provisional flag); 2024 press snippet said 45,825",
      prov_years=())

# ----------------------------------------------------------------- MEXICO (comparator; 3 distinct series, do NOT splice)
print("MEXICO (CONAPO / INEGI) - comparator")
# CONAPO modeled TFR: conciliacion <=2019, PROJECTION >=2020
write("MEX", "tfr_conapo_modeled",
      [(2010,2.3705),(2011,2.3151),(2012,2.2587),(2013,2.2154),(2014,2.1779),
       (2015,2.1359),(2016,2.0807),(2017,2.0402),(2018,2.0289),(2019,2.0177),
       (2020,1.9888,"PROJECTION (conciliacion ends 2019)","provisional"),
       (2021,1.9651,"PROJECTION","provisional"),(2022,1.9398,"PROJECTION","provisional"),
       (2023,1.9140,"PROJECTION","provisional"),(2024,1.8884,"PROJECTION","provisional")],
      "CONAPO Conciliacion Demografica 1950-2019 + Proyecciones 2020-2070 (2023 base), 5_Indicadores xlsx",
      default_method="modeled/conciliated; Censo-2020 rebased; DO NOT splice with INEGI/ENADID series")
# INEGI ENADID survey period TGF (survey years only) - materially lower than CONAPO
write("MEX", "tfr_enadid_survey",
      [(2014,2.21),(2018,2.07),(2023,1.60)],
      "INEGI ENADID survey period TGF (2014, 2018, 2023 boletines)",
      default_method="direct survey period TGF; survey years only; 2023 = lowest ever; NOT comparable to CONAPO modeled",
      prov_years=())
# INEGI registered births (by ANO DE REGISTRO - registration-lag caveat; 2020 COVID anomaly)
write("MEX", "births_registered_inegi",
      [(2014,2463420),(2015,2353596),(2016,2293708),(2017,2234039),(2018,2162535),
       (2019,2092214),(2020,1629211,"COVID registry-office disruption, NOT a fertility drop","definitive"),
       (2021,1912178,"rebound = late-registration catch-up","definitive"),
       (2022,1891388),(2023,1820888),(2024,1672227,"only 64.9% of 2024-registered births occurred in 2024","provisional")],
      "INEGI Estadisticas de Nacimientos Registrados (ENR) 2023/2024",
      default_method="tabulated by ANO DE REGISTRO not occurrence; recent years undercount true occurrence; DO NOT use as occurrence series",
      prov_years=())

print("\nnational CSVs ->", OUT)

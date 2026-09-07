#!/usr/bin/env python3
"""
Fase 0.5 — adjudicación pendiente del ejercicio 2025.

Recomputa DESDE CERO, sin reusar los construir_*.py de documento_2025, los cinco
puntos que la instrucción 2026 §8 manda adjudicar. La única entrada son los
analíticos del PEF aprobado 2024 y 2025 y las cifras del CGPE ya extraídas.

Uso: python documento_2026/fase05_adjudicacion.py
"""
import pandas as pd
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DEFLACTOR_CGPE = 1.043       # deflactor del PIB declarado por el CGPE 2025
DEFLACTOR_CIEP = 1.04252     # recuperado de los cuadros de CIEP 2025 en la corrida 2025


def cargar(anio: str, corte: str) -> pd.DataFrame:
    """Carga un analítico del PEF aprobado. Hoja1, encabezado en la primera fila
    con >= 8 celdas. Devuelve IMPORTE en millones de pesos."""
    f = RAIZ / anio / f"{anio}_pef_analitico-{corte}.xlsx"
    if not f.exists():
        alt = list((RAIZ / anio).glob(f"{anio}_pef_analitico-{corte}*.xlsx"))
        if not alt:
            raise FileNotFoundError(f)
        f = alt[0]
    cache = Path(__file__).resolve().parent / "_cache" / f"{anio}_{corte}.pkl"
    if cache.exists():
        return pd.read_pickle(cache)
    crudo = pd.read_excel(f, sheet_name="Hoja1", header=None)
    fila = next(i for i in range(len(crudo)) if crudo.iloc[i].notna().sum() >= 8)
    df = pd.read_excel(f, sheet_name="Hoja1", header=fila)
    df.columns = [str(c).strip() for c in df.columns]
    col_imp = [c for c in df.columns if "IMPORTE" in c.upper()][0]
    df["MDP"] = pd.to_numeric(df[col_imp], errors="coerce") / 1e6
    df = df.dropna(subset=["MDP"])
    cache.parent.mkdir(exist_ok=True)
    df.to_pickle(cache)
    return df


def clave(serie: pd.Series) -> pd.Series:
    """Primer token de una columna que puede venir '5 Educación' o '5'."""
    return serie.astype(str).str.strip().str.split().str[0]


def real(v2024: float, v2025: float, defl: float) -> tuple[float, float]:
    base = v2024 * defl
    return v2025 - base, (v2025 / base - 1) * 100


def sep(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


# ---------------------------------------------------------------- punto 1: salud
def punto1_salud():
    sep("PUNTO 1 — la caída de salud: -12.2 y -7.2 nuestros contra -11.0 del género")
    out = {}
    for anio in ("2024", "2025"):
        gf = cargar(anio, "gf-ramo-funcion-ur-objeto")
        ef = cargar(anio, "entidades-ramo-funcion-ur-objeto")
        gf_s = gf[(clave(gf["F"]) == "2") & (clave(gf["FN"]) == "3")]
        ef_s = ef[(clave(ef["F"]) == "2") & (clave(ef["FN"]) == "3")]
        out[anio] = {
            "gf_total": gf_s["MDP"].sum(),
            "ef_total": ef_s["MDP"].sum(),
            "gf_ramo": gf_s.groupby(clave(gf_s["RAMO"]))["MDP"].sum(),
            "ef_ent": ef_s.groupby(ef_s["ENTIDAD"].astype(str).str.strip())["MDP"].sum(),
        }
    t24 = out["2024"]["gf_total"] + out["2024"]["ef_total"]
    t25 = out["2025"]["gf_total"] + out["2025"]["ef_total"]
    d_nom = t25 - t24
    d_real, v_real = real(t24, t25, DEFLACTOR_CGPE)
    print(f"Función Salud (finalidad 2, función 3), GF + entidades, BRUTO")
    print(f"  2024 = {t24:>12,.1f} mdp   (GF {out['2024']['gf_total']:,.1f} + ent {out['2024']['ef_total']:,.1f})")
    print(f"  2025 = {t25:>12,.1f} mdp   (GF {out['2025']['gf_total']:,.1f} + ent {out['2025']['ef_total']:,.1f})")
    print(f"  diferencia nominal = {d_nom:>+12,.1f} mdp")
    print(f"  diferencia real    = {d_real:>+12,.1f} mdp   -> {v_real:+.2f} % real (deflactor CGPE {DEFLACTOR_CGPE})")
    dr_ciep, vr_ciep = real(t24, t25, DEFLACTOR_CIEP)
    print(f"  con el deflactor implícito de CIEP ({DEFLACTOR_CIEP}): {vr_ciep:+.2f} % real")

    # el adeudo liquidado: Ramo 19, programa R023
    print("\n  Descuento del adeudo liquidado (Ramo 19, R023):")
    for anio in ("2024", "2025"):
        pp = cargar(anio, "gf-ramo-programa-ur-objeto")
        pp = pp[clave(pp["RAMO"]) == "19"]
        cod = pp["MOD"].astype(str).str.strip().str[0] + pp["PP"].astype(str).str.strip().str.zfill(3).str[:3]
        r023 = pp[cod == "R023"]["MDP"].sum()
        s038 = pp[cod == "S038"]["MDP"].sum()
        out[anio]["r023"], out[anio]["s038"] = r023, s038
        print(f"    {anio}: R023 = {r023:>10,.1f}   S038 IMSS-Bienestar = {s038:>10,.1f}")
    a24, a25 = out["2024"]["r023"], out["2025"]["r023"]
    d_ex, v_ex = real(t24 - a24, t25 - a25, DEFLACTOR_CGPE)
    print(f"    sin R023: 2024 {t24-a24:,.1f} -> 2025 {t25-a25:,.1f}  =  {v_ex:+.2f} % real")
    b24 = t24 - a24 - out["2024"]["s038"]
    b25 = t25 - a25 - out["2025"]["s038"]
    _, v_ex2 = real(b24, b25, DEFLACTOR_CGPE)
    print(f"    sin R023 ni S038: {b24:,.1f} -> {b25:,.1f}  =  {v_ex2:+.2f} % real")

    print("\n  Por ramo (GF) y entidad, 2024 -> 2025, variación real con deflactor CGPE:")
    for k in sorted(set(out["2024"]["gf_ramo"].index) | set(out["2025"]["gf_ramo"].index)):
        v24 = out["2024"]["gf_ramo"].get(k, 0.0)
        v25 = out["2025"]["gf_ramo"].get(k, 0.0)
        if max(v24, v25) < 1000:
            continue
        _, vr = real(v24, v25, DEFLACTOR_CGPE) if v24 else (0, float("nan"))
        print(f"    ramo {k:>3}: {v24:>12,.1f} -> {v25:>12,.1f}   {vr:>+7.1f} %")
    for k in sorted(set(out["2024"]["ef_ent"].index) | set(out["2025"]["ef_ent"].index)):
        v24 = out["2024"]["ef_ent"].get(k, 0.0)
        v25 = out["2025"]["ef_ent"].get(k, 0.0)
        if max(v24, v25) < 1000:
            continue
        _, vr = real(v24, v25, DEFLACTOR_CGPE) if v24 else (0, float("nan"))
        print(f"    ent {k:>6}: {v24:>12,.1f} -> {v25:>12,.1f}   {vr:>+7.1f} %")
    return t24, t25




# ------------------------------------------- punto 1b: el perímetro de CIEP, reconstruido
CIEP_SALUD = {  # su cuadro 4.1, mdp de 2025; la columna 2024 viene deflactada por ellos
    "IMSS": (475517.3, 491976.4), "ISSSTE": (79608.5, 81803.2),
    "Pemex": (20091.1, 18442.6), "IMSS-Bienestar": (134145.2, 165352.2),
    "FASSA": (141354.8, 81220.5), "SSa": (101114.1, 66693.2),
    "Bienestar": (0.0, 2000.0), "Aportaciones SS": (68034.3, 760.6),
    "Sedena": (8349.9, 6677.0), "Semar": (3814.5, 3521.2),
}


def perimetro_ciep(anio: str) -> dict:
    """Reconstruye el perímetro declarado en la nota al pie 6 de CIEP 2025, sobre el
    PEF APROBADO del año. Enumerable, línea por línea."""
    gff = cargar(anio, "gf-ramo-funcion-ur-objeto")
    eff = cargar(anio, "entidades-ramo-funcion-ur-objeto")
    gfp = cargar(anio, "gf-ramo-programa-ur-objeto")
    efp = cargar(anio, "entidades-ramo-programa-ur-objeto")

    salud_gf = gff[(clave(gff["F"]) == "2") & (clave(gff["FN"]) == "3")]
    salud_ef = eff[(clave(eff["F"]) == "2") & (clave(eff["FN"]) == "3")]

    def cod(df):
        return (df["MOD"].astype(str).str.strip().str[0]
                + df["PP"].astype(str).str.strip().str.zfill(3).str[:3])

    def cod_ef(df):
        return df["PP"].astype(str).str.strip()

    ent = salud_ef["ENTIDAD"].astype(str).str.strip()
    inv_ef = efp[efp["PP"].astype(str).str.contains("Investigación y desarrollo tecnológico en salud",
                                                    case=False, na=False)]
    inv_por_ent = inv_ef.groupby(inv_ef["ENTIDAD"].astype(str).str.strip())["MDP"].sum()

    # AI 231 = "Personal activo y jubilado saludable y con calidad de vida"; la columna AI
    # trae la CLAVE, no el nombre. Vive en la función 3.3, fuera de la función Salud.
    pemex_ai = efp[efp["ENTIDAD"].astype(str).str.contains("Pemex", case=False, na=False)
                   & (clave(efp["AI"]) == "231")]

    r12 = gff[clave(gff["RAMO"]) == "12"]
    r33_fassa = gfp[(clave(gfp["RAMO"]) == "33") & (cod(gfp) == "I002")]
    casa = gfp[gfp["PP"].astype(str).str.contains("casa por casa", case=False, na=False)]

    def gf_ramo(n):
        return salud_gf[clave(salud_gf["RAMO"]) == n]["MDP"].sum()

    def ent_salud(pat):
        return salud_ef[ent.str.contains(pat, case=False, na=False)]["MDP"].sum()

    def inv(pat):
        m = [v for k, v in inv_por_ent.items() if pat.lower() in k.lower()]
        return sum(m)

    return {
        "IMSS": ent_salud("Instituto Mexicano del Seguro Social") + inv("Instituto Mexicano"),
        "ISSSTE": ent_salud("Trabajadores del Estado") + inv("Trabajadores del Estado"),
        "Pemex": pemex_ai["MDP"].sum(),
        "IMSS-Bienestar": gf_ramo("47"),
        "FASSA": r33_fassa["MDP"].sum(),
        "SSa": r12["MDP"].sum(),
        "Bienestar": casa["MDP"].sum(),
        # CIEP toma solo la UR 420 del Ramo 19 y EXCLUYE al ISSFAM (UR HXA)
        "Aportaciones SS": salud_gf[(clave(salud_gf["RAMO"]) == "19")
                                    & salud_gf["UR"].astype(str).str.strip().str.startswith("420")]["MDP"].sum(),
        "Aportaciones SS (función completa)": gf_ramo("19"),
        "Sedena": gf_ramo("07"),
        "Semar": gf_ramo("13"),
    }


def punto1b():
    sep("PUNTO 1b — el perímetro de CIEP reconstruido sobre el PEF APROBADO")
    p24, p25 = perimetro_ciep("2024"), perimetro_ciep("2025")
    print(f"{'línea':<18}{'CIEP 24 (mdp25)':>17}{'nuestro 24 nom':>16}{'CIEP 25 proy':>14}"
          f"{'nuestro 25 apr':>16}{'dif 25':>11}")
    tot_c24 = tot_c25 = tot_n24 = tot_n25 = 0.0
    for k, (c24, c25) in CIEP_SALUD.items():
        n24, n25 = p24[k], p25[k]
        tot_c24 += c24; tot_c25 += c25; tot_n24 += n24; tot_n25 += n25
        print(f"{k:<18}{c24:>17,.1f}{n24:>16,.1f}{c25:>14,.1f}{n25:>16,.1f}{n25-c25:>+11,.1f}")
    print(f"{'TOTAL':<18}{tot_c24:>17,.1f}{tot_n24:>16,.1f}{tot_c25:>14,.1f}"
          f"{tot_n25:>16,.1f}{tot_n25-tot_c25:>+11,.1f}")
    print(f"\n  CIEP, proyecto contra aprobado 2024 deflactado: "
          f"{(tot_c25/tot_c24-1)*100:+.2f} % real  (publican -11.0)")
    _, v = real(tot_n24, tot_n25, DEFLACTOR_CGPE)
    print(f"  Su perímetro sobre el APROBADO 2025 contra aprobado 2024: {v:+.2f} % real")
    print(f"  Su base 2024 implícita en pesos nominales: {tot_c24/DEFLACTOR_CIEP:,.1f}"
          f"   nuestra reconstrucción: {tot_n24:,.1f}"
          f"   dif {tot_n24-tot_c24/DEFLACTOR_CIEP:+,.1f}")




# ------------------------------------------------------------ punto 2: educación
def punto2_educacion():
    sep("PUNTO 2 — la caída de educación: +0.7 nuestro contra -1.2 del género")
    res = {}
    for anio in ("2024", "2025"):
        gff = cargar(anio, "gf-ramo-funcion-ur-objeto")
        edu = gff[(clave(gff["F"]) == "2") & (clave(gff["FN"]) == "5")]
        r = clave(gff["RAMO"])
        propio = edu["MDP"].sum()                                     # función Educación GF bruta
        # perímetro CIEP: ramos 11, 38 y 48 completos + resto de la función Educación
        tres = gff[r.isin(["11", "38", "48"])]["MDP"].sum()
        edu_en_tres = edu[clave(edu["RAMO"]).isin(["11", "38", "48"])]["MDP"].sum()
        ciep = tres + (propio - edu_en_tres)
        res[anio] = dict(propio=propio, ciep=ciep, tres=tres, edu_en_tres=edu_en_tres,
                         por_ramo=edu.groupby(clave(edu["RAMO"]))["MDP"].sum())
    p24, p25 = res["2024"]["propio"], res["2025"]["propio"]
    c24, c25 = res["2024"]["ciep"], res["2025"]["ciep"]
    _, vp = real(p24, p25, DEFLACTOR_CGPE)
    _, vc = real(c24, c25, DEFLACTOR_CGPE)
    _, vc_d = real(c24, c25, DEFLACTOR_CIEP)
    print(f"  Perímetro PROPIO (función Educación, GF, bruta), aprobado contra aprobado")
    print(f"    2024 {p24:>12,.1f}   2025 {p25:>12,.1f}   {vp:+.2f} % real   (publicamos +0.7)")
    print(f"  Perímetro de CIEP (ramos 11+38+48 completos + resto de la función), aprobado")
    print(f"    2024 {c24:>12,.1f}   2025 {c25:>12,.1f}   {vc:+.2f} % real "
          f"(defl. CGPE) / {vc_d:+.2f} % (defl. CIEP)")
    print(f"    su cifra publicada del PROYECTO: 1,142,490 mdp, -1.2 % real")
    print(f"    su base 2024 implícita en nominales: {1142490/0.988*0:,.1f}" if False else "")
    base_ciep_2025pesos = 1142490 / (1 - 0.012)
    print(f"    base 2024 implícita en su columna (mdp 2025): {base_ciep_2025pesos:,.1f}"
          f"   -> nominal {base_ciep_2025pesos/DEFLACTOR_CIEP:,.1f}")
    print(f"    nuestra reconstrucción de su base 2024 nominal: {c24:,.1f}"
          f"   dif {c24-base_ciep_2025pesos/DEFLACTOR_CIEP:+,.1f}")
    print(f"\n  Descomposición de la brecha -1.2 -> +{vp:.1f}:")
    print(f"    efecto OBJETO   (proyecto -> aprobado, su perímetro): -1.2 -> {vc:+.2f}"
          f"   =  {vc+1.2:+.2f} pp")
    print(f"    efecto PERÍMETRO (su perímetro -> el nuestro, aprobado): {vc:+.2f} -> {vp:+.2f}"
          f"   =  {vp-vc:+.2f} pp")
    print(f"    la Cámara movió, en su perímetro: {c25 - 1142490:+,.1f} mdp nominales")
    print(f"\n  Función Educación por ramo, 2024 -> 2025 (aprobado):")
    for k in sorted(set(res['2024']['por_ramo'].index) | set(res['2025']['por_ramo'].index)):
        v24 = res["2024"]["por_ramo"].get(k, 0.0); v25 = res["2025"]["por_ramo"].get(k, 0.0)
        if max(v24, v25) < 300:
            continue
        _, vr = real(v24, v25, DEFLACTOR_CGPE) if v24 else (0, float("nan"))
        print(f"    ramo {k:>3}: {v24:>12,.1f} -> {v25:>12,.1f}   {vr:>+7.1f} %")


# -------------------------------------------------------------- punto 3: Defensa
def punto3_defensa():
    sep("PUNTO 3 — Defensa: ramo contra función")
    for anio in ("2024", "2025"):
        gff = cargar(anio, "gf-ramo-funcion-ur-objeto")
        gfp = cargar(anio, "gf-ramo-programa-ur-objeto")
        r07f = gff[clave(gff["RAMO"]) == "07"]
        r07p = gfp[clave(gfp["RAMO"]) == "07"]
        tot = r07p["MDP"].sum()
        print(f"\n  {anio}: Ramo 07 total = {tot:,.1f} mdp (corte por programa)"
              f"   |  {r07f['MDP'].sum():,.1f} (corte por función)")
        print("    por función:")
        g = r07f.groupby([clave(r07f["F"]), clave(r07f["FN"])])["MDP"].sum().sort_values(ascending=False)
        for (f, fn), v in g.items():
            if v < 500:
                continue
            print(f"      {f}.{fn}  {v:>12,.1f}")
        print("    por unidad responsable (>2,000 mdp):")
        ur = r07p.groupby(r07p["UR"].astype(str).str.strip())["MDP"].sum().sort_values(ascending=False)
        for k, v in ur.items():
            if v < 2000:
                continue
            print(f"      {k[:64]:<64} {v:>12,.1f}")




# ---------------------------------------- punto 4: la tasa real del costo financiero
def punto4_tasa_real():
    sep("PUNTO 4 — la tasa real del costo financiero y la compensación por inflación")
    # CGPE 2025, anexos II.6 (p. 82), III.1 (p. 84) y III.2 (p. 85). Leídos como imagen.
    pib24, pib25 = 33927.7, 36166.4           # miles de millones, estimado 2024 y 2025
    d24 = 51.4                                # SHRFSP % PIB, 2024 estimado
    ext24 = 12.9                              # SHRFSP externo % PIB, 2024 estimado
    defl = 0.043                              # deflactor del PIB 2025 (CGPE III.1)
    cpi_prom, cpi_dic = 0.038, 0.035          # inflación 2025 promedio y dic/dic (CGPE III.1)
    tc24, tc25 = 19.7, 18.5                   # tipo de cambio fin de periodo
    cf25, rfspf25 = 1388373.6, 1428348.1      # mdp
    adecuaciones = 0.4                        # "Adecuaciones a registros presupuestarios", % PIB

    n = pib25 / pib24 - 1
    g = (1 + n) / (1 + defl) - 1
    print(f"  Crecimiento nominal del PIB      n = {n*100:.3f} %")
    print(f"  Deflactor del PIB (CGPE)         π = {defl*100:.2f} %  ->  crecimiento real"
          f" implícito γ = {g*100:.3f} %")
    e_crec = -d24 * g / (1 + n)
    e_infl = -d24 * defl * (1 + g) / (1 + n)
    e_fx = ext24 * (tc25 / tc24 - 1)
    print(f"\n  Efectos del denominador (los publicamos así):")
    print(f"    crecimiento real      {e_crec:+.3f} pp   (publicamos -1.06)")
    print(f"    inflación, denominador{e_infl:+.3f} pp   (publicamos -2.12)")
    print(f"    tipo de cambio        {e_fx:+.3f} pp   (publicamos -0.79)")
    print(f"    RFSPF                 {rfspf25/pib25/1000*100:+.3f} pp   (publicamos +3.9)")
    suma = rfspf25 / (pib25 * 1000) * 100 + e_crec + e_infl + e_fx
    print(f"    SUMA DEL MARCO        {suma:+.3f} pp   contra un cambio observado de 0.0")

    print(f"\n  La compensación por inflación pagada, bajo tres convenciones:")
    for nom, p in (("deflactor del PIB, 4.3 (la que publicamos)", defl),
                   ("INPC promedio, 3.8 (el que usa el propio CGPE para la tasa real)", cpi_prom),
                   ("INPC dic/dic, 3.5", cpi_dic)):
        comp = d24 * p / (1 + n)
        print(f"    {nom:<62} {comp:+.3f} pp   ->  neto {e_infl + comp:+.3f} pp")
    print(f"    solo la compensación IDENTIFICABLE en el paquete (línea 'Adecuaciones a")
    print(f"    registros presupuestarios', que el CGPE declara que contiene el componente")
    print(f"    inflacionario de la deuda indexada, y que además trae otras tres cosas):")
    print(f"    {'a lo sumo ' + str(adecuaciones):<62} {adecuaciones:+.3f} pp"
          f"   ->  neto {e_infl + adecuaciones:+.3f} pp")

    tasa_efectiva = cf25 / (d24 / 100 * pib24 * 1000) * 100
    print(f"\n  Tasa nominal efectiva sobre el acervo = costo financiero 2025 / SHRFSP 2024 est."
          f" = {tasa_efectiva:.2f} %")
    print(f"    real con el deflactor 4.3: {tasa_efectiva-4.3:.2f} %   "
          f"real con el INPC promedio 3.8: {tasa_efectiva-3.8:.2f} %")
    print(f"    el CGPE publica, para Cetes 28: nominal promedio 8.9, REAL promedio 4.9")
    print(f"\n  VEREDICTO: la descomposición de cuatro variables NO cambia (la compensación")
    print(f"  es una lectura del RFSPF, no un término aditivo). Lo que no resiste es el -0.05:")
    print(f"  el efecto neto de la inflación va de -0.05 a -1.72 según qué índice se use para")
    print(f"  el pago, y el paquete no identifica cuál. La cota está declarada desde 2023.")


# ------------------------------------------- punto 5: los niveles nominales del acervo
def punto5_acervo():
    sep("PUNTO 5 — los niveles nominales del acervo")
    fuente = {  # CGPE 2025, Anexo II.6, p. 82, leído de la página renderizada a 150 dpi
        "SHRFSP 2024 aprobado": (16787906.1, 34374.0, 48.8),
        "SHRFSP 2024 estimado": (17440245.8, 33927.7, 51.4),
        "SHRFSP 2025 estimado": (18591005.5, 36166.4, 51.4),
    }
    print("  Cotejo del nivel nominal contra su razón a PIB publicada (la prueba de que el")
    print("  nivel se leyó de la fuente y no se derivó del porcentaje):")
    for k, (mdp, pib, pct) in fuente.items():
        calc = mdp / (pib * 1000) * 100
        print(f"    {k:<24} {mdp:>14,.1f} mdp   PIB {pib:>9,.1f} mmp"
              f"   {calc:>6.3f} % calculado contra {pct} publicado   dif {calc-pct:+.3f} pp")
    print("\n  Identidad flujo-acervo en pesos (la prueba independiente):")
    d_stock = fuente["SHRFSP 2025 estimado"][0] - fuente["SHRFSP 2024 estimado"][0]
    rfspf = 1428348.1
    fx_pp = 12.9 * (18.5 / 19.7 - 1)
    fx_mdp = fx_pp / 100 * 36166.4 * 1000
    print(f"    Δ acervo observado                       {d_stock:>14,.1f} mdp")
    print(f"    RFSPF 2025                               {rfspf:>14,.1f} mdp")
    print(f"    efecto de tipo de cambio ({fx_pp:+.3f} pp)     {fx_mdp:>14,.1f} mdp")
    print(f"    RFSPF + tipo de cambio                   {rfspf+fx_mdp:>14,.1f} mdp")
    print(f"    RESIDUO                                  {d_stock-rfspf-fx_mdp:>+14,.1f} mdp"
          f"   =  {(d_stock-rfspf-fx_mdp)/(36166.4*1000)*100:+.3f} % del PIB")
    print("\n  VEREDICTO: los tres niveles son restitución de la fuente, no derivación del")
    print("  porcentaje: las tres razones recalculadas coinciden con las publicadas y la")
    print("  identidad flujo-acervo cierra a dos centésimas de punto del PIB con el efecto")
    print("  de tipo de cambio dentro. Las cifras resisten.")


if __name__ == "__main__":
    punto1_salud()
    punto1b()
    punto2_educacion()
    punto3_defensa()
    punto4_tasa_real()
    punto5_acervo()

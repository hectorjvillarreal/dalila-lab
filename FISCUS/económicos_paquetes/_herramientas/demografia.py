#!/usr/bin/env python3
"""Capa demográfica: descarga los denominadores y construye las series.

Precarga §3.1 de INSTRUCCIONES_preparacion_2027.md. NINGUNA de estas fuentes depende
del paquete económico: todo esto se descarga y se verifica ANTES de la entrega.

    python demografia.py --descargar    # trae los crudos a datos_demograficos/_crudos/
    python demografia.py --construir    # deriva las series y escribe _fuentes.csv
    python demografia.py                # las dos cosas

REGLAS DE LA CASA que este archivo obedece y que el documento debe repetir:
  · Cuadro presupuestal y cuadro per cápita van SEPARADOS.
  · Toda cifra per cápita declara su denominador, con fuente y año de referencia.
  · En educación hay TRES denominadores distintos que dan tres lecturas distintas:
    población total, población en edad escolar y matrícula. No son intercambiables.
  · Una razón de presión demográfica NO es una prestación media: el denominador
    incluye a quien no recibe y el numerador puede incluir a quien no está en el
    grupo. Esa advertencia se conserva siempre.
"""
from __future__ import annotations
import argparse, csv, json, re, subprocess, sys, time
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
DEST = RAIZ / "datos_demograficos"
CRUDOS = DEST / "_crudos"
BUNDLE = AQUI / "_certs" / "bundle.pem"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/128.0 Safari/537.36")
CKAN = "https://www.datos.gob.mx/api/3/action"
PAUSA = 2.0
TIER = "externa_demografica"

# Tramos de edad y el nivel educativo al que corresponden. El corte 18-24 es el que
# CONAPO publica agregado; la edad típica de educación superior es 18-22, de modo que
# el denominador de superior queda ANCHO. Se declara, no se corrige en silencio.
NIVEL_EDAD = {
    "preescolar":      ("POB_3_5",   "3 a 5 años"),
    "primaria":        ("POB_6_11",  "6 a 11 años"),
    "secundaria":      ("POB_12_14", "12 a 14 años"),
    "media_superior":  ("POB_15_17", "15 a 17 años"),
    "superior":        ("POB_18_24", "18 a 24 años (ancho: la edad típica es 18 a 22)"),
}

FUENTES: list[dict] = []


def anota(archivo, concepto, documento, ubicacion, anio_ref, cobertura, liga, nota=""):
    FUENTES.append(dict(archivo=archivo, concepto=concepto, documento=documento,
                        ubicacion=ubicacion, anio_referencia=anio_ref, cobertura=cobertura,
                        liga=liga, tier=TIER, fecha_acceso=date.today().isoformat(), nota=nota))


# --------------------------------------------------------------------------- red
def bajar(url: str, destino: Path, minimo: int = 500) -> bool:
    """Descarga con verificación TLS activa. Comprueba que no sea un soft-404."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["curl", "-sSL", "-A", UA, "--max-time", "600", "-o", str(destino),
           "-w", "%{http_code}\t%{content_type}"]
    if BUNDLE.exists():
        cmd[1:1] = ["--cacert", str(BUNDLE)]
    p = subprocess.run(cmd + [url], capture_output=True, text=True)
    cod, _, tipo = p.stdout.partition("\t")
    n = destino.stat().st_size if destino.exists() else 0
    ok = cod.startswith("2") and n >= minimo and "text/html" not in tipo
    print(f"  [{'OK ' if ok else 'FALLA'}] {destino.name:<46} {cod} {n:>12,} b  {tipo.strip()[:28]}")
    if not ok and destino.exists():
        destino.unlink()          # un soft-404 guardado es peor que un hueco
    time.sleep(PAUSA)
    return ok


UMBRAL_REDUCCION = 200_000_000        # 200 MB


def reducir(archivo: Path) -> None:
    """Un padrón nominal de cientos de MB no se conserva: se agrega y se borra.

    Lo que el documento necesita de un padrón es el conteo, no el registro. Guardar
    el nominal cuesta gigabytes, no aporta una cifra más y arrastra datos personales
    seudonimizados que este proyecto no tiene por qué custodiar."""
    if archivo.stat().st_size < UMBRAL_REDUCCION:
        return
    import pandas as pd
    print(f"  reduciendo {archivo.name} ({archivo.stat().st_size/1e9:.2f} GB)…")
    llaves = ("anio", "mes", "entidad", "sexo", "modalidad", "sector")
    acum, n = None, 0
    for trozo in pd.read_csv(archivo, chunksize=500_000, low_memory=False):
        trozo.columns = [c.strip().lstrip("\ufeff") for c in trozo.columns]
        cols = [c for c in llaves if c in trozo.columns]
        if not cols:
            print("    sin columnas de agrupación conocidas; se conserva el crudo"); return
        n += len(trozo)
        g = trozo.groupby(cols, dropna=False).size().rename("personas").reset_index()
        acum = g if acum is None else (pd.concat([acum, g])
                                       .groupby(cols, dropna=False)["personas"].sum().reset_index())
    salida = archivo.with_name(archivo.stem + "__agregado.csv")
    acum.sort_values("personas", ascending=False).to_csv(salida, index=False)
    archivo.unlink()
    print(f"    {n:,} registros -> {len(acum):,} renglones en {salida.name}; crudo borrado")


def ckan(pkg: str) -> dict | None:
    cmd = ["curl", "-sSL", "-A", UA, "--max-time", "60", f"{CKAN}/package_show?id={pkg}"]
    if BUNDLE.exists():
        cmd[1:1] = ["--cacert", str(BUNDLE)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    time.sleep(PAUSA)
    try:
        d = json.loads(p.stdout)
    except json.JSONDecodeError:
        return None
    return d["result"] if d.get("success") else None


# ------------------------------------------------------- IMSS: cubo de asegurados
# El catálogo nacional NO tiene asegurados del IMSS: se buscó dos veces en la corrida
# 2026 y no está. El dato vive en el portal propio del Instituto, que es Drupal y no
# CKAN, así que no responde a package_search. La ruta directa del archivo mensual es
# estable desde 1997 y es ésta.
IMSS_CUBO = "http://datos.imss.gob.mx/sites/default/files/asg-{mes}.csv"
IMSS_MESES = ("2025-07-31", "2026-07-31")   # mismo mes, dos años: comparación limpia
IMSS_ENT = {  # cve_entidad del cubo -> nombre. 33 y 99 no son entidades.
    1:"Aguascalientes",2:"Baja California",3:"Baja California Sur",4:"Campeche",
    5:"Coahuila",6:"Colima",7:"Chiapas",8:"Chihuahua",9:"Ciudad de México",
    10:"Durango",11:"Guanajuato",12:"Guerrero",13:"Hidalgo",14:"Jalisco",15:"México",
    16:"Michoacán",17:"Morelos",18:"Nayarit",19:"Nuevo León",20:"Oaxaca",21:"Puebla",
    22:"Querétaro",23:"Quintana Roo",24:"San Luis Potosí",25:"Sinaloa",26:"Sonora",
    27:"Tabasco",28:"Tamaulipas",29:"Tlaxcala",30:"Veracruz",31:"Yucatán",32:"Zacatecas",
}


def imss_asegurados(meses=IMSS_MESES) -> None:
    """Baja el cubo mensual (≈400 MB), lo agrega por entidad, sexo y edad, y lo borra.

    ASEGURADOS NO ES DERECHOHABIENTES. El cubo cuenta puestos de trabajo afiliados y
    asegurados sin empleo asociado; los familiares beneficiarios NO están. Un gasto
    por afiliado calculado con este denominador da una cifra varias veces mayor que
    el mismo gasto por derechohabiente. La distinción se declara en `_fuentes.csv` y
    tiene que llegar al cuadro."""
    import pandas as pd
    CRUDOS.mkdir(parents=True, exist_ok=True)
    for mes in meses:
        salida = CRUDOS / f"imss_asegurados_{mes}.csv"
        if salida.exists():
            print(f"  [YA ] {salida.name}"); continue
        crudo = CRUDOS / f"asg-{mes}.csv"
        if not bajar(IMSS_CUBO.format(mes=mes), crudo, minimo=10_000_000):
            continue
        acum = None
        for t in pd.read_csv(crudo, sep="|", chunksize=400_000, low_memory=False,
                             encoding="latin-1"):
            t.columns = [c.strip().lstrip("\ufeff") for c in t.columns]
            g = (t.groupby(["cve_entidad", "sexo", "rango_edad"], dropna=False)["asegurados"]
                   .sum().reset_index())
            acum = g if acum is None else (pd.concat([acum, g])
                    .groupby(["cve_entidad", "sexo", "rango_edad"], dropna=False)["asegurados"]
                    .sum().reset_index())
        acum.insert(0, "mes", mes)
        acum.to_csv(salida, index=False)
        crudo.unlink()          # 400 MB no se conservan: lo que hace falta es el conteo
        print(f"    {len(acum):,} renglones en {salida.name}; crudo borrado "
              f"({acum.asegurados.sum():,.0f} asegurados)")


# ---------------------------------------------------------------------- descarga
def descargar() -> None:
    CRUDOS.mkdir(parents=True, exist_ok=True)
    print("CONAPO — proyecciones 1950-2070")
    bajar("https://repodatos.atdt.gob.mx/CONAPO/proyecciones/05_Indicadores_demograficos_proyecciones.csv",
          CRUDOS / "conapo_indicadores_1950_2070.csv", minimo=100_000)
    # 45 MB de edad simple. Solo hace falta si se quiere un tramo que los indicadores
    # no traigan agregado; los tramos escolares y 65+ sí vienen agregados.
    ya = RAIZ / "documento_2026/datos/_externas/conapo_pob_mitad_1950_2070.csv"
    if ya.exists() and not (CRUDOS / "conapo_pob_mitad_1950_2070.csv").exists():
        (CRUDOS / "conapo_pob_mitad_1950_2070.csv").write_bytes(ya.read_bytes())
        print(f"  [OK ] conapo_pob_mitad_1950_2070.csv               copiado de la corrida 2026")
    else:
        bajar("https://repodatos.atdt.gob.mx/CONAPO/proyecciones/00_Pob_Mitad_1950_2070.csv",
              CRUDOS / "conapo_pob_mitad_1950_2070.csv", minimo=1_000_000)

    print("\nPadrones — catálogo nacional de datos abiertos")
    for pkg, pref, n in (("padron_derechohabientes_activos", "issste_derechohabientes", 1),
                         ("personas_sin_seguridad_social_registro_padron_imss_bienestar",
                          "imssb_sin_seguridad_social", 2),
                         ("padron_unico_beneficiarios_bienestar", "bienestar_padron_unico", 1)):
        r = ckan(pkg)
        if not r:
            print(f"  [FALLA] el catálogo no devuelve el paquete {pkg}")
            continue
        for i, res in enumerate(r["resources"][:n]):
            slug = "".join(c if c.isalnum() else "_" for c in str(res.get("name", ""))[:44]).strip("_")
            destino = CRUDOS / f"{pref}__{i}_{slug}.csv"
            if bajar(res["url"], destino):
                reducir(destino)

    print("\nContraste externo — Banco Mundial (SP.POP.TOTL), sustituto declarado de CELADE")
    bajar("https://api.worldbank.org/v2/country/MEX/indicator/SP.POP.TOTL"
          "?format=json&date=2015:2030&per_page=40", CRUDOS / "bm_poblacion_mex.json", minimo=200)

    print("\nSEP — matrícula por tipo educativo (ASP.NET WebForms, POST con __VIEWSTATE)")
    sep_matricula()

    print("\nIMSS — cubo mensual de asegurados (portal propio, no el catálogo nacional)")
    imss_asegurados()


# ------------------------------------------------------------------- SEP: scraper
SEP = "https://www.planeacion.sep.gob.mx/principalescifras/"
# valores del desplegable de ciclo escolar, leídos de la página
SEP_CICLOS = {"2025-2026": "29", "2024-2025": "28", "2023-2024": "27", "2022-2023": "26"}
SEP_TIPOS = {"1": "Educación Básica", "3": "Educación Media Superior", "4": "Educación Superior"}


def _sep_get(datos: str | None = None) -> str:
    cmd = ["curl", "-sSL", "-A", UA, "--max-time", "90"]
    if BUNDLE.exists():
        cmd += ["--cacert", str(BUNDLE)]
    if datos is not None:
        cmd += ["-X", "POST", "--data-binary", datos,
                "-H", "Content-Type: application/x-www-form-urlencoded"]
    p = subprocess.run(cmd + [SEP], capture_output=True, text=True)
    time.sleep(PAUSA)
    return p.stdout


def sep_matricula() -> None:
    """Consulta el sistema de la DGPPyEE. Devuelve alumnos, escuelas y docentes por
    tipo educativo y ciclo. La página es WebForms: hay que conservar __VIEWSTATE."""
    import re, html as _h, urllib.parse as up

    def oculto(t, n):
        m = re.search(r'name="%s"[^>]*value="([^"]*)"' % n, t)
        return _h.unescape(m.group(1)) if m else ""

    def formulario(t, **kw):
        f = {"__EVENTTARGET": "", "__EVENTARGUMENT": "", "__LASTFOCUS": "",
             "__VIEWSTATE": oculto(t, "__VIEWSTATE"),
             "__VIEWSTATEGENERATOR": oculto(t, "__VIEWSTATEGENERATOR"),
             "__EVENTVALIDATION": oculto(t, "__EVENTVALIDATION"),
             "DDLciclos": "29", "DDLEscolarizadas": "1", "DDLNivel": "0", "DDLModalidad": "0",
             "DDLServicio": "0", "DDLControl": "0", "DDLSostenimiento": "0",
             "DDLEntidad": "0", "DDLMunicipio": "0"}
        f.update(kw)
        return up.urlencode(f)

    def total(t):
        """La fila TOTAL de la tabla de resultados: escuelas, alumnos, M, H, docentes."""
        for tb in re.finditer(r"<table[^>]*>(.*?)</table>", t, re.S | re.I):
            for fila in re.findall(r"<tr[^>]*>(.*?)</tr>", tb.group(1), re.S | re.I):
                c = [" ".join(_h.unescape(re.sub("<[^>]+>", "", x)).split())
                     for x in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", fila, re.S | re.I)]
                if c and c[0].strip().upper() == "TOTAL" and len(c) >= 6:
                    return [int(v.replace(",", "")) if v.replace(",", "").isdigit() else None
                            for v in c[1:6]]
        return None

    def consultar(cv, tipo_cv):
        """Cascada completa por consulta. Reutilizar el __VIEWSTATE de una consulta
        anterior devuelve tablas de otro ciclo sin avisar: en la primera corrida así,
        la media superior de 2023-2024 salió 20 717 alumnos en vez de cinco millones.
        Cada consulta parte de cero."""
        b0 = _sep_get()
        if "DDLciclos" not in b0:
            return None
        p1 = _sep_get(formulario(b0, DDLciclos=cv, DDLEscolarizadas="0",
                                 __EVENTTARGET="DDLciclos"))
        p2 = _sep_get(formulario(p1, DDLciclos=cv, __EVENTTARGET="DDLEscolarizadas"))
        return total(_sep_get(formulario(p2, DDLciclos=cv, DDLNivel=tipo_cv,
                                         Button1="Consulta")))

    filas, sospechas = [], []
    for ciclo, cv in SEP_CICLOS.items():
        por_tipo = {}
        for tipo_cv, tipo_nom in [("0", "Todos los tipos")] + list(SEP_TIPOS.items()):
            t = consultar(cv, tipo_cv)
            if not t:
                print(f"  [FALLA] {ciclo} {tipo_nom}: sin fila TOTAL")
                continue
            esc, al, alm, alh, doc = t
            por_tipo[tipo_nom] = al
            filas.append(dict(ciclo=ciclo, tipo_educativo=tipo_nom, modalidad="escolarizada",
                              escuelas=esc, alumnos=al, alumnos_mujeres=alm,
                              alumnos_hombres=alh, docentes=doc))
            print(f"  [OK ] {ciclo} {tipo_nom:<26} alumnos {al:>12,}")
        # CONTROL DE CONSISTENCIA: los tres tipos deben sumar el total del ciclo.
        piezas = [por_tipo.get(v) for v in SEP_TIPOS.values()]
        tot = por_tipo.get("Todos los tipos")
        if tot and all(piezas):
            d = sum(piezas) - tot
            if abs(d) > 1000:
                sospechas.append((ciclo, sum(piezas), tot, d))
                print(f"  [ALERTA] {ciclo}: los tres tipos suman {sum(piezas):,} contra un "
                      f"total de {tot:,} (dif {d:+,}). El ciclo se DESCARTA.")
                filas = [f for f in filas if f["ciclo"] != ciclo]
            else:
                print(f"  [CTRL] {ciclo}: los tres tipos suman el total (dif {d:+,})")
    if sospechas:
        print(f"  {len(sospechas)} ciclo(s) descartado(s) por inconsistencia interna. "
              f"No se publica una matrícula que no cierra contra su propio total.")
    if filas:
        CRUDOS.mkdir(parents=True, exist_ok=True)
        with (CRUDOS / "sep_matricula.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
        print(f"  escrito _crudos/sep_matricula.csv con {len(filas)} filas")


# ------------------------------------------------------------------- construcción
def construir(anios=range(2018, 2031)) -> None:
    import pandas as pd
    DEST.mkdir(parents=True, exist_ok=True)
    ind = CRUDOS / "conapo_indicadores_1950_2070.csv"
    if not ind.exists():
        print(f"falta {ind}. Corre --descargar primero.", file=sys.stderr); return
    df = pd.read_csv(ind, low_memory=False)
    # TRAMPA VERIFICADA EL 2026-09-07: las DOS rutas oficiales al mismo archivo de
    # indicadores de CONAPO sirven convenciones DISTINTAS de nombre de columna. La ruta
    # repodatos.atdt.gob.mx/CONAPO/proyecciones/ da POB_12_14; la de
    # www.datos.gob.mx/dataset/f2b9b220-.../download/ da POB_012_014. Mismos datos,
    # nombres distintos. Se normaliza quitando los ceros a la izquierda de cada tramo.
    df.columns = [re.sub(r"_0+(\d)", r"_\1", str(c).strip()) for c in df.columns]
    df = df[df.ANIO.isin(anios)]

    # --- nacional -----------------------------------------------------------
    nac = df[df.ENTIDAD_FEDERATIVA == "República Mexicana"].copy()
    cols = {"ANIO": "anio", "POB_MIT_ANIO": "poblacion_total", "POB_65_MAS": "poblacion_65_mas",
            "RAZ_DEP": "razon_dependencia", "RAZ_DEP_ADU": "razon_dependencia_adulta",
            "RAZ_DEP_INF": "razon_dependencia_infantil", "TGF": "tasa_global_fecundidad",
            "EV": "esperanza_vida", "IND_ENV": "indice_envejecimiento"}
    for nivel, (col, _) in NIVEL_EDAD.items():
        cols[col] = f"edad_escolar_{nivel}"
    n = nac[list(cols)].rename(columns=cols).sort_values("anio")
    n.to_csv(DEST / "poblacion_nacional.csv", index=False, float_format="%.4f")
    anota("poblacion_nacional.csv",
          "población total, 65 y más, edad escolar por nivel, razones de dependencia, TGF y "
          "esperanza de vida",
          "CONAPO, Proyecciones de la Población de México 2020-2070",
          "05_Indicadores_demograficos_proyecciones.csv, renglón República Mexicana",
          f"{min(anios)}-{max(anios)}", "nacional",
          "https://repodatos.atdt.gob.mx/CONAPO/proyecciones/05_Indicadores_demograficos_proyecciones.csv",
          "Población a mitad de año. El tramo de superior es 18-24, más ancho que la edad "
          "típica 18-22: sobreestima el denominador y por tanto subestima el gasto por persona "
          "en edad de cursar superior.")

    # --- por entidad --------------------------------------------------------
    ent = df[df.ENTIDAD_FEDERATIVA != "República Mexicana"].copy()
    ent["edad_escolar_3_14"] = ent.POB_3_5 + ent.POB_6_11 + ent.POB_12_14
    e = (ent[["ANIO", "CVE_GEO", "ENTIDAD_FEDERATIVA", "POB_MIT_ANIO", "POB_65_MAS",
              "edad_escolar_3_14", "RAZ_DEP"]]
         .rename(columns={"ANIO": "anio", "CVE_GEO": "cve_geo",
                          "ENTIDAD_FEDERATIVA": "entidad", "POB_MIT_ANIO": "poblacion_total",
                          "POB_65_MAS": "poblacion_65_mas", "RAZ_DEP": "razon_dependencia"})
         .sort_values(["anio", "cve_geo"]))
    e.to_csv(DEST / "poblacion_entidad.csv", index=False, float_format="%.4f")
    anota("poblacion_entidad.csv", "población total, 65 y más y 3 a 14 años por entidad",
          "CONAPO, Proyecciones de la Población de México 2020-2070",
          "05_Indicadores_demograficos_proyecciones.csv, renglones por entidad",
          f"{min(anios)}-{max(anios)}", "32 entidades federativas",
          "https://repodatos.atdt.gob.mx/CONAPO/proyecciones/05_Indicadores_demograficos_proyecciones.csv")

    # --- matrícula ----------------------------------------------------------
    mat = CRUDOS / "sep_matricula.csv"
    if mat.exists():
        m = pd.read_csv(mat)
        m.to_csv(DEST / "matricula_sep.csv", index=False)
        anota("matricula_sep.csv", "matrícula, escuelas y docentes por tipo educativo",
              "SEP, DGPPyEE, Principales Cifras del Sistema Educativo Nacional",
              "consulta al sistema en línea; fuente primaria, cuestionarios del Formato 911",
              "ciclos " + ", ".join(sorted(m.ciclo.unique())), "nacional, modalidad escolarizada",
              SEP,
              "MATRÍCULA NO ES POBLACIÓN EN EDAD ESCOLAR. El gasto por alumno usa esta "
              "columna; el gasto por persona en edad de cursar usa poblacion_nacional.csv. "
              "Dan lecturas distintas y no se mezclan en un mismo cuadro.")

    # --- padrones -----------------------------------------------------------
    for patron, salida, concepto, doc, cobertura, nota in (
        ("issste_derechohabientes__*.csv", "derechohabientes_issste.csv",
         "padrón de derechohabientes activos del ISSSTE",
         "ISSSTE, padrón de derechohabientes activos, mensual", "nacional",
         "Derechohabientes activos, no asegurados cotizantes: incluye familiares. "
         "No es comparable con el padrón de asegurados del IMSS."),
        ("imssb_sin_seguridad_social__*.csv", "sin_seguridad_social_imssb.csv",
         "personas sin seguridad social con registro en el padrón de IMSS-Bienestar",
         "IMSS-Bienestar, padrón trimestral", "PARCIAL: solo las entidades adheridas",
         "COBERTURA PARCIAL. En 2T2025 eran 23 de 32 entidades. Es un padrón de registro, "
         "no una medición de la población sin afiliación: quien no se registra no aparece. "
         "Para población sin afiliación como tal, la fuente es censal o de encuesta."),
        ("bienestar_padron_unico__*.csv", "padron_bienestar.csv",
         "padrón único de beneficiarios de la Secretaría de Bienestar",
         "Secretaría de Bienestar, padrón único consolidado por entidad", "nacional",
         "Consolidado por entidad y programa. Es la fuente de los padrones de los programas "
         "pensionarios no contributivos, incluida la pensión para mujeres, donde el programa "
         "aparezca desglosado."),
    ):
        arch = sorted(CRUDOS.glob(patron))
        if not arch:
            print(f"  falta {patron}: no se construye {salida}")
            continue
        partes = []
        for a in arch:
            try:
                d = pd.read_csv(a, low_memory=False)
            except Exception as ex:
                print(f"  no se pudo leer {a.name}: {ex}"); continue
            d.insert(0, "archivo_origen", a.name)
            partes.append(d)
        if not partes:
            continue
        pd.concat(partes, ignore_index=True).to_csv(DEST / salida, index=False)
        anota(salida, concepto, doc, ", ".join(a.name for a in arch),
              date.today().year, cobertura,
              "https://www.datos.gob.mx/ (catálogo nacional de datos abiertos)", nota)

    # --- IMSS: asegurados ---------------------------------------------------
    arch = sorted(CRUDOS.glob("imss_asegurados_*.csv"))
    if arch:
        a = pd.concat([pd.read_csv(x) for x in arch], ignore_index=True)
        a["entidad"] = a.cve_entidad.map(IMSS_ENT).fillna("no asignado o extranjero")
        a["sexo"] = a.sexo.map({1: "hombres", 2: "mujeres"}).fillna("no especificado")
        a = a[["mes", "cve_entidad", "entidad", "sexo", "rango_edad", "asegurados"]]
        a.sort_values(["mes", "cve_entidad", "sexo", "rango_edad"]).to_csv(
            DEST / "asegurados_imss.csv", index=False)
        tot = a.groupby("mes")["asegurados"].sum()
        anota("asegurados_imss.csv", "asegurados del IMSS por entidad, sexo y rango de edad",
              "IMSS, cubo mensual de puestos de trabajo afiliados y asegurados sin un empleo "
              "asociado", ", ".join(x.name for x in arch),
              ", ".join(sorted(a.mes.unique())), "nacional y 32 entidades",
              "http://datos.imss.gob.mx/dataset/asg-2026 (archivo: "
              "http://datos.imss.gob.mx/sites/default/files/asg-AAAA-MM-DD.csv)",
              "ASEGURADOS NO ES DERECHOHABIENTES: cuenta a la persona asegurada, no a sus "
              "familiares beneficiarios, de modo que un gasto por afiliado con este "
              "denominador da una cifra varias veces mayor que el mismo gasto por "
              "derechohabiente, y NO es comparable con el padrón del ISSSTE, que sí incluye "
              "familiares. Incluye asegurados sin empleo asociado. Totales: "
              + "; ".join(f"{m} = {v:,.0f}" for m, v in tot.items())
              + ". El catálogo nacional NO tiene esta serie: el portal propio del Instituto "
                "es Drupal y no responde a package_search, así que la ruta es directa al "
                "archivo. El cubo mensual pesa unos 400 MB y NO se conserva: se agrega y se "
                "borra. La columna `no_trabajadores` no se agregó en la corrida del "
                "2026-09-07; para separarla hay que volver a bajar el cubo.")

    # --- contraste externo --------------------------------------------------
    bm = CRUDOS / "bm_poblacion_mex.json"
    if bm.exists():
        d = json.loads(bm.read_text())
        filas = [dict(anio=int(r["date"]), poblacion_banco_mundial=r["value"])
                 for r in d[1] if r.get("value")]
        c = pd.DataFrame(filas).sort_values("anio").merge(
            n[["anio", "poblacion_total"]].rename(columns={"poblacion_total": "poblacion_conapo"}),
            on="anio", how="inner")
        c["diferencia"] = c.poblacion_conapo - c.poblacion_banco_mundial
        c["diferencia_pct"] = c.diferencia / c.poblacion_banco_mundial * 100
        c.to_csv(DEST / "contraste_poblacion.csv", index=False, float_format="%.4f")
        anota("contraste_poblacion.csv", "población total de México, CONAPO contra Banco Mundial",
              "Banco Mundial, World Development Indicators, SP.POP.TOTL",
              "api.worldbank.org/v2/country/MEX/indicator/SP.POP.TOTL",
              f"{c.anio.min()}-{c.anio.max()}", "nacional",
              "https://api.worldbank.org/v2/country/MEX/indicator/SP.POP.TOTL",
              "SUSTITUTO DECLARADO de CELADE, que no se pudo obtener: la API de CEPALSTAT "
              "responde por indicador pero su endpoint de catálogo devuelve 404 y el "
              "identificador del indicador de población no se pudo descubrir sin adivinar "
              "rutas. Se usa el Banco Mundial como vara externa y se declara la sustitución.")

    if FUENTES:
        with (DEST / "_fuentes.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(FUENTES[0])); w.writeheader(); w.writerows(FUENTES)
        print(f"\nescrito datos_demograficos/_fuentes.csv con {len(FUENTES)} series")
    for p in sorted(DEST.glob("*.csv")):
        print(f"  {p.name:<34} {sum(1 for _ in p.open(encoding='utf-8')) - 1:>8,} filas")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--descargar", action="store_true")
    ap.add_argument("--construir", action="store_true")
    a = ap.parse_args()
    if not (a.descargar or a.construir):
        a.descargar = a.construir = True
    if a.descargar:
        descargar()
    if a.construir:
        print()
        construir()
    return 0


if __name__ == "__main__":
    sys.exit(main())

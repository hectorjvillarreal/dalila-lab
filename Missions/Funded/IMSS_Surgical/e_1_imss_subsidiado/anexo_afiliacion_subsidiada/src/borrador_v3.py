"""Instrucción v1.3: ANEXO_borrador_v3.md a partir de ANEXO_borrador_v2.md, sustituyendo solo las cifras en puntos
del salario y en % de los ingresos del SEM por sus valores con el denominador común; trazabilidad y verificaciones 3.1-3.5."""

from __future__ import annotations

import io
import json
import re
import subprocess

import pandas as pd

from common import DALILA, NUMBERS_JSON, PROJECT, TABLES, record, table

V2 = PROJECT / "ANEXO_borrador_v2.md"
V3 = PROJECT / "ANEXO_borrador_v3.md"
COMMIT_V2 = "2253249"     # salidas con los denominadores anteriores (las que cita el borrador v2)
CAMBIOS = DALILA / "Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/tablas/exp1_cambios_denominador.csv"

FRASE_DENOM_V2 = ("Se calculan con 337 días cotizados (Cuadro II.18), para que los puntos del SBC sean comparables "
                  "con las primas del Informe.")
FRASE_DENOM_V3 = ("Los puntos del salario se miden sobre la masa con tope de 25 UMA, 337 días cotizados (Cuadro II.18) y "
                  "distribución R1 con piso en el salario mínimo, y los porcentajes de los ingresos del SEM usan el Cuadro V.13 "
                  "del Informe; el libro de Finanzas se usa para cotizantes, salarios y supuestos.")

ORACION_2055 = "El año 2055 no se reporta porque la proyección institucional cambia de régimen ese año."
COLS_X1 = ["C1_2026", "C1_2030", "C1_2040", "C1_2054", "C2_2040", "C2_2054"]
SLUG_X1 = {"Pagos determinados": "determinados", "Pagos cobrados": "cobrados", "Prima no cobrada": "no_cobrada",
           "GF: cuota fija F_g": "GF_fija", "GF: subsidio": "GF_subsidio", "GF: Bloque B": "GF_bloqueB",
           "Costo de atención": "costo", "Saldo sin fuente asignada (π_m = 0)": "saldo",
           "Saldo sin fuente asignada (π_m = 1 %)": "saldo_pim1"}
# llave v12b ya registrada antes de la v1.3 (columnas C1 de años de reporte), para la verificación 3.3
V12B = {"determinados": ("A", "pagos_determinados"), "cobrados": ("A", "pagos_privados"), "no_cobrada": ("A", "no_cobrado"),
        "GF_fija": ("A", "GF_cuota_fija"), "GF_subsidio": ("A", "GF_subsidio"), "GF_bloqueB": ("B", "GF_subsidio"),
        "costo": ("Total", "costo"), "saldo": ("Total", "saldo")}
X2 = {"Base": "base", "S2 focalizado": "S2", "S3 amplio": "S3", "G1: el informal paga F_g": "G1",
      "D1: precio plano en UMA (v1.1)": "D1", "Adopción 0.30": "tau30", "Adopción 0.70": "tau70",
      "Adopción 0.90 (solo con descuento automático)": "tau90", "Afiliación voluntaria (T1)": "T1", "Cobro 0.50": "rho50",
      "Cobro 1.00": "rho100", "Selección 1.00": "mu100", "Selección 1.30": "mu130",
      "Individual, beneficiarios ENIGH (0.80)": "U2_enigh", "Individual, beneficiarios Informe (1.07)": "U2_informe",
      "Costo per cápita +1 % real anual": "pim1", "Costo per cápita +2 % real anual": "pim2",
      "C2: población ligada a la formalización": "C2", "F1 dentro del esquema": "F1", "Perfil de costo plano": "plano",
      "Perfil 65+/20-64 = 2": "estilizado_2", "Perfil 65+/20-64 = 4": "estilizado_4", "Umbrales fijos en UMA": "umbral_fijo"}


def fmt(v: float, dec: int, absoluto: bool = False) -> str:
    v = abs(v) if absoluto else v
    s = f"{round(v, dec) + 0.0:.{dec}f}"
    return "0." + "0" * dec if float(s) == 0 else s.replace("-", "−")


def _git_csv(name: str) -> pd.DataFrame:
    rel = (TABLES / f"{name}.csv").relative_to(DALILA)
    txt = subprocess.run(["git", "-C", str(DALILA), "show", f"{COMMIT_V2}:{rel}"], capture_output=True, text=True, check=True).stdout
    return pd.read_csv(io.StringIO(txt))


def _celdas(linea: str) -> list[str]:
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def _linea(celdas: list[str]) -> str:
    return "| " + " | ".join(celdas) + " |"


def sustituciones() -> list[dict]:
    """Cada cifra en puntos o en % del SEM del borrador: (sección, fila, columna, clave, valor viejo, valor nuevo, decimales)."""
    new = {n: pd.read_csv(TABLES / f"{n}.csv") for n in ("cuadro_X1_pts_sbc", "cuadro_X1_pct_sem", "sensibilidades_v12",
                                                        "bloque_C_vs_status_quo", "efecto_indexacion", "resultados_v12")}
    old = {n: _git_csv(n) for n in new}
    S = []

    def add(sec, fila, col, clave, vo, vn, dec, absoluto=False):
        S.append({"seccion": sec, "fila": fila, "columna": col, "clave": clave, "valor_anterior": vo, "valor_nuevo": vn,
                  "dec": dec, "abs": absoluto})

    # X.4, texto: saldo de 2030 en puntos y en % del SEM (valor absoluto)
    for d, tag in ((new, "n"), (old, "o")):
        b = d["resultados_v12"]
        b = b[(b.corrida == "base") & (b.bloque == "Total") & (b.anio == 2030)].iloc[0]
        if tag == "n":
            pn, sn = b.saldo_pts_sbc, b.saldo_pct_sem
        else:
            po, so = b.saldo_pts_sbc, b.saldo_pct_sem
    add("X.4 texto", "Saldo sin fuente asignada", "2030 puntos", "v12b_Total_saldo_pts_2030", po, pn, 2, True)
    add("X.4 texto", "Saldo sin fuente asignada", "2030 % SEM", "v12b_Total_saldo_sem_2030", so, sn, 1, True)
    # Cuadro X.1 (b) y (c)
    for panel, n, dec in (("(b)", "cuadro_X1_pts_sbc", 2), ("(c)", "cuadro_X1_pct_sem", 1)):
        tn, to = new[n].set_index("concepto"), old[n].set_index("concepto")
        pan = "pts_sbc" if panel == "(b)" else "pct_sem"
        for concepto, slug in SLUG_X1.items():
            for col in COLS_X1:
                clave = f"X1_{pan}_{slug}_{col}"
                if slug in V12B and col.startswith("C1"):
                    bl, c = V12B[slug]
                    clave = f"v12b_{bl}_{c}_{'pts' if pan == 'pts_sbc' else 'sem'}_{col[3:]}"
                add(f"Cuadro X.1 {panel}", concepto, col, clave, to.loc[concepto, col], tn.loc[concepto, col], dec)
    # X.5, efecto neto en puntos
    bn, bo = (d["bloque_C_vs_status_quo"].set_index(["anio", "cuota"]) for d in (new, old))
    for y in (2030, 2040, 2054):
        for cuota, et in (("D2", "D2"), ("vigente", "vigente")):
            add("X.5", "Efecto neto (pts SBC)", f"{y} {et}", f"v12_C_{cuota}_neto_pts_{y}",
                bo.loc[(y, cuota), "efecto_neto_pts_sbc"], bn.loc[(y, cuota), "efecto_neto_pts_sbc"], 2)
    # X.6, efecto de indexación
    en, eo = (d["efecto_indexacion"].set_index("anio") for d in (new, old))
    for y in (2030, 2040, 2054):
        add("X.6", "Puntos del SBC", str(y), f"v12_indexacion_pts_{y}", eo.loc[y, "diferencia_pts_sbc"], en.loc[y, "diferencia_pts_sbc"], 2)
        add("X.6", "% de los ingresos del SEM", str(y), f"v12_indexacion_sem_{y}", eo.loc[y, "diferencia_pct_sem"], en.loc[y, "diferencia_pct_sem"], 1)
    # Cuadro X.2, saldo en puntos 2030 y 2054
    sn_, so_ = (d["sensibilidades_v12"].set_index("corrida") for d in (new, old))
    for et, c in X2.items():
        for y in (2030, 2054):
            add("Cuadro X.2", et, f"Saldo {y} (pts SBC)", f"v12_{c}_saldo_pts_sbc_{y}",
                so_.loc[c, f"saldo_pts_sbc_{y}"], sn_.loc[c, f"saldo_pts_sbc_{y}"], 2)
    # X.7, texto: costo per cápita +2 % en 2054
    add("X.7 texto", "Costo per cápita +2 %", "2054 puntos", "v12_pim2_saldo_pts_sbc_2054",
        so_.loc["pim2", "saldo_pts_sbc_2054"], sn_.loc["pim2", "saldo_pts_sbc_2054"], 2)
    for s in S:
        s["texto_anterior"] = fmt(s["valor_anterior"], s["dec"], s["abs"])
        s["texto_nuevo"] = fmt(s["valor_nuevo"], s["dec"], s["abs"])
    return S


def construir(S: list[dict]) -> tuple[str, list[str]]:
    """Aplica las sustituciones al texto del borrador v2; devuelve el v3 y las discrepancias de mapeo (texto v2 ≠ valor viejo)."""
    L = V2.read_text(encoding="utf8").split("\n")
    malos = []

    def tabla_desde(marca: str) -> int:
        i = next(k for k, ln in enumerate(L) if ln.strip().startswith(marca))
        return next(k for k in range(i, len(L)) if L[k].startswith("|"))

    def poner(k: int, idx: int, s: dict):
        c = _celdas(L[k])
        if c[idx] != s["texto_anterior"]:
            malos.append(f"{s['seccion']} / {s['fila']} / {s['columna']}: v2 dice {c[idx]}, valor anterior {s['texto_anterior']}")
        c[idx] = s["texto_nuevo"]
        L[k] = _linea(c)

    por = lambda sec: [s for s in S if s["seccion"] == sec]  # noqa: E731
    for marca, sec in (("**(b) Puntos del SBC", "Cuadro X.1 (b)"), ("**(c) Porcentaje de los ingresos del SEM", "Cuadro X.1 (c)")):
        k0 = tabla_desde(marca)
        filas = {_celdas(L[k])[0]: k for k in range(k0, k0 + 12) if L[k].startswith("|")}
        for s in por(sec):
            poner(filas[s["fila"]], 1 + COLS_X1.index(s["columna"]), s)
    k0 = tabla_desde("## X.5")
    k = next(j for j in range(k0, k0 + 8) if L[j].startswith("| Efecto neto (pts SBC)"))
    cols = ["2030 D2", "2030 vigente", "2040 D2", "2040 vigente", "2054 D2", "2054 vigente"]
    for s in por("X.5"):
        poner(k, 1 + cols.index(s["columna"]), s)
    k0 = tabla_desde("## X.6")
    for s in por("X.6"):
        k = next(j for j in range(k0, k0 + 5) if _celdas(L[j])[0] == s["fila"])
        poner(k, 1 + ["2030", "2040", "2054"].index(s["columna"]), s)
    k0 = tabla_desde("**Cuadro X.2.")
    filas = {_celdas(L[k])[0]: k for k in range(k0, k0 + 26) if L[k].startswith("|")}
    for s in por("Cuadro X.2"):
        poner(filas[s["fila"]], 2 if "2030" in s["columna"] else 3, s)
    # textos
    txt = "\n".join(L)
    a, b = por("X.4 texto")
    old_s = f"{a['texto_anterior']} puntos del SBC y {b['texto_anterior']} % de los ingresos del SEM"
    if old_s not in txt:
        malos.append(f"X.4 texto: no se encontró «{old_s}»")
    txt = txt.replace(old_s, f"{a['texto_nuevo']} puntos del SBC y {b['texto_nuevo']} % de los ingresos del SEM")
    (c,) = por("X.7 texto")
    old_s = f"llega a {c['texto_anterior']} puntos del SBC"
    if old_s not in txt:
        malos.append(f"X.7 texto: no se encontró «{old_s}»")
    txt = txt.replace(old_s, f"llega a {c['texto_nuevo']} puntos del SBC")
    if FRASE_DENOM_V2 not in txt:
        malos.append("X.3: no se encontró la oración del denominador")
    txt = txt.replace(FRASE_DENOM_V2, FRASE_DENOM_V3)
    return txt, malos


NUM = re.compile(r"−?\d[\d,]*(?:\.\d+)?")


def verificar(S: list[dict], v3: str) -> tuple[dict, list[str]]:
    v2 = V2.read_text(encoding="utf8")
    reg = json.loads(NUMBERS_JSON.read_text())
    l2, l3 = v2.split("\n"), v3.split("\n")
    nuevos = {s["texto_nuevo"] for s in S} | {s["texto_anterior"] for s in S}
    fuera, montos = 0, 0
    for a, b in zip(l2, l3):
        if a == b:
            continue
        if FRASE_DENOM_V2 in a:
            continue
        ta, tb = NUM.split(a), NUM.split(b)
        na, nb = NUM.findall(a), NUM.findall(b)
        if ta != tb or len(na) != len(nb):
            fuera += 1
            continue
        for x, y in zip(na, nb):
            if x != y and not (x in nuevos and y in nuevos):
                montos += 1
    # 3.2: el texto nuevo coincide con el registro (dentro del redondeo del registro)
    no_reg, viejas = [], 0
    for s in S:
        v = reg.get(s["clave"], {}).get("valor")
        if v is None:
            no_reg.append(s["clave"])
            continue
        v = abs(v) if s["abs"] else v
        if abs(float(s["texto_nuevo"].replace("−", "-")) - v) > 0.5 * 10 ** -s["dec"] + 0.0005:
            no_reg.append(s["clave"])
    cambian = [s for s in S if s["texto_anterior"] != s["texto_nuevo"]]
    c186 = set(pd.read_csv(CAMBIOS).clave) if CAMBIOS.exists() else set()
    claves = {s["clave"] for s in cambian}
    chk = {"3.1 montos en mdp que cambian (v2 → v3)": montos,
           "3.2 cifras sustituidas sin registro o con valor distinto en NUMBERS.md": len(no_reg),
           "3.3 cifras que cambian de texto": len(cambian),
           "3.3 claves distintas entre ellas": len(claves),
           "3.3 de ellas, entre las 186 de exp1_cambios_denominador.csv": len(claves & c186),
           "3.3 de ellas, registradas en la v1.3 (columnas C2 y años sin clave previa del Cuadro X.1)": len(claves - c186),
           "3.4 líneas que cambian fuera de cifras y de la oración del denominador": fuera,
           "3.5 apariciones de 2055 en el borrador v3 fuera de la oración del v2 que dice que no se reporta":
               len(re.findall(r"(?<!\d)2055(?!\d)", v3.replace(ORACION_2055, "")))}
    return chk, no_reg


def main():
    S = sustituciones()
    v3, malos = construir(S)
    V3.write_text(v3, encoding="utf8")
    t = pd.DataFrame([{k: s[k] for k in ("clave", "texto_anterior", "texto_nuevo", "seccion", "fila", "columna")} for s in S])
    t["cambia"] = t.texto_anterior != t.texto_nuevo
    table(t, "exp1_borrador_v2_a_v3")
    chk, no_reg = verificar(S, v3)
    chk["mapeo: celdas del v2 que no coinciden con el valor anterior"] = len(malos)
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk13_{i}", v, k)
    record("v13_cifras_en_borrador", len(S), "Cifras en puntos o % del SEM del borrador (sustituibles)")
    (PROJECT / "data" / "derived" / "checks_v13.json").write_text(json.dumps({**chk, "mapeo_detalle": malos, "sin_registro": no_reg},
                                                                            ensure_ascii=False, indent=1))
    print(json.dumps({**chk, "mapeo_detalle": malos[:5], "sin_registro": no_reg[:5]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

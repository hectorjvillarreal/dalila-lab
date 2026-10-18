"""Verificaciones del texto de la sección 10 (instrucción 20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.0):
extensión (8.1), cifras con respaldo (8.2), expresiones prohibidas (8.4), años (8.5), legibilidad (8.6), apartados (8.7),
frases obligatorias (8.8) y términos definidos (8.9). Escribe tablas/seccion10_cifras.csv y data/verificaciones.json."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parents[1]
MD = AQUI / "N13_seccion10_esquemas_financiamiento_v1.md"
E1 = AQUI.parent / "e_1_imss_subsidiado" / "anexo_afiliacion_subsidiada"
E2 = AQUI.parent / "e_2_imss_nuevoseguro"
APARTADOS = ["El problema", "La idea", "Supuestos", "Resultados", "Qué tan robusto es", "Lo que el ejercicio no dice", "En resumen"]
CUARTILLA = 1800

PROHIBIDAS = {
    "Incidencia": ["costo para el patrón", "costo laboral", "costo de la formalidad", "abarata", "más barato contratar",
                   "subsidio cruzado entre patrones", "quién paga en realidad", "lo pagan los trabajadores"],
    "Sostenibilidad": ["sostenible", "insostenible", "se autofinancia", "cubre su costo"],
    "Autoría": ["propuesta del IMSS", "propuesta del Gobierno"],
    "Causalidad": ["aumentará la formalidad", "incentiva la formalización", "incentiva la formalidad", "aumenta la formalidad"],
    "Supuestos": ["estimación ilustrativa", "se estima que la adopción", "estimamos"],
    "Interno": ["Claude", "agente", "Debb", "v1.3", "v1.2", "K1", "K2", "M2", "M3", "D2", "Dalila", "/home/", ".csv", ".py"],
}
# «proyección del IMSS» solo se permite para el supuesto («la proyección del IMSS supone…», «formalización de la proyección del IMSS»)
PROY_OK = re.compile(r"(formalizaci[oó]n (que supone|de) la proyecci[oó]n del IMSS|(la )?que supone la proyecci[oó]n del IMSS|la proyecci[oó]n del IMSS supone|no (es|son) (una )?proyecci[oó]n(es)? del IMSS|mismo horizonte que la proyecci[oó]n del IMSS)", re.I)
FRASE1 = ("Con una reserva que se acumula hasta 2034, el 2 % alcanza para pagar el déficit de gastos médicos de pensionados en todo "
          "el periodo 2027-2054, tanto con la formalización que supone la proyección del IMSS como con la mitad de ella. "
          "Si la formalidad se queda como está hoy, alcanza hasta 2037.")
FRASE2 = ("La reserva no crea recursos: cambia cuándo y para qué se usan. En cada escenario, lo que se destina a cuidados más lo "
          "que queda en la reserva, menos lo que falta para GMP, vale lo mismo con reserva y sin ella.")
TERMINOS = {"UMA": r"La UMA \(Unidad de Medida y Actualización\)", "SBC": r"salario base de cotización \(SBC\)",
            "cuota fija": r"cuota fija por trabajador igual a", "GMP": r"gastos médicos de pensionados \(GMP\)",
            "cuña contributiva legal": r"La cuña contributiva legal es", "valor presente": r"El valor presente suma",
            "provisiones": r"provisiones \(montos que el IMSS separa"}
TERM_BUSCA = {"UMA": r"\bUMA\b", "SBC": r"\bSBC\b|salario base de cotización", "cuota fija": r"cuota fija",
              "GMP": r"\bGMP\b", "cuña contributiva legal": r"cuña contributiva legal|cuña legal", "valor presente": r"valor presente",
              "provisiones": r"provisiones"}


def secciones(txt: str) -> dict:
    i_a, i_b = txt.index("\n## 10a. "), txt.index("\n## 10b. ")
    return {"intro": txt[:i_a], "10a": txt[i_a:i_b], "10b": txt[i_b:]}


def texto_corrido(t: str) -> str:
    out = []
    for ln in t.split("\n"):
        s = ln.strip()
        if not s or s.startswith(("|", "#", "![", "**Figura", "**Tabla", "*Fuente")):
            continue
        out.append(s)
    return "\n".join(out)


def limpio(t: str) -> str:
    t = re.sub(r"\[REVISAR[^\]]*\]", "", t)
    t = re.sub(r"[*_`]", "", t)
    return re.sub(r"^- ", "", t, flags=re.M)


def oraciones(t: str) -> list[str]:
    t = limpio(t).replace("\n", " ")
    partes = re.split(r"(?<=[.!?:;])\s+(?=[A-ZÁÉÍÓÚÑ¿¡0-9])", t)
    return [p.strip() for p in partes if len(p.split()) >= 2]


def silabas(palabra: str) -> int:
    w = palabra.lower()
    w = re.sub(r"[^a-záéíóúüñ]", "", w)
    if not w:
        return 0
    fuertes, debiles_tilde = "aeoáéó", "íú"
    n, prev = 0, ""
    for ch in w:
        if ch in "aeiouáéíóúü":
            if prev and prev in "aeiouáéíóúü":
                # hiato: dos fuertes, o débil acentuada
                if (prev in fuertes and ch in fuertes) or ch in debiles_tilde or prev in debiles_tilde:
                    n += 1
            else:
                n += 1
        prev = ch
    return max(n, 1)


def legibilidad(t: str) -> dict:
    ors = oraciones(t)
    palabras = [w for o in ors for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", o)]
    nw = len(palabras)
    ns = sum(silabas(w) for w in palabras)
    largos = [len(re.findall(r"\S+", o)) for o in ors]
    return {"oraciones": len(ors), "palabras": nw, "promedio_palabras_por_oracion": round(sum(largos) / len(largos), 1),
            "oracion_mas_larga": max(largos), "oraciones_mas_de_40": sum(x > 40 for x in largos),
            "fernandez_huerta": round(206.84 - 0.60 * (ns / nw * 100) - 1.02 * (len(ors) / nw * 100), 1)}


def registro() -> list[tuple[str, str, float]]:
    """(experimento, clave, valor) de los dos registros, más las cifras de las tablas de cifras semilla."""
    out = []
    for exp, base in (("1", E1), ("2", E2)):
        reg = json.loads((base / "data" / "derived" / "numbers_computed.json").read_text())
        out += [(exp, k, float(v["valor"])) for k, v in reg.items() if isinstance(v["valor"], (int, float))]
        num = (base / "NUMBERS.md").read_text(encoding="utf8")
        for ln in num.split("\n"):
            if ln.startswith("| ") and not ln.startswith("| Clave"):
                k = ln.split("|")[1].strip()
                for tok in re.findall(r"(?<![\w.])-?\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.])-?\d+(?:\.\d+)?", ln):
                    out.append((exp, f"semilla:{k}", float(tok.replace(",", ""))))
    return out


NUM = re.compile(r"(?<![\w.−-])−?\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.−-])−?\d+(?:\.\d+)?")


def _valor(exp: str, clave: str, regs: dict, textos: dict, cfg: dict):
    """Valor de la clave y si está respaldado: json del experimento, cifra semilla de NUMBERS.md o parámetro de config.yaml."""
    if clave.startswith(("semilla:", "config:")):
        lit = clave.split("=")[-1].strip()
        v = float(lit)
        fuente = textos[exp] if clave.startswith("semilla:") else cfg[exp]
        nombre = clave.split(":")[1].split("=")[0].split(" ")[0]
        ok = (nombre.split(".")[-1] in fuente) and any(f in fuente.replace(",", "") for f in (lit, lit.rstrip("0").rstrip("."), lit.lstrip("-")))
        return v, ok
    v = regs[exp].get(clave, {}).get("valor")
    return (float(v), True) if isinstance(v, (int, float)) else (None, False)


def cifras(txt: str) -> tuple[pd.DataFrame, list]:
    from cifras_mapa import MAPA
    regs = {e: json.loads((b / "data" / "derived" / "numbers_computed.json").read_text()) for e, b in (("1", E1), ("2", E2))}
    textos = {e: (b / "NUMBERS.md").read_text(encoding="utf8") for e, b in (("1", E1), ("2", E2))}
    cfg = {e: (b / "config.yaml").read_text(encoding="utf8") for e, b in (("1", E1), ("2", E2))}
    filas, sin = [], []
    for sec, t in secciones(txt).items():
        for n_ln, ln in enumerate(t.split("\n"), 1):
            s = ln.strip()
            if not s or s.startswith(("#", "![")):
                continue
            s2 = re.sub(r"\[REVISAR[^\]]*\]", "", s)   # las marcas de revisión no son cifras de la sección
            s2 = re.sub(r"(sección|secciones|Figura|Tabla|Cuadro|Anexo|percentil|P)\s*[\dA-Z.]+(?:\s+y\s+[\d.]+)?", "", s2)
            s2 = re.sub(r"\b10[ab]\.\d\b|\b10[ab]\b|Cuadro [IVXA]+\.\d+", "", s2)
            s2 = re.sub(r"\b\d{4}-\d{4}\b", "", s2)
            s2 = re.sub(r"\b\d+ (a \d+ )?años\b|\bde \d+ a \d+\b|cada 100 pesos|\b\d+ y \d+ años", "", s2)
            for tok in NUM.findall(s2):
                v = float(tok.replace(",", "").replace("−", "-"))
                if "." not in tok and 1990 <= abs(v) <= 2060:
                    continue
                ents = [m for m in MAPA if m[0] == sec and m[1] == tok]
                ent = next((m for m in ents if m[2] and re.search(m[2], s)), None) or next((m for m in ents if not m[2]), None)
                if not ent:
                    sin.append((sec, n_ln, tok, "sin entrada en el mapa", s[:80]))
                    continue
                _, _, _, exp, clave, fac, dec = ent
                val, ok = _valor(exp, clave, regs, textos, cfg)
                red = None if val is None else (round((val - 1) * 100, dec) if fac == "sobrecosto" else round(val * fac, dec))
                coincide = ok and red is not None and abs(red - v) < 1e-9
                if not coincide:
                    sin.append((sec, n_ln, tok, f"{clave}: {red} ({'respaldada' if ok else 'sin respaldo'})", s[:80]))
                filas.append({"experimento": exp, "clave_NUMBERS": clave, "valor_exacto": val, "factor": fac,
                              "valor_redondeado": tok, "ubicacion": f"texto {sec}, línea {n_ln}", "coincide": coincide,
                              "fuente": "config.yaml" if clave.startswith("config:") else "NUMBERS.md"})
    # cifras impresas en las figuras
    fig = AQUI / "figuras"
    a = pd.read_csv(fig / "F10a_2_asequibilidad.csv")
    for _, r in a.iterrows():
        for col, k in (("pct_ingreso_laboral_D2_G2", "D2_G2"), ("pct_ingreso_laboral_D1_G1", "D1_G1")):
            clave = f"aseq_p{int(r.percentil)}_pctlab_{k}"
            val = regs["1"].get(clave, {}).get("valor")
            ok = val is not None and round(float(val), 1) == round(float(r[col]), 1)
            filas.append({"experimento": "1", "clave_NUMBERS": clave, "valor_exacto": val, "factor": 1, "valor_redondeado": f"{r[col]:.1f}",
                          "ubicacion": "Figura 10.2", "coincide": ok, "fuente": "NUMBERS.md"})
            if not ok:
                sin.append(("F10a.2", 0, f"{r[col]:.1f}", clave, ""))
    d = pd.read_csv(fig / "F10a_3_saldo_SEM.csv")
    for _, r in d.iterrows():
        clave = f"v12b_Total_saldo_pts_{int(r.anio)}"
        val = regs["1"].get(clave, {}).get("valor")
        ok = val is not None and round(float(val), 1) == round(float(r.saldo), 1)
        filas.append({"experimento": "1", "clave_NUMBERS": clave, "valor_exacto": val, "factor": 1, "valor_redondeado": f"{r.saldo:.1f}",
                      "ubicacion": "Figura 10.3", "coincide": ok, "fuente": "NUMBERS.md"})
        if not ok:
            sin.append(("F10a.3", 0, f"{r.saldo:.1f}", clave, ""))
    b = pd.read_csv(fig / "F10a_4_formalizacion.csv")
    for _, r in b.iterrows():
        clave = f"v12_C_{r.cuota}_neto_{int(r.anio)}"
        val = regs["1"].get(clave, {}).get("valor")
        ok = val is not None and round(float(val) / 1000) == round(float(r.efecto_neto_SEM) / 1000)
        filas.append({"experimento": "1", "clave_NUMBERS": clave, "valor_exacto": val, "factor": MMIL, "valor_redondeado": f"{r.efecto_neto_SEM / 1000:.0f}",
                      "ubicacion": "Figura 10.4", "coincide": ok, "fuente": "NUMBERS.md"})
        if not ok:
            sin.append(("F10a.4", 0, f"{r.efecto_neto_SEM / 1000:.0f}", clave, ""))
    return pd.DataFrame(filas), sin


MMIL = 1e-3


def main():
    txt = MD.read_text(encoding="utf8")
    sec = secciones(txt)
    chk = {}
    # 8.1 extensión
    for k, t in sec.items():
        c = texto_corrido(t)
        chk[f"8.1 caracteres de texto corrido, {k}"] = len(limpio(c))
        chk[f"8.1 cuartillas de texto corrido, {k}"] = round(len(limpio(c)) / CUARTILLA, 2)
    # 8.4 prohibidas
    plano = limpio(txt)
    hits = []
    for g, lst in PROHIBIDAS.items():
        for e in lst:
            patron = r"\b" + re.escape(e) + r"\b" if re.match(r"\w", e) else re.escape(e)
            for m in re.finditer(patron, plano, flags=0 if g == "Interno" else re.I):
                hits.append((g, e, plano[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
    for m in re.finditer(r"proyecci[oó]n del IMSS", plano):
        ctx = plano[max(0, m.start() - 60):m.end() + 30]
        if not PROY_OK.search(ctx):
            hits.append(("Autoría", "proyección del IMSS", ctx.replace("\n", " ")))
    # gasto no contributivo: «alcanza» o «puede reasignarse» en el mismo párrafo
    for p in plano.split("\n"):
        if re.search(r"sin seguridad social fue|no contributiv", p) and re.search(r"alcanza|puede reasignarse", p):
            hits.append(("Gasto no contributivo", "alcanza / puede reasignarse", p[:120]))
    chk["8.4 expresiones prohibidas"] = len(hits)
    chk["8.4 marcas de revisión (se retiran al cerrar la redacción)"] = len(re.findall(r"\[REVISAR", txt))
    # 8.5 años después de 2054
    figtxt = "".join(p.read_text(encoding="utf8") for p in (AQUI / "figuras").glob("*.csv"))
    chk["8.5 años después de 2054 (texto y datos de figuras)"] = len(re.findall(r"(?<!\d)20(5[5-9]|[6-9]\d)(?!\d)", txt + figtxt))
    # 8.6 legibilidad
    for k in ("intro", "10a", "10b"):
        for kk, v in legibilidad(texto_corrido(sec[k])).items():
            chk[f"8.6 {kk}, {k}"] = v
    # 8.7 apartados
    for k in ("10a", "10b"):
        enc = re.findall(rf"^## {k}\.\d (.+)$", sec[k], flags=re.M)
        chk[f"8.7 apartados de {k} (esperados 7, en orden)"] = int(enc == APARTADOS)
    # 8.8 frases obligatorias y su coincidencia con el Cuadro X-2.3
    plano_frases = re.sub(r"[*]", "", txt).replace("\n", " ")
    chk["8.8 frase obligatoria 1 presente"] = int(FRASE1 in plano_frases)
    chk["8.8 frase obligatoria 2 presente"] = int(FRASE2 in plano_frases)
    sv = pd.read_csv(E2 / "tablas" / "sensibilidad_v13.csv").set_index(["regla", "escenario_masa"])
    col = "con provisiones, masa del libro"
    chk["8.8 cifras de la frase 1 = Cuadro X-2.3"] = int(sv.loc[("K2", "base"), col] == 2054 and sv.loc[("K2", "M3"), col] == 2054
                                                         and sv.loc[("K2", "M2"), col] == 2037)
    # 8.9 términos definidos en su primera aparición
    malos = []
    for t, d in TERMINOS.items():
        m_def = re.search(d, txt)
        m_1 = re.search(TERM_BUSCA[t], txt)
        if not m_def or (m_1 and m_1.start() < m_def.start() - 250):
            malos.append(t)
    chk["8.9 términos sin definir en su primera aparición"] = len(malos)
    # 8.2 cifras
    c, sin = cifras(txt)
    (AQUI / "tablas").mkdir(exist_ok=True)
    c.to_csv(AQUI / "tablas" / "seccion10_cifras.csv", index=False)
    chk["8.2 cifras registradas en seccion10_cifras.csv (texto, tablas y figuras)"] = len(c)
    chk["8.2 de ellas, respaldadas en NUMBERS.md"] = int(((c.fuente == "NUMBERS.md") & c.coincide).sum())
    chk["8.2 de ellas, parámetros del escenario en config.yaml (no están en NUMBERS.md)"] = int(((c.fuente == "config.yaml") & c.coincide).sum())
    chk["8.2/8.3 cifras sin respaldo o que no coinciden"] = len(sin)
    det = {"prohibidas": hits, "sin_respaldo": sin, "terminos_mal": malos}
    (AQUI / "data").mkdir(exist_ok=True)
    (AQUI / "data" / "verificaciones.json").write_text(json.dumps({"checks": chk, "detalle": det}, ensure_ascii=False, indent=1))
    return chk, det


if __name__ == "__main__":
    c, d = main()
    print(json.dumps(c, ensure_ascii=False, indent=1))
    print(json.dumps(d, ensure_ascii=False, indent=1)[:3000])

"""Figura del experimento 2 (base, M3 y M2), verificaciones 3.6/7.6 y 3.7, y NUMBERS.md (sección «Experimento 2»)."""

from __future__ import annotations

import json
import re

import matplotlib
import pandas as pd

from comun import DERIVED, FIGURAS, NUMBERS_JSON, PROJECT, TABLAS, record

from reporte import AZUL, GRIS, NARANJA, TINTA, TINTA2, _estilo   # estilo de las figuras del experimento 1

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

FUENTE = ("Ejercicio preliminar ITED; no es una proyección del IMSS ni una propuesta del IMSS o del Gobierno. "
          "Fuentes: Informe IMSS 2025-2026 (Cuadro V.24); libro de Finanzas 07/09/2026; CONAPO; ENIGH 2024.")
ANEXO = "ANEXO_experimento2_borrador_v2.md"

# (clave, valor, fuente, estado) — instrucción, sección 6, más las cifras que la ejecución añadió
SEMILLA = [
    ("Infonavit_tasa", "5 % del SBC, tope 25 UMA", "Ley del Infonavit, art. 29; Informe, nota 176", "5 % confirmado en la nota 176; el tope se toma de la instrucción (la Ley no se consultó en esta corrida)"),
    ("NS_tasa", "2 % del SBC, tope 25 UMA", "Supuesto del experimento", "—"),
    ("GMP_V24_base", "Ingresos 89,499 / 104,369 / 119,537 / 142,886 / 169,522 / 197,734 / 217,061; saldo −68,398 / −97,760 / −134,117 / −138,282 / −157,934 / −180,930 / −203,895 (2026, 2031, …, 2051 y año final); VP 2,750,260 y −2,631,460", "Informe, Cuadro V.24 (base)", "confirmada celda por celda contra el PDF (verificación 3.2)"),
    ("GMP_V19", "Saldo −97,653 (2031) y −135,137 (2036) frente a −97,760 y −134,117 del V.24; VP gasto 5,388,234, ingresos 2,750,887, saldo −2,637,347", "Informe, Cuadro V.19", "nueva; los dos cuadros del escenario base no coinciden exactamente"),
    ("GMP_V20", "Aportaciones futuras 2,647,226 (1.50 % del VPSF); otros ingresos 103,662; reserva 46,532; prima de equilibrio 3.05 %", "Informe, Cuadro V.20", "nueva"),
    ("GMP_prima_fin / eq", "1.5 % / 3.1 %", "Informe, Cuadro II.16", "confirmada (3.05 % en el Cuadro V.20)"),
    ("Vol_salarios_VP_SEM", "176,481,700 mdp de 2026", "Informe, Cuadro V.15 (base)", "confirmada"),
    ("SEM_ingresos_V13", "562,126 / 642,375 / 740,391 / 859,501 / 995,073 / 1,131,634 / 1,215,833 (2026, 2031, …, 2051 y año final); VP 16,456,453", "Informe, Cuadro V.13", "nueva; denominador de «% de los ingresos del SEM» (decisión de Héctor, 18-10)"),
    ("Tasa_descuento", "3 % real", "Informe, Cuadro II.16, nota 1", "confirmada"),
    ("DH_65mas_2025", "16.6 % de la población adscrita a médico familiar", "Informe, Gráfica I.31", "confirmada"),
    ("DH_total", "79,178,109", "Informe, Cuadro I.4", "confirmada"),
    ("PAMF_2025", "63,598,543 adscripciones a médico familiar (60,266,622 personas por CURP)", "Informe, texto del Cuadro I.4 y Gráfica I.23", "solo para la regresión v1.0; la v1.1 elimina esta base"),
    ("ENIGH_IMSS_65mas", "Tasa de afiliación al IMSS (poblacion.inst_1 = 1) por grupo quinquenal (65-69 … 85+) y sexo, ponderada con factor", "ENIGH 2024 (INEGI), tabla poblacion", "nueva (v1.1); base de personas mayores, × CONAPO por año; mismo método del experimento 1"),
    ("GMP_V19_provisiones", "123 / 9,971 / 19,577 / 541 / 540 / 542 / 545 mdp de 2026 (2026, 2031, …, 2051 y año final)", "Informe, Cuadro V.19, fila Provisiones", "nueva (v1.1); margen sin provisiones"),
    ("SM_2023 / UMA_2023", "207.44 pesos/día (resto del país) / 103.74 pesos/día (vigente desde el 1-02-2023): el SM equivale a 2.00 UMA", "DOF 07-12-2022, Resolución del Consejo de Representantes de la CONASAMI; DOF 10-01-2023, INEGI, valor de la UMA", "nueva (v1.1); el tramo «1.01 SM a 1.50 UMA» ya estaba vacío en 2023"),
    ("Vivienda_al_pensionarse", "71.45 % (base) / 57.45 % (riesgo); 83 % en 2026-2035, baja a 50 % al final del horizonte (base)", "Informe, Cuadro II.18 y nota 3", "confirmada"),
    ("CyV_patronal_2025_2026_2030", "Tabla de la sección 1.5 de la instrucción", "DOF 16-12-2020, Segundo Transitorio (tabla en imagen, leída) y art. 168 fr. II a) (texto); Informe, Cuadro A.3 nota 6 (2025)", "verificada en el DOF: coincide en todas las celdas"),
    ("Cuota_social_dic2025", "1 SM 12.18; 1.01 SM-1.50 UMA 11.33; 1.51-2 10.48; 2.01-2.5 9.63; 2.51-3 8.78; 3.01-3.5 7.93; 3.51-4 7.08 pesos por día", "Informe, Cuadro A.3, nota 8", "nueva; se mantiene constante en UMA reales (se indexa al INPC)"),
    ("c_D2", "3.467 % (0.0346703)", "Corrida v1.2", "confirmada"),
    ("SBC_prom_dic2025", "5.55 veces la UMA (627.87 pesos/día)", "Informe, sección I.1.3", "confirmada en la v1.2; nivel «promedio» de la tabla de cuña"),
    ("Patronales SEM, SIV, SGPS, Retiro", "Cuota fija 20.40 % UMA; excedente 1.10 %; prestaciones en dinero 0.70 %; GMP 1.05 %; IV 1.75 %; GPS 1.00 %; Retiro 2.00 %", "Informe, Cuadro A.3; libro, hoja `Tasas de Contribución`", "confirmada"),
    ("RT_prima_promedio", "1.9078 % en el Cuadro X-2.2; 1.80 % en las proyecciones de masa e ingreso", "Informe, Cuadro A.3, nota 1 (vigencia mar. 2025-feb. 2026); libro, hoja `Tasas de Contribución`, nota 2 (promedio 2023-2025)", "v1.1: el cuadro de cuña usa 1.9078 %; la regresión v1.0 usa 1.80 %"),
    ("Obreras y federales", "Obrera: excedente 0.40, PD 0.25, GMP 0.375, IV 0.625, CyV 1.125; federal: cuota fija 14.83 % UMA, PD 0.05, GMP 0.075, IV 0.125", "Informe, Cuadro A.3", "nueva"),
    ("Art_36_LSS", "«Corresponde al patrón pagar íntegramente la cuota señalada para los trabajadores, en los casos en que éstos perciban como cuota diaria el salario mínimo.»", "Ley del Seguro Social, art. 36, texto vigente publicado por la Cámara de Diputados (última reforma DOF 15-01-2026)", "verificada (v1.1); coincide con la redacción citada"),
    ("Criterio_SUA_1.01SM", "No encontrado", "Búsqueda en documentación pública del IMSS y del DOF (18-10-2026); la página del SUA requiere sesión", "pendiente de confirmación con el IMSS (visita de Juan Pablo)"),
    ("Infonavit_recaudacion_efectiva", "No obtenida", "Estados financieros del Infonavit 2024-2025", "omitida, como manda la instrucción"),
]


def figura():
    d = pd.read_parquet(DERIVED / "ingreso_vs_GMP.parquet")
    reg = json.loads(NUMBERS_JSON.read_text())
    escs = [e for e in ("base", "M3", "M2") if e in set(d.escenario_masa)]
    titulos = {"base": "Base (formalización institucional)", "M3": "M3 (mitad de la formalización)", "M2": "M2 (formalidad constante)"}
    FIGURAS.mkdir(parents=True, exist_ok=True)
    fig, axs = plt.subplots(1, len(escs), figsize=(12, 4.6), sharey=True)
    ymax = float(d[["ingreso_NS", "deficit_GMP"]].max().max()) / 1000 * 1.06
    for ax, e in zip(axs, escs):
        x = d[d.escenario_masa == e].set_index("anio")
        t, i, dd = x.index, x.ingreso_NS / 1000, x.deficit_GMP / 1000
        ax.fill_between(t, dd, i, where=i >= dd, color=AZUL, alpha=0.15, lw=0, interpolate=True)
        ax.fill_between(t, dd, i, where=i < dd, color=NARANJA, alpha=0.25, lw=0, interpolate=True)
        ax.plot(t, i, color=AZUL, lw=2.2, label="Ingreso del nuevo seguro (2 %)")
        ax.plot(t, dd, color=TINTA, lw=1.8, label="Déficit de GMP")
        p = reg[f"{e}_k1_primer_anio_no_cubre"]["valor"]
        sub = "cubre todo el horizonte" if p == "ninguno" else f"sin cobertura desde {p}"
        ax.set_title(f"{titulos[e]}\n{sub}", fontsize=9.5, color=TINTA, loc="left")
        ax.set_xticks([2027, 2035, 2045, 2054])   # 2055 no se reporta (3.6)
        ax.set_xlim(2027, 2054)
        ax.set_ylim(0, ymax)
        _estilo(ax)
        ax.grid(axis="y", color="#ebeae6", lw=0.8)
    axs[0].set_ylabel("Miles de millones de pesos de 2026", fontsize=8, color=TINTA2)
    axs[0].legend(fontsize=7.5, frameon=False, loc="upper left")
    fig.text(0.01, 0.01, FUENTE + "\nAzul: remanente para cuidados (K1); naranja: déficit no cubierto. El déficit de M3 y M2 incluye "
             "la menor recaudación de GMP con menos cotizantes.", fontsize=6.5, color=TINTA2)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(FIGURAS / "ingreso_vs_GMP.png", dpi=160)
    plt.close(fig)


def sin_2055() -> int:
    """3.6: ninguna celda ni encabezado de las tablas contiene 2055."""
    n = 0
    for f in TABLAS.glob("*.csv"):
        txt = f.read_text(encoding="utf8")
        n += len(re.findall(r"(?<![\d.])2055(?![\d])", txt))
    return n


def numbers_md():
    reg = json.loads(NUMBERS_JSON.read_text())
    L = ["# NUMBERS — Experimento 2", "",
         "Registro de cifras del experimento 2 del anexo del Núcleo 13 (cuota del Infonavit a un nuevo seguro solidario de salud y cuidados en la vejez).",
         "Regla 3.7: ninguna cifra aparece en el borrador del anexo si no está en este registro. Ejercicio de análisis de ITED; no es una proyección ni una propuesta del IMSS o del Gobierno.",
         "Montos en millones de pesos de 2026 (mdp) salvo indicación. «Puntos del salario» = % de la masa salarial con tope de 25 UMA y 337 días.", "",
         "## Experimento 2 — 1. Cifras semilla (instrucción, sección 6)", "",
         "| Clave | Valor | Fuente | Estado |", "|---|---|---|---|"]
    L += [f"| {k} | {v} | {s} | {e} |" for k, v, s, e in SEMILLA]
    L += ["", "## Experimento 2 — 2. Cifras calculadas (generadas por `src/`, archivo `data/derived/numbers_computed.json`)", "",
          "| Clave | Valor | Fuente / cálculo |", "|---|---|---|"]
    for k in sorted(reg):
        v = reg[k]["valor"]
        vs = f"{v:,.6f}".rstrip("0").rstrip(".") if isinstance(v, float) else (f"{v:,}" if isinstance(v, int) else str(v))
        L.append(f"| {k} | {vs} | {reg[k]['fuente']} |")
    (PROJECT / "NUMBERS.md").write_text("\n".join(L) + "\n", encoding="utf8")


NUM = re.compile(r"(?<![\w.-])\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.-])\d+(?:\.\d+)?")
NUM_REG = re.compile(r"(?<![\w.])-?\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.])-?\d+(?:\.\d+)?")   # el registro escribe negativos con «-»
NO_CIFRA = {"97"}   # «Ley 97»


def cifras_sin_registro() -> list[str]:
    """3.7: cifras del borrador del anexo que no aparecen en NUMBERS.md (salvo redondeo o expresión en %).
    Se omiten años, enteros de hasta 30 (numerales, parámetros de diseño como 5 %, 2 %, 25 UMA) y nombres como «Ley 97»."""
    anexo = PROJECT / ANEXO
    if not anexo.exists():
        return ["(falta el borrador)"]
    reg = [float(t.replace(",", "")) for t in NUM_REG.findall((PROJECT / "NUMBERS.md").read_text(encoding="utf8"))]
    cand = reg + [v * 100 for v in reg]
    faltan = []
    for tok in NUM.findall(anexo.read_text(encoding="utf8")):
        v = float(tok.replace(",", ""))
        if tok in NO_CIFRA or "." not in tok and (abs(v) <= 30 or 1990 <= v <= 2070):
            continue
        dec = len(tok.split(".")[1]) if "." in tok else 0
        if not any(round(abs(c), dec) == abs(v) for c in cand):
            faltan.append(tok)
    return sorted(set(faltan))


def main():
    figura()
    n = sin_2055()
    record("chk_3.6", n, "3.6/7.6 apariciones de 2055 en las tablas")
    numbers_md()
    faltan = cifras_sin_registro()
    return {"3.6/7.6 apariciones de 2055 en las tablas": n, "3.7/7.6 cifras del borrador v2 sin registro en NUMBERS.md": len(faltan),
            "3.7 detalle": ", ".join(faltan)}


if __name__ == "__main__":
    print(main())

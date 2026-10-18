"""Escribe NUMBERS.md: cifras semilla confirmadas en las fuentes y cifras calculadas por el pipeline."""

from __future__ import annotations

import json

from common import NUMBERS_JSON, PROJECT

# (clave, valor, fuente, página del PDF del Informe o ubicación en el libro, estado)
SEMILLA = [
    ("UMA_dic2025", "113.14 pesos/día", "Informe, Cuadro A.3, nota 2; libro, hoja `Tasas de Contribución`, nota 3", "pág. PDF 250", "confirmada"),
    ("UMA_2024", "108.57 pesos/día", "Informe, Cuadro I.2, nota 1 (UMA vigente en el levantamiento de la ENIGH)", "pág. PDF 26", "nueva; confirmada"),
    ("CF_patron", "20.40 % UMA", "Informe, Cuadro A.3", "pág. PDF 250", "confirmada"),
    ("CF_GF", "14.83 % UMA (16.78 pesos/día, dic. 2025)", "Informe, Cuadro A.3, nota 3", "pág. PDF 250", "confirmada"),
    ("CF_total", "35.23 % UMA", "Informe, Cuadro A.3", "pág. PDF 250", "confirmada"),
    ("Excedente", "1.10 % patrón + 0.40 % trabajador sobre (SBC − 3 UMA)", "Informe, Cuadro A.3", "pág. PDF 250", "confirmada"),
    ("Prest_dinero", "0.70 / 0.25 / 0.05 % SBC", "Informe, Cuadro A.3", "pág. PDF 250", "confirmada"),
    ("GMP", "1.05 / 0.375 / 0.075 % SBC (total 1.50)", "Informe, Cuadro A.3", "pág. PDF 250", "confirmada"),
    ("Tasa_efectiva_SEM", "9.60 % SBC (patrón 5.97, trabajador 0.82, GF 2.81)", "Informe, Cuadro A.4", "pág. PDF 251", "confirmada"),
    ("Tasa_efectiva_SEM-A", "8.10 % SBC (4.92 / 0.44 / 2.74)", "Informe, Cuadro A.4", "pág. PDF 251", "confirmada"),
    ("Prima_eq_SEM / Prima_fin_SEM", "12.94 % / 8.9 % SBC (2026-2055)", "Informe, texto del Cuadro V.13 y Cuadro V.14 (8.93)", "págs. PDF 141-142", "confirmada"),
    ("Prima_eq / fin SEM-A", "9.9 % / 7.4 %", "Informe, Cuadro II.16 (fila Asegurados)", "pág. PDF 71", "confirmada"),
    ("Prima_eq / fin GMP", "3.1 % / 1.5 %", "Informe, Cuadro II.16 (fila Pensionados)", "pág. PDF 71", "confirmada"),
    ("SBC_prom_dic2025", "627.87 pesos/día (5.55 veces la UMA; 5.41 en 2024)", "Informe, sección I.1.3", "pág. PDF 23", "confirmada"),
    ("SBC_crec_UMA_2025", "+2.6 % (de 5.41 a 5.55 veces la UMA)", "Informe, sección I.1.3", "pág. PDF 23", "nueva; confirmada"),
    ("SM_2025", "278.80 pesos/día (zona general)", "Informe, sección I.1.3", "pág. PDF 23", "confirmada"),
    ("Dias_cotizados", "337 (base) / 324 (riesgo)", "Informe, Cuadro II.18", "pág. PDF 73", "confirmada"),
    ("Especie_SEM_2026", "494,275 mdp de 2026", "Informe, Cuadro V.13", "pág. PDF 141", "confirmada"),
    ("Crec_gasto_medico", "3.8 % real anual (2026-2055)", "Informe, Cuadro II.15", "pág. PDF 71", "confirmada"),
    ("SEM_resultado_2025", "−151,127 mdp corrientes; pensiones y jubilaciones 164,456", "Informe, Cuadro V.11", "págs. PDF 138-139", "confirmada"),
    ("SSFAM_2025", "Ingresos 3,724; gastos 21,674; resultado −17,950 mdp", "Informe, Cuadro VII.2", "pág. PDF 194", "confirmada"),
    ("SSFAM_cuotas", "8,900 a 21,300 pesos (2025); 9,300 a 22,150 (2026), por persona según edad", "Informe, Cuadro A.5", "pág. PDF 251", "confirmada"),
    ("PIB_2026", "38,715,900 mdp", "Informe, nota 51 (CGPE 2026)", "pág. PDF 71", "confirmada"),
    ("DH_total", "79,178,109 (titulares 38,197,323; familiares 40,980,786), cierre 2025", "Informe, Cuadro I.4 («casi 80 millones», Introducción, pág. PDF 14)", "pág. PDF 33", "cifra exacta extraída"),
    ("Ingresos_2025_Informe", "Cuotas 625,443; GF 158,947; otros 46,643; total 831,033 mdp de 2026", "Informe, Cuadro II.14", "pág. PDF 67", "confirmada"),
    ("Aseg_dic2025 / TIMSS_dic2025", "21,800,692 / 551,894", "Libro 07/09, matrices dic25 y `Pob Emp & Nuevos`", "—", "confirmada"),
    ("SBC_ponderado_libro", "627.21 pesos/día", "Cálculo propio: `Sal SEM-Emp_dic25` × `Mat_Aseg SEM_dic25`", "—", "confirmada (627.2063)"),
    ("GF_SEM-A_2025", "146,457 mdp de 2026", "Libro, hoja `Ingresos IMSS`", "—", "confirmada (146,457.28)"),
    ("Ingresos_2025_libro", "Cuotas 634,265; GF 157,892; otros 59,154; total 851,311", "Libro, hoja `Ingresos IMSS`, Consolidado", "—", "confirmada"),
    ("Nuevos_2054 / Nuevos_2055", "1.525 / 0.695 millones", "Libro, hoja `Pob Emp & Nuevos`", "—", "confirmada (1,525,376 / 695,451)"),
    ("Cotizantes_2054", "46.8 millones", "Libro, hoja `Pob Emp & Nuevos`", "—", "confirmada (46,801,970)"),
    ("SM_real", "+8.97 % (2026); +7.97, 7.99, 7.92, 7.92 % (2027-2030); +0.5 % después", "Libro, hoja `Sup_Fin`", "—", "confirmada"),
    ("Inflacion_2026", "3.70 %", "Libro, hoja `Sup_Fin`", "—", "confirmada"),
    ("SM_2024", "248.93 pesos/día (resto del país); 374.89 en la Zona Libre de la Frontera Norte", "Resolución del H. Consejo de Representantes de la CONASAMI, DOF 12/12/2023 (dof.gob.mx, nota 5711066)", "—", "nueva (v1.2); verificada en el DOF"),
    ("h_b_Informe", "1.0729 = 40,980,786 familiares / 38,197,323 titulares", "Informe, Cuadro I.4 (los titulares incluyen pensionados y Seguro Facultativo)", "pág. PDF 33", "nueva (v1.2)"),
    ("Ocupacion_hospitalaria_2025", "75.7 % segundo nivel; 83.7 % tercer nivel", "Informe, texto de capacidad hospitalaria", "pág. PDF 115", "nueva (v1.2)"),
    ("PEF2026_salud_no_contributivo", "SSa 68,964.2; IMSS-Bienestar 177,591.9; FASSA 87,344.2; Bienestar 4,128.0; total 338,028.3 mdp de 2027", "CIEP, «PPEF 2027: Gasto en salud por subsistema», Cuadro 1 (cifras del PEF 2026; proporcionado por Héctor el 08-10-2026)", "—", "nueva (v1.2); solo contexto"),
    ("Inflacion_2027", "3.82 %", "Libro, hoja `Sup_Fin`", "—", "nueva (v1.2)"),
    ("N13_DH_2025", "70.69 millones", "Informe del Núcleo 13, Anexo I, Tabla I.1", "—", "referencia de contraste"),
    ("Ingresos_SEM_V13", "562,126 / 642,375 / 740,391 / 859,501 / 995,073 / 1,131,634 / 1,215,833 mdp de 2026 (2026, 2031, …, 2051 y año final), interpolación lineal", "Informe, Cuadro V.13", "pág. PDF 141", "nueva (18-10); denominador de «% de los ingresos del SEM» de las salidas v1.2, común con el experimento 2 (decisión de Héctor)"),
    ("Denominador_puntos_v12", "Masa R1: cotizantes del libro × SBC R1 con tope de 25 UMA y piso en el SM × UMA × 337 días (la base de la tasa D2)", "Cálculo propio", "—", "nueva (18-10); denominador común con el experimento 2. El libro de Finanzas se sigue usando para cotizantes, salarios y supuestos, no para el denominador de ingresos del SEM. Las corridas v1.1 conservan sus denominadores"),
]


def main():
    reg = json.loads(NUMBERS_JSON.read_text())
    L = ["# NUMBERS — registro de cifras del anexo de afiliación subsidiada", "",
         "Regla 3.7: ninguna cifra aparece en el anexo si no está en este registro. Ejercicio preliminar de ITED; no es una proyección del IMSS.",
         "Páginas del Informe: numeración del PDF (`pdfinfo`: 338 páginas), no la impresa. Montos en pesos de 2026 salvo indicación.",
         "Las desagregaciones por seguro, la retención y el modelo de cohortes son **reconstrucciones propias**.", "",
         "## 1. Cifras semilla (instrucción, sección 8), confirmadas en I1 e I2", "",
         "| Clave | Valor | Fuente | Página | Estado |", "|---|---|---|---|---|"]
    L += [f"| {k} | {v} | {s} | {p} | {e} |" for k, v, s, p, e in SEMILLA]
    L += ["", "## 2. Cifras calculadas (generadas por `src/`, archivo `data/derived/numbers_computed.json`)", "",
          "| Clave | Valor | Fuente / cálculo |", "|---|---|---|"]
    for k in sorted(reg):
        v = reg[k]["valor"]
        vs = f"{v:,.4f}".rstrip("0").rstrip(".") if isinstance(v, float) else (f"{v:,}" if isinstance(v, int) else str(v))
        L.append(f"| {k} | {vs} | {reg[k]['fuente']} |")
    (PROJECT / "NUMBERS.md").write_text("\n".join(L) + "\n", encoding="utf8")


if __name__ == "__main__":
    main()

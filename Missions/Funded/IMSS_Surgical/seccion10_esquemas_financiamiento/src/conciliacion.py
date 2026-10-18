"""Conciliación de las cifras compartidas entre el informe del Núcleo 13 (documento de Juan Pablo) y los anexos de los
experimentos 1 y 2. Lee los registros `numbers_computed.json` y fija los valores del informe tal como aparecen en el
documento (tabla y página indicadas). Marca toda diferencia mayor a 1 %. Escribe `tablas/conciliacion_seccion10.csv`."""

from __future__ import annotations

import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
E1 = json.loads((RAIZ.parent / "e_1_imss_subsidiado/anexo_afiliacion_subsidiada/data/derived/numbers_computed.json").read_text())
E2 = json.loads((RAIZ.parent / "e_2_imss_nuevoseguro/data/derived/numbers_computed.json").read_text())


def v(reg, clave, factor=1.0):
    x = reg[clave]
    return (x["valor"] if isinstance(x, dict) else x) * factor


# (concepto, unidad, año, valor del informe, ubicación en el informe, valor de los anexos, fuente de los anexos, nota)
FILAS = [
    ("Derechohabientes IMSS", "millones", 2025, 70.69, "Anexo I, Tabla I.1",
     79.178109, "Informe al Ejecutivo 2025-2026, Cuadro I.4 (semilla DH_total)",
     "Fuentes distintas: el informe aplica tasas de la ENIGH a CONAPO; los anexos usan el registro administrativo [REVISAR-JP]"),
    ("Derechohabientes IMSS, mismo método que el Anexo I", "millones", 2025, 70.69, "Anexo I, Tabla I.1",
     v(E1, "ENIGH_IMSS_escalado_CONAPO_2025", 1e-6), "Experimento 1, ENIGH_IMSS_escalado_CONAPO_2025",
     "Réplica del método del Anexo I con la ENIGH 2024; no reproduce los 70.69 millones [REVISAR-JP]"),
    ("Cotizantes SEM", "millones", 2025, 22.35, "Anexo I, Tabla I.1",
     22.352586, "Libro de Finanzas, cotizantes dic. 2025 (Informe_DH_por_cotizante)", ""),
    ("Cotizantes SEM", "millones", 2030, 25.23, "Anexo I, Tabla I.1",
     v(E2, "cotizantes_2030", 1e-6), "Experimento 2, cotizantes_2030", ""),
    ("Cotizantes SEM", "millones", 2040, 33.88, "Anexo I, Tabla I.1",
     v(E2, "cotizantes_2040", 1e-6), "Experimento 2, cotizantes_2040", ""),
    ("Cotizantes SEM (informe 2055, anexos 2054)", "millones", 2054, 46.69, "Anexo I, Tabla I.1 (2055)",
     v(E2, "cotizantes_2054", 1e-6), "Experimento 2, cotizantes_2054",
     "Años distintos: el informe llega a 2055 y la sección 10 a 2054"),
    ("Ingresos del SEM, libro", "miles de millones de pesos de 2026", 2030, 611.2, "Tabla 5",
     v(E1, "ingreso_SEM_mdp_2030", 1e-3), "Experimento 1, ingreso_SEM_mdp_2030 (libro)", "Misma fuente"),
    ("Ingresos del SEM, libro frente a Cuadro V.13", "miles de millones de pesos de 2026", 2030, 611.2, "Tabla 5",
     v(E2, "SEM_ingresos_2030", 1e-3), "Informe al Ejecutivo, Cuadro V.13 (denominador común de la sección 10)",
     "La sección 10 expresa los saldos como % de los ingresos del Cuadro V.13, no del libro [REVISAR-JP]"),
    ("Ingresos del SEM, libro frente a Cuadro V.13", "miles de millones de pesos de 2026", 2040, 833.1, "Tabla 5",
     v(E2, "SEM_ingresos_2040", 1e-3), "Informe al Ejecutivo, Cuadro V.13", ""),
    ("Ingresos del SEM, libro (informe 2055, anexos 2054)", "miles de millones de pesos de 2026", 2054, 1215.3,
     "Tabla 5 (2055)", v(E2, "SEM_ingresos_libro_2054", 1e-3), "Experimento 2, SEM_ingresos_libro_2054",
     "Años distintos (2055 frente a 2054)"),
    ("Ingresos totales del IMSS", "miles de millones de pesos de 2026", 2025, 851.3, "Anexo M, Tabla M.2",
     851.311, "Experimento 1, NUMBERS.md semilla Ingresos_2025_libro", "Misma fuente"),
    ("Tasa efectiva del SEM", "% del SBC", 2026, 9.60, "Sección 2 (texto)",
     9.60, "Experimento 1, NUMBERS.md semilla Tasa_efectiva_SEM (Cuadro A.4)", ""),
    ("Prima de equilibrio del SEM", "% del SBC", 2026, 12.9, "Sección 2 (texto)",
     12.94, "Experimento 1, NUMBERS.md semilla Prima_eq_SEM (Cuadro V.13)", ""),
    ("Prima de financiamiento del SEM", "% del SBC", 2026, 8.9, "Sección 2 (texto)",
     8.93, "Experimento 1, NUMBERS.md semilla Prima_fin_SEM (Cuadro V.14)", ""),
    ("Gasto de bolsillo en salud por hogar", "pesos al año", 2024, 6421, "Sección 3 (texto, cita CIEP)",
     v(E1, "aseq_decil5_oop"), "Experimento 1, aseq_decil5_oop (ENIGH 2024, hogares objetivo, pesos de 2026)",
     "Conceptos distintos: promedio nacional de todos los hogares (pesos de 2024) frente a hogares sin seguridad "
     "social del decil V; no son comparables y la sección 10 no los mezcla"),
    ("Población de 65 años o más", "millones", 2025, None, "No se publica en el informe (reporta 60 años o más)",
     v(E2, "CONAPO_65mas_2025", 1e-6), "Experimento 2, CONAPO_65mas_2025", "Sin cifra del informe que conciliar"),
]


def main() -> None:
    sal = RAIZ / "tablas/conciliacion_seccion10.csv"
    with sal.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["concepto", "unidad", "anio", "valor_informe", "ubicacion_informe", "valor_anexos",
                    "fuente_anexos", "diferencia_pct", "mayor_a_1pct", "nota"])
        for c, u, a, vi, ui, va, fa, n in FILAS:
            dif = None if vi is None else round((va / vi - 1) * 100, 2)
            w.writerow([c, u, a, vi if vi is not None else "", ui, round(va, 3), fa,
                        "" if dif is None else dif, "" if dif is None else int(abs(dif) > 1), n])
    print(sal.read_text())


if __name__ == "__main__":
    main()

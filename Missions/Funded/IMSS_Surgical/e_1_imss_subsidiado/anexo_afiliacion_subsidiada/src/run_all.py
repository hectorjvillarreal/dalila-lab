"""Corre el pipeline completo en orden: F0-F4 (salvo la prosa de REPORT.md y ANEXO_borrador.md)."""

from __future__ import annotations

import cifras
import conapo
import cotizantes
import enigh
import esquemas
import f0_inventario
import libro
import proyeccion
import reporte
from common import NUMBERS_JSON

if __name__ == "__main__":
    NUMBERS_JSON.unlink(missing_ok=True)
    for mod in (libro, conapo, enigh, cotizantes, esquemas, proyeccion, f0_inventario, reporte, cifras):
        print(f"→ {mod.__name__}")
        mod.main()

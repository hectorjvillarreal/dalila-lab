"""Corre el pipeline completo en orden: F0-F4, v1.2 y el borrador v3 de la v1.3 (salvo la prosa de REPORT.md y de los borradores v1 y v2)."""

from __future__ import annotations

import borrador_v3
import cifras
import conapo
import cotizantes
import enigh
import esquemas
import f0_inventario
import libro
import proyeccion
import reporte
import v12
from common import NUMBERS_JSON

if __name__ == "__main__":
    NUMBERS_JSON.unlink(missing_ok=True)
    for mod in (libro, conapo, enigh, cotizantes, esquemas, proyeccion, f0_inventario, reporte, v12, borrador_v3, cifras):
        print(f"→ {mod.__name__}")
        mod.main()

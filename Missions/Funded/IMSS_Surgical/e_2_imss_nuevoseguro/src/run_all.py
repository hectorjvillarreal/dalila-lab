"""Corre el experimento 2 completo en orden (salvo la prosa de REPORT.md y del borrador del anexo)."""

from __future__ import annotations

import json

import cambios_exp1
import cuna_legal
import formalidad
import nuevo_seguro
import salidas
import sensibilidades_v12
from comun import DERIVED, NUMBERS_JSON

if __name__ == "__main__":
    NUMBERS_JSON.unlink(missing_ok=True)
    DERIVED.mkdir(parents=True, exist_ok=True)
    chk = {}
    for mod in (nuevo_seguro, sensibilidades_v12, cuna_legal, cambios_exp1, formalidad, salidas):
        print(f"→ {mod.__name__}")
        chk.update(mod.main())
    (DERIVED / "checks.json").write_text(json.dumps(chk, ensure_ascii=False, indent=1))
    print(json.dumps(chk, ensure_ascii=False, indent=1))

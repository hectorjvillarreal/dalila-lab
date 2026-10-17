"""Población a mitad de año de CONAPO 2023 (proyecciones 2020-2070), nacional, edad simple y sexo."""

from __future__ import annotations

import io
import zipfile

import pandas as pd

from common import inp, record, save

SEX = {"Hombres": "H", "Mujeres": "M"}


def main():
    z = zipfile.ZipFile(inp("conapo_zip"))
    with z.open("ConDem50a19_ProyPob20a70/0_Pob_Mitad_1950_2070.xlsx") as f:
        pop = pd.read_excel(io.BytesIO(f.read()))
    pop = pop[(pop.CVE_GEO == 0) & pop["AÑO"].between(2024, 2054)]
    pop = pop.assign(sexo=pop.SEXO.map(SEX)).rename(columns={"AÑO": "anio", "EDAD": "edad", "POBLACION": "pob"})
    pop = pop[["anio", "edad", "sexo", "pob"]].astype({"anio": int, "edad": int, "pob": float})
    save(pop, "conapo_pob")
    tot = pop.groupby("anio").pob.sum()
    record("CONAPO_pob_2025", round(tot[2025]), "CONAPO 2023, 0_Pob_Mitad_1950_2070.xlsx, CVE_GEO=0 (= 133.37 M del Núcleo 13, Tabla I.1)")
    record("CONAPO_pob_2054", round(tot[2054]), "CONAPO 2023, 0_Pob_Mitad_1950_2070.xlsx, CVE_GEO=0")


if __name__ == "__main__":
    main()

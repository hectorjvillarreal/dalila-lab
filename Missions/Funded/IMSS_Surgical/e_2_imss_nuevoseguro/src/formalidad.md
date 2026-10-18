# `formalidad.py`

Instrucción v1.2, sección 4: serie 2005-2025 de puestos de trabajo afiliados al IMSS entre población ocupada, solo con fuentes primarias.

- **Numerador:** puestos de trabajo afiliados al IMSS al 31 de diciembre (Memoria Estadística 2025, capítulo I, Cuadro I.2, fila Nacional).
- **Denominador:** población ocupada de 15 años o más de la ENOE, cuarto trimestre (microdatos del INEGI, tabla SDEMT: r_def = 0, c_res ∈ {1, 3}, clase2 = 1, 15 ≤ eda ≤ 97; factor `fac` hasta 2019 y `fac_tri` desde 2020). Se usa el cuarto trimestre para empatar con el corte de diciembre del IMSS.
- **Empalme:** compara el valor de 2025 con la formalidad implícita del libro (cotizantes / ocupados de CONAPO × ENIGH), sin ajustar. Las definiciones difieren: puestos frente a personas, y ocupados de la ENOE frente a ocupados estimados.
- **Insumos:** `data/raw/imss_memoria/01-Asegurados.xlsx` y `data/raw/enoe/*trim4*.zip`, no versionados. Las fechas de descarga están en `data/raw/descargas.json` y en `NUMBERS.md`.
- **Salida:** `tablas/formalidad_historica.csv`

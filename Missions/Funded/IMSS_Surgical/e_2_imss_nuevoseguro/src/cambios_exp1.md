# `cambios_exp1.py`

Sección 4 de la v1.1: el experimento 1 (salidas v1.2) pasa al denominador común (masa R1 con tope y piso, 337 días) y a los ingresos del SEM del Cuadro V.13. El cambio se hizo en `proyeccion.py` del experimento 1; este módulo solo lo documenta y lo verifica.

- **`cambios`:** compara el registro del experimento 1 al commit `2253249` (`data/v10/exp1_numbers_computed_v12.json`) con el actual y lista toda cifra que cambió → `tablas/exp1_cambios_denominador.csv`.
- **`montos_sin_cambio`:** verificación 7.4; compara las columnas de montos de `resultados_v12.csv` con su versión en git.
- **`contraste_sem`:** ingresos del SEM del Cuadro V.13 frente al libro (SEM-A + SEM-GMP), 2026, 2030, 2040 y 2054 → `tablas/contraste_ingresos_SEM_V13_libro.csv`.
- **Instrucción:** `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.1`

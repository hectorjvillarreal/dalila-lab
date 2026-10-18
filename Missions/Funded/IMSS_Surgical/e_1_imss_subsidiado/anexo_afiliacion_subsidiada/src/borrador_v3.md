# `borrador_v3.py`

Instrucción `20261018_BDH_N13_anexo-afiliacion-subsidiada_build_v1.3`. Genera `ANEXO_borrador_v3.md` a partir de `ANEXO_borrador_v2.md`. Solo sustituye las cifras en puntos del salario y en % de los ingresos del SEM por sus valores con el denominador común (masa R1, Cuadro V.13), y cambia la oración del denominador en X.3. Montos y redacción no cambian.

- **`sustituciones`:** lista cada cifra (texto de X.4, Cuadro X.1 b y c, X.5, X.6, Cuadro X.2 y texto de X.7) con su clave en `NUMBERS.md`, su valor anterior (salidas al commit `2253249`, vía git) y su valor nuevo. Respeta los decimales del v2.
- **`construir`:** aplica las sustituciones celda por celda. Antes de sustituir, comprueba que el texto del v2 sea el valor anterior (verificación de mapeo).
- **`verificar`:**
  - 3.1, ningún monto cambia.
  - 3.2, el texto nuevo coincide con el registro.
  - 3.3, conteo frente a las 186 cifras de `exp1_cambios_denominador.csv`.
  - 3.4, ninguna línea cambia fuera de cifras y de la oración del denominador.
  - 3.5, 2055.
- **Salidas:** `ANEXO_borrador_v3.md`, `outputs/tables/exp1_borrador_v2_a_v3.csv`, `data/derived/checks_v13.json`

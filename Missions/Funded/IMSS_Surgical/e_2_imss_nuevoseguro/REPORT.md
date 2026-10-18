# REPORT — Experimento 2 del anexo del Núcleo 13

**Instrucción:** `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.0` (Beth; lectura fiscal pendiente de Cath), archivada en `_crossrefs/_build_instructions/2026-10-18_BDH-N13_experimento2-seguro-salud-cuidados_initial-scaffold_v1.0.md`.
**Ejecutó:** Claude Code, 2026-10-18, autorizado por Héctor.
**Rótulo:** diseño de análisis de ITED; no es una proyección ni una propuesta del IMSS o del Gobierno. Tasas legales (incidencia legal), no incidencia económica.
**Reproducir:** `conda activate dalila && python src/run_all.py` (unos 30 s; la serie de formalización lee los microdatos de la ENOE de `data/raw/`). Reutiliza los módulos y derivados de la v1.2 del experimento 1 (`../e_1_imss_subsidiado/anexo_afiliacion_subsidiada/`) sin escribir en ellos. Todas las cifras están en `NUMBERS.md`.

**Decisiones de Héctor (18-10-2026), previas a la ejecución:**

1. Las salidas van en `e_2_imss_nuevoseguro/`, no dentro de la carpeta del experimento 1.
2. K1: cuando el ingreso no cubre el déficit de GMP, la diferencia se reporta como **déficit no cubierto**, no como reserva negativa.
3. K2, regla de 1/20: a criterio de Claude Code (ver [REVISAR] 1).
4. El contraste 3.3 se hace con **horizontes iguales**.
5. «% de los ingresos del SEM» usa los ingresos del **Informe** (Cuadro V.13).
6. Se aceptan los 79,178,109 derechohabientes como base (ver [REVISAR] 2).

---

## Experimento 2, v1.3 (2026-10-18)

**Instrucción:** `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.3` (Beth; K2 como regla principal a propuesta de Cath, decisión de Héctor). Archivada en `_crossrefs/_build_instructions/2026-10-18_BDH-N13_experimento2-seguro-salud-cuidados_retrofit_v1.3.md`; la v1.2 queda como `superseded`. Producto: `ANEXO_experimento2_borrador_v4.md`; el v3 se conserva. Corrida activa: `corrida: v1.3`. Es el mismo modelo que la v1.2: cambian la presentación, el escenario MH y la convención de fechas. **Es la última versión de modelo antes de redacción.**

**Decisiones de Héctor al ejecutar (18-10):**

- MH tiene tope en la formalidad de la base.
- La reserva final es el saldo de cierre de 2054.

### E2v13.1 Resumen K2 y K1 (`tablas/resumen_K2_K1.csv`)

| | Base, K2 | Base, K1 | M3, K2 | M3, K1 | M2, K2 | M2, K1 |
|---|---|---|---|---|---|---|
| Último año con cobertura completa | 2054 | 2054 | 2054 | 2034 | 2037 | 2032 |
| Déficit no cubierto en 2054 | 0 | 0 | 0 | 35,712 | 148,093 | 148,093 |
| Déficit no cubierto, VP | 0 | 0 | 0 | 114,602 | 728,630 | 831,627 |
| Cuidados, VP | 747,074 | 801,935 | 6,498 | 151,254 | 0 | 102,997 |
| Reserva final, VP | 54,861 | 0 | 30,155 | 0 | 0 | 0 |
| Cuidados más reserva final, VP | 801,935 | 801,935 | 36,653 | 151,254 | 0 | 102,997 |

- **Reserva final:** es el saldo de cierre de 2054 (125,518 mdp en la base), descontado a 2026. La instrucción citaba la reserva de *inicio* de 2054 (135,034 mdp, unos 59,000 en VP); se usó el cierre, como define la verificación 6.4 (decisión de Héctor).
- **Equivalencia en la base:** K2 y K1 dan exactamente el mismo valor presente, 801,935, porque la reserva rinde 3 % real, la misma tasa de descuento, y la base no tiene faltantes.

### E2v13.2 MH y Cuadro X-2.3 ampliado (`tablas/sensibilidad_v13.csv`)

- **MH:**
  - Parte de 34.0 % en 2025 y sube 0.3274 puntos por año: (37.68 − 31.14) / 20, con los extremos exactos de la serie.
  - Llega a 43.49 % en 2054; la instrucción esperaba unos 43.6 %, porque usaba un paso redondeado de 0.33.
  - Tiene tope en la formalidad de la base, que solo actúa en 2026 y 2027: sin tope, MH daría 34.32 % en 2026 frente a 34.08 % de la base.
  - De 2026 a 2034 queda por encima de M3 (35.63 % frente a 35.23 % en 2030), porque la proyección institucional formaliza más despacio al principio.
- **Último año con cobertura completa:**

| Regla | Escenario | Con prov., libro | Sin prov., libro | Con prov., S-masa | Sin prov., S-masa |
|---|---|---|---|---|---|
| K2 | Base | 2054 | 2054 | 2054 | 2054 |
| K2 | M3 | 2054 | 2054 | 2045 | 2051 |
| K2 | MH | 2049 | 2050 | 2043 | 2047 |
| K2 | M2 | 2037 | 2042 | 2036 | 2039 |
| K1 | Base | 2054 | 2054 | 2054 | 2054 |
| K1 | M3 | 2034 | 2041 | 2033 | 2036 |
| K1 | MH | 2034 | 2039 | 2033 | 2036 |
| K1 | M2 | 2032 | 2034 | 2031 | 2033 |

- **Oración del texto:** «Si la formalización avanzara al ritmo de 2005-2025, la formalidad llegaría a 43.49 % en 2054, entre M2 y M3; con reserva, el 2 % cubriría el déficit de GMP hasta 2049.»

### E2v13.3 Frase de apertura

«Con una reserva que se acumula hasta 2034, el 2 % cubre el déficit de GMP en todo el horizonte con la formalización que supone la proyección institucional y también con la mitad de esa formalización; con formalidad constante, lo cubre hasta 2037. Sin reserva, la cobertura con la mitad de la formalización llega hasta 2034 (2041 sin las provisiones de GMP), y con formalidad constante hasta 2032 (2034).»

Coincide con los Cuadros X-2.2 y X-2.3. Todas las celdas de la plantilla correspondían, así que no hubo que ajustarla.

### E2v13.4 Año de descuento

- Todos los valores presentes del anexo, desde la v1.0, se descuentan al 3 % real a **2026**, el mismo año y la misma tasa que los valores presentes del Informe.
- No hubo que unificar nada y ninguna cifra cambió.
- El borrador v4 lo declara en la sección de datos.

### E2v13.5 Verificaciones (sección 6)

| # | Resultado | Estado |
|---|---|---|
| 6.1 | La configuración v1.2 reproduce sus seis tablas: `ingreso_vs_GMP`, `valor_presente`, `remanente_por_mayor`, `resumen_escenarios`, `sensibilidad_provisiones_masa` y `reserva_K2`. Desviación máxima de 3.7e-9 mdp, la precisión del CSV | ✓ |
| 6.2 | Resumen K2/K1 frente a la v1.2: desviación 1.5e-11 mdp; 0 fechas que no correspondan (último año = primer año sin cobertura − 1) | ✓ |
| 6.3 | MH ≤ base en todos los años: 0 fallas. Entre M2 y M3 de 2035 a 2054 en formalidad, masa y déficit ajustado: 0 fallas. Último año con cobertura de MH entre los de M2 y M3 en las 8 columnas: 0 fallas. De 2026 a 2034, MH queda por encima de M3 (9 años; informativo) | ✓, con la salvedad de 2026-2034 (decisión de Héctor) |
| 6.4 | Reserva final en VP = (inicio de 2054 + movimiento de 2054) descontada a 2026: desviación 0. En K1 es 0 | ✓ |
| 6.5 | «Primer año sin cobertura» en el borrador v4: 0 apariciones. La frase de apertura coincide con los cuadros | ✓ |
| 6.6 | El documento no contiene las secciones eliminadas (se revisó tras actualizarlo) | ✓ |
| 6.7 | Sin 2055 en las tablas; todas las cifras del borrador v4 están en `NUMBERS.md` | ✓ |

### E2v13.6 Decisiones propias [REVISAR]

1. **[REVISAR] Cuadro X-2.4 (K1 sin reserva):** contiene el remanente y el déficit no cubierto de K1 por año. Es el «cuadro aparte» de la sección 1.1.
2. **[REVISAR] Numeración de cuadros del borrador v4:** X-2.1 principal (K2), X-2.2 resumen K2/K1, X-2.3 sensibilidades (como pide la instrucción), X-2.4 K1, X-2.5 trayectoria de la reserva y X-2.6 cuña legal.
3. **[REVISAR] «Remanente» con K2:** con K2 la fila se llama «gasto en cuidados», porque incluye el retiro fijo de la reserva. El término «remanente» se reserva para K1.

---

## Experimento 2, v1.2 (2026-10-18)

**Instrucción:** `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.2` (Beth; Cath avaló la v1.1). Archivada en `_crossrefs/_build_instructions/2026-10-18_BDH-N13_experimento2-seguro-salud-cuidados_retrofit_v1.2.md`. Producto: `ANEXO_experimento2_borrador_v3.md`; el v2 se conserva. Corrida activa: `corrida: v1.2`. Las configuraciones v1.0 y v1.1 siguen en `config.yaml` para las pruebas de regresión.

### E2v12.1 Con y sin provisiones (sección 1)

Primer año sin cobertura de GMP con la masa del libro:

| | Base | M3 | M2 |
|---|---|---|---|
| K1, con provisiones | ninguno | 2035 | 2033 |
| K1, sin provisiones | ninguno | 2042 | 2035 |
| K2, con provisiones | ninguno | ninguno | 2038 |
| K2, sin provisiones | ninguno | ninguno | 2043 |
| Déficit no cubierto, VP, K1 (con / sin) | 0 / 0 | 114,602 / 99,808 | 831,627 / 755,864 |
| Déficit no cubierto, VP, K2 (con / sin) | 0 / 0 | 0 / 0 | 728,630 / 607,575 |
| Margen mínimo y año (con) | 19,991 (2036) | −35,712 (2054) | −148,093 (2054) |
| Margen mínimo y año (sin) | 37,200 (2027) | −35,167 (2054) | −147,549 (2054) |

**La fecha sí depende de las provisiones**, sobre todo en M3: sin ellas, M3 cubre hasta 2041 y no hasta 2034. La explicación es que la interpolación reparte el pico de provisiones de 2036 entre 2032 y 2040, justo cuando M3 está casi en equilibrio. Por eso la frase de apertura agrega el rango: «… con formalidad constante, lo cubre hasta 2032 (hasta 2034 sin las provisiones de GMP); con la mitad de esa formalización, hasta 2034 (hasta 2041 sin las provisiones de GMP)».

### E2v12.2 Consistencia de masa y S-masa (sección 2)

**Diagnóstico r(t)** = ingreso de GMP del Cuadro V.24 / masa propia de la base: 1.691 % en 2027, 1.634 % en 2030, 1.551 % en 2036 y en 2040, y 1.544 % en 2054. La caída 2027-2054 es de −8.69 %. Casi toda ocurre antes de 2036; después la razón queda casi plana. Eso sugiere que el libro y el Informe difieren sobre todo en el **nivel** de la masa de los primeros años, más que en su crecimiento de largo plazo.

**S-masa:**

| | Base | M3 | M2 |
|---|---|---|---|
| K1, primer año sin cobertura (con / sin provisiones) | ninguno / ninguno | 2034 / 2037 | 2032 / 2034 |
| K2, primer año sin cobertura (con / sin) | ninguno / ninguno | 2046 / 2052 | 2037 / 2040 |
| Margen de 2036 (con provisiones) | 7,272 | −16,937 | −41,145 |
| Margen de 2040 (con provisiones) | 26,034 | −13,435 | −52,904 |
| Déficit no cubierto, VP, K1 (con) | 0 | 280,658 | 976,427 |

La referencia de Cath se reproduce: en la base, el margen de 2036 baja de 19,991 a 7,272 mdp (ella estimó unos 7,300) y el de 2040 de 40,745 a 26,034 (unos 26,000). La base sigue cubriendo todo el horizonte.

**[REVISAR] Asimetría de S-masa.** S-masa toma el nivel propio de 2027, que es el más bajo de las dos fuentes, y le aplica el crecimiento del Informe, que es el más lento. Es la combinación más conservadora. Una variante con nivel y crecimiento del Informe daría más ingreso; no se corrió porque la instrucción no la pide.

### E2v12.3 Orden de usos en K2 (sección 3)

**Lo que hacía el código v1.1** (`tablas/k2_v11_anios_con_faltante.csv`): desde 2035, en los años con faltante de GMP, la reserva cubría primero el faltante y, con lo que quedaba, pagaba además el retiro fijo para cuidados. Eso adelantaba el agotamiento de la reserva.

- **M3:** pagó cuidados en 15 años con faltante de GMP (2035-2040 y 2042-2050), 134,154 mdp en total.
- **M2:** pagó cuidados en 3 años (2035-2037), 16,643 mdp.
- **Base:** no tiene años con faltante.

**La v1.2 aplica la regla de Beth y K2 sí cambia** (`tablas/k2_cambios_v11_v12.csv`):

| | Antes (v1.1) | Después (v1.2) |
|---|---|---|
| M3: primer año sin cobertura, K2 | 2051 | ninguno |
| M3: cuidados, VP (K2) | 90,603 | 6,498 |
| M3: déficit no cubierto, VP (K2) | 53,950 | 0 |
| M3: reserva al cierre de 2054 | 0 | 68,993 |
| M2: cuidados, VP (K2) | 12,387 | 0 |
| M2: déficit no cubierto, VP (K2) | 741,017 | 728,630 |
| Base | sin cambio | sin cambio |

**Trayectoria de la reserva** (`tablas/reserva_K2.csv`, con provisiones):

- **Base:** 271,337 mdp al inicio de 2035 y 135,034 al inicio de 2054. Retira 271,337 para cuidados (20 × 13,567) y no se agota.
- **M3:** retira 227,552 para GMP y 9,557 para cuidados, y no se agota.
- **M2:** retira 119,940 para GMP y se agota en 2038.

### E2v12.4 Serie histórica de formalización (sección 4)

`tablas/formalidad_historica.csv`, solo con fuentes primarias:

- **Numerador:** puestos de trabajo afiliados al IMSS al 31 de diciembre (Memoria Estadística 2025, Cuadro I.2, fila Nacional).
- **Denominador:** población ocupada de 15 años o más de la ENOE, cuarto trimestre, calculada con los microdatos del INEGI (SDEMT; `fac` hasta 2019, `fac_tri` desde 2020).
- **Por qué el cuarto trimestre:** el cuadro de la Memoria es al cierre del año, así que el cuarto trimestre empata mejor con ese corte que el promedio anual.
- **Descargas:** el 18-10-2026. Los 21 archivos de la ENOE y la Memoria están en `data/raw/` (no versionados). Las fechas están en `data/raw/descargas.json` y en el registro.

| | 2005 | 2010 | 2015 | 2020 | 2025 |
|---|---|---|---|---|---|
| Puestos de trabajo IMSS (31-dic) | 13,061,565 | 14,738,783 | 17,884,033 | 19,773,732 | 22,517,076 |
| Ocupados ENOE T4 (15+) | 41,949,328 | 45,147,139 | 50,768,849 | 53,084,911 | 59,751,051 |

- **Serie:** de 31.1 % en 2005 a 37.7 % en 2025, 6.5 puntos en 20 años. El máximo es 37.7 % en 2025.
- **Proyección base:** 29.1 puntos en 29 años.
- **Empalme con el libro:** en 2025, la serie da 37.7 % y la formalidad implícita del libro 34.0 %, una diferencia de 3.7 puntos. Las dos razones se reportan sin ajustar porque difieren por definición:
  - la serie cuenta puestos de trabajo (una persona puede tener varios) sobre ocupados de la ENOE;
  - el libro cuenta cotizantes sobre ocupados estimados con CONAPO y la tasa de ocupación de la ENIGH, unos 65.7 millones frente a 59.8 millones de la ENOE.
- **Oración del borrador (limitación 7):** «Entre 2005 y 2025, la razón … pasó de 31.1 % a 37.7 % (6.6 puntos en 20 años); la proyección supone 29.1 puntos en 29 años…»

### E2v12.5 Personas mayores (sección 5)

- Se agregó la nota obligatoria: en la base, las cifras de 2040 y 2054 son una cota superior.
- **Variante opcional: no construida.** El Informe no trae una proyección anual de pensionados del IMSS, solo la del RJP (grupo cerrado, Gráfica VIII.1).

### E2v12.6 Cuña legal (sección 6)

- **2026, ley vigente:** mínimo 26.53 %, promedio 25.102 %, 25 UMA 22.705 %. Con la columna (c): −7.13, −3.209 y −0.349 puntos.
- **2030, ley vigente:** mínimo 24.793 %, promedio 29.464 %. Con la columna (c): −5.128 (la instrucción decía 5.127; la diferencia es de redondeo), −3.209 y −0.349 puntos.
- **Escalón a 1.01 SM, lectura por UMA, 2030:** +4.435 puntos con la ley vigente y +4.49 con la columna (c). En 2026: +0.426 y +0.501.
- **D2 en 25 UMA:** (c) − (b) = +2.651 puntos, en 2026 y en 2030.
- **Aportación federal fuera de la cuña:**
  - En el salario promedio de 2030, la cuña legal (patrón y trabajador) pasa de 32.023 % a 29.023 %, y la aportación federal es de 2.922 %.
  - Con la definición anterior, que la sumaba, pasa de 34.945 % a 31.945 %.
  - Tabla completa en `tablas/cuna_legal_resumen_v12.csv`.

### E2v12.7 Verificaciones (sección 8)

| Verificación | Resultado |
|---|---|
| 8.1 regresión v1.1: ingreso_vs_GMP (máx. desviación) | 1.9e-09 |
| 8.1 regresión v1.1: valor_presente (máx. desviación) | 4.7e-10 |
| 8.1 regresión v1.1: remanente_por_mayor (máx. desviación) | 3.7e-09 |
| 8.1 regresión v1.1: resumen_escenarios (máx. desviación) | 4.7e-10 |
| 8.2 años con déficit sin provisiones > con provisiones | 0 |
| 8.2 déficit con provisiones frente a la v1.1 (máx. desviación, mdp) | 0.000 |
| 8.3 S-masa: ingreso 2027 = ingreso base 2027 (desviación, mdp) | 1.5e-11 |
| 8.3 S-masa: razón ingreso nuevo / ingreso GMP constante en la base (rango) | 2.2e-16 |
| 8.4 K2: años con faltante de GMP y retiro para cuidados | 0 |
| 8.4 K2: identidad de la reserva (máx. desviación, mdp) | 1.2e-10 |
| 8.1 regresión v1.1: cuna_legal_por_salario (máx. desviación) | 7.1e-15 |
| 8.6 cuña sin aportación federal ≥ cuña con ella (niveles que fallan) | 0 |
| 8.1 regresión v1.1: exp1_cambios_denominador (máx. desviación) | 9.7e-17 |
| 8.5 serie de formalización: años sin fuente primaria | 0 |
| 3.6/8.7 apariciones de 2055 en las tablas | 0 |
| 3.7/8.7 cifras del borrador v3 sin registro en NUMBERS.md | 0 |

Todas se cumplen. Las desviaciones de las regresiones (≤ 3.7e-9 mdp) son la precisión del texto del CSV. Las verificaciones de la v1.0 y la v1.1 (3.1-3.7 y 7.1-7.4) siguen cumpliéndose con los mismos valores.

### E2v12.8 Decisiones propias [REVISAR]

1. **[REVISAR] Retiro fijo cuando la reserva no alcanza.** En los años sin faltante, el retiro para cuidados se paga hasta donde alcance la reserva, de forma parcial si hace falta. La instrucción dice «solo si la reserva alcanza», lo que también admite la lectura de todo o nada. No cambia ninguna cifra reportada: en la base la reserva nunca baja del retiro fijo.
2. **[REVISAR] S-masa:** la asimetría descrita en E2v12.2.
3. **[REVISAR] Serie de formalización:** puestos de trabajo (no personas) al 31 de diciembre, frente a ocupados del cuarto trimestre. Ver E2v12.4.

---

## Experimento 2, v1.1 (2026-10-18)

**Instrucción:** `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.1` (Beth y Cath). Archivada en `_crossrefs/_build_instructions/2026-10-18_BDH-N13_experimento2-seguro-salud-cuidados_retrofit_v1.1.md`. Producto: `ANEXO_experimento2_borrador_v2.md`. El primer borrador (`ANEXO_experimento2_borrador.md`) se conserva como registro de la v1.0, pero varias de sus cifras ya no están en el registro: las de M2 cambiaron y la base de adscripciones se eliminó.

**Decisiones de Héctor sobre la ejecución (18-10):**

- El borrador v2 del experimento 1 (`ANEXO_borrador_v2.md`) queda intacto; solo se publican las tablas de cambios hasta que Beth decida.
- La limitación «sin precedente histórico» se redacta sin esa afirmación si no se encuentra una serie. No se encontró una serie primaria comparable (cotizantes entre ocupados), así que el borrador describe el supuesto sin compararlo con la historia.

**Corrida activa:** `config.yaml` → `corrida: v1.1`. Con `corrida: v1.0` se reproduce la corrida anterior.

### E2v11.1 Resultados por escenario de formalidad (sección 1.3)

Con la formalización que supone la proyección institucional, el 2 % cubre el déficit de GMP en todo el horizonte. Con formalidad constante, lo cubre hasta 2032; con la mitad de esa formalización, hasta 2034.

| | Base | M3 | M2 |
|---|---|---|---|
| Formalidad implícita en 2054 | 63.13 % | 48.56 % | 34.0 % |
| Primer año sin cobertura, K1 | ninguno | 2035 | 2033 |
| Primer año sin cobertura, K2 | ninguno | 2051 | 2038 |
| Años sin cobertura 2027-2054, K1 | 0 | 19 | 22 |
| Déficit no cubierto en 2054 (mdp) | 0 | 35,712 | 148,093 |
| Déficit no cubierto, VP (K1 / K2) | 0 / 0 | 114,602 / 53,950 | 831,627 / 741,017 |
| Remanente, VP (K1) | 801,935 | 151,254 | 102,997 |

- **Qué cambió frente a la v1.0:** el ajuste del ingreso de GMP adelanta en dos años el primer año sin cobertura de M2 (de 2035 a 2033). El déficit de M2 en 2054 sube de 198,154 a 296,092 mdp.
- **M3:** queda casi en equilibrio alrededor de 2040 (déficit no cubierto de 648 mdp ese año) y después se abre la brecha.
- **Margen de 2036 (sección 5):** en la base, con provisiones, es de 19,991 mdp. Sin las provisiones de GMP del Cuadro V.19 es de 39,568 mdp, y el mínimo pasa a 2027 (37,200 mdp).

### E2v11.2 Remanente por persona mayor con base ENIGH (sección 2)

- **Base ENIGH:** 46.62 % de las personas de 65+ declara afiliación al IMSS (`inst_1`); entre las de 80+, 41.84 %. Se usan grupos quinquenales (85 y más) por sexo; la celda más chica tiene 1,329 observaciones.
- **Conteo:** con CONAPO, 5,923,223 personas de 65+ con IMSS en 2027 y 13,476,177 en 2054, 46.6 % y 45.9 % de la población nacional de 65+ (verificación 7.3).
- **Remanente K1 de la base:** 5,927 pesos por persona de 65+ en 2027 y 5,689 en 2054; por persona de 80+, 30,602 y 20,197. Es más del doble que con el conteo máximo del Informe (2,456 pesos en 2027), que equivale a 112.4 % de la población nacional de 65+ y queda solo en nota.

### E2v11.3 Criterio del SUA para 1.01 SM (sección 3.3)

- **Tramo vacío desde 2023:** el salario mínimo de 2023 era de 207.44 pesos (DOF 07-12-2022) y la UMA de 103.74 (DOF 10-01-2023), así que el mínimo equivalía a 2.00 UMA. Se confirma que el tramo «1.01 SM a 1.50 UMA» está vacío desde que empezó el calendario.
- **Fuentes revisadas, solo del IMSS y del DOF:**
  - El art. 168 vigente (Cámara de Diputados, última reforma DOF 15-01-2026) no trae regla para ese caso.
  - El decreto del 16-12-2020 tampoco.
  - La página del SUA en imss.gob.mx requiere sesión.
  - Las búsquedas en imss.gob.mx no dieron guía ni preguntas frecuentes con el criterio.
- **Resultado:** no encontrado. Queda **pendiente de confirmación con el IMSS** (visita de Juan Pablo). El borrador presenta las dos lecturas.
- **Escalón a 1.01 SM con la lectura por UMA:** +0.426 puntos en 2026 y +4.435 en 2030. Con el primer tramo: −1.924 y −1.44 puntos.
- **Art. 36:** la redacción verificada contra el texto vigente de la Cámara de Diputados coincide con la citada.

### E2v11.4 Experimento 1: denominador común y fuente única de ingresos del SEM (sección 4)

En las salidas v1.2 del experimento 1, el denominador de los puntos del salario es ahora la masa R1 con tope y piso (337 días) y los ingresos del SEM son los del Cuadro V.13. Cambian 186 cifras del registro: 123 en puntos del salario y 63 en % de los ingresos del SEM. Los montos en mdp no cambian. La tabla completa está en `tablas/exp1_cambios_denominador.csv`. Selección:

| Cifra del experimento 1 | Antes | Después |
|---|---|---|
| Saldo total, puntos del salario, 2026 | −1.568 | −1.539 |
| Saldo total, puntos del salario, 2030 | −1.357 | −1.305 |
| Saldo total, puntos del salario, 2054 | −0.593 | −0.585 |
| Saldo total, % ingresos del SEM, 2026 | −14.68 | −14.44 |
| Saldo total, % ingresos del SEM, 2030 | −13.25 | −12.93 |
| Saldo total, % ingresos del SEM, 2054 | −6.66 | −6.72 |
| Pagos federales del Bloque A, puntos, 2030 | 1.237 | 1.189 |
| Efecto de indexación, puntos, 2054 | 0.730 | 0.720 |
| Efecto de indexación, % SEM, 2054 | 8.20 | 8.28 |
| Bloque C con D2, efecto neto, puntos, 2030 | −0.193 | −0.186 |

**Contraste de ingresos del SEM (sección 4.4), mdp de 2026:**

| | 2026 | 2030 | 2040 | 2054 |
|---|---|---|---|---|
| Cuadro V.13 − libro (SEM-A + SEM-GMP) | 9,232 | 15,148 | 2,620 | −11,640 |
| Diferencia, % del libro | 1.67 | 2.48 | 0.31 | −0.96 |

`ANEXO_borrador_v2.md` del experimento 1 **sigue citando las cifras anteriores**, por ejemplo «1.36 puntos del SBC y 13.2 % de los ingresos del SEM» en 2030, que ahora son 1.305 y 12.93. Hay que actualizarlo cuando Beth lo indique.

### E2v11.5 Verificaciones (sección 7)

| # | Resultado | Estado |
|---|---|---|
| 7.1 | La configuración v1.0 reproduce las cuatro tablas de la corrida anterior (`data/v10/`). La desviación máxima es de 3.7e-9 mdp, la precisión del texto del CSV; la cuña legal, 7e-15. | ✓ |
| 7.2 | En la base, el déficit ajustado es igual al del Cuadro V.24 (desviación 0). El déficit de M2 es mayor que el de M3 y el de M3 mayor que el de la base en todos los años: 0 fallas. | ✓ |
| 7.3 | Base ENIGH de 65+ ≤ 100 % de la población nacional: el máximo es 46.6 %. | ✓ |
| 7.4 | Experimento 1: montos en mdp de `resultados_v12` sin cambio (desviación 0); 0 cifras cambiadas fuera de puntos y % del SEM. Sus verificaciones internas (7.1-7.8 y 6.x) dan los mismos resultados que antes. | ✓ |
| 7.5 | Columna (b) = (a) − 3 con la prima de RT de 1.9078 %: desviación 0. | ✓ |
| 7.6 | Sin 2055 en las tablas; las cifras del borrador v2 están todas en `NUMBERS.md` (0 faltantes). | ✓ |

Las verificaciones 3.1-3.5 de la v1.0 siguen cumpliéndose con los mismos valores.

### E2v11.6 Decisiones propias [REVISAR]

1. **[REVISAR] Referencia de M3.** M3 toma, año por año, la mitad de la ganancia de formalidad sobre **2025** (la misma referencia de M2): 48.56 % en 2054. La instrucción decía 48.8 %, que usa 2027 como punto de partida.
2. **[REVISAR] Puntos del salario por escenario.** En el Cuadro X-2.1 (b), cada escenario se expresa sobre su propia masa, con la misma construcción R1. Así, el ingreso siempre es 2.00 puntos y el déficit sube en puntos cuando la masa baja. La alternativa sería dividir todo entre la masa de la base.
3. **[REVISAR] Gasto de GMP sin ajuste en M3 y M2**, como pide la instrucción (sección 1.1).
4. **[REVISAR] Lectura del Cuadro X-2.3 en 2030.** La afirmación de 3.4 vale para 2026. En 2030 el orden cambia: la tasa en el mínimo (24.793 %) queda por debajo de la del promedio (29.464 %). Hay dos razones: el calendario de cesantía y vejez sube más en los tramos altos, y el mínimo crece en UMA. El borrador limita la lectura a 2026.
5. **[REVISAR] Grupos de edad de la ENIGH.** Se usan grupos quinquenales y no edad simple: con edad simple, las celdas de 85 años o más quedarían con pocas observaciones. La tasa se mantiene constante por edad y sexo en el horizonte.
6. **[REVISAR] Limitación sobre la formalización.** Se redactó sin la afirmación «sin precedente histórico» (decisión de Héctor): describe el supuesto, unos 29 puntos en 29 años, y aclara que el anexo no lo compara con la historia.

---

## Experimento 2

### E2.1 Resumen

- **¿Cubre el déficit de GMP?** Sí, en todos los años de 2027 a 2054 en el escenario base. El 2 % de la masa con tope rinde 109,378 mdp en 2027 y 274,824 en 2054, frente a un déficit de 74,270 y 198,154. El margen más estrecho es de 19,991 mdp (0.259 puntos del salario), en 2036. En valor presente 2027-2054 al 3 % real: ingreso 3,265,351 mdp, déficit 2,463,416 y remanente 801,935.
- **La conclusión depende de la formalización implícita.** Con formalidad constante (M2), la masa de 2054 es 53.85 % de la base y el ingreso **deja de cubrir el déficit desde 2035**. Con K1, el déficit no cubierto llega a 50,155 mdp en 2054 (203,014 en valor presente). Con K2, la reserva acumulada lo posterga hasta 2047.
- **Remanente por persona mayor (K1, base):** 2,456 pesos por derechohabiente de 65+ en 2027 y 2,322 en 2054; por derechohabiente de 80+, 11,382 y 7,453. Con K2 no hay nada antes de 2035; en 2054 son 2,733 pesos por persona de 65+.
- **Cuña contributiva legal:** baja 3 puntos del salario en todo nivel hasta 25 UMA. En 2030, el total a cargo del patrón en el salario promedio (5.55 UMA) pasa de 29.356 % a 26.356 %. Con D2 queda en 26.147 %. El agregado es de 164,066 mdp en 2027 y 412,235 en 2054.
- **Escalón de cesantía y vejez:** el tramo «1.01 SM a 1.50 UMA» está vacío desde 2026. Según la lectura, el total a cargo del patrón a 1.01 SM sube 4.435 puntos o baja 1.44 puntos en 2030 (sección E2.3).

### E2.2 Verificaciones (sección 3)

| # | Resultado | Estado |
|---|---|---|
| 3.1 | La masa con tope reproduce exactamente la base de la tasa D2 de la v1.2 (recaudación D2 / c; desviación máxima 2.2e-16). Por encima del tope queda 1.74 % de la masa sin tope en 2027 y 2.71 % en 2054. Frente al denominador de «puntos del SBC» de la v1.2 (cotizantes × SBC promedio × crecimiento, sin piso en el SM), la masa R1 es 2.27 % mayor en 2027 y 1.40 % en 2054, por el piso en el salario mínimo. | ✓ |
| 3.2 | El Cuadro V.24 transcrito coincide con el PDF celda por celda (pág. PDF 161, leída por el código). La interpolación preserva los años ancla (desviación 0). El valor presente del déficit interpolado (descuento a fin de año) es 2,618,336, 0.50 % menor que el publicado; con descuento a mitad de año sería 2,579,923. | ✓ |
| 3.3 | Con horizontes iguales (30 años desde 2026), 2 % × masa propia = 3,488,044 frente a 2 % × volumen de salarios del Informe = 3,529,634: **−1.18 %**. Necesitó extender la masa un año más allá de 2054 (solo para este contraste; esa fila no se reporta). | ✓ |
| 3.4 | Identidad de la reserva R(t+1) = R(t)·(1 + r) + I − D − U (+ déficit no cubierto) en todos los años, K1 y K2, base y M2: desviación máxima 5.8e-11 mdp. | ✓ |
| 3.5 | Columna (b) = (a) − 3 puntos en todos los niveles (desviación 0). Las tasas de cesantía y vejez coinciden con la tabla de 1.5, que a su vez coincide con el Segundo Transitorio del DOF del 16-12-2020 (imagen de la tabla, leída) y, para 2030, con el texto del art. 168 fr. II a). | ✓ |
| 3.6 | Ninguna celda ni encabezado de las tablas contiene 2055; la figura no lo muestra en el eje. | ✓ |
| 3.7 | Todas las cifras del borrador del anexo están en `NUMBERS.md` (verificación automática en `salidas.py`). | ✓ |

**Contraste 1.2.** 1.6 puntos × 176,481,700 = 2,823,707 mdp, frente a 2,631,460 del Cuadro V.24. La diferencia se explica entera (residuo de −1 mdp):

- 82,699 por redondeo de las primas: 3.1 − 1.5 publicadas frente a 3.053 − 1.500 exactas.
- 103,662 de otros ingresos de GMP, que no entran en la prima de financiamiento.
- 5,887 de diferencia entre los Cuadros V.19 y V.24 para el mismo escenario base.

Los dos cuadros difieren también en 2031 y 2036 (−97,653 y −135,137 en el V.19, frente a −97,760 y −134,117 en el V.24). Se usa el V.24, como pide la instrucción.

### E2.3 Escalón de cesantía y vejez arriba del salario mínimo

- El texto legal (art. 168 fr. II a) y Segundo Transitorio, DOF 16-12-2020) define tramos «1.00 SM», «1.01 SM a 1.50 UMA» y luego tramos por UMA. **No dice qué hacer cuando el mínimo rebasa 1.50 UMA**, y eso ya ocurre: el SM vale 2.685 UMA en 2026 y 3.646 en 2030 con la trayectoria de `Sup_Fin`.
- **Lectura por UMA:** un salario de 1.01 SM cae en el tramo que su valor en UMA indica, 2.51-3.00 UMA en 2026 y 3.51-4.00 UMA en 2030. La tasa patronal salta de 3.150 % a 6.026 % (+2.876 puntos) en 2026 y a 10.077 % (+6.927) en 2030. Neto del fin del art. 36, el total a cargo del patrón sube 0.426 puntos en 2026 y 4.435 en 2030.
- **Primer tramo tras el mínimo:** 3.676 % en 2026 y 4.202 % en 2030. El total a cargo del patrón baja 1.924 y 1.44 puntos, porque a 1.01 SM el patrón deja de cubrir la cuota obrera (art. 36).
- **Hallazgo:** con la lectura por UMA hay un escalón legal grande justo arriba del mínimo, y crece hasta 2030. Ninguna de las dos lecturas está zanjada en el texto del DOF; conviene confirmar el criterio operativo del IMSS (SUA / IDSE) antes de citar el escalón en el anexo. El anexo presenta ambas.

### E2.4 Decisiones propias [REVISAR]

1. **[REVISAR] K2, regla de 1/20.** Se retira un **monto fijo real** igual a 1/20 de la reserva al inicio de 2035 (13,567 mdp en la base), de 2035 a 2054, además del remanente del año. Como la reserva rinde 3 %, queda un saldo de 125,518 mdp al cierre de 2054. La alternativa, 1/20 del saldo de cada año, decae geométricamente y deja más saldo al final.
2. **[REVISAR] Denominador de personas mayores.** La instrucción aplica 16.6 % (proporción de 65+ en la **población adscrita a médico familiar**, Gráfica I.31) a los 79,178,109 derechohabientes (población potencial). Eso da 13,143,566 personas de 65+ en 2025, **112.4 % de la población nacional de 65+ de CONAPO** (11,698,499). Aplicada a su propia base (63,598,543 adscripciones), da 10,557,358 (90.2 %). Se mantiene la base de la instrucción y se reporta la de PAMF como sensibilidad en `remanente_por_mayor.csv`; el remanente por persona del anexo es, por eso, un piso.
3. **[REVISAR] Proyección de personas mayores.** La cobertura del IMSS entre las personas de 65+ se mantiene constante: los derechohabientes de 65+ crecen como la población de 65+ de CONAPO. El 80+ se toma con la razón 80+/65+ de CONAPO.
4. **[REVISAR] M2.** «Índice C2 aplicado a los cotizantes» se implementó como cotizantes × (formalidad implícita de 2025 / formalidad implícita del año), con la prueba C de la v1.2 (ocupados = CONAPO × tasa de ocupación ENIGH). Así los cotizantes crecen al ritmo de los ocupados. El factor C2 de la v1.2 escala a la población **informal**; aplicado directamente a los cotizantes no tendría la interpretación pedida.
5. **[REVISAR] Masa salarial.** Se usa la base R1 de la tasa D2 (piso en el salario mínimo y tope de 25 UMA). Es hasta 4 % mayor que el denominador de «puntos del SBC» de la v1.2 en los años de alza real del mínimo. Por eso los puntos del salario de este experimento no son idénticos a los del experimento 1.
6. **[REVISAR] Cuña legal:**
   - En el salario mínimo, la cuota obrera se carga al patrón (LSS art. 36; texto tomado de fuentes secundarias, no del DOF).
   - La prima de Riesgos de Trabajo es 1.80 % (libro, promedio 2023-2025), como pide la instrucción. El Cuadro A.3 del Informe reporta 1.9078 %; el cambio no afecta la diferencia (b) − (a).
   - La cuota social y la cuota fija federal se mantienen constantes en UMA reales.
   - La columna (c) supone que los formales con salario mínimo o más no reciben el subsidio del experimento 1. En la v1.2 el Bloque B es 0 en todos los años, así que el supuesto es consistente.
7. **[REVISAR] Niveles debajo del mínimo.** 2 UMA (2026 y 2030) y 3 UMA (2030) quedan por debajo del salario mínimo. Se reportan marcados con †, solo como referencia.
8. **[REVISAR] Interpolación del Cuadro V.24.** El año ancla 2036 trae provisiones altas (19,577 mdp en el Cuadro V.19), y por eso el margen mínimo cae en 2036. La interpolación lineal reparte ese pico entre 2032 y 2040.
9. **Infonavit.** No se obtuvo la recaudación efectiva de 2024 o 2025: la búsqueda solo dio cifras de prensa acumuladas a agosto de 2024. Se omitió, como manda la instrucción.
10. **Horizonte del contraste.** Para el contraste 3.3, la masa de 2055 se extiende con los cotizantes, el crecimiento del SBC y el salario mínimo del libro, con la composición por edad y sexo de 2054.

### E2.5 Salidas

| Archivo | Contenido |
|---|---|
| `tablas/ingreso_vs_GMP.csv` | 2027-2054, base y M2: masa, ingreso, déficit, K1, K2 (reserva de inicio y cierre), reducción de la cuña y 5 % teórico del Infonavit; en mdp, puntos del salario y % de los ingresos del SEM |
| `tablas/valor_presente.csv` | VP 2027-2054 (base y M2) y contrastes con el Informe sobre su propio horizonte |
| `tablas/remanente_por_mayor.csv` | K1 y K2 por persona de 65+ y 80+ (2027, 2030, 2040, 2054); denominadores DH total y PAMF |
| `tablas/cuna_legal_por_salario.csv` | Componente por componente, (a), (b) y (c), 2026 y 2030; incluye las dos lecturas de 1.01 SM |
| `figuras/ingreso_vs_GMP.png` | Ingreso frente a déficit, remanente sombreado, M2 punteado |
| `ANEXO_experimento2_borrador.md` | Borrador del anexo, unas 3 páginas |

---

## Corrección del 18-10-2026 (sección 10 v1.1, punto 2.4.2)

`ANEXO_experimento2_borrador_v4.md`, limitación 7: el cambio de la formalidad 2005-2025 pasa de «6.6 puntos» a **6.5 puntos**. El 6.6 era la resta de los extremos ya redondeados (37.7 − 31.1). La resta exacta es 37.685 − 31.137 = 6.548 (`tablas/formalidad_historica.csv`), y así está registrada en `NUMBERS.md` (`form_hist_cambio_pts` = 6.5). La sección 10 usa la misma cifra. No cambia ninguna corrida.

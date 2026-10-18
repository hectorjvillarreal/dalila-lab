# REPORT — Experimento 2 del anexo del Núcleo 13

**Instrucción:** `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.0` (Beth; lectura fiscal pendiente de Cath), archivada en `_crossrefs/_build_instructions/2026-10-18_BDH-N13_experimento2-seguro-salud-cuidados_initial-scaffold_v1.0.md`.
**Ejecutó:** Claude Code, 2026-10-18, autorizado por Héctor.
**Rótulo:** diseño de análisis de ITED; no es una proyección ni una propuesta del IMSS o del Gobierno. Tasas legales (incidencia legal), no incidencia económica.
**Reproducir:** `conda activate dalila && python src/run_all.py` (unos 3 s). Reutiliza los módulos y derivados de la v1.2 del experimento 1 (`../e_1_imss_subsidiado/anexo_afiliacion_subsidiada/`) sin escribir en ellos. Todas las cifras están en `NUMBERS.md`.

**Decisiones de Héctor (18-10-2026), previas a la ejecución:**

1. Las salidas van en `e_2_imss_nuevoseguro/`, no dentro de la carpeta del experimento 1.
2. K1: cuando el ingreso no cubre el déficit de GMP, la diferencia se reporta como **déficit no cubierto**, no como reserva negativa.
3. K2, regla de 1/20: a criterio de Claude Code (ver [REVISAR] 1).
4. El contraste 3.3 se hace con **horizontes iguales**.
5. «% de los ingresos del SEM» usa los ingresos del **Informe** (Cuadro V.13).
6. Se aceptan los 79,178,109 derechohabientes como base (ver [REVISAR] 2).

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

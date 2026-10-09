---
mission: CAF_DEM
producto: P4
tipo: reporte-claude-code
instrucciones: CAF_DEM_P4_correccion_intereses_Mexico.md
fecha: 2026-10-09
rama: p4-intereses-mexico (desde p4-revision-final)
commit: 4ea046a
entrega: sábado 10 de octubre de 2026
---

# CAF_DEM · P4 — Corrección de intereses de México: reporte final

> **Decisiones de Héctor (9 de octubre).** Perímetro del denominador: **opción (b)**. La deuda neta sigue siendo el SHRFSP y la nota declara la diferencia de perímetros. Clasificación de México: se mantiene en el **Tipo B**.

## 1. Serie usada

- **Fuente:** SHCP, Estadísticas Oportunas de Finanzas Públicas, datos abiertos (`ingreso_gasto_finan.csv`), descargados el 2026-10-09.
- **Clave:** XAC21, "Costo financiero del sector público", sector público federal presupuestario, base pagado, suma de 12 meses.
- **Qué incluye:** intereses, comisiones y gastos de la deuda (XAC2110) **más** el costo de los programas de apoyo a ahorradores y deudores de la banca, Ramo 34 (XAC2120).
- **Archivo:** `weo/shcp_costo_financiero_presupuestario_mex.csv`. Trae ambos componentes por separado.

| Año | mmdp | % PIB (WEO) | Sin Ramo 34 | Anterior (RFSP) |
|---|---|---|---|---|
| 2015 | 408,3 | 2,12 | 2,07 | 2,82 |
| 2016 | 473,0 | 2,28 | 2,18 | 3,13 |
| 2017 | 533,1 | 2,37 | 2,21 | 3,76 |
| 2018 | 615,0 | 2,54 | 2,39 | 3,90 |
| 2019 | 666,5 | 2,65 | 2,45 | 3,92 |
| 2020 | 686,1 | 2,85 | 2,67 | 4,07 |
| 2021 | 686,7 | 2,57 | 2,53 | 3,97 |
| 2022 | 815,2 | 2,76 | 2,63 | 4,37 |
| 2023 | 1.045,1 | 3,28 | 3,11 | 4,71 |
| 2024 | 1.150,4 | 3,39 | 3,21 | 5,17 |

La cifra de 2024 coincide con la de IMCO (1,15 billones de pesos, 3,4 % del PIB).

**Contraste con la SHCP.** El informe sobre la situación económica, las finanzas públicas y la deuda pública del cuarto trimestre de 2024 publica el costo financiero en % del PIB (cuadro "Situación financiera del Sector Público", p. 36 del PDF de la Gaceta Parlamentaria, 1 de febrero de 2025). Da 3,3 % en 2023 y 3,4 % en 2024, igual que nuestro cálculo con el PIB del WEO (3,28 y 3,39). La nota (a) lo menciona.

El mismo cuadro explica el "3,7 %" de las instrucciones del 8 de octubre, que no se reproducía: es la cifra **programada** para 2024 (1.264,0 mmdp), no la observada.

**Ramo 34 (decisión de Héctor, 9 de octubre).** Se conserva la serie XAC21 completa, con Ramo 34: 3,39 % en 2024.

**Perímetros (opción b).** El numerador tiene perímetro presupuestario. El denominador es la deuda neta del WEO (51,4 % del PIB en 2024), que para México coincide con el SHRFSP. Como el perímetro de los intereses es más estrecho, la tasa implícita de México está sesgada a la baja. Esto se declara en la nota (a) de la Tabla de espacio fiscal, en la nota (b) de la Tabla de síntesis, en la ficha de México y en §6.2.

## 2. Valores de México y ordenamiento

| | Anterior | Nuevo |
|---|---|---|
| Intereses 2024 (% PIB) | 5,17 | 3,39 |
| Tasa implícita, 2015–2024 | 9,3 % | 6,2 % |
| Crecimiento nominal, 2015–2024 | 6,5 % | 6,5 % |
| (r−g) | 2,8 | −0,2 |
| pb\* | 1,4 | −0,1 |
| **Brecha** | **1,2** | **−0,3** |
| Brecha con deuda bruta | 1,3 | −0,3 |
| Ventana proyectada | n.c. | n.c. |
| Total en la Tabla de presión (mín.–máx.) | 4,9–5,6 | 3,5–4,1 |

El incremento demográfico de México no cambia: 3,8 a 4,4 puntos.

**Ordenamiento en espacio fiscal, ventana histórica (brecha de mayor a menor):**

| Posición | Anterior | Nuevo |
|---|---|---|
| 1 | Panamá 5,2 | Panamá 5,2 |
| 2 | Brasil 3,1 | Brasil 3,1 |
| 3 | Chile 1,4 | Chile 1,4 |
| 4 | **México 1,2** | Costa Rica 0,2 |
| 5 | Costa Rica 0,2 | Colombia 0,0 |
| 6 | Colombia 0,0 | **México −0,3** |

- **Con deuda bruta:** antes México (1,3) pasaba delante de Chile (1,0). Ahora el orden coincide con el de deuda neta.
- **Con la proyección del FMI:** Colombia sigue cuarta, y México queda sin calcular (n.c.).

## 3. Cambios del Paso 2

### Cálculo y base

| Archivo | Cambio |
|---|---|
| `calc_seccion6.py` | Lee la serie XAC21. Un comentario declara la opción (b). La fila de la base pasa a `SHCP_XAC21`, con `cobertura_institucional = "Sector público presupuestario"`. Se ejecutó de nuevo y sólo cambiaron las filas de México. |
| `seccion6_espacio_fiscal.csv`, `seccion6_presion_demografica.csv`, `weo/series_nuevas_P4.csv` | Regenerados. |
| `base_analisis_P4.csv` | Se sustituyeron las 10 filas `SHCP_RF213000SPFC` por las 10 filas `SHCP_XAC21`. Se conservan el orden, el BOM y el formato. |
| `base_analisis_P4_diccionario.csv`, `tablas/anexo_diccionario_base.tex`, `pipeline_P4.R` | La advertencia de uso describe la serie nueva, el Ramo 34 y el sesgo por perímetro. También registra la serie RFSP de la versión del 8 de octubre. |

`pipeline_P4.R` **no se ejecutó de nuevo**, porque volvería a estimar todas las proyecciones. Sólo cambió su cadena de advertencia, y la base y el diccionario se editaron directamente.

### Documento

| Lugar | Cambio |
|---|---|
| `tablas/tab_espacio_fiscal.tex` | La fila de México queda con (r−g) −0,2, pb\* −0,1, brecha −0,3 y deuda bruta −0,3, y baja al último lugar. |
| `tablas/tab_presion_demografica.tex` | El total de México pasa a 3,5–4,1. |
| Principales hallazgos (l. 270–283) | Costa Rica es "cuarta" en espacio fiscal y México "último en presión demográfica y en espacio fiscal". México se suma a la frase de presión casi enteramente demográfica (−0,3; 3,5 a 4,1). |
| §6.2, datos y supuestos | Se menciona "el costo financiero del sector público presupuestario que reporta la SHCP". |
| Nota (a) de la Tabla de espacio fiscal | Texto aprobado, más la frase sobre el perímetro y el sesgo a la baja. |
| §6.2, posiciones | "Chile y México ocupan una posición intermedia" pasa a "Chile ocupa una posición intermedia". México entra al párrafo de brechas mínimas, nulas o negativas, con sus dos salvedades y el aumento de 4,7 puntos en la deuda neta. |
| §6.2, Chile | Se quitó "es el único país del grupo que estabilizaría su deuda con un déficit primario moderado". Colombia y México también tienen pb\* negativo con la ventana histórica. |
| §6.2, sensibilidad con deuda bruta | Reescrita: el orden no cambia. |
| §6.3, México | Brecha negativa, cociente no informativo y presión de 3,5 a 4,1. Colombia y Costa Rica: "el cociente *tampoco* es informativo". |
| Ficha de México, espacio fiscal | Costo financiero de 3,4 %, brecha de −0,3 y salvedad de perímetro. Se quitó "perímetro RFSP". |
| Tabla de síntesis | Costa Rica 4 (0,2), Colombia 5 (0,0), México 6 (−0,3). Nota (b) nueva sobre el perímetro. |
| §6.6, Dónde divergen | Costa Rica "cuarta", México "último en presión demográfica y en espacio fiscal", Colombia "quinto o cuarto". |
| §6.6, Tipo B | México: deuda neta +4,7 puntos y brecha −0,3 sesgada a la baja. Su riesgo es sobre todo de arquitectura (sustitución contributivo→no contributivo). |
| Conclusiones, espacio fiscal | "Chile en posición intermedia" y "México con una brecha ligeramente negativa que depende del perímetro de los intereses". El cociente se limita a Brasil y Chile: "entre casi cuatro y siete veces". México entra con Colombia y Costa Rica en "presión adicional predominantemente demográfica". |

## 4. Paso 3 — Frases del árbitro

| | Lugar | Estado |
|---|---|---|
| 3.1 | §4.3, primera hipótesis | Aplicada. Se conserva la explicación. |
| 3.2 | Conclusiones, última oración | Aplicada con "la metodológica", no "la tercera". |
| 3.3 | Principales hallazgos y Conclusiones | Aplicada. En Hallazgos se reemplazó el bloque completo para no repetir "casi enteramente demográfica". |
| 3.4 | §6.2, ficha de Costa Rica y Conclusiones | Aplicada. |

La frase de Conclusiones que comparten los Pasos 2 y 3 quedó coherente con ambos.

## 5. Verificación

- [x] Tres compilaciones con pdflatex (TinyTeX): 0 errores, 0 referencias o citas indefinidas, 105 páginas. Las dos cajas que se salían del margen en §3.1 se corrigieron después (ver «Ajustes posteriores»).
- [x] `grep RFSP main.tex tablas/*.tex`: sin menciones en el texto. Sólo queda en `anexo_diccionario_base.tex`, como registro de la serie anterior.
- [x] `grep 5,2`: sólo Panamá, más un 5,25 de Costa Rica que no tiene relación.
- [x] `grep` de las frases del árbitro: cero coincidencias.
- [x] `grep 9,3|2,8`: ninguna mención a la tasa ni al diferencial anteriores de México. Hay un 9,3 de otra cosa en l. 2203.
- [x] Cifras y ordenamientos de México coinciden en la tabla de espacio fiscal, la Tabla de presión, la Tabla de síntesis, §6.2, §6.3, §6.6, la ficha, Principales hallazgos y Conclusiones.

**Diff:** `git diff f9d65c3 4ea046a`. Rama `p4-intereses-mexico` publicada en origin. `main.pdf` actualizado en el commit.

## Ajustes posteriores (9 de octubre, por indicación de Héctor)

- **Ramo 34:** se conserva (3,39 %).
- **Cociente de Chile:** §6.3 dice ahora "entre cinco y siete veces y media" y Conclusiones "entre casi cuatro y siete veces y media". El cociente máximo es 7,5.
- **Porcentaje de la SHCP:** incorporado como contraste en la nota (a) de la Tabla de espacio fiscal. La fuente de la nota incluye ahora el informe del cuarto trimestre de 2024.
- **Cajas que se salían del margen:** en las tablas del Pilar 1 y del Pilar 2 (§3.1), la primera columna pasa de 1,6 a 1,7 cm, porque "Colombia" no cabía. El log ya no tiene ninguna caja sobrellena.
- Se compiló tres veces: 0 errores, 0 referencias indefinidas, 0 cajas sobrellenas, 105 páginas.
- Zip para Overleaf: `caf_dem_p4_overleaf_v3.zip`. Sustituye al v2.

## Pendiente

- Visto bueno de Héctor y revisión de Juan Pablo.
- Subir `caf_dem_p4_overleaf_v3.zip` a Overleaf.
- Envío a CAF. El plazo contractual es el 22 de octubre.

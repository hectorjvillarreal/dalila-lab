# Bitácora — evaluación del documento CIEP, ejercicio 2021

## Corrida
- Inicio: 2026-09-05T14:25:42-06:00 (lectura de los tres archivos de `_aprendizaje/` y extracción de texto de los PDF de `2021/`).
- Interrupción: la sesión que corrió las fases 1–5 y 6 agotó su contexto a las 16:25 con tres artefactos pendientes (CSV consolidado, `03_evaluacion_calidad.md`, esta bitácora). El CSV se consolidó a las 16:43 con las filas del agente de extracción. Una segunda sesión retomó a las 22:34 y escribió `03` y la bitácora.
- Fin: 2026-09-05T22:45:00-06:00 (aprox.; escritura de esta bitácora).
- Máquina: Dalila. Herramientas: pdftotext (poppler), python3/pandas/openpyxl en `dalila`; un subagente de extracción para los capítulos distintos de salud (ver "Método").
- CIEP: `2021/ciep_implicaciones2021.pdf`, 88 páginas PDF, sha256 `e0a808f4…2629bf`, registrado en el manifiesto como `derivada_ciep`. Paginación: impresa = PDF − 14 en capítulos; frente en romanos (resumen PDF 7–9; "Los retos fiscales" PDF 10–11).

## Orden de fases (obligatorio)
- Índice general de CIEP (PDF 4–6) leído a las 14:28:09. Nada más del documento antes de la fase 2. La instrucción 2021 no citaba cifras de CIEP: no hubo contaminación como la declarada en 2020.
- Cierre de fase 1 (`00_inventario_paquete.md`): 14:35:35.
- **Cierre de fase 2 (`01_capitulo_propio_salud.md`): 14:38:10.**
- **Primera lectura del capítulo 3 de CIEP (PDF 30–35): 16:13:50.**
- El orden se respetó. La comparación (04) es válida.

## Descargas (fase 1, obligatorias por la instrucción §2)
Ocho analíticos xlsx, verificados (cabecera `PK`), una petición cada 2 s, registrados en `_manifiesto.csv` con sha256 y tier `oficial_primaria`. Manifiesto: 50 filas (35 tras la corrida 2020 + 8 analíticos + 7 PDF de CIEP).

| archivo | hora | ruta |
|---|---|---|
| `2021/2021_ppef_analitico-ramo-programa-ur-objeto.xlsx` (9.45 MB) | 14:27:19 | `ppef.hacienda.gob.mx/work/models/PPEF2021/analiticosPresupuestarios/Proyecto/ac01_ra_pp_ur_og.xlsx` |
| `2021/2021_ppef_analitico-ramo-funcion-ur-objeto.xlsx` (6.70 MB) | 14:27:26 | ídem `ac01_ra_f_ur_og.xlsx` |
| `2021/2021_ppef_analitico-entidades-ramo-programa-ur-objeto.xlsx` (3.54 MB) | 14:27:32 | ídem `…_efe.xlsx` |
| `2021/2021_ppef_analitico-entidades-ramo-funcion-ur-objeto.xlsx` (3.26 MB) | 14:27:37 | ídem `…_efe.xlsx` |
| `2020/2020_pef_analitico-ramo-programa-ur-objeto.xlsx` (9.90 MB) | 14:27:47 | `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/2020/Autorizado/ac01_ra_pp_ur_og.xlsx` |
| `2020/2020_pef_analitico-ramo-funcion-ur-objeto.xlsx` (7.09 MB) | 14:27:56 | ídem `ac01_ra_f_ur_og.xlsx` |
| `2020/2020_pef_analitico-entidades-ramo-programa-ur-objeto.xlsx` (3.49 MB) | 14:28:02 | ídem `…_efe.xlsx` |
| `2020/2020_pef_analitico-entidades-ramo-funcion-ur-objeto.xlsx` (3.21 MB) | 14:28:07 | ídem `…_efe.xlsx` |

Los ocho se bajaron **antes** de escribir el capítulo propio, como pedía la instrucción. Motivación: base t−1 aprobada a nivel programa/UR/función (el 17 % no verificable de 2020) y perímetros de salud 2021.

**Tier provisional.** Los siete `ciep_implicaciones{2020–2026}.pdf` se registraron con tier `derivada_ciep` (origen "descarga manual (Héctor, 2026-09-05; URL no registrada)"; sha256 calculado en la corrida). Provisional: el tier es propiedad de la sección, no del documento, y la columna a nivel de sección sigue pendiente de decisión.

## Método de la fase 3
- Capítulo 3 (salud) y su párrafo del resumen: extraídos y verificados en la sesión principal (V001–V029), con los ocho analíticos cargados en pandas (pickles en scratchpad).
- Resto del documento (resumen, retos, caps. 1–2 y 4–12): extraídos y verificados por un subagente con las mismas reglas (instrucción §6, tolerancias, tipología `tipo_error`, deflactor 1.034, "no aproximes"), sin red, con el inventario y los textos oficiales por página. Sus filas (V030–V206) se consolidaron sin edición. La sesión que escribió `03` releyó el documento completo y cotejó una muestra de las filas del subagente contra el texto de CIEP y las cifras del inventario (V030, V046, V108, V134, V151, V177, V183, V186, cuadros 2, 3, 5, 12, 14): todas fieles. No se hizo cotejo exhaustivo de las derivaciones del subagente contra los analíticos.

## Conteo de afirmaciones (`02_verificacion_cifras.csv`, 206 filas; 2020: 187)

| tipo | 2021 | 2020 |
|---|---|---|
| (a) restitución | 63 | 78 |
| (b) derivación | 79 | 79 |
| (a/b) mixta | 47 | 21 |
| (c) juicio | 14 | 7 |
| (a/c), (b/c) mixtas | 3 | 2 |

| coincide | 2021 | % | 2020 | % |
|---|---|---|---|---|
| sí | 112 | 54.4 | 72 | 38.5 |
| aprox | 14 | 6.8 | 33 | 17.6 |
| no | 36 | 17.5 | 41 | 21.9 |
| no_verificable | 30 | 14.6 | 32 | 17.1 |
| vacío (juicios) | 14 | 6.8 | 9 | 4.8 |

`tipo_error` (42 filas con etiqueta: 36 `no` + 6 `aprox`): perimetro 16 (14 no + 2 aprox); contrafactual 13; transcripcion 11 (9 + 2); deflactor 2 (ambas aprox); omision 0. En 2020 la tipología no era columna; por lectura de las notas, dominaba contrafactual. **El error dominante pasó de la base al perímetro.**

Motivos de `no_verificable` (30): fuente externa al paquete (CONAPO, SESNSP, BID, SEP, ENDUTIH, planes de Pemex/SENER, padrones) 13; Informe trimestral 2T-2020 4 (V086, V090, V115, V144); Cuenta Pública / ejercido 3 (V017, V093, V136); modelo propio de CIEP 3 (V023, V026, V205); definición no declarada por CIEP 4 (espacio fiscal V034/V065, 83.7 % V066, 890→882 V089, "infraestructura" V148); iniciativas o leyes no en carpeta 2 (LGS/INSABI V010; miscelánea V188); serie 2010–2015 V181; mecanismo no documentado V018. El grupo "base PEF t−1" de 2020 (18 filas) desapareció gracias a los analíticos del PEF 2020.

Por capítulo (filas / no / no_verificable): Resumen 14/3/1; Retos 1; Deuda 14/2/0; Egresos 34/7/5; Salud 28/3/7; Educación 11/0/2; Pensiones 15/2/2; Energía 13/4/1; Federalizado 15/2/4; Inversión 17/4/2; Seguridad 13/6/1; Ingresos 15/3/3; Ingresos energía 11/0/1; Implicaciones 5/0/1. Seguridad es el capítulo con peor razón (6 de 13, todas `contrafactual`); Ingresos energía y Educación no tienen ninguna discrepancia.

## Pendientes heredados de 2020
- **9.1 (CGPE 2020 p. 129 vs p. 122): resuelto, no es contradicción.** La p. 129 habla de las "presiones ocasionadas por el pago de pensiones en curso del antiguo régimen" (costo de transición, que se extingue con las cohortes); la p. 122 proyecta "pensiones y jubilaciones" (rubro consolidado, que crece por demografía y por el propio régimen 1973 mientras dure). Dos objetos, dos trayectorias. Lo que sí queda como hueco oficial: el paquete no cuantifica el costo de transición como serie; la aportación del DEC art. 6 pasa de 344,161.7 (2020) a 409,179.3 (2021), +19 % nominal, es decir, todavía creciendo. Incorporado a `especificacion_genero.md` §6 como ejemplo canónico de por qué el perímetro debe declararse. La palabra "contradicción" no se usa.
- **9.2 (126.7 vs 120.0): resuelto hasta donde la carpeta permite.** 126,650.3 es el programa PP 176 en el analítico del PPEF 2020 (EM redondea 126.7); 129,350.3 en el PEF 2020 aprobado. 120,017.9 del Anexo 14 es una atribución transversal parcial que no coincide con ninguna partición por partida ni por tipo de gasto. Costo por beneficiario 18,491 pesos (+20.9 % sobre 15,300); sin gastos indirectos TG 7 (2,279.5 mdp) 18,158 (+18.7 %). Pago de marcha, altas y dispersión no se separan sin reglas de operación y Cuenta Pública. **Cifra congelada para calibración.** Detalle en `rubrica.md`, adenda 2021.
- La tesis del IVA de 2020 no se tocó.

## Tarea lateral (instrucción §11): analíticos 2022–2026
Solo HEAD, nada descargado (16:16–16:18). Las cinco páginas `ppef.hacienda.gob.mx/es/PPEF{t}/analiticos_presupuestarios` responden 200 y listan 25 xlsx cada una; **todos los archivos devuelven 404** (misma página de error de 2,978 bytes que los tomos). 2022–2023 enlazan a `…/analiticosPresupuestarios/Proyecto/…`; 2024–2026 a `…/analiticosPresupuestarios/…` sin `Proyecto`. Alternativa por probar: `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/` (la ruta del aprobado, que sirvió 2020). Registrado en `mapa_fuentes.md`. Implicación para 2022: si solo existe el aprobado, la comparación deja de ser proyecto contra aprobado; hay que decidirlo antes de correr.

## Fase 6
Adendas fechadas en `## Historial` de los tres archivos de `_aprendizaje/` (16:20:56): género (§6: cambios 2020→2021, comparación canónica pensiones IMSS/cuotas 1.31 → 1.46, propuesta de comparación estructural para salud, resolución 9.1); mapa de fuentes (rutas PPEF t y PEF t−1, estado 2022–2026, cuadro de dónde vive cada perímetro de salud); rúbrica (reorden, convenciones §1, `tipo_error`, casos límite de perímetro, resolución 9.2, lo que no funcionó).

## Anomalías (descritas, no resueltas)
- ISSSTE "Gastos administrativos por operación de fondos y seguros": CIEP 10,635 (2020, pesos 2021); analítico 15,113. Recurrente desde 2020 (entonces 10,283 vs 14,616). No sé qué excluye CIEP.
- Espacio fiscal 511,545 mdp / "83.7 % gastos obligatorios": ninguna combinación de líneas de ILIF/EM reproduce ninguna de las dos.
- "De 890 a 882 programas": ningún conteo del analítico (pares ramo×PP 662 → 614; códigos únicos 512 → 468) da esas cifras.
- Capítulo 9: todas las tasas "reales" caen entre la real y la nominal calculadas con el analítico; no hay cuadro con 2020. Hipótesis: base 2020 distinta (¿modificado?) no declarada.
- Deuda no presupuestaria "+285 %": no reproducible contra ninguna línea del cuadro de RFSP de CGPE 2020 ni 2021.
- Discrepancias **entre fuentes oficiales**: INEGI 7,393.6 (EM p. 203) vs 7,746.1 (analítico); SCT base 2020 55,830.2 (EM) vs 56,222.7 (analítico); aeropuerto 21,314.8 (CGPE p. 54) vs 21,814.8 (analítico PP 019 Defensa); petroleros 936,765.4 (CGPE) vs 936,708.4 (ILIF art. 1o.); PIB del aprobado 2020 presentado con dos denominadores (CGPE p. 110 vs p. 13/103). CIEP sigue al analítico en los tres primeros.
- Internet para Todos 1,986.2 (CIEP) vs 2,485.6 (analítico CFE PP 583); ningún subconjunto por capítulo da la cifra.
- IMSS "Estudios de preinversión 0 → 10" y "Mantenimiento 949 → 0" del cuadro 8: no verificados (programas fuera de la lista principal del analítico de entidades).
- CIEP aplica ≈1.0342 en lugar de 1.034: consistente en todo el documento, no declarado.
- Erratas del original: "−8-8", "ILIF 2020" por 2021, "LIF 2021" por 2020, "SHCP (2029)", "mdp" por mmp (p. 56), "pesos reales" por mdp (p. viii, 40), "aportaciones y aportaciones" (p. 40), "−56.33".
- Del propio capítulo (04): tenía UR y EF en los analíticos y no construí ni el cuadro de UR ni el FASSA por entidad.

## Lo que debería cambiar en la instrucción para 2022
1. **Fuentes.** Decidir si entran los Informes trimestrales (2T de t−1) y la Cuenta Pública (t−2): CIEP compara contra "modificado" y "ejercido" en 7 afirmaciones que hoy quedan `no_verificable`. Es decisión de alcance.
2. **Analíticos t.** Si el árbol PPEF sigue en 404, fijar antes de correr qué sustituye al proyecto (aprobado con etiqueta, o Transparencia Presupuestaria) y cómo se declara el contrafactual resultante.
3. **CSV.** Columna booleana `contrafactual_explicito` por fila comparativa; el conteo del criterio 1 sigue siendo manual y sensible a la agrupación.
4. **Capítulo propio.** Exigir cuadro de UR con variación y distribución territorial cuando el rubro tenga fondo federalizado; exigir un diff de códigos PP/UR/SF entre t−1 y t antes de escribir, para anticipar reclasificaciones (Seguro Popular → INSABI rompió la serie por subfunción).
5. **ILIF en el inventario del rubro.** Leer los transitorios de la ILIF como parte del inventario de salud: la única cifra oficial del FONSABI estaba ahí y no en el PPEF.
6. **Perímetro de salud.** Fijar el cuadro de la EM p. 67–68 como perímetro canónico de FISCUS (siete líneas, dos bloques), Pemex como partida informativa. Hoy es decisión de la corrida, no convención.
7. **Método de extracción.** Admitir explícitamente el reparto (rubro propio en sesión principal, resto por subagente) y exigir un cotejo mínimo de las filas delegadas (todas las `no` y una muestra de las `si`) contra los analíticos, no solo contra el texto.
8. **Tier por sección.** Sigue pendiente; `derivada_ciep` a nivel documento es provisional.

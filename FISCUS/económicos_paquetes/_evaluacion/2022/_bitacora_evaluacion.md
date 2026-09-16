# Bitácora — evaluación del documento CIEP, ejercicio 2022

## Corrida
- Inicio: 2026-09-05T22:55:03-06:00 (extracción de texto de CGPE, ILIF, DEC y CIEP 2022; ILIF 2021 tomada del scratchpad de la corrida 2021).
- Fin: 2026-09-05T23:40:00-06:00 (aprox.; escritura de esta bitácora y del memo).
- Máquina: Dalila. Herramientas: pdftotext (poppler), python3; un subagente de extracción para los capítulos distintos de ingresos (ver "Método").
- CIEP: `2022/ciep_implicaciones2022.pdf`, 96 páginas PDF, sha256 `8f0d86f8…997fb05`, fecha en portada 17-sep-2021, registrado como `derivada_ciep`. Paginación: impresa = PDF − 12 en capítulos; resumen PDF 7–10; introducción PDF 11–12; Parte I (caps. 1–2) PDF 15–24; cap. 3 PDF 27; cap. 13 PDF 76; cap. 14 PDF 82.
- Capítulo propio: **ingresos** (instrucción 2022 §0). Cambio deliberado de Parte II a Parte I.

## Orden de fases (obligatorio)
- Índice general de CIEP (PDF 4–6) leído a las 22:56. **Declaración de contaminación:** el comando que extrajo el índice imprimió también las líneas siguientes del texto, que contienen el primer bloque del resumen ejecutivo (p. vii): ingresos 21.9 % del PIB, 14.0 pp de impuestos, 6,172,635 mdp, +0.6 pp respecto a la LIF 2021, "crecimiento optimista 6.3 / 4.1", "miscelánea sin expectativas de aumento sustancial", "mayor tolerancia al endeudamiento", "desaparece la idea de reforma fiscal integral". La lectura se detuvo ahí. Todas las cifras son restituciones del CGPE que el capítulo propio obtiene de la fuente; los tres juicios no se usaron. La instrucción 2022 no citaba cifras de CIEP.
- Cierre de fase 1 (`00_inventario_paquete.md`, con diff §4 y reconciliación §5): 23:05:42.
- **Cierre de fase 2 (`01_capitulo_propio_ingresos.md`): 23:08:49.**
- **Primera lectura de los capítulos 1 y 2 de CIEP (PDF 15–26): 23:09:04.** En el mismo momento se leyeron el resumen completo, la introducción y el capítulo 14.
- El orden se respetó. La comparación (04) es válida con la salvedad declarada.

## Descargas y rutas
- **Nada descargado.** Verificación de la ILIF (instrucción §4): completa, 124 páginas, exposición I–LVIII, articulado art. 1o. en PDF 59, art. 16 en PDF 96, transitorios PDF 118–124.
- Intentos (HEAD, una petición cada 2 s): EM del PPEF 2022 (`docs/exposicion/EM_Documento_Completo.pdf`, `EM_Capitulo_1.pdf`) 404 a las 22:56:51; miscelánea (`paquete/ingresos/LISR_LIVA_LIEPS_CFF.pdf`), LFD (`LFD_2022.pdf`) y LIF (`LIF_2022.pdf`) en `ppef.hacienda.gob.mx/work/models/PPEF2022/` 404 a las 23:01:41.
- Consecuencia: sin cuentas dobles, sin pensiones por institución, sin programas ni UR, sin impacto recaudatorio de la miscelánea. Registrado en `mapa_fuentes.md`.
- Manifiesto sin cambios (50 filas).

## Método de la fase 3
- Parte I (caps. 1–2), los cuatro párrafos de ingresos del resumen, el cuadro macro y los párrafos de crecimiento de la introducción: extraídos y verificados en la sesión principal (V001–V061).
- Resto (resumen sin ingresos, introducción "Un año después" y "Visión 2022", caps. 3–14): subagente con las mismas reglas, las columnas nuevas, la convención 1.037, las dos presentaciones del PIB 2021 y los textos oficiales 2022 y 2021 por página (V062–V258). Sus filas se consolidaron sin edición.
- **Cotejo mínimo (instrucción §1.5), hecho contra las fuentes y no solo contra el texto de CIEP:** las 25 filas `no` del subagente se cotejaron contra CGPE p. 100 (PIB 2024), p. 112 (SHRFSP +0.5), p. 118 (SCT, Marina, Economía, Bienestar, Entidades no sectorizadas, CFE), p. 120 (RFSP 3.5), p. 48–49 (Tren Maya 68.0; 63,231.6), DEC 2022 Anexo 1 (Pemex, CFE, neteo 1,023,474.8), Anexo 20 (73,000; 20,424.1), DEC 2021 Anexo 1 y Anexo 20 (SCT 55,919.6; Marina 35,476.7; Economía 6,538.5; no sectorizadas 12,213.9; 70,000; 18,890.8), y con aritmética propia (8.9 vs 8.6; 2.26 y 1.60 % del PIB; −20.5 %; 28,500 × 1.037). Las 25 se sostienen. Muestra de `si` cotejada: V119–V129 y V135–V144 contra CGPE p. 118; V181–V183 contra DEC Anexo 22 (FONE 424,326.2; FASSA 117,537.2; FAIS 94,321.0; FORTAMUN 95,547.8; FAFEF 52,205.8) y CGPE p. 50; V243–V248 contra CGPE p. 42 y CGPE 2021 p. 49; V089 y V233 contra CGPE p. 49 y 51: todas fieles.

## Conteo de afirmaciones (`02_verificacion_cifras.csv`, 258 filas; 2021: 206; 2020: 187)

| tipo | 2022 | 2021 | 2020 |
|---|---|---|---|
| (a) restitución | 56 | 63 | 78 |
| (b) derivación | 81 | 79 | 79 |
| (a/b) mixta | 76 | 47 | 21 |
| (c) juicio | 17 | 14 | 7 |
| mixtas con juicio | 28 | 3 | 2 |

| coincide | 2022 | % | 2021 | % | 2020 | % |
|---|---|---|---|---|---|---|
| sí | 88 | 34.1 | 112 | 54.4 | 72 | 38.5 |
| aprox | 14 | 5.4 | 14 | 6.8 | 33 | 17.6 |
| no | 33 | 12.8 | 36 | 17.5 | 41 | 21.9 |
| no_verificable | 105 | 40.7 | 30 | 14.6 | 32 | 17.1 |
| vacío (juicios) | 18 | 7.0 | 14 | 6.8 | 9 | 4.8 |

**Sobre lo verificable** (sí + aprox + no): 2022 135 filas: sí 65 %, aprox 10 %, no 24 %; 2021 162: 69 / 9 / 22; 2020 146: 49 / 23 / 28. La tasa de discrepancia sobre lo verificable es la misma en 2021 y 2022; lo que cambia en 2022 es el tamaño de lo no verificable (41 %), que es un hecho de la carpeta (EM y analíticos ausentes: 43 filas; fuentes externas: 29; ex post: 20; miscelánea: 3), no del documento.

`tipo_error` (33 filas `no`): **transcripcion 14**, contrafactual 10, perimetro 7, deflactor 2, omision 0. Serie: 2021 perimetro 16 / contrafactual 13 / transcripcion 11 / deflactor 2; 2020 (por lectura de notas) contrafactual dominante. En 2022 domina la transcripción: rótulos de columna, % del PIB copiados de otra fila, cifras del resumen que contradicen al capítulo (DUC 58/54; Tren Maya 63.7/67.3; CFE 6.5/4.0; IMSS-ISSSTE −4.2/−21).

**Parte I (ingresos, 61 filas):** sí 33, no_verificable 9, no 8 (transcripcion 6, contrafactual 2), aprox 4, juicio 7. Ningún error de perímetro. Los dos `contrafactual` son la tesis del capítulo (elasticidad, V018) y la "recuperación de 63 %" del FMP (V053). **¿Un género o dos?** Sobre lo verificable, ingresos 65 % sí / 16 % no y gasto 65 % sí / 26 % no; la distribución de errores difiere (ingresos sin perímetro, gasto con perímetro y bases mezcladas) pero la tasa no. La instrucción preguntaba si tendríamos "un patrón del género" o "dos géneros": el patrón de acierto es uno; el tipo de error depende del objeto (en ingresos el objeto es una participación o una elasticidad y el error es de base o de copia; en gasto es un monto por ramo y el error es de perímetro).

`tier_seccion`: restitucion 171 (sí 70, no_verificable 62, no 26, aprox 10, vacío 3); juicio 64 (no_verificable 25, sí 18, vacío 14, no 5, aprox 2); mixta 23 (no_verificable 18, aprox 2, no 2, vacío 1). Las secciones "Incidencia" son casi enteramente no verificables (fuentes externas): 18 de 23.

`contrafactual_explicito`: 144 comparativas, 98 explícitas (68 %), 46 incompletas (32 %); por capítulo, salud 10, educación 5, energía-ingresos 4, resumen 4, gasto 4, federalizado 3, pensiones 3, deuda 3. En 2021 el conteo manual dio 20 %.

## Tareas laterales
- **11.1 Rutas de analíticos 2022–2026 (23:16:09, solo HEAD).** `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/ac01_ra_pp_ur_og.xlsx` responde **200 con content-type xlsx para 2022, 2023, 2024, 2025 y 2026**. Las páginas `pef.hacienda.gob.mx/es/PEF{t}/analiticos_presupuestarios` responden 200 (los enlaces no se detectan con `href="…xlsx"`; navegar antes de descargar). La ruta del proyecto (`ppef.hacienda.gob.mx/work/models/PPEF{t}/analiticosPresupuestarios/…`) sigue en 404. `transparenciapresupuestaria.gob.mx/es/PTP/Datos_Abiertos` responde 200; no explorada. **Nada descargado.** Registrado en `mapa_fuentes.md`. Implicación para 2023: existe el aprobado a nivel programa/UR/función para 2022–2026, no el proyecto; la decisión aprobado contra aprobado con etiqueta queda para la instrucción 2023 (§1.3).
- **11.2 Serie pensiones IMSS / cuotas IMSS.** Cuotas IMSS 2022: 411,852.5 mdp (ILIF art. 1o. numeral 2). Gasto en pensiones del IMSS 2022: **no computable** con la carpeta (vive en la exposición de motivos del PPEF, cuentas dobles / pensiones por institución, ausente). La razón queda: 2020 1.31; 2021 1.46; 2022 pendiente. Como referencia distinta y etiquetada, no como sustituto: aportación del Gobierno Federal para pensiones en curso de pago del régimen 1973 (DEC art. 5) 474,317.2 mdp = 1.15 × las cuotas (2021: 409,179.3 = 1.07 ×).

## Reconciliación y diff (instrucción §6.2–6.3)
- ILIF art. 1o. ↔ CGPE IV.6: reconcilia por completo con una reclasificación de 56.9 mdp de "impuestos" (ILIF) a "petroleros del Gobierno Federal" (CGPE), no explicada en ningún documento; hipótesis: ISR de contratistas y asignatarios; mismo monto (57.0) en 2021. Identidades ingreso = gasto, déficit y diferimiento cierran exactamente (inventario §5).
- Diff ILIF 2021 → 2022: sin ruptura en los grandes rubros; renumeración de derechos por servicios (FGR sale, Bienestar entra); exclusión de inversión 2.2 → 3.1 % del PIB con cobertura ampliada; desaparecen los arts. 22 (CNBV) y 23 (estímulo al RIF) de 2021 y aparece el art. 22 (DUC 40 %); tasa de retención 0.97 → 0.08; estímulo nuevo a libros; transitorios 14 → 16 (Lotería, FONSABI remanente sin cifra, FEIEF, IMSS-Bienestar con FASSA); "Presupuesto de Gastos Fiscales" pasa a llamarse "Renuncias Recaudatorias"; estímulos fiscales 75,985 → 260,466 mdp (inventario §4).

## Anomalías (descritas, no resueltas)
- 56.9 mdp reclasificados entre ILIF y CGPE sin nota; la hipótesis (ISR petrolero) requiere la nota metodológica "Balance Fiscal en México" (abril 2021), no en carpeta.
- "Otros aprovechamientos" 179,329.1 (0.64 % del PIB, +19.7 % real) sin origen; tres transitorios sin monto (FONSABI remanente, Lotería, rendimientos de fideicomisos) como candidatos; la propia ILIF ordena informarlo ex post.
- Costo recaudatorio del DUC 54 → 40 %: no cuantificado en CGPE ni ILIF; la exposición afirma que "no representa un riesgo".
- Cuotas IMSS +4.0 % real con reforma de subcontratación y 20.3 millones de afiliados: el paquete cuantifica la reforma (21 mmp de evasión; 2.83 mmp INFONAVIT) y no la vincula con el renglón.
- Dos presentaciones oficiales del aprobado 2021 (PIB de aprobación vs revisado) que invierten el signo de las comparaciones en % del PIB (ingresos −0.3 / +0.6 pp; gasto 0.0 / +1.0).
- Dos bases oficiales 2021 por ramo (PPEF y PEF en CGPE p. 118) que difieren en SCT, Marina, Economía y Bienestar; CIEP usa una u otra sin declararlo.
- CIEP cuadro 1.1: último tramo del RSC 3.0 % contra 2.5 % del CGPE y del propio texto de CIEP; su fuente (miscelánea) no está en carpeta.
- CIEP: 10.2 millones de contribuyentes potenciales del RSC (SHCP) contra 21 millones de "universo potencial" en CGPE p. 44: objetos distintos, ninguno en la ILIF.
- CIEP cuadro 11.1: montos de Pemex, CFE y Sener que no coinciden con el Anexo 1 en ninguna combinación programable / costo financiero.
- CIEP cuadro 3.3: "gasto bruto" igual al neto y neteo de 123,025.3 no identificable.
- CGPE p. 40: "apoyos a los programas de deudores por −0.1 % del PIB" mientras el cuadro p. 102 pone +0.1 en 2022.
- Erratas del original CIEP: "PPEF 2020" (p. viii, 15), "cierre de 20221" (p. vii), "proyectado para 2021" (p. 28), "aprobado en 2022" (p. 54), cuadro 2.1 "ILIF 2021 / LIF 2020", cuadro 13.1 "Aprobado 2020 / Propuesto 2021", cuadro 10.1 con fuente "ILIF 2021", "8962.2" (cuadro 9.1), "6.4 %" (cuadro 10.1).
- Del propio capítulo (04): no probé rutas alternativas para la miscelánea (Gaceta Parlamentaria) ni reconstruí la trayectoria del DUC con los decretos del DOF.

## Lo que debería cambiar en la instrucción para 2023 (deuda y balance)
1. **Nivel de carpeta declarado en fase 1.** Antes de escribir, listar qué piezas del paquete faltan (en 2022: EM, miscelánea, LFD) y qué criterios quedan condicionados. El 41 % no verificable de 2022 es de la carpeta, y la rúbrica debe distinguirlo del documento.
2. **Analíticos.** Decidir aprobado contra aprobado con etiqueta para 2022–2026 (la ruta del PEF autorizado sirve; la del PPEF no), o buscar el proyecto en Transparencia Presupuestaria. Sin eso, ningún capítulo de gasto de 2023 en adelante puede verificar programas.
3. **Quinta declaración del contrafactual para razones a PIB:** con qué PIB para cada año, cuando el año base tiene PIB revisado. Lo pide el caso de 2022 (signo invertido) y lo pedirá cualquier año con revisión.
4. **Para deuda:** exigir en el inventario las tres presentaciones del saldo (SHRFSP, deuda neta, deuda bruta del sector público no financiero: 51.0 / 49.7 / 58.6 en 2022), el perfil de amortizaciones (CGPE III.3), los indicadores del portafolio (p. 56), la posición financiera neta (p. 86) y los techos por entidad (ILIF art. 2o.; Pemex y CFE por separado); y distinguir techo de endeudamiento (ILIF) de déficit del GF (CGPE), que en 2022 valen ambos "850 mil".
5. **Frente del documento como objeto propio.** El resumen y la introducción contradicen a los capítulos en cuatro cifras (DUC, Tren Maya, CFE, IMSS-ISSSTE); la verificación del frente no puede darse por restitución del capítulo.
6. **Miscelánea y decretos de estímulo a Pemex** como piezas de la carpeta de ingresos, con ruta alternativa (Gaceta Parlamentaria; DOF), si se vuelve a evaluar ingresos.
7. **Subagente:** el reparto funcionó por segunda vez; el cotejo de las `no` contra fuentes tomó 15 minutos y no encontró fallas. Mantener y añadir el cotejo de una muestra de `no_verificable` para confirmar que la fuente que se declara ausente lo está.

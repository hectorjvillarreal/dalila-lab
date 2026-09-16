# Bitácora — evaluación del documento CIEP, ejercicio 2020

## Corrida
- Inicio: 2026-09-05T12:17:21-06:00 (extracción de texto de los cinco PDF de `2020/`).
- Fin: 2026-09-05T13:05:16-06:00 (escritura de artefactos).
- Máquina: Dalila. Herramientas: pdftotext (poppler), python3 y pandas/openpyxl en el entorno `dalila`.
- CIEP: `2020/ciep_implicaciones2020.pdf`, 105 páginas PDF, sha256 `327c7e28…53b47f`, fecha en portada 11-sep-2019. Paginación: impresa = PDF − 16 en capítulos.

## Orden de fases (obligatorio)
- Índice general de CIEP (PDF 14–16) leído a las 12:19. **Declaración:** al buscar el índice se imprimieron también las PDF 2–5; la 5 contiene el primer párrafo de "Implicaciones" (ingresos) y se leyó antes de la fase 2. No contiene cifras de pensiones. Además, la instrucción de trabajo cita el "4.2 %", "absorbe toda la recaudación del IVA" y "faltante de 100 mil millones": la derivación de ese agregado no fue ciega.
- Cierre de fase 1 (`00_inventario_paquete.md`): 12:25:00.
- **Cierre de fase 2 (`01_capitulo_propio_pensiones.md`): 12:26:55.**
- **Primera lectura del capítulo 7 de CIEP (PDF 68–72): 12:27:29.**
- El orden se respetó. La corrida es válida con la salvedad declarada arriba.

## Descargas por demanda (sección 7 de la instrucción)
Los Tomos PDF del PPEF 2020 no son alcanzables (`/work/models/PPEF2020/docs/…` y `/paquete/…` devuelven 404, ver `_bitacora.md` de adquisición). La página de analíticos presupuestarios sí responde y sus xlsx se sirven. Se descargaron cuatro archivos, verificados (cabecera `PK` de xlsx), registrados en `_manifiesto.csv` con sha256 y tier `oficial_primaria`, guardados en `2020/` con nomenclatura `2020_ppef_analitico-…xlsx`:

| archivo | hora | verificación que lo motivó |
|---|---|---|
| `2020_ppef_analitico-ramo-programa-ur-objeto.xlsx` (`ac01_ra_pp_ur_og.xlsx`, 9.98 MB) | 12:32:40 | cuadro 3.1 de CIEP (18 programas prioritarios) y programas de salud del cuadro 4.2; Ramo 19 por programa; SSPC por UR |
| `2020_ppef_analitico-ramo-funcion-ur-objeto.xlsx` (`ac01_ra_f_ur_og.xlsx`, 7.14 MB) | 12:32:45 | perímetros de CIEP para salud (656,761), educación (807,305), seguridad (284,137) y función Combustibles y Energía |
| `2020_ppef_analitico-entidades-ramo-programa-ur-objeto.xlsx` (`…_efe.xlsx`, 3.53 MB) | 12:36:15 | programas de IMSS/ISSSTE (cuadro 4.2), Pemex y CFE (cap. 8), inversión pública cap. 6000 (cap. 5) |
| `2020_ppef_analitico-entidades-ramo-funcion-ur-objeto.xlsx` (`…_efe.xlsx`, 3.26 MB) | 12:36:20 | función salud de IMSS/ISSSTE; función C&E de Pemex/CFE |

La sección 7 pide `.pdf`; los analíticos son xlsx. Se juzgó dentro del espíritu de la regla (fuente oficial SHCP, un archivo por necesidad demostrada). Una petición cada 2 s.

## Conteo de afirmaciones (`02_verificacion_cifras.csv`, 187 filas)

| tipo | filas |
|---|---|
| (a) restitución | 78 |
| (b) derivación | 79 |
| (a/b) mixta | 21 |
| (c) juicio | 7 |
| (a/c) mixta | 2 |

| coincide | filas |
|---|---|
| sí | 72 |
| aprox (≤0.2 pp o ≤0.5 %, deflactor/redondeo) | 33 |
| no | 41 |
| no_verificable | 32 |
| vacío (juicios) | 9 |

Motivos de `no_verificable` (32): base PEF 2019 en pesos de 2020 (18), Cuentas Públicas 2013–2018 (5), fuentes externas al paquete (CONAPO, SENER, OMS, SEP, informes Pemex) (5), miscelánea fiscal y decreto de DUC (2), modelo propio de CIEP (2). Para 2021 el primer grupo se resuelve descargando también el analítico del PEF t−1.

## Hallazgos que conviene destacar (evidencia en el CSV)
- V102: el anexo "Programas para superar la pobreza" existe en la EM (p. 215, 470,626 mdp); CIEP lo da por desaparecido y deriva de ahí un −13.6 % y un "cambio de estrategia".
- V015/V048/V056: la tesis de "debilidad no explicada del IVA" se sostiene contra el aprobado 2019 y no contra el cierre estimado 2019 que el texto declara (oficial: +3.6 % real).
- V003/V004: "casi 97 % contributivo" y "aprox. 7 %" contradicen al propio capítulo 7 (87.5 %, 6.2 %).
- V059–V063: ninguna tasa real del cuadro 2.1 coincide con CGPE p. 86.
- V076: "6.5 % del gasto total" es 6.5 % del PIB.
- V105, V108: dos cifras aparentemente extrañas (Ramo 19 = 137,614; "cuotas ISSSTE" = 120,020) se reproducen exactamente como neteos de líneas oficiales.
- V088: el +17,250 en Coordinación de la Política de Gobierno es el INE, que en la base 2019 de CIEP aparece vacío.
- V178–V184: el capítulo de deuda mezcla aprobado y estimado, usa 2.9 % de costo financiero (oficial 2020: 2.8) y la deuda per cápita adicional no cierra ($1,705 implica 0.83 % del PIB, no 0.3).

## Anomalías (descritas, no resueltas)
- Analíticos: el ISSSTE "Gastos administrativos por operación de fondos" da 14,616.1 en 2020; CIEP 10,283. No sé si CIEP excluye alguna UR o si hubo una versión posterior del analítico.
- Pensión para el Bienestar de las Personas con Discapacidad: EM p. 215 dice 11.6 mmp; analítico y DEC Anexo 14 dan 11,905.9 / 11,187.2; CIEP 11,906. La EM parece citar la porción del anexo pobreza como si fuera el programa.
- Pensión adultos mayores: EM 126.7 mmp; Anexo 14 120.0; Anexo 11 80.8; Anexo 13 38.8; Anexo 10 33.6. Consistente con atribuciones parciales, pero el anexo de grupos vulnerables debería contener el programa completo.
- CIEP repite 30,475 para dos becas y 28,995 para dos programas; son erratas cruzadas (los valores correctos son 30,475 básica / 28,995 media superior / 7,776 JEF).
- CIEP 10.3 (p. 74): "desaparición del programa Aportaciones federales… 789,826.7 mdp" en el Ramo 28. No existe tal programa en el Ramo 28 en 2020 ni la cifra es localizable.
- Cuadros 3.3/3.4 de CIEP dan bases 2019 ~0.03 % por encima de las de la EM: deflactor distinto no declarado.
- Salud: la EM p. 190 da función salud 634,388.2 (consolidado neto) y CIEP 656,761 (bruto con SSA por ramo). Ambos correctos, perímetros distintos; ningún lector lo sabría por el documento.
- Texto de CIEP con ligaduras (ﬁ) y palabras pegadas en el PDF; tres saltos "sección ??" (p. 22) indican referencia rota en el original.

## Lo que debería cambiar en la instrucción para 2021
1. Autorizar y pedir en fase 1 la descarga de los cuatro analíticos del PPEF t **y** del PEF t−1 (`pef.hacienda.gob.mx`). Sin t−1 el 17 % de las afirmaciones queda sin verificar y el capítulo propio no puede hablar de programas.
2. Admitir xlsx/csv en la sección 7 y fijar nomenclatura `{año}_ppef_analitico-{slug}.xlsx`.
3. Fase 2: permitir usar los analíticos (son oficiales) para el capítulo propio; hoy la instrucción sugiere que solo la carpeta de PDF cuenta.
4. Definir en la instrucción el umbral "aprox" y las cuatro dimensiones del contrafactual, para que el conteo del criterio 2 sea comparable entre años.
5. Añadir al criterio 1 una lista mínima de cifras que deben buscarse (pasivo pensionario, cláusula de excepción, gastos fiscales, techo de deuda, meta de Pemex, anexo pobreza).
6. Pedir que la fase 3 registre, por afirmación, si el error es de transcripción, de contrafactual, de perímetro o de omisión; en 2020 esa tipología surgió sola y sería útil como columna.
7. Advertir que el árbol de Tomos puede estar caído y que los analíticos viven en otra ruta.

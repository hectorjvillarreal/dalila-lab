# Bitácora — evaluación del documento CIEP, ejercicio 2023

## Corrida
- Inicio: 2026-09-06T09:17:58-06:00 (extracción de texto de CGPE, ILIF y DEC 2023, ILIF y DEC 2022, CGPE 2022 y 2024, CIEP 2023).
- Fin: 2026-09-06T15:50:00-06:00 (aprox.). Pausa forzada de ~10:00 a ~15:30 por límite de sesión del modelo (HTTP 429); el subagente terminó durante la pausa. Trabajo efectivo: 09:18–10:00 y 15:35–15:50.
- Máquina: Dalila. Herramientas: pdftotext y pdftoppm (poppler), python3 (pandas/openpyxl del env `dalila` para los xlsx), curl con el bundle de certificados de la bitácora general, Wayback Machine; un subagente de extracción y verificación para los capítulos 1–10.
- CIEP: `2023/ciep_implicaciones2023.pdf`, 103 páginas PDF, sha256 `f5d45902…`, `derivada_ciep`. **37 páginas son imagen sin capa de texto** (portadas y láminas infográficas, incluidas las de deuda PDF 80 y 85); se leyeron como PNG a 110 dpi. Paginación: impresa = PDF − 12 en capítulos; frente PDF 6–11; Parte III PDF 79–89 (caps. 11 y 12); Parte IV PDF 91–94 (cap. 13).
- Capítulo propio: **deuda y balance** (instrucción 2023 v2). Se cierran las tres partes del género.

## Orden de fases (obligatorio)
- Índice de CIEP (PDF 3–5) leído a las 09:18, filtrado por líneas con puntos de guía: sin contaminación (no se imprimió texto del resumen).
- Cierre de fase 1 (`00_inventario_paquete.md`): 09:36:48.
- **Cierre de fase 2 (`01_capitulo_propio_deuda.md`): 09:41:02.**
- **Primera lectura del frente, de los capítulos 11–12 y del capítulo 13 de CIEP: 09:41:22.**
- El orden se respetó; la comparación (04) es válida.

## Descargas y rutas (motivo de cada una)
- **SHCP, Balance Fiscal en México, abril 2023** (instrucción §5.2.1): ruta canónica sirve la edición 2026; Wayback sin 2023; obtenida de la Gaceta Parlamentaria (`Shcp_balanceF-20230509.pdf`, 44 pp, escaneo; sha256 `9b044dd5…`; 09:25:07). Cotejo visual de pp. 3–4, 26, 40–41 contra la edición 2022 con texto (Gaceta `Shcp-20220503.pdf`, descargada como auxiliar, no registrada). Registrada en `_manifiesto.csv` como `oficial_primaria`, ejercicio `na`, carpeta `_metodologia/`.
- **Cantú, Ramones y Villarreal (2016)** (§5.2.2): ruta viva 404; obtenida del Wayback (captura 2025-10-18; 26 pp; sha256 `ecc85b10…`; 09:29:25). Registrada como **`autoral_ited`**: **el vocabulario de tier pasa de dos a tres valores**; la decisión de tier por sección (`tier_seccion`) sigue pendiente y debe resolverse junto con esta ampliación (Héctor con Clavellina).
- **PEF aprobado, analíticos de entidades 2022 y 2023** (§10.2, reintento de la serie pensiones IMSS / cuotas): `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/ac01_ra_pp_ur_og_efe.xlsx` (3.4 y 2.9 MB; 09:27). Registrados, `oficial_primaria`, en `2022/` y `2023/`. El subagente los usó además como base 2022 y para IMSS/ISSSTE/Pemex/CFE 2023, etiquetando "aprobado, no proyecto".
- DOF (§10.3): decretos 5581294 (09-12-2019) y 5609025 (28-12-2020) leídos en HTML (`dof.gob.mx` sin `www`); no se guardaron como piezas.
- **Sonda a Transparencia Presupuestaria (§10.1, 09:26:44):** `…/es/PTP/Datos_Abiertos` 200 (cáscara JS de 1.9 KB sin enlaces); tres rutas adivinadas de zip 404. Nada descargado. Registrado en `mapa_fuentes.md`. Decisión sobre analíticos diferida a 2024, como manda §2.2.
- Manifiesto: 50 → **55 filas** (cuatro nuevas más… ver nota: 51 tras 2022 era 50 filas de datos; ahora 54 de datos + encabezado).
- Nada dentro de `2023/` se modificó salvo el analítico agregado y su fila.

## Método de la fase 3
- Sesión principal: Presentación, Resumen ejecutivo, caps. 11, 12 y 13 (V001–V078), con los PNG de las láminas y de las páginas con figuras (PDF 80, 82, 83, 85, 87, 88).
- Subagente: caps. 1–10 (V101–V398, 298 filas), con las mismas reglas, el valor `objeto`, la quinta declaración y los analíticos del PEF aprobado. Sus filas se consolidaron sin edición.
- **Cotejo (instrucción §3):** las 39 filas `no` del subagente se revisaron por lectura y una muestra aritmética se rehízo contra las fuentes: V123 (24.05), V126 (91.06), V145 (0.89 / 0.66), V163 (28.5 / 23.3), V174 (1.70), V240 (2.16 / 1.40), V199 (3.4), V216 (3.57), V395 (335,499.4; 15.9×), V129 (CGPE p. 74: sistema renta +15.3), V359 (CGPE p. 80: +15.6). Todas se sostienen. Muestra de `si`: V211 (22.7), V286 participaciones, V273 ISSSTE 18.3, cotejadas por aritmética propia. Muestra de `no_verificable`: V019, V025, V029 y las de educación (cap. 7, 23 de 32 filas) requieren analíticos del proyecto o Tomo I, confirmados ausentes (404 el 2026-09-05 y sonda TP 2026-09-06).

## Resultado de la validación 2022 (instrucción §6.3) — primero que nada
**Reprodujo el signo y el orden de magnitud.** Con la añada del CGPE 2024 (SHRFSPF 49.2 → 47.7, RFSPF 4.3, crecimiento 3.9, deflactor 6.7, tipo de cambio −0.9, activos −0.3) el marco da **−1.72 pp contra −1.5 observado** (residuo +0.2, del tamaño del redondeo de los componentes oficiales de la ILIF 2024: −4.8 + 4.5 − 0.3 − 0.1 − 0.8). Las otras dos añadas del mismo tránsito (SHCP 2023 Anexo IV: 50.8 → 49.4, −1.4; instrucción: 50.7 → 49.4, −1.3) dan el mismo signo y magnitud. Reparto: crecimiento −1.7; inflación neta −0.1 (denominador −3.1, compensación pagada +3.0); tasa real +0.8 (cota alta) a −0.2 (cota baja); tipo de cambio −0.9; primario y resto +0.5 a +1.5; activos −0.3. **La narrativa de la instrucción ("inflación alta" como factor de la caída) es correcta solo para el denominador.** Aplicado a 2023: +0.4 (CGPE +0.5), con la tasa real (+1.4) como variable dominante.

## Conteo de afirmaciones (`02_verificacion_cifras.csv`, 376 filas; 2022: 258; 2021: 206; 2020: 187)

| tipo | 2023 | 2022 | 2021 | 2020 |
|---|---|---|---|---|
| (a) restitución | 76 | 56 | 63 | 78 |
| (b) derivación | 172 | 81 | 79 | 79 |
| (a/b) mixta | 72 | 76 | 47 | 21 |
| (c) juicio | 33 | 17 | 14 | 7 |
| mixtas con juicio (a/c, b/c) | 23 | 28 | 3 | 2 |

| coincide | 2023 | % | 2022 | % | 2021 | % | 2020 | % |
|---|---|---|---|---|---|---|---|---|
| sí | 113 | 30.1 | 88 | 34.1 | 112 | 54.4 | 72 | 38.5 |
| aprox | 65 | 17.3 | 14 | 5.4 | 14 | 6.8 | 33 | 17.6 |
| no | 53 | 14.1 | 33 | 12.8 | 36 | 17.5 | 41 | 21.9 |
| no_verificable | 111 | 29.5 | 105 | 40.7 | 30 | 14.6 | 32 | 17.1 |
| vacío (juicios) | 34 | 9.0 | 18 | 7.0 | 14 | 6.8 | 9 | 4.8 |

**Sobre lo verificable** (231 filas): sí 49 %, aprox 28 %, no 23 % (2022: 65 / 10 / 24; 2021: 69 / 9 / 22; 2020: 49 / 23 / 28). La tasa de discrepancia sobre lo verificable es la de siempre (22–28 %); lo que cambia en 2023 es el peso de `aprox` (28 %), casi todo por el deflactor 1.0492 de CIEP contra 1.0497 del CGPE, es decir, décimas. `no_verificable` baja de 41 % a 29.5 % gracias a los analíticos del aprobado y a que deuda casi no los necesita; 72 % de lo no verificable sigue siendo carpeta (EM, Tomo I, analíticos del proyecto, iniciativas), no documento.

**`tipo_error` (53 filas `no`): transcripción 29, perímetro 8, objeto 7, contrafactual 6, omisión 3, deflactor 0.** Serie: 2022 transcripción 14 / contrafactual 10 / perímetro 7 / deflactor 2; 2021 perímetro 16 / contrafactual 13 / transcripción 11; 2020 contrafactual dominante. **Capítulos de deuda (11–12, 35 filas): sí 10, aprox 7, no 10, no_verificable 6, juicio 2; de los `no`: objeto 4, transcripción 4, contrafactual 1, omisión 1.** ¿Se parece a alguno o es un cuarto patrón? Sobre lo verificable, deuda da 37 % sí / 26 % aprox / 37 % no: la tasa de discrepancia es mayor que en cualquier parte anterior, y el tipo de error es nuevo: **el objeto** (con cifra correcta) es el primero, empatado con la transcripción, y el perímetro desaparece. Es un cuarto patrón, el que la instrucción anticipó: en deuda todo suma y una de cada tres cosas verificables nombra otra cosa. En el resto del documento (caps. 1–10) domina la transcripción (láminas contra cuadros contra texto: tres cifras para un dato en los caps. 2, 6, 7 y 9) y el perímetro reaparece en gasto, como en 2021–2022.

`tier_seccion`: restitución 250 (sí 87, no_verificable 60, aprox 59, no 40, vacío 4); mixta 81 (no_verificable 41, sí 19, no 10, vacío 8, aprox 3); juicio 45 (vacío 22, no_verificable 10, sí 7, no 3, aprox 3). Las secciones "Incidencia" siguen siendo mayoritariamente no verificables (fuentes externas, per cápita, perímetros propios).

`contrafactual_explicito`: 178 comparativas, **30 explícitas (16.9 %)**, 148 incompletas. Contra 68 % en 2022. La caída es del criterio (quinta declaración exigida en toda razón a PIB con base 2022) más que del documento; se reporta el estricto. Con el criterio de 2022 (cuatro declaraciones) el subagente estima que la mayoría de las comparaciones del cap. 3 y del cap. 12 serían explícitas.

## Tareas laterales
- **10.1 Transparencia Presupuestaria:** ver "Descargas y rutas". Sin salida programática; nada descargado.
- **10.2 Series de seguimiento (sin interpretación):**

| serie | 2020 | 2021 | 2022 | 2023 | fuentes 2023 |
|---|---|---|---|---|---|
| Pensiones IMSS / cuotas IMSS | 1.31 | 1.46 | 1.55 (PEF 2022 aprobado TG 4 636,461.8 / ILIF 2022 411,852.5) | **1.59** (PEF 2023 aprobado TG 4 750,252.1 / ILIF 2023 470,845.4) | analítico entidades; ILIF art. 1o. numeral 2. Objeto 2022–2023: aprobado por tipo de gasto; 2020–2021: EM del proyecto. |
| Pasivo pensionario, % PIB | 43.2 | 47.7 | 52.1 (dato 2020) | **43.6** (dato 2021; ISSSTE con dato 2020) | CGPE 2023 p. 104–105; −8.5 pp sin nota |
| Supuesto oficial de crecimiento real de pensiones | — | 7.0 % | 4.2 % | **4.2 %** | CGPE 2023 p. 137 |
| Tributarios / gastos obligatorios con pensiones | — | 0.671 | 0.674 | **0.691** (con cuotas IMSS 0.762) | ILIF art. 1o.; DEC Anexo 3 (6,689,188.3; +8.9 % real; composición no verificable desde el decreto) |

- **10.3 Trayectoria del DUC con decretos (sin interpretación):** 65 % en 2019 (LISH art. 39 original, DOF 11-08-2014, código 5355983); **58 % en 2020** (Decreto de reforma a la LISH, DOF 09-12-2019, código 5581294, Transitorio Segundo: "durante el ejercicio fiscal de 2020, los Asignatarios aplicarán la tasa de 58 % en sustitución de la prevista en el citado artículo 39"); **54 % desde 2021** (mismo decreto, art. 39 reformado: "aplicando una tasa del 54 %"); crédito fiscal contra el DUC para asignatarios (Decreto de beneficios fiscales, DOF 21-04-2020, citado en el considerando del decreto 5609025 de 28-12-2020, que además difiere al 7-ene-2021 el pago provisional de noviembre de 2020); **40 % en 2022** (LIF 2022 art. 22, en carpeta como ILIF 2022 art. 22); **40 % en 2023** (ILIF 2023 art. 22, PDF 94: "en sustitución de la tasa prevista en el citado artículo 39"). CGPE 2023 p. 50: "de 65 % en 2019 a 40 % en 2022". Fecha DOF de la LIF 2022 no verificada.
- **10.4 Candidata para el harness (registrada, sin desarrollar):** *¿Por qué una inflación menor puede elevar la razón deuda/PIB manteniendo RFSPF y crecimiento constantes?* Respuesta: con E_t = E_{t−1}/[(1+γ)(1+π)] + rf y rf fijo en % del PIB, desde 49.1 con rf 5 y γ 3 durante veinte años, π = 5 da 62.75 % y π = 3 da 75.45 % (estados estacionarios 66.4 y 87.1). Derivación: rf incluye los intereses nominales pagados; fijar rf y bajar π equivale a subir la tasa real que el sector público paga, porque la compensación inflacionaria que dejaría de pagar no reduce rf por supuesto. Menos inflación con el mismo rf nominal es más deuda; menos inflación con la misma tasa real es la misma deuda. No es contestable de memoria y se resuelve por completo con el marco.

## Reconciliación y diffs (instrucción §5.4–5.5)
- ILIF ↔ CGPE: presupuestarios 7,123,474.0 exacto; tributarios ILIF 4,623,583.1 vs CGPE 4,620,165.3: **3,417.8 mdp** reclasificados (2022: 56.9; 2021: 57.0), sin nota en ningún documento; candidato: IAEEH 7,676.6 y otros conceptos que el CGPE lleva a petroleros. Identidades del DEC cierran (déficit 1,134,140.7; diferimiento 42,033.1 = Adefas).
- Flujo–acervo ex ante: cierra a 0.1 pp (12 mmp en pesos). Descomposiciones oficiales ex post de la ILIF (2019→2020, 2020→2021, 2021→2022) tabuladas en `00` §9.
- Diff ILIF art. 2o.: techo interno 850,000 → 1,170,000; externo 3,800 → 5,500 mdd; Pemex 27,242/1,860 → 27,068.4/142.2; CFE 4,127/794 → 12,750/397; CDMX 4,500 → 3,000; estructura sin cambio.
- Diff de definiciones: "neta" → "bruta" en el cuadro del portafolio con las mismas cifras; SHRFSP 2020 51.6 / 52.4 en el mismo CGPE; "déficit público" (CGPE 2023) → "déficit presupuestario" (CGPE 2024) para la misma línea; PIB base 2013 → 2018 en el CGPE 2024; balance sin inversión con tope 3.1 % (2022) → sin tope (ILIF 2023) → "hasta 3.1 %" de nuevo en la LIF aprobada según la nota metodológica 2023 p. 26 (55,653 mdp de balance sin inversión aprobado; ex post, no usado como base); énfasis oficial en el balance presupuestario desde 2023.
- Anexo 3: 5,850,523.5 → 6,689,188.3 (+8.9 % real); composición no verificable desde el decreto.

## Anomalías (descritas, no resueltas)
- El CGPE 2023 da RFSPF 2019 = 1.8 % (p. 120) contra 2.3 en los CGPE 2022 y 2024 y en CIEP.
- Dos SHRFSPF 2020 en el mismo CGPE (51.6 / 52.4) con una nota que no explica la añada.
- Pasivo pensionario 52.1 (2020) → 43.6 (2021) sin explicación; ISSSTE sigue con dato 2020.
- Reclasificación ILIF–CGPE de 3,417.8 mdp en tributarios, 60 veces la de 2021–2022.
- Seguro catastrófico de 5 mmp "vigente hasta el 5 de julio de 2022" listado como amortiguador en un documento de septiembre de 2022.
- Sensibilidad al tipo de cambio: el cuadro pone +738 mdp de costo financiero bajo "apreciación de 10 centavos" y la nota lo llama "aumento del costo externo": signo contradictorio en la fuente.
- Balance sin inversión: la ILIF excluye toda la inversión; la LIF aprobada (según SHCP 2023 p. 26 y CGPE 2024 p. 119) vuelve al tope de 3.1 %. Cambió en la Cámara; no verificable con la carpeta.
- ILIF 2022: endeudamiento neto informativo 845,807.3 vs déficit del GF 850,012.7 (4,205.4 sin nota); en 2023 coinciden.
- CIEP: tres cifras para la caída de ingresos energéticos/petroleros (−15.5 real CGPE; −11.5 nominal resumen; −13 cap. 13); dos per cápita 2022 (114,574 / 114,732); "6.3 billones" de gasto; cuadro 2.1 que no suma; pastel con FMP y CFE intercambiados; gasto bruto y neteo que no reconcilian con el DEC (anomalía 2 del subagente); tasa "5.5 %" para 2023.
- Del subagente (no resueltas): CFE cierre 2022 no publicado por entidad; participaciones funcionales del PPEF (educación 11.4, energía 16.8) requieren Tomo I; cuadro 8.1 con líneas de IMSS/ISSSTE que difieren del aprobado (reasignaciones de la Cámara, esperable); FAM asistencia social con ponderadores que cambian entre años.
- Resuelta: el balance económico primario de CGPE p. 150 (−54,553.7) no es −1,134,140.7 + 1,079,087.1 = −55,053.6; la diferencia (500.0 mdp) es el costo financiero no presupuestario que la nota metodológica 2023 p. 26 lista aparte ('VII. Costo financiero no presupuestario 500').
- Propias: la lectura de figuras desde imagen es aproximada (V042 se sostiene solo contra la figura 11.2 de CIEP); el reparto crecimiento/inflación del efecto denominador es una convención; la cota de indexación deja el interés real 2022 en un rango de un punto.

## Lo que debería cambiar en la instrucción para 2024 (gasto: educación; decisión de analíticos)
1. **Analíticos.** Decidir. Tres hechos: el proyecto no se obtiene por ninguna ruta probada (portal 404, TP sin API visible); el aprobado sirve para 2022–2026 y a nivel entidad ya se usó; el subagente pudo verificar programas de IMSS/ISSSTE con el aprobado y dejó 23 de 32 filas de educación sin verificar por falta del GF. Opción mínima: descargar `ac01_ra_pp_ur_og.xlsx` (GF, ~10 MB) del PEF aprobado 2023 y 2024, etiquetar "aprobado contra aprobado" en la sección cero y aceptar la asimetría de objeto declarada. Opción máxima: navegador para TP.
2. **Quinta declaración como criterio separado.** Reportar dos tasas de `contrafactual_explicito`: con cuatro declaraciones (comparable con 2020–2022) y con cinco. En 2023 solo se reportó la estricta y rompe la serie.
3. **Lectura de imágenes.** Prever que CIEP imprime láminas y portadas como imagen: tiempo de fase 3 ×1.5; rendir a PNG en fase 1 y anotar en la sección cero cuántas páginas son imagen.
4. **Deflactor de CIEP.** Fijar de antemano la prueba de 1.0492 (implícito redondeado) además del oficial; en 2023 explicó 65 `aprox`.
5. **Frente del documento.** Mantener filas propias; en 2023 aportó 4 `no` y la lámina de cada capítulo aportó otros (tres cifras para un dato: lámina, cuadro, texto). Añadir la regla: verificar lámina contra cuadro contra texto dentro de cada capítulo antes que contra la fuente.
6. **Subagente.** Tercera vez que funciona; el cotejo de `no` tomó 10 minutos por muestreo aritmético. Pedirle además una tabla "lámina vs cuadro vs texto" por capítulo.
7. **Educación 2024.** Exigir en fase 1 el perímetro de "gasto educativo" (función educación neta vs Ramo 11 + FONE + R25 + IMSS/ISSSTE) y los dos PIB; el "+0.14 pp del PIB" de 2023 nació de dividir pesos de 2023 entre un PIB de 2022.
8. **Marco de cuatro variables:** ya validado; en 2024 basta aplicarlo (la ILIF 2025 traerá la descomposición oficial de 2023 para validar de nuevo).

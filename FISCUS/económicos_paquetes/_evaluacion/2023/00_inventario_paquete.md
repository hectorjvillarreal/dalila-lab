# Inventario de deuda y balance del paquete económico 2023, piezas metodológicas y diffs 2022 → 2023

**Corrida:** evaluación CIEP 2023 · FISCUS · Dalila · 2026-09-06
**Fase:** 1. Construido antes de leer el documento CIEP más allá de su índice (PDF 3–5, leído 09:18; ver bitácora).
**Capítulo propio:** deuda y balance (instrucción 2023 v2 §0). Con esta corrida quedan recorridas las tres partes del género: gasto (2020, 2021), ingresos (2022), balance y deuda (2023).
**Convenciones fijadas (instrucción §3):** deflactor del PIB 5.0 % para 2023 (CGPE III.1, p. 134; factor 1.050); comparación ex ante contra ex ante (ILIF/PPEF 2023 vs LIF/PEF 2022 aprobados, a precios y PIB de cada aprobación) salvo etiqueta en contrario; cierre estimado 2022 solo donde el CGPE lo da y etiquetado "est."; perímetro y añada declarados antes de cada cuadro; **nomenclatura de la casa (§2.7): RFSPF = RFSP y SHRFSPF = SHRFSP, un solo objeto con dos grafías**; en este documento se escribe la forma corta cuando se cita un documento oficial que la usa y la forma larga cuando se habla en voz propia.

mmp = miles de millones de pesos; mdp = millones de pesos; mmd = miles de millones de dólares; mdd = millones de dólares; "a" = aprobado 2022; "est." = cierre estimado 2022 (CGPE 2023); "p" = proyecto 2023; pp = puntos porcentuales del PIB.

---

## Estado de la carpeta

**Piezas oficiales del paquete 2023 presentes** (todas `oficial_primaria`, `_manifiesto.csv`):

| clave | archivo | páginas | paginación |
|---|---|---|---|
| CGPE | `2023/2023_cgpe_criterios-generales.pdf` | 152 | impresa = PDF |
| ILIF | `2023/2023_ilif_iniciativa.pdf` | 128 | exposición en romanos I–XLVIII (= PDF 1–48); articulado impreso 1 = PDF 49 (art. 1o.); art. 2o. impreso 12 = PDF 60; art. 22 impreso 46 = PDF 94 |
| DEC | `2023/2023_ppef_proyecto-decreto.pdf` | 168 | impresa = PDF; Anexo 1 p. 59–61; Anexo 3 p. 62; Anexo 8 p. 66 |
| CIEP | `2023/ciep_implicaciones2023.pdf` (`derivada_ciep`) | 103 PDF | **37 de las 103 páginas son imagen sin capa de texto** (incluidas las del capítulo de deuda: PDF 79, 80, 84, 85, 89); se leerán como imagen en fases 3–5 |

**Piezas ausentes y ruta probada para cada ausencia:**

| pieza | ruta probada (fecha, solo HEAD o GET único) | resultado | consecuencia para deuda |
|---|---|---|---|
| Exposición de motivos del PPEF 2023 (Tomo I) | `ppef.hacienda.gob.mx/work/models/PPEF2023/docs/exposicion/…` 404 el 2026-09-05 (corrida 2022, mismo árbol) | ausente | sin desagregación del Ramo 24 por intereses internos/externos/comisiones/coberturas; sin cuadro de costo financiero por entidad más allá del Anexo 1.E; sin cuentas dobles |
| Analíticos del **proyecto** PPEF 2023 | `ppef.hacienda.gob.mx/work/models/PPEF2023/analiticosPresupuestarios/Proyecto/*.xlsx` 404 (2026-09-05) | ausente | no afecta al capítulo de deuda (no usa analíticos); afecta la serie pensiones IMSS / cuotas IMSS, que se computa con el **aprobado** (ver §7) |
| Plan Anual de Financiamiento 2023 | no forma parte del paquete (se publica en diciembre); no se buscó | fuera de perímetro | si CIEP lo cita, es fuente externa |
| Informes Trimestrales / Cuenta Pública 2022 | fuentes ex post; no se descargaron | fuera de perímetro por decisión (§1.2 de 2022; §3 de 2023) | la validación §6.3 usa los observados 2022 que trae el paquete **2024** (CGPE 2024 Anexo I y III.1; ILIF 2024 exposición), ya en carpeta |

**Piezas metodológicas (§5.2), descargadas y registradas en `_manifiesto.csv` (dos filas nuevas, carpeta `_metodologia/`):**

1. **SHCP, *Balance Fiscal en México. Definición y Metodología*, abril de 2023.** Ruta canónica (`secciones.hacienda.gob.mx/work/models/estadisticas_oportunas/metodologias/1bfm.pdf`) sirve hoy la edición **abril 2026** (42 pp, creada 2026-04-29) y el Wayback Machine solo conserva las ediciones 2022-10-04 y 2024-08-20. La edición **abril 2023** se obtuvo de la Gaceta Parlamentaria (`gaceta.diputados.gob.mx/PDF/65/2023/may/Shcp_balanceF-20230509.pdf`, 44 pp, PDF creado 2023-05-08; sha256 `9b044dd5…`), es decir, el ejemplar que la SHCP remitió a la Cámara de Diputados en cumplimiento del art. 107 LFPRH. **Es un escaneo sin capa de texto**; se cotejó visualmente que sus pp. 3–4 coinciden palabra por palabra con la edición abril 2022 (Gaceta, `Shcp-20220503.pdf`, con texto), que se usa como auxiliar de búsqueda. Toda cita al documento metodológico en esta corrida remite a la edición 2023 por número de página y se verificó contra la imagen. `tier = oficial_primaria`, emisor SHCP (Unidad de Planeación Económica de la Hacienda Pública). Nota: el CGPE 2023 cita la edición de abril de **2022** en p. 120 y la de abril de **2021** en p. 122 para un mismo objeto (PFN); el CGPE 2024 cita la de abril de 2023.
2. **Cantú, Ramones y Villarreal (2016), "Por un sistema fiscal sostenible y con objetivos", *Revista de Economía Mexicana. Anuario UNAM*, núm. 1, pp. 259–284.** La ruta viva (`economia.unam.mx/assets/pdfs/econmex/01/07CantuRamones.pdf`) devuelve 404 desde 2026 (el sitio migró de CMS); se obtuvo del Wayback Machine (captura 2025-10-18, 26 pp, PDF creado 2016-05-03; sha256 `ecc85b10…`). `tier = autoral_ited`. **El vocabulario de tier pasa de dos valores a tres** (`oficial_primaria`, `derivada_ciep`, `autoral_ited`); queda anotado en la bitácora junto con la decisión pendiente de tier por sección.

**Criterios de la rúbrica condicionados por la carpeta:**

- **Criterio 1 (identidad de objeto):** no condicionado; las dos piezas metodológicas están en carpeta. La única salvedad es que la edición 2023 del documento SHCP es imagen y su verificación página por página es más lenta.
- **Criterio 3 (cierre contable y flujo–acervo):** condicionado parcialmente. El paquete da el SHRFSPF en % del PIB y no en pesos (salvo el saldo de deuda neta y bruta a julio de 2022, CGPE p. 126); la brecha flujo–acervo se reconstruye con esos datos y con la descomposición oficial que la ILIF publica cada año (§6.2).
- **Criterio 5 (cobertura):** condicionado en la desagregación del costo financiero (Ramo 24 por concepto vive en el Tomo I, ausente) y en el perfil de amortizaciones por instrumento del Gobierno Federal (la ILIF da totales interno/externo por año, p. XXXIX; el CGPE da el del sector público por tipo de acreedor, p. 139).
- **Serie de seguimiento pensiones IMSS / cuotas IMSS:** condicionada: el numerador sale del PEF **aprobado** (TG 4 del analítico de entidades), no del proyecto ni de la EM; se etiqueta.

**Proporción esperada de `no_verificable` atribuible a la carpeta:** baja para el capítulo de deuda (el CGPE y la ILIF traen todo lo que un capítulo de deuda cita, salvo el detalle del Ramo 24 y series largas); para el resto del documento CIEP (gasto por programa y UR, salud, educación, cuidados), alta, como en 2022 (EM y analíticos del proyecto ausentes). Se cuantifica en la bitácora al cierre de la fase 3, separando "carpeta" de "documento".

**Asimetría de objeto (instrucción §2.2):** para 2022–2026 solo existe el PEF **aprobado** a nivel programa/UR; CIEP evalúa el **proyecto**. Cuando esta corrida use el aprobado (serie de pensiones) no evalúa el mismo objeto que CIEP; se dice en cada lugar.

---

## 1. Los tres flujos (CGPE 2023)

Perímetro de cada flujo, adjudicado contra SHCP (2023) p. 3 y pp. 25–26 (definiciones legales del art. 2 LFPRH y cobertura institucional): **balance presupuestario** = sector público presupuestario (Gobierno Federal + IMSS, ISSSTE, Pemex, CFE); **balance público o económico** = presupuestario + no presupuestario (entidades de control indirecto no financieras), cobertura equivalente al sector público **no financiero**; **RFSPF** = balance público + necesidades de financiamiento fuera del presupuesto (Pidiregas, IPAB, FONADIN, deudores, banca de desarrollo y fondos de fomento, adecuaciones de registro), cobertura del sector público **federal** (incluye empresas públicas financieras; excluye al banco central). Ninguno de los tres incluye entidades federativas ni municipios.

| flujo | 2022 aprobado (CGPE 2022) | 2022 estimado (CGPE 2023) | 2023 proyecto | fuente |
|---|---|---|---|---|
| Balance presupuestario, mdp | −875,570.5 | −875,570.5 | −1,134,140.7 | CGPE p. 150–151; DEC art. 2 |
| Balance no presupuestario | 0.0 | 0.0 | 0.0 | p. 150 |
| **Balance público (= económico)**, mdp | −875,570.5 | −875,570.5 | −1,134,140.7 | p. 69, 150 |
| Balance público, % PIB | −3.1 | −3.0 | −3.6 | p. 19, 58, 135 |
| **Balance público sin inversión** | 0.0 | 0.0 | 0.0 | p. 69, 150; ILIF art. 1o. párrafo 7o. |
| Inversión excluida del equilibrio | "hasta 3.1 % del PIB" (LIF 2022 art. 1o.) | 3.1 % | **el total del gasto de inversión presupuestario** (ILIF 2023 art. 1o.: "no se contabilizará para efectos del equilibrio") | CGPE p. 150 nota 1; ILIF PDF 58 |
| Balance primario (económico), mdp | −83,606.6 | +29,854.7 | −54,553.7 | p. 150–151 |
| Balance primario, % PIB | −0.3 | +0.1 | −0.2 | p. 69, 135 |
| Necesidades fuera del presupuesto, % PIB | −0.4 | −0.8 | −0.5 | p. 58, 135 |
| **RFSPF**, mdp | −996,568.8 | −1,097,136.6 | −1,291,149.2 | p. 150–151 |
| RFSPF, % PIB | −3.5 | −3.8 | −4.1 | p. 19, 66, 135 |

Composición del RFSPF 2023 fuera del presupuesto (CGPE p. 66–67, en % del PIB; cuadro III.2 p. 135 redondea a un decimal): IPAB 0.10 (componente inflacionario de sus intereses), deudores 0.01, adecuaciones a registros 0.23 (componente inflacionario de la deuda indexada, ingresos por operaciones de financiamiento, venta neta de activos y adquisición neta de pasivos distintos de deuda), Pidiregas 0.14 (con lo cual CFE dispone de 0.20 % del PIB para inversión), banca de desarrollo −0.01 (superávit). Suma 0.47 ≈ 0.5.

Componentes del balance presupuestario 2023 (CGPE p. 69): Gobierno Federal −1,168,313.9 (−3.7 % PIB); IMSS +25,406.7; ISSSTE +8,766.5; Pemex 0.0; CFE 0.0; suma organismos y empresas +34,173.2 (0.1). **Endeudamiento neto del Gobierno Federal (ILIF art. 1o., numeral 0, partida informativa): 1,168,313.9 mdp**, igual al déficit del Gobierno Federal; "Ingresos derivados de financiamientos" 1,176,173.8 = endeudamiento interno 1,210,347.0 (GF 1,168,313.9 + diferimiento de pagos 42,033.1) + externo 0.0 − superávit de organismos de control directo 34,173.2. En 2022 la partida informativa era 845,807.3 y el déficit del GF 850,012.7 (diferencia 4,205.4 sin nota).

**Regla de balance invocada (CGPE p. 16, 66):** art. 11 del Reglamento de la LFPRH: se admite déficit presupuestario para compensar un aumento del costo financiero por tasas que exceda 25 % del aprobado del ejercicio anterior; el costo financiero 2023 crece **29.9 %** nominal respecto al aprobado 2022 (1,079,087.1 / 791,463.8 = 1.363: **36.3 % nominal, 29.9 % real** con deflactor 1.050; el CGPE llama "29.9 %" al crecimiento sin decir que es real; cuadro IV.6 p. 150 sí lo etiqueta "crec. real"). El umbral legal es sobre el monto aprobado, no especifica real o nominal; en ambas lecturas se rebasa.

**Metas de las EPE (CGPE p. 68):** Pemex y CFE con balance financiero en equilibrio (0.0); techo de servicios personales Pemex 106.1 mmp, CFE 69.9 mmp.

**Variación del déficit presupuestario 2023 (CGPE p. 70, mmp de 2023):** −215.1 respecto al aprobado 2022 **y** −215.1 respecto al estimado 2022 (mismo déficit nominal 875,570.5 en ambas columnas de 2022, p. 150–151).

## 2. Los tres acervos

Perímetro (SHCP 2023 p. 40, Anexo IV; CGPE p. 135): **SHRFSPF** = deuda neta del sector público presupuestario + obligaciones netas del IPAB, FONADIN, Pidiregas, programas de deudores y pérdida esperada de la banca de desarrollo y fondos de fomento (medida **neta** de activos financieros disponibles); **deuda neta del sector público federal** = Gobierno Federal + banca de desarrollo + EPE, neta de activos (ILIF p. XXXIII); **deuda bruta del sector público no financiero** = pasivos brutos del gobierno central y las empresas no financieras. Ninguno incluye entidades federativas ni municipios.

| acervo, % del PIB | 2020 | 2021 | 2022 aprobado | 2022 estimado | 2023 proyecto | 2024–2028 | fuente |
|---|---|---|---|---|---|---|---|
| **SHRFSPF** | 51.6 (p. 120) / 52.4 (p. 122) | 49.9 | 51.0 | 48.9 | **49.4** | 49.4 constante | CGPE p. 101, 120, 135 |
| interno | 33.1 | 33.1 | 34.5 | 33.4 | 34.7 | 35.2 → 36.6 | p. 101, 120 |
| externo | 18.5 | 16.8 | 16.5 | 15.5 | 14.6 | 14.2 → 12.7 | p. 101, 120 |
| **Deuda neta del sector público federal** | 51.3 | 49.6 | 49.7 | 48.7 | **49.2** | 49.2 → 49.1 | p. 123, 135; ILIF p. XXXIX |
| interna | 32.5 | 32.5 | 32.8 | 33.0 | 34.4 | 34.9 → 36.5 | p. 135 |
| externa | 18.9 | 17.1 | 16.9 | 15.8 | 14.8 | 14.3 → 12.6 | p. 135 |
| **Deuda bruta del sector público no financiero** | 57.7 | 55.3 | 57.4 | 54.5 | **54.9** | 54.9 constante | p. 120, 135 |
| Posición financiera neta del SPF | 51.0 | 48.2 | — | 46.9 (junio 2022) | — | — | p. 122 |

**Dos valores oficiales para el SHRFSPF 2020 en el mismo CGPE:** 51.6 % (Anexo I.1, p. 120, con el PIB revisado) y 52.4 % (cuadro de la PFN, p. 122, con el PIB de la edición anterior); el CGPE 2022 daba 52.4. Es la quinta declaración dentro de un solo documento.

**En pesos (CGPE p. 126, "Deuda del Sector Público", saldos):** deuda neta 2021 13,041.7 mmp y julio 2022 13,387.9; deuda bruta 13,489.7 y 14,150.5; interna 8,927.7 y 9,669.8 (valores gubernamentales 7,878.5 y 8,604.2); externa 4,562.0 y 4,480.7 mmp (221.6 y 218.4 mmd; bonos 3,475.9 y 3,411.8 mmp). SHRFSPF 2023 en pesos: 49.4 % × 31,401.7 = 15,512 mmp (el CGPE 2024 p. 119 lo confirma: 15,500,270.6 mdp "aprobado 2023"). SHRFSPF 2021 en pesos: 49.9 % × 26,273.5 = 13,110 mmp (SHCP 2023 Anexo IV: 13,103,964 mdp al cierre de 2021, 50.0 % del PIB de esa edición).

**Proporción en moneda extranjera (dos objetos, dos cifras):** deuda **del Gobierno Federal**: externa 22.1 % (2021), 20.6 % (2022e), 19.2 % (2023e) del total (CGPE p. 88; p. 18 y 89); deuda **del sector público / SHRFSPF**: externo 16.8/49.9 = 33.7 % (2021), 15.5/48.9 = 31.7 % (2022e), 14.6/49.4 = **29.6 %** (2023e). La "cuarta parte" de la instrucción está entre las dos: un quinto del Gobierno Federal, un tercio del sector público (Pemex y CFE cargan la diferencia: deuda externa de las EPE 6.6 % del PIB sobre 7.3 % de deuda neta de las EPE, ILIF p. XXXIII).

## 3. Techos de endeudamiento (ILIF 2023 arts. 2o. y 3o.; CGPE p. 18–19, 87)

**El techo es una autorización de endeudamiento neto (flujo autorizado, no déficit).** Cobertura del techo externo: Gobierno Federal **y banca de desarrollo** (ILIF nota 1, p. XXXV; CGPE p. 87). Cobertura del techo interno: Gobierno Federal.

| techo | 2022 (ILIF 2022 art. 2o.–3o.) | 2023 (ILIF 2023) | variación |
|---|---|---|---|
| Interno neto, Gobierno Federal | 850,000 mdp | **1,170,000 mdp** | +37.6 % nominal |
| Externo neto, sector público (GF + banca de desarrollo) | 3,800 mdd | **5,500 mdd** | +44.7 % |
| Pemex interno / externo | 27,242 mdp / 1,860 mdd | 27,068.4 mdp / 142.2 mdd | −0.6 % / −92.4 % |
| CFE interno / externo | 4,127 mdp / 794 mdd | 12,750 mdp / 397 mdd | +209 % / −50 % |
| Ciudad de México (art. 3o.) | 4,500 mdp | 3,000 mdp | −33.3 % |
| Banca de desarrollo y fondos de fomento: déficit por intermediación financiera | 0 | 0 | — |
| IPAB | solo canje y refinanciamiento | solo canje y refinanciamiento | — |
| Cláusula de intercambio interno ↔ externo | sí | sí (recíproca, cómputo el último día hábil al tipo de cambio Banxico) | — |

**Techo vs déficit vs endeudamiento (los tres objetos, 2023):** techo interno GF 1,170,000 mdp; endeudamiento neto del GF (ILIF art. 1o. informativo) 1,168,313.9; déficit del GF (CGPE p. 69) 1,168,313.9; déficit presupuestario 1,134,140.7; balance público 1,134,140.7; RFSPF 1,291,149.2. En 2022 techo (850,000) y déficit del GF (850,012.7) coincidían al millar y la ILIF informaba 845,807.3; en 2023 el techo excede en 1,686 mdp al endeudamiento del GF. Los techos de Pemex y CFE **no** son sus déficits: ambas tienen balance financiero 0.0 (CGPE p. 69) y aun así piden techos positivos (refinanciamiento y calendario de amortizaciones; el uso "deberá cumplir con la meta de balance financiero aprobado", ILIF PDF 62).

## 4. Costo financiero

| concepto, mdp | 2022 aprobado | 2022 estimado | 2023 proyecto | var. real 23/22a | fuente |
|---|---|---|---|---|---|
| **Costo financiero del sector público** | 791,463.8 | 904,925.2 | **1,079,087.1** | +29.9 % (36.3 nominal) | CGPE p. 150–151 |
| % del PIB | 2.8 | 3.1 | 3.4 | — | p. 135 |
| Ramo 24 Deuda Pública (GF) | 580,638.2 | — | 840,943.3 | +37.9 % | DEC 2022 y 2023 Anexo 1 y Anexo 8 |
| Ramo 34 Apoyo a ahorradores y deudores (IPAB 54,216.5; deudores 0.9) | 38,683.9 | — | 54,216.5 | +33.5 % | DEC Anexo 8 |
| Costo financiero de las EPE (Anexo 1.E) | 172,141.7 | — | 183,927.2 (Pemex 148,086.0; CFE 35,841.2) | +1.8 % | DEC Anexo 1 |
| Suma | 791,463.8 ✓ | | 1,079,087.0 ✓ | | |
| Costo financiero del Gobierno Federal (Ramos 24 + 34), % PIB | 2.6 (2022e) | | 2.9 | | CGPE p. 88 |
| Intereses, comisiones y gastos de la deuda, RFSPF gobierno central, % PIB | 2.6 | 2.9 | — | | p. 121 |
| Pidiregas: costo financiero de inversión directa (CFE) | — | — | 6,782.7 (6.8 mmp de 2023) | | DEC Anexo 6.F; CGPE p. 140 |

Desagregación del Ramo 24 por intereses internos/externos, comisiones y coberturas: **no obtenible** (Tomo I ausente). La sensibilidad publicada del costo financiero: 100 pb en la tasa = 30,218.0 mdp (0.11 % del PIB, **incluye IPAB**); 10 centavos en el tipo de cambio = 738.0 mdp de "aumento del costo externo en pesos de la deuda externa del Gobierno Federal" (CGPE p. 102; el cuadro lo presenta bajo el rótulo "apreciación de 10 centavos" con signo positivo en costo financiero y la nota habla de aumento: signo ambiguo en la fuente, se registra).

## 5. Perfil de amortizaciones e indicadores del portafolio

**Amortizaciones del Gobierno Federal (ILIF p. XXXIX, saldo contractual al 31 de julio de 2022):**

| | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 |
|---|---|---|---|---|---|---|
| Interno, mdp | 1,569,020.1 | 1,046,239.1 | 733,482.4 | 738,363.2 | 539,484.1 | 377,599.8 |
| Externo, mdd | 2,722.0 | 3,071.5 | 8,351.9 | 6,879.7 | 7,348.7 | 7,012.4 |

**Amortizaciones del sector público (CGPE III.3, p. 139, saldo a junio de 2022):** interna, saldo 9,610.9 mmp; pagos 2022 (resto) 921.9; 2023 **1,581.5**; 2024 1,180.0; 2025 781.8; 2026 824.3; 2027 563.7; 2028 379.6; otros años 3,378.1 (emisión de papel 9,022.6 del saldo). Externa, saldo 220.0 mmd; pagos 2022 11.6; 2023 **11.4**; 2024 9.9; 2025 14.4; 2026 13.0; 2027 16.1; 2028 12.1; otros 131.6 (bonos 167.5 del saldo; 2023 bonos 5.2). Bonos externos **del Gobierno Federal** con vencimiento en 2023: ≈ 420 mdd, "el menor monto de la actual administración" (CGPE p. 87; ILIF p. XXXVII). Tres objetos: GF externo total 2,722 mdd; sector público externo 11.4 mmd (incluye Pemex y CFE); bonos de mercado del GF 420 mdd.

**Indicadores del portafolio del Gobierno Federal (CGPE p. 88; 2021 / 2022e / 2023e):** deuda externa 22.1 / 20.6 / 19.2 % del total (rótulo **"bruta"**; el CGPE 2022 p. 56 rotulaba **"neta"** con los mismos 22.1 y 20.6 para 2021 y 2022e: cambio de nombre sin cambio de cifra); deuda interna en valores a tasa nominal fija y largo plazo 49.7 / 47.3 / 47.7; a tasa fija y largo plazo 78.2 / 77.0 / 79.1; plazo promedio 7.3 / 7.8 / 7.9 años; duración 4.6 / 4.7 / 4.5; deuda externa de mercado a tasa fija 100 / 100 / 100; a plazo mayor a un año 98.6 / 99.4 / 98.8; vida media 21.0 / 20.4 / 19.5; duración 11.1 / 9.8 / 9.5; **deuda que revisa tasa 31.9 / 33.1 / 31.3 % del total**; costo financiero del GF (Ramos 24 y 34) 2.1 / 2.6 / 2.9 % del PIB. Observados a junio de 2022 (ILIF p. XXXIII): 79 % en pesos, plazo promedio interno 7.6 años, 73.9 % a tasa fija y largo plazo. Cierre 2021 (ILIF p. XXXII): 77.7 % en pesos / 22.3 % en moneda extranjera, plazo promedio 7.3, 78.2 % tasa fija.

**Marco macro relevante para la deuda (CGPE III.1, p. 134; 2021 obs. / 2022e / 2023 / 2024–2028):** PIB real 4.8 / 2.4 / 3.0 / 2.4; PIB nominal 26,273.5 / 29,058.3 / 31,401.7 mmp; deflactor 7.1 / 8.0 / 5.0 / 3.5; inflación dic/dic 7.4 / 7.7 / 3.2 / 3.0; tipo de cambio fin de periodo 20.6 / 20.6 / 20.6 / 20.7 → 21.6; Cetes 28 fin 5.49 / 9.50 / 8.50 / 7.50 → 5.50; promedio 4.42 / 7.48 / 8.95 / 7.95 → 5.50; **Cetes real promedio −1.19 / −0.25 / 4.04 / 4.73 → 2.43**; SOFR 3m 0.1 / 1.3 / 2.7 / 2.3 → 2.1.

## 6. Contingencias y amortiguadores (CGPE 4.3, p. 102–107)

- **Pasivo pensionario** al cierre de 2021: 11,457.9 mmp de 2021 = **43.6 % del PIB** (IMSS-RJP 3,348.6 = 12.7; ISSSTE 5,869.7 = 22.3, *dato 2020*; CFE 579.1 = 2.2; Pemex 1,384.1 = 5.3; otros 276.4 = 1.1). "Menor en 8.5 pp respecto a lo registrado en 2020 (52.1 %)", sin explicar el cambio (p. 104). Activos del SAR 5.0 billones = 18.0 % del PIB (junio 2022). PBAM 238.0 mmp (2022) → 335.5 (2023), +34.3 % real. Riesgo de mediano plazo nombrado: "pensiones en curso del sistema de reparto anterior" (p. 103).
- **Pidiregas:** solo CFE; pasivos ya incluidos en el SHRFSPF; exposición máxima contingente de la inversión condicionada 183.2 mmp a ~30 años (p. 106). Compromisos de pago 2023 (p. 140, mmp de 2023): directos, amortización 11.7 + costo financiero 6.8; condicionados, cargos fijos 19.3 y variables 45.7. APP con fuente presupuestaria: 2023 pago por disponibilidad 9.4 y por servicios 3.1.
- **Seguro de depósitos:** depósitos 6.43 billones = 23.3 % del PIB (marzo 2022); garantía 400 mil UDI por persona; ICAP 18.76 % (junio 2022).
- **Banca de desarrollo:** cartera directa e impulsada 1.7 billones; capitalización 30.7 %; cartera vencida 48.6 mmp; estimaciones 64.7 mmp.
- **Desastres:** pérdida esperada anual 10.2 mmp; PML 95 % 11.3; PML 99 % 34.3; exposición 4,500.5 mmp (base 2016 actualizada a abril de 2022).
- **Amortiguadores (p. 103):** coberturas petroleras al 100 % de la exposición del GF; Línea de Crédito Flexible FMI 50 mmd; swap FED 3 mmd; swap Tesoro 9 mmd; reservas 198.8 mmd (26-ago-2022); 79.4 % de la deuda del GF en moneda nacional y 77.0 % de valores a tasa fija y largo plazo; seguro catastrófico 5 mmp **"con vigencia hasta el 5 de julio de 2022"** (vencido dos meses antes de la fecha del documento); bono catastrófico 485 mdd hasta marzo de 2024.
- **Garantías** del Gobierno Federal a Pemex o CFE: no hay línea en el paquete 2023.

## 7. Series de seguimiento permanente (instrucción §2.6; sin interpretación)

| serie | 2020 | 2021 | 2022 | 2023 | fuentes 2023 |
|---|---|---|---|---|---|
| Pensiones IMSS / cuotas IMSS | 1.31 | 1.46 | **1.55** (PEF 2022 aprobado, TG 4 IMSS 636,461.8 / ILIF 2022 cuotas 411,852.5) | **1.59** (PEF 2023 aprobado, TG 4 IMSS 750,252.1 / ILIF 2023 cuotas 470,845.4) | `2023/2023_pef_analitico-entidades-ramo-programa-ur-objeto.xlsx` (GYR, TG = 4); ILIF art. 1o. numeral 2 |
| Pasivo pensionario, % del PIB | 43.2 (CGPE 2020) | 47.7 (CGPE 2021) | 52.1 (CGPE 2022, dato 2020) | **43.6** (CGPE 2023 p. 104, dato 2021; ISSSTE con dato 2020) | CGPE p. 104–105 |
| Supuesto oficial de crecimiento real de pensiones | — | 7.0 % (CGPE 2021) | 4.2 % (CGPE 2022) | **4.2 %** (CGPE 2023 p. 137, "con base en estudios actuariales disponibles y el comportamiento observado") | CGPE p. 137 |
| Tributarios / gastos obligatorios con pensiones | — | 0.671 | 0.674 | **0.691** (4,623,583.1 / 6,689,188.3); con cuotas IMSS 0.762 (5,094,428.5 / 6,689,188.3) | ILIF art. 1o. numerales 1 y 2; DEC Anexo 3 |

Notas de objeto: (i) el numerador de la primera serie en 2020–2021 salía de la EM del PPEF (pensiones por institución, cuentas dobles) y en 2022–2023 sale del PEF **aprobado** por tipo de gasto 4; **no es estrictamente el mismo objeto ni la misma añada** (aprobado vs proyecto), se marca; (ii) el denominador es la ILIF (proyecto) en los cuatro años; (iii) ISSSTE TG 4: 278,180.2 (2022) y 309,763.1 (2023), como referencia; (iv) el pasivo pensionario de 2022 (52.1, dato 2020) y el de 2023 (43.6, dato 2021) son dos cortes del mismo objeto que cambian 8.5 pp sin nota metodológica: se describe, no se resuelve (§13, congelado).

**Diff del Anexo 3 (condición de §2.1):** DEC 2022 p. 55: gastos obligatorios 4,678,198.6; con pensiones 5,850,523.5. DEC 2023 p. 62: 5,355,844.5; **6,689,188.3** (+14.3 % nominal, +8.9 % real). El Anexo es de dos líneas en ambos años y el decreto no define su composición (remite a la LFPRH art. 2 fr. XXXV); el diff textual del articulado no muestra cambio en la referencia (art. 3 fr. III en ambos). La serie se extiende con esa salvedad: la composición no es verificable desde el decreto.

## 8. Diffs previos (instrucción §5.4)

**8.1 Artículos de endeudamiento, ILIF 2022 → 2023 (art. 2o. y 3o.).** Cambios de cifra en el cuadro de §3; sin cambios de estructura: la cláusula de intercambio interno/externo, la autorización al IPAB para canje y refinanciamiento (con informe trimestral), la definición del déficit por intermediación financiera (cero pesos) y la obligación de informar trimestralmente el Programa Anual de Financiamiento están en ambos años con la misma redacción. El techo de Pemex cambia de "27 mil 242 / 1 mil 860" a "27 mil 068.4 / 142.2" (interno prácticamente igual, externo −92 %); CFE de "4 mil 127 / 794" a "12 mil 750 / 397". CDMX 4,500 → 3,000.

**8.2 Definiciones del CGPE, 2022 → 2023, contra SHCP (2023).**
- Nombres de los flujos: el CGPE 2023 usa "balance público" (p. 16, 66, 135), "balance económico" (p. 150–151, "balance económico primario") y "déficit público" (p. 68, cuadro; p. 120 "III. Déficit público (I−II)") para **un mismo objeto**; el documento metodológico (p. 3) lo autoriza: "balance público, balance económico, balance presupuestario, balance financiero y RFSP corresponden al concepto de balance fiscal y son diferentes por aspectos de cobertura institucional y de operaciones" y (p. 26) "el balance económico o público, que suma los balances presupuestario y no presupuestario". En el CGPE 2022 la misma triple nomenclatura. **Sin cambio.**
- "Déficit presupuestario" aparece en el DEC art. 2 (1,134,140.7) y en el CGPE 2024 el cuadro I.1 lo rebautiza "III. Déficit presupuestario (I−II)" donde el CGPE 2023 decía "Déficit público": cambio de etiqueta en la serie oficial entre paquetes, con la misma cifra.
- El cuadro de indicadores del portafolio cambia el rótulo de "deuda externa/interna **neta** (% del total)" (CGPE 2022 p. 56) a "deuda externa/interna **bruta** % del total" (CGPE 2023 p. 88) con cifras idénticas para 2021 y 2022e.
- El SHRFSPF 2020 vale 51.6 en la serie (p. 120) y 52.4 en la PFN (p. 122) del mismo CGPE 2023; en el CGPE 2022 valía 52.4 en ambos cuadros (p. 84, 86). Añada de PIB distinta, no declarada en p. 122.
- El CGPE 2024 cambia el año base del PIB (2013 → 2018) y reexpresa toda la serie: SHRFSPF 2021 49.2 y 2022 47.7 (CGPE 2024 p. 99) donde el CGPE 2023 decía 49.9 y 48.9e. Se declara en §9.
- El CGPE 2023 cita la nota metodológica de "abril de 2022" (p. 120) y de "abril de 2021" (p. 122): dos ediciones para dos cuadros contiguos.
- Balance sin inversión: 2022 excluía "hasta 3.1 % del PIB" de inversión física del GF y las EPE (LIF 2022 art. 1o.; el documento metodológico 2022 p. 26 dice "hasta el 2.0 %", **errata de la nota metodológica**, corregida a 3.1 en su edición 2023 p. 26 — verificar en imagen); 2023 excluye "el gasto de inversión del sector público presupuestario" completo (ILIF art. 1o.). **Cambio de perímetro de la regla de equilibrio**: el balance sin inversión de 2022 y el de 2023 no son comparables.

**8.3 Anexo 3:** ver §7.

## 9. Reconciliaciones obligatorias (instrucción §5.5)

**9.1 ILIF ↔ CGPE en ingresos.** ILIF 2023 art. 1o.: total 8,299,647.8; numeral 0 (financiamientos) 1,176,173.8; ingresos presupuestarios = 8,299,647.8 − 1,176,173.8 = **7,123,474.0** = CGPE p. 150 ✓. Tributarios ILIF numeral 1 = 4,623,583.1; CGPE tributarios = **4,620,165.3**; diferencia **3,417.8 mdp** (2022: 56.9; 2021: 57.0). El residuo cambia de orden de magnitud: la hipótesis de 2022 (ISR de contratistas y asignatarios reclasificado a petroleros) explicaba ~57 mdp; en 2023 la ILIF incluye en "impuestos" 7,676.6 de "impuesto por la actividad de exploración y extracción de hidrocarburos" (numeral 1.18.01) y otros conceptos que el CGPE puede reclasificar a petroleros; petroleros CGPE 1,317,653.2 vs ILIF (Pemex 7.72 + FMP 9.97) no verificable al detalle sin el desglose de la partida 7 en el articulado (queda para la fase 3 si CIEP lo usa). **Reaparece y crece; no explicado por ningún documento.** Identidades: ingresos totales = gasto neto total (DEC art. 2: 8,299,647,800,000 ✓); déficit presupuestario DEC art. 2 = 1,134,140,700,000 = CGPE ✓; financiamientos 1,176,173.8 − déficit 1,134,140.7 = 42,033.1 = diferimiento de pagos = Adefas 2023 (Ramo 30: 42,033,100,000 ✓).

**9.2 Flujo contra acervo (ex ante 2023).** ΔSHRFSPF 2023 = 49.4 − 48.9 = **+0.5 pp** del PIB; RFSPF 2023 = **4.1 %** del PIB. La brecha de −3.6 pp es el efecto del crecimiento nominal del PIB sobre el acervo heredado: 48.9 × (1 − 1/1.0815) = 48.9 × 0.0754 = **3.69 pp** con PIB nominal +8.15 % (3.0 real, 5.0 deflactor), y 48.9 − 3.69 + 4.1 = 49.31 ≈ 49.4 (residuo +0.1: redondeo y tipo de cambio 20.6 → 20.6, nulo por supuesto). **Cierra.** En pesos: 15,512 (2023) − 14,209 (48.9 % × 29,058.3) = 1,303 mmp ≈ RFSPF 1,291 mmp (diferencia 12 mmp, 0.04 % del PIB). El paquete no publica el SHRFSPF en pesos ni una descomposición ex ante; la descomposición **ex post** sí la publica cada año la ILIF (2022 p. XXX–XXXI para 2019→2020; 2023 p. XXXII para 2020→2021; 2024 p. XXVIII–XXIX para 2021→2022), y se usa en §6.3 del capítulo.

**Descomposiciones oficiales del cambio del SHRFSPF (ILIF, exposición "Evolución de la deuda del Gobierno Federal"), pp del PIB:**

| tránsito | PIB nominal | endeudamiento bruto | activos presupuestarios | activos no presupuestarios | euro/dólar | peso/dólar | Δ declarada |
|---|---|---|---|---|---|---|---|
| 2019 → 2020 (ILIF 2022 p. XXX) | +2.5 | +4.4 | +1.1 | −1.2 | +0.3 | +0.8 | 44.5 → 52.4 (+7.9) |
| 2020 → 2021 (ILIF 2023 p. XXXII) | −5.6 | +2.9 | +0.2 | +0.5 | −0.2 | +0.5 | 51.6 → 49.9 (−1.7) |
| 2021 → 2022 (ILIF 2024 p. XXVIII) | −4.8 | +4.5 | −0.3 (activos, sin separar) | — | −0.1 | −0.8 | 49.2 → 47.7 (−1.5; PIB base 2018) |

## 10. Añada de PIB (quinta declaración) adoptada para esta corrida

- **Ex ante 2023:** CGPE 2023, PIB base 2013, nominal 2022e 29,058.3 y 2023 31,401.7 mmp; SHRFSPF 48.9 → 49.4. Es la añada de toda la comparación del capítulo propio y de la verificación de CIEP.
- **Ex post 2022 (solo validación §6.3):** CGPE 2024 / ILIF 2024, PIB base 2018, nominal 2022 observado 29,503.8 mmp; SHRFSPF 49.2 (2021) → 47.7 (2022); RFSPF 2022 4.3 %; crecimiento real 3.9; deflactor 6.7; tipo de cambio fin de periodo 20.6 → 19.4; Cetes promedio 7.6 (real −0.2). La instrucción cita otra añada (50.7 → 49.4 con RFSPF 4.5, presumiblemente Informe Trimestral 4T-2022 con PIB base 2013): no está en carpeta; se reporta como segunda lectura y se dice cuál se adopta (la del CGPE 2024, porque está en carpeta y trae su descomposición oficial).
- Cuando dos añadas cambien el signo de una lectura, se presentan ambas.

## 11. Lo que 2023 tiene de particular (instrucción §6.6), verificado contra el texto

- **Ciclo de alzas:** el CGPE supone Cetes 28 fin de 2022 9.50 y fin de 2023 8.50 (promedio 8.95, real promedio 4.04, la más alta de la serie 2021–2028); costo financiero +29.9 % real vs aprobado 2022 y +13.6 % real vs cierre 2022 estimado; 31.3 % de la deuda del GF revisa tasa (p. 88); sensibilidad 100 pb = 30,218 mdp (con IPAB). El CGPE 2022 suponía 5.3 % de Cetes al cierre de 2023 (p. 16). El desvío de tasas es el motivo declarado del déficit (regla del 25 %).
- **Apoyos a Pemex, tres caminos:** (a) aportación patrimonial: **no hay línea** en el paquete 2023 (el CGPE 2023 p. 143 nota **/ recuerda que 2016 incluyó 1.5 % del PIB de aportaciones a Pemex y CFE); (b) reducción de carga fiscal: DUC 40 % (ILIF art. 22; CGPE p. 68 "se mantiene reducida la carga fiscal"); (c) endeudamiento de la empresa: techo neto 27,068.4 mdp interno y 142.2 mdd externo con balance financiero 0.0 (CGPE p. 69). El efecto sobre flujo: (b) baja ingresos del GF y sube los de Pemex sin tocar el balance público; (c) no toca el balance (balance 0) pero sí el acervo bruto; (a) ausente.
- **Registro de proyectos de inversión:** el balance sin inversión excluye "el gasto de inversión del sector público presupuestario" (presupuestario); Pidiregas de CFE (no presupuestario) entra en RFSPF por 0.14 % del PIB; inversión física 3.6 % del PIB en 2023 (p. 135), 2.2 % en 2024–2028 "monto equivalente al balance público" (p. 137).
- **Plan Anual de Financiamiento:** no forma parte del paquete; la ILIF (art. 2o. último párrafo) obliga a informar trimestralmente su avance.

## 12. Lista cerrada de cifras que un lector del paquete esperaría en un capítulo de deuda (para el criterio de cobertura)

Tres flujos con cifra y % PIB; balance sin inversión y perímetro de la exclusión; primario; RFSPF por componente fuera del presupuesto; balance por entidad (GF, IMSS, ISSSTE, Pemex, CFE); tres acervos con interno/externo; SHRFSPF 2024–2028 y RFSPF "inercial" 2.7 %; techos por entidad y su cláusula de intercambio; techo CDMX; endeudamiento neto informativo del art. 1o.; costo financiero total y por ramo/entidad, % PIB, crecimiento real vs aprobado y vs cierre; regla del 25 %; sensibilidades (tasa, tipo de cambio); indicadores del portafolio (moneda, tasa fija, plazo, duración, revisa tasa); amortizaciones 2023–2028 interno/externo (GF y sector público); bonos externos 2023 (420 mdd); marco macro de tasas, inflación, tipo de cambio y crecimiento con su senda a 2028; pasivo pensionario y supuesto de crecimiento de pensiones; Pidiregas y APP; IPAB; amortiguadores (FCL, swaps, reservas, coberturas, bono cat); calificaciones (p. 49: grado de inversión con ocho agencias); descomposición oficial ex post del cambio del SHRFSPF (ILIF); PFN; LMGCE rebasado en 102.2 mmp (p. 69).

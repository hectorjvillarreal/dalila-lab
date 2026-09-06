# Mapa de fuentes — qué documento oficial alimenta cada sección del género

Válido para la estructura del paquete 2020; verificar paginación en cada ejercicio. Paginación: CGPE y EM, impresa = PDF; ILIF, exposición en romanos y articulado impreso 1 = PDF 52; DEC impresa = PDF.

## Documentos y cuadros clave

| pieza | qué contiene que se usa | cuadro / ubicación 2020 |
|---|---|---|
| CGPE | marco macro; metas RFSP/balance; 12 indicadores; ingresos y gasto 2019–2020 en pesos constantes; mediano plazo 2021–2025; riesgos; pasivo pensionario; series 2013–2019 en % PIB | p. 69 (macro); p. 73 (balance público); p. 100 (12 indicadores); p. 86–87 (ingresos); p. 88–95 (gasto); p. 112, 120, 122, 124 (mediano plazo); p. 127–130 (riesgos, pasivo); p. 177–178 (series); Anexo C p. 184–186 |
| ILIF | ingresos por concepto (art. 1o.); techo de deuda (art. 2o.); método de pronóstico; series y proyección de ingresos; gastos fiscales; "otras medidas" (dividendo, Pidiregas, meta Pemex) | PDF 52–61 (art. 1o.); 65–66 (art. 2o.); I–XII (método, series, gastos fiscales); XXX–XXXV (otras medidas) |
| EM (PPEF) | acciones de gasto; programas por ramo (texto); series 2015–2019 por clasificación; perspectiva 2021–2025; estimación 2020 y cuentas dobles; clasificación administrativa, económica (incl. pensiones por institución), funcional, federalizado; anexos transversales | p. 14 (acciones); p. 63–72 (Bienestar, IMSS, ISSSTE); p. 127–134 (series); p. 140–143 (2021–2025); p. 146–152 (estimación, costo financiero, cuentas dobles); p. 155–167 (administrativa); p. 169–171 (económica; pensiones p. 171); p. 188 (federalizado); p. 189–192 (funcional); p. 195–217 (anexos transversales) |
| DEC (PPEF) | gasto neto (art. 2); metas Pemex/CFE (art. 5); IMSS aportaciones GF (art. 6); Anexo 1 por ramo; Anexo 2 GCE; Anexo 3 gastos obligatorios con/sin pensiones; Anexos 10–19 transversales; Anexo 25/26 programas | p. 2, 6–7; p. 57–58 (Anexo 1); p. 59 (Anexos 2–5); p. 65–88 (transversales); p. 141–144 |
| Analíticos PPEF (xlsx) | todo lo de abajo | `ppef.hacienda.gob.mx/es/PPEF{año}/analiticos_presupuestarios` → `/work/models/PPEF{año}/analiticosPresupuestarios/Proyecto/` |

## Analíticos: archivos y columnas

| archivo | cobertura | columnas | usos |
|---|---|---|---|
| `ac01_ra_pp_ur_og.xlsx` | Gobierno Federal (ramos 01–49), bruto 4,642,291.9 mdp en 2020 | RAMO, TPP, GPP, MOD, PP, UR, F, FN, SF, AI, TG, FF, PE, EF, CC, IMPORTE PEF (pesos) | programas prioritarios; Ramo 19 por programa; capítulo de gasto (primer dígito de PE); tipo de gasto TG (4 = pensiones); por entidad federativa (EF) |
| `ac01_ra_f_ur_og.xlsx` | GF | RAMO, F, FN, UR, SF, AI, TG, FF, PE, EF, CC, IMPORTE PEF | funciones/subfunciones con nombre (salud, educación, seguridad, C&E, protección social) |
| `ac01_ra_pp_ur_og_efe.xlsx` | IMSS (GYR), ISSSTE (GYN), Pemex (TYY), CFE (TVV); 2,300,061.9 mdp | SECTOR, ENTIDAD, TPP, GPP, IPP, PP, F, FN, SF, AI, TG, FF, PE, EF, CC, IMPORTE PEF | programas de IMSS/ISSSTE/Pemex/CFE; pensiones por entidad (TG=4); cap. 6000 (inversión pública) |
| `ac01_ra_f_ur_og_efe.xlsx` | entidades | SECTOR, ENTIDAD, F, FN, SF, AI, MOD, PP, TG, FF, PE, EF, CC, IMPORTE PEF | función salud IMSS/ISSSTE; C&E Pemex/CFE |

Nota: la hoja de datos es la segunda ("Hoja1"); la primera es carátula. Cargar con pandas `header=None` y tomar la primera fila con ≥8 celdas como encabezado. GF bruto + entidades − neteo (846,017.9 en 2020, DEC p. 59) = gasto neto.

## Mapa sección → fuente

| sección del género | fuente primaria | cuadro concreto (2020) | requiere además |
|---|---|---|---|
| Ingresos totales y composición | ILIF art. 1o. | PDF 52–61 | PIB nominal CGPE p. 69 para % PIB |
| Ingresos vs cierre / vs LIF anterior | CGPE | p. 86–87 (mmp de 2020, ambas bases) | — |
| Series de ingresos | CGPE Anexo B | p. 177 | Cuenta Pública para años anteriores a 2013 |
| Medidas de ingresos | CGPE 3.2.3 | p. 80–85 | **miscelánea fiscal** (iniciativa separada, no en el paquete descargado) |
| Gastos fiscales | ILIF exposición | p. XII | Presupuesto de Gastos Fiscales |
| Ingresos energéticos | ILIF art. 1o.; CGPE p. 86; ILIF "otras medidas" | — | decreto de DUC / estímulo a Pemex (DOF) |
| Gasto neto, programable, no programable | EM cap. 2; DEC art. 2 | p. 146–147 | — |
| Costo financiero | EM 2.2.1 | p. 148 | — |
| Clasificación administrativa | EM 3.1; DEC Anexo 1 | p. 155, 157, 160, 165–167; p. 57–58 | analíticos para 2019 resectorizado vs original |
| Clasificación económica; pensiones por institución | EM 3.2 | p. 169–171 | — |
| Clasificación funcional | EM 3.3 | p. 189–192 (consolidado neto) | analíticos (bruto) para perímetros propios |
| Programas prioritarios | analítico `ac01_ra_pp_ur_og` | PP por ramo | PEF t−1 analítico para variación |
| Anexos transversales | DEC Anexos 10–19; EM 3.5 | p. 65–88; p. 195–217 | **el anexo pobreza está en EM p. 215 aunque no tenga anexo numerado en el DEC** |
| Salud por subsistema | analítico función (GF y efe) | FN "Salud" por RAMO/ENTIDAD; Ramo 12 total | programas: `pp` (SSA, IMSS, ISSSTE, Pemex PP 013) |
| Inversión | EM 3.2.2; analíticos cap. 6000/7000/8000 | p. 169–172 | Tomo VIII para proyectos |
| Educación | analítico función (FN Educación por SF; Ramo 11 en otras FN) | — | — |
| Pensiones | EM p. 171; DEC art. 6; analíticos Ramo 19 y TG=4; CGPE p. 122/124/130; EM p. 141 | — | PEF t−1 para no contributivo; Cuenta Pública para series; CONAPO para cobertura |
| Energía (gasto) | analíticos FN "Combustibles y Energía" (GF: R18, R23, CRE, CNH; efe: Pemex, CFE); AI de Pemex (226 producción, 229 exploración, 232 pensiones, 234 corporativo) | — | estrategias programáticas por ramo (PPEF docs/52, docs/53) |
| Seguridad | analítico función GF: FN 7 (SF 1–4), FN 3 (SF 2,3,4,5), FN 2 (SF 1–4), FN 8 (SF 4,5), FN 6 (SF 1–3); Ramo 36 por UR | — | — |
| Gasto federalizado | EM 3.2.3 | p. 188 | analíticos por EF para per cápita; CONAPO población |
| Deuda | CGPE p. 73, 100, 120–125; ILIF art. 2o. y p. XXVIII–XXIX | — | CONAPO para per cápita |
| Mediano plazo y riesgos | CGPE cap. 4; EM 1.4 | p. 112, 120–132; p. 140–143 | — |

## Tomos descargados en 2020 y para qué

Ninguno de los Tomos PDF (el árbol `/work/models/PPEF2020/docs/` y `/paquete/` devolvía 404 el 2026-09-05). Se descargaron cuatro analíticos xlsx (ver arriba) para: verificar el cuadro de programas prioritarios (CIEP 3.1), el cuadro de programas de salud (4.2), los perímetros de salud/educación/seguridad/energía/inversión, el Ramo 19 por programa y la SSPC por UR. Los cuatro bastaron para todo el 2020 salvo lo que exige PEF 2019 o Cuenta Pública.

## Adenda 2021

**Rutas de analíticos (procedimiento estándar desde 2021):**
- PPEF t: `https://www.ppef.hacienda.gob.mx/es/PPEF{t}/analiticos_presupuestarios` → `/work/models/PPEF{t}/analiticosPresupuestarios/Proyecto/ac01_ra_pp_ur_og.xlsx`, `ac01_ra_f_ur_og.xlsx`, y sus `_efe` (entidades). Verificado 2020 y 2021.
- PEF t−1 aprobado: `https://www.pef.hacienda.gob.mx/es/PEF{t-1}/analiticos_presupuestarios` → `/work/models/PEF/Analiticos_Historico/{t-1}/Autorizado/ac01_ra_pp_ur_og.xlsx` (y `_f_`, `_efe`). Verificado 2020 (descargado) y 2021 (HEAD 200, 9.4 MB).
- Estado 2022–2026 (tarea lateral, 2026-09-05, solo HEAD, nada descargado): la página de analíticos responde 200 en los cinco ejercicios y lista 25 xlsx cada una; 2022 y 2023 enlazan a `/work/models/PPEF{t}/analiticosPresupuestarios/Proyecto/…`, 2024–2026 a `/work/models/PPEF{t}/analiticosPresupuestarios/…` (sin `Proyecto`). **Todos los archivos devuelven 404** (misma página de error de 2,978 bytes). Alternativa a probar en la corrida correspondiente: los aprobados en `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/`.

**Dónde vive cada perímetro de salud (2021):**

| perímetro | fuente | 2021 |
|---|---|---|
| Cuadro oficial "Gasto en salud, dependencias, entidades y ramos generales" | EM p. 67–68 | 667,236.4 (IMSS 325,506.8; ISSSTE 64,202.8; SSA ramo 145,414.6; FASSA 109,501.3; IMSS-Bienestar 13,607.6; Sedena 6,462.9; Semar 2,540.3) |
| Función Salud consolidada neta (con serie 2016–2020) | EM p. 203; p. 150 | 664,659.6 |
| Función Salud bruta por ramo/entidad y subfunción | AN `ac01_ra_f_ur_og` (FN "Salud") y `_efe` | GF 280,644.6; entidades 389,709.6 |
| Ramo 12 por programa y UR (INSABI = UR M7B; Seguro Popular = U005 hasta 2020; U013; E023) | AN `ac01_ra_pp_ur_og` | 145,414.6 |
| FASSA | EM p. 201 (federalizado); DEC Anexo 22; AN R33 PP I002; por entidad: AN columna EF | 109,501.3 |
| IMSS-Bienestar | EM p. 61; AN R19 PP S038 | 13,607.6 |
| Servicios médicos Pemex | AN `_efe` Pemex PP E013 (en función C&E, no Salud); por AI en CIEP | 17,441.6 |
| FONSABI (fideicomiso) | aportación: AN R12 partida 46101; extracción: ILIF transitorios (2021: 13o., PDF 122); uso: EM texto (p. 64) | +16,703.5 / −33,000 / 3,819.3 |
| Medicamentos | EM p. 62 (cuadro por institución); AN partidas 253xx | 90,572.4 |
| Plazas y residentes | EM p. 64–67; AN partida 16102 | 6,566.2 (SSA) |
| Gasto extraordinario COVID | CGPE 3.2 (p. 22–26) y 3.4 (p. 36) para 2020; **sin línea en PPEF 2021** | — |
| Gasto de bolsillo / total en salud | fuera del paquete (EM p. 59 cita OCDE) | — |

## Adenda 2022: capítulo de ingresos y estado de las rutas

**Rutas (tarea lateral 11.1, 2026-09-05 23:16, solo HEAD, nada descargado):** la ruta del **PEF aprobado** `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/ac01_ra_pp_ur_og.xlsx` responde **200 con content-type xlsx para 2022, 2023, 2024, 2025 y 2026**; las páginas `pef.hacienda.gob.mx/es/PEF{t}/analiticos_presupuestarios` responden 200 (los enlaces no se extraen con el patrón `href=".xlsx"`; navegar la página antes de descargar). La ruta del **PPEF (proyecto)** sigue en 404 para 2022–2026 (confirmado 2026-09-05). `transparenciapresupuestaria.gob.mx/es/PTP/Datos_Abiertos` responde 200 (no explorada). **Implicación:** para 2022–2026 existe el aprobado a nivel programa/UR/función y no el proyecto; la instrucción 2023 decide si se compara aprobado contra aprobado con etiqueta (§1.3 de la instrucción 2022).

**Otros 404 del 2026-09-05 en `ppef.hacienda.gob.mx/work/models/PPEF2022/`:** `docs/exposicion/EM_Documento_Completo.pdf`, `docs/exposicion/EM_Capitulo_1.pdf`, `paquete/ingresos/LISR_LIVA_LIEPS_CFF.pdf` (miscelánea), `paquete/ingresos/LFD_2022.pdf`, `paquete/ingresos/LIF_2022.pdf`. La ILIF se obtiene de `finanzaspublicas.hacienda.gob.mx/work/models/Finanzas_Publicas/docs/paquete_economico/ilif/ilif_{t}.pdf` (sirve). La miscelánea no tiene ruta conocida que sirva; probar `diputados.gob.mx` (Gaceta Parlamentaria) en 2023.

**Dónde vive cada objeto del capítulo de ingresos (2022):**

| objeto | fuente | ubicación 2022 |
|---|---|---|
| Ingresos por concepto, estimados | ILIF art. 1o. | PDF 59–70 (impresa 1–12); numerales 1 impuestos, 2 cuotas, 3 mejoras, 4 derechos, 5 productos, 6 aprovechamientos, 7 ventas (7.71 IMSS/ISSSTE, 7.72 Pemex/CFE), 9.97 FMP, 0 financiamientos |
| Ingresos presupuestarios (sin financiamiento) y su cierre con CGPE | ILIF art. 1o. total − numeral 0; CGPE IV.6 | PDF 59, 69; CGPE p. 120–121 (reconciliación en `_evaluacion/2022/00` §5: 56.9 mdp de ISR petrolero reclasificados) |
| RFP; inversión excluida del equilibrio; pago en especie; obligación de informar "Otros aprovechamientos" | ILIF art. 1o. párrafos posteriores al cuadro | PDF 70–72 |
| Techos de deuda | ILIF art. 2o.; CGPE 3.2.4 | PDF 73; CGPE p. 54 |
| Estímulos fiscales y exenciones | ILIF art. 16 | PDF 96–106 |
| Tasa de retención a intereses (metodología) | ILIF art. 21 | PDF 109–110 |
| DUC | ILIF art. 22; exposición IV | PDF 110; p. LII–LIII |
| Renuncias recaudatorias (cinco cifras); memoria de cálculo; series y proyección de ingresos | ILIF exposición I | p. I–VIII (memoria), IX–X (series 2017–2021, 2023–2027), X–XIII (renuncias) |
| Transitorios con ingresos (FONSABI remanente, Lotería, rendimientos de fideicomisos, FEIEF, IMSS-Bienestar con FASSA) | ILIF transitorios | PDF 118–124 |
| Ingresos 2021–2022 en pesos de 2022 con dos bases (LIF y estimado) por rubro e impuesto | CGPE 3.2.2 | p. 46–47 |
| Política de ingresos (medidas sin cifra) | CGPE intro y 3.2.2 | p. 13; 43–46 |
| Marco macro (aprobado 2021, estimado 2021, 2022) y mediano plazo | CGPE p. 39, 119; III.1 p. 100 | — |
| Precio máximo de referencia (fórmula art. 31 LFPRH) | CGPE IV.3 | p. 117 |
| Sensibilidades y amortiguadores | CGPE 3.3 | p. 58 |
| Series 2015–2021 en % PIB (ingresos por rubro e impuesto) | CGPE Anexo I.2 | p. 87 (y 84–86 RFSP, posición financiera neta) |
| 12 indicadores (tributarios sin IEPS combustibles; gasto neto sin inversión financiera, pensiones, participaciones, costo financiero) | CGPE IV.1 | p. 112 |
| Proyección 2023–2027 de ingresos y supuestos | CGPE 4.3 y III.2 | p. 80, 102, 104 |
| Reforma de subcontratación (cifras de evasión y afiliados) | CGPE 4.1.1; 2.1.2 | p. 65; p. 27 |
| Aportaciones del GF al IMSS (seguros; pensiones en curso; reservas) | DEC art. 5 | p. 7 |
| Gastos obligatorios con y sin pensiones | DEC Anexo 3 | p. 55 |
| Gasto neto y déficit | DEC art. 2 | p. 2 |
| Base LIF t−1 por concepto | ILIF t−1 art. 1o. | 2021: PDF 56–64 |

## Adenda 2023: deuda y balance, piezas metodológicas, rutas y sondas

**Rutas y sondas (2026-09-06):**
- **Nota metodológica SHCP "Balance Fiscal en México. Definición y Metodología":** la ruta canónica `secciones.hacienda.gob.mx/work/models/estadisticas_oportunas/metodologias/1bfm.pdf` sirve siempre la **edición vigente** (abril 2026 al consultar; 42 pp, con texto). Ediciones anteriores: Wayback conserva 2022-01/07/09/10 (abril 2022) y 2024-08 (abril 2024), no 2023. La **edición abril 2023** está en la Gaceta Parlamentaria como anexo del oficio de la SHCP: `gaceta.diputados.gob.mx/PDF/65/2023/may/Shcp_balanceF-20230509.pdf` (44 pp, **escaneo sin texto**; pp. 3–4 y 26 y 40–41 cotejadas contra la edición 2022 con texto: mismo contenido y paginación en las secciones I, IV.1 y Anexo IV). Patrón para otros años: índice HTML `gaceta.diputados.gob.mx/Gaceta/65/{año}/may/{aaaammdd}.html` y buscar `Shcp_balanceF` o `Shcp-…`; la edición abril 2022 está en `PDF/65/2022/may/Shcp-20220503.pdf` (con texto).
- **Cantú, Ramones y Villarreal (2016):** `economia.unam.mx/assets/pdfs/econmex/01/07CantuRamones.pdf` devuelve 404 desde 2026 (el sitio migró); Wayback captura 2025-10-18 (`web.archive.org/web/20251018171417id_/…`). El índice del número 1 tampoco está vivo; los PDF se llaman `NNApellido.pdf` (00Presentacion, 01Ros, 02CIbarra, 03HdzLaos, 04CamposVqz, 05Fujii, 06MorenoBrid, 07CantuRamones).
- **DOF (para el DUC):** `dof.gob.mx/nota_detalle.php?codigo=…&fecha=…` sirve HTML con el texto del decreto (el host `www.dof.gob.mx` falla por certificado; usar sin `www`). Decreto de reforma a la LISH: código 5581294, 09-12-2019 (art. 39 → 54 %; Transitorio Segundo: 58 % para 2020; 65 % era la tasa de 2019). Decreto de beneficios fiscales a asignatarios (crédito contra el DUC): 21-04-2020 (citado en el considerando del decreto 5609025 de 28-12-2020, que difiere el pago de noviembre de 2020). 40 % para 2022 y 2023: LIF 2022 art. 22 e ILIF 2023 art. 22 (PDF 94), "en sustitución de la tasa prevista en el artículo 39".
- **Transparencia Presupuestaria (sonda acotada, instrucción §10.1):** `transparenciapresupuestaria.gob.mx/es/PTP/Datos_Abiertos` responde 200 pero es una cáscara JavaScript sin enlaces en el HTML (1.9 KB); las rutas adivinadas `work/models/PTP/DatosAbiertos/Bases_de_datos_presupuestales/{PPEF_2023,ppef_2023,PEF_2023}.zip` devuelven 404. **Resultado: el proyecto 2023 a nivel programa no se obtuvo por esta vía; harían falta un navegador o la API del portal.** Nada descargado. La decisión sobre analíticos sigue diferida a 2024.
- **PEF aprobado, analítico de entidades** (`pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/ac01_ra_pp_ur_og_efe.xlsx`): descargado para 2022 (3.4 MB) y 2023 (2.9 MB) con el bundle de certificados de la bitácora; hoja `Hoja1`, columnas ETAPA, CICLO, SECTOR, ENTIDAD, TPP, GPP, IPP, PP, F, FN, SF, AI, TG, FF, PE, EF, CC, IMPORTE PEF (pesos). Sirve para IMSS TG 4 (pensiones): 636,461.8 (2022) y 750,252.1 (2023) mdp.
- `www.ppef.hacienda.gob.mx/work/models/PPEF2023/…` sigue en 404 (Tomo I, analíticos del proyecto).

**Dónde vive cada objeto del capítulo de deuda (2023):**

| objeto | fuente | ubicación 2023 |
|---|---|---|
| Balance público / presupuestario / no presupuestario / sin inversión / primario / RFSPF, en mdp y % PIB | CGPE IV.6 (dos columnas 2022: aprobado con PIB de aprobación; estimado) | p. 150–151; p. 69 (por entidad: GF, IMSS, ISSSTE, Pemex, CFE); p. 19 (resumen) |
| Fuera del presupuesto por componente (IPAB, Pidiregas, adecuaciones, deudores, banca) | CGPE 3.2 texto (dos decimales) y III.2 (un decimal) | p. 66–67; p. 135 |
| Regla del 25 % del costo financiero (art. 11 RLFPRH) | CGPE 3.2 | p. 16, 66 |
| Inversión excluida del equilibrio (perímetro de la regla) | ILIF art. 1o. párrafo tras el cuadro; CGPE nota 1 del IV.6 | ILIF PDF 58; CGPE p. 150 |
| Déficit presupuestario (cifra legal) | DEC art. 2 | p. 2 |
| Endeudamiento neto del GF (informativo) y financiamientos por fuente | ILIF art. 1o. numeral 0 | PDF 57 |
| Techos interno/externo GF, Pemex, CFE, IPAB (canje), banca (intermediación), CDMX; cláusula de intercambio | ILIF arts. 2o.–3o.; CGPE 3.5 | ILIF PDF 60–63; CGPE p. 18–19, 87 |
| SHRFSPF, deuda neta SPF, deuda bruta SPNF (% PIB, interno/externo, 2016–2028) | CGPE Anexo I.1 y III.2 | p. 120 (serie; nota: SHRFSP 2020 = 51.6), p. 122 (PFN; SHRFSP 2020 = 52.4), p. 135 (2022–2028) |
| Deuda neta/bruta en pesos, colocación y amortización, 2014–jul 2022 | CGPE Anexo I | p. 126 |
| Costo financiero total, GF (Ramos 24 y 34), EPE | CGPE IV.6; DEC Anexo 1 (ramos generales y 1.E) y Anexo 8 | CGPE p. 150; DEC p. 61, 66 |
| Costo financiero por fuente (externa, valores internos, otros) | **Tomo I** (ausente); CIEP fig. 11.2 lo reproduce | — |
| Indicadores del portafolio (moneda, tasa fija, plazo, duración, revisa tasa) | CGPE 3.5 cuadro | p. 88 (rótulo "bruta"; CGPE 2022 p. 56 decía "neta") |
| Amortizaciones GF 2023–2028 (interno mdp, externo mdd) | ILIF exposición III | p. XXXIX |
| Amortizaciones sector público por acreedor, saldo jun-2022 | CGPE III.3 | p. 139 |
| Bonos externos GF con vencimiento en el año | CGPE 3.5; ILIF III | p. 87; p. XXXVII |
| Sensibilidades (0.5 pp PIB, 1 dpb, 10 centavos, 50 mbd, 100 pb) | CGPE 4.3.1 | p. 102 |
| Marco macro con Cetes nominal y real, deflactor, tipo de cambio, 2021–2028 | CGPE III.1 (y 3.1 p. 39–40 para 2022–2023) | p. 134 |
| Supuestos fiscales de mediano plazo (pensiones +4.2 % real; inversión = balance; RFSPF 2.7) | CGPE III.2 cuadros de supuestos | p. 137–138 |
| Pasivo pensionario por institución; SAR; PBAM | CGPE 4.3.2 | p. 104–105 |
| Pidiregas (exposición contingente; compromisos de pago) y APP | CGPE 4.3.2 y III.3; DEC Anexo 6 | p. 106, 140; DEC p. 64–65 |
| Seguro de depósitos, banca de desarrollo, desastres, amortiguadores | CGPE 4.3 | p. 103, 105–107 |
| Descomposición oficial ex post del cambio del SHRFSPF (PIB, endeudamiento bruto, activos, euro, peso) | ILIF del año siguiente, exposición III "Evolución de la deuda del Gobierno Federal" | ILIF 2022 p. XXX (2019→2020); ILIF 2023 p. XXXII (2020→2021); ILIF 2024 p. XXVIII (2021→2022) |
| SHRFSPF en pesos por componente, ex post | Nota metodológica SHCP, Anexo IV | edición 2023 p. 40 (2021: 13,103,964; 2022: 14,065,537 mdp) |
| Definiciones de balances, sectores y deuda bruta/neta | Nota metodológica SHCP | p. 3 (LFPRH art. 2), p. 6 (subsectores MEFP), p. 12–13 (sector público federal y subsectores), p. 16 (deuda bruta/neta), p. 25–26 (presupuestario, no presupuestario, público; énfasis en presupuestario desde 2023), p. 40 (SHRFSP) |
| Ecuación de la razón deuda/PIB con crecimiento e inflación separados; "señoreaje fiscal" | Cantú, Ramones y Villarreal (2016) | p. 268–270 (ecuación y tres implicaciones), p. 272–276 (proyecciones 2030) |

## Historial
- 2026-09-05 · ejercicio 2020 · creado.
- 2026-09-05 · ejercicio 2021 · adenda (rutas PPEF t y PEF t−1, estado 2022–2026, perímetros de salud).
- 2026-09-05 · ejercicio 2022 · adenda (rutas: aprobado 2022–2026 sirve, proyecto 404, miscelánea y EM 2022 404; mapa del capítulo de ingresos).
- 2026-09-06 · ejercicio 2023 · adenda (rutas de la nota metodológica y del artículo autoral, DOF para el DUC, sonda a Transparencia Presupuestaria, analíticos del PEF aprobado de entidades; mapa del capítulo de deuda).

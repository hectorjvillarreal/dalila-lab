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

---

## Adenda 2026-09-06 · corrida de evaluación CIEP 2024 (educación)

### Dónde vive cada peso del gasto educativo

**Por ramo (función Educación del Gobierno Federal, finalidad 2 / función 5, bruta, PEF aprobado 2024, mdp):** Ramo 33 Aportaciones Federales **526,250.1** (51.0 %); Ramo 11 Educación Pública **411,848.3** (39.9 %); Ramo 25 Previsiones y Aportaciones **82,460.5** (8.0 %); Ramo 08 Agricultura 5,346.7; Ramo 07 Defensa 3,854.1; Ramo 13 Marina 2,230.0; Ramo 47 Entidades no Sectorizadas 631.7. **Total 1,032,621.4.** Las entidades de control directo (IMSS, ISSSTE, Pemex, CFE) tienen **cero** en función Educación; el EBDI del ISSSTE (3,013.0) es Protección Social.

**Por subfunción (misma fuente, 2024 aprobado):** 1 Educación básica 650,707.5; 2 Media superior 145,417.1; 3 Superior 165,466.5; 4 Posgrado 10,322.0; 5 Adultos 5,452.1; 6 Otros servicios educativos 55,256.3.

**Los fondos federalizados (Ramo 33, programas):** I013 FONE servicios personales 454,187.0; I014 FONE otros de gasto corriente 11,823.4; I015 FONE gasto de operación 17,901.9; I016 FONE fondo de compensación 12,880.5 (**FONE total 496,792.7 = 48.1 % de la función**); I009 FAETA tecnológica 5,798.0; I010 FAETA adultos 3,593.8; I007 FAM infraestructura educativa básica 12,842.0; I008 FAM infraestructura MS y S 7,223.6. **El reparto del FONE por entidad está en el Anexo 22 del decreto** y es reproducible desde el analítico de Gobierno Federal por la columna EF. **La Ciudad de México no está en el FONE:** su educación básica y normal va por el Ramo 25 (PP 003 y 004).

**Ramo 25:** PP 003 Servicios de educación básica en la CDMX 49,736.3; PP 004 Educación normal en la CDMX 1,378.4; PP 002 Previsiones salariales del FONE 25,637.0; PP 003 Previsiones del FAETA 311.9; PP 001 Actividades de apoyo administrativo 5,198.0; PP 001 Becas para la población atendida por el sector educativo 199.0. **Las previsiones se distribuyen al FONE durante el año y no aparecen en el FONE al aprobar.**

**Educación superior:** subsidio a universidades públicas estatales = U006 (UR 511), 110,558.4 en 2024, con **reparto por entidad en el Anexo 29 del decreto** (74,688.8 entre 31 entidades; el resto vive en las UR 514, 515 y otras). Universidades federales como UR del Ramo 11: A3Q UNAM 50,418.4; M00 TecNM 21,715.2; B00 IPN 21,361.5; A2M UAM 9,465.5; L4J Cinvestav 2,908.0; A00 UPN 1,077.1. Antonio Narro va en el Ramo 08 (1,260.5).

**Becas:** las tres Benito Juárez y Elisa Acuña viven en el **Ramo 11, UR O00 Coordinación Nacional de Becas** (101,324.2 aprobado, la UR más grande de la SEP), **no en Bienestar**. Posgrado en el Ramo 38 (S190); artísticas en el 48; militares en 07 y 13; 199.0 en el Ramo 25.

**Cultura y CTI, para no confundirlos con educación:** cultura, deporte y recreación es **finalidad 2 / función 4** y vale 24,541.9 en el Gobierno Federal (cruza los ramos 48 y 11). Ciencia, tecnología e innovación es **finalidad 3 / función 8** y vale 60,385.7 (ramos 38, 11, 12, 08 y 23); sus subfunciones son 1 Investigación científica, 2 Desarrollo tecnológico, 3 Servicios científicos y tecnológicos, 4 Innovación (esta última íntegramente en el Ramo 23). El Anexo 12 del decreto (transversal de CTI, todos los ramos) vale 148,154.2.

### Rutas verificadas

- **Analíticos del PEF aprobado, Gobierno Federal:** `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/ac01_ra_pp_ur_og.xlsx` (ramo × programa × UR × objeto, ~9 MB) y `ac01_ra_f_ur_og.xlsx` (ramo × función × UR × objeto, ~6.7 MB). Descargados para 2023 y 2024 con el bundle de certificados. **Los datos están en la hoja `Hoja1`, no en la primera hoja**, que es un resumen de 45 filas por ramo y hace creer que el archivo está vacío. Columnas: ETAPA AC01, CICLO, RAMO, TPP, GPP, MOD, PP, UR, **F** (finalidad), **FN** (función), **SF** (subfunción), AI, TG, FF, PE, EF, CC, IMPORTE PEF (pesos). El código de programa se arma como `MOD[0] + PP[:3]`: la modalidad va en su columna, no en el código del PP.
- **Analíticos de entidades:** mismas rutas con sufijo `_efe`. Descargados para 2024 (y ya se tenían 2022 y 2023).
- **LIF aprobada:** en el portal, en la tabla del punto de entrada, columna LIF. Descargadas 2022, 2023 y 2024. Las cuotas del IMSS están en el artículo 1o., numeral 2, renglón 01 «Cuotas para el Seguro Social a cargo de patrones y trabajadores»: **411,852.5 (2022), 470,845.4 (2023), 535,254.7 (2024)**, idénticas a las de la ILIF de cada año.

### Resultado de las sondas (2026-09-06, una petición cada 2 s, verificación TLS activa)

- **El árbol PPEF sigue caído para 2024 y sigue vivo para 2021.** Las **subpáginas** responden 200 en los dos años (`/es/PPEF2024/exposicion_de_motivos`, `/es/PPEF2024/analiticos_presupuestarios`) y **listan los archivos**, pero para 2024 **los siete archivos que la página enumera dan 404**: `docs/carta/Carta.pdf`, `docs/exposicion/EM_Anexo.pdf` y `EM_Capitulo_{1..4}.pdf`, `EM_Documento_Completo.pdf`. Control 2021: `work/models/PPEF2021/docs/exposicion/EM_Documento_Completo.pdf` responde **200 application/pdf**. **Diagnóstico: almacén de archivos roto o reubicado para 2022–2026, no retirada de documentos.** Las páginas índice se generan de una base que sí conserva las entradas.
- **Trampa de ruta en las páginas de analíticos.** La página lista `analiticosPresupuestarios/ac01_*.xlsx` **sin el segmento `/Proyecto/`**, y esa ruta da 404 **incluso para 2021**. La ruta que funciona en 2021 es `analiticosPresupuestarios/**Proyecto**/ac01_ra_pp_ur_og.xlsx` (200, xlsx). Las páginas índice están desactualizadas respecto al almacén en todos los años; no tomar sus href como ruta canónica.
- **Wayback no tiene la exposición de motivos del PPEF 2024** (consulta a `archive.org/wayback/available` con y sin `www`: `archived_snapshots` vacío).
- **Transparencia Presupuestaria comparte la cadena TLS rota de la SHCP** y el mismo bundle la arregla: `www.transparenciapresupuestaria.gob.mx` falla con «unable to get local issuer certificate» contra el almacén del sistema y responde 200 con `--cacert`. Hallazgo nuevo, aplicable a futuras sondas. `/es/PTP/Datos_Abiertos` devuelve **1,919 bytes de cáscara JS sin un solo enlace a archivo y sin la cadena «PPEF»**, lo que corrobora lo que CIEP denuncia en su presentación: no hay base de datos del PPEF en datos abiertos.

### Contenido de la ILIF única · RESUELTO tras cinco corridas

**El portal no ofrece una «exposición de motivos de la ILIF» como pieza separada porque no existe: el PDF de la ILIF la contiene.** Estructura verificada en los nueve ejercicios 2018–2026: oficio de remisión a la Mesa Directiva, **exposición de motivos**, articulado. En 2020–2026 la sección lleva el encabezado literal «EXPOSICIÓN DE MOTIVOS»; en 2018 y 2019 el mismo texto va sin encabezado. En 2024 la exposición ocupa las páginas 1–65 del PDF y el articulado empieza en la 66 (artículo 1o.).

**Consecuencia para el manifiesto:** las nueve piezas «ILIF exposición de motivos» dejan de contarse como faltantes. El faltante real del proyecto se reduce a **cinco documentos: la exposición de motivos del PPEF 2022–2026**, y esos están caídos en el servidor, no ausentes del portal.

---

## Adenda 2026-09-06 · corrida de producción, documento propio 2025

### Piezas del paquete 2025 y su estado

| pieza | ruta | estado |
|---|---|---|
| CGPE 2025 | `finanzaspublicas.hacienda.gob.mx/work/models/Finanzas_Publicas/docs/paquete_economico/cgpe/cgpe_{t}.pdf` | **sirve, y viene SIN CAPA DE TEXTO** |
| LIF aprobada | `…/docs/paquete_economico/lif/lif_{t}.pdf` | sirve; descargadas 2022–2025 |
| ILIF | `…/docs/paquete_economico/ilif/ilif_{t}.pdf` | sirve; contiene su propia exposición de motivos |
| Analíticos del PEF aprobado | `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/{ac01_ra_pp_ur_og, ac01_ra_f_ur_og, + _efe}.xlsx` | sirven; 2025 descargados y verificados al byte |
| Exposición de motivos del PPEF | `ppef.hacienda.gob.mx/work/models/PPEF{t}/docs/exposicion/…` | **404 para 2022–2026**; el control de 2021 sirve |

### El CGPE 2025 no tiene capa de texto

**Noventa de sus noventa y una páginas son imagen.** La única con texto es la 34 y contiene las fórmulas del PIB potencial y del límite máximo de gasto corriente estructural, que quedaron como objetos incrustados. Se comprobó que el portal no sirve otra edición: la ruta canónica devuelve el mismo archivo de 22,852,266 bytes.

**Procedimiento que funcionó:** leer el índice (p. 2) para mapear el documento, renderizar con `pdftoppm -png -r 150 -f N -l N` solo las páginas de los anexos, y leerlas como imagen. Los cuatro anexos que resuelven casi todo el documento son **II.5 (p. 81) marco macro 2024-2025**, **II.6 (p. 82) estimación de finanzas públicas**, **III.1 (p. 84) marco macro 2023-2030** y **III.2 (p. 85) perspectivas de finanzas públicas 2024-2030**. Con esas cuatro páginas se construyen el capítulo macro, el de agregados de gasto y el de deuda.

**Validación:** no por relectura sino por identidad contable. Cincuenta pruebas de cierre y de coherencia entre anexos, todas pasan. Ver `documento_2025/verificar.py`.

### Estructura de los analíticos, precisada

- La hoja de datos es **`Hoja1`**; la primera es una carátula de 45 filas por ramo.
- En los cortes **por función** (`ac01_ra_f_ur_og` y `_efe`) las columnas `F` y `FN` vienen **como texto con nombre** («2 Desarrollo Social», «5 Educación»); en los cortes por programa vienen como número. Coercionarlas a número sin mirar destruye la etiqueta. Con pandas 3 el dtype es `str`, no `object`: preguntar por `is_numeric_dtype`, no por `== object`.
- El código de programa se arma como `MOD[0] + PP[:3]`.
- **Agrupar siempre por clave, nunca por nombre:** el Ramo 38 se llama «Humanidades, Ciencias, Tecnologías e Innovación» en 2024 y «Ciencia, Humanidades, Tecnología e Innovación» en 2025.

### Identidades que cierran y sirven de control

- Gobierno Federal bruto + entidades − neteo del Anexo 1 = gasto neto total del decreto. En 2025: 7,603,962.3 + 3,191,122.8 − 1,493,069.3 = 9,302,015.8. **Exacto.**
- Total de la Ley de Ingresos = gasto neto total del decreto = 9,302,015.8.
- Gasto neto total − diferimiento de pagos = gasto neto pagado del CGPE.
- **Anexo 3 del decreto: gastos obligatorios con pensiones − sin pensiones = pensiones y jubilaciones de la clasificación económica.** 2024: 7,327,588.8 − 5,828,550.2 = 1,499,038.6. 2025: 7,684,111.9 − 6,046,446.8 = 1,637,665.1. Reproduce al mdp la construcción desde los analíticos (tipo de gasto 4 de entidades más tipo de gasto 4 del GF sin la partida 45203). **Es la fuente que adjudica el perímetro de pensiones.**

### Dónde vive cada objeto de 2025

- **Pensiones no contributivas:** Ramo 20, programas **S176** (Adultas Mayores, 483,427.6), **S286** (Discapacidad, 28,961.4) y **U316** (Mujeres Bienestar, 15,000.0, nuevo en 2025). Seleccionar por clave: el nombre está en femenino.
- **Función Salud:** finalidad 2, función 3. El programa **R023** del Ramo 19 (adeudos con IMSS e ISSSTE) pasa de 52,324.5 a 339.8: era una liquidación de 2024 y su desaparición no es un recorte al servicio. **S038** IMSS-Bienestar sale del Ramo 19 y el organismo del Ramo 47 sube.
- **Obra de transporte:** la función 3.5 apenas se mueve (212,619.2 → 214,635.9) pero cambia de ejecutor: Defensa 127,556.9 → 41,772.1, Secretaría de Infraestructura 80,811.1 → 147,181.7, Marina 4,251.2 → 25,682.1. En la Secretaría, la dirección de desarrollo ferroviario cambia de clave 311 a 215.
- **Guardia Nacional:** unidad **H00 del Ramo 36** en los dos años, 70,767.4 → 33,799.8. **No se mudó a Defensa.**

### El deflactor de CIEP 2025

**1.04252**, recuperado de seis programas independientes de su cuadro 6.1 que cierran al décimo. No es el deflactor del PIB de 4.3 % que declara el CGPE: es el 4.25 % de la fórmula del límite de gasto corriente estructural. Sus columnas rotuladas «PEF 2024» están en pesos de 2025.


---

## Adenda 2026-09-07 · corrida 2026, fase 1 · **LOS ANALÍTICOS DEL PROYECTO SÍ EXISTEN**

### La corrección más importante de este archivo

Desde el 2026-09-05 este mapa registra que «la ruta del PPEF (proyecto) sigue en 404 para
2022–2026» y que «para 2022–2026 existe el aprobado a nivel programa/UR/función y no el
proyecto». **Era un problema de host, no un documento ausente.**

Los analíticos del **proyecto** viven en el almacén histórico de `pef.hacienda.gob.mx`, en
una subcarpeta `Proyecto/` paralela a la `Autorizado/` que este mapa documenta desde 2021:

```
https://www.pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Proyecto/{archivo}.xlsx
https://www.pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/{archivo}.xlsx
```

Archivos: `ac01_ra_pp_ur_og`, `ac01_ra_f_ur_og`, y sus `_efe`. **Verificado el 2026-09-07:
los cuatro cortes responden 200 para 2021, 2022, 2023, 2024, 2025 y 2026** — veinticuatro
peticiones, veinticuatro 200. Con el bundle de certificados; sin él, falla el TLS.

**Nadie sondeó esa ruta** porque el proyecto se buscó siempre en `ppef.hacienda.gob.mx`, que
es donde estuvo hasta 2021 y donde el almacén sigue roto. La página de analíticos del portal
PPEF **sigue** listando los archivos —y sigue listándolos sin el segmento `/Proyecto/`, la
trampa de rutas ya documentada— y **los catorce enlaces devuelven 404** para 2026
(reverificado 2026-09-07). El control de 2021 en ese host sigue en 200.

**Prueba de aceptación, contra una cifra publicada por un tercero.** El perímetro educativo
de CIEP 2025 —ramos 11, 38 y 48 completos más el resto de la función Educación— reconstruido
sobre `2025/Proyecto/ac01_ra_f_ur_og.xlsx` da **1,142,490.5 mdp** contra los **1,142,490.0**
que CIEP publica del proyecto. **Medio millón de pesos sobre 1.14 billones.** El archivo es
el proyecto, no una copia del aprobado: sobre el aprobado el mismo perímetro da 1,161,164.8.

**Consecuencias para el resto de la serie FISCUS:**
- La comparación **proyecto contra proyecto** es posible desde 2021, a nivel de programa y de
  unidad responsable. Deja de haber techo de granularidad en la línea primaria.
- La serie **pensiones IMSS / cuotas IMSS ex ante**, congelada desde 2022 por falta de la
  exposición de motivos del PPEF, **se puede reconstruir** desde el analítico de entidades
  del proyecto, tipo de gasto 4, para 2021–2026.
- La decisión de la corrida 2025 de trabajar «aprobado contra aprobado» era legítima con lo
  que se sabía y **su premisa era falsa**. El documento 2025 declaró su objeto y no cambia;
  lo que cambia es el motivo por el que lo eligió.

### El repositorio de datos abiertos de la SHCP (ATDT)

Segundo hallazgo de la fase 1. Existe y no estaba en este mapa. Se descubre por la API CKAN
de `datos.gob.mx` (`/api/3/action/package_search?q=...`; el host `datos.gob.mx` devuelve 403
al navegador y 200 a la API, y `/busca/api/...` es 404: usar `datos.gob.mx/api/3/...`).

| conjunto | ruta | contenido |
|---|---|---|
| Proyecto de PEF | `repodatos.atdt.gob.mx/api_update/secretaria_hacienda/proyecto_presupuesto_egresos_federacion/PPEF_2026.csv` | 129,908 filas, 33 columnas: ciclo, ramo, UR, grupo funcional, función, subfunción, AI, modalidad, PP, **capítulo, concepto, partida genérica y específica**, tipo de gasto, fuente de financiamiento, **entidad federativa**, **clave de cartera**, monto. 77 MB |
| Anexos transversales del PPEF | `…/analitico_plazas_remuneraciones_apf_ppef/anexos_transversales_ppef2026.csv` | el desglose por programa de cada anexo transversal, con vertiente y componente. 124 MB |
| Plazas y remuneraciones del PPEF | `…/analitico_plazas_remuneraciones_apf_ppef/analitico_plazas_apf_PPEF.csv` | plazas, horas y percepciones por unidad y rango salarial. 11.7 MB |

**Es más rico que los xlsx**: funde el corte por programa y el corte por función en una sola
tabla y añade partida específica y clave de cartera. Cubre Gobierno Federal **y** entidades:
los ramos 50 IMSS, 51 ISSSTE, 52 Pemex, 53 CFE, 54 Mujeres, 55 ATDT y **56 Servicios de
Salud del IMSS para el Bienestar**. Total bruto 2026: **11,746,796.8 mdp**.

**Trampa capital: el repositorio guarda UNA sola ranura y la sobrescribe.** `PPEF_2025.csv`,
`PPEF_2024.csv` y los anteriores devuelven **503** (dos intentos cada uno, con control 200
sobre `PPEF_2026.csv` y 503 sobre el listado del directorio). El conjunto de CKAN declara un
solo recurso. **Lo que no se descargue el día de la entrega desaparece cuando llega el
paquete siguiente.** Y la nota del conjunto ya dice «ejercicio fiscal 2027» mientras el
archivo todavía sirve `ciclo = 2026`: la ranura está por rotar.

Nota de fecha: el recurso figura como creado el **2026-02-24**, tres meses después de la
entrega del paquete 2026. No se puede saber desde CKAN si eso es la primera publicación o
una migración del portal. **Queda como pregunta abierta para la corrida 2027: comprobar el
día de la entrega si el CSV ya está.**

### La Gaceta Parlamentaria publica el paquete completo el día de la entrega

Tercer hallazgo, y el más útil para una lectura en vivo. El paquete 2026 se entregó el
**8 de septiembre de 2025** y la Gaceta Parlamentaria de ese día (año XXVIII, número 6871)
lo publica íntegro, con URLs estables:

```
https://gaceta.diputados.gob.mx/Gaceta/66/2025/sep/20250908.html      (índice)
https://gaceta.diputados.gob.mx/PDF/66/2025/sep/20250908-{A..L}.pdf   (anexos)
```

| anexo | contenido |
|---|---|
| A | **Iniciativa de Ley de Ingresos** 2026 |
| B | **Proyecto de Presupuesto de Egresos** 2026 |
| C | **Criterios Generales de Política Económica** 2026 |
| D | Ley Federal de Derechos |
| E | **Ley del IEPS** |
| F | **Código Fiscal de la Federación** |
| G | Informe sobre la facultad arancelaria (art. 131 constitucional) |
| H, J, K | Nota metodológica y listados de zonas de atención prioritaria 2026 |
| I | Comunicaciones de la Junta de Coordinación Política |
| L | Recursos federales para subsidios de vivienda y suelo |

**Esto resuelve el problema de adquisición de una lectura en vivo.** El portal de la
Secretaría es lento y su almacén se rompe; la Gaceta publica las tres piezas grandes y la
miscelánea el mismo día, en un host que conserva su archivo histórico. Para la corrida 2027:
**la Gaceta del día de la entrega es la primera parada, no la última.**

**Hallazgo de contenido:** la miscelánea 2026 son tres leyes —Derechos, IEPS y Código
Fiscal— y **no hay iniciativa de reforma al ISR ni al IVA**. Es una afirmación del capítulo
de ingresos que se obtiene del índice de la Gaceta en un minuto.

### Capa demográfica (tier `externa_demografica`)

| denominador | ruta | cobertura |
|---|---|---|
| Población a mitad de año | `repodatos.atdt.gob.mx/CONAPO/proyecciones/00_Pob_Mitad_1950_2070.csv` | 1950–2070, **32 entidades × edad simple 0–109 × sexo**. 45 MB. Verificado: 2026 = 134,407,258 personas; 65 y más = 12,201,321; de 3 a 14 años = 25,421,421 |
| Indicadores demográficos | `datos.gob.mx/dataset/f2b9b220-…/download/05_indicadores_demograficos_proyecciones.csv` | 1950–2070 por entidad: esperanza de vida, índice de envejecimiento, nacimientos, migración. 1.7 MB. **Devuelve 403 sin `User-Agent` de navegador**; con él, 200 |

Resuelve cuatro de los siete denominadores del pacto: población total, población de 65 y
más, población en edad escolar y población por entidad. Quedan pendientes matrícula,
afiliación a IMSS e ISSSTE, y padrón de programas pensionarios.

### Estado del bundle TLS, reverificado

`http://yr1.i.lencr.org/` sirve el intermedio en **DER**: hay que convertirlo con
`openssl x509 -inform DER -outform PEM` antes de concatenarlo. Un `cat` del DER produce un
bundle que curl acepta sin protestar y que **no arregla nada**; el síntoma es idéntico al de
no tener bundle. Con el PEM correcto, `pef` y `ppef.hacienda.gob.mx` verifican.
`repodatos.atdt.gob.mx`, `datos.gob.mx` y `gaceta.diputados.gob.mx` no lo necesitan.

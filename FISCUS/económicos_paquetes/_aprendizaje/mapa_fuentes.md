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

## Historial
- 2026-09-05 · ejercicio 2020 · creado.
- 2026-09-05 · ejercicio 2021 · adenda (rutas PPEF t y PEF t−1, estado 2022–2026, perímetros de salud).

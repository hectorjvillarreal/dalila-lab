# Reporte — NTA y envejecimiento

## Parte 1 · `nta_p1_demografia`

Terminada el 1 de noviembre de 2026. PDF de exposición de 50 páginas y PDF para repartir de 20, compilados con `latexmk -pdf`, sin errores ni cajas desbordadas. Revisión visual hecha página por página sobre la versión para repartir. No queda ningún [VERIFICAR] en pantalla.

### Diapositivas y fuentes

| # | Título | Fuente | Min |
|---|---|---|---|
| 1 | Portada | — | 1 |
| 2 | Las finanzas públicas cobran a unas edades y gastan en otras | Manual, pp. 1–2 | 2 |
| 3 | Cuatro fases, dos curvas | Lee (2003); van de Kaa (1987); Lesthaeghe (2010) | 4 |
| 4 | La mortalidad cae primero | WPP 2024 | 3 |
| 5 | La fecundidad cae después | WPP 2024; INEGI; Manual, p. 8 | 4 |
| 6 | Debajo del reemplazo (opcional) | WPP 2024; proyección propia | 3 |
| 7 | Las pirámides cuentan la historia | WPP 2024; Censo 2020; proyección propia | 3 |
| 8 | América Latina envejece más rápido que Europa | Cálculo con WPP 2024; EIC 2025; Cecchini et al., p. 11 | 3 |
| 9 | El bono demográfico se abre y se cierra | Cecchini et al., pp. 32–33 y 44; Mason y Lee (2006); WPP 2024 | 2 |
| 10 | Nuestra pregunta | Redacción nueva sobre `DFD_rag.md` | 2 |
| 11 | Lo que proyectan y lo que medimos no coincide | WPP 2024; fuentes nacionales; Nota EIC 2025 v1.0 | 4 |
| 12 | El laboratorio DFD | `_ops/20260407_CROSS_CF_cross-tar-001-prep_v1.md` | 3 |
| 13 | El núcleo (opcional) | Misma; `DFD_rag.md`; `Integrated_6.tex` | 4 |
| 14 | Automatización | Acemoglu et al. (2026); nota de corpus | 4 |
| 15 | Una seguridad social para una población que envejece | Presentación para la CEPAL, láminas 5–10 | 4 |
| 16 | Pensiones: la trampa de la formalización | Presentación para la CEPAL; deck de Boston; CAF_DEM | 4 |
| 17 | Hicimos las cuentas de México | `Missions/Funded/NTA_Inequality/` | 2 |
| 18 | Cómo trabajamos (opcional) | PROTO-RAG-001; README del corpus | 3 |
| 19 | Tres ideas para llevarse | — | 3 |
| 20 | Para la Parte 2 | — | 2 |

Preguntas a la clase como último overlay: diapositivas 5, 11 y 20.

**Opcionales:** 6 (3 min), 13 (4 min) y 18 (3 min). Suman 10 minutos.

### Cifras verificadas

| Cifra | Fuente |
|---|---|
| Natalidad y mortalidad de México, 1950–2023; TGF 6.53 (1970) y 2.71 (2000); cruce de 2.1 en 2016 | WPP 2024, archivo de indicadores en Dalila |
| América Latina y el Caribe, TGF 1.80 en 2024 | WPP 2024 |
| México: 47.7 % menores de 15 y 2.7 % de 65+ en 1970 | WPP 2024 |
| México: 25.3 % y 8.2 % en 2020; 126.0 millones en total | Censo 2020, `inegi_cpv2020_single_age_prorated.csv` |
| México 2050: 129.4 M, 22.6 % de 65+, 12.7 % menores de 15 | Motor nacional, vuelto a correr: reproduce sus resultados guardados |
| Máximo de 132.5 M en 2038; 20 % de 65+ hacia 2045 | `projections_national.csv` |
| Años de 10 % a 20 % de 65+ | Cálculo con WPP 2024, `datos/p1_velocidad.csv` |
| Dependencia: 88 por 100 en 1965, 48 hacia 2029 | Cálculo con WPP 2024 |
| Fin del bono en 2028; 6.1 % y 0.9 % | Cecchini et al., pp. 32–33 |
| TGF 1.9 (2019) y 1.23 (2024); 10 % de 65+ en 2025 | INEGI, entrada de corpus del 22 de septiembre |
| TGF de Chile, Costa Rica y Colombia | `scenario_anchors.md` y WPP 2024 |
| Escenarios 2050: 144.2, 135.5, 128.7 y 121.2 M | `nota_EIC2025_v1.0` |
| ONU 2050: 148.9 M | WPP 2024 |
| 88.6 %, 54.5 %, 76.3 %, 71.7 % | `resumen_ejecutivo.tex` |
| Lee (2003), van de Kaa (1987), Lesthaeghe (2010), Mason y Lee (2006) | Bibliotecas y bibliografía del informe |
| Acemoglu et al.: julio de 2026 | PDF de NBER. Resuelve la fecha en disputa de la nota de corpus: junio es el borrador del MIT |

### Lo que quité o no pude verificar

- **«Historia contributiva» (diapositiva 13).** Quitada. En IM-6 la pensión es una tasa de reemplazo por el ingreso laboral medio; no encontré esa variable.
- **Observatorio Demográfico 2025.** No lo pude abrir: CEPAL bloquea la descarga y no hay copia archivada de los enlaces probados. Uso WPP 2024, la misma revisión, y cito ONU. Los valores de Chile y Costa Rica coinciden con los de `scenario_anchors.md`.
- **20 % a 40 % del ingreso del hogar (Fietz et al.).** Solo en la nota del presentador, tomado del deck de Boston. No volví a la fuente.
- **Cuantificaciones de Acemoglu et al.** Fuera de pantalla: la nota de corpus no está respaldada.
- **Presentación para la CISS.** No apareció.

### Archivos de Dalila usados

| Archivo | Respaldo |
|---|---|
| `_crossrefs/corpus/demographics/scenario_anchors.md` | `endorsed_by: Anne` |
| `_crossrefs/corpus/demographics/releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md` | `endorsed_by: Anne` |
| `_crossrefs/corpus/demographics/2026-07-11_baby-busts-growth-booms.md` | **`endorsed_by` vacío**: revisión pendiente de Cath y Elle |
| `GrandPlan/DFD/research/fertility_collapse_abm/STAGE3a_Nina_signoff.md` | `endorsed_by: Nina`, con cinco condiciones |
| `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/nota_EIC2025_v1.0.pdf` | Revisada por Anne y Cath; pendiente de tu firma |
| `GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa/` | Sin respaldo; producto de comunicación |
| `_ops/20260407_CROSS_CF_cross-tar-001-prep_v1.md` | Sin respaldo; preparatorio |
| `GrandPlan/DFD/DFD_rag.md`, `Missions/Funded/BID2/Integrated_6.tex` | No son entradas de corpus |
| `Missions/Funded/NTA_Inequality/` | Sin respaldo; trabajo en curso |
| Presentación para la CEPAL, `boston_20260828_v2.tex`, `caf-dem-entregable-final/main.tex` | No son entradas de corpus |

### Desviaciones del esquema aprobado

1. **Escenarios de 2050.** El esquema traía 144.5, 135.8, 129.0 y 121.4 M, cifras de una versión previa. La Nota v1.0 dice 144.2, 135.5, 128.7 y 121.2 M. Uso estas, y corregí el esquema.
2. **Dos cifras parecidas para 2050.** La diapositiva 7 da 129.4 M (motor nacional) y la 11 da 128.7 M (Nota). Son modelos distintos con la misma TGF; la nota del presentador lo advierte.
3. **Diapositiva 8.** Agregué que México, con datos nacionales, tardaría unos 20 años y no 28. Quité Alemania del gráfico.
4. **Diapositiva 9.** Agregué una gráfica de dependencia calculada con WPP. El mínimo cae en 2029; CEPAL dice 2028.
5. **Diapositiva 7.** Muestra menores de 15 y 65+. El grupo de 15 a 64 se quitó por espacio.
6. **Diapositiva 16.** La interpretación de «el cero se habla con el uno» es mía.
7. **Diapositiva 19.** La tercera idea junta diseño y medición; no estaba redactada en el esquema.

## Parte 2 · `nta_p2_manual`

Terminada el 1 de noviembre de 2026. PDF de exposición de 58 páginas y PDF para repartir de 22, compilados con `latexmk -pdf`, sin errores ni cajas desbordadas. No queda ningún [VERIFICAR] en pantalla.

### Diapositivas y fuentes

| # | Título | Fuente | Min |
|---|---|---|---|
| 1 | Portada | — | 1 |
| 2 | Consumimos toda la vida y producimos solo una parte | ntaccounts.org; Manual, pp. 3–4 | 2 |
| 3 | La economía generacional | Manual, pp. 1–3 | 2 |
| 4 | Tres formas de cubrir el déficit | Manual, pp. 3–5, cuadro 1.1 | 3 |
| 5 | Cada país paga la vejez de otra manera | ntaccounts.org con WPP 2024; Manual, pp. 15–16 | 3 |
| 6 | La razón de sostenimiento | Manual, pp. 10–11; cap. 5, cuadro 5.6 | 3 |
| 7 | Los dos bonos, en una identidad | Manual, pp. 10–14, ecs. 1.1–1.2 | 3 |
| 8 | Las flechas de Lee (opcional) | Manual, pp. 17–18, fig. 1.8 | 4 |
| 9 | La razón de sostenimiento fiscal | Manual, pp. 18–19 | 2 |
| 10 | Qué miden las NTA, y qué no | Manual, pp. 6, 25–29, 34–35 | 3 |
| 11 | La identidad de flujos | Manual, p. 29, ecs. 2.1–2.2 | 4 |
| 12 | El ciclo de vida económico, en dólares | Manual, pp. 35 y 39, cuadro 2.4 | 3 |
| 13 | El déficit del ciclo de vida, y una sorpresa mexicana | Manual, cuadros 2.2–2.3; ntaccounts.org; Misión NTA | 4 |
| 14 | Reasignaciones públicas | ntaccounts.org; Manual, pp. 16–17 y 40 | 4 |
| 15 | Reasignaciones privadas | Manual, pp. 27–28, 41, 53 | 3 |
| 16 | Reasignaciones basadas en activos | Manual, cuadros 2.2, 2.6 y 2.8 | 3 |
| 17 | Población por perfiles | Manual, pp. 3, 30, 50–51 | 3 |
| 18 | Comparaciones: México se sale del patrón (opcional) | ntaccounts.org | 3 |
| 19 | Lo que las NTA no ven | Manual, pp. 52–53 | 3 |
| 20 | Qué datos se necesitan (opcional) | Manual, pp. 28 y 56; Misión NTA | 3 |
| 21 | El presupuesto es un sistema de reasignaciones por edad | Manual, pp. 16–22 | 3 |
| 22 | Para la Parte 3 | — | 2 |

Preguntas a la clase como último overlay: diapositivas 5, 9, 14 y 22.

**Opcionales:** 8 (4 min), 18 (3 min) y 20 (3 min). Suman 10 minutos.

### Cifras verificadas

| Cifra | Fuente |
|---|---|
| Perfiles de Filipinas 1999, Alemania 2003, México 2004, 2010 y 2014, Brasil 2008, Chile 2018, Alemania 2008 | ntaccounts.org, `datos/ntaccounts_perfiles.csv`; normalización en `datos/prep_p2.py` |
| Cruces de 27, 60 y 58 años | Manual, p. 3; se reproducen con la base |
| Superávit de México: 45–46 años (2014), 37–50 (2010), 33–48 (2004) | Cálculo con la base |
| Reparto del déficit de 65+ en México, Japón, Alemania, Costa Rica y Suecia | Cálculo con la base y WPP 2024; suma 100 en cada país |
| China: 1.40, 0.73 y 0.52; 0.7 % y 0.5 % anual | Manual, cap. 5, cuadro 5.6; p. 11 |
| Valores de las flechas de Lee | Manual, fig. 1.8; la suma de riqueza da 366 contra 365 del texto |
| Brasil: 30 % | Manual, p. 19 |
| Todas las cifras de Estados Unidos 2003 | Manual, cuadros 2.2–2.8; 80 % = (10,400 + 9,835) / 25,273 |
| 76.3 %, 54.5 %, 10–53 %, 1.9–9.9 | `resumen_ejecutivo.tex`, `NTA_paper.pdf` |

### Lo que quité o no pude verificar

- **Cuenta Pública (diapositiva 20).** Quitada: nuestro trabajo no la usa como control.
- **Puntos de la fig. 1.6 (triángulo).** El Manual no da valores; los recalculé con la base y los muestro como cuadro.
- **Serie de la fig. 1.9 (Brasil).** El Manual solo da el 30 %, así que la barra dice «cerca de 0.7». No volví a calcular la serie.

### Archivos de Dalila usados

| Archivo | Respaldo |
|---|---|
| `Missions/Funded/NTA_Inequality/paper_final.tex`, `resumen_ejecutivo.tex` | Sin respaldo; trabajo en curso, rotulado así en pantalla |

La Parte 2 no usa entradas de corpus.

### Desviaciones del esquema aprobado

1. **Datos reales en lugar de gráficas estilizadas.** ntaccounts.org es pública y trae a México; la decisión 5 la dejaba como alternativa. Las diapositivas 2, 13, 14 y 18 usan perfiles reales. El servidor exige el encabezado `Referer` de un navegador; `datos/baja_ntaccounts.sh` lo manda.
2. **Hallazgo nuevo, diapositiva 13.** El promedio mexicano casi no tiene superávit en la base pública. No estaba en el esquema; es una serie independiente de nuestra base y coincide en dirección con nuestro resultado.
3. **Diapositiva 5.** Cuadro calculado en lugar del texto del Manual. Confirma lo que dice el Manual sobre México.
4. **Diapositiva 6.** Agregué el ejemplo de China del cap. 5, fuera de la lectura.
5. **Diapositiva 14.** Cambié la pregunta: el esquema hablaba del IVA de las medicinas, y las medicinas tienen tasa cero. Ahora son restaurante y predial. Es Brasil 2008 y México 2004, los años con pensiones por edad en la base.
6. **Diapositiva 13.** «Sorpresa mexicana» se suma al título aprobado.

## Parte 3 · `nta_p3_cepal`

Terminada el 1 de noviembre de 2026. PDF de exposición de 61 páginas y PDF para repartir de 22, compilados con `latexmk -pdf`, sin errores ni cajas desbordadas. No queda ningún [VERIFICAR] en pantalla. Fuente principal: Cecchini, Comelatto, Holz, Kang y Paes (2025), Serie Población y Desarrollo 140, LC/TS.2025/50; título, serie y año confirmados en el PDF.

### Diapositivas y fuentes

| # | Título | Fuente | Min |
|---|---|---|---|
| 1 | Portada | — | 1 |
| 2 | El informe en una diapositiva | Informe, pp. 7, 67–68 | 2 |
| 3 | En 28 años, la región duplica su proporción de mayores | Informe, pp. 9–11; WPP 2024 | 3 |
| 4 | El bono se acaba en 2028 | Informe, pp. 32–34 | 3 |
| 5 | La razón de sostenimiento ya tocó techo | Informe, pp. 35–36 | 3 |
| 6 | El déficit se muda a la vejez | Informe, pp. 39–45, cuadro 1, gráfico 25 | 4 |
| 7 | Crecimiento: pierden los que van adelante | Informe, pp. 46–47, gráfico 26 | 2 |
| 8 | Tres presiones que crecen al mismo tiempo | [FUERA] ntaccounts.org y WPP 2024; Informe, pp. 10, 67 | 3 |
| 9 | Pensiones: muchos cobran, pero no les alcanza | Informe, pp. 17–19; [FUERA] entregable CAF_DEM | 3 |
| 10 | Los niños son más pobres que los abuelos (opcional) | Informe, p. 16 | 3 |
| 11 | Pensiones en México | [FUERA] LSS, CPEUM, DOF, CGPE 2027 | 3 |
| 12 | Salud: el gasto sube con la edad | Informe, pp. 27, 49; [FUERA] ntaccounts.org | 2 |
| 13 | Financiamiento de la salud | [FUERA] OMS GHED; presentación para la CEPAL | 3 |
| 14 | Cuidados | Informe, pp. 10, 49, 68; [FUERA] cálculo propio | 3 |
| 15 | El tiempo también se transfiere | [FUERA] Manual NTTA (2024); INEGI | 2 |
| 16 | Cómo se paga todo junto | Informe, pp. 42–45; Manual NTA; presentación para la CEPAL | 3 |
| 17 | Lo que recomienda el informe | Informe, pp. 67–68 | 3 |
| 18 | Corea (opcional) | Informe, pp. 53–58 | 4 |
| 19 | México en el informe | Informe, pp. 19, 34, 47; cálculo propio; Misión NTA | 2 |
| 20 | La economía plateada (opcional) | Informe, pp. 11–13, 48–51 | 3 |
| 21 | Lectura crítica | Lectura propia | 3 |
| 22 | Para llevarse de las tres partes | — | 2 |

Preguntas a la clase como último overlay: diapositivas 16 y 21.

**Opcionales:** 10 (3 min), 18 (4 min) y 20 (3 min). Suman 10 minutos.

### Cifras verificadas

| Cifra | Fuente |
|---|---|
| 9.9 %, 18.9 %, 1.9 %, 5.1 %; 12 a 37 millones | Informe, pp. 9–10 |
| Fin del bono en 2028; duraciones por país; 6.1 % y 0.9 % | Informe, pp. 32–34, gráfico 18 leído en la imagen |
| Años de máximo de la razón de sostenimiento | Informe, p. 36 |
| Cuadro 1; edades medias | Informe, cuadro 1 y gráfico 25, leído en la imagen |
| Efecto en el PIB por persona | Informe, gráfico 26, leído en la imagen |
| 75.5 %, 43 %, más de 83 %; valores por sexo y quintil | Informe, p. 17, gráfico 4 |
| Pobreza por edad | Informe, gráfico 3 |
| 8.9 % en salud | Informe, p. 27 |
| Corea: fechas, TGF 0.73, recorte de 2024 | Informe, pp. 53–57 |
| 45.1 a 59.7 %; 36.7 a 42.5 % | Informe, recuadro 4 |
| Perfil fijo por población, diapositiva 8 | Cálculo con ntaccounts.org y WPP 2024, `datos/prep_p3.py` |
| Salud por edad, México 2014 | ntaccounts.org |
| Mujeres de 45–64 por 80+: 6.0 a 2.6; 5.7 a 2.1 | WPP 2024; motor nacional |
| Máximo de México hacia 2040 | Cálculo con ntaccounts.org: 2039 y 2042 con WPP, 2040 y 2042 con el motor |
| 3.150 %, 2023–2030 | LSS, art. 168; `clase03_incidencia.tex` |
| 1.84 billones, 4.7 % del PIB | `FISCUS/.../documento_2027/capitulos/07_pensiones.tex` |
| 2.7 % y 41 %; 4.1 % y 30 % | OMS GHED 2023, tomado de `boston_20260828_v2.tex` |
| 23.9 %, 72.6 % | INEGI, reporte 48/25 (`fuentes/INEGI_CSTNRHM2024_RR.pdf`), cifras preliminares |
| Retiro del cuidado después del retiro laboral | Manual NTTA (2024) (`fuentes/UN_2024_NTTA_Manual.pdf`) |

### Lo que quité o no pude verificar

- **Escenarios fiscales del informe.** No existen. La diapositiva 16 no los usa y lo dice en pantalla.
- **Textos del DOF.** No pude abrir dof.gob.mx: falló su certificado. Las fechas de 2020 y 2024 del art. 4 (DOF 8-05-2020, 68 años; DOF 2-12-2024, 65 años) y del Fondo (DOF 1-05-2024) las verifiqué con la síntesis de la SCJN, notas legislativas y la ASF.
- **Gasto público en salud de 2.6 % (presentación de mayo).** Uso 2.7 %, la cifra de GHED 2023 del deck de Boston. No volví a consultar GHED.
- **Monto de la pensión no contributiva y Pensión Mujeres Bienestar.** Fuera: las fuentes se contradicen.
- **Punto de México en el gráfico 6.** El informe no da valor; no lo cito.
- **Martinica, 15 puntos de Chile, nota 6 y «6 países».** Erratas del informe; no se repiten.

### Archivos de Dalila usados

| Archivo | Respaldo |
|---|---|
| `Missions/Funded/CAF_DEM/caf-dem-entregable-final/main.tex` | No es entrada de corpus |
| `FISCUS/económicos_paquetes/documento_2027/capitulos/07_pensiones.tex` | No es entrada de corpus |
| `Comunidad_conocimiento_financiamientosalud_LATAM/Roche/boston_20260828/boston_20260828_v2.tex` | No es entrada de corpus |
| Presentación para la CEPAL | No es entrada de corpus |
| `Missions/Funded/NTA_Inequality/` | Sin respaldo; trabajo en curso |
| `GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa/` | Sin respaldo; producto de comunicación |

La Parte 3 no usa entradas de corpus.

### Desviaciones del esquema aprobado

1. **Diapositiva 8.** El esquema proponía una gráfica con el perfil de la Parte 2. Va una tabla calculada: perfiles fijos por población, 2024 y 2050. Es nuestra, no del informe, y lleva el rótulo «aritmética, no pronóstico».
2. **Diapositiva 12.** Agregué el perfil real de salud de México 2014.
3. **Diapositiva 14.** Agregué mujeres de 45–64 por persona de 80+, cálculo propio.
4. **Diapositiva 19.** Agregué el máximo de la razón de sostenimiento de México, hacia 2040. Replicado en cinco países del informe, el método cae a 2–4 años de sus fechas: es orden de magnitud. Sin revisión de terceros.
5. **Diapositiva 7.** Muestra 10 de los 16 países, por espacio.
6. **Diapositiva 11.** El entregable CAF fecha el Fondo el 30 de abril de 2024. Ese día salió la reforma de leyes; el decreto del Fondo es del 1 de mayo. Conviene corregir CAF_DEM si se reutiliza.

## Versión 2 · 2 de noviembre de 2026

Héctor pidió que las tres presentaciones reflejen su voz, sus ideas y sus años de trabajo. La tabla de la Parte 3 de arriba queda superada: ahora son 25 diapositivas.

### Criterio de lenguaje

En los textos que son seguro suyos (columna de *Nexos*, «Contabilidad de la Muerte») escribe oraciones completas, explicativas y moderadas. Lo telegráfico de la versión 1 venía de seguir «frases cortas» de este encargo. La versión 2 prefiere la oración completa, la cifra con punto de comparación y el desacuerdo que concede antes de objetar.

### Cambios

| Parte | Cambio | Fuente |
|---|---|---|
| 1 | Thompson (1929), quinta fase y tesis del reacomodo por edades | Nexos (2025) |
| 1 | Nueva, diapositiva 11: «Llevamos más de diez años haciéndonos esta pregunta» | Cantú, Ramones y Villarreal (2016); Villarreal y Macías (2020); CEPAL 2022, 2025 y 2026 |
| 1 | Nueva, diapositiva 13: «¿Una sexta fase?» | Borrador «Cohort Replacement, Not Cascade»; Fernández-Villaverde y Norrick (2026) |
| 1 | Pilares con su juicio de 2022 | CEPAL (2022) |
| 2 | Cierre: gobierno mediador entre generaciones; propuesta de cuentas generacionales y NTA en las cuentas nacionales | Resumen ejecutivo NTA; CEPAL 2022 y 2025 |
| 2 | Mujeres de 60 y más: 24.0 % menos en transferencias públicas netas | `paper_final.tex` |
| 3 | Reescrita; gráficas de 65+, razón de dependencia, un hijo por mujer, bolsillo por edad y salto de 2020 | Motor nacional; escenario LAC; BID2/motivation |
| 3 | Nueva, diapositiva 13: quién paga, solo en el PDF de exposición | BID2, Draft-October |
| 3 | Nueva, diapositiva 20: «competencia mayúscula» y Bolsa de 4.0 % del PIB | CEPAL 2022 y 2025; SobreMéxico 2026 |
| 3 | Diapositiva 19: cuenta ilustrativa de México, +3.4 a +10.1 puntos del PIB | CGPE 2027, OMS, ntaccounts.org, motor nacional |

**Opcionales de la Parte 3:** 8 (2 min), 11 (3), 22 (3) y 23 (3). Suman 11 minutos. El total da unos 62 minutos.
**Opcionales de la Parte 1:** 6, 15 y 20, sin cambio. Las Partes 1 y 3 quedan algo arriba de 60 minutos.

### Restricciones de uso

- **CAF:** el reporte es de circulación restringida y la misión dice «No divulgar». Se retiró de pantalla y de los PDF el recuadro de la versión 1 y la gráfica de presión. La versión 1, ya subida en 6c6fb3a, sí citaba ese documento en un recuadro.
- **BID2, Draft-October:** dice «do not cite or circulate» y tiene tres coautores más. Va en el PDF de exposición, no en el de repartir (`<handout:0>`).
- **«Cohort Replacement, Not Cascade»:** dice «not for circulation». Va en ambos PDF porque Héctor, autor único, lo autorizó el 2 de noviembre.
- **IMSS N13:** no se usó: es preliminar y con insumos del IMSS.
- **Sexta fase:** es hipótesis de Héctor y va como pregunta. El borrador habla de compresión de la segunda transición.

### No verificado o abierto

- 34 y 21.7, 9 y 4 % del PIB: tomados de la lámina de 2025; no se volvió a la OCDE.
- CIEP, pensiones arriba de 40 % de los ingresos tributarios: solo en nota, tomado de la columna.
- Villarreal y Macías (2020): título y resumen por búsqueda web; cepal.org devolvió 403.
- La versión en español de *Nexos* está tras muro de pago; se leyó la inglesa.
- Reforma del borrador: trata a México como comparador lento (1.60); hay que revisarlo con la EIC 2025.
- Tres fuentes de la Parte 1 siguen sin respaldo formal; la Nota EIC sigue pendiente de firma.
- Errata en la columna: la nota 1 dice «Warren, T.»; es Thompson, W. S. (1929).

---
mission: CAF_DEM
producto: P4
tipo: instrucciones-claude-code
alcance: documento completo + secciones nuevas + apéndices
autor: Beth (dirección analítica) y Cath (soporte fiscal-macro) — BDH Core Team
revisor: Juan Pablo López Reynosa
fecha: 2026-09-16
entrega_contractual: 22 de octubre de 2026
---

# CAF_DEM · Producto 4 — Instrucciones de trabajo

> **Nota para Juan Pablo (revisor).** Este documento tiene dos lectores. Claude Code lo ejecuta; tú lo revisas. Por eso cada bloque explica *por qué* se hace algo antes de decir *qué* hacer. Si algo aquí contradice tu criterio técnico, la instrucción no es obligatoria: repórtalo a Héctor antes de ejecutarlo. Hay tres decisiones marcadas como **⚠ DESVIACIÓN** que se apartan de lo aprobado en P1 y que están señaladas deliberadamente para que las veas, no para que pasen inadvertidas.

---

## 0. Qué pide el contrato

Producto 4, plazo 22 de octubre de 2026, seis meses desde la firma:

> *Versión integral revisada del documento, que incluye un análisis heurístico de riesgos macrofiscales, considerando espacio fiscal y transición demográfica. Se incluirá un breve apéndice teórico sobre efectos de equilibrio general respecto a gasto público en pensiones y salud, impactos demográficos y sostenibilidad fiscal.*

Tres componentes, en este orden de prioridad: (1) revisión integral, (2) análisis heurístico de riesgos, (3) apéndice de equilibrio general **breve**.

La palabra "breve" del contrato es vinculante para el apéndice. Objetivo: 5 a 7 páginas. Si crece más allá de eso, se recorta.

## 0.1 Insumos disponibles

| Archivo | Qué es | Para qué |
|---|---|---|
| `main.tex` | Documento P3 entregado, secciones 1–5 | Base de trabajo |
| `graficas/` (12 png), `tablas/` (7 tex) | Salidas del pipeline | Se conservan; algunas se regeneran |
| `FISCAL_DEMO_v4_1_.html` | R Markdown tejido completo de la Sección 5 | **Pipeline reproducible**; contiene el anexo de quiebres estructurales |
| `base_analisis_P3.csv` | 1,745 filas · 6 países · 7 indicadores · 1990–2050 | Fuente única para todo cálculo nuevo |
| `base_analisis_P3_diccionario.csv` | Diccionario + advertencia de uso | Documentación de la base |
| `IADB_SpendingSmarter-1.pdf` | Paper OLG del BID, 74 pp, 31 ago 2026 | Base del Apéndice A |
| `Slides_Latam.pdf` | Fernández-Villaverde, 15 sep 2026 | Base de §6.4 |
| `(In)Formalizing Jobs in LAC` (World Bank 2025) | Fietz et al. | Marco FTR, ya citado |

**No están disponibles** los `.xlsx` crudos (`WEO_Gobierno_balance.xlsx`, `IMF_Pensiones_salud.xlsx`, `demografia_LIMPIA.xlsx`). No hacen falta: `base_analisis_P3.csv` es la base consolidada y es suficiente para todo lo que este documento pide.

## 0.2 Restricciones que no se negocian

1. **Propiedad intelectual de CAF** (Anexo A, CW29884). No deben quedar comentarios LaTeX de deliberación interna en el archivo entregado. Barrer al final.
2. **Fietz et al. (2025) siempre parafraseado**, nunca citado textualmente.
3. **El paper del BID es propiedad del BID con licencia de uso.** Se cita como fuente externa con su nota de copyright. No se incorpora como material propio ni se reproducen sus tablas; se describen sus resultados y se reproduce su identidad de cierre PAYG, que es notación estándar.
4. **Ningún número inventado.** Si un dato no está en `base_analisis_P3.csv`, en el `.tex` actual o en una fuente citada, **se reporta como pendiente, no se completa.** Esta regla anula cualquier otra instrucción de este documento.
5. **Ningún cálculo sin su supuesto escrito al lado.** Todo lo que se compute en el Bloque C lleva el supuesto en el texto visible, no en una nota al pie.

---

## 1. Preparación

```bash
cd ~/Dalila/Missions/Funded/CAF_DEM/
git checkout -b p4-version-final
```

Diagnóstico inicial — reportar resultados antes de editar nada:

```bash
grep -n "VERIFICAR\|\\\\VER{" main.tex
grep -n "^%" main.tex | grep -viE "^[0-9]+:% =|^[0-9]+:% -"
grep -noP "Secci[oó]n[~ ]*[0-9][0-9.]*" main.tex      # refs escritas a mano
grep -c "citep{" main.tex
```

Extraer el código R del `.html` tejido a un `.Rmd` o `.R` reutilizable:

```bash
# El HTML es knitr output; los bloques de código están en <pre class="r">
python3 -c "
from bs4 import BeautifulSoup
s=BeautifulSoup(open('FISCAL_DEMO_v4_1_.html',encoding='utf-8').read(),'html.parser')
bloques=[p.get_text() for p in s.find_all('pre') if 'r' in (p.get('class') or [])]
open('pipeline_P3_extraido.R','w',encoding='utf-8').write('\n\n'.join(bloques))
print(len(bloques),'bloques extraídos')
"
```

Verificar que R y las librerías estén disponibles (`readxl`, `tidyverse`, `forecast`, `tseries`, `strucchange`, `knitr`). **Si R no está disponible en el entorno, detenerse y reportar** — el Bloque B depende de ello. Los Bloques A, C (parcial), D–H se pueden hacer sin R.

---

## 2. BLOQUE A — Revisión general del documento existente

Pendientes heredados del P3. Todos son de `.tex`.

### A.1 Nota (a) huérfana en la Tabla 8
Al eliminarse la columna "Cobertura contributiva (PEA)" en el P3, el superíndice `(a)` se reubicó sobre el valor 81.0 de Brasil en *Cob. 65+ contributiva*, pero el texto de la nota sigue abriendo con *"la cobertura contributiva de la PEA activa no se reporta en las bases utilizadas"* — que describía la columna eliminada. Un lector ve una nota que no corresponde a la celda marcada.

Eliminar esa primera oración. La nota debe empezar en *"El RGPS es de afiliación obligatoria…"*, que sí explica el 81.0.

### A.2 `Bases de datos` y `Fuentes normativas` quedaron huérfanas
Están como `\subsection*` después de `\end{thebibliography}`, lo que las convierte en subsecciones de la Sección 5 y las deja fuera del índice. Convertir a `\section*` con `\addcontentsline{toc}{section}{...}`, o moverlas antes del entorno de bibliografía.

### A.3 Enlazar las citas al cuerpo
Sólo hay un `\citep` en todo el documento (`wb2025`). Holzmann y Hinz (2005), Hyndman y Athanasopoulos (2021), CEPAL (2020) y Bai y Perron (2003) se mencionan en texto plano. Con `natbib` ya cargado, convertir a `\citep{}` / `\citet{}` según corresponda. Añadir las entradas nuevas de P4 (ver Bloque H).

### A.4 Marco fiscal brasileño (§4.2.2)
Quedó en redacción segura, sin nombrar el instrumento que sustituyó el techo de gasto de la EC 95/2016 en 2023. **Verificar el instrumento y su denominación antes de escribirlo.** Si no se puede verificar con certeza, dejar la redacción actual.

### A.5 Cosméticos
- Panel A de la Tabla 9: el encabezado "Gasto de bolsillo" parte con hueco visible; alinear las cifras por decimal (`siunitx` con `S[table-format=2.2]` o `dcolumn`).
- `\hbox` desbordado de 42 pt en la Tabla 7 (`SAR/AFORE/PENSIONISSSTE`). Preexistente. Insertar `\-` o `\allowbreak` en la cadena.

### A.6 Coherencia de producto
Barrer `P3` → `P4` en encabezado corrido, portada, `pdftitle`, `pdfauthor`, nota de alcance y fecha de entrega. Reescribir la nota de alcance para que describa el documento **integral**, no la versión intermedia. Igualmente §1.2 y §1.4: ahora el documento tiene ocho secciones y dos apéndices.

---

## 3. BLOQUE B — Corrección de las proyecciones

> **Para Juan Pablo.** Este bloque existe gracias a tu control de rango automatizado. La alerta que programaste detecta las tres series problemáticas por sí sola, y la ADVERTENCIA DE USO del diccionario documenta la causa correctamente: la ventana de validación contiene el choque de 2020 y eso sesga la selección hacia tendencia no amortiguada. En P3 esto se neutralizó con texto porque no había acceso al pipeline. Ahora sí lo hay, y la corrección de fondo es preferible a la advertencia.

### B.1 Re-estimar con ventana de validación que excluya 2020
Para las series de gasto funcional (salud y pensiones, CEPAL/FMI-GFS), reejecutar la selección de modelo con una de estas dos opciones, la que produzca diagnósticos más limpios:

- **Opción 1:** ventana de validación de los últimos cuatro años **anteriores a 2020**.
- **Opción 2:** mantener la ventana pero restringir el conjunto de especificaciones a las amortiguadas (Holt damped, ETS con `damped=TRUE`), que impiden la extrapolación lineal indefinida.

Las tres series que deben cambiar: gasto en salud de Chile (hoy 6.03 → 12.38), gasto en pensiones de México (3.01 → 5.30), gasto en salud de México (1.24 → 1.65).

**Criterio de aceptación:** el control de rango del propio pipeline debe dejar de disparar alerta. Si sigue disparando después de ambas opciones, **no forzar** — conservar la proyección y la advertencia textual, y reportarlo.

### B.2 Podar las series no informativas
Criterio: MASE > 2 respecto del método ingenuo de persistencia. Con los valores actuales caen:

| Figura | Paneles afectados |
|---|---|
| Ingresos | Costa Rica (2.89), Chile (2.24) |
| Balance primario | Costa Rica (5.59), Brasil (4.23), Panamá (3.26), Chile (2.37) |
| Deuda neta | Costa Rica (7.38, RMSE 36.6 pp del PIB sobre n=14) |
| Salud | Chile (2.64), Colombia (2.28) |
| Pensiones | ninguno |

**Decisión sobre el balance primario:** con cuatro de seis paneles caídos, la figura no se sostiene mutilada. Eliminar la Figura 9 completa y sustituirla por dos o tres oraciones que expliquen por qué: el balance primario es la única de las cinco series estacionaria o próxima a serlo, revierte a la media alrededor de cero por su naturaleza de flujo, y la extrapolación univariada no aporta información más allá de esa media. Sale más fuerte que una figura incompleta.

Las demás series podadas se retiran de su panel pero **se conservan en la Tabla 13** con marca explícita de no informativas.

### B.3 Sincronía obligatoria
Cualquier cambio de modelo obliga a regenerar **en el mismo pase**: la figura, la fila correspondiente de `tablas/tab_modelos.tex` (RMSE, MASE, Ljung-Box), `tablas/tab_frecuencia_modelos.tex`, y las filas de `tipo = "Proyección propia"` de `base_analisis_P3.csv`. Una figura actualizada con tabla vieja es peor que no corregir nada.

Si `base_analisis_P3.csv` cambia, **actualizar también la ADVERTENCIA DE USO del diccionario** para que refleje el estado nuevo. Renombrar ambos a `base_analisis_P4.csv` / `base_analisis_P4_diccionario.csv` y conservar los de P3 sin tocar, como provenance.

---

## 4. BLOQUE C — Sección 6: Análisis heurístico de riesgos macrofiscales

Es el corazón del entregable. Estructura en seis subsecciones.

> **⚠ DESVIACIÓN 1 respecto de P1.** El índice aprobado preveía un *Apéndice B: Fichas-país*. Se propone eliminarlo: la Sección 3.1 ya contiene fichas institucionales por país mucho más profundas de lo que P1 anticipaba, y §6.5 aporta la ficha de riesgo. Un tercer bloque país-por-país sería repetición. El Apéndice B pasa a ser el anexo técnico (Bloque G). **Héctor debe confirmar esta decisión antes de la entrega.**

### 6.1 Marco del análisis

Qué se entiende aquí por riesgo macrofiscal demográfico y por qué el análisis es **heurístico** y no actuarial: no se proyecta sistema por sistema con reglas paramétricas y cohortes, sino que se ordena la exposición relativa de los seis países combinando tres dimensiones ya documentadas — arquitectura institucional (Secciones 3 y 4), presión demográfica (Sección 5) y espacio fiscal (Sección 5). Decir explícitamente que el resultado es un **ordenamiento comparado**, no una cuantificación de pasivos.

Conectar con el eje BDH: la pregunta de si el componente no contributivo es complemento o sustituto (§3.2) determina por qué canal la demografía se convierte en riesgo fiscal, vía erosión de la base contributiva. Parafrasear a Fietz et al. (2025), no citar.

### 6.2 Espacio fiscal: la métrica

**Métrica principal: brecha de balance primario estabilizador de deuda.**

```
pb* = b · (r − g) / (1 + g)
brecha = pb* − pb_observado
```

donde `b` es deuda neta / PIB (2024), `pb_observado` el balance primario 2024, y `(r − g)` el diferencial entre tasa de interés implícita y crecimiento nominal del PIB.

**Problema: `base_analisis_P3.csv` no contiene ni crecimiento del PIB ni tasa implícita.** Dos rutas, en orden de preferencia:

- **Ruta A (preferida).** Traer dos series del FMI-WEO abril 2025 — crecimiento del PIB nominal y, si está disponible, gasto en intereses / deuda para la tasa implícita. Son series públicas de descarga directa. Al incorporarlas, **añadirlas a la base con su `tipo`, `fuente` y `cobertura_institucional`** siguiendo el esquema del diccionario, no como cálculo suelto.
- **Ruta B (respaldo).** Despejar un `(r − g)` implícito de la propia identidad de acumulación de deuda con las series que ya están en la base, promediando sobre 2015–2024 para amortiguar el ruido. Absorbe el ajuste stock-flujo; **etiquetarlo explícitamente como implícito** y advertir que incluye ese residuo.

Si se usa la Ruta B, decirlo en el texto visible, no en nota al pie.

Presentar como tabla de seis filas: país · `b` 2024 · `pb` 2024 · `(r−g)` · `pb*` · brecha. Ordenar por brecha descendente.

**Advertencia obligatoria en la nota de la tabla:** el documento usa deuda **neta**; la comparación internacional de `b` es menos directa que con deuda bruta por la heterogeneidad en la valuación de activos (ya justificado en §5.2). Y las cifras de 2024 son estimación del FMI en Brasil, Costa Rica y Panamá, y observadas en Chile, Colombia y México.

### 6.3 Presión demográfica sobre pensiones y salud

**Incremento mecánico del gasto por cambio en la estructura por edades**, a costo por edad constante.

Para **pensiones**, la elasticidad unitaria respecto de la razón de dependencia está justificada teóricamente por la identidad de cierre PAYG que se desarrolla en el Apéndice A: la tasa de contribución de equilibrio es la tasa de reemplazo escalada por la razón de dependencia del sistema. Por tanto:

```
Δgasto_pensiones = gasto_2024 × (RD_2050 / RD_2025 − 1)
```

Con los valores de la base (`RD_2050/RD_2025`): Brasil 2.16, Chile 2.03, Colombia 2.17, Costa Rica 2.20, México 2.04, Panamá 2.00.

Para **salud** la elasticidad unitaria **no** es defendible: el gasto en salud recae sobre toda la población, no sólo sobre los mayores de 65. Sin perfiles de gasto por edad para los seis países —que el documento reconoce como pendiente en §4.3.1— la única opción honesta es presentar una **banda ilustrativa** con dos elasticidades explícitas (por ejemplo 0.5 y 1.0) y decir en el texto que la banda es ilustrativa y que su estrechamiento requiere cuentas de salud por grupo etario o perfiles NTA.

**No presentar un punto central de salud como si fuera estimación.** Banda, siempre.

Cerrar con la pregunta que da sentido a la sección: **qué fracción de la brecha de §6.2 absorbe este incremento demográfico.** Ese cociente es el número comparable entre los seis países y es el lenguaje que la DEM lee sin fricción.

**Advertencias:** las series de gasto funcional son de cobertura de gobierno central y subestiman el gasto efectivo en Costa Rica y Panamá, donde CCSS y CSS operan fuera del perímetro (ya documentado en la reconciliación de §5.2.2). Remitir a ella explícitamente. El ejercicio compara *destinos*, no trayectos: es estática comparada, no una senda.

### 6.4 La calidad del insumo demográfico

> **⚠ DESVIACIÓN 2 respecto de P3.** El documento declara en §5.1 que no ajusta modelo propio sobre las series de UN WPP porque remodelarlas sería redundante y metodológicamente inferior al insumo original. Esta subsección **no revierte** esa decisión —el WPP sigue siendo la base del documento— pero introduce una discusión sobre su sesgo que hasta ahora no existía. Es una decisión tomada por Héctor el 16 de septiembre de 2026.

Fuente: Jesús Fernández-Villaverde (University of Pennsylvania, NBER, CEPR), *A Recent Population History of Latin America and the Caribbean*, presentación del 15 de septiembre de 2026.

**Atribución.** Citar la presentación de forma explícita, con autor, título, institución y fecha, señalando que es material de presentación. **Y además** anclar cada cifra concreta en el registro vital nacional del que procede, de modo que el argumento se sostenga aunque el lector no tenga acceso al material. Si Héctor prefiere no citar material no publicado, la sección debe poder reescribirse apoyándose sólo en los registros vitales.

**Qué desarrollar, en cuatro movimientos:**

1. **La discrepancia.** El WPP estima nacimientos por encima de los registros vitales oficiales incluso donde el propio sistema de Naciones Unidas califica la cobertura de registro como superior al 90%. El caso documentado: Colombia 2023, registro de 515,549 nacimientos frente a una estimación de 705,000, un exceso del 37%. Las proyecciones descansan además en un supuesto de reversión a la media que produce un rebote de la fecundidad con independencia de la velocidad de la caída observada.

2. **La magnitud para nuestra muestra.** La Tabla 1 del documento reporta, de WPP, una TFR de 1.63 para Colombia y 1.14 para Chile. Los registros vitales dan, para 2025, 1.01 y 0.99 respectivamente. Es una diferencia de orden, no de decimales. **Presentar como tabla de contraste**, no como afirmación en prosa.

3. **La dirección del sesgo es unívoca.** Es lo más importante de la subsección. Todos los errores identificados apuntan en el mismo sentido: sobreestimar nacimientos y fecundidad futura, y por tanto **subestimar** la velocidad del envejecimiento. No hay un caso simétrico en que el WPP subestime. En consecuencia, las razones de dependencia senil de la Tabla 1 y todo el análisis de §6.2 y §6.3 construido sobre ellas deben leerse como **cota inferior del riesgo**.

4. **La implicación para el Apéndice A.** Por la identidad de cierre PAYG, la tasa de contribución de equilibrio escala con la razón de dependencia del sistema. Si el denominador demográfico está sesgado a la baja, la tasa de contribución de equilibrio bajo demografía 2050 es **mayor** que la que reporta el ejercicio del BID. Una o dos oraciones; el desarrollo va en el apéndice.

**Tono.** Esto no es una objeción al WPP como fuente ni una recomendación de abandonarlo: el documento lo sigue usando y explica por qué. Es una calificación sobre la dirección del error. Escribirlo con esa moderación — es lo que lo hace citable por la DEM en lugar de polémico.

### 6.5 Reporte de riesgo por país

Seis fichas breves, una a dos páginas cada una, **construidas exclusivamente con información ya compilada en las Secciones 2 a 5 y en §6.2–6.4**. No se introduce dato nuevo aquí.

Estructura fija e idéntica para los seis, para que sean comparables:

1. **Posición demográfica** — RD senil 2025 y 2050, TFR, etapa de transición (Sección 2 y Tabla 1)
2. **Arquitectura y exposición** — qué pilares tiene, dónde está el pasivo fiscal, si hay Pilar 1-B (Sección 3)
3. **Salud** — composición del financiamiento, gasto de bolsillo, segmentación (Sección 4)
4. **Espacio fiscal** — deuda neta, balance primario, brecha de §6.2 (Sección 5)
5. **Vector de riesgo dominante** — la oración que sintetiza por dónde se materializa el riesgo en ese país
6. **Señal de alerta temprana** — qué indicador observable movería el diagnóstico

El punto 5 es el que da valor. Debe ser **específico y distinto entre países**, no una plantilla rellenada. Orientación, a contrastar con los datos:

- **Brasil** — el mayor gasto en pensiones de la muestra (8.83% del PIB), reparto puro sin Pilar 2, cobertura contributiva de 65+ del 81%, recaudación alta (38.8%) pero deuda neta la más alta (61.5%). El riesgo es de rigidez presupuestaria, no de cobertura.
- **Chile** — transición más avanzada (RD 21.2 hoy, 43.1 en 2050), deuda neta más baja (25.8%), pero gasto en salud que ya representa 20.7% del gasto público y la PGU cumpliendo dos funciones a la vez. El riesgo migró de pensiones a salud.
- **Colombia** — deterioro fiscal agudo en 2024 (ingresos −4.0 pp, deuda +5.1 pp), arquitectura pensional en suspensión constitucional (Ley 2381), informalidad 56%. El riesgo es de incertidumbre institucional sobre un punto de partida que se debilita.
- **Costa Rica** — integración CCSS, deuda neta 58.9%, recaudación 15.1%, la mayor brecha de género contributiva (+23.1 pp), y la mayor aceleración demográfica proyectada (factor 2.20). El riesgo es de estrechez recaudatoria frente a presión acelerada.
- **México** — bono demográfico más amplio (RD 12.6), pero gasto público en salud más bajo (2.68% del PIB), bolsillo elevado, y expansión no contributiva de rango constitucional. El riesgo es de sustitución contributivo→no contributivo, el caso más nítido de la muestra.
- **Panamá** — el deterioro fiscal más pronunciado de 2024 (balance primario −4.5%, deuda +5.8 pp), reforma de 2025 recién aprobada, recaudación 15.5%. El riesgo es paramétrico e inmediato, no demográfico agregado.

### 6.6 Síntesis comparada

Ordenamiento de los seis países por exposición. **Evitar el índice sintético compuesto** — agrega dimensiones heterogéneas con ponderaciones arbitrarias y es lo primero que un lector de la DEM cuestiona. En su lugar: un ordenamiento por cada dimensión (presión demográfica, espacio fiscal, rigidez institucional) y una lectura de dónde coinciden y dónde divergen. Los casos interesantes son los de divergencia.

Cerrar recordando que todo el ordenamiento es cota inferior, por §6.4.

---

## 5. BLOQUE D — Sección 7: Consideraciones de política

Tres a cinco páginas. **No es una lista de recomendaciones** — el contrato pide una nota técnica, no un documento de incidencia, y el paper del BID ya demuestra que los márgenes de reforma difieren mucho menos en bienestar que en incidencia.

Organizar alrededor de los márgenes que la identidad PAYG deja abiertos: tasa de contribución, tasa de reemplazo, y frontera entre contribuyentes y beneficiarios. Para cada uno: qué países tienen ese margen disponible según su arquitectura (Sección 3), y qué implicaciones de incidencia tiene (Apéndice A).

Añadir dos consideraciones que salen del eje BDH y no de la identidad:

- **El diseño del componente no contributivo determina el canal de riesgo.** Donde el Pilar 0 opera como sustituto, la reforma paramétrica del pilar contributivo no resuelve el problema fiscal: lo desplaza.
- **La credibilidad institucional es carga estructural.** Sin ella, el rediseño paramétrico no mejora los incentivos de formalización. Parafrasear a Fietz et al.

Cerrar con la restricción temporal: la región tiene aproximadamente una cuarta parte del tiempo que tuvo Europa para el mismo ajuste, y el punto de partida fiscal de 2024 se está debilitando precisamente durante la ventana en que sería más favorable fortalecerlo (dato ya en §5.2.1).

---

## 6. BLOQUE E — Sección 8: Conclusiones

Dos a tres páginas. Sin números nuevos. Sin recomendaciones nuevas. Recapitulación de los tres ejes analíticos aprobados en P1 (arquitectura institucional, presión demográfica diferenciada, espacio fiscal) a la luz de lo que el documento encontró.

Debe incluir, sin adornos, las tres limitaciones: cobertura de gobierno central en el gasto funcional, proyecciones univariadas sin determinante demográfico, y el sesgo direccional del insumo demográfico.

---

## 7. BLOQUE F — Apéndice A: Efectos de equilibrio general

**Límite duro: 5 a 7 páginas.** El contrato dice "breve".

Fuente: *Spending Smarter* (Banco Interamericano de Desarrollo, 2026), OLG estocástico estimado para México. Citar con su nota de copyright del BID.

### Qué debe contener

**A.1 Por qué hace falta.** Las Secciones 3 a 6 son equilibrio parcial: toman precios, salarios y retornos como dados y suman gasto. El equilibrio general dice qué se mueve cuando la demografía cambia — y lo que se mueve altera el resultado en dirección no obvia.

**A.2 La estructura mínima.** Economía OLG con salud como capital endógeno que eleva supervivencia, productividad y el valor que los hogares dan al consumo. Agentes diferenciados por sexo y educación, cada tipo con sus propios perfiles medidos de eficiencia y supervivencia. Precios de los factores y tasa de contribución se determinan en equilibrio.

**A.3 La identidad de cierre.** Es el puente con el resto del documento y debe escribirse explícitamente:

```
τᵖ = κ · (Nᴿ / Nᵂ)
```

La tasa de contribución de equilibrio es la tasa de reemplazo escalada por la razón de dependencia del sistema. **Este es el mecanismo por el que la presión demográfica llega a los hogares como cuña sobre el trabajo formal** — y por tanto el vínculo directo con el eje de formalización de §3.2 y con la Sección 6 completa.

**A.4 El resultado central.** Bajo demografía de 2050 y política sin cambio, la tasa de contribución más que se duplica, de 5.66 a 12.26 por ciento, y sin embargo un recién nacido queda prácticamente igual de bien. La razón es la profundización del capital: el menor crecimiento poblacional inclina la distribución por edades hacia hogares mayores y con más activos, el retorno cae y el salario sube, y para quien llega sin nada esas ganancias casi pagan la cuña duplicada.

**El punto que ninguna contabilidad de equilibrio parcial produce:** el envejecimiento bajo política sin cambio **redistribuye más que empobrece**. El costo recae sobre quienes ya tienen activos, y crece marcadamente con la edad.

**A.5 El menú de reforma.** Los tres márgenes y su incidencia. Frente a la inacción, el recorte de beneficios vale más que el retiro más tardío para un recién nacido, y todos los tipos ordenan igual; el orden se invierte con la edad. Los márgenes difieren mucho menos en el bienestar que entregan que en de quién es la vejez que paga.

**A.6 Qualification.** Obligatoria, sin suavizar: son equilibrios estacionarios. Los números valoran **destinos**, no los trayectos entre ellos, y las generaciones de transición de cualquier reforma no están modeladas. Añadir la limitación que el propio paper reconoce sobre el canal de inversión endógena en salud.

**A.7 Vínculo con §6.4.** Dos o tres oraciones. Si el insumo demográfico subestima Nᴿ/Nᵂ, la tasa de contribución de equilibrio bajo demografía 2050 es mayor que la reportada. El resultado del apéndice hereda la misma asimetría que el análisis de riesgo: es cota inferior.

### Qué NO debe contener

- Derivación completa del modelo, condiciones de primer orden, o el problema de optimización del hogar. Remitir al paper.
- Reproducción de tablas del BID.
- Extensión de los resultados de México a los otros cinco países. **El paper está estimado para México.** Se puede decir que la identidad de cierre es general y que el mecanismo de profundización de capital opera en cualquier economía que envejece, pero las magnitudes son mexicanas y deben presentarse como tales.

---

## 8. BLOQUE G — Apéndice B: Anexo técnico

> **⚠ DESVIACIÓN 3 respecto de P1.** Sustituye al *Apéndice B: Fichas-país* previsto. Ver justificación en el Bloque C.

Material ya computado, hoy en el `.html` tejido y explícitamente reservado allí como insumo para el Producto 4. Se recupera sin recomputar salvo que el Bloque B haya cambiado las series.

**B.1 Quiebres estructurales.** Prueba supF de Quandt-Andrews y procedimiento de Bai-Perron sobre las treinta series fiscales. Incluir las figuras `anexo_quiebres_*.png` y la tabla de fechas de quiebre. Explicar brevemente el marco (el estadístico F evalúa en cada punto candidato si partir la muestra mejora el ajuste; Bai-Perron identifica número y ubicación óptimos por BIC) y por qué se mantuvo fuera del cuerpo.

**Valor añadido para P4:** las fechas de quiebre detectadas dan contenido empírico a la advertencia sobre estabilidad paramétrica de §5.3.3, que hasta ahora era una afirmación cualitativa.

**B.2 Diccionario de la base.** Reproducir `base_analisis_P4_diccionario.csv` como tabla, incluida la advertencia de uso actualizada. Es el respaldo de auditoría de todo el análisis cuantitativo y conviene que esté dentro del documento entregado a CAF.

---

## 9. BLOQUE H — Bibliografía, compilación y verificación

### H.1 Entradas nuevas
- Banco Interamericano de Desarrollo (2026), *Spending Smarter* — con nota de copyright del BID
- Fernández-Villaverde, J. (2026), presentación del 15 de septiembre, University of Pennsylvania / NBER / CEPR
- Registros vitales nacionales citados en §6.4 (DANE para Colombia, y los correspondientes)
- Cualquier fuente WEO adicional incorporada en §6.2

Mantener la separación en tres bloques ya establecida: bibliografía académica, bases de datos, fuentes normativas.

### H.2 Compilación
Compilar tres veces (referencias cruzadas, bibliografía, índice).

### H.3 Lista de verificación obligatoria sobre el PDF final

- [ ] Cero errores de compilación, cero referencias indefinidas, cero citas indefinidas
- [ ] `grep "VERIFICAR"` → cero
- [ ] `grep "^%"` → sólo separadores estructurales, ningún comentario de deliberación
- [ ] Encabezado, portada, `pdftitle`, fecha: todo dice P4
- [ ] Índice: ocho secciones y dos apéndices
- [ ] Toda referencia `Sección X.Y` resuelta vía `\ref`, ninguna escrita a mano
- [ ] Ningún número en §6 sin su supuesto explícito en texto visible
- [ ] Figuras, `tab_modelos.tex` y `base_analisis_P4.csv` mutuamente consistentes tras el Bloque B
- [ ] Ninguna tabla del BID reproducida
- [ ] Ninguna cita textual de Fietz et al.
- [ ] Las tres ⚠ DESVIACIÓN señaladas en el reporte final

### H.4 Git

```bash
git add -A
git commit -m "P4: versión integral — revisión general, análisis de riesgos macrofiscales, apéndices de EG y técnico"
git push -u origin p4-version-final
```

**No fusionar a `main` sin revisión de Héctor y de Juan Pablo.**

---

## 10. Reporte final requerido

Al terminar, entregar en markdown:

1. Bloques completados y bloques con incidencia.
2. **Las tres ⚠ DESVIACIÓN**, con su estado: aplicada, aplicada con modificación, o no aplicada.
3. Resultado del Bloque B: qué series se re-estimaron, con qué opción, si el control de rango dejó de disparar. **Si no se pudo ejecutar R, decirlo en la primera línea.**
4. Qué ruta se usó para `(r − g)` en §6.2 — A o B — y por qué.
5. **Cualquier dato que una instrucción pedía y no estaba disponible.** Reportarlo, no completarlo. Esta es la regla que anula todas las demás.
6. Cadenas no localizadas, referencias cruzadas rotas encontradas, y cualquier comentario de deliberación interna eliminado con su contenido, para registro.
7. Conteo de páginas y extensión del Apéndice A — si excede siete páginas, decirlo explícitamente.

---

## Anexo: orden de ejecución sugerido

| Prioridad | Bloque | Depende de |
|---|---|---|
| 1 | A — revisión general | — |
| 2 | B — corrección de proyecciones | R disponible |
| 3 | C.2, C.3 — métrica de espacio fiscal y presión demográfica | B (si cambian series), datos `(r−g)` |
| 4 | F — Apéndice A | — (independiente, se puede paralelizar) |
| 5 | C.4 — insumo demográfico | — |
| 6 | C.5, C.6 — fichas país y síntesis | C.2, C.3, C.4 |
| 7 | D, E — política y conclusiones | C completo |
| 8 | G — anexo técnico | B |
| 9 | H — bibliografía y verificación | todo |

Los Bloques A y F no dependen de nada y son los primeros que pueden avanzar. El Bloque C.5 depende de casi todo y es el último del cuerpo.

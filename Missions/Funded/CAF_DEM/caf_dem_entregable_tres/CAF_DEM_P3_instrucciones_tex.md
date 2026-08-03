---
mission: CAF_DEM
producto: P3
tipo: instrucciones-claude-code
alcance: solo-tex
autor: Beth (dirección analítica) y Cath (soporte fiscal-macro) — BDH Core Team
fecha: 2026-08-03
entrega_objetivo: miércoles 5 de agosto de 2026
---

# CAF_DEM · Producto 3 — Instrucciones de corrección (solo `.tex`)

## 0. Alcance y restricción dura

Este pase corrige **exclusivamente el archivo LaTeX**. Los scripts de R que generan las Figuras 1–12 y la Tabla 13 no están disponibles en esta ventana de trabajo.

**Restricción absoluta: no se regenera ninguna figura, no se modifica ningún valor numérico de las Tablas 10–13, y no se altera ningún archivo de imagen.** Todo el riesgo asociado a las proyecciones se neutraliza mediante texto, no mediante recorte de series.

Si alguna instrucción de este documento pareciera exigir un recálculo, **detente y repórtalo** en lugar de improvisar el número.

## 1. Preparación

1. Ubica el repositorio en `~/Dalila/Missions/CAF_DEM/`. Identifica el `.tex` principal (probablemente `main.tex`; confirma comparando con el índice del PDF `caf_dem_ptwo_v1.pdf`).
2. Crea rama de trabajo: `git checkout -b p3-correcciones-tex`.
3. **No dispones del `.tex` en este documento — sólo del PDF compilado.** Localiza cada cadena por búsqueda antes de editar. Usa `str_replace` con contexto suficiente para garantizar unicidad; no regeneres el archivo completo.
4. Antes de empezar, ejecuta un barrido de diagnóstico y reporta resultados:

```bash
grep -n "P2" main.tex | head -50
grep -n "VERIFICAR" main.tex
grep -n "Producto 2\|Producto 3\|Producto 4" main.tex
grep -n "^%" main.tex | grep -i "interna\|no mencionar\|discusión\|nota metodológica"
grep -n "Marina" main.tex
```

5. **Los dos últimos grep son de seguridad.** El traspaso documenta comentarios LaTeX de deliberación interna en el archivo (originalmente hacia las líneas 136-139, 406-407 y 661-662) y un crédito de autoría obsoleto. **Cualquier comentario de deliberación interna debe eliminarse: la propiedad intelectual del documento es de CAF.** El crédito a Marina González parece ya corregido en la portada del PDF, pero verifica que no persista en metadatos, `\author{}`, o comentarios.

---

## BLOQUE A — Identidad del documento (máxima prioridad)

El documento se presenta como P2 en todas partes salvo la palabra "PRODUCTO 3" de la portada. Es lo primero que verá el ERC.

### A.1 Encabezado corrido
Localiza la definición del encabezado (probablemente en `\fancyhead` o similar) con la cadena `P2 · CAF · CW29884`. Cámbiala a `P3 · CAF · CW29884`. **Afecta las 60 páginas; es un único punto de edición.**

### A.2 Portada
- Subtítulo actual: `Marco institucional y jurídico: sistemas de pensiones y financiamiento de salud`
- Sustituir por: `Versión intermedia: marco institucional, datos compilados y proyecciones fiscales`
- Fecha: `Fecha de entrega prevista: 30 de junio de 2026` → `Fecha de entrega: 5 de agosto de 2026`

### A.3 Nota de alcance (página 2)
Texto actual:
> Este documento desarrolla el marco institucional y jurídico de los sistemas de pensiones y de salud (secciones 1 a 4). Los marcadores en rojo señalan elementos que requieren verificación contra fuente primaria antes de la entrega oficial.

Sustituir íntegramente por:
> **Alcance.** Este documento corresponde al Producto 3 del contrato CW29884. Desarrolla el marco institucional y jurídico de los sistemas de pensiones y de salud (secciones 1 a 4) e incorpora la compilación estadística demográfica y fiscal comparada, con proyecciones inerciales de mediano plazo (sección 5). El análisis heurístico de riesgos macrofiscales, las consideraciones de política y el apéndice sobre efectos de equilibrio general corresponden al Producto 4.

**La segunda oración desaparece por completo.** Decirle a CAF que lo entregado requiere verificación posterior descalifica la entrega.

### A.4 Sección 1.2 — reescritura del párrafo de alcance
Párrafo actual (segundo de §1.2), que empieza `El Producto 2 cubre el marco institucional y jurídico…`. Sustituir por:

> El Producto 2 estableció el marco institucional y jurídico: qué reglas rigen hoy los sistemas de pensiones y salud en cada país, cómo se articulan los componentes contributivo y no contributivo, y qué cobertura efectiva producen. Este Producto 3 conserva y actualiza esa base institucional —necesaria para interpretar cualquier cifra— y añade la dimensión estadística: compilación y homologación de las series demográficas y fiscales de los seis países, su caracterización descriptiva y una proyección inercial de mediano plazo de los agregados fiscales. El Producto 4 incorporará, sobre esta base, el análisis heurístico de riesgos con su respectivo apéndice de equilibrio general.

### A.5 Sección 1.4 — estructura
Texto actual: `El documento se organiza en cuatro secciones.` → `El documento se organiza en cinco secciones.`

Al final de ese mismo párrafo, tras la oración sobre la Sección 4, añadir:

> La Sección 5 aporta la dimensión cuantitativa: documenta la trayectoria demográfica que define el marco poblacional de referencia, describe la posición fiscal de partida de los seis países y proyecta la evolución inercial de mediano plazo de los agregados fiscales relevantes.

---

## BLOQUE B — Contradicciones internas y referencias cruzadas

### B.1 §4.3.2 — contradicción crítica
Última oración de §4.3.2, actualmente:
> La proyección cuantitativa de este efecto, bajo supuestos transparentes sobre la evolución de la canasta y de la estructura por edades, será el objeto del Producto 3.

**Este documento *es* el Producto 3, y su Sección 5 declara explícitamente que sus proyecciones no incorporan la demografía.** No basta con cambiar el número. Sustituir por:

> La Sección 5 de este documento establece el punto de partida cuantitativo —trayectoria demográfica, posición fiscal observada y proyección inercial de los agregados— sobre el cual esta presión puede evaluarse. La proyección condicionada al envejecimiento, bajo supuestos explícitos sobre la evolución de la canasta de servicios y de la estructura por edades, corresponde al Producto 4.

### B.2 §5.3.3 — referencia cruzada rota
Texto actual: `…la presión demográfica documentada en la Sección 4.1…`

La demografía está en la **Sección 2**; la 4.1 son esquemas de financiamiento de salud. Corregir a: `…la presión demográfica documentada en las Secciones 2 y 4.3…`

Preferentemente sustituir por `\ref{}` con la etiqueta correspondiente. **Barre todo el documento en busca de referencias cruzadas escritas a mano** (`grep -n "Sección [0-9]" main.tex`) y verifica cada una contra el índice compilado. El traspaso ya documentaba desalineación de numeración; asume que hay más de una rota.

### B.3 Nota de cierre
Primera oración: `Este documento cierra el alcance del Producto 3` — es correcta y **debe conservarse**. Verifica sólo que el resto del párrafo no reintroduzca lenguaje de P2.

---

## BLOQUE C — Bibliografía

**El documento tiene una sola entrada bibliográfica (World Bank 2025) y cita al menos cuatro obras y siete bases de datos en el cuerpo.** Es el defecto de forma más visible del documento.

Construir la sección de Referencias con, como mínimo:

- **Fuentes citadas en el cuerpo:** Holzmann, R. y Hinz, R. (2005), *Old Age Income Support in the 21st Century*, Banco Mundial; Hyndman, R. y Athanasopoulos, G. (2021), *Forecasting: Principles and Practice*, 3.ª ed., OTexts; CEPAL (2020) —localizar la referencia exacta que sustenta el dato de 92.1 % de afiliación al IVM costarricense en §3.1.2—; Bai, J. y Perron, P. (2003) sobre detección múltiple de rupturas, citado implícitamente en la Nota de cierre.
- **Bases de datos, en subsección aparte:** UN World Population Prospects 2024; WHO Global Health Expenditure Database (GHED); OIT-ILOSTAT; SEDLAC (CEDLAS y Banco Mundial); FMI, World Economic Outlook (abril 2025); CEPAL/FMI-GFS, gasto público por función.
- **Instrumentos normativos:** dado el volumen de leyes citadas (Ley 51/2005 y 462/2025 Panamá; Ley 21.735 y DL 3.500 Chile; Ley 100/1993 y 2381/2024 Colombia; EC 103/2019 Brasil; LSS, LSAR y Ley del ISSSTE México; Ley 7983 y 2738 Costa Rica), **crear una subsección de Fuentes normativas** o un anexo breve. No mezclar con la bibliografía académica.

Usar estilo consistente con lo ya presente. Si el proyecto tiene `.bib`, poblarlo; si no, escribir el entorno `thebibliography` directamente.

---

## BLOQUE D — Tabla 9 (composición del gasto en salud)

**Problema:** en tres filas un componente excede su propio total. Costa Rica: contributivo 4.67 > público total 4.61. Colombia: 5.99 > 5.74. Chile: 5.83 > 5.25. La nota al pie lo explica correctamente, pero visualmente la tabla se lee como error aritmético.

**Solución (sin tocar un solo número): partir en dos paneles.**

- **Panel A — Agregados (GGHE-D / PVT-D):** País · Gasto total · Gasto público total · Gasto privado total · Gasto de bolsillo. Aquí la identidad contable cierra y el lector la verifica de inmediato.
- **Panel B — Desagregación del gasto público por esquema de financiamiento (SHA 2011):** País · Contributivo (HF.1.2) · Presupuestario (HF.1.1). Encabezado del panel, no nota al pie:

> Los valores de este panel proceden de la clasificación por esquema de financiamiento de GHED y **no son estrictamente aditivos respecto al agregado del Panel A**: en Colombia y Chile una fracción del esquema contributivo obligatorio se clasifica fuera del perímetro del gobierno general, por lo que sus valores contributivos constituyen una cota superior. La suma reproduce el gasto público total con exactitud en México y Brasil y con desviación menor a 0,25 pp en Costa Rica y Panamá.

Conservar la nota de fuente y la verificación de identidad contable del Panel A. Usar `booktabs`, coherente con el resto del documento.

---

## BLOQUE E — Reconciliación GHED / CEPAL-GFS

**Problema:** el gasto público en salud de Costa Rica aparece como 4.61 % del PIB en la Tabla 9 y como 0.69 % en la Tabla 11. Panamá: 4.27 vs 1.72. México: 2.68 vs 1.24. Cada tabla explica su propia limitación; **ninguna remite a la otra.** Cuarenta páginas de distancia. Un lector que cite el 0.69 % de Costa Rica nos deja en posición insostenible.

### E.1 Párrafo de reconciliación
Insertar al inicio de §5.2.2, **antes** de la frase que introduce las Figuras 5 y 6:

> Antes de leer estas series conviene reconciliarlas con las de la Sección 4.1. Los niveles de gasto público en salud que aquí se reportan son sistemáticamente inferiores a los de la Tabla 9 porque miden cosas distintas: la Tabla 9 recoge el gasto público total en salud según la clasificación GHED de la Organización Mundial de la Salud, que incorpora los esquemas de seguro social obligatorio con independencia de su ubicación institucional; las series de esta sección proceden de la base de gasto por función de CEPAL/FMI-GFS con **cobertura de gobierno central**, que excluye a las instituciones de seguridad social con autonomía presupuestaria. La brecha es mayor donde esa autonomía es mayor: Costa Rica registra 4,61 % del PIB en la Tabla 9 y 0,69 % en la Tabla 11, diferencia que corresponde casi enteramente al Seguro de Enfermedad y Maternidad de la CCSS; Panamá presenta la misma discrepancia por la CSS, y México una versión atenuada por el IMSS y el ISSSTE. **Los niveles de esta sección no deben citarse como medida del gasto público en salud de estos países; su utilidad es la consistencia interna en el tiempo, que es la propiedad que requiere el análisis de series que sigue.**

### E.2 Referencias cruzadas recíprocas en las notas
- Nota de la **Tabla 9** (o del Panel A), añadir al final: `Estas cifras no son comparables con las de la Tabla 11, de cobertura de gobierno central; véase la reconciliación al inicio de la Sección 5.2.2.`
- Nota de la **Tabla 11**, añadir al final: `Los niveles no son comparables con los de la Tabla 9 (GHED, cobertura institucional completa); véase la reconciliación al inicio de esta subsección.`
- Añadir la misma advertencia, en una línea, a la nota de la **Tabla 12**, que hereda el problema en el numerador.

---

## BLOQUE F — Tabla 8 (cobertura efectiva)

**Problema:** en el producto cuyo objeto contractual es la compilación de datos, hay una columna íntegramente vacía y una fila casi vacía.

### F.1 Eliminar la columna "Cobertura contributiva (PEA)"
Está en `Pend.` para los seis países. Suprimir la columna del cuerpo de la tabla y trasladar el compromiso al texto de §3.3.2:

> La cobertura contributiva de la población económicamente activa —proporción de la PEA que cotiza activamente— no se deriva de las bases utilizadas en esta compilación y se incorporará en el Producto 4 a partir de registros administrativos nacionales: CONSAR e IMSS en México, CCSS en Costa Rica, CSS en Panamá, Colpensiones y Superintendencia Financiera en Colombia, INSS en Brasil, y Superintendencia de Pensiones en Chile. Es un indicador conceptualmente distinto de los que sí recoge la Tabla 8: las columnas de cobertura de 65 años y más miden receptores de pensión, no cotizantes activos.

Conservar íntegramente la nota (a) sobre Brasil, reubicándola.

### F.2 Fila de Chile
No la elimines. Conserva los `Pend.` con la nota (b) ya redactada, que identifica correctamente fuente prevista (IPS / Superintendencia de Pensiones) y motivo de la ausencia (Chile excluido del archivo SEDLAC). **Es disciplina de verificación bien ejecutada y así debe leerse.** Verifica sólo que la nota (b) quede visible y no comprimida.

### F.3 Caveat de acervo en la brecha de género
El hallazgo del signo opuesto sistemático es sólido y debe conservarse. Añadir, al final del párrafo de §3.3.2 que interpreta la brecha:

> Esta lectura requiere una precisión temporal. La cobertura de la población de 65 años o más es un indicador de acervo: refleja las historias laborales de cohortes nacidas aproximadamente entre 1935 y 1958, no las condiciones de formalización vigentes. No puede leerse, por tanto, como enunciado sobre los incentivos que hoy enfrentan hombres y mujeres al decidir su participación en el empleo formal, dimensión sobre la cual la evidencia reciente para la región apunta en dirección no necesariamente coincidente.

---

## BLOQUE G — Vínculo con el marco de incentivos de formalización

**Problema sustantivo, no de forma.** La referencia central del ángulo BDH —World Bank (2025), Fietz et al.— figura en la bibliografía y **no se cita ni una vez en el cuerpo**. Las Secciones 3.2 y 4.2.2 plantean la pregunta correcta (complemento o sustituto) y la abandonan sin cerrar el canal fiscal. Es lo que distingue este documento de una compilación de taxonomías ya publicadas.

**Restricción de derechos:** parafrasear siempre; no citar textualmente la fuente.

### G.1 Cierre de §3.2
Añadir como último párrafo de la subsección, tras la Tabla 7:

> La distinción no es sólo clasificatoria: determina por qué canal la demografía se convierte en riesgo fiscal. Cuando el componente no contributivo opera como sustituto —cuando el beneficio asistencial resulta accesible en condiciones comparables al contributivo sin exigir historia de cotización—, el valor que el trabajador atribuye a contribuir se reduce, y con él el retorno percibido de la formalización. La literatura reciente sobre incentivos de formalización en la región documenta este mecanismo mediante indicadores compuestos que integran la cuña tributaria, la valoración del beneficio y los costos de cumplimiento, y muestra que la valoración del componente contributivo —la riqueza previsional que el trabajador percibe haber acumulado— es determinante de la decisión de cotizar (World Bank, 2025). La consecuencia macrofiscal es de segundo orden pero acumulativa: un diseño sustitutivo erosiona la base contributiva sobre la que descansa el financiamiento del Pilar 1, desplazando el peso hacia las rentas generales justamente cuando la razón de dependencia senil se duplica. El envejecimiento amplifica una tensión que el diseño institucional ya contiene.

### G.2 Cierre de §4.2.2
La subsección ya plantea la pregunta y la deja abierta. Añadir tras el párrafo final:

> El mecanismo es el mismo que en pensiones, con una diferencia que lo agrava: en salud el beneficio es de disfrute inmediato y no diferido, de modo que la comparación entre la red contributiva y la presupuestaria es directamente observable para el trabajador. Cuando la red no contributiva provee servicios de calidad y oportunidad cercanas sin exigir cotización, el diferencial de valor que sostiene la decisión de formalizarse se estrecha —y, a diferencia del caso previsional, sin el descuento intertemporal que atenúa la percepción del beneficio pensional. La segmentación descrita en la Sección 4.2.1 opera así en dos direcciones simultáneas: genera un costo no monetario de la informalidad donde la brecha de calidad es amplia, y un incentivo a permanecer informal donde esa brecha se cierra sin contrapartida contributiva.

---

## BLOQUE H — Neutralización textual del riesgo de las proyecciones

**Sin regenerar figuras.** Toda la exposición se acota mediante texto. Este bloque sustituye a la poda por MASE que habría requerido re-correr el pipeline.

### H.1 Advertencia sobre series no informativas — §5.3.3
Insertar como **primera** precisión de §5.3.3, antes de las tres actuales (que pasan a ser segunda, tercera y cuarta; ajustar los ordinales del texto):

> La primera y más importante precisión concierne al desempeño desigual de los modelos entre series. El error absoluto medio escalado (MASE) reportado en la Tabla 13 compara cada modelo con el método ingenuo de persistencia: un valor superior a la unidad indica que la especificación seleccionada no supera a la regla de suponer que la serie mantiene su último valor observado. Ese es el caso en poco más de la mitad de las treinta series. En algunas la discrepancia es de una magnitud que las inhabilita como estimación puntual: la deuda neta de Costa Rica, estimada sobre catorce observaciones, arroja un MASE de 7,38 y una raíz del error cuadrático medio de 36,6 puntos del PIB; el balance primario de Costa Rica (5,59), Brasil (4,23) y Panamá (3,26) muestra un patrón análogo. **Las trayectorias correspondientes a series con MASE superior a dos se presentan por completitud del ejercicio uniforme y no deben leerse como pronóstico ni citarse como estimación puntual.** El caso del balance primario merece mención propia: es la única de las cinco series que resulta estacionaria o próxima a serlo, y su reversión a la media alrededor de cero —consistente con su naturaleza de flujo, según se documentó en la Sección 5.3.1— hace que la extrapolación univariada aporte poca información más allá de esa media. La lectura informativa de este ejercicio se concentra en las series de nivel con memoria larga: deuda neta, ingresos y gasto funcional en los países donde la muestra es suficiente.

### H.2 Nota de la Figura 11 (gasto público en salud)
Añadir al pie:

> La trayectoria proyectada para Chile —que extiende el nivel observado de 6,0 % del PIB en 2020 hacia valores sustancialmente superiores al final del horizonte— es resultado de la extrapolación de una tendencia histórica pronunciada y sostenida, sin restricción de plausibilidad ni amortiguación de la pendiente. Constituye una caracterización de la inercia de la serie, no un escenario de gasto. La misma advertencia aplica, en menor magnitud, a Colombia.

### H.3 Nota de la Figura 12 (gasto público en pensiones)
Añadir al pie:

> La proyección para México extrapola la maduración del régimen de transición documentada en la Sección 3.1.1, cuya dinámica histórica es fuertemente ascendente por construcción demográfica y de cohorte. Al no incorporar el agotamiento previsible de esa cohorte, la extrapolación univariada sobreestima la pendiente de mediano plazo.

### H.4 Nota de la Figura 9 (balance primario)
Añadir al pie: `Cuatro de las seis series de este panel presentan MASE superior a dos; véase la primera precisión de la Sección 5.3.3.`

### H.5 Advertencia sobre solapamiento de horizonte
Añadir a la precisión de cobertura temporal de §5.3.3 (la actualmente segunda, tras la reordenación):

> Adicionalmente, dado que las series de gasto funcional terminan entre 2017 y 2020, un horizonte de proyección de diez años cubre en parte años ya transcurridos. El tramo inicial de esas trayectorias no es pronóstico sino reconstrucción inercial de un período observable por otras fuentes.

### H.6 Promesa de anexo inexistente
En §5.3.2, la oración `…la incertidumbre, que crece de forma sustancial con el horizonte y que se documenta en el anexo técnico de este producto.`

**No hay anexo técnico.** Sustituir el final por: `…la incertidumbre, que crece de forma sustancial con el horizonte y cuya cuantificación mediante intervalos de pronóstico se incorporará en el Producto 4.`

---

## BLOQUE I — Marcadores `[VERIFICAR]`

Hay al menos seis en texto visible. **Ninguno se resuelve inventando la cifra.** La regla es: reescribir la oración para que no dependa del dato faltante, apoyándose en información que el documento ya contiene y verificó.

### I.1 §2.1 — fecundidad regional y esperanza de vida
Los dos marcadores piden agregados regionales que el documento no compiló. **Reescribir el párrafo para apoyarse en la muestra de seis países, que sí está verificada en la Tabla 1:**

> La transición demográfica de América Latina y el Caribe presenta, observada en agregado, los rasgos esperables de una región que entró tarde pero avanza rápido respecto a las economías de la OCDE. En los seis países de este estudio la tasa global de fecundidad promedia 1,62 hijos por mujer en 2024 y se sitúa por debajo del nivel de reemplazo poblacional (2,1) en cinco de ellos, con Panamá en el umbral; la esperanza de vida al nacer promedia 78,6 años, con convergencia parcial hacia los niveles de la OCDE (véase la Tabla 1).

### I.2 §2.4 — diferencial de PIB per cápita
Reescribir sin la magnitud, conservando el argumento cualitativo:

> Las economías que hoy componen la OCDE alcanzaron las razones de dependencia senil actualmente vigentes en ALC con un producto per cápita significativamente mayor al que registran hoy los países de la región. La cuantificación de ese diferencial, sobre series comparables a paridad de poder adquisitivo, se incorporará al análisis del Producto 4.

### I.3 §4.1 — cobertura de *saúde suplementar*
Reescribir sin porcentaje:

> El SUS coexiste con una red privada (*saúde suplementar*) que cubre a una fracción significativa de la población, mayoritariamente vía planes vinculados al empleo formal, y cuya magnitud precisa se documentará con estadística de la Agência Nacional de Saúde Suplementar.

### I.4 §4.2.2 — techo de gasto brasileño
El régimen de la EC 95/2016 fue sustituido por un nuevo marco fiscal en 2023. **Confirma el instrumento y su denominación antes de escribir la cifra o el número de ley.** Redacción segura mientras tanto:

> El financiamiento, sin embargo, está sujeto a presiones recurrentes: los recursos efectivamente destinados al SUS son objeto de las negociaciones fiscales del marco general, cuyo régimen de límite de gasto fue sustituido en 2023 por un nuevo marco fiscal con reglas de crecimiento del gasto distintas a las de la Emenda Constitucional 95/2016.

### I.5 §4.3.1 — cociente de gasto en salud por edad
El rango de tres a cinco veces es consistente con la literatura de perfiles de gasto por edad. Eliminar el marcador y sustituir por nota al pie:

> Rango consistente con los perfiles de gasto en salud por edad de la metodología National Transfer Accounts y con las cuentas nacionales de salud por grupo etario disponibles para la región. El cálculo específico para los seis países del estudio se incorporará en el Producto 4.

### I.6 Barrido final
`grep -n "VERIFICAR" main.tex` debe devolver **cero resultados**. Si el proyecto define un comando o color para estos marcadores, elimina también la definición si queda sin uso.

---

## BLOQUE J — Precisiones metodológicas menores

### J.1 Deuda neta vs. bruta
El documento usa deuda neta sin justificarlo. Añadir en §5.2, tras la enumeración de los cinco indicadores:

> Se emplea deuda neta y no bruta porque descuenta los activos financieros del sector público, entre ellos las reservas de los regímenes previsionales de capitalización colectiva, cuya magnitud difiere sustancialmente entre los seis países y distorsionaría la comparación de posición fiscal si se ignorara. La contrapartida es que la deuda neta es menos comparable internacionalmente que la bruta, por la heterogeneidad en la valuación de activos.

### J.2 Series de la Tabla 13
No modificar ningún valor. Verificar únicamente que la tabla quepa sin desbordar el margen y que la nota al pie sobre MASE remita ahora a la Sección 5.3.3.

---

## BLOQUE K — Erratas

Corregir todas:

| Ubicación | Actual | Corregido |
|---|---|---|
| §5.3.3 | `normalización posfinal de la pandemia` | `normalización posterior a la pandemia` |
| §5.1 / Fig. 1 | `El tramo final del bono demográfico, es el período` | `El tramo final del bono demográfico es el período` |
| Nota de cierre | `…publique ejercicios posteriores, permitirá revisar…` | `…publique ejercicios posteriores, lo que permitirá revisar…` |
| §5.2 | `ingresos del gobierno, balance primario y deuda neta del gobierno y provienen del…` | falta la raya de cierre del inciso: `…y deuda neta del gobierno— y provienen del…` |
| §3.1.1 | `el artículo 4.oreconoce` y `del artículo 4.oconstitucional` | espacio faltante tras `4.º` (buscar todas las ocurrencias del patrón) |
| Tabla 8 | superíndices de año pegados al valor | verificar espaciado en la versión compilada |

Barrido adicional recomendado: `grep -n "\.o[a-z]" main.tex` para detectar más ordinales pegados.

---

## BLOQUE L — Compilación y verificación

1. Compilar dos veces (referencias cruzadas y bibliografía).
2. **Lista de verificación obligatoria sobre el PDF compilado:**
   - [ ] Encabezado dice `P3` en todas las páginas
   - [ ] Portada: subtítulo, fecha y autores correctos
   - [ ] `grep "VERIFICAR"` → cero resultados
   - [ ] `grep "^%.*interna"` → cero comentarios de deliberación
   - [ ] Ninguna referencia a "Marina"
   - [ ] Índice muestra cinco secciones
   - [ ] Bibliografía con todas las entradas citadas
   - [ ] Tabla 9 en dos paneles, sin componente mayor que su total en el Panel A
   - [ ] Tabla 8 sin columna PEA
   - [ ] Todas las referencias `Sección X.Y` verificadas contra el índice
   - [ ] Ninguna figura ni valor numérico de las Tablas 10–13 alterado
3. Reportar el conteo de páginas antes y después.

## BLOQUE M — Git

```bash
git add -A
git commit -m "P3: correcciones de identidad, reconciliación de fuentes, vínculo FTR y acotación de proyecciones (solo .tex)"
git push -u origin p3-correcciones-tex
```

No fusionar a `main` sin revisión de Héctor.

---

## Reporte final requerido

Al terminar, entrega:
1. Bloques completados y bloques con incidencia.
2. **Cualquier cadena que no hayas podido localizar** — el PDF y el `.tex` pueden divergir.
3. Cualquier lugar donde una instrucción exigiera un dato no disponible: **repórtalo, no lo completes.**
4. Referencias cruzadas rotas encontradas más allá de las documentadas en el Bloque B.
5. Comentarios de deliberación interna eliminados, con su contenido, para registro de Héctor.

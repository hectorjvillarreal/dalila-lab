# FISCUS — Preparación para la corrida 2027

**Documento 1 de 2.** Se ejecuta **antes** de que se publique el Paquete
Económico 2027. El documento 2 (`INSTRUCCIONES_corrida_en_vivo_2027.md`) se
activa cuando CGPE, ILIF y PPEF estén publicados.

**Proyecto:** FISCUS · **Ubicación:** `FISCUS/económicos_paquetes/` · **Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Antecedentes:** documentos propios 2025 y 2026, y sus dos comparaciones anónimas.

---

## 0. Por qué existe este documento

La corrida 2027 será la primera **sin documento de CIEP para comparar** y con
reloj real: solo lo que se publique el día de la entrega. La comparación anónima
de 2026 señaló que nuestro documento gana en método y pierde en velocidad, y que
la restricción de simulación no demuestra que el mismo nivel de profundidad sea
factible en 72 horas.

La respuesta a eso no es apurarse. Es **mover fuera del reloj todo lo que no
depende del paquete**. Capa demográfica, infraestructura de diffs, pruebas de
identidad, esqueleto de LaTeX, plantillas y series históricas se pueden construir
y probar antes. El día de la entrega solo debe quedar el trabajo que sí depende
del documento.

Este archivo tiene dos partes: **corregir lo que la comparación 2026 encontró**
(§1–§2) y **precargar** (§3).

---

# PARTE A — Correcciones

## 1. La compuerta semántica

Es la lección principal de la comparación 2026: **las identidades contables
validan aritmética, no semántica.** Treinta y tres pruebas cerraron y aun así
tres afirmaciones excedieron su perímetro. Un sistema puede cerrar perfectamente
y contener un titular demasiado amplio.

### 1.1 Las tres correcciones concretas

Aplícalas al documento 2026 y a las plantillas:

| Dice | Debe decir |
|---|---|
| "Pensiones caen 0.7 %" | "El agregado de pensiones y jubilaciones de la clasificación económica cae 0.7 % real, mientras las pensiones no contributivas crecen" |
| "casi la mitad de todo el gasto de capital" son instrumentos financieros | "Dentro de los capítulos 6000 y 7000, cerca de la mitad corresponde a inversiones financieras y provisiones, con la aportación de capital a Pemex como componente dominante" |
| "menos recursos condicionados" | "Los recursos de libre disposición crecen más rápido que los condicionados" (las aportaciones aumentan, a menor tasa) |

Las tres son la misma falla: **el cálculo cerró y la oración excedió su
perímetro.**

Corrige también la inconsistencia de la nota metodológica del documento 2026: usa
un ejemplo de variación educativa que no coincide con el resultado del capítulo
correspondiente.

### 1.2 La regla, para incorporar a la rúbrica

> **El perímetro de la frase debe coincidir con el perímetro del cálculo.**

Un agregado que se calculó sobre una clasificación, una función o dos capítulos
del objeto del gasto **no puede nombrarse con la palabra general** que designa al
conjunto mayor. Si el cálculo es de "pensiones y jubilaciones de la clasificación
económica", la frase no dice "pensiones". Si es de los capítulos 6000 y 7000, la
frase no dice "gasto de capital".

### 1.3 El procedimiento

Construye `_aprendizaje/compuerta_semantica.md` y aplícalo como paso obligatorio
al cierre de cada capítulo, **antes** de compilar:

1. Toma cada titular, cada frase del resumen y cada pie de figura.
2. Localiza el renglón de la ficha metodológica del que sale su cifra.
3. Compara el sujeto de la frase con el perímetro de la ficha. Si el sujeto es
   más amplio, **reescribe la frase**, no la ficha.
4. Marca cada afirmación causal y pregunta las cuatro del reporte: ¿está
   documentada por la fuente? ¿puede ser reclasificación? ¿puede ser composición?
   ¿puede ser un efecto contable?
5. Registra en la bitácora cuántas frases se reescribieron.

Es una revisión editorial, no una prueba automática. **Ninguna identidad contable
la sustituye.**

## 2. La nota del deflactor

La comparación pide explicar mejor por qué usamos el deflactor del PIB. La regla
que ya tenemos es correcta y lo que faltó fue exponerla. Escribe un **recuadro
metodológico** para el documento, no un segundo juego de cifras por capítulo:

- Deflactor del PIB para agregados fiscales y toda razón a PIB, por consistencia
  con cuentas nacionales.
- Índice de precios al consumidor cuando la pregunta es el poder de compra de una
  prestación individual, porque ahí la pregunta es de bienestar.
- Una sola línea de sensibilidad con inflación promedio, **en el recuadro
  metodológico y no en los capítulos**, para que nadie mezcle las dos
  convenciones en un cuadro.

---

# PARTE B — Precarga

## 3. Lo que se construye antes de la entrega

Todo lo de esta sección **no depende del Paquete Económico 2027** y debe quedar
construido y **probado** antes de que se publique. El criterio de terminación de
este documento es que todo §3 esté hecho y verificado.

### 3.1 Capa demográfica cargada, con padrones

En la corrida 2026 no publicamos gasto por afiliado porque no conseguimos los
padrones bajo el protocolo de fuentes. **Los padrones no dependen del paquete.**

Construye `datos_demograficos/` con su `_fuentes.csv`, cada serie con fuente, año
de referencia, cobertura y liga, tier `externa_demografica`:

- Población total y por grupo de edad, nacional y por entidad: CONAPO, con
  proyección; CELADE como contraste.
- Población en edad escolar por nivel y **matrícula** por nivel: estadística
  educativa oficial.
- **Asegurados y derechohabientes del IMSS**; derechohabientes del ISSSTE.
- Población sin afiliación a seguridad social.
- Padrones de programas pensionarios no contributivos, incluida la pensión para
  mujeres, donde exista publicación.
- Población de 65 años y más, nacional y por entidad.

**Reglas que ya rigen y se conservan:** cuadros presupuestales y cuadros per
cápita van separados; toda cifra per cápita declara su denominador; en educación
se distinguen población total, población en edad escolar y matrícula, que dan
tres lecturas distintas; y una razón de presión demográfica no es una prestación
media —el denominador incluye a quien no recibe y el numerador puede incluir a
quien no está en el grupo—. Esa advertencia se conserva siempre.

### 3.2 Serie del perímetro de la regla fiscal · PRIORITARIA

Es el hallazgo que ambos documentos perdieron en 2026 y el de mayor valor para
2027.

La ILIF 2026 propone **no contabilizar, hasta 3.6 % del PIB**, gasto en inversión
física, inversión financiera y **desarrollo de capital humano** —educación, salud
preventiva, formación y certificación de competencias— para efectos del
equilibrio presupuestario, excluyendo pensiones, transferencias no
condicionadas, subsidios generalizados y gasto administrativo.

**Reconstruye la serie del perímetro de exclusión, ejercicio por ejercicio, de
2018 a 2026**, con estos campos: artículo de la ILIF que lo establece; artículo
de la LIF aprobada, donde difiera; tope en porcentaje del PIB; conceptos
incluidos; conceptos excluidos.

Puntos conocidos que deben aparecer y verificarse: la ILIF 2023 retiró el tope y
la LIF aprobada lo devolvió a 3.1 %; la ILIF 2026 lo fija en 3.6 % e incorpora
capital humano.

**Y establece la conexión que nadie hizo:** la aportación de capital a Pemex,
clasificada en el capítulo 7000 como adquisición de títulos y valores, **es
inversión financiera** y por tanto candidata a quedar fuera del cómputo del
equilibrio. Los dos hallazgos estaban en nuestro documento 2026, en capítulos
distintos, sin juntar. Verifica si la conexión se sostiene y déjala documentada.

Resultado: `_aprendizaje/serie_perimetro_regla_fiscal.md`. En 2027 este es un
capítulo o recuadro propio y su primera tarea es leer el artículo correspondiente
de la ILIF.

### 3.3 Infraestructura de diffs, probada

Escribe y **prueba contra 2025 → 2026** el diff institucional:

- Ramos que aparecen, desaparecen y cambian.
- Claves de programa presupuestario: altas, bajas, cambios de modalidad.
- Unidades responsables: altas, bajas, cambios de ramo.
- Funciones y subfunciones.

**Agrega por clave, no por nombre.** Y anota la limitación que la corrida 2026
descubrió: la clave completa tampoco es siempre estable, así que el
emparejamiento usa número de programa más contexto de ramo, verificado contra el
diff.

Casos de prueba obligatorios, porque son los que rompen una lectura ingenua:
IMSS-Bienestar, que ha cambiado de ubicación tres veces; y la Guardia Nacional,
donde coexisten cambio de ramo y reducción propia.

En 2026 fueron 271 claves nuevas y 358 desaparecidas. El diff no es un lujo: sin
él, una comparación automática produce recortes y aumentos falsos.

### 3.4 Pruebas de identidad, parametrizadas

Toma las treinta y tres pruebas del documento 2026 y déjalas como **script
parametrizado por ejercicio**, no como cálculo del año. Mínimo:

- Ingreso total = gasto neto total.
- Gasto bruto − neteo = gasto neto.
- Bruto coincidente por rutas independientes.
- Reconciliaciones entre anexos.
- Consistencia del agregado pensionario.
- Coherencia del balance y de los tres flujos.
- Reconciliación ILIF ↔ CGPE en ingresos.
- Suma por ramos ↔ suma por función.
- Flujo contra acervo (SHRFSPF / RFSPF).

Pruébalo contra 2026, que ya cerró, y déjalo listo para correr contra 2027.

### 3.5 Esqueleto de LaTeX compilado y probado

**Ningún minuto del reloj de 2027 debe irse en depurar compilación.**

Construye `_documento_2027/` con `main.tex`, `capitulos/` con un archivo vacío
por capítulo previsto, `datos/`, `figuras/`, `bibliografia.bib` y `LEEME.md`.
Portada, autoría y filiación de ITED ya puestas.

Restricciones duras, ya establecidas: **sin `siunitx`** —los números se formatean
al generar los cuadros—; `pgfplots` con `compat=1.16`; solo `babel` (spanish),
`geometry`, `fancyhdr`, `booktabs`, `graphicx`, `hyperref`, `caption`,
`longtable`, `array`, `pgfplots`; nada que requiera `shell-escape`; nada que haya
que instalar.

**Compílalo con contenido de relleno y verifica que produce PDF.** Y prueba el
ZIP en un entorno limpio. Si una figura resulta frágil, la salida es generar su
PDF por separado e incluirlo con `\includegraphics`, conservando script y datos.

### 3.6 Plantillas

- **Lámina de capítulo:** titular cuantitativo con signo y base declarada; figura
  principal; párrafo de "qué cambió"; párrafo de "por qué importa".
- **Ficha metodológica de cierre:** perímetro, línea de comparación, deflactor,
  año de los pesos, PIB y añada, denominadores, fuentes, y **qué no puede
  afirmarse con ellas**.
- **Sección "qué no sabemos"**, por capítulo.
- **Declaración de capítulo no redactable**, escrita en el registro del documento.

### 3.7 Series históricas extendidas a 2026

Deja calculadas y verificadas, para que en 2027 solo se agregue un punto:

| Serie | Capítulo |
|---|---|
| Tributarios / gastos obligatorios (con y sin cuotas IMSS) | Ingresos |
| Pensiones + costo financiero / tributarios | Gasto total |
| Pensiones IMSS / cuotas IMSS (serie aprobada y serie ex ante, separadas) | Pensiones |
| Cuotas obrero-patronales / gasto en salud IMSS | Salud |
| Educación / pensiones y jubilaciones; segunda línea contra pensiones totales | Educación |
| Costo financiero / tributarios; SHRFSPF / tributarios en años | Deuda |
| Perímetro de exclusión de la regla fiscal (§3.2) | Regla fiscal |

Ninguna línea híbrida: ex ante con ex ante, aprobado con aprobado.

### 3.8 Rutas de descarga probadas

Deja un guion de descarga con las rutas **ya verificadas**, para no explorar con
el reloj corriendo:

- CGPE, ILIF y PPEF en el portal de la Secretaría.
- **Analíticos del proyecto**, en este orden: portal de la Secretaría; **portal
  de datos abiertos**, que es donde suelen aparecer el día de la entrega;
  Transparencia Presupuestaria.
- Iniciativa de miscelánea en la Gaceta Parlamentaria.

Notas de operación ya conocidas: prepara el **bundle de certificados TLS** —hoja
firmada por el intermedio YR1, el servidor envía R10— sin desactivar la
verificación; los analíticos traen los datos en la hoja **`Hoja1`**, no en la
primera, que es un resumen por ramo; las figuras sin capa de texto se leen
renderizando la página; el PDF de la ILIF **contiene su exposición de motivos**,
no la busques aparte.

Prueba las rutas contra 2026 y deja registrado cuáles respondieron.

### 3.9 Checklist de omisiones propias · SUSTITUYE AL COMPARADOR

En 2027 no habrá documento de CIEP para detectar lo que se nos pase. **Esta lista
es su reemplazo.**

Constrúyela en `_aprendizaje/checklist_omisiones.md` a partir de los apartados
"lo que el otro documento tiene y nosotros no" de las comparaciones 2025 y 2026.
Al menos:

- Política tributaria en detalle: Código Fiscal, facturación, RFC, aduanas,
  comercio electrónico, impuestos específicos.
- Comparación del marco macro con consenso de analistas, banco central y
  organismos internacionales.
- Salud por tipo de afiliación y gasto de bolsillo.
- Gasto por alumno por nivel educativo.
- Desigualdad pensionaria.
- Federalismo más allá de los Ramos 28 y 33: convenios, subsidios, coordinación
  fiscal, distribución subnacional.
- Medio ambiente y agua como política, no solo como composición funcional.
- Economía de cuidados: qué parte del anexo es gasto preexistente.
- Género: concentración del anexo y qué proporción son pensiones.
- Balances de empresas públicas con y sin apoyos.

Para cada renglón, la checklist dice **qué fuente lo resuelve y si esa fuente
estará disponible en vivo**. Los que no lo estén se declaran fuera de alcance en
el documento, con su razón.

---

## 4. Alcance de la corrida 2027 — decidido de antemano

No se intentan las seis capas del estándar ideal en la ventana de una entrega.
**Se conserva el motor, que es la ventaja, y se añade lo que cabe:**

**Se hace:** integridad contable y perímetros; dos líneas de comparación;
reclasificaciones; deuda con descomposición de cuatro variables; capa demográfica
precargada; anexos transversales como auditoría de etiquetado; **capítulo de la
regla fiscal**; compuerta semántica; lámina y ficha por capítulo.

**No se intenta:** incidencia distributiva completa, política de cuidados,
política de género, y política ambiental sectorial. Género y cuidados se tratan
**solo** como auditoría de anexos, que es donde nuestro método aporta. Lo que
quede fuera se declara en el documento con su razón, no se omite en silencio.

---

## 5. Criterio de terminación

Este documento está terminado cuando:

1. Las tres correcciones semánticas y la nota del deflactor están aplicadas.
2. `compuerta_semantica.md` existe y está probado sobre un capítulo de 2026.
3. La capa demográfica está cargada con sus fuentes declaradas.
4. La serie del perímetro de la regla fiscal está reconstruida de 2018 a 2026.
5. El diff corre contra 2025 → 2026 y resuelve los dos casos de prueba.
6. Las pruebas de identidad corren contra 2026.
7. **El esqueleto de LaTeX compila y produce PDF**, y el ZIP abre limpio.
8. Las series históricas están extendidas a 2026.
9. Las rutas de descarga están probadas y registradas.
10. La checklist de omisiones existe con su columna de disponibilidad en vivo.

Reporta en la bitácora cuáles quedaron cumplidos y cuáles no. **Lo que no quede
precargado se pagará con reloj.**

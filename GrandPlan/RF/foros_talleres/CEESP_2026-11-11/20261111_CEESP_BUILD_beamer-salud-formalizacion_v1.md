---
id: BUILD-20261111-CEESP-BEAMER
title: "Build instruction — Beamer, presentación virtual ante el CEESP (11-nov-2026): financiamiento de la salud, formalización y demografía"
type: build_instruction
track: seminario / discusión pública (NO es producto RF)
version: v1
derives_from: presentación del foro «Los retos del espacio fiscal en México», sesión 2 (22-sep-2026); BUILD-20261022-EXATEC-BEAMER v2
added_by: Cath
endorsed_by:
date: 2026-11-10
target: Claude Code (Dalila)
deadline: PDF y página de revisión hoy, 10-nov, antes de las 23:00; presentación virtual el 11-nov
status: draft v1
---

# Instrucción de construcción: presentación ante el CEESP

## 0. Qué se hace

Héctor presenta en forma virtual ante el Centro de Estudios Económicos del Sector Privado (CEESP). Tiene cerca de una hora de exposición, con interrupciones, y después treinta minutos de discusión. Sin notas del orador.

**Base:** la presentación del 22 de septiembre, *¿Cómo financiar la salud universal? Espacio fiscal, aseguramiento y una agenda regional* (26 láminas). Busca su `.tex` en Dalila; el PDF se llama `foro_20260922_salud_hjvp.pdf`. Copia todo a `.../foros_talleres/CEESP_2026-11-11/` y no modifiques el original. Conserva su tema y su estilo; las láminas que vengan de EXATEC se adaptan a ese estilo, no al revés.

**Cambios de fondo respecto a la base:**

1. Datos actualizados: Contabilidad de la muerte a enero–septiembre, PEF en lugar de PPEF y la reforma al ISR en su versión final.
2. **Demografía ampliada:** tres láminas nuevas.
3. **Formalización ampliada:** el modelo de formalización y la propuesta de retirar Infonavit, con base en el trabajo hecho para el IMSS.
4. Adaptación al público: economistas del sector privado, a quienes les importa quién paga las cuotas y qué espacio hay para el financiamiento privado.
5. Un apéndice para la discusión.

Meta: unas 35 láminas de exposición, más fuentes y apéndice.

**Límites:**

- Sin vocabulario interno: nada de "RF", "G1–G5", "pilares", "OSF", "neteo", "DFD", "BDH", nombres de agentes ni rutas.
- **Sin atribución institucional en el tema Modalidad 40** (lámina 29). En la portada no aparece ITED (sección 3, lámina 1).
- No inventar cifras. Toda cifra nueva debe tener fuente documentada en Dalila o venir de la tabla de la sección 2. Si una lámina nueva no tiene sustento, **no se construye**: se omite y se reporta.
- No buscar en la web.

## 1. Fuentes permitidas: uso de otros proyectos

Héctor autoriza usar material de otros proyectos en Dalila, además de RF:

- **Trabajo para el IMSS** sobre el modelo de formalización y la propuesta de retirar Infonavit. Es la fuente principal del bloque de formalización. Búscalo con `grep -ril` sobre "IMSS", "formalización", "Infonavit", "trampa de formalización", "FTR".
- **Proyecto demográfico-fiscal:** proyecciones de población, razón de dependencia, perfiles por edad, material de Cuentas Nacionales de Transferencia (NTA) y monitor demográfico.
- **Proyecto de seguridad social y salud:** parámetros, notas y corpus.
- **Presentaciones previas:** CEPAL (Santiago, mayo de 2026: arquitectura de seguridad social, impuesto negativo), CISS v2 (pensiones, escalón de la trampa de formalización, arquitectura multipilar) y EXATEC del 22 de octubre (v2).
- **Monitor mensual de la Contabilidad de la muerte.**

**Cautelas:**

1. **Artículo sobre elección de formalidad (logit condicional, ENIGH 2022):** tiene correcciones obligatorias pendientes (manejo de ponderadores que infla los errores estándar, etiqueta de modelo, umbral μ de 0.2 en el código y 0.3 en el texto). **No uses sus estimaciones** salvo que exista una re-estimación posterior documentada. Si no la hay, cita solo la lógica del modelo.
2. **Trabajo para el IMSS:** si algún documento está marcado como confidencial, interno o borrador para la institución, usa la lógica y el diseño, no cifras institucionales. En la página de revisión lista **cada cifra derivada de ese trabajo** con su archivo de origen, para que Héctor confirme que puede mostrarse.
3. **Demografía:** hay una discrepancia abierta entre las TFR del archivo de línea base y los datos del Observatorio Demográfico de CELADE 2025 para México. No uses las TFR de ese archivo; usa las de la lámina 4 de la base (WPP 2024 e INEGI).
4. En los pies de lámina, las fuentes se citan en forma pública (autor, institución, año), nunca por proyecto ni ruta.

## 2. Cifras nuevas verificadas (usar tal cual)

| Cifra | Valor | Fuente para el pie |
|---|---|---|
| Reforma al ISR, versión final | Tope a deducciones de 96.67 % de los ingresos acumulables para empresas con ingresos > 50 mdp; el Senado (27 de octubre) excluyó a las armadoras y ensambladoras de vehículos en depósito fiscal y a los expendedores de gasolina y diésel; la Cámara de Diputados ratificó los cambios el 4 de noviembre | Congreso de la Unión, minuta LISR 2027 |
| LIF 2027 | Aprobada por el Senado el 27 de octubre | Ídem |
| PEF 2027 | Gasto neto total de 10.64 billones de pesos; dictamen aprobado por la Comisión de Presupuesto el 5 de noviembre con reasignaciones menores | Cámara de Diputados, dictamen del PEF 2027 |
| Costo financiero de la deuda | 4.0 % del PIB | PEF 2027; CIEP con datos de SHCP |
| Techo de endeudamiento del Gobierno Federal | ≈ 4.9 % del PIB; programado ≈ 4.0 %; meta de RFSP 3.9 % | LIF 2027, arts. 1o y 2o; SHCP, CGPE 2027 |
| Modalidad 40 | Las cifras de la tabla de la instrucción EXATEC v1, sección 2 | Acuerdo ACDO.AS2.HCT.101026/302.P.DG, DOF, 21-oct-2026 |

Etiqueta del presupuesto en todas las láminas: "PEF 2027 (dictamen de la Cámara de Diputados)". Es cierta tanto si el pleno ya votó como si no.

## 3. Contenido por lámina

Clave de origen: **B** = base del 22-sep (número original); **E** = EXATEC v2; **N** = nueva.

### Apertura

**1 — Portada** (B1, adaptada)
- Título y subtítulo como en la base.
- Héctor Juan Villarreal Páez · Escuela de Gobierno y Transformación Pública, Tecnológico de Monterrey · Comunidad Latinoamericana del Conocimiento sobre Financiamiento de la Salud. **Sin ITED.**
- Centro de Estudios Económicos del Sector Privado (CEESP) · Sesión virtual · 11 de noviembre de 2026.

**2 — Tres preguntas** (B2, adaptada)
- Quitar la referencia a "la sesión anterior".
- Mantener las tres preguntas (quién paga, cuánto, por cuánto tiempo).
- Cambiar la agenda a cinco temas: demografía, espacio fiscal, formalización, nuestra propuesta y financiamiento privado.

### Demografía (7 láminas)

**3 — Menores de 15 y mayores de 65** (B3, sin cambios)

**4 — ¿Y si Naciones Unidas se queda corta?** (B4, sin cambios)

**5 — La ventana demográfica se cierra** (N)
- Población en edad de trabajar (15–64) como proporción del total, o razón de dependencia, 1970–2100. Misma fuente y variante que la lámina 3 (WPP 2024, variante media).
- Mensaje: el periodo en que la estructura por edades ayudaba a las finanzas públicas ya terminó o está por terminar. Marca el año del máximo.

**6 — El ciclo de vida económico** (N; solo con fuente)
- Perfil por edad de consumo e ingreso laboral para México (NTA), si está documentado en Dalila.
- Mensaje: los años de déficit del ciclo de vida, la niñez y la vejez, se financian con transferencias, y en México la vejez pesa cada vez más.
- Si no hay perfil NTA con fuente, omite la lámina.

**7 — También cambia la forma en que nos enfermamos** (B5, sin cambios)

**8 — El efecto puro de la demografía sobre el gasto** (N; solo con fuente)
- Gasto en salud y pensiones como % del PIB, manteniendo constantes los perfiles por edad y cambiando solo la estructura de la población, si existe un ejercicio documentado en Dalila con método explícito.
- Mensaje: aunque nada cambie en las reglas, el gasto sube.
- Si no hay ejercicio documentado, omite la lámina; no construyas la proyección hoy.

**9 — Esto ya no depende de nosotros. Lo que sigue, sí.** (B6)

### Espacio fiscal (5 láminas)

**10 — ¿Cuánto queda para decidir?** (B7, actualizada)
- Contabilidad de la muerte con enero–septiembre de 2026, del monitor mensual. Si la Bolsa cambia de 4.0, actualiza todas las láminas que la citan (10, 11 y apéndice).

**11 — La deuda ya cuesta tanto como el margen de decisión** (E5)
- Si la Bolsa con enero–septiembre ya no es 4.0, cambia el signo de igual por la relación que corresponda y ajusta el título. No fuerces la igualdad.

**12 — La brecha en salud** (B8, actualizada)
- Miscelánea 2027: las exclusiones del Senado reducen el rendimiento. Usa una estimación actualizada si existe en Dalila. Si no, escribe "alrededor de 0.3 puntos", con nota: "estimación previa a las exclusiones aprobadas por el Senado; el rendimiento final es algo menor".

**13 — Las pensiones le quitan espacio a la salud** (B9; PPEF → PEF)

**14 — ¿Financiar todo con impuestos generales?** (B10)

### Salud en el presupuesto (2 láminas)

**15 — Salud en el presupuesto 2027** (B11; PPEF → PEF)

**16 — Dos sistemas y el gasto de bolsillo** (B12)

### Formalización (6 a 8 láminas)

**17 — El dilema Gruber** (B13)

**18 — El costo de formalizarse** (B14)

**19 — La cuota fija pesa más donde menos se gana** (N)
- La cuota patronal fija del seguro de enfermedades y maternidad (Ley del Seguro Social, art. 106, fr. I: porcentaje de la UMA por trabajador) como % del salario, para 1, 2, 5 y 10 salarios mínimos de 2026.
- Calcula solo con valores documentados: el texto de la LSS, la UMA 2026 (INEGI) y el salario mínimo 2026 (CONASAMI), en el corpus local. Si falta alguno, haz un esquema sin escala de la curva decreciente.
- Mensaje: la parte de la cuota que distorsiona es la que no guarda relación con lo que el trabajador recibe, y se concentra en los salarios bajos.

**20–22 — Nuestro modelo de formalización** (N, de 1 a 3 láminas, del trabajo para el IMSS)
- Estructura sugerida, ajustable a lo que contenga el trabajo:
  - **20 — Cómo decide un trabajador:** qué compara al elegir entre empleo formal e informal (costos, beneficios valorados, transferencias que pierde), en términos llanos.
  - **21 — El escalón:** la trampa de formalización, es decir, dónde se pierde ingreso neto al formalizarse. Si el trabajo trae gráfica, úsala; si no, adapta el esquema de la presentación CISS v2.
  - **22 — Qué mueve la decisión:** los resultados principales del modelo, con las cautelas de la sección 1.
- Si el trabajo da para menos, usa menos láminas. No rellenes.

**23 — Infonavit: la propuesta** (N, del trabajo para el IMSS)
- Qué se propone, por qué y qué pasa con la aportación patronal y con los derechos de los trabajadores.
- Un detalle que importa a este público: si la propuesta reasigna la aportación de 5 % (por ejemplo, a salud o a retiro) o la reduce, dilo con precisión. Determina lo que puede afirmar la lámina 25.
- Si el trabajo menciona el financiamiento del Instituto vía emisión de bonos fuera de presupuesto, puede entrar como argumento.

### Nuestra propuesta (8 láminas)

**24 — Bismarck, Beveridge y nuestra propuesta** (B15)

**25 — Cómo funcionaría** (B16, adaptada)
- Agrega una banda con una afirmación sobre las cuotas, **consistente con la lámina 23**:
  - Si la propuesta de Infonavit reasigna sin reducir: "La propuesta no sube las cuotas obrero-patronales: las reordena."
  - Si reduce la carga: dilo así, con la magnitud del trabajo para el IMSS.
  - Si no es claro: "La propuesta no sube las cuotas obrero-patronales."

**26 — El IMSS como sistema nacional de seguros de salud** (B17)

**27 — Consolidar transferencias** (B18)

**28 — ¿De dónde saldría el 6 % del PIB?** (B19)

**29 — Contener el gasto en pensiones: Modalidad 40** (N, fusión de EXATEC 12 y 13 en una sola lámina)
- Título: *Seguir cotizando es razonable; comprar una pensión no lo es.*
- Izquierda: qué cambió el 21 de octubre. Derecha: quién paga.
- Conecta con el remate de la lámina 28: "Nada de esto funciona si no se contiene el gasto en pensiones."
- Sin atribución institucional.

**30 — Financiamiento privado (I): prepago, no bolsillo** (B20, primera mitad)
- La meta de 8 % del PIB, con 6 puntos públicos y 2 privados, y la diferencia entre prepago y gasto de bolsillo.

**31 — Financiamiento privado (II): instrumentos y reglas** (N, a partir de la segunda mitad de B20)
- Consultorios adyacentes a farmacias, regulados y conectados al sistema; seguros médicos privados de bajo costo con estímulos fiscales o descuento en la prima del IMSS; seguros de largo plazo pagados durante la vida laboral.
- Cierra con la pregunta al público: *¿Qué reglas necesita el sector privado para participar sin fragmentar el sistema?*
- Sin cifras nuevas.

### Cierre (4 láminas)

**32 — Dos preguntas para cualquier propuesta** (B21)

**33 — Sin ancla, cualquier reforma es frágil** (E15 v2, adaptada)
- Dos barras: techo 4.9 frente a programado 4.0, con la línea de la meta de RFSP 3.9.
- Título: *El techo de deuda no ancla: la LIF autoriza casi un punto más de lo programado.*
- Banda nueva: *Responder la primera pregunta exige un ancla fiscal creíble: la reforma de salud y la de ingresos deben ir amarradas a ella.*

**34 — La Comunidad** (B22 y B23 fusionadas)
- Las tres instituciones.
- La reunión de San José del 5 al 7 de octubre, en pasado.
- Una línea sobre lo que salió de ella: `[TEXTO DE HÉCTOR]` en rojo. Héctor lo llena en la revisión.
- Dos de las preguntas abiertas: gasto de bolsillo a prepago y reglas del financiamiento privado.

**35 — Cierre** (B24, sin cambios en la pregunta)

### Fuentes y apéndice

**36–37 — Fuentes** (B25–26, actualizadas con todo lo nuevo, en forma pública)

**A1 — El paquete 2027 mueve la base en el margen** (E6, actualizada con las exclusiones del Senado)

**A2 — Cuatro frentes de reforma** (E9)

**A3 — Detalle del techo de endeudamiento** (interno y externo, Pemex y CFE; cifras de la instrucción EXATEC v1)

## 4. Metadatos y limpieza

- Con `pikepdf`: Title = título de la portada; Author = "Héctor Juan Villarreal Páez". Eliminar Creator, Producer, rutas y demás metadatos.
- Nombre del archivo final: `Villarreal_CEESP_2026-11-11.pdf`.

## 5. Verificación antes de entregar

1. Compilar dos veces sin errores.
2. Revisión visual con `pdftoppm -r 150` de todas las láminas nuevas y adaptadas.
3. `pdftotext` y búsqueda de: vocabulario interno de la sección 0, "ITED", "Iniciativa para la Transición", "PPEF" (salvo en una fuente histórica), "sesión anterior", "Villareal". Todo vacío.
4. Página de revisión, como las de SobreMéxico y EXATEC, con:
   - láminas en miniatura con su origen (B, E, N);
   - **láminas nuevas omitidas** por falta de sustento (6, 8, 19, 20–22) y por qué;
   - **tabla de cifras derivadas del trabajo para el IMSS**, con archivo de origen, para el visto bueno de Héctor;
   - la Bolsa enero–septiembre y si alteró las láminas 10 y 11;
   - qué afirmación quedó en la banda de la lámina 25 y por qué.
5. Commit citando `BUILD-20261111-CEESP-BEAMER v1`.

## 6. Retención

Archivar en `_crossrefs/_build_instructions/`, conforme a PROTO-RAG-001. Esta instrucción autoriza por primera vez el uso cruzado de material de otros proyectos en una presentación pública; queda registrado como precedente. `endorsed_by` queda vacío hasta revisión.

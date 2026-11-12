---
id: BUILD-20261112-RIUSS-BEAMER
title: "Build instruction — Beamer, conferencia magistral de apertura, Congreso RIUSS, CIESS (12-nov-2026)"
type: build_instruction
track: seminario / discusión pública (NO es producto RF)
version: v1
derives_from: BUILD-20261111-CEESP-BEAMER v1 (versión final revisada)
added_by: Cath
endorsed_by:
date: 2026-11-11
target: Claude Code (Dalila)
deadline: PDF y página de revisión hoy, 11-nov, antes de las 23:30; Héctor revisa a primera hora; conferencia el 12-nov a las 9:30
status: draft v1
---

# Instrucción de construcción: conferencia magistral RIUSS

## 0. Qué se hace

Conferencia magistral de apertura del Congreso de la Red Internacional de Investigación en Seguridad Social (RIUSS): **45 minutos de exposición y 15 de preguntas**. El público son investigadores y especialistas de las Américas; el congreso presenta 48 trabajos. La conferencia debe dar un marco regional para todo el día. Sin notas del orador.

**Base:** la presentación del CEESP del 11 de noviembre, en su versión final revisada (`.../foros_talleres/CEESP_2026-11-11/`). Copia todo a `.../foros_talleres/RIUSS_2026-11-12/` y no modifiques el original. Se conservan su tema, su estilo y su lógica.

**Cambios respecto a la base:**

1. **Demografía regional:** América Latina, no solo México.
2. **Pensiones:** bloque de avances y transformaciones de 25 años, tomado de la presentación de CEPAL (Santiago, mayo de 2026) y, donde sirva, de la presentación en Colombia.
3. **México se queda solo como ejemplo** en el bloque fiscal, rotulado así.
4. **Tiempo suficiente para nuestra propuesta de modelo.**
5. **El nacimiento de CONOSAFI**, en dos láminas.
6. **Una lámina breve sobre instrumentos de cuidados.**
7. Fuera: el detalle del presupuesto y del paquete 2027, el techo de deuda, la Modalidad 40 y el financiamiento privado como bloque propio (este último se integra a la lámina de instrumentos).

**Meta:** entre 30 y 33 láminas de exposición, más fuentes y apéndice. Si te pasas, mueve láminas al apéndice en el orden de la sección 5.

**Límites:**

- Sin vocabulario interno: nada de "RF", "G1–G5", "pilares" en el sentido del proyecto (sí "pilares" en el sentido de la arquitectura de pensiones), "OSF", "neteo", "DFD", "BDH", nombres de agentes ni rutas.
- Sin Modalidad 40.
- No inventar cifras. Toda cifra nueva debe tener fuente documentada en Dalila o venir de la sección 2. Si una lámina nueva no tiene sustento, se omite y se reporta.
- No buscar en la web.
- Fuentes en el pie siempre en forma pública (autor, institución, año).

## 1. Fuentes permitidas

Sigue vigente la autorización de usar material de otros proyectos (instrucción del CEESP, sección 1, con sus cautelas). Para esta presentación busca además:

- **Presentación de CEPAL** (XXXVIII Seminario Regional de Política Fiscal, Santiago, mayo de 2026): arquitectura de seguridad social para la región, sus dos ejes de reforma, las cifras regionales de cobertura y el impuesto negativo.
- **Presentación en Colombia:** búscala con `grep -ril` sobre "Colombia", "Bogotá", "Universidad de los Andes" o "Andes". Toma lo que sirva para pensiones o salud en la región. Si encuentras más de una, usa la más reciente y repórtalo.
- **Presentación CISS v2:** arquitectura multipilar ("el cero se habla con el uno, el dos con el tres") y el escalón de la trampa de formalización.
- **CONOSAFI:** busca "CONOSAFI" y los documentos de la Comunidad Latinoamericana del Conocimiento sobre Financiamiento de la Salud (presentación de la iniciativa, reunión de San José). Usa el nombre CONOSAFI con su nombre completo tal como aparezca en los documentos. Si "CONOSAFI" no aparece en Dalila, úsalo de todos modos, porque así lo nombró Héctor, y repórtalo.
- **Cuidados:** material sobre instrumentos de cuidados de largo plazo (seguros de ciclo de vida, seguros pagados durante la vida laboral que cubren en la vejez) en el material de seguridad social y salud o en la presentación de CEPAL.
- **Demografía regional:** WPP 2024 (agregado "Latin America and the Caribbean" y países) y CELADE, si están en el corpus.

**Cautela demográfica:** sigue abierta la discrepancia de TFR entre el archivo de línea base y CELADE 2025 para **Chile, Costa Rica y México**. No uses las TFR del archivo de línea base para ningún país. Usa WPP 2024 directamente; si citas CELADE para esos tres países, muestra ambas fuentes o ninguna.

## 2. Cifras nuevas verificadas (usar tal cual)

| Tema | Contenido | Fuente para el pie |
|---|---|---|
| Chile, reforma de 2025 | Ley 21.735, publicada el 26 de marzo de 2025. Nueva cotización del empleador de 7 % de la renta imponible, gradual (1 punto desde agosto de 2025; completa en 9 años, extensible a 11), que con el 1.5 % del seguro de invalidez y sobrevivencia suma 8.5 %: 4.5 % a ahorro individual y 4 % a un nuevo Seguro Social. La PGU sube a 250 mil pesos de forma escalonada por edad (septiembre de 2025 a septiembre de 2027) | Ley 21.735; Ministerio de Hacienda de Chile, 2025 |
| Colombia, reforma de 2024 | Ley 2381 de 2024: sistema de pilares. La Corte Constitucional declaró exequible la mayor parte de la reforma en agosto de 2026 y devolvió nueve artículos a la Cámara para subsanar vicios de trámite; entrada en vigor prevista para el 1 de abril de 2027 | Corte Constitucional de Colombia, 2026 |

Las demás fechas de la cronología de reformas (Chile 1981 y 2008, Argentina 2008, Bolivia 2010, México 1997 y 2020, retiros anticipados en Chile y Perú) se toman **solo** de las presentaciones de CEPAL, Colombia o CISS. Si alguna no está ahí, se omite.

## 3. Contenido por lámina

Clave de origen: **C** = CEESP final; **P** = CEPAL; **K** = CISS v2; **Co** = presentación en Colombia; **N** = nueva.

### Apertura

**1 — Portada** (N)
- Título: *La seguridad social en las Américas en el primer cuarto del siglo XXI*
- Subtítulo: *Avances, transformaciones y desafíos persistentes*
- Héctor Juan Villarreal Páez
- ITED · Escuela de Gobierno y Transformación Pública · Tecnológico de Monterrey
- CONOSAFI (con nombre completo)
- Conferencia magistral de apertura · Congreso de la Red Internacional de Investigación en Seguridad Social (RIUSS)
- CIESS, Auditorio Benito Coquet, Ciudad de México · 12 de noviembre de 2026

**2 — Tesis y ruta** (N)
- Tesis en una frase: *En 25 años la región amplió la cobertura como nunca; no resolvió cómo pagarla durante la transición demográfica.*
- Ruta: demografía, pensiones, salud y formalización, una propuesta, CONOSAFI.

### Demografía de la región (5–6 láminas)

**3 — América Latina: menores de 15 y mayores de 65** (C3, regionalizada)
- Mismo diseño, con el agregado regional de WPP 2024 (variante media). Marca el año del cruce.

**4 — La fecundidad cae más rápido de lo previsto** (C4, regionalizada)
- TFR de países seleccionados de la región, con la cautela de la sección 1. Mantén el argumento de Fernández-Villaverde: las proyecciones oficiales tienden a sobrestimar la fecundidad.

**5 — La ventana demográfica se cierra** (C5, regionalizada)
- Proporción de 15–64 años o razón de dependencia, región y dos o tres países.

**6 — Envejecer antes de ser ricos** (N; solo con fuente)
- Velocidad del envejecimiento (años para pasar de 10 % a 20 % de mayores de 65) en la región frente a Europa, o ingreso per cápita al llegar a cierto umbral de envejecimiento. Solo con fuente documentada; si no hay, omite la lámina.

**7 — También cambia la forma en que nos enfermamos** (C7)
- Regionalízala si hay fuente regional (GBD o IHME para la región). Si no, déjala como ejemplo mexicano, rotulada "Un ejemplo: México".

**8 — Esto ya no depende de nosotros. Lo que sigue, sí.** (C)

### Pensiones: 25 años (5 láminas)

**9 — Avances: la expansión no contributiva** (P)
- La cobertura de pensiones en la vejez, antes y ahora, con cifras regionales de la presentación de CEPAL. Mensaje: el gran avance del cuarto de siglo fue no contributivo.

**10 — Transformaciones: el péndulo de las reformas** (P, Co, N)
- Línea de tiempo horizontal de 1981 a 2027, con hitos solo de las fuentes indicadas en la sección 2.
- Mensaje: la región pasó de reformar parámetros, o de ir y venir entre modelos, a preguntarse por la arquitectura.

**11 — Chile 2025 y Colombia 2024: dos respuestas al mismo problema** (Co, N)
- Dos columnas con las cifras de la sección 2.
- Punto común: ambas combinan un componente solidario con ahorro individual y aumentan la contribución.
- Si la presentación en Colombia trae una lectura propia, úsala.

**12 — Lo que sigue pendiente en pensiones** (P)
- Suficiencia de la generación de cuentas individuales, cobertura contributiva estancada e informalidad. Cifras solo de la presentación de CEPAL.

**13 — Una arquitectura multipilar** (K, P)
- "El cero se habla con el uno, el dos con el tres."

### El espacio fiscal: un ejemplo, México (3 láminas)

Rotula el bloque y cada lámina con "Un ejemplo: México".

**14 — ¿Cuánto queda para decidir?** (C10, Contabilidad de la muerte, enero–septiembre)

**15 — La brecha en salud** (C12)

**16 — Las pensiones le quitan espacio a la salud** (C13)
- Mensaje regional en la banda: *En toda la región, cada punto adicional en pensiones compite con la salud.*

### Salud y formalización (5 láminas)

**17 — ¿Financiar todo con impuestos generales?** (C14)
- Regionaliza la comparación de capacidad tributaria si la presentación de CEPAL trae cifras regionales. Si no, déjala con México.

**18 — Dos sistemas y el gasto de bolsillo** (C16)
- Rotúlala "Un ejemplo: México", salvo que haya cifras regionales de gasto de bolsillo con fuente.

**19 — El dilema Gruber** (C17)

**20 — El costo de formalizarse** (C18; ya es regional, Banco Mundial)

**21 — El escalón** (K o C21)
- La trampa de formalización, una sola lámina.

### Nuestra propuesta (6 láminas)

Este bloque necesita tiempo. No lo recortes para ganar espacio en otros.

**22 — Bismarck, Beveridge y nuestra propuesta** (C24)

**23 — Cómo funcionaría** (C25)
- Con la banda que quedó en el CEESP.

**24 — Qué mueve la decisión de formalizarse** (C22)
- El resultado principal del modelo de formalización, en una sola lámina. Las cautelas sobre las cifras del trabajo para el IMSS son las mismas que en el CEESP. Usa solo las cifras que Héctor aprobó ahí.

**25 — Consolidar transferencias: un impuesto negativo** (C27 y P, segundo eje)

**26 — Nuevos instrumentos para financiar la salud** (P, primer eje, y C30–31)
- Cuotas rediseñadas, primas graduadas según el ingreso, seguros de ciclo de vida y prepago en lugar de gasto de bolsillo. Aquí se integra lo esencial del financiamiento privado del CEESP.

**27 — Cuidados: el siguiente instrumento** (N, breve)
- Una sola lámina. Plantea que la demanda de cuidados de largo plazo crece con el envejecimiento y que hay instrumentos posibles: seguros pagados durante la vida laboral que cubren en la vejez, y la complementariedad entre lo público y lo privado.
- Contenido tomado del material de Dalila. Si no hay, usa solo lo que dice la base ("seguros de largo plazo que se paguen durante la vida laboral y cubran en la vejez") y plantéalo como pregunta.
- Sin cifras nuevas salvo con fuente.

**28 — Dos preguntas para cualquier propuesta** (C32)

### CONOSAFI (2 láminas)

**29 — El nacimiento de CONOSAFI** (C34, ampliada)
- Por qué nace: la región discutió mucho cómo ampliar la cobertura y poco cómo pagarla en los próximos veinte o treinta años.
- Quién la funda: Tecnológico de Monterrey (coordinación, Héctor Villarreal), Universidad de los Andes (Ramiro Guerrero) y Pontificia Universidad Católica de Chile (Pablo Celhay).
- Cuándo: anunciada en el Seminario de CEPAL (mayo de 2026), con primera reunión de trabajo en San José, Costa Rica, del 5 al 7 de octubre de 2026.
- Lo que salió de San José: usa la línea que Héctor escribió en la revisión del CEESP. Si quedó vacía, deja `[TEXTO DE HÉCTOR]` en rojo.
- Horizonte de al menos cinco años y tres trabajos en curso.

**30 — Una agenda para la RIUSS** (C, preguntas abiertas, ampliada)
- Las cuatro preguntas abiertas de la base (gasto de bolsillo a prepago, reglas para el financiamiento privado, detección temprana, espacio que dejan las pensiones a la salud), más una sobre cuidados.
- Cierra con una invitación: *Buscamos investigadores y datos comparables en la región.* Es una invitación natural a los participantes del congreso.

### Cierre

**31 — Cierre** (C35)
- Misma pregunta final de la base, adaptada a la región: *¿Podemos diseñar sistemas de protección social que la gente valore lo suficiente para querer participar, y que nuestros países puedan pagar durante su transición demográfica?*

**32–33 — Fuentes**, actualizadas, en forma pública.

### Apéndice (para preguntas)

- **A1** — La cuota fija pesa más donde menos se gana (C19)
- **A2** — Infonavit: la propuesta (C23)
- **A3** — El IMSS como sistema nacional de seguros de salud (C26)
- **A4** — ¿De dónde saldría el 6 % del PIB? (C28)
- **A5** — Salud en el presupuesto 2027 (C15)

## 4. Metadatos y limpieza

- Con `pikepdf`: Title = título de la portada; Author = "Héctor Juan Villarreal Páez". Eliminar Creator, Producer, rutas y demás metadatos.
- Nombre del archivo final: `Villarreal_RIUSS_2026-11-12.pdf`.

## 5. Si te pasas de 33 láminas

Mueve al apéndice, en este orden: 18, 17, 7, 6, 12. Nunca recortes el bloque de la propuesta (22–28) ni el de CONOSAFI (29–30).

## 6. Verificación antes de entregar

1. Compilar dos veces sin errores.
2. Revisión visual con `pdftoppm -r 150` de todas las láminas nuevas y adaptadas.
3. `pdftotext` y búsqueda de: vocabulario interno de la sección 0, "Modalidad 40", "CEESP", "PPEF", "sesión anterior", "Villareal". Todo vacío, salvo "PPEF" en una fuente histórica.
4. Página de revisión, como las anteriores, con:
   - láminas en miniatura con su origen (C, P, K, Co, N);
   - láminas omitidas o movidas al apéndice, y por qué;
   - qué presentación de Colombia se usó y qué se tomó de ella;
   - cómo aparece CONOSAFI en Dalila (nombre completo y documento);
   - toda cifra demográfica de Chile, Costa Rica o México, con su fuente;
   - hitos de la línea de tiempo de la lámina 10, cada uno con su fuente local.
5. Commit citando `BUILD-20261112-RIUSS-BEAMER v1`.

## 7. Retención

Archivar en `_crossrefs/_build_instructions/` junto a la cadena del CEESP, conforme a PROTO-RAG-001. `endorsed_by` queda vacío hasta revisión.

---
id: BUILD-20261022-EXATEC-BEAMER
title: "Build instruction — Beamer, 3er Encuentro EXATEC, conferencia «Implicaciones y retos del PEF 2027» (22-oct-2026)"
type: build_instruction
track: seminario / discusión pública (NO es producto RF)
version: v1
derives_from: BUILD-20261022-SOBREMEXICO-BEAMER v2
added_by: Cath
endorsed_by:
date: 2026-10-21
target: Claude Code (Dalila)
priority: después de cerrar SobreMéxico v2 (mesa a las 11:15)
deadline: PDF para revisión de Héctor hoy, 21-oct, idealmente antes de medianoche; límite duro 22-oct a las 14:00; conferencia a las 18:40
status: draft v1
---

# Instrucción de construcción: conferencia EXATEC, 15 láminas

## 0. Qué se hace

Una conferencia de 30 minutos para egresados de la Escuela de Gobierno y Transformación Pública. Se construye a partir de la presentación de SobreMéxico **ya corregida conforme a la v2**: las láminas 2 a 9 de SobreMéxico se reutilizan y se añaden siete láminas nuevas. Total: **15 láminas**, portada incluida. Sin notas del orador.

Estructura en dos partes de peso similar:

- **Implicaciones del PEF 2027** (láminas 2–8): el diagnóstico de SobreMéxico.
- **Retos: cuatro frentes** (láminas 9–15): un frente por lámina, cada uno anclado en algo aprobado o publicado este mes, y un cierre sobre la regla fiscal.

**Límites:**

- Sin vocabulario interno: nada de "RF", "G1–G4", "pilares", "OSF", "neteo", nombres de agentes ni rutas.
- **Sin atribución institucional en el tema Modalidad 40.** Ni en las láminas 12–13 ni en ninguna otra deben aparecer "ITED", "Iniciativa para la Transición Económica y Demográfica" ni frases como "hemos propuesto". El análisis va en voz propia del ponente.
- No inventar cifras. Las cifras nuevas están en la sección 2, ya verificadas. Para las cifras marcadas como *opcionales*: si no están en el material local con fuente documentada, **se omiten** (no se pone marcador rojo) y se reporta la omisión.
- No buscar en la web.

## 1. Punto de partida en Dalila

1. Primero termina SobreMéxico v2. Esta presentación depende de su versión corregida.
2. Copia la carpeta corregida a `.../foros_talleres/EXATEC_2026-10-22/`. No modifiques la de SobreMéxico.
3. Mismo tema, paleta, tipografía y macros (`\frente`, `\punto`, `\fuente`). Las láminas nuevas usan el mismo estilo de cajas de las láminas 4, 5 y 9.

## 2. Cifras nuevas (verificadas; usar tal cual)

| Cifra | Valor | Fuente para el pie |
|---|---|---|
| Ley catastral | Ley General para el Fortalecimiento y Armonización Catastral y Registral; aprobada por el Senado el 14 de octubre de 2026 (69 votos a favor, 32 en contra), tras su aprobación en la Cámara de Diputados | Senado de la República, 14 de octubre de 2026 |
| Contenido de la ley catastral | Catastros y registros digitalizados y armonizados con modelos técnicos comunes; actualización de valores "de forma progresiva y técnica"; los municipios conservan la decisión sobre sus contribuciones | Ídem |
| Modalidad 40: antes | Cualquier salario de cotización de hasta 25 UMA (casi 3 mil pesos diarios), sin relación con el salario previo; se permitían inscripciones con fecha anterior | Acuerdo ACDO.AS2.HCT.101026/302.P.DG, DOF, 21 de octubre de 2026 |
| Modalidad 40: ahora | El último salario registrado, o ese salario más una UMA (unos 117 pesos diarios), nunca por debajo del mínimo; sin inscripciones retroactivas; trámite solo digital; los inscritos conservan sus condiciones hasta terminar su periodo | Ídem |
| Modalidad 40: plazos | Medida temporal: el IMSS tiene seis meses para estimar el costo y otros seis para proponer cambios a las normas | Ídem |
| Modalidad 40: mecanismo | Pensiones de quienes cotizaron antes de julio de 1997: salario promedio de los últimos cinco años; la estrategia permitía pensiones vitalicias que pueden superar 80 mil pesos al mes; la diferencia entre cuotas y pensión la cubre el Gobierno Federal | Ídem, y Ley del Seguro Social de 1973 |
| Pemex: techos de deuda propios | Endeudamiento neto interno hasta 160,619.5 mdp y externo hasta 5,259.4 mdd, condicionado a la meta de balance financiero | LIF 2027, art. 4o, dictamen de la Cámara de Diputados |
| CFE: techos de deuda propios | Interno hasta 16,742 mdp; externo hasta 725 mdd | Ídem |
| Techo del Gobierno Federal | Endeudamiento neto interno hasta 1.7 billones de pesos más externo hasta 13,500 mdd, compensables entre sí; ≈ 1.94 billones ≈ 4.9 % del PIB | LIF 2027, art. 2o; % del PIB con el PIB de SHCP |
| Endeudamiento programado del Gobierno Federal | 1.57 billones de pesos ≈ 4.0 % del PIB | LIF 2027, art. 1o, numeral 0 |
| Meta de RFSP | 3.9 % del PIB | SHCP, CGPE 2027 |
| Tope a deducciones | 96.67 % de los ingresos acumulables, empresas con ingresos > 50 mdp; equivale a un ISR mínimo de ≈ 1 % de los ingresos | Minuta LISR, Cámara de Diputados |

Cifras **opcionales** (solo con fuente documentada en Dalila; si no, se omiten):

- Gastos fiscales como % del PIB (SHCP, *Renuncias recaudatorias*), lámina 10.
- Proporción de empresas que usa el crédito de un impuesto mínimo acreditable (evidencia de Pakistán, ≈ 1.3 %), lámina 10. Si no hay fuente, se deja la idea sin el número.
- Recaudación de predial como % del PIB, México frente a América Latina u OCDE, lámina 11.
- Apoyos a Pemex como % del PIB, lámina 14: tomarlo de la nota de la cascada (0.7, actualización 2026), que ya está en la lámina 3.

## 3. Contenido por lámina

**Lámina 1 — Portada**
- Título: *Implicaciones y retos del PEF 2027*
- Subtítulo: *Contabilidad de la muerte y cuatro frentes de reforma*
- Ponente: Héctor Juan Villarreal Páez
- Afiliación: Escuela de Gobierno y Transformación Pública, Tecnológico de Monterrey (solo esta; ver sección 0)
- Evento: 3er Encuentro EXATEC · Escuela de Gobierno y Transformación Pública
- Lugar y fecha: Teatro de Decisiones, Sede Mixcoac · 22 de octubre de 2026
- Sin logos.

**Láminas 2–8 — Implicaciones** (de SobreMéxico v2, en el mismo orden y sin cambios de contenido)
- 2 El gasto ya supera al ingreso (SobreMéxico 2)
- 3 De cada peso, casi todo ya tiene dueño (SobreMéxico 3)
- 4 Todo compite por la Bolsa (SobreMéxico 4)
- 5 La deuda ya cuesta tanto como el margen de decisión (SobreMéxico 5, versión v2)
- 6 El paquete 2027 mueve la base en el margen (SobreMéxico 6)
- 7 Una reforma pequeña no basta (SobreMéxico 7)
- 8 Sin reforma, la Bolsa se encoge cada año (SobreMéxico 8)

En las láminas que dicen "PEF 2027" o "PPEF 2027", deja "PPEF 2027": el Presupuesto aún no se aprueba (plazo: 15 de noviembre).

**Lámina 9 — Cuatro frentes** (SobreMéxico 9 sin la banda de cierre)
- Título: *Cuatro frentes de reforma*
- Los cuatro bloques como están. Debajo, una línea pequeña: "Cada uno ya se movió este mes, pero en el margen."

**Lámina 10 — Frente federal: el impuesto mínimo ya llegó**
- Título: *El paquete ya trae un impuesto mínimo; el diseño importa más que el nombre*
- Tres puntos:
  1. El tope a deducciones de 96.67 % equivale a un ISR mínimo de alrededor de 1 % de los ingresos para empresas con ingresos mayores a 50 mdp.
  2. Un impuesto de *t* sobre ingresos equivale a un piso de margen de *t*/τ: con 1 % y una tasa de 30 %, el piso es 3.33 %. Las empresas con márgenes legítimamente bajos pagan de más.
  3. Un mínimo "acreditable" tiende a volverse definitivo en la práctica: casi ninguna empresa recupera el crédito. (Con el ≈ 1.3 % de Pakistán solo si hay fuente.)
- Banda inferior: *Lo pendiente en el frente federal: los gastos fiscales* (con la cifra opcional, si existe).

**Lámina 11 — Frente local: predial y catastro**
- Título: *Sin catastro no hay predial; la nueva ley crea la condición, no el ingreso*
- Contenido: qué hace la ley (tabla de la sección 2) en dos o tres líneas; la cifra opcional de predial, si existe.
- Mensaje: el ingreso depende de que estados y municipios actualicen valores y cobren. La ley es necesaria pero no suficiente.
- Registro técnico: no usar la palabra "predialazo".

**Lámina 12 — Seguridad social (I): Modalidad 40**
- Título: *Modalidad 40: lo que cambió el 21 de octubre*
- Dos columnas, estilo de la lámina 6: **Hasta el 21 de octubre** frente a **Desde el 22 de octubre**, con el contenido de la tabla de la sección 2.
- Pie: el acuerdo del DOF.

**Lámina 13 — Seguridad social (II): quién paga**
- Título: *Seguir cotizando es razonable; comprar una pensión no lo es*
- Columna izquierda, **Quién paga**: el promedio de los últimos cinco años abría la puerta a pensiones vitalicias de más de 80 mil pesos al mes; las cuotas no alcanzan y la diferencia la paga el Gobierno Federal, es decir, todos los contribuyentes, incluidos quienes nunca tendrán pensión; la estrategia solo está al alcance de quien puede adelantar cientos de miles de pesos.
- Columna derecha, **Lo que falta**: es una medida temporal (6 + 6 meses); el análisis de costo debe hacerse público; la solución definitiva necesita base legal firme, porque un acuerdo invita a los amparos; debe respetarse a quien ya cotiza.
- Sin cifras de costo: nadie ha publicado una.

**Lámina 14 — Empresas del Estado**
- Título: *Pemex: un costo repartido y fuera de la vista*
- Cuatro piezas del costo, en cajas pequeñas: transferencias y apoyos del presupuesto (0.7 % del PIB en la actualización 2026, si se toma de la cascada); deuda propia autorizada en la LIF 2027 (techos de Pemex y CFE, sección 2); pasivos contingentes que no aparecen en el presupuesto.
- Mensaje: *Ningún documento presupuestario muestra el costo completo; el primer paso es registrarlo.*

**Lámina 15 — Regla fiscal y cierre**
- Título: *La regla fiscal no ancla: el techo de deuda está un punto arriba de la meta*
- Gráfica de tres barras horizontales en % del PIB, con "LIF 2027" o "CGPE 2027" en cada etiqueta: techo autorizado al Gobierno Federal 4.9; endeudamiento programado del Gobierno Federal 4.0; meta de RFSP 3.9.
- Pie obligatorio: "Perímetros distintos: el techo y el programado son del Gobierno Federal; los RFSP consolidan el sector público. La comparación muestra holgura, no incumplimiento. % del PIB con el PIB de SHCP."
- Banda de cierre: *Ninguno de los cuatro frentes cierra la cuenta solo, y la reforma de ingresos necesita una regla que la ancle. Ordenar las finanzas exige decisiones poco visibles, técnicas y a veces impopulares.*

## 4. Metadatos y limpieza

- Con `pikepdf`: Title = "Implicaciones y retos del PEF 2027"; Author = "Héctor Juan Villarreal Páez". Eliminar Creator, Producer, rutas y demás metadatos.
- Nombre del archivo final: `Villarreal_EXATEC_2026-10-22.pdf`.

## 5. Verificación antes de entregar

1. Compilar dos veces sin errores. Confirmar exactamente 15 páginas.
2. Revisión visual con `pdftoppm -r 150` de todas las láminas, con atención especial a las nuevas (1 y 9–15).
3. `pdftotext` y búsqueda de: vocabulario interno de la sección 0, "ITED", "Iniciativa para la Transición", "SobreMéxico", "Iberoamericana", "Naranja", "Villareal", "predialazo". Todo vacío.
4. Publicar una página de revisión como la de SobreMéxico: láminas en miniatura, estado de cada una (nueva, reutilizada) y lista de cifras opcionales usadas u omitidas, con su fuente local.
5. Commit citando `BUILD-20261022-EXATEC-BEAMER v1`.

## 6. Retención

Archivar en `_crossrefs/_build_instructions/` junto a la cadena 13-oct → SobreMéxico v1 → SobreMéxico v2, conforme a PROTO-RAG-001. `endorsed_by` queda vacío hasta revisión.

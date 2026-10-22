---
id: BUILD-20261022-SOBREMEXICO-BEAMER
title: "Build instruction — Beamer, Mesa de discusión 1, Congreso SobreMéxico 2026 (22-oct-2026)"
type: build_instruction
track: seminario / discusión pública (NO es producto RF)
supersedes: none
derives_from: BUILD-20261013-FORO-HACENDARIO-BEAMER
added_by: Cath
endorsed_by:
date: 2026-10-21
target: Claude Code (Dalila)
deadline: PDF listo para revisión de Héctor hoy, 21-oct, antes de las 22:00; mesa el 22-oct a las 11:15
status: draft v1
---

# Instrucción de construcción: ampliar la presentación del 13 de octubre a 9 láminas

## 0. Qué se hace

Se reutiliza la presentación Beamer del foro del 13 de octubre (*Contabilidad de la muerte: por qué una reforma fiscal pequeña no basta*) y se amplía de 6 a **9 láminas**, portada incluida, para la Mesa de discusión 1 del Congreso SobreMéxico 2026. Sin notas del orador.

Los cambios respecto de la versión anterior:

1. Portada nueva (otro evento, otro organizador).
2. Lámina del punto de partida actualizada con la Ley de Ingresos ya aprobada por la Cámara de Diputados.
3. Tres láminas nuevas: el costo de la deuda frente a la Bolsa; lo que aprobó el Congreso en el paquete 2027; el horizonte de mediano y largo plazo.
4. Las láminas de Contabilidad de la muerte, Todo compite por la Bolsa, Una reforma pequeña no basta y Cuatro frentes se conservan como están.

El público es académico (congreso de economía de la IBERO). El registro puede ser algo más técnico que en el foro, pero sigue siendo una exposición, no un seminario: una idea por lámina.

**Límites que se mantienen:**

- Sin vocabulario interno: nada de "RF", "G1–G4", "pilares", "OSF", "neteo", "Bolsa" con mayúscula como término de proyecto fuera de su definición en la lámina, nombres de agentes ni rutas de archivos.
- No inventar cifras. Las cifras nuevas de esta versión vienen en la tabla de la sección 2, ya verificadas; úsalas tal cual. Cualquier otra cifra sale del material local o queda como `[CIFRA PENDIENTE]` en rojo.
- No buscar en la web.

## 1. Punto de partida en Dalila

1. Localiza la fuente de la presentación del 13 de octubre: el `.tex` y la carpeta de gráficas que produjeron `Villarreal_ForoPoliticaHacendaria_2026-10-13.pdf` (busca por nombre de archivo o por `grep -ril "Contabilidad de la muerte"` bajo `~/Dalila/`).
2. **Copia** todo a una carpeta nueva (`.../SobreMexico_2026-10-22/`). No modifiques el original.
3. Conserva tema, paleta, tipografía y gráficas existentes. La restricción de no usar naranja ya no es necesaria, pero no cambies la paleta: la identidad visual se mantiene.

## 2. Cifras nuevas (verificadas; usar tal cual)

| Cifra | Valor | Etiqueta de año | Fuente para el pie |
|---|---|---|---|
| Ingresos presupuestarios | 9.16 billones de pesos (23.2% del PIB) | LIF 2027 | Fuente: dictamen LIF 2027, Cámara de Diputados |
| Ingresos totales LIF (incluye financiamiento) | 10.64 billones de pesos | LIF 2027 | Ídem |
| RFSP | 3.9% del PIB | Paquete Económico 2027 | Fuente: SHCP, CGPE 2027 |
| Saldo histórico de los RFSP | 55% del PIB | Paquete Económico 2027 | Fuente: SHCP, CGPE 2027 |
| Costo financiero de la deuda | 4.0% del PIB | PPEF 2027 | Fuente: CIEP con datos de SHCP |
| Inversión pública | 1.13 billones de pesos (2.9% del PIB) | PPEF 2027 | Fuente: CIEP con datos de SHCP |
| Pensiones | 2.5 billones de pesos (6.3% del PIB) | PPEF 2027 | Fuente: CIEP con datos de SHCP |
| Límite a deducciones (ISR) | Deducciones topadas en 96.67% de los ingresos acumulables, empresas con ingresos > 50 mdp | Minuta LISR 2027 | Fuente: minuta de reforma a la LISR, Cámara de Diputados |
| Pérdidas fiscales | Amortización limitada a 50% de la utilidad fiscal del ejercicio | Minuta LISR 2027 | Ídem |
| Programa de regularización | 100% de condonación de multas, recargos y gastos de ejecución; la Cámara eliminó el tope de 300 mdp de ingresos y la exclusión de grandes contribuyentes | LIF 2027, transitorio vigésimo primero | Fuente: dictamen y reserva aprobada, Cámara de Diputados |

Nota de denominador: las razones al PIB de SHCP y CIEP usan el PIB nominal 2027 de Hacienda (≈ 39.5 billones). En las láminas 2 y 5 agrega al pie: "Razones calculadas con el PIB de SHCP; con un PIB más conservador serían algo mayores."

## 3. Contenido por lámina

**Lámina 1 — Portada**
- Título: *Contabilidad de la muerte: por qué una reforma fiscal pequeña no basta*
- Evento: Congreso SobreMéxico 2026
- Mesa: Mesa de discusión 1 · Repensando las finanzas públicas: una perspectiva de mediano y largo plazo
- Organiza: Departamento de Economía, Universidad Iberoamericana
- Ponente: Héctor Juan Villarreal Páez (con doble "r"; el programa lo escribe mal, no copiar de ahí)
- Afiliación: Escuela de Gobierno y Transformación Pública, Tecnológico de Monterrey
- Lugar y fecha: Auditorio Ernesto Meneses, Universidad Iberoamericana · 22 de octubre de 2026
- Sin logos salvo que Héctor los proporcione.
- Elimina toda referencia al foro anterior y a sus organizadores.

**Lámina 2 — El punto de partida** (actualizar la existente)
- Mantén la gráfica de ingresos frente a gasto, pero cambia la etiqueta a "LIF 2027 aprobada por la Cámara de Diputados" y usa 9.16 billones de ingresos presupuestarios.
- Añade, en texto pequeño bajo la gráfica: "RFSP 3.9% del PIB · Deuda amplia 55% del PIB".
- Mensaje (título): *El gasto ya supera al ingreso, y la diferencia se financia con deuda.*

**Lámina 3 — Contabilidad de la muerte** (sin cambios)

**Lámina 4 — Todo compite por la Bolsa** (sin cambios)

**Lámina 5 — La deuda ya compite por la Bolsa** (nueva)
- Gráfica de tres barras horizontales, en % del PIB, cada una con su año en la etiqueta:
  1. Bolsa de gasto discrecional (actualización 2026): 4.0
  2. Costo financiero de la deuda (PPEF 2027): 4.0
  3. Inversión pública (PPEF 2027): 2.9
- Mensaje (título): *Pagar intereses ya cuesta lo mismo que todo el margen de decisión.*
- Pie: aclarar que los años difieren ("Bolsa: actualización 2026; costo financiero e inversión: PPEF 2027") y la nota de denominador.

**Lámina 6 — Lo que se aprobó para 2027** (nueva)
- Dos columnas, sin gráfica:
  - **Amplía la base (en el margen):** límite a deducciones en 96.67% de los ingresos para empresas con ingresos mayores a 50 mdp, que equivale a un mínimo de alrededor de 1% de los ingresos; pérdidas fiscales limitadas a 50% de la utilidad.
  - **Abarata el incumplimiento:** programa de regularización con condonación total de multas y recargos, ampliado a grandes contribuyentes.
- Mensaje (título): *El paquete 2027 mueve la base en el margen; no cambia la restricción.*
- Etiqueta de estado, en el pie: "Minutas aprobadas por la Cámara de Diputados en octubre de 2026."
- Registro analítico, no de denuncia. Sin adjetivos.

**Lámina 7 — Una reforma pequeña no basta** (sin cambios)

**Lámina 8 — El tiempo juega en contra** (nueva; responde al "mediano y largo plazo" de la mesa)
- Mensaje (título): *Sin reforma, la Bolsa se encoge cada año.*
- Contenido preferente: una gráfica de trayectoria del gasto en pensiones como % del PIB a 2035 o más allá, tomada del material local de pensiones o de las proyecciones demográfico-fiscales en Dalila. Punto de anclaje 2027: 6.3% del PIB (CIEP).
- Si no encuentras una proyección local con fuente documentada, no la construyas. En su lugar, haz un diagrama sin cifras: la Bolsa al centro y tres presiones que la comprimen (pensiones contributivas de la generación de transición; pensión no contributiva con rango constitucional; costo financiero de la deuda). Solo el 6.3% de 2027 lleva número. Repórtalo en el informe final.

**Lámina 9 — Cuatro frentes y una decisión** (sin cambios en los bloques)
- Banda de cierre ligeramente ajustada a la mesa: *Ninguno de los cuatro frentes cierra la cuenta por sí solo. Pensar a mediano plazo es decidir ahora el replanteamiento integral.*

## 4. Metadatos y limpieza

- Con `pikepdf`: Title = título de la portada; Author = "Héctor Juan Villarreal Páez". Eliminar Creator, Producer, rutas locales y cualquier otro metadato.
- Nombre del archivo final: `Villarreal_SobreMexico_2026-10-22.pdf`.

## 5. Verificación antes de entregar

1. Compilar dos veces sin errores.
2. Confirmar que el PDF tiene exactamente 9 páginas.
3. Renderizar cada lámina con `pdftoppm -r 150` y revisar visualmente: nada desbordado, gráficas legibles, años y fuentes visibles en cada gráfica.
4. `pdftotext` del PDF y buscar: "Naranja", "Pensando en México", "13 de octubre", "Villareal" (con una sola r) y el vocabulario interno de la sección 0. Todo debe salir vacío.
5. Reportar a Héctor: ruta del PDF; qué láminas cambiaron; qué ruta se tomó en la lámina 8 (proyección o diagrama) y con qué fuente; lista de `[CIFRA PENDIENTE]`, si los hay.

## 6. Retención

Esta instrucción se conserva como provenance en `_crossrefs/_build_instructions/`, conforme a PROTO-RAG-001, junto a la del 13 de octubre de la que deriva. `endorsed_by` queda vacío hasta revisión.

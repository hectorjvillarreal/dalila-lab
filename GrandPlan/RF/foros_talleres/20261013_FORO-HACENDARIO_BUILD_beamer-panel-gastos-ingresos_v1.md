---
id: BUILD-20261013-FORO-HACENDARIO-BEAMER
title: "Build instruction — Beamer, Panel Gastos e Ingresos (Foro Política hacendaria, 13-oct-2026)"
type: build_instruction
track: seminario / discusión pública (NO es producto RF)
added_by: Cath
endorsed_by:
date: 2026-10-13
target: Claude Code (Dalila)
deadline: PDF listo para revisión de Héctor a las 15:00; panel a las 16:00
status: draft v1
---

# Instrucción de construcción: presentación Beamer, 6 láminas

## 0. Contexto y límites

Héctor presenta hoy a las 16:00 en un panel de ~15 minutos. La presentación usa el ejercicio **Contabilidad de la muerte** para sostener una tesis: **una reforma fiscal pequeña no basta**. Máximo **6 láminas en total, portada incluida**. Sin notas del orador.

Es una intervención pública, no un producto del proyecto RF. Por lo tanto:

- No usar vocabulario interno: nada de "RF", "G1–G4", "pilares", "OSF", "neteo", nombres de agentes ni rutas de archivos.
- El foro lo coorganiza un partido político. Registro técnico y no partidista. **No usar naranja** como color de acento.
- No inventar cifras. Si una cifra no está en las fuentes locales, dejar el marcador visible `[CIFRA PENDIENTE]` en rojo y reportarlo al final. No buscar cifras en la web.

## 1. Fuentes en Dalila

1. **Documento Contabilidad de la muerte (actualización 2026).** Buscar bajo `~/Dalila/GrandPlan/RF/` (por ejemplo `grep -ril "contabilidad de la muerte"`). De ahí salen todos los componentes de la cascada y la Bolsa (4.0% del PIB, denominador PIB 36,500 mmdp).
2. **Gráficas CIEP sobre las implicaciones del Paquete Económico 2027.** Localizarlas en Dalila. Si no aparecen, preguntar a Héctor de inmediato; no esperar al final.
3. Cifras del foro (vienen de los organizadores): ingresos 2027 de 9.2 billones de pesos y gasto de 10.6 billones. Contrastarlas con el material CIEP del paquete 2027 si está disponible. Si difieren, usar la cifra CIEP y reportar la diferencia.

## 2. Especificaciones técnicas

- `\documentclass[aspectratio=169]{beamer}`, `babel` en español, UTF-8.
- Tema sobrio: `metropolis` si está instalado; si no, tema por defecto con paleta neutra (gris oscuro y azul petróleo, por ejemplo). Sin símbolos de navegación. Número de lámina discreto.
- Una idea por lámina, texto mínimo (máximo ~25 palabras de cuerpo por lámina, sin contar gráficas y fuentes). Tipografía grande y legible a distancia.
- **Cada gráfica lleva el año en su etiqueta** (ej. "Actualización 2026", "Paquete Económico 2027") y **una línea de fuente** en el pie ("Fuente: CIEP con datos de SHCP", "Fuente: elaboración propia con datos de SHCP").
- Gráficas propias en matplotlib, exportadas en PDF vectorial, misma paleta que el tema.

## 3. Contenido por lámina

**Lámina 1 — Portada**
- Título: *Contabilidad de la muerte: por qué una reforma fiscal pequeña no basta*
- Evento: Foro "Política hacendaria: los límites del presente y las posibilidades del futuro"
- Mesa: Panel Gastos e Ingresos
- Organizan: Pensando en México · La Fuerza Naranja
- Ponente: Héctor Juan Villarreal Páez
- Afiliación: Escuela de Gobierno y Transformación Pública, Tecnológico de Monterrey (Héctor puede ajustar)
- Fecha: 13 de octubre de 2026
- Logos: solo si Héctor proporciona los archivos. No descargarlos de la web. Sin logos, los nombres en texto bastan.

**Lámina 2 — El punto de partida**
- Mensaje: en 2027 el gasto supera a los ingresos por ~1.4 billones de pesos.
- Gráfica: la de CIEP sobre el paquete 2027 que mejor muestre ingresos frente a gasto. Si no hay una adecuada, dos barras simples (9.2 frente a 10.6 billones), etiquetadas "Paquete Económico 2027".

**Lámina 3 — Contabilidad de la muerte** (lámina central)
- Gráfica de cascada (*waterfall*) en % del PIB: ingresos totales → menos Pemex (neutralización vía FMP) → menos costo financiero de la deuda → menos participaciones → menos pensiones contributivas → menos gasto propio de IMSS, ISSSTE y CFE → **Bolsa = 4.0% del PIB**.
- Valores exactos tomados del documento fuente; no redondear distinto de como aparecen ahí.
- La barra final (la Bolsa) resaltada con color de acento.
- Nota al pie: "Supuestos generosos con la SHCP (PIB nominal 2026 de 36,500 mmdp); la bolsa real probablemente es menor. Actualización 2026."
- Título de la lámina como mensaje: *De cada peso, casi todo ya tiene dueño.*

**Lámina 4 — Todo compite por la Bolsa**
- Mensaje: salud, educación, seguridad, infraestructura, agua, ciencia y tecnología, y la inversión pública salen de esos ~4 puntos del PIB. Recomponer el gasto es repartir la escasez.
- Gráfica: la de CIEP sobre salud o inversión pública del paquete 2027 que mejor lo ilustre. Si no hay, un diagrama simple: un bloque de 4.0% del PIB con las funciones listadas dentro.

**Lámina 5 — Una reforma pequeña no basta**
- Gráfica de dos barras: (a) lo que rinde una reforma fiscal clásica, **"del orden de 1.5 puntos del PIB"**, sin atribuir a ningún reporte; (b) la brecha de recaudación de México frente al promedio de América Latina, según *Revenue Statistics in Latin America and the Caribbean* (OCDE/CEPAL/CIAT/BID). Tomar la cifra del material local; si no está, `[CIFRA PENDIENTE]`.
- Mensaje: la reforma clásica cubre menos de la mitad de la brecha.

**Lámina 6 — Cuatro frentes y una decisión**
- Cuatro bloques con una línea cada uno, centrada en el problema que resuelven, no en cuánto recaudan:
  1. **Reforma fiscal clásica (federal):** bases gravables, gastos fiscales, IVA, ISR.
  2. **Haciendas locales:** ingresos propios de estados y municipios (predial, tenencia moderna) y financiamiento de sus funciones.
  3. **Seguridad social:** pensiones y salud con financiamiento sostenible e inclusión de trabajadores informales.
  4. **Empresas del Estado:** pasivos contingentes de Pemex y CFE fuera del presupuesto corriente.
- Banda inferior con el mensaje de cierre: *La decisión no es una medida, es un replanteamiento integral: ninguno de los cuatro frentes cierra la cuenta por sí solo.*

## 4. Metadatos y limpieza

- Con `pikepdf`: Title = título de la portada; Author = "Héctor Juan Villarreal Páez". Eliminar Creator, Producer, rutas locales y cualquier otro metadato.
- Nombre del archivo final: `Villarreal_ForoPoliticaHacendaria_2026-10-13.pdf`.

## 5. Verificación antes de entregar

1. Compilar dos veces sin errores.
2. Confirmar que el PDF tiene exactamente 6 páginas.
3. Renderizar cada lámina con `pdftoppm -r 150` y revisar visualmente: nada desbordado, gráficas legibles, fuentes y años visibles en cada gráfica.
4. Buscar en el texto del PDF (`pdftotext`) cualquier vocabulario interno de la lista de la sección 0; debe salir vacío.
5. Reportar a Héctor: ruta del PDF, tabla de cada cifra usada con su fuente local (archivo y página o línea), y lista de `[CIFRA PENDIENTE]`, si los hay.

## 6. Retención

Esta instrucción se conserva como provenance en `_crossrefs/_build_instructions/`, conforme a PROTO-RAG-001. `endorsed_by` queda vacío hasta revisión.

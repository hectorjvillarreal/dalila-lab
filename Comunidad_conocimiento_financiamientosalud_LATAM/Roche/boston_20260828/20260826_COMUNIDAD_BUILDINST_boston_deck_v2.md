---
doc_id: 20260826_COMUNIDAD_BUILDINST_boston_deck_v2
project: COMUNIDAD
doctype: BUILDINST
slug: boston_deck
version: 2
supersedes: 20260826_COMUNIDAD_BUILDINST_boston_deck_v1
date: 2026-08-26
added_by: Debb
endorsed_by:
status: Tareas A, B, C y E ejecutadas por Claude Code (2026-08-26); Tarea D pendiente en Overleaf — ver verificaciones_boston_v2.md
plazo: entrega jueves 27 de agosto, mañana (evento: viernes 28, 8:30 am, Boston)
---

# Instrucciones v2 — Cierre del deck de Boston

## 0. Qué cambió respecto a v1

La v1 produjo `boston_20260828.tex` (343 líneas, 25 láminas) y `verificaciones_boston_v1.md` (17 verificaciones). El autor revisó el resultado y pidió cuatro correcciones:

1. Demasiado austero: falta color.
2. Una sola gráfica en 25 láminas es muy poco.
3. El lenguaje suena a IA; hay que humanizarlo.
4. Una nota al pie no cabe.

**Esas cuatro correcciones las ejecuta Debb, no Claude Code.** Son decisiones editoriales y de contenido. Debb entrega `boston_20260828_v2.tex` ya reescrito, con la paleta aplicada, las gráficas nuevas escritas y las fuentes reorganizadas.

**Estas instrucciones cubren únicamente lo que queda después de esa entrega.** Son cinco tareas acotadas.

---

## 1. Tarea A — Verificar Argentina (bloqueante)

La lámina 12 lleva una gráfica de barras con la proporción de ocupados que cotizan o están afiliados a un sistema de pensiones, por país. Siete de los ocho países presentes en la sala ya están verificados (V-serie de `verificaciones_boston_v1.md`):

| País | Valor | Estado |
|---|---|---|
| Uruguay | 77 % | verificado |
| Costa Rica | 73 % | verificado |
| Colombia | 43 % | verificado |
| República Dominicana | 43 % | verificado |
| Ecuador | 35 % | verificado |
| México | 34 % | verificado |
| Paraguay | 25 % | verificado |
| **Argentina** | — | **pendiente** |

**Instrucción:** obtener el dato de Argentina **de CEPALSTAT, con el mismo indicador y la misma cosecha (2023–2024)** que los otros siete. Es una consulta a base de datos, no una búsqueda web.

**No sustituir por indicadores parecidos.** En particular, la Secretaría de Seguridad Social de Argentina publica que el 28.4 % de la *población total* aporta a la seguridad social por su actividad. **Ese dato tiene otro denominador y no entra.** Tampoco entran tasas de informalidad de INDEC, ni asalariados no registrados, ni cobertura de la PEA: son conceptos distintos.

**Si el dato no existe en CEPALSTAT con ese corte exacto:** la gráfica se publica con siete barras y una nota al pie que declare que Argentina no está disponible en la misma serie. **Un hueco declarado es aceptable; un dato con denominador distinto no lo es.** En la sala hay tres participantes argentinos.

Contexto cualitativo verificado, útil solo para juzgar si el valor obtenido es plausible: Arenas de Mesa (2019, citado en CEPAL) ubica a Argentina en el grupo de mayor cobertura contributiva de la región, junto con Uruguay, Panamá, Costa Rica, Chile y Brasil. Si el valor obtenido cae por debajo de 50 %, revisar que se trate del indicador correcto antes de usarlo.

---

## 2. Tarea B — Sustituir la imagen de Naciones Unidas

El `.tex` que entrega Debb usa un marcador en blanco del mismo tamaño, porque el archivo real no estaba disponible en su entorno.

- Sustituir por `wpp2024_lac_broad_age_groups.png`: la imagen oficial descargada del portal WPP 2024, agregado **Latin America and the Caribbean**.
- **Conservar el pie de atribución incrustado.** Licencia CC BY 3.0 IGO. No recortar, no reescalar de modo que el pie quede ilegible.
- **Verificar que NO sea la versión etiquetada `LLDC: Latin America`.** Esa agrupación corresponde a los países en desarrollo sin litoral —Bolivia y Paraguay— y fue descartada. La escala del eje vertical distingue ambas: la correcta llega a 400 millones; la incorrecta, a 21.

---

## 3. Tarea C — Cotejar las gráficas nuevas contra las verificaciones

Debb añade cuatro elementos visuales. Dos llevan datos y dos son esquemas conceptuales.

### Con datos — cotejar cifra por cifra contra `verificaciones_boston_v1.md`

**Figura 1 (lámina 8) — Gasto en salud, México y promedio regional.** Cuatro barras: gasto público en salud como % del PIB (México 2.7 · promedio LAC 4.1) y gasto de bolsillo como % del gasto corriente en salud (México 41 · promedio LAC 30). Fuente: OMS, *Global Health Expenditure Database*, 2023.

**Figura 2 (lámina 12) — Cotizantes por país.** Barras ordenadas de mayor a menor, con los ocho países presentes en la sala. Datos en la tabla de la Tarea A. Fuente: CEPALSTAT, 2023–2024.

Si alguna cifra del `.tex` no coincide con la tabla de verificaciones, **no corregir por cuenta propia: reportar la discrepancia.**

### Conceptuales — sin ejes numéricos, sin datos

**Figura 3 (lámina 9) — Espacio fiscal.** Esquema: pensiones absorbiendo el espacio disponible, salud desplazada. Sin cifras, sin eje.

**Figura 4 (lámina 18) — Escalón y pendiente.** Esquema del beneficio neto: el escalón abrupto del sistema actual frente a la reducción gradual del impuesto negativo. Sin cifras, sin eje.

Ambas deben quedar visualmente identificables como esquemas. **No añadirles números, ejes ni escalas para "completarlas".**

**Excluida deliberadamente:** la composición del FTR. El hallazgo del Banco Mundial —que las contribuciones a seguridad social son el componente mayor— es cualitativo. Graficar proporciones no verificadas está prohibido. No reintroducirla.

---

## 4. Tarea D — Compilar y verificar que no hay desbordes

En v1, la lámina 15 desbordaba 19.17 pt (`Overfull \vbox` en la línea 232): tabla, frase destacada y seis fuentes no caben juntas. La v2 resuelve esto moviendo el aparato de fuentes a dos láminas al final del deck.

**Instrucción:**

```bash
pdflatex -interaction=nonstopmode boston_20260828_v2.tex   # dos pasadas
```

Revisar el log y reportar **todo** `Overfull \vbox` y `Overfull \hbox` mayor a 2 pt, indicando lámina y línea. No corregirlos por cuenta propia salvo que sean menores a 2 pt y se resuelvan con un ajuste de espaciado que no toque el texto.

Verificar además:
- Compila en `aspectratio=169`.
- Babel español activo (en v1 falló con `Unknown option 'spanish'`; si el entorno no tiene `babel-spanish`, instalarlo o reportar).
- 25 láminas de contenido más las láminas de fuentes.
- Ninguna ecuación, símbolo matemático ni letra griega en ninguna lámina.

---

## 5. Tarea E — Entrega

1. `boston_20260828_v2.tex` con Argentina resuelta.
2. `boston_20260828_v2.pdf` compilado.
3. `verificaciones_boston_v2.md`: la tabla de v1 más la entrada de Argentina (dato, fuente, indicador exacto, cosecha, URL, estado) y el cotejo de las Figuras 1 y 2.
4. Reporte breve de desbordes, si los hay.

---

## 6. Prohibiciones — releer antes de tocar el archivo

El `.tex` de v2 contiene decisiones editoriales tomadas deliberadamente. Un modelo que lo lea tenderá a "mejorarlo" y revertirá varias. **No hacerlo.**

1. **No reescribir el lenguaje.** La v2 elimina de forma deliberada la construcción antitética repetida ("no es X, es Y"), reduce las frases destacadas de diez a cuatro, y convierte los fragmentos sin verbo en oraciones completas. Si una lámina parece "menos punchy" que sus vecinas, es intencional: el remate en cada lámina anulaba el efecto de todos.
2. **No devolver las fuentes completas a las láminas.** En cada lámina queda una línea de fuente; el aparato va en las láminas finales. No es un descuido.
3. **No añadir más color.** La paleta es de cuatro elementos: azul de estructura, tono cálido reservado **exclusivamente a cifras**, banda gris tenue para encabezados de tabla y láminas de transición, y una regla fina bajo el título. Nada más lleva color. Si algo parece soso, es la instrucción.
4. **No añadir gráficas adicionales** más allá de las cuatro especificadas.
5. **No incluir ninguna lámina de "economía plateada"**, ni mencionar industria farmacéutica, biotecnología o sector asegurador como sectores de oportunidad. El evento es anfitrionado por Roche.
6. **No presentar los seguros privados de ciclo de vida como recomendación.** Aparecen solo como pregunta abierta de investigación (lámina 23).
7. **No ofrecer lugares de viaje ni traslados financiados** en ninguna lámina.
8. **No anunciar "seminario inaugural, septiembre 2026".** La cita es San José, Costa Rica, 5 al 7 de octubre de 2026.
9. **No reconstruir la gráfica de Naciones Unidas.** Se inserta la imagen original.
10. **No cambiar "coordinador" por otro título** en la lámina 22. No usar "Líder Vocal" ni describir a Uniandes y a la PUC como "universidades asociadas": son núcleo fundador.

---

## 7. Insumos

- `boston_20260828_v2.tex` — entrega de Debb. Base del trabajo.
- `verificaciones_boston_v1.md` — 17 verificaciones, 2026-08-26. Referencia de cotejo.
- `wpp2024_lac_broad_age_groups.png` — descargar del portal WPP 2024, agregado Latin America and the Caribbean.
- `20260826_COMUNIDAD_BUILDINST_boston_deck_v1.md` — instrucciones originales, contexto y estructura de las 25 láminas.

---

*Redactadas por Debb. Revisión de rigor pendiente (Beth). Ejecución: Claude Code. Entrega esperada: jueves 27 de agosto por la mañana.*

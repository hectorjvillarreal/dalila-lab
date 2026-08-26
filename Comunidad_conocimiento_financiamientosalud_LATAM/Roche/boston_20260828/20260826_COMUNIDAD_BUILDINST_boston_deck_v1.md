---
doc_id: 20260826_COMUNIDAD_BUILDINST_boston_deck_v1
project: COMUNIDAD
doctype: BUILDINST
slug: boston_deck
version: 1
date: 2026-08-26
added_by: Debb
endorsed_by:
status: verificación completa (verificaciones_boston_v1.md) y deck v1 construido (boston_20260828.tex) — 2026-08-26; PDF se compila en Overleaf; revisión del autor pendiente
---

# Instrucciones de construcción — Deck Boston, 28 de agosto de 2026

## 0. Contexto mínimo

Presentación de Héctor Juan Villarreal Páez en las **Regional Special Sessions** del programa *Building Strong Health Systems for the Future* (Harvard T.H. Chan School of Public Health / Roche).

- **Fecha y hora:** viernes 28 de agosto de 2026, 8:30–9:30 am.
- **Sede:** Hilton Boston Back Bay, 40 Dalton Street, Boston.
- **Sala:** track América Latina. África y Medio Oriente sesionan en salones paralelos.
- **Formato:** 60 minutos. 45 de exposición + 15 de presentación de la Comunidad. Dudas puntuales al final.
- **Audiencia:** funcionarios de ministerios, aseguradores, oncólogos y equipos de país de Argentina, Colombia, Costa Rica, Ecuador, México, Paraguay, República Dominicana y Uruguay. **No es audiencia académica.**
- **Idioma:** todo en español, por solicitud expresa.
- **Restricción dura:** **cero ecuaciones, cero notación matemática, cero letras griegas.** Toda la lógica se expresa en prosa.

Tras esta sesión siguen tres presentaciones de país (México MAU-CaMa, Colombia Consultorios Rosados, CCAV ImpulSALUD) y una plenaria de cierre conducida por Fernando Ruiz.

---

## 1. Estilo del beamer — LIGERO

Instrucción explícita del autor: **ligero, no barroco.** Los decks previos usaban `Madrid`, que trae barras de color arriba y abajo. Se abandona.

```latex
\documentclass[aspectratio=169,11pt]{beamer}

\usetheme{default}
\usecolortheme{default}
\usefonttheme{professionalfonts}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}[frame number]
\setbeamertemplate{itemize items}{--}
\setbeamertemplate{blocks}[default]   % sin sombras ni bordes redondeados
```

Reglas de estilo:

- **Sin headline.** Sin barra de sección, sin nombre del autor repetido en cada lámina, sin logo en cada lámina. Logo solo en portada.
- **Un solo color de acento**, sobrio (azul o gris oscuro), aplicado únicamente al título de lámina y a la palabra clave que se quiera destacar. Nada más lleva color.
- **Fondo blanco.** Sin degradados, sin texturas, sin marcos.
- **Sin bloques decorativos** (`\begin{block}`, `alertblock`, `exampleblock`). Si se necesita destacar una frase, va centrada y en negritas, sin caja.
- **Sin viñetas anidadas más allá de un nivel.**
- **Máximo 5 líneas de texto por lámina.** Frases cortas. La lámina es apoyo, no guion.
- Fuente sans serif. Tamaño de título `\large`, no mayor.
- Sin animaciones ni `\pause` salvo donde se indique explícitamente abajo.
- **No usar `tikz`/`pgfplots` para reconstruir gráficas.** Las gráficas se insertan como imagen (`\includegraphics`).

---

## 2. Estructura: 25 láminas, seis movimientos

### PARTE I — 45 minutos

**Apertura (2 min)**

1. **Portada.** Título, Héctor Juan Villarreal Páez, ITED / Escuela de Gobierno y Transformación Pública, Tecnológico de Monterrey. Comunidad Latinoamericana del Conocimiento sobre Financiamiento de la Salud. Boston, 28 de agosto de 2026.
2. **Lo que esta semana no discutió.** Cuatro días sobre compra estratégica, pago por valor, aseguramiento social y política de la reforma: todo sobre cómo gastar mejor lo que hay. Falta la pregunta de qué ocurre cuando cambia la estructura por edades. Anuncio de las dos restricciones: una determinada, otra decidida.

**Movimiento 1 — La demografía ya está decidida (10 min)**

3. **Gráfica UN WPP 2024, América Latina y el Caribe, población por grandes grupos de edad.** Imagen a lámina casi completa. **Conservar íntegro el pie de atribución** (© 2024 United Nations, DESA, Population Division · CC BY 3.0 IGO · World Population Prospects 2024). No recortar.
4. **Lo que no es pronóstico.** Las bandas de predicción de 65+ y de 25–64 son angostas porque esas personas ya nacieron. Lo incierto es la fecundidad; el envejecimiento es contabilidad.
5. **El envejecimiento del envejecimiento.** Población de 80 y más: de 12 a 37 millones entre 2024 y 2050. Es donde manda la dependencia funcional y el cuidado de largo plazo.
6. **La ventana se cierra en 2028.** El bono demográfico regional concluye, en promedio, el año próximo.

**Movimiento 2 — El espacio fiscal sí es una decisión (10 min)**

7. **El giro.** Lámina de transición, una sola frase centrada. Lo anterior está dado; lo que sigue no.
8. **Gasto público críticamente bajo.** México, 2.6 % del PIB desde el sector público. El complemento no es ausencia de gasto: es gasto de bolsillo, no planeado, por urgencia. Regresivo y empobrecedor.
9. **Pensiones desplazan salud.** Bisagra de la hora. Las promesas previsionales maduraron antes de que se ampliara la base contributiva. Las pensiones no contributivas son un avance real en cobertura y un costo fiscal creciente. Sin reforma paramétrica, el gasto en pensiones desplaza todo lo demás. Frase de cierre destacada: *reformar pensiones no es un tema separado de financiar salud; es su condición previa.*
10. **Un solo problema fiscal.** Pensiones, salud y cuidados compiten por el mismo espacio presupuestario. Toda propuesta que dependa de impuestos generales debe demostrar que es financiable a 20 años.

**Movimiento 3 — La tenaza (10 min)**

11. **Dos cosas al mismo tiempo.** Que la gente no se arruine cuando se enferma, y que valga la pena estar dentro del sistema contributivo. Casi todo lo intentado mejora una a costa de la otra. *(Es el marco φ–β. Se expresa así, en prosa. Sin símbolos.)*
12. **La base no da.** Informalidad estructural. Los sistemas contributivos cubren a menos de la mitad de la fuerza laboral. Bismarck no falla por teoría; falla por base contributiva estrecha.
13. **La trampa de la formalización.** El costo neto de ser formal. Hallazgo central: el componente mayor no son los impuestos, son las contribuciones a seguridad social. Si el trabajador no valora lo que recibe, la contribución se percibe como impuesto puro. Referencia en pie: Banco Mundial (2025).
14. **El escalón.** Costo cierto e inmediato al formalizarse; pérdida posible de beneficios. Uruguay eliminó el tope de ingreso de AFAM-PE reconociendo el desincentivo. Cierre con el dilema del paquete diferenciado.

**Movimiento 4 — Qué ha intentado la región (5 min)**

15. **Cinco casos, cinco piezas.** Una sola lámina. Tabla de cinco renglones, tres columnas: país / qué resolvió / qué le sigue faltando. **Sin banderas, sin mapas, sin logos.** Costa Rica, Uruguay, Colombia, México, Brasil. Frase de cierre destacada: *elegir Beveridge no evita la dualidad; solo cambia el lugar por donde aparece.*

**Movimiento 5 — Una nueva seguridad social (6 min)**

16. **Ampliar, no abandonar.** Quien puede contribuir, contribuye; quien no cotiza paga al menos un tramo proporcional a su ingreso; el gobierno cubre la prima completa solo para los más necesitados.
17. **Dos instrumentos.** Cuotas contributivas rediseñadas, canalizadas a salud, con vínculo claro entre contribución y beneficio. Primas graduadas para no cotizantes. Cierre: todos dentro del sistema de seguros, nadie afuera en un esquema paralelo.
18. **Consolidar transferencias.** Impuesto negativo sobre la renta como puente: el beneficio decrece suavemente, no hay salto, el trabajador siempre gana al formalizarse. Condición necesaria: observabilidad de ingresos, hoy factible por digitalización de pagos y facturación electrónica.
19. **El guiño.** Existe un tercer instrumento posible —prefondear el gasto de salud de la vejez— sobre el que hay pregunta, no recomendación. Se retoma al cierre. *Costura hacia la Parte II. Una sola frase.*

**Movimiento 6 — La doble prueba (2 min)**

20. **Dos preguntas para todo.** ¿Es financiable a lo largo de la transición demográfica sin dinámicas de deuda insostenibles? ¿Fortalece o debilita el incentivo a cotizar? Fallar en cualquiera de las dos es debilidad estructural. *(El expositor la aplicará en voz alta a los tres modelos que siguen. La lámina solo enuncia el criterio.)*

### PARTE II — La Comunidad (15 minutos)

21. **El hueco.** La región discute cobertura desde hace décadas y discute mucho menos solvencia de largo plazo.
22. **Qué es y quiénes.** Nombre completo de la Comunidad. Núcleo fundador: Tecnológico de Monterrey; Universidad de los Andes (Ramiro Guerrero); Pontificia Universidad Católica de Chile (Pablo Celhay). Héctor Villarreal como **coordinador**. Horizonte de cinco años, vocación de red regional. En la misma lámina: financiamiento semilla de Roche al Tec, cuatro reglas explícitas de independencia, y la regla completa de que la producción puede analizar críticamente el gasto farmacéutico y los precios de los medicamentos, sin excepción por identidad del patrocinador.
23. **Cuatro preguntas abiertas.** (a) Cuánto pesa el financiamiento privado y qué parte del gasto catastrófico de bolsillo puede convertirse en prepago mancomunado. (b) Bajo qué reglas un instrumento privado complementa el pool público en vez de vaciarlo. (c) Si detectar antes ahorra recursos al sistema o adelanta y prolonga el gasto. (d) Si las promesas de pensiones dejan margen para financiar salud a 20 años.
24. **El pedido y la cita.** Mapa regional de investigadores. Acceso a datos donde exista la posibilidad. San José, Costa Rica, 5 al 7 de octubre de 2026, reunión de trabajo.
25. **Cierre.** Pregunta final, centrada: ¿podemos diseñar sistemas de protección social que la gente valore lo suficiente como para querer participar, y que los gobiernos puedan financiar a lo largo de la transición demográfica? Datos de contacto.

---

## 3. Prohibiciones explícitas

Estas se derivan de decisiones ya tomadas. No revertir.

1. **No incluir ninguna lámina de "economía plateada" ni lista de sectores con potencial en una región que envejece.** En particular, **no mencionar industria farmacéutica, biotecnología ni sector asegurador como oportunidad de negocio.** El evento es anfitrionado por Roche; esa lámina se leería como complacencia con el patrocinador.
2. **No presentar los seguros privados de ciclo de vida como recomendación en la Parte I.** Van solo como pregunta abierta de investigación en la lámina 23.
3. **No ofrecer lugares de viaje ni traslados financiados desde el escenario.** Eso se resuelve bilateralmente.
4. **No anunciar "seminario inaugural, septiembre 2026, Escuela de Gobierno".** Esa información está desactualizada en los materiales fuente. La cita es San José, 5–7 de octubre de 2026.
5. **No usar gráficas etiquetadas como "perfiles estilizados"** de los decks docentes previos. Si una gráfica no tiene datos reales, no entra.
6. **No reconstruir la gráfica de Naciones Unidas.** Se inserta la imagen original con su atribución.
7. **No incluir ecuaciones, símbolos griegos ni notación**, ni siquiera en pie de lámina.

---

## 4. Verificaciones requeridas — ANTES de compilar

**Regla dura: ninguna cifra entra al deck sin fuente y año verificados. Si una cifra no se puede verificar, se marca y se consulta con el autor. No se aproxima, no se rellena, no se cita de memoria.**

En la sala hay colombianos, uruguayos, costarricenses, mexicanos, paraguayos, ecuatorianos, argentinos y dominicanos. Un dato mal citado sobre el sistema propio de alguien cuesta más que todos los aciertos.

### 4.1 Gráfica y cifras demográficas (UN WPP 2024, LAC)

| # | Dato a verificar | Uso |
|---|---|---|
| V1 | Año en que la línea de 65+ cruza a la de 0–14 | Lámina 3 |
| V2 | Año y nivel del máximo de la población 25–64, y su nivel proyectado a 2100 | Lámina 3 |
| V3 | Amplitud de las bandas de predicción al 95 % para 65+ y 25–64 (hasta qué año permanecen angostas) | Lámina 4 |

Fuente: UN DESA, Population Division, *World Population Prospects 2024*, agregado **Latin America and the Caribbean**. No usar agrupaciones LLDC ni LDC.

### 4.2 Cifras CEPAL

| # | Dato a verificar | Uso |
|---|---|---|
| V4 | Población 65+ en LAC: ~65 millones (9.9 %) en 2024 → 138 millones (18.9 %) en 2050 | Movimiento 1 |
| V5 | Población 80+: 12 → 37 millones (1.9 % → 5.1 %), 2024–2050 | Lámina 5 |
| V6 | Cierre del bono demográfico regional en 2028 (promedio) | Lámina 6 |

Identificar el documento CEPAL exacto (título, año, número de página) del que provienen. El material fuente las atribuye a CEPAL sin referencia completa.

### 4.3 Gasto e informalidad

| # | Dato a verificar | Uso |
|---|---|---|
| V7 | Gasto público en salud de México como % del PIB (2.6 %) — fuente, año, y si es gasto público total o gasto de gobierno general | Lámina 8 |
| V8 | Gasto de bolsillo como % del gasto corriente en salud, México | Lámina 8 |
| V9 | Rango de informalidad laboral en la región (40–60 %) — fuente y definición usada (OIT / CEPAL / Banco Mundial) | Lámina 12 |

Fuentes preferentes: OMS *Global Health Expenditure Database*, OCDE, CEPAL, OIT. Anotar cuál se usó.

### 4.4 Banco Mundial — FTR

| # | Dato a verificar | Uso |
|---|---|---|
| V10 | Que las contribuciones a seguridad social son el componente mayor del FTR | Lámina 13 |
| V11 | Referencia bibliográfica completa de Fietz et al. (2025), *(In)Formalizing Jobs in Latin America and the Caribbean* | Pie lámina 13 |

### 4.5 Uruguay — AFAM-PE

| # | Dato a verificar | Uso |
|---|---|---|
| V12 | Eliminación del tope de ingreso formal para acceder a AFAM-PE: año, norma, alcance | Lámina 14 |

### 4.6 Los cinco casos país (lámina 15)

Verificar arquitectura y, para cada uno, **una sola cifra defendible**:

| # | País | A verificar |
|---|---|---|
| V13 | Costa Rica | Cobertura del seguro de salud de la CCSS; velocidad de envejecimiento y caída de fecundidad respecto a la región |
| V14 | Uruguay | SNIS/FONASA: cobertura, e incorporación progresiva de cónyuges, hijos y jubilados (años) |
| V15 | Colombia | Ley 100: cobertura de aseguramiento actual; unificación del plan de beneficios (año); tasa de informalidad |
| V16 | México | Número de arquitecturas institucionales desde 2019 (Seguro Popular → INSABI → IMSS-Bienestar) y fechas |
| V17 | Brasil | SUS (Constitución de 1988) y tamaño del sector suplementario privado: % de población con plan de salud; tratamiento fiscal favorable (deducibilidad) |

### 4.7 Panel comparativo de los ocho países en la sala — OPCIONAL

Producir como **archivo aparte**, no como lámina, salvo que el autor lo pida. Argentina, Colombia, Costa Rica, Ecuador, México, Paraguay, República Dominicana, Uruguay. Indicadores: % población 65+ hoy y 2050; año de cierre del bono demográfico; gasto público en salud % PIB; gasto de bolsillo % del gasto corriente en salud; informalidad.

---

## 5. Entregables

1. **`verificaciones_boston_v1.md`** — tabla con las 17 verificaciones: dato afirmado, dato verificado, fuente completa, año, URL, y estado (`confirmado` / `corregido` / `no verificable`). **Este archivo se entrega primero y se revisa antes de compilar.**
2. **`boston_20260828.tex`** — el deck, 25 láminas, español, estilo ligero según sección 1.
3. **`boston_20260828.pdf`** — compilado.
4. **`panel_ocho_paises.md`** — opcional, según 4.7.

Ninguna cifra marcada como `no verificable` entra al `.tex`. Se deja el hueco señalado y se consulta.

---

## 6. Insumos disponibles

- `2-Population_by_broad_age_groups_1_.png` — gráfica UN WPP 2024, LAC. **Ya verificada como la correcta.** (Una versión anterior estaba etiquetada `LLDC: Latin America` = Bolivia y Paraguay; descartada.)
- `CEPAL_NuevaSegSocial_Villarreal_Héctor-1.pdf` — presentación al XXXVIII Seminario Regional de Política Fiscal de CEPAL, Santiago, mayo 2026. **Fuente principal de la Parte I.**
- `Comunidad_Financiamiento_Salud_Lanzamiento_CostaRica.pdf` — documento de presentación de la Comunidad. **Fuente principal de la Parte II.**
- `main.tex`, `main_1_.tex`, `main_2_.tex` — decks docentes de Economía Poblacional. **Fuente conceptual, no de láminas.** Contienen ecuaciones y perfiles estilizados que no se reutilizan.
- `Metodología_Harvard_Side_Event.docx` — metodología del taller. **Desactualizada en tiempos y en el nombre de la Comunidad.** Usar solo para contexto de los tres casos país.

---

*Instrucciones redactadas por Debb. Revisión de rigor pendiente (Beth). Verificación de cifras pendiente (Fina / Claude Code).*

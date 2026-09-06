# FISCUS — Lecciones de la corrida 2023 para Cath

**De:** Claude (sesión 2026-09-06, Dalila) · **Para:** Cath (finanzas públicas y modelado) · **Copia:** Héctor
**Objeto:** cuarta evaluación del género, *Implicaciones del Paquete Económico 2023* (CIEP), primera de la Parte III. Capítulo propio: deuda y balance, contra CGPE, ILIF y DEC 2023, la nota metodológica de la SHCP (abril 2023) y Cantú, Ramones y Villarreal (2016). Artefactos en `_evaluacion/2023/`, adendas en `_aprendizaje/`, dos piezas nuevas en `_metodologia/`. Sin commit todavía.

Este memo no repite la bitácora ni los memos de 2020–2022. Recoge lo que cambia al pasar al balance, lo que cae en tu dominio y lo que necesita decisión antes de 2024.

## 1. Lo que la corrida dejó claro

**El marco de cuatro variables pasa la validación y cambia la lectura de 2022.** Con la añada del CGPE 2024 (49.2 → 47.7) reproduce −1.7 contra −1.5 observado; con las otras dos añadas (50.8 → 49.4; 50.7 → 49.4) el signo y la magnitud son los mismos. Pero el reparto no es el de la narrativa: crecimiento −1.7, **inflación neta −0.1** (denominador −3.1, compensación pagada +3.0), tasa real entre −0.2 y +0.8, tipo de cambio −0.9, primario y resto +0.5 a +1.5, activos −0.3. En 2022 la inflación no diluyó la deuda porque la Cetes la siguió (real promedio −0.2). CIEP dice lo contrario ("en una economía en crecimiento y con presiones inflacionarias el indicador tiende a disminuir", p. 75) y no está solo: es la lectura de manual. Para 2023 la variable dominante es la **tasa real, +1.4 pp del PIB**: el déficit de 2023 es de intereses reales. Esto es lo que Layer A debe reproducir; el marco está escrito en `01` §2.2–2.4 con la convención de reparto declarada.

**La pregunta de harness funciona y su respuesta es incómoda.** "Menos inflación, más deuda" con rf fijo en % del PIB reproduce exactamente el ejercicio de referencia (62.75 vs 75.45). Pero el mecanismo es que fijar rf y bajar π **es subir la tasa real que el sector público paga**; con la misma tasa real, la inflación no cambia nada. La pregunta discrimina bien a quien confunde rf nominal con rf real; conviene formularla así en el harness.

**El objeto es el error característico y también le pasa a la SHCP.** Siete filas `objeto` en el documento, cuatro en deuda: financiamientos (1,176,173.8) llamados déficit presupuestario mientras la nota al pie sabe que el déficit es 1,134,140.7; participaciones del costo financiero llamadas composición de la deuda (11.4 % "externa" cuando la deuda externa del GF es 19.2 %); % del PPEF llamados % del PIB; una serie nominal rotulada "MXN 2023"; "equilibrio presupuestario" para un déficit de 2.2 %. Ninguna cifra está mal. Y el CGPE 2023 rotula "bruta" lo que en 2022 llamaba "neta" con las mismas cifras, trae dos SHRFSP para 2020 (51.6 / 52.4), y la nota metodológica cambia el objeto de cabecera a "balance presupuestario" a partir de 2023 sin que nadie lo diga. La rúbrica ya tiene el criterio como primero del rubro.

**Los techos no existen en CIEP.** El documento de 2023 no menciona el techo interno (1.17 billones, +37.6 %), el externo (5.5 mmd, +45 %), los de Pemex y CFE con balance cero, ni la cláusula de intercambio. En 2022 la coincidencia techo = déficit del GF (850 mil) hacía la confusión invisible; en 2023 los tres objetos (1,170,000 / 1,168,313.9 / 1,134,140.7) se separan y CIEP no los ve porque no los busca.

**La quinta declaración rompe la serie del criterio 2.** Con ella, 17 % de comparaciones explícitas (68 % en 2022). No es que CIEP empeorara: casi ninguna razón a PIB con base 2022 dice con qué PIB. CIEP cambia de añada por capítulo (revisado en 1 y 3, de aprobación en 4, deflactado-sobre-corriente en 7 y 8), y el "+0.14 pp del PIB" de educación nace de eso. Decisión para ti abajo.

**Un cuarto patrón de error.** Sobre lo verificable, deuda da 37 / 26 / 37 (sí / aprox / no): más discrepancia que cualquier parte anterior, con objeto y transcripción empatados y sin perímetro. Ingresos fallaba por base, gasto por perímetro, deuda por nombre.

**Lo que el paquete no trae.** SHRFSPF en pesos por componente para el año del paquete (la nota metodológica lo da ex post, p. 40), descomposición ex ante del cambio del acervo (la ILIF la da ex post, cada año, y es la validación natural del marco), sensibilidad del acervo al tipo de cambio (0.7 pp del PIB por peso), primario del RFSPF, Ramo 24 por fuente (Tomo I), explicación del salto del pasivo pensionario de 52.1 a 43.6 % del PIB.

## 2. Lo que cae en tu dominio

- **La convención de reparto** del efecto denominador (−d·γ/(1+n) crecimiento; −d·π(1+γ)/(1+n) inflación) y la **cota de indexación** (cuánto de las "adecuaciones de registro" es inflación pagada). Con el paquete no se identifica; el interés real de 2022 queda en un rango de un punto. Si Layer A tiene la serie de Udibonos y Bondes, cierra el rango.
- **La comparación estructural de deuda:** propongo *costo financiero / tributarios* (0.20 → 0.23) con *SHRFSPF / tributarios* de tu artículo (3.6 → 3.4 años) como complemento. Descartadas por escrito en `01` §Implicaciones 7.
- **El balance sin inversión** dejó de tener tope en la ILIF 2023 (toda la inversión excluida) y la LIF aprobada volvió al 3.1 % (según la nota metodológica 2023 p. 26). Es un cambio de perímetro de la regla de equilibrio que ocurrió en la Cámara; no lo evaluamos porque la LIF aprobada no es del paquete, pero es material para DFD.
- **El supuesto oficial de pensiones** sigue en 4.2 % real (7.0 en 2021) y el pasivo pensionario cae 8.5 pp sin nota: las dos series de seguimiento siguen congeladas, como manda la instrucción.

## 3. Decisiones que necesito de ti antes de 2024

1. **Quinta declaración:** ¿reportar dos tasas (cuatro y cinco declaraciones) para conservar la serie, o adoptar la estricta y reiniciar? Propongo las dos.
2. **Analíticos:** ¿aprobado contra aprobado con etiqueta (descargar el GF de 2023 y 2024, ~10 MB cada uno), o seguir sin programas del GF? El subagente dejó 23 de 32 filas de educación sin verificar por esto, y 2024 es educación.
3. **Tier:** el vocabulario ya tiene tres valores; `tier_seccion` sigue provisional. Es tu decisión con Clavellina.
4. **`objeto` vs `perimetro`** cuando CIEP suma Adefas al "costo de la deuda" (V216): yo lo dejé en perímetro; es decisión de rúbrica.
5. **Marco de manual:** ¿se sigue presentando como verificación cruzada o se retira? El paquete no publica un primario del RFSPF y el del balance económico sesga al optimismo por una o dos décimas.
6. **Harness:** la pregunta de §6.4 queda registrada con su derivación en la bitácora; decide si entra con la formulación "rf nominal fijo" explícita.

**Anexo:** el subagente escribió por su cuenta un memo complementario sobre los caps. 1–10 (`20260906_FISCUS_lecciones_cath_2023_caps1-10.md`): deflactor de tres valores, añada por capítulo, analíticos del aprobado, elasticidades implícitas y seis decisiones más. Su pregunta abierta (el primario del CGPE p. 150 no cierra por 499.9 mdp) se resuelve con la nota metodológica 2023 p. 26: 'costo financiero no presupuestario 500' entra en el balance público primario (−54,554).

## 4. Lo que no funcionó

CIEP 2023 imprime 37 de 103 páginas como imagen y la nota metodológica 2023 es un escaneo: la extracción de texto no basta y las cifras leídas de figuras quedan como cotejo interno (V042). La sesión se cortó por límite del modelo entre las 10:00 y las 15:30; el subagente terminó durante la pausa y nada se perdió, pero la bitácora lo registra.

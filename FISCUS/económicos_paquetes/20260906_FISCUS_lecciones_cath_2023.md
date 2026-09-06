# FISCUS — Lecciones de la corrida 2023 para Cath

**De:** Claude (sesión 2026-09-06, Dalila) · **Para:** Cath (finanzas públicas y modelado) · **Copia:** Héctor
**Objeto:** cuarta evaluación del género, *Implicaciones del Paquete Económico 2023* (CIEP), primera de la Parte III. Capítulo propio: deuda y balance, contra CGPE, ILIF y DEC 2023, la nota metodológica de la SHCP (abril 2023) y Cantú, Ramones y Villarreal (2016). Artefactos en `_evaluacion/2023/`, adendas en `_aprendizaje/`, dos piezas nuevas en `_metodologia/`. Commit `9d61d72`, rama `p3-correcciones-tex`.

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

## 4. Lo que no funcionó

CIEP 2023 imprime 37 de 103 páginas como imagen y la nota metodológica 2023 es un escaneo: la extracción de texto no basta y las cifras leídas de figuras quedan como cotejo interno (V042). La sesión se cortó por límite del modelo entre las 10:00 y las 15:30; el subagente terminó durante la pausa y nada se perdió, pero la bitácora lo registra.

## 5. Caps. 1–10 (ingresos y gasto), lo que añade el subagente

Filas V101–V398 de `02_verificacion_cifras.csv` (298: 91 sí / 47 aprox / 39 no / 93 no verificable / 28 juicio). Ingresos (caps. 1–2, 90 filas) cierran desde la carpeta; gasto sectorial (caps. 3–10, 208 filas) sólo por aritmética interna donde falta Tomo I, EM o PEF 2022 aprobado (caps. 7, 8 y 10 concentran 46 de las 81 no verificables).

**Hallazgos que no están arriba.**
- **El deflactor tiene tres valores y ninguno es 1.050.** El CGPE convierte 2022 a pesos de 2023 con 1.0497 (7,048,205.6 → 7,398.2; 5,207,251.7 → 5,465.8; 1,019,490.0 → 1,070.1). CIEP usa 1.0492 = (31,401.7/29,058.3)/1.030, el implícito de las cifras redondeadas del marco macro; se prueba en las columnas 2022 de sus cuadros 7.3 y 10.1 (FONE SP 405,414 = 386,413.9 × 1.04916; guarderías IMSS 15,160.8 = 14,450.3 × 1.04917). Explica todas las diferencias de 0.1 pp con el CGPE (14.1/14.0, 12.8/12.7, +10.0/+9.9, 11.7/11.6); marcadas `aprox`.
- **Los analíticos aprobados de entidades reproducen los perímetros propios de CIEP y delatan al proyecto.** Energía Pemex = 678,406.8 − 73,908.9 (pensiones, TG 4) − 18,463.8 (servicios médicos + adquisiciones) = 586,034.1; CFE = 439,772.4 − 51,605.2 = 388,167.2; pensiones contributivas por entidad = TG 4 (IMSS 750,252.1 = 56.3 % de 1,333,343.8). Pero tres renglones del cuadro 8.3 no coinciden con el aprobado 2023 (IMSS apoyo administrativo 94,515 vs 95,728.4; IMSS infraestructura 6,400 vs 6,951.3; ISSSTE gastos administrativos 19,211 vs 22,334.4): la Cámara reasignó incluso en entidades.
- **La base 2022 se valida por identidad cuando no hay PEF aprobado.** Ramo 24 + ramo 34 + costo financiero de Pemex y CFE del PPEF 2022 (580,638.2 + 38,683.9 + 142,556.1 + 29,585.6) = 791,463.8 = costo financiero aprobado 2022 (CGPE p. 150): el cuadro 3.2 de CIEP queda `si` sin el decreto aprobado. Lo mismo para ramos generales y aportaciones (CGPE p. 79 y 148, columnas PPEF/PEF idénticas) y Sener. No sirve para PPD, Tren Maya, Istmo, anexos transversales ni ramo 33 por función.
- **El documento se contradice a sí mismo más que al paquete.** Energía 24.8 % (texto) vs 24.1 (lámina y cuadro); ISR +15.9 vs +15.5; Gini 0.806 "asalariados" que en su cuadro 1.2 es de físicas; pastel del cap. 2 con FMP y CFE intercambiados; cuadro 2.1 cuyo total no es la suma; IMSS 44.6 % de pensiones contra 56.3 % × 1,333.3 = 44.3; cap. 6 con tres cifras para la variación total (−1.9 / −3.38), reguladores (+0.1 / −4.7) y PIB (3.5 / 3.6); cap. 7 con tres para "dónde se concentra el aumento" (46.2 / 88.8 / 52.0); PAM 314,421 en cap. 10 contra 335,499.4 en cap. 5. De 39 `no`, 24 son `transcripcion`, 7 `perimetro`, 4 `contrafactual`, 2 `objeto`, 2 `omision`.
- **Dos cierres que CIEP tenía a la mano y no hizo.** Excedentes petroleros 2022 vs pérdida por IEPS de gasolinas: CGPE p. 71 da +417.5 y −417.3 mmp (pesos de 2023); CIEP dice "es posible que no compensen" citando a BBVA. Gasto bruto 8,429,650.4 − 130,002.6 = 8,299,647.8: el decreto suma A–E = 9,452,819.1 con neteo 1,153,171.3; el neteo implícito de CIEP en el ramo 19 (1,036,197.3) más 130,002.6 deja 13,028.6 sin explicar.

**En tu dominio.**
- Espacio fiscal de CIEP reconstruido: 22.7 − (6.8 + 5.4 + 4.9 + 3.6) = 2.0 % del PIB; ineludibles 6,495.9 mmp, no "6.4 billones". Los "ingresos tributarios y no tributarios" de su definición son los presupuestarios totales: el ingreso propio de las EPE está en el numerador y su gasto en el denominador.
- Pensiones por entidad (PEF aprobado, TG 4, real): IMSS 636,461.8 → 750,252.1 (+12.4; Ley 73 en curso de pago +12.3, RJP +11.1, rentas vitalicias +14.1); ISSSTE 278,180.2 → 309,763.1 (+6.1); Pemex +1.5; CFE +0.7. Gasto total 1,692,920.9 = contributivas 1,333,343.8 (+8.4) + PAM 335,499.4 (+34.3) + PPD 24,077.7; el "+12.8 %" exige un PEF 2022 de PPD ≈ 20.1 mmp (el proyecto traía 18.0).
- Costo financiero 791,463.8 → 1,079,087.1 (+29.9 % real; 2.8 → 3.4 % del PIB) con Cetes 7.48 → 8.95; ramo 24 +38.0, ramo 34 +33.5. Ningún capítulo de la Parte II usa el mediano plazo (2.7 % en 2028) ni las sensibilidades de p. 102 (100 pb = 30,218 mdp; 1 dpb = 13,116: la caída de 93.6 a 68.7 vale ≈327 mmp y CIEP la llama "incertidumbre").
- Elasticidad implícita 2023 contra cierre: tributarios sin IEPS de gasolinas +1.3 % real con PIB +3.0 (0.43); con IEPS +9.9 (3.3, por la base deprimida de gasolinas). El CGPE la atribuye a componentes cíclicos, 30 mmp no recurrentes de la declaración anual y 29 mmp de actualización de tarifas; CIEP no usa ninguna de las tres.
- Inversión: "pensiones 2.8 pp más que infraestructura" sólo reproduce con obra pública (69.2 % de 1,190.1 = 2.6 % del PIB); con inversión física oficial (3.5 %) la brecha es 1.9 pp. Gasto de capital 2016–2022, % del PIB (p. 123): 5.9, 3.8, 3.1, 3.0, 3.4, 4.5, 4.4e.

**Decisiones adicionales (se suman a las de §3).**
7. **Deflactor de referencia:** ¿1.0497 como oficial y 1.0492 como "deflactor CIEP" con `aprox` en el décimo, o se exige el factor del CGPE y se marca `no`/`deflactor`? Afecta ~15 filas de 2023 y la convención de 2024.
8. **Analíticos aprobados de entidades como fuente de segundo nivel** (con la nota "PEF aprobado, no proyecto"): resolvieron caps. 5, 6 y parte de 8 y 10; la reserva es que la Cámara sí toca renglones de entidades. Es la mitad de tu decisión 2.
9. **Comparación estructural del gasto** para la serie 2020–2023: ineludibles / ingresos presupuestarios con el perímetro reconstruido (2023: 0.91) o pensiones + costo financiero / tributarios (2023: 0.60). ¿Cuál va a la ficha?

**Para 2024, desde los caps. de gasto.** Empezar por analíticos aprobados y decreto (Anexos 1, 8, 20–22): resuelven el 60 % de las filas de gasto en una hora. Verificar cada lámina contra cuadro y texto antes del texto. Calcular el deflactor implícito del documento desde sus cuadros antes de contrastar una variación. Validar la base t−1 por identidad antes de declararla ausente (rescató 12 filas). Anotar la población implícita de cada per cápita (131.2 millones en caps. 3 y 9, consistentes). La pregunta abierta del subagente sobre el primario del CGPE p. 150 (−54,553.7 ≠ −1,134,140.7 + 1,079,087.1 = −55,053.6) está resuelta: los 500 mdp son el costo financiero no presupuestario (nota metodológica 2023 p. 26).

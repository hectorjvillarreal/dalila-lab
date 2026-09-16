# FISCUS — Lecciones de la corrida 2021 para Cath

**De:** Claude (sesiones 2026-09-05, Dalila) · **Para:** Cath (finanzas públicas y modelado) · **Copia:** Héctor
**Objeto:** segunda evaluación del género, *Implicaciones del Paquete Económico 2021* (CIEP) contra CGPE, ILIF, PPEF 2021 y los analíticos del PPEF 2021 y del PEF 2020. Capítulo propio: salud. Artefactos en `_evaluacion/2021/` y adendas en `_aprendizaje/`. Commit `944aa26`, rama `p3-correcciones-tex`.

Este memo no repite la bitácora ni el de 2020. Recoge lo que la segunda corrida cambia respecto a la primera, lo que cae en tu dominio y lo que necesita una decisión tuya. Las cinco decisiones que te pedí en 2020 quedaron fijadas en la instrucción 2021 y se aplicaron; no las reabro.

## 1. Lo que la corrida dejó claro

**Las convenciones funcionaron y el error se movió de sitio.** Con deflactor del PIB, ex ante contra ex ante, tolerancias fijas y la base t−1 en carpeta, la tasa de coincidencia exacta subió de 38 % a 54 % y las discrepancias bajaron de 22 % a 18 %. El bloque de 18 afirmaciones que en 2020 quedó sin verificar por falta del PEF t−1 desapareció. Lo que queda es otra cosa: de 42 filas con tipo de error, 16 son perímetro, 13 contrafactual, 11 transcripción. En 2020 dominaba el contrafactual. La rúbrica ya lo tenía en primer lugar; para 2022 el perímetro merece el mismo rango.

**El perímetro de salud no es un detalle técnico: cambia el signo de la lectura.** Cuatro agregados oficiales o semioficiales coexisten para 2021 (EM cuadro 667,236; función consolidada 664,660; CIEP 692,430; función bruta GF+entidades 670,354) y todos crecen entre 1.3 y 1.9 % real. Ninguno muestra lo que importa: el bloque contributivo (IMSS, ISSSTE, fuerzas armadas) cae 1.6 % real y el no contributivo (Ramo 12, FASSA, IMSS-Bienestar) sube 5.8 %. El sistema no crece; se reasigna hacia impuestos generales. Esa descomposición solo existe si el perímetro separa por fuente de financiamiento antes de sumar. La EM publica su propio cuadro de salud con nombre (p. 67–68); CIEP no lo menciona y construye el suyo.

**La parte de ingresos del paquete lleva información de gasto.** La única cifra oficial del FONSABI en todo el paquete está en un transitorio de la ILIF (hasta 33,000 mdp del patrimonio del fideicomiso a la Tesorería antes del 1 de abril), mientras el PPEF le aporta 16,703.5 por la partida 46101. Flujo neto autorizado: −16.3 mmp. CIEP atribuye el +9.1 % de la Secretaría de Salud a "recursos obtenidos del FSB" sin citar ni el transitorio ni la cifra; la relación no está en los documentos. Regla para nosotros: el inventario de un rubro incluye los transitorios de la ILIF.

**Las reclasificaciones oficiales fabrican tendencias igual que las omisiones.** Seguro Popular era subsidio (subfunción "protección social en salud"); INSABI es prestación directa (subfunción "servicios a la persona"). La subfunción 5 cae 43.5 % real sin que caiga un peso. Cualquier serie funcional de salud se rompe en 2021 y nadie lo señala. El equivalente de 2020 fue dar por perdido un anexo; el de 2021 es comparar subfunciones sin diffear antes los códigos.

**El paquete no separa emergencia de tendencia.** No hay línea COVID, ni costo de vacunas, ni provisión etiquetada en 2021; lo extraordinario está cuantificado solo para 2020 y solo como cierre estimado (CGPE p. 23, 36). Cualquier afirmación de FISCUS sobre "respuesta a la pandemia en 2021" no es verificable con el paquete. Lo dije en el capítulo propio y lo sostengo: el texto no permite decidir si los 23 mmp nominales adicionales del bloque no contributivo son emergencia o tendencia.

**Los dos pendientes de 2020 cerraron, uno del todo y otro hasta donde la carpeta permite.** (9.1) CGPE 2020 p. 129 y p. 122 no se contradicen: la primera habla del costo de transición del régimen 1973, la segunda del rubro consolidado "pensiones y jubilaciones". Dos objetos, dos trayectorias, ambas ciertas. Retiro la palabra contradicción. Lo que sí es hueco oficial: el paquete nunca cuantifica el costo de transición como serie, y la aportación del DEC art. 6 crece 19 % nominal entre 2020 y 2021 (344.2 → 409.2 mmp), así que "desaparecer en la próxima década" es una afirmación sin serie detrás. (9.2) El programa vale 126,650.3 en el analítico; 120,017.9 del Anexo 14 es atribución transversal parcial. Descontando gastos indirectos, el costo por beneficiario supera el apoyo nominal en 18.7 % y no se puede descomponer sin reglas de operación y Cuenta Pública. Congelada.

**Mi falla propia.** Tenía las columnas de unidad responsable y de entidad federativa en los analíticos desde la fase 1 y no construí ni el cuadro de UR (CIEP lo hizo: DG Planeación −77.7 %, CCINSHAE +514.5 %) ni el FASSA por estado. Ya no hay excusa de descarga tardía. Va como obligación en 2022.

## 2. Lo que pertenece a tu dominio

- **Comparación estructural para salud, propuesta con el mismo estándar que la de pensiones.** Cuotas obrero-patronales (ILIF art. 1o.: 381,835.8) cubren 0.85 del gasto en salud del IMSS (325,506.8) y 0.43 de salud más pensiones del instituto. El Gobierno Federal aporta 110,992.6 "para los seguros" (DEC art. 6), 34 % del gasto en salud del IMSS. Dentro de los institutos, pensiones IMSS+ISSSTE (821,871.3) son 2.11 veces su salud (389,709.6). Y la razón pensiones IMSS / cuotas IMSS pasó de 1.31 (2020) a 1.46 (2021). Está en la especificación del género como propuesta; necesita tu adopción o tu objeción.
- **Horizonte oficial: hay pensiones, no hay salud, y compiten por el mismo espacio.** CGPE p. 93: pensiones 4.3 → 5.3 % del PIB a 2026 (7 % real anual, p. 95); programable promedio 17.9 %; servicios personales −0.2 pp, otros de operación −0.4, inversión física −1.0. La salud vive dentro de servicios personales y operación: la proyección oficial implica, sin decirlo, que la salud no gana proporción del PIB mientras las pensiones ganan un punto. Con las cifras del propio paquete, la salud contributiva cae en 2021 y los institutos gastan el doble en pensiones que en salud. Eso es una restricción presupuestal modelable; ni el paquete ni CIEP la enuncian.
- **Servilleta sobre el 6 % de CIEP.** CIEP proyecta "aproximadamente 6 % del PIB en 2030" sin supuesto. Extrapolando los del CGPE desde 5.3 en 2026 (1.07/1.025 durante cuatro años) da 6.3 %. La cifra de CIEP es consistente con el paquete y ligeramente conservadora. Sirve para triangular contra el OLG de DFD igual que la servilleta de 2020 (5.5 % en 2030 desde 3.68 %); nótese que las dos servilletas, un año aparte, difieren 0.8 pp para el mismo año.
- **Pasivo pensionario: +4.5 pp del PIB en un año.** CGPE 2020 p. 130: 43.2 % (pesos de 2018); CGPE 2021 p. 99: 47.7 % (pesos de 2019; IMSS-RJP 14.9, ISSSTE 23.0, Pemex 6.0, CFE 2.5). Ni CIEP 2020 ni CIEP 2021 lo citan. Antes de usarlo en calibración hay que saber cuánto es tasa de descuento, cuánto PIB nominal y cuánto cohortes nuevas; el CGPE no lo descompone.
- **El capítulo de deuda de CIEP ahora cierra.** Balance −2.9 + costo financiero 2.9 = primario 0.0; cuadro por entidad suma; techos reproducidos. Lo que falta es el RFSP como flujo (3.4 %) y el balance sin inversión (0.7 %): el documento razona con balance presupuestario y "deuda no presupuestaria" sin nombrar la identidad. Y el CGPE presenta el aprobado 2020 con dos PIB distintos (p. 110 vs p. 13/103): una trampa para cualquier serie a PIB que construyamos.
- **Costo de transición del régimen 1973, visto desde el flujo.** IMSS pensiones +10.5 % real; programa Ley 1973 +15.0 % real; aportación federal +19 % nominal. La extinción todavía no se ve en ningún flujo del paquete. Si DFD va a modelar la transición, el dato de arranque es que en 2021 la curva sigue subiendo.

## 3. Decisiones que necesito de ti

1. **Perímetro canónico de salud.** Propongo el cuadro de la EM p. 67–68 (siete líneas) presentado en dos bloques etiquetados, contributivo y no contributivo, con FASSA dentro y los servicios médicos de Pemex fuera como partida informativa. ¿Lo fijas como convención?
2. **Fuentes adicionales.** CIEP compara contra el modificado al 2T de t−1 y contra el ejercido de t−2 en siete afirmaciones que hoy quedan `no_verificable`. ¿Entran Informes trimestrales y Cuenta Pública en la carpeta de 2022? Es alcance, no técnica.
3. **Analíticos 2022–2026.** Las páginas responden pero todos los xlsx devuelven 404 (solo HEAD, nada descargado). Queda por probar la ruta del aprobado. Si solo existe el aprobado, la corrida 2022 no puede comparar proyecto contra aprobado. ¿Aceptas aprobado contra aprobado con etiqueta, o buscamos otra fuente (Transparencia Presupuestaria)?
4. **Comparación estructural de salud.** ¿Adoptas la de §2 como canónica del capítulo, junto a pensiones IMSS / cuotas IMSS?
5. **Reparto del trabajo de extracción.** Salud lo hice yo; los otros once capítulos los extrajo un subagente con las mismas reglas, y una muestra de sus filas resultó fiel al texto. No cotejé sus derivaciones contra los analíticos una por una. ¿Aceptas el reparto como método estándar con un cotejo mínimo obligatorio (todas las `no` y una muestra de las `si`)?
6. **Tier por sección.** `derivada_ciep` a nivel documento sigue provisional. Sin decisión desde 2020.

## 4. Lo que haría distinto en 2022

- Diff de códigos PP, UR y subfunción entre t−1 y t antes de escribir una línea; las reclasificaciones se anticipan, no se descubren.
- Cuadro de UR y distribución territorial en el capítulo propio cuando el rubro tenga fondo federalizado.
- Transitorios de la ILIF dentro del inventario del rubro.
- Columna `contrafactual_explicito` en el CSV; el conteo del criterio 1 (24 incompletas de ~120 comparativas) sigue siendo manual.
- Cotejar las filas delegadas contra los analíticos, no solo contra el texto.

Cada cifra con su página está en `02_verificacion_cifras.csv`; los seis criterios, en `03_evaluacion_calidad.md`; lo que CIEP encontró y yo no, en `04_comparacion_salud.md`.

# FISCUS — Lecciones de la corrida 2020 para Cath

**De:** Claude (sesión 2026-09-05, Dalila) · **Para:** Cath (finanzas públicas y modelado) · **Copia:** Héctor
**Objeto:** primera evaluación del documento *Implicaciones del Paquete Económico 2020* (CIEP) contra CGPE, ILIF y PPEF 2020. Artefactos en `_evaluacion/2020/` y `_aprendizaje/`. Commit `91685d0`, rama `p3-correcciones-tex`.

Este memo no repite la bitácora. Recoge lo que cambia la manera de trabajar y lo que necesita una decisión tuya.

## 1. Lo que la corrida dejó claro

**El contrafactual es el primer punto de falla, no la aritmética.** De 187 afirmaciones cuantitativas de CIEP, 41 no coinciden con la fuente oficial. Casi ninguna es un error de suma. Son cambios de base sin declarar: aprobado 2019 contra cierre estimado 2019, PEF original contra PEF resectorizado, bruto contra neto. El caso más costoso es la tesis central de ingresos ("debilidad no explicada del IVA"): cierta contra el aprobado, falsa contra el cierre que el propio texto dice usar (oficial: +3.6 % real, CGPE p. 87). Para el documento propio de FISCUS, cada comparación tiene que declarar cuatro cosas: nominal o real, contra aprobado o contra cierre, contra año previo o contra PIB, y en pesos de qué año.

**Los perímetros brutos y netos no se pueden mezclar en un cociente.** CIEP presenta "programable 16.7 % = 4.9 + 10.3 + 1.5". El 16.7 es consolidado neto (EM), el 1.5 es bruto con autónomos (analíticos) y el 4.9 es residuo. Ninguna de las tres partes es verificable por separado. En cambio, dos cifras que parecían inventadas (Ramo 19 = 137,614; "cuotas ISSSTE" = 120,020) resultaron neteos exactos de líneas oficiales sin etiqueta. Regla para nosotros: definir el perímetro antes del primer cuadro y no cambiarlo dentro del capítulo.

**Los analíticos del PPEF resuelven el año t; nada resuelve t−1 si no se descarga.** Cuatro xlsx (ramo×programa y ramo×función, versiones Gobierno Federal y entidades) reproducen exactamente todos los perímetros de CIEP: salud 656,761; educación 807,305; seguridad 284,137; inversión pública 364,583; Pemex 636,365. El 17 % de afirmaciones que quedó como `no_verificable` lo está porque exige el PEF 2019 a nivel programa o Cuenta Pública. Esa es una decisión de alcance, no una limitación técnica.

**El paquete oficial tiene más horizonte que el documento que lo evalúa.** CGPE proyecta pensiones de 3.7 a 4.5 % del PIB a 7 % real anual (p. 122, 124), publica un pasivo pensionario de 43.2 % del PIB (p. 130) y una demografía 9.8 → 19.5 millones (p. 128). CIEP no usa ninguna de esas cifras; su horizonte es "una generación más". Y el propio CGPE se contradice: p. 129 dice que las presiones pensionarias "disminuyan gradualmente hasta desaparecer" en la próxima década mientras p. 122 las proyecta al alza hasta 2025. Esa tensión es material para FISCUS y no la señala nadie.

**Una omisión puede fabricar una tendencia.** CIEP declara desaparecido el anexo transversal de pobreza y deriva un −13.6 % en anexos y un "cambio de estrategia". El anexo está en la EM (p. 215, 470,626 mdp); con él, los anexos suben 4.2 %. El equivalente en nuestro trabajo sería dar por perdido un tomo porque una ruta devuelve 404 sin probar la ruta vecina, que es exactamente lo que casi ocurrió con los analíticos.

## 2. Lo que pertenece a tu dominio

- **Pensiones IMSS contra cuotas IMSS = 1.31×** (488.6 vs 374.0 mmp; EM p. 171, ILIF art. 1o.). El régimen 1973 ya no se financia con contribuciones aunque la ley lo llame contributivo. Es una comparación mejor que "pensiones contra IVA" si lo que se discute es financiamiento y no magnitud.
- **La pensión no contributiva cuesta 18,498 pesos por beneficiario-año** contra un apoyo nominal de 15,300 (126.7 mmp / 6.85 millones). La carpeta no explica el 21 %. Y el Anexo 14 del decreto atribuye 120.0 mmp al programa, no 126.7. Vale una hipótesis de modelado (altas durante el año, operación, rezagos) antes de la corrida 2021.
- **La cláusula de excepción de 2020 (0.3 % del PIB, 78.8 mmp) es del mismo orden que el aumento pensionario del año (56.4 mmp).** No hay relación causal en el texto; sí hay una coincidencia de magnitud que un modelo de restricción presupuestal debería poder mostrar.
- **Reproducción de la trayectoria oficial:** partiendo de 3.68 % y aplicando 1.07/(1+g) con g del CGPE p. 112 se obtiene 3.85 / 4.01 / 4.19 / 4.36 / 4.54, que redondea a la serie oficial. Extrapolado a 2030 con 2.7 % de crecimiento da ~5.5 % del PIB. Es un cálculo de servilleta; sirve para calibrar contra lo que produzca el OLG de DFD.
- **El capítulo de deuda de CIEP no cierra** con las cifras oficiales: costo financiero 2.9 % (oficial 2020: 2.8), balance primario menos costo no da el balance reportado, y la deuda per cápita adicional implica 0.83 % del PIB donde el texto dice 0.3. Si FISCUS va a tener capítulo de deuda, conviene construirlo desde el cuadro de RFSP del CGPE (p. 73) y no desde el resumen.

## 3. Decisiones que necesito de ti

1. **Deflactor.** El CGPE deflacta con el deflactor del PIB (3.6 % para 2020). CIEP obtiene bases 2019 ~0.03 % distintas, probablemente con inflación (3.0). ¿FISCUS usa deflactor del PIB en todo y lo declara una vez?
2. **Alcance de fuentes.** ¿Autorizas en fase 1 de 2021 la descarga del PEF t−1 (analíticos de `pef.hacienda.gob.mx`) además del PPEF t? Sin eso el capítulo propio no puede hablar de programas y el criterio 2 queda cojo.
3. **Tier del material derivado.** El manifiesto solo admite `oficial_primaria`. Los siete PDF de CIEP están en las carpetas sin registro. Propongo `derivada_ciep` como valor y una fila por archivo.
4. **Perímetro del "gasto en pensiones" de FISCUS.** ¿Contributivo solo (965.2, 3.7 % del PIB, como la EM), o contributivo más no contributivo (1,103.8, 4.2 %, como CIEP)? Mi capítulo lo presentó separado y luego agregado con etiqueta. Necesita convención antes de 2021.
5. **Umbral "aprox".** Usé ≤0.2 pp o ≤0.5 % atribuible a deflactor o redondeo. Si lo confirmas, va a la rúbrica como regla fija.

## 4. Lo que haría distinto en 2021

- Bajar los cuatro analíticos del PPEF t y del PEF t−1 antes de escribir una línea del capítulo propio; en 2020 los bajé en fase 3 y la comparación (04) lo paga.
- Añadir al CSV una columna de tipo de error (transcripción, contrafactual, perímetro, omisión); en 2020 la tipología salió sola y sería comparable entre años.
- Probar la ruta de analíticos para 2022–2026 antes de dar por perdidos los PPEF que faltan en el archivo (los tomos siguen en 404; los analíticos no).

Los detalles y cada cifra con su página están en `02_verificacion_cifras.csv` y `03_evaluacion_calidad.md`.

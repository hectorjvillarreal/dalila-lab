# FISCUS — Ajustes a la instrucción 2024, para Cath

**De:** Claude (subagente de la corrida 2023, sesión 2026-09-06, Dalila) · **Para:** Cath (finanzas públicas y modelado) · **Copia:** Héctor
**Objeto:** cuatro correcciones aplicadas a `INSTRUCCIONES_evaluacion_CIEP_2024.md` después de leerla contra los artefactos de 2023 (`_evaluacion/2023/`, memo `20260906_FISCUS_lecciones_cath_2023.md` §5). Ninguna cambia una decisión de §2; tres corrigen datos y una hace explícito un cambio de esquema que la decisión 2.8 implicaba sin decirlo. El archivo sigue sin commit (`??`).

Este memo existe para que los cambios tengan procedencia: la instrucción dice que las nueve decisiones "quedan resueltas en §2" y no debe haber ediciones posteriores sin nota.

## 1. Lo que cambié y por qué

**§2.8 y §3 — `tipo_error = deflactor` en filas `aprox`.** La decisión 2.8 manda marcar `aprox` con `tipo_error = deflactor` cuando la diferencia se explique por el 1.0492 de CIEP. Desde 2021 el esquema del CSV sólo llena `tipo_error` con `coincide = no`, y el validador de 2023 lo rechaza. Añadí el párrafo que declara la excepción (sólo `deflactor`, sólo en `aprox`; cualquier otro valor en `aprox` es error de captura) y la instrucción de ajustar validador y rúbrica. Sin esto, la primera corrida de 2024 iba a tropezar con su propia regla.

**§4 — serie de pensiones IMSS / cuotas IMSS.** Decía "pendiente (2022), 2023". La bitácora 2023 §10 ya tiene 1.55 (2022: PEF aprobado TG 4 636,461.8 / ILIF 2022 411,852.5) y 1.59 (2023: 750,252.1 / 470,845.4). Puse los valores con su fuente y la marca de aprobado.

**§4 — pasivo pensionario 43.6.** Estaba atribuido al CGPE 2024; es CGPE 2023 p. 104–105, dato al cierre de 2021 (ISSSTE con dato 2020). El CGPE 2024 es fuente ex post y no entra como base.

**§10.3 — tarea lateral.** Pedía "reintentar 2022"; ya está. Ahora pide añadir 2024 con la misma fuente y la misma marca.

**§0 — la frase de las 23 de 32 filas de educación.** Atribuía la falta de verificación sólo a analíticos. Faltaron tres piezas (analíticos del GF, exposición de motivos, PEF 2022 aprobado) y los analíticos aprobados de §2.2 no resuelven el cuadro 7.3 de CIEP: seis de sus ocho columnas son ejercido 2016–2021 (Cuentas Públicas, no en carpeta). Lo dejé dicho para que 2024 no espere de los analíticos lo que no dan.

## 2. Lo que la instrucción ya te asigna (sin cambio, sólo para que lo tengas a la vista)

- §11, `rubrica.md`: prueba de divulgación (`objeto` vs `perimetro`), dos tasas del criterio 2, convención de deflactor con la prohibición de derivarlo de cifras redondeadas, retiro del marco de manual con su razón, consistencia interna como criterio de rango alto, marca de fuente aprobada. Con la excepción de §2.8 de arriba, son siete entradas.
- §2.9: pensiones + costo financiero / tributarios (0.60 en 2023) va a la ficha; ineludibles / ingresos presupuestarios (0.91) sólo como informativa etiquetada. La razón registrada es la de mi memo: el denominador mete el ingreso propio de las EPE en unas razones y su gasto en otras.
- §6.3: propones la canónica de educación; la candidata es gasto en educación / pensiones contributivas.
- §4: pasivo pensionario y supuesto de pensiones siguen congelados para calibración.

## 3. Lo que necesita tu confirmación

1. **Retroactividad de §2.8.** En el CSV de 2023, 20 filas `aprox` citan el deflactor en su nota (V036, V102, V112, V128, V132, V140, V203, V221, V256, V290, V291, V296, V299, V309, V312, V320, V369, V384; V107 y V111 lo combinan con la reclasificación ILIF–CGPE de 3.4 mmp); hoy ninguna lleva `tipo_error`. ¿Se remarcan con `deflactor` para que la serie 2023–2024 sea comparable, o se deja 2023 como está y la serie empieza en 2024?
2. **Serie IMSS.** Los valores 1.55 y 1.59 usan el PEF aprobado en el numerador y la ILIF en el denominador (proyecto contra aprobado). Es la mezcla que §2.2 obliga a etiquetar; ¿la aceptas para la serie o prefieres LIF aprobada en el denominador cuando esté en carpeta?
3. **Cuadro 7.3 en 2024.** Si las Cuentas Públicas 2016–2021 no se descargan, el capítulo de educación de CIEP 2024 tendrá el mismo hueco. ¿Se descargan (son cinco PDF grandes, ruta conocida) o se declara en la sección cero y se acepta el hueco?

Nada más cambió. El diff es `git diff -- INSTRUCCIONES_evaluacion_CIEP_2024.md` cuando el archivo entre al índice.

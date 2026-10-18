# `seccion10_v11.py`

Cifras que pide la sección 10 v1.1 del Núcleo 13. No agrega supuestos: usa `base_v12` y salidas ya calculadas.

- **1.1** Parte patronal de la cuota fija (20.40 % de la UMA) con el mismo subsidio, umbrales y días que la cuota proporcional de la Figura 10.2 (`pago_informal` con D1·G2: cuota anual de 365 días; excedente sobre 3 UMA con 337 días, como en `asequibilidad`). Percentiles 10 a 90 del ingreso laboral del titular informal, 2026.
- **1.5** Afiliación individual (U2): cada integrante paga 3.467 % del ingreso por persona del hogar, con subsidio por persona, más el excedente de quien trabaja. Mediana del pago del hogar en la banda de ±2.5 percentiles alrededor de la mediana del titular.
- **1.3** Costo por persona con 70.69 M de derechohabientes (Núcleo 13) en lugar de 79,178,109 (Cuadro I.4): se escala el costo de 2030, sin otra corrida. Proporción de la población con IMSS en 2030 (tasas ENIGH × CONAPO), sin el esquema y con él.
- **1.9** Saldo de 2030 entre los ingresos del SEM de la Tabla 5 del Núcleo 13 (611.2 mil mdp).

- **Insumos:** `Insumos()` (ENIGH, CONAPO, umbrales), `resultados_v12`, `enigh_edad_sexo`, `conapo_pob`
- **Salidas:** `outputs/tables/seccion10_v11_cuota_fija_patronal.csv`; claves `s10v11_*` en `NUMBERS.md`
- **Instrucción:** `20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.1`

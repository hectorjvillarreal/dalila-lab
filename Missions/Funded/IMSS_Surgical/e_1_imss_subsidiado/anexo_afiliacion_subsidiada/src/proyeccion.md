# `proyeccion.py`

Motor de proyección 2026-2054 de los Bloques A, B y C para la malla de `config.yaml`.

Bloque A: microdatos reponderados a CONAPO; pago por titular (U1) o por persona (U2); adopción y selección adversa (T); costo = c(edad) × (1+π_m)^(t−2026). Bloque B: forma R1 × cotizantes por grupo; m crece con el SBC real y tiene piso en el SM. Bloque C: fracción de hogares objetivo que cotiza (F1). Métricas: mdp, puntos del SBC, % de ingresos del SEM, % del PIB 2026. Verificaciones 7.5, 7.7 y 7.8.

**v1.2:** `correr` acepta el diseño D1 (precio plano en UMA) o D2 (tasa proporcional neutral c, calculada en `Insumos`), adopción τ, cobro ρ (pagos determinados frente a cobrados), selección μ, umbrales fijos o indexados y 337 o 365 días. Corre `malla` (v1.1, sin cambios) y `malla_v12`; añade el Bloque C contra el status quo, el efecto de indexación sobre los formales y las verificaciones 6.1-6.5 (la 6.1 compara la corrida `regresion_v11` con la base v1.1).

- **Insumos:** todas las anteriores
- **Salidas:** `resultados_malla`, `resultados_v12` (parquet y CSV); tablas `efecto_indexacion`, `bloque_C_vs_status_quo`
- **Instrucción:** `..._build_v1.1` y `..._build_v1.2`

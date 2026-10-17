# `proyeccion.py`

Motor de proyección 2026-2054 de los Bloques A, B y C para la malla de `config.yaml`.

Bloque A: microdatos reponderados a CONAPO; pago por titular (U1) o por persona (U2); adopción y selección adversa (T); costo = c(edad) × (1+π_m)^(t−2026). Bloque B: forma R1 × cotizantes por grupo; m crece con el SBC real y tiene piso en el SM. Bloque C: fracción de hogares objetivo que cotiza (F1). Métricas: mdp, puntos del SBC, % de ingresos del SEM, % del PIB 2026. Verificaciones 7.5, 7.7 y 7.8.

- **Insumos:** todas las anteriores
- **Salidas:** `resultados_malla` (parquet y CSV)
- **Instrucción:** `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1`

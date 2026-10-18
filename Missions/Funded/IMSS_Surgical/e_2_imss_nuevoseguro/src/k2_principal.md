# `k2_principal.py`

Instrucción `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.3`. K2 pasa a ser la regla principal y K1 queda como variante sin reserva. El modelo es el de la v1.2; cambian la presentación, el escenario MH y la convención de fechas.

- **`cuadro_principal`:** base, M3 y M2 en 2027, 2030, 2040 y 2054, en mdp y en puntos del salario. Filas: ingreso, déficit de GMP, depósito a la reserva (+) o retiro para GMP (−), gasto en cuidados y déficit no cubierto → `tablas/cuadro_principal_K2.csv`.
- **`resumen_k2_k1`:** último año con cobertura completa; déficit no cubierto en 2054 y en VP; cuidados en VP; reserva al final del horizonte en VP (saldo de cierre de 2054 descontado a 2026; en K1 es 0); cuidados más reserva → `tablas/resumen_K2_K1.csv`.
- **`sensibilidad_v13`:** base, M3, MH y M2 × K2 y K1 × con o sin provisiones × masa del libro o S-masa; último año con cobertura completa → `tablas/sensibilidad_v13.csv`. MH se define en `insumos.py`: paso de la serie histórica y tope en la formalidad de la base.
- **Verificaciones:**
  - 6.1, regresión con la configuración v1.2 (`data/v12/`).
  - 6.2, el resumen coincide con la v1.2.
  - 6.3, MH: ≤ base siempre y entre M2 y M3 desde 2035, en formalidad, masa, déficit y fechas.
  - 6.4, reserva final.
  - La 6.5, 6.7 y la ausencia de «primer año sin cobertura» se revisan en `salidas.py`.
- **Convención:** «último año con cobertura completa» = primer año con déficit no cubierto − 1; 2054 si no hay.

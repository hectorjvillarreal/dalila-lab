# `sensibilidades_v12.py`

Instrucción `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.2`, secciones 1 a 3 y verificaciones 8.1 a 8.4. El resultado principal sigue siendo el de `nuevo_seguro.py`: déficit con provisiones y masa del libro. Aquí van las sensibilidades.

- **`grilla`:** base, M3 y M2 × con o sin provisiones de GMP (Cuadro V.19) × masa del libro o S-masa. En S-masa, el ingreso del nuevo seguro arranca en su nivel propio de 2027 y crece al ritmo del ingreso de GMP del Cuadro V.24 (× masa_M / masa_base en M3 y M2). Reporta el primer año sin cobertura (K1 y K2), el déficit no cubierto en valor presente y el margen mínimo → `tablas/sensibilidad_provisiones_masa.csv`.
- **`razon_ingreso_gmp`:** r(t) = ingreso de GMP / masa propia base → `tablas/razon_ingresoGMP_masa.csv`.
- **`reserva_k2`:** saldos de inicio en 2035, 2040, 2045, 2050 y 2054; retiros para GMP y para cuidados acumulados; año de agotamiento → `tablas/reserva_K2.csv`.
- **`k2_v11_faltantes`:** lo que pagaba la regla v1.1 a cuidados en años con faltante de GMP → `tablas/k2_v11_anios_con_faltante.csv`.
- **`k2_cambios`:** comparación K2 antes y después → `tablas/k2_cambios_v11_v12.csv`.
- **Verificaciones:**
  - 8.1, regresión con la configuración v1.1 (`data/v11/`).
  - 8.2, sin provisiones ≤ con provisiones.
  - 8.3, consistencia de S-masa.
  - 8.4, sin retiro para cuidados en años con faltante; identidad de la reserva.

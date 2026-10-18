# `nuevo_seguro.py`

Secciones 1.1 a 1.4 de la v1.0, 1, 2 y 5 de la v1.1 y la regla K2 de la v1.2; verificaciones 3.1 a 3.4 y 7.1 a 7.3.

- **Corridas:** `config.yaml` define `corrida` (v1.2 activa) y `corridas` (escenarios, ajuste del ingreso de GMP, prima de RT y bases de personas). `regresion_v10` recalcula con la configuración v1.0 y compara con `data/v10/` (verificación 7.1).

- **`simular`:** año por año, de 2027 a 2054, para la masa base y la M2.
  - Ingreso I = 2 % de la masa con tope del escenario. Déficit D del Cuadro V.24; en v1.1, D_M = D + ingreso de GMP × (1 − masa_M / masa_base), sin ajustar el gasto. También el margen sin provisiones (Cuadro V.19).
  - K1: U = max(0, I − D); déficit no cubierto = max(0, D − I); sin reserva.
  - K2: la reserva acumula al 3 % hasta 2034. La regla depende de `k2_regla`:
    - v1.1: desde 2035, U = remanente + 1/20 de la reserva de inicio de 2035, acotado por lo disponible, aun en años con faltante de GMP.
    - v1.2 (regla de Beth, activa): el ingreso cubre GMP; el faltante sale de la reserva; el retiro fijo para cuidados solo en años sin faltante y hasta donde alcance la reserva. Registra intereses, depósitos y retiros para GMP y para cuidados.
    - En las dos, si la reserva no alcanza, la diferencia es déficit no cubierto.
  - Opciones de sensibilidad (v1.2): `sin_prov` resta las provisiones de GMP del Cuadro V.19; `s_masa` hace crecer el ingreso al ritmo del ingreso de GMP del Informe.
- **`valor_presente`:** VP 2027-2054 al 3 % real a 2026.
- **`contrastes`:** contrastes con el Informe sobre su horizonte de 30 años: volumen de salarios, VP del déficit interpolado (a fin y a mitad de año) y descomposición de 1.6 puntos × volumen frente al Cuadro V.24.
- **`por_mayor`:** remanente por persona de 65+ y 80+ con las bases de la corrida (v1.1: ENIGH y conteo máximo del Informe).
- **`resumen`:** por escenario, primer año sin cobertura (K1 y K2), déficit no cubierto en 2054 y en VP, remanente en VP.
- **`v24_del_pdf`:** lee la pág. PDF 161 del Informe para la verificación 3.2.
- **Salidas:** `tablas/ingreso_vs_GMP.csv`, `tablas/valor_presente.csv`, `tablas/remanente_por_mayor.csv`, `tablas/resumen_escenarios.csv`
- **Instrucciones:** `..._build_v1.0`, `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.1`

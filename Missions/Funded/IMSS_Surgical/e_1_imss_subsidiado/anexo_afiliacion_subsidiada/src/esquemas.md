# `esquemas.py`

Tabla única de pago, no arbitraje (7.6), brecha GMP, cuota fija como % del SM, indicador de incentivos.

Umbrales m0/m1 = percentiles ENIGH × 1.0689 (llevados a 2026), fijos en UMA. Pagos por G1/G2; verificación en malla 0-25 UMA × S × G × U; figura de π_I, π_F y π_F vigente.

- **Insumos:** salidas de `enigh`, `libro`
- **Salidas:** tablas `no_arbitraje_antes_despues`, `brecha_GMP`, `cuota_fija_pct_sm`, `indicador_incentivos_2026`; figura `pagos_pi_I_pi_F.png`
- **Instrucción:** `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1`

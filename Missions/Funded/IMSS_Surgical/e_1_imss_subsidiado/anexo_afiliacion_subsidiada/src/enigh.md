# `enigh.py`

ENIGH 2024: población objetivo, R1, R2, ocupación y verificaciones 7.4.

Cobertura contributiva = `inst_1`..`inst_4`; ocupado = registro en `trabajos`; ingreso laboral = claves P001-P022 + negocios (noagro, agro); titular = ocupado sin cobertura de mayor ingreso (15+). Calcula percentiles del ingreso del titular y del per cápita, beneficiarios por titular (R2), la forma del ingreso de asalariados con IMSS (R1) y la informalidad por decil.

- **Insumos:** I4
- **Salidas:** `enigh_personas`, `enigh_edad_sexo`, `r1_forma_sbc` (parquet); tablas `A_poblacion_objetivo_*`, `R2_*`, `enigh_informalidad_por_decil`
- **Instrucción:** `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1`

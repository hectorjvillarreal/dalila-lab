# `insumos.py`

Construye `Insumos2` a partir de `proyeccion.Insumos` de la v1.2. No escribe en el registro del experimento 1: su `record` se anula al importar.

- **Masa salarial:** cotizantes del libro × distribución R1, con tope de 25 UMA, piso en el salario mínimo y 337 días; es la misma base de la tasa D2. También calcula la masa sin tope, para medir la proporción por encima del tope. 2055 se extiende un año solo para el contraste 3.3.
- **Escenarios de formalidad (v1.1):** M2 mantiene la formalidad implícita de 2025; M3 toma, año por año, la mitad de la ganancia institucional sobre 2025. Factor de masa = formalidad del escenario / formalidad base (prueba C de la v1.2).
- **Personas mayores:**
  - 16.6 % (Gráfica I.31) × 79,178,109 (Cuadro I.4), con el crecimiento de la población de 65+ de CONAPO; 80+ con la razón 80+/65+.
  - Base ENIGH (v1.1): tasa de afiliación al IMSS (`inst_1`) por grupo quinquenal (85 y más) y sexo × CONAPO por año, para 65+ y 80+.
  - El conteo del Informe queda como conteo máximo; la base PAMF (63,598,543) solo se usa en la regresión v1.0.
- **Informe:** déficit e ingresos de GMP (Cuadro V.24), provisiones de GMP (Cuadro V.19) e ingresos del SEM (Cuadro V.13), interpolados linealmente. También guarda los ingresos del SEM del libro, para el contraste.
- **`cargar()`:** una sola construcción por proceso.
- **Insumos:** derivados de la v1.2 (`libro_*`, `r1_forma_sbc`, `prueba_c_agregado`, `conapo_pob`, `efecto_indexacion`).
- **Instrucciones:** `..._build_v1.0`, `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.1`

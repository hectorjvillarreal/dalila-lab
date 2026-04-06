# Transversal macro — Consistencia macroeconómica OLG/DSGE

**Responsables:** Edmundo Molina Pérez, Hermilo Cortés González
**Coordinación:** Cath (Core Team) — arquitecta del modelo
**Estado:** Infraestructura computacional lista (Dalila, 2026-03-31); calibración pendiente

## Mandato

Verificar la coherencia macroeconómica de las propuestas RF mediante modelo
DSGE-OLG y simulaciones en equilibrio general. Examinar ahorro, mercados
laborales, balances fiscales e incidencia intergeneracional.

## Arquitectura del modelo

El modelo OLG para RF es una extensión del núcleo DFD con sector fiscal explícito:

- **Sector productivo:** Cobb-Douglas, factor market clearing
- **Hogares:** problema de ciclo de vida, consumo-ahorro, oferta laboral
- **Gobierno:** presupuesto con tres instrumentos de ingreso (trabajo, capital, consumo)
  y tres de gasto (pensiones, salud, gobierno general); deuda endógena
- **Equilibrio:** salarios y retorno al capital emergen de optimización de firmas

## Parámetros clave a calibrar para RF

| Parámetro | Fuente | Estado |
|---|---|---|
| Elasticidades base gravable por instrumento | G1 microsimulaciones | Pendiente exportar |
| Trayectoria demográfica 2025-2070 | Anne (DFD) | Disponible vía DFD |
| Gasto pensionario por cohorte | G3 / Beth | Pendiente |
| Gasto salud por cohorte | G3 / Beth | Pendiente |
| Espacio fiscal estatal proyectado | G2 | Pendiente |

## Escenarios a simular

1. **Base:** sin reforma, trayectoria actual
2. **Reforma parcial:** paquete acotado G1 + administración tributaria
3. **Replanteamiento completo:** tres ejes + transversales integradas
4. **Sensibilidad demográfica:** bajo distintas trayectorias poblacionales (Anne)

## Stack computacional

- Julia: modelo OLG, equilibrio general, simulaciones
- Python: preprocesamiento de datos, visualización
- CUDA: aceleración GPU para simulaciones de gran escala
- Git/GitHub: control de versiones

## Archivos

- `modelo/calibracion/` — Parámetros documentados con fuente y rango de sensibilidad
- `modelo/simulaciones/` — Scripts de escenarios
- `modelo/resultados/` — Outputs para neteo integrado
- `codigo/julia/` — Implementación OLG
- `codigo/python/` — Preprocesamiento y visualización

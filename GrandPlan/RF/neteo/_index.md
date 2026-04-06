# Neteo integrado — Producto final RF

**Estado:** Pendiente — requiere completar G1, G2, G3 y transversal macro

## Descripción

El neteo integrado consolida los tres ejes del proyecto RF en un análisis
unificado de efectos sobre: recaudación, incidencia, sostenibilidad fiscal
intertemporal y redistribución del ingreso.

La estructura permite ver el neteo considerando solo algunos elementos
o el conjunto completo. Esto es esencial para la disyuntiva anticipada:
replanteamiento completo vs. reforma parcial.

## Metodología (4 etapas)

1. Literatura y estudios previos — completada
2. Aproximaciones lineales con parámetros reconocidos — parcialmente completada (G1)
3. Simulador fiscal mecánico CIEP (flujos + sostenibilidad) — pendiente
4. Modelo OLG/DSGE — pendiente (transversal macro)

## Escenarios

### A — Replanteamiento completo
Tres grupos + transversales. Meta: 25% PIB presión fiscal en 2036.
Ver: `escenarios/replanteamiento_completo/`

### B — Reforma parcial
G1 prioritario + administración tributaria. Meta: espacio fiscal de corto plazo.
Ver: `escenarios/reforma_parcial/`

## Outputs esperados

- Recaudación adicional por escenario (% PIB, por instrumento)
- Incidencia distributiva por decil
- Trayectoria de deuda pública (% PIB, 2025-2036)
- Efectos sobre factor prices (salarios, retorno al capital)
- Incidencia intergeneracional (OLG)

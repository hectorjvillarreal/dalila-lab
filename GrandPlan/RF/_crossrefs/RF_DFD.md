# Referencias cruzadas RF ↔ DFD

## RF → DFD (insumos que RF provee al modelo DFD)

| Insumo | Origen en RF | Destino en DFD | Estado |
|---|---|---|---|
| Elasticidades de bases gravables | G1 microsimulaciones | Calibración sector fiscal | Pendiente |
| Parámetros de informalidad laboral | G1 Nota Técnica | Factor markets | Pendiente |
| Trayectoria gasto pensionario | G3 | Restricción presupuestal | Pendiente |
| Trayectoria gasto en salud | G3 | Restricción presupuestal | Pendiente |
| Tasas impositivas por escenario | neteo/ | Experimentos de política | Pendiente |

## DFD → RF (lo que DFD devuelve a RF)

| Output | Origen en DFD | Uso en RF | Estado |
|---|---|---|---|
| Verificación equilibrio general | Transversal macro | Consistencia neteo | Pendiente |
| Efectos sobre salarios y r | OLG core | Incidencia distributiva | Pendiente |
| Trayectoria demográfica base | Anne / DFD | Calibración G1, G2, G3 | Disponible |
| Ratio de dependencia endógeno | OLG core | Sostenibilidad pensionaria | Pendiente |

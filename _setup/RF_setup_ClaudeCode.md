# RF — Instrucciones para Claude Code
# Preparación de la arquitectura de archivos en Dalila
# Fecha: 2026-04-06

## Contexto

Este archivo instruye a Claude Code para crear la estructura de directorios y archivos
base del proyecto RF (Reforma Fiscal para México) dentro del ecosistema Dalila.
El proyecto forma parte del Grand Plan y tiene dependencias activas con DFD, BDH y Aurora.

---

## Tarea

Crear la siguiente estructura de directorios y archivos en la ruta base indicada.

**Ruta base:** `~/Dalila/GrandPlan/RF/`

---

## Paso 1 — Crear la estructura de directorios

```bash
mkdir -p ~/Dalila/GrandPlan/RF/{docs/archivos_recibidos,_crossrefs}
mkdir -p ~/Dalila/GrandPlan/RF/G1_reforma_fiscal_clasica/{borradores,datos,codigo,notas}
mkdir -p ~/Dalila/GrandPlan/RF/G2_finanzas_subnacionales/{borradores,datos,codigo,referencias}
mkdir -p ~/Dalila/GrandPlan/RF/G3_seguridad_social/{borradores,datos,codigo,referencias/articulos_arena_publica}
mkdir -p ~/Dalila/GrandPlan/RF/transversal_macro/{modelo/{calibracion,simulaciones,resultados},codigo/{julia,python},notas}
mkdir -p ~/Dalila/GrandPlan/RF/transversal_juridica/dictamenes
mkdir -p ~/Dalila/GrandPlan/RF/neteo/{escenarios/{replanteamiento_completo,reforma_parcial},resultados}
```

---

## Paso 2 — Crear los archivos base

### `_index.md` — Raíz del proyecto

```bash
cat > ~/Dalila/GrandPlan/RF/_index.md << 'EOF'
# Proyecto RF — Reforma Fiscal para México

## Descripción

Replanteamiento hacendario integral para México. Tres ejes sustantivos:
reforma fiscal clásica, finanzas públicas subnacionales, y seguridad social.
Dos transversales: consistencia macroeconómica (OLG/DSGE) y viabilidad jurídica.

## Estructura del proyecto

| Componente | Responsables | Mandato |
|---|---|---|
| G1 Reforma fiscal clásica | Ricardo Cantú, Diego Vázquez | ISR, IVA, IEPS, renuncias recaudatorias |
| G2 Finanzas subnacionales | Sunny Villa, José Luis Clavellina | Ingresos propios, federalismo fiscal |
| G3 Seguridad social | Héctor Villarreal, Alejandra Macías | Pensiones, salud, cuidados |
| Transversal macro | Edmundo Molina, Hermilo Cortés | DSGE-OLG, equilibrio general |
| Transversal jurídica | Patricia López | Viabilidad constitucional |

## Objetivo de presión fiscal

| Año | % PIB |
|---|---|
| 2025 (base) | 17% |
| 2036 (meta) | 25% |

Incremento requerido: 8 puntos del PIB en once años.

## Documentos clave

- `docs/` — Propuesta original y nota interna extensa del Core Team
- `neteo/` — Producto integrado final con escenarios alternativos
- `_crossrefs/` — Referencias cruzadas con DFD, BDH y Aurora

## Vínculos

- [[DFD]] — Modelo OLG recibe parámetros de G1 y G3
- [[BDH]] — Trayectorias de gasto en salud
- [[Aurora]] — Escenarios fiscales de largo plazo
EOF
```

---

### `_status.md` — Estado del proyecto

```bash
cat > ~/Dalila/GrandPlan/RF/_status.md << 'EOF'
# RF — Estado del proyecto

**Estado:** CONGELADO (razones políticas) | En preparación técnica activa
**Última actualización:** 2026-04-06

---

## Entregables completados

- [x] Borrador #1 RF Clásica — Ricardo Cantú y Diego Vázquez (julio 2025)
- [x] Diagnóstico subnacional TALD — Villarreal, Cantú, Sánchez (octubre 2023)
- [x] Boletín tenencia CIEP — Emilio Sánchez (septiembre 2024)
- [x] Nota interna extensa Core Team (julio 2025)
- [x] Serie Arena Pública: seguridad social partes I, II, III (jul-oct 2024)
- [x] Artículo "Nuestro largo peregrinar fiscal" (enero 2025)

## Entregables pendientes

- [ ] Borrador #1 Seguridad Social (G3)
- [ ] Borrador #1 Finanzas Subnacionales (G2) — versión RF
- [ ] Modelo OLG calibrado para México (transversal macro)
- [ ] Neteo integrado — versión preliminar
- [ ] Validaciones jurídicas (transversal jurídica)

---

## Disyuntiva anticipada

Cuando el proyecto se reactive, habrá que elegir entre:

**Escenario A — Replanteamiento completo**
Activar los tres grupos y ambas transversales. Producto: neteo integrado
con efectos sobre recaudación, incidencia, sostenibilidad y redistribución.
Horizonte: 2036. Meta: 25% PIB presión fiscal.

**Escenario B — Reforma parcial**
Priorizar G1 (reforma fiscal clásica) y administración tributaria.
Producto: paquete acotado de medidas con estimación de espacio fiscal generado.
Horizonte: corto plazo (1-2 años).

---

## Dependencias activas con otros proyectos

| Proyecto | Flujo | Descripción |
|---|---|---|
| DFD | RF → DFD | Elasticidades de bases gravables, parámetros de informalidad, trayectorias de gasto pensionario |
| DFD | DFD → RF | Consistencia de equilibrio general — cierre en factor markets y presupuesto público |
| BDH | RF → BDH | Escenarios de gasto en salud y fuentes de financiamiento |
| Aurora | RF → Aurora | Escenarios fiscales como insumo para trayectorias estratégicas de largo plazo |

---

## Notas de la última sesión de trabajo

- Arquitectura de archivos preparada: 2026-04-06
- Revisión analítica de G1 completada (Cath): ver `G1_reforma_fiscal_clasica/notas/`
- Revisión de G2 completada (Cath): ver `G2_finanzas_subnacionales/`
- Marco fiscal 2025-2036 registrado desde artículos Arena Pública
EOF
```

---

### `_index.md` — G1 Reforma fiscal clásica

```bash
cat > ~/Dalila/GrandPlan/RF/G1_reforma_fiscal_clasica/_index.md << 'EOF'
# G1 — Reforma fiscal clásica

**Responsables:** Ricardo Cantú Calderón, Diego Alejo Vázquez Pimentel
**Estado:** Borrador #1 completado (julio 2025)

## Mandato

Diagnosticar la estructura impositiva mexicana y proponer ajustes en ISR, IVA e IEPS.
Incluye análisis de bases gravables, tasas efectivas, renuncias recaudatorias, evasión,
informalidad y efectos distributivos. Línea ambiciosa: RFC como plataforma de integración
fiscal y social.

## Hallazgos centrales del borrador #1

- Presión fiscal 2022: 17% PIB (vs. 21.5% promedio ALC, 34% OCDE)
- Tasa efectiva sobre ingresos laborales: 13.1% sobre base de 42.6% PIB
- Tasa efectiva sobre personas físicas con ingresos mixtos: 1.7% (tasa nominal hasta 35%)
- Tasa efectiva IVA sobre consumo: ~9% (tasa nominal 16%)
- Renuncias recaudatorias: ~4.7% PIB

## Propuestas en borrador #1

1. Ajustes progresivos en tarifas ISR
2. Eliminación de exenciones IVA (tasa cero → exento con compensaciones)
3. IEPS tabaco y alcohol
4. Tasas negativas de ISR para pequeños contribuyentes (estímulo fiscal)

## Insumos requeridos para modelo OLG

- [ ] Elasticidades de bases gravables por instrumento (exportar del modelo de microsimulación)
- [ ] Trayectoria proyectada de base gravable 2025-2070 bajo demografía base (Anne)
- [ ] Recaudación potencial bajo formalización completa por tipo de impuesto

## Archivos

- `borradores/` — Capítulo preliminar julio 2025
- `datos/` — ENIGH 2022, SHCP estadísticas oportunas, CEPAL
- `codigo/` — Modelo de elección discreta (informalidad), microsimulaciones
- `notas/` — Revisión analítica Cath
EOF
```

---

### `_index.md` — G2 Finanzas subnacionales

```bash
cat > ~/Dalila/GrandPlan/RF/G2_finanzas_subnacionales/_index.md << 'EOF'
# G2 — Finanzas públicas subnacionales

**Responsables:** Sunny Villa Juárez, José Luis Clavellina Miller
**Estado:** Diagnóstico base disponible (TALD 2023); borrador RF pendiente

## Mandato

Examinar ingresos, gasto y deuda de entidades federativas. Identificar fuentes
de ingresos propios. Analizar financiamiento de educación, salud, infraestructura,
seguridad y pensiones estatales.

## Hallazgos centrales (Diagnóstico TALD + Boletín Tenencia)

- Dependencia de transferencias federales: 84% del ingreso estatal promedio
- Recursos etiquetados por federación: 72.5% del gasto federalizado
- Ingresos propios: 13.1% del total (dominados por impuesto sobre nómina)
- Espacio fiscal estatal promedio 2021: $7,385 pesos per cápita (-21.8% desde 2014)
- Potencial tenencia rediseñada (32 estados): ~125 mil mdp adicionales

## Instrumentos subnacionales subexplotados

| Instrumento | Potencial | Condición |
|---|---|---|
| Tenencia modernizada | Alto — ~125 mil mdp | Requiere Ley General; padrón vehicular |
| Predial | Alto — mediano plazo | Requiere catastros actualizados |
| Impuestos cedulares | Medio | Requiere administración tributaria local |
| Impuestos ambientales | Medio | Requiere marco normativo |

## Meta RF para ingresos subnacionales

De 1.0% PIB (2025) a 2.5% PIB (2036): +1.5 puntos del PIB en once años.

## Insumos requeridos para modelo OLG

- [ ] Proyección espacio fiscal estatal 2025-2036 bajo demografía base
- [ ] Heterogeneidad entre estados: al menos 3 tipos para calibración
- [ ] Pasivo pensionario estatal implícito (actualmente opaco en 11 estados)

## Archivos

- `referencias/diagnostico_TALD.pdf`
- `referencias/boletin_tenencia.pdf`
EOF
```

---

### `_index.md` — G3 Seguridad social

```bash
cat > ~/Dalila/GrandPlan/RF/G3_seguridad_social/_index.md << 'EOF'
# G3 — Seguridad social

**Responsables:** Héctor Villarreal, Alejandra Macías Sánchez
**Estado:** Marco conceptual disponible (serie Arena Pública); borrador RF pendiente

## Mandato

Pensiones, salud, cuidados y seguro de desempleo. Integración entre
seguridad social, asistencia social, RFC e impuestos negativos.

## Marco analítico (serie Arena Pública 2024 + artículo enero 2025)

### Pensiones
- Gasto 2025: 6% PIB (contributivas + no contributivas)
- Proyección CIEP 2030: ~7.1% PIB; meta con reforma: contener en 7% PIB
- Crecimiento sistema reparto: >6% anual por al menos dos sexenios más
- Problemas: generación de transición abierta, pasivos contingentes no reconocidos,
  opacidad entre subsistemas, Modalidad 40

### Salud
- Gasto público actual: ~2.9% PIB (insuficiente bajo cualquier métrica)
- Meta RF: 6% PIB gasto público en salud para 2036
- Dilema Gruber: sistema mixto Bismarck/Beveridge
- Cuotas IMSS destinadas a salud: de 1.5% PIB a 2.5% PIB en 2036

### Cuidados
- Sin sistema reconocido. Gasto federal en cuidados: muy escueto y a la baja
- Opciones de financiamiento: gobiernos subnacionales o extensión seguridad social
- Experiencias: Uruguay (integrado), Costa Rica (adultos mayores), Chile Cuida

## Insumos requeridos para modelo OLG

- [ ] Trayectoria de gasto pensionario 2025-2036 bajo demografía base y alternativa
- [ ] Parámetros de contribución y cobertura IMSS/ISSSTE
- [ ] Perfil de gasto en salud por cohorte de edad

## Archivos

- `referencias/articulos_arena_publica/` — Serie ¿Se puede reformar la seguridad social? (I, II, III)
- `referencias/articulos_arena_publica/` — Nuestro largo peregrinar fiscal (enero 2025)
EOF
```

---

### `_index.md` — Transversal macro (OLG/DSGE)

```bash
cat > ~/Dalila/GrandPlan/RF/transversal_macro/_index.md << 'EOF'
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
EOF
```

---

### `_index.md` — Neteo integrado

```bash
cat > ~/Dalila/GrandPlan/RF/neteo/_index.md << 'EOF'
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
EOF
```

---

### Referencias cruzadas

```bash
cat > ~/Dalila/GrandPlan/RF/_crossrefs/RF_DFD.md << 'EOF'
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
EOF

cat > ~/Dalila/GrandPlan/RF/_crossrefs/RF_BDH.md << 'EOF'
# Referencias cruzadas RF ↔ BDH

## RF → BDH

| Insumo | Origen en RF | Uso en BDH |
|---|---|---|
| Escenarios de financiamiento salud | G3 | Sostenibilidad sistema salud |
| Trayectoria cuotas IMSS | G3 | Flujos de financiamiento BDH |
| Espacio fiscal federal proyectado | neteo/ | Restricción presupuestal BDH |

## BDH → RF

| Output | Uso en RF |
|---|---|
| Proyecciones gasto salud por cohorte | Calibración G3 y transversal macro |
| Escenarios cobertura universal | Parámetros neteo integrado |
EOF

cat > ~/Dalila/GrandPlan/RF/_crossrefs/RF_Aurora.md << 'EOF'
# Referencias cruzadas RF ↔ Aurora

## RF → Aurora

| Insumo | Descripción |
|---|---|
| Escenario A (replanteamiento completo) | Trayectoria fiscal bajo reforma integral |
| Escenario B (reforma parcial) | Trayectoria fiscal bajo reforma acotada |
| Espacio fiscal 2025-2036 | Restricción para escenarios estratégicos Aurora |

## Aurora → RF

| Output | Uso en RF |
|---|---|
| Escenarios de crecimiento económico | Sensibilidad de bases gravables |
| Escenarios de cambio tecnológico | Impacto en mercado laboral formal/informal |
| Escenarios geopolíticos (Gina) | Stress testing sostenibilidad fiscal |
EOF
```

---

### `.gitignore`

```bash
cat > ~/Dalila/GrandPlan/RF/.gitignore << 'EOF'
# Datos sensibles
datos/raw/
datos/microdatos/

# Outputs grandes
modelo/simulaciones/resultados_intermedios/
*.jld2
*.h5

# Entornos
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/

# OS
.DS_Store
Thumbs.db
EOF
```

---

## Paso 3 — Verificar la estructura creada

```bash
find ~/Dalila/GrandPlan/RF -type f | sort
```

---

## Paso 4 — Inicializar Git (si no está ya inicializado en el repo padre)

```bash
cd ~/Dalila
git add GrandPlan/RF/
git commit -m "feat: inicializar arquitectura de archivos RF

- Estructura de directorios para G1, G2, G3
- Transversales macro y jurídica
- Neteo integrado con escenarios A y B
- Referencias cruzadas RF-DFD, RF-BDH, RF-Aurora
- _index.md y _status.md con estado al 2026-04-06"
```

---

## Notas para Claude Code

- Ejecutar los pasos en orden
- Si `~/Dalila/GrandPlan/RF/` ya existe, verificar antes de sobreescribir archivos
- Los archivos `_index.md` son documentos vivos — actualizar conforme avance el proyecto
- Las referencias cruzadas en `_crossrefs/` usan formato de tabla Markdown para facilitar consultas futuras
- El `.gitignore` protege datos sensibles y outputs pesados del control de versiones

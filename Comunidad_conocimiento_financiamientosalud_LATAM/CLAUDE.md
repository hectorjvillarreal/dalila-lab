# CLAUDE.md — Comunidad Latinoamericana del Conocimiento sobre Financiamiento de la Salud

**Raíz:** `/Dalila/Comunidad_conocimiento_salud_LATAM`
**Naturaleza:** Raíz independiente. NO forma parte del árbol `Missions/` ni de `/Grand Plan/`.
**Estatus:** Activo — fase de inicio (2026).
**Última actualización:** Abril 2026.

---

## Qué es este árbol

Esta raíz contiene el trabajo de la **Comunidad Latinoamericana del Conocimiento sobre Financiamiento de la Salud**, una institución académica de la Tríada (Tecnológico de Monterrey, Universidad de los Andes, Pontificia Universidad Católica de Chile) con horizonte estimado de cinco años.

**PI:** Héctor Juan Villarreal Páez (Tec de Monterrey).

Esta es una **institución con financiamiento externo multi-patrocinador**, no una misión analítica de BDH. Comparte espina intelectual con BDH (marco fiscal-demográfico) pero es una entidad separada, con gobernanza y propiedad propias.

El documento fundacional del proyecto —con gobernanza, provenance, equipo, principios éticos y arquitectura— vive en el proyecto de Claude correspondiente y se titula `PROYECTO_Comunidad_Financiamiento_Salud_LATAM.md`. Este CLAUDE.md es el reflejo operativo de ese documento en el sistema de archivos.

---

## Independencia respecto a otros árboles

- Esta raíz es **hermana**, no hija, del árbol `Missions/` y de `/Grand Plan/`.
- No debe reconciliarse, fusionarse ni anidarse bajo BDH ni bajo Missions.
- Lo que la Comunidad toma de BDH (marco analítico, infraestructura de modelación DFD) entra como **referencia o insumo**, nunca como pertenencia estructural.
- Si se encuentra una referencia externa que trate esta raíz como parte de Missions o de BDH, esa referencia está obsoleta y debe corregirse hacia esta arquitectura, no al revés.

---

## Regla estructural innegociable: frontera dura por patrocinador

La Comunidad recibe financiamiento de múltiples patrocinadores farmacéuticos con objetivos específicos distintos (Roche, AMGEN probable, terceros anticipados).

- **Cada patrocinador tiene su propia subcarpeta** desde el día uno: `/roche/`, `/amgen/`, etc.
- **Ningún entregable, paper o actividad queda sin atribución de fondeo.** Todo archivo de trabajo pertenece a la subcarpeta del patrocinador que lo financia.
- Material compartido, transversal o de gobernanza va en subcarpetas neutrales (`/_gobernanza/`, `/_comun/`, `/_crossrefs/`), nunca dentro de la carpeta de un patrocinador.
- Esta separación es una **protección de trazabilidad**: ante cualquier auditoría o pregunta, el rastro de fondos a entregables debe ser inequívoco.

---

## Estructura sugerida del árbol

```
/Dalila/Comunidad_conocimiento_salud_LATAM/
├── CLAUDE.md                  (este archivo)
├── _gobernanza/               (documento fundacional, cláusula de independencia, decisiones)
├── _comun/                    (marco analítico compartido, referencias, insumos de BDH/DFD)
├── roche/                     (etapa inaugural 2026 — objetivos específicos Roche)
│   ├── papers/
│   ├── seminario/
│   └── entregables/
├── amgen/                     (probable — objetivos específicos distintos)
└── _crossrefs/                (protocolos, provenance, build instructions)
```

---

## Principios que rigen el trabajo en este árbol

1. **Independencia analítica.** Ningún patrocinador tiene veto ni revisión previa vinculante sobre las conclusiones. La producción puede analizar críticamente el gasto farmacéutico y los precios de medicamentos sin excepción por identidad del patrocinador.

2. **Rigor sostenido.** Beth es guardiana del rigor: cada producto responde a la pregunta central y sostiene la identidad analítica fiscal-demográfica. Esto es producción intelectual, no plataforma de convocatoria.

3. **Provenance.** Toda decisión estructural se documenta. Los documentos fundacionales se retienen indefinidamente.

4. **Idioma.** El trabajo es principalmente en español, con partes bilingües en inglés según la naturaleza de cada tarea.

---

*Este CLAUDE.md es la autoridad operativa del árbol en Dalila. En caso de conflicto con documentos de misión previos, prevalece este archivo. La autoridad conceptual reside en el documento fundacional del proyecto en Claude.*

# Prueba de comprensión de Qwen3.5-9B sobre el corpus FISCUS (2026-10-31)

Prueba local de si `qwen3.5:9b` (Ollama) entiende documentos SHCP ingeridos con el pipeline RAG
del repositorio de Elena Villalobos (`LDataLab/fiscus`, commit `e39e6d1`). Corrió en una copia
desechable del repositorio; el clon en `../../fiscus-ldatalab/` no se modificó.

Informe completo para Elena: https://claude.ai/artifact/TApgpi5BenAkaHHjEHLjE8

## Archivos

| Archivo | Contenido |
|---|---|
| `run_test.py` | Script de la prueba: 16 preguntas × 2 modos × thinking sí/no |
| `results.jsonl` | Las 62 respuestas, una línea JSON por llamada |

## Diseño

- **Corpus:** Pre-Criterios 2027 (42 pp.) y Miscelánea 2027 Anexo N (6 pp.), en
  `../../económicos_paquetes/2027/`; convertidos con Docling (`t01`), fragmentados (`t02`, 108
  fragmentos con un ejemplo de d01) y embebidos con `multilingual-e5-small` (`t03`).
- **Preguntas:** 8 de hechos (F1–F8), 3 de razonamiento (R1–R3), 5 de disciplina (D1–D5; D5 es un
  fragmento con una instrucción plantada). La clave está en el Anexo A del informe y en los campos
  `expect` del script (verificación gruesa; la calificación final fue manual).
- **Modos:** `comprension` (se dan los fragmentos con la respuesta) y `rag` (top 5 de `retrieve()`
  de `t04`; el ejemplo de d01 se excluye).
- **Prompt:** reglas de `respuestas/c01_chat.py` + citas, fragmentos como datos y fórmula de rechazo.
- **Parámetros:** `num_ctx` 16 384, `temperature` 0.3, `top_p` 0.9, `seed` 7; 100 % GPU.

## Resultados

| Modo | Sin thinking | Con thinking |
|---|---|---|
| Comprensión | 16/16 | 16/16 |
| RAG | 13/15 | 14/15 |
| Mediana de segundos por respuesta | 1.6 (comp.) / 2.6 (RAG) | 34 / 45 |

Ninguna cifra inventada en 62 respuestas. Fallas en RAG: F1 (el rango del PIB solo está en tablas
que no llegaron al top 5) y F5 sin thinking (antepone «No está» y luego da la cifra correcta).

## Campos de `results.jsonl`

`id`, `block`, `mode`, `think`, `question`, `expect`, `gold_in_top5` (solo RAG; `null` si no
aplica), `context_chunk_ids` (ids de `rag.chunks` en esa base de prueba), `answer`,
`thinking_chars`, `seconds`, `eval_count`, `prompt_eval_count`.

## Cómo volver a correrlo

Requiere una copia del repositorio con `uv sync --frozen`, PostgreSQL 17 + pgvector con el esquema
`rag` cargado por `t01`–`t03`, y `ollama pull qwen3.5:9b`. Luego:

```bash
export PGHOST=localhost PGPORT=5433 PGUSER=postgres PGDATABASE=fiscus
<copia>/.venv/bin/python run_test.py <copia> results_nuevo.jsonl
```

El primer argumento es la raíz de la copia (de ahí importa `src/fiscus/rag/t04_retrieve.py`); el
segundo, el archivo de salida. Los `chunk_id` cambian si la base se reconstruye, así que el script
localiza los fragmentos de la clave por texto (`gold`), no por id.

La base de prueba (Postgres en el scratchpad de la sesión) no se conservó; se reconstruye con los
pasos del Anexo B del informe.

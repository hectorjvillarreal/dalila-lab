# Dalila compute envelope — brief for Claude.ai Core Team agents

**For:** Anne · Beth · Cath · Debb · Elle · Fina · Nina (Core Team modular agents on Claude.ai)
**From:** Claude Code (Dalila session, Debb mode)
**Date:** 2026-05-16
**Status:** Verified operational. Persists across shells.

---

## 1. Why this brief exists

You (Claude.ai agent) advise Héctor on Dalila work. You don't execute code on
his machine — you recommend what he should run, write code he'll run himself,
or interpret results he pastes back. This brief tells you what compute is
actually available so your recommendations match the hardware and stack he
has, not generic defaults.

The hardware is more capable than typical advisor defaults assume. Lean
into it. Recommend GPU-accelerated paths confidently. Don't suggest cloud
notebooks or external services when local compute fits.

---

## 2. Hardware envelope

- **Machine:** Lenovo ThinkPad P1 Gen 8, Ubuntu 24.04 LTS.
- **GPU:** NVIDIA RTX PRO 2000 Blackwell Generation Laptop GPU.
  - Compute capability **12.0 (sm_120)** — this is the Blackwell architecture.
  - **8.0 GB VRAM** (`8151 MiB` reported; ~7.5 GB usable after system reservation).
  - Driver: 580.126.09; CUDA driver version 13.0.
- **CPU:** Intel-class workstation laptop (specifics in CLAUDE.md §3 if needed).
- **Terminal stack:** Ghostty → Zsh → Zellij. Long-running jobs go in Zellij
  sessions so they survive disconnects.

The sm_120 / Blackwell architecture is **new** (2024-2025 silicon). Many
default install paths from training-data-era documentation **do not include
sm_120 kernels** and fail at runtime even though they appear to install. See §4.

---

## 3. Verified compute stack (as of 2026-05-16)

All three paths below pass `tests/gpu_check.py` / `tests/gpu_check.jl` with
exit 0 and a 1024×1024 matmul on `cuda:0`. State persists across fresh
shells (`env -i` strip confirmed).

### Python — Miniforge + `dalila` conda env
- Miniforge at `~/miniforge3/`, conda 26.3.2.
- Env: `dalila`, Python 3.12.13, at `~/miniforge3/envs/dalila/`.
- Numerical: NumPy, SciPy, Pandas, Matplotlib (conda-forge).
- **PyTorch:** `torch 2.12.0+cu130` from `https://download.pytorch.org/whl/cu130`. CUDA 13.0, cudnn 9.20, cublas 13.1.1.
- **JAX:** `jax 0.10.0` with `jax[cuda13]` extras. Plugin reuses PyTorch's cu13 NVIDIA libs.
- Numpy 2.4, SciPy 1.17.

### Julia — system install + default env
- Julia 1.11.7 at `/usr/local/bin/julia`.
- Default env: `~/.julia/environments/v1.11/`.
- **CUDA.jl 6.1.0** — CUDA toolchain 13.2 via JLLs (cuBLAS 13.4, cuSPARSE 12.7, cuSOLVER 12.2, cuFFT 12.2, cuRAND 10.4).
- Driver matches: 580.126.9 for 13.2.

### Local LLM — ollama
- Decision finalized May 2026: **Qwen3.5-9B** via ollama.
- 262K-token context window (sufficient for long fiscal documents).
- GPU offload available.
- Use case: RAG queries, document processing, natural-language interface to simulation.

---

## 4. Critical pin: do not regress to cu126 or older PyTorch wheels

PyTorch wheels from indexes `cu124`, `cu126`, and earlier **do not include
sm_120 kernels** and fail at runtime with:

```
torch.AcceleratorError: CUDA error: no kernel image is available for
execution on the device (cudaErrorNoKernelImageForDevice)
```

`torch.cuda.is_available()` returns `True` and the device is correctly
listed, but actual kernel launch fails. PyTorch's own startup warning is
explicit:

> NVIDIA RTX PRO 2000 Blackwell Generation Laptop GPU with CUDA capability
> sm_120 is not compatible with the current PyTorch installation. ... Please
> install a PyTorch release that supports one of these CUDA versions:
> 13.0, 13.2.

**Always recommend** `--index-url https://download.pytorch.org/whl/cu130` for
PyTorch installs on this machine. Same for JAX: prefer `jax[cuda13]` over
`jax[cuda12]`, both for correctness and to avoid a duplicate cu12 NVIDIA
stack alongside the cu13 one already installed.

This pin should be revisited if/when PyTorch ships a cu131/cu132 stable
wheel index that better matches the driver, but cu130 is the current
canonical choice.

---

## 5. Recommendations by workload

### 5a. OLG / DSGE simulation — Julia + CUDA.jl
Cath's primary territory. The DFD calibration engine is Julia-native; the
existing `~/dsge_olg_training/code/` blocks (static GE → two-period → many-
period lifecycle → retirement & survival) are the foundation.

- **Recommend:** `using CUDA` for large numerical kernels. `CuArray{Float32}`
  for the bulk of OLG state arrays. `Float32` over `Float64` when precision
  allows — VRAM is 8 GB, double-precision halves headroom.
- **`KernelAbstractions.jl`** is installed alongside CUDA.jl (came with the
  install) — good for kernel code that should also be CPU-compilable.
- **Profile before optimizing:** `CUDA.@profile`, `CUDA.@time`. Many small
  kernels are slower than a few large kernels — batch operations.
- **Multi-process is fine; multi-GPU is not** — this is a single-GPU
  machine. Don't recommend distributed CUDA setups.

### 5b. ML / data pipelines / RAG — Python (PyTorch or JAX)
- **PyTorch** for: standard supervised ML, fine-tuning, anything with rich
  pretrained-model ecosystem (`transformers`, `peft`, etc.).
- **JAX** for: differential equations, custom-gradient research code,
  jit-heavy numerical work where the JAX compiler's optimization helps.
- Both dispatch to the same GPU; pick whichever has better library support
  for the task. Don't mix in the same script unless there's a real reason.
- **`numpy`-only workloads** stay on CPU — no point moving small arrays to
  device. The transfer cost dominates.

### 5c. RAG corpus build / LLM queries — ollama + Qwen3.5-9B
Debb's territory. PROTO-RAG-001 (`_crossrefs/protocols/PROTO-RAG-001.md`)
governs corpus structure.

- 9B at FP16 fits in 8 GB VRAM with reasonable batch size. Q4 quantization
  if context needs to scale toward the 262K ceiling.
- ollama auto-detects GPU and offloads layers; if you suspect CPU fallback,
  check `ollama ps` for the loaded model's GPU memory footprint.
- For long-document RAG (typical for fiscal corpora), prefer chunking via
  the LLM's own attention with the long context, not pre-chunked retrieval
  windows, when the context fits.

### 5d. Inference-heavy strategic foresight — Aurora
Elle's territory. Mostly LLM-side. Use ollama-hosted Qwen3.5-9B for first
passes; reserve external API calls for cases where the local model
genuinely underperforms.

---

## 6. Per-agent quick guidance

- **Anne** (population economics) — Demographic projections (CELADE, UN WPP)
  are small datasets. CPU/pandas is fine for tabular work. GPU only enters
  if Anne is running large Monte Carlo of cohort scenarios — and even then,
  Julia CUDA.jl beats Python+pandas here.
- **Beth** (social security + health economics) — Same as Anne by default;
  IRMAA-style or microsimulation work would push toward Julia + CuArrays.
- **Cath** (public finance + modeling) — Primary GPU consumer. All major
  simulation work goes here. Always Julia-first.
- **Debb** (infrastructure + workflow) — Owns this brief. RAG ingestion,
  corpus build, env setup. References to `_setup/python_env.md` and
  `tests/gpu_check.{py,jl}` are the canonical truth.
- **Elle** (strategic foresight) — Aurora. Mostly LLM. ollama path.
- **Fina** (cross-project coherence) — No direct compute; she reads outputs.
- **Nina** (code documentation + personal finance) — Light compute. CPU
  paths fine. If touching the simulation engine for documentation passes,
  read CuArray code as you'd read any numerical Julia.

---

## 7. VRAM budget (8 GB) — overflow strategy

When a recommended workload doesn't fit in 8 GB, in priority order:

1. **Mixed precision** (FP16 / BF16) — typical 1.5-2x VRAM relief for
   training; FP32 for accumulation, FP16 for storage.
2. **Gradient checkpointing** — recomputes activations on backward pass;
   trades compute for memory.
3. **Batch reduction + gradient accumulation** — smaller batches, multiple
   backward passes before optimizer step. Math equivalent, slower wall time.
4. **LoRA / parameter-efficient fine-tuning** — only update small adapter
   matrices instead of full model weights.
5. **CPU fallback** — last resort. Surface the trade-off explicitly with
   wall-time estimate.
6. **External compute** (institutional cluster, cloud spot instance) —
   final option. Flag it as a project-level decision, not a default.

For the eventual 2027 ~13B-parameter institutional model (CLAUDE.md §10),
training will exceed 8 GB regardless of tricks. That's a known constraint
and is part of why CIEP and ITED partnership matters. Don't try to fit it
on Dalila's single GPU.

---

## 8. How to invoke compute (instructions to give Héctor)

You (Claude.ai agent) cannot execute these. Give Héctor the exact command
to paste. Patterns:

### Python (from a fresh shell)

```bash
# Option A — direct binary, no activation needed:
~/miniforge3/envs/dalila/bin/python script.py

# Option B — activate first:
source ~/miniforge3/etc/profile.d/conda.sh
conda activate dalila
python script.py
```

### Julia (default env handles CUDA.jl automatically)

```bash
julia script.jl
# or, with a project-specific env:
julia --project=GrandPlan/DFD script.jl
```

### Verification — always recommend before/after env changes

```bash
~/miniforge3/envs/dalila/bin/python ~/Dalila/tests/gpu_check.py
julia ~/Dalila/tests/gpu_check.jl
```

Both exit 0 when CUDA is operational. Either exiting non-zero means
something is wrong — recommend the troubleshooting checks below before
proceeding with workload code.

---

## 9. Troubleshooting cheatsheet

| Symptom | Likely cause | Fix |
|---|---|---|
| `cudaErrorNoKernelImageForDevice` | Wrong PyTorch/JAX wheel (cu12-era) | Reinstall with cu130 index (see §4) |
| `torch.cuda.is_available() == False` | Driver issue, or non-CUDA torch build | Run `nvidia-smi`; reinstall torch from cu130 |
| Julia `using CUDA` `MethodError ... world age` | Inside-function dynamic load | Use top-level `using CUDA` (see `tests/gpu_check.jl`) |
| `out of memory` (CUDA OOM) | VRAM exceeded | See §7; default: FP16 + gradient checkpointing |
| ollama runs on CPU when GPU expected | Wrong build, or driver mismatch | `ollama ps` to confirm; reinstall ollama if needed |
| `numpy not found` from torch | Env missing numpy | `conda install -n dalila numpy` |

---

## 10. Cross-references

- **CLAUDE.md** (Dalila root) — full project orientation including §3 hardware, §7 stack, §8 Core Team, §9 conventions.
- **`_setup/python_env.md`** — canonical Python env reference: install state, activation patterns, package addition, standing pins (cu130, cuda13).
- **`tests/gpu_check.py`** and **`tests/gpu_check.jl`** — durable verification scripts; both exit non-zero on any GPU regression.
- **PROTO-RAG-001** (`_crossrefs/protocols/PROTO-RAG-001.md`) — corpus entry and build instruction protocol.
- **Memory notes** (Claude Code session-local):
  `feedback-dalila-workstation` — treat Dalila as primary compute locus.
  `feedback-gpu-default` — default to GPU paths; verify; surface CPU fallback explicitly.

---

## 11. What this brief does not cover

- Detailed PyTorch / JAX / CUDA.jl APIs — assume training-data knowledge.
- Project-specific calibration choices (DFD, BDH, RF, Aurora) — those live
  in each project's docs.
- Non-Dalila compute (institutional cluster, cloud) — flagged as escalation
  paths in §7 but not specified.
- Long-term roadmap toward the 2027 ~13B-parameter model — CLAUDE.md §10
  is the source.

When in doubt: read CLAUDE.md, then `_setup/python_env.md`, then ask
Héctor for the specific compute target.

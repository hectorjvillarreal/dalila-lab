# Python env setup — Dalila

**Last updated:** 2026-05-16
**Owner:** Debb (infrastructure)
**Scope:** Documents the Miniforge install + `dalila` conda env that hosts
the Python scientific computing stack (PyTorch CUDA, JAX CUDA, pandas, etc.)
referenced by CLAUDE.md §7.

---

## Install state (2026-05-16)

| Component | Location | Version |
|---|---|---|
| Miniforge | `~/miniforge3/` | 26.3.2 |
| Base Python | `~/miniforge3/bin/python` | 3.13.13 |
| `dalila` env | `~/miniforge3/envs/dalila/` | Python 3.12.13 |
| `dalila` pip | `~/miniforge3/envs/dalila/bin/pip` | 26.1.1 |

Miniforge ships `conda-forge` as the default channel.

Shell init was **not** auto-applied (no `conda init zsh` run). The user's
`~/.zshrc` is unchanged. To use the env, see Activation below.

---

## Activation

### Interactive shell (one-off)

```bash
source ~/miniforge3/etc/profile.d/conda.sh
conda activate dalila
```

Confirms with `which python` → `~/miniforge3/envs/dalila/bin/python`.

### Persistent shell integration

Run once if you want `conda` and `conda activate` to work without sourcing:

```bash
~/miniforge3/bin/conda init zsh
```

This appends a managed block to `~/.zshrc`. Restart the shell after.

### Direct binary invocation (no activation needed)

For scripts and one-off commands, use the env's binaries directly:

```bash
~/miniforge3/envs/dalila/bin/python script.py
~/miniforge3/envs/dalila/bin/pip install <pkg>
```

This is the pattern to use from Claude Code tool calls, where shell state
doesn't persist between calls.

---

## Running the GPU verification

`tests/gpu_check.py` must run from inside the `dalila` env (or any env with
torch / jax installed). The system `python3` won't see `torch`.

```bash
# Direct binary path (works from any cwd, no activation):
~/miniforge3/envs/dalila/bin/python ~/Dalila/tests/gpu_check.py

# Or after activation:
conda activate dalila
python ~/Dalila/tests/gpu_check.py
```

Exit code is 0 if at least one Python ML framework (torch or jax) can
dispatch to CUDA. Exit code 1 if the driver is broken OR no framework can
use the GPU.

The Julia counterpart `tests/gpu_check.jl` does not depend on the conda env;
run it with the system `julia` (`/usr/local/bin/julia tests/gpu_check.jl`).
It will use whatever Julia project env is active (default `~/.julia/
environments/v1.11/` unless `--project=<path>` is passed).

---

## Adding packages to `dalila`

Preferred via conda (`conda-forge`) when the package is available there;
falls back to pip when not.

```bash
~/miniforge3/bin/conda install -n dalila -y <pkg>
# or, when needed:
~/miniforge3/envs/dalila/bin/pip install <pkg>
```

Mixing conda and pip in one env is acceptable for the scientific stack but
keep notes: pip installs can shadow conda packages and break solver state.
When pip-installing, prefer wheels with explicit CUDA tags (e.g., the
PyTorch cu130 index) so the install matches the GPU driver.

---

## Standing pins

- **PyTorch** is installed from `https://download.pytorch.org/whl/cu130`
  (verified 2026-05-16: `torch-2.12.0+cu130`, built with CUDA 13.0, cudnn
  9.20, cublas 13.1.1). The cu130 wheels ship Blackwell (sm_120) kernels
  — required for the RTX PRO 2000 Blackwell. **Do not use cu126 or earlier
  wheels:** they were tried on 2026-05-16 and fail at runtime with
  `torch.AcceleratorError: CUDA error: no kernel image is available for
  execution on the device` (`cudaErrorNoKernelImageForDevice`). PyTorch's
  own warning explicitly directs Blackwell users to CUDA 13.0 or 13.2.
  The `tests/gpu_check.py` smoke test (1024×1024 matmul on cuda:0) is the
  canonical check.
- **JAX** when installed: use `pip install -U "jax[cuda12]"` for matching
  CUDA 12 support.

---

## Recreating the env from scratch

If the env is corrupted or you want a clean rebuild:

```bash
~/miniforge3/bin/conda env remove -y -n dalila
~/miniforge3/bin/conda create -y -n dalila python=3.12 pip
~/miniforge3/envs/dalila/bin/pip install torch --index-url https://download.pytorch.org/whl/cu130
# ... plus whatever else
```

The Miniforge install itself lives in `~/miniforge3/` and is independent of
any single env; removing an env doesn't affect Miniforge.

---

## Cross-references

- → CLAUDE.md §3 (hardware), §7 (scientific computing stack), §9 (GPU
  verification convention)
- → `tests/gpu_check.py` and `tests/gpu_check.jl` (durable verification
  scripts)
- → [[feedback-dalila-workstation]] in memory (Dalila as primary compute
  locus)
- → [[feedback-gpu-default]] in memory (GPU-default execution preference)

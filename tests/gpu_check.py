#!/usr/bin/env python3
# Dalila GPU verification — Python stack
# Per CLAUDE.md §9: run after any environment change to confirm CUDA is operational.
# Exit 0 if at least one Python ML framework can use CUDA; exit 1 otherwise.

import shutil
import subprocess
import sys


def section(title: str) -> None:
    bar = "=" * len(title)
    print(f"\n{title}\n{bar}")


def run_nvidia_smi() -> bool:
    section("nvidia-smi (driver + hardware)")
    if shutil.which("nvidia-smi") is None:
        print("FAIL  nvidia-smi not on PATH — NVIDIA driver missing?")
        return False
    cmd = [
        "nvidia-smi",
        "--query-gpu=name,driver_version,memory.total,memory.free,compute_cap",
        "--format=csv",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAIL  nvidia-smi returned {result.returncode}")
        print(result.stderr)
        return False
    print(result.stdout.strip())
    return True


def check_torch() -> bool:
    section("PyTorch")
    try:
        import torch
    except ImportError:
        print("SKIP  torch not installed (`pip install torch --index-url https://download.pytorch.org/whl/cu124`)")
        return False
    print(f"      torch version: {torch.__version__}")
    print(f"      built with CUDA: {torch.version.cuda}")
    if not torch.cuda.is_available():
        print("FAIL  torch.cuda.is_available() == False (CPU-only build, or driver/lib mismatch)")
        return False
    n = torch.cuda.device_count()
    print(f"OK    devices: {n}")
    for i in range(n):
        cap = torch.cuda.get_device_capability(i)
        print(f"      [{i}] {torch.cuda.get_device_name(i)} (sm_{cap[0]}{cap[1]})")
    # Round-trip a small tensor to confirm functional dispatch
    x = torch.randn(1024, 1024, device="cuda")
    y = (x @ x.T).sum().item()
    print(f"      smoke test: 1024x1024 matmul on cuda:0 → scalar {y:.2f}")
    return True


def check_jax() -> bool:
    section("JAX")
    try:
        import jax
    except ImportError:
        print("SKIP  jax not installed (`pip install -U \"jax[cuda12]\"`)")
        return False
    print(f"      jax version: {jax.__version__}")
    gpu_devices = [d for d in jax.devices() if d.platform == "gpu"]
    if not gpu_devices:
        print(f"FAIL  no GPU devices visible to JAX; jax.devices() = {jax.devices()}")
        return False
    print(f"OK    devices: {len(gpu_devices)}")
    for d in gpu_devices:
        print(f"      {d}")
    import jax.numpy as jnp
    x = jnp.ones((1024, 1024))
    y = float((x @ x.T).sum())
    print(f"      smoke test: 1024x1024 matmul on GPU → scalar {y:.2f}")
    return True


def main() -> int:
    print("Dalila GPU check — Python stack")
    hw_ok = run_nvidia_smi()
    torch_ok = check_torch()
    jax_ok = check_jax()

    section("Summary")
    print(f"  nvidia-smi : {'OK' if hw_ok else 'FAIL'}")
    print(f"  PyTorch    : {'OK' if torch_ok else 'not usable'}")
    print(f"  JAX        : {'OK' if jax_ok else 'not usable'}")

    # Exit non-zero if hardware is broken OR no framework can use CUDA.
    if not hw_ok:
        return 1
    if not (torch_ok or jax_ok):
        print("\nNote: GPU is healthy at the driver level but no Python ML framework")
        print("can use it yet. Install torch and/or jax with CUDA support and re-run.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

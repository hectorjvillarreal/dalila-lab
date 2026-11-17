# CryptoABM — package entry point

Companion to `CryptoABM.jl`. It includes the asset-agnostic core (`core/ABMCore.jl`, `core/Moments.jl`) and the bitcoin adapter (`adapters/crypto/CryptoAdapter.jl`), and re-exports the three modules. Use it with `using CryptoABM, CryptoABM.ABMCore, CryptoABM.Moments, CryptoABM.CryptoAdapter`. Design note B0 v1.2 governs it; see `../README.md`.

"""
    CryptoABM

Aurora mechanism laboratory, phase B1 (design note B0 v1.2). Generic core (`ABMCore`,
`Moments`) plus the bitcoin adapter (`CryptoAdapter`). CPU only in B1a.
"""
module CryptoABM
include("core/ABMCore.jl")
include("core/Moments.jl")
include("adapters/crypto/CryptoAdapter.jl")
using .ABMCore, .Moments, .CryptoAdapter
export ABMCore, Moments, CryptoAdapter
end

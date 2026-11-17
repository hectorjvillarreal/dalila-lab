# Cath — Review of B1b (GPU kernel)

*Commit 6d19589. I read `BatchGPU.jl` and its `.md`, `b1b_timing.jl`, the B1b report and `b1b_timing.txt`. I compared the kernel line by line with `ABMCore.jl` (`clear!`, `simulate!`) and `CryptoAdapter.jl` as they stand after the B1a fixes; the adapter is unchanged since 999b613. I ran nothing and edited nothing. 2026-11-17.*
*Filed verbatim by Claude Code, 2026-11-17. Fixes 1, 2, 4 and 5 were applied in the commit that filed this memo. Fix 3 is recorded in `BatchGPU.md` for any B3 GPU objective.*

## Verdict

**Approve with minor fixes (listed; no re-check needed).** The kernel implements the same model as the CPU engine. I found no race and no deadlock. Leaving the non-price state off the GPU is safe in B1. The fixes are guards that stop a future change from making the two engines diverge silently.

## Findings

**Same model:**
- **Cumulative-flow clearing: matches.** `XC_` is reset at the ordinary clearing (`BatchGPU.jl:184`), and `clear_shared!` (`:94–105`) is the same as `ABMCore.jl:158–168` under both laws, in Float64.
- **λ cap and frozen σ̂: match.** `SIG_` is written only by thread 1 after the loop (`:257`). The margin requirement is computed once before the loop (`:197`), as `ctx.σhat` is on the CPU.
- **Decay before the σ̂ update: matches** (`:248–257` vs `ABMCore.jl:296–300`).
- **Order of operations: matches.** Ordinary orders → clear → settle → cascade → conviction flags and peaks → leveraged countdown → funding when `step % (K÷3) == 0`, at the last cleared price → decay → σ̂.
- **Daily low and close: match.** The low takes every clearing price and the post-decay price (`:103`, `:260`) and is reset daily (`:147`). The close is the post-decay price.
- **Momentum ring: correct.** It reads `day − h` with h ≤ 63 and writes `day` mod 64 at the end of the day, so a slot is never read in the same day it is written. The `h_max < WMAX` assert guards this (`:285`).
- **Leveraged traders: match.** Equity is injected at the pre-clear price and liquidation uses the same test (`:206` vs `CryptoAdapter.jl:249`). A position closes when l_q + (−l_q) = 0 exactly. The countdown restarts and then falls in the same sub-step, as on the CPU.
- **Conviction flags and re-entry: match** (`:155`, `:202`, `:228–235`).
- **Cascade rules and the cap: match.** The cap is N_c + N_l + 1, the same N + 1 as the CPU's `n_constrained`.

**Synchronisation:**
- Every `bsum` is reached by all threads. The break conditions read `red[1]` after a sync, so all threads see the same F and round count, and the funding branch tests `step`, which is the same for all threads.
- Every read of shared state by the other threads comes after a sync that follows thread 1's write (`:144`, `:148`, `:187`, `:217`, `:262`, `:271`).
- The trailing sync in `bsum` (`:85`) stops `red` being overwritten before every thread has read it.
- So there is no divergent barrier and no read before write.

**Non-price state:** In the CPU engine, none of the liquidity provider's books, the loss fund, the ledger, or conviction and momentum cash is ever read by `clear!`, `impact_lambda` or any agent rule. Only leveraged cash, through equity, reaches prices, and the kernel tracks it. Leaving the rest out is safe *for B1 only*. A liquidity-provider capacity limit or wealth-dependent sizing (B1a limitation 9) would break this silently.

**Float32:**
- Leveraged equity is cash + q·p, a cancellation between two terms of size about 1e-3 that leaves about 7e-5. Float32 error is about 1e-10, against a liquidation threshold of about 1e-5. Flow reductions and prices carry a relative error of about 1e-7.
- None of these has a systematic sign. Box–Muller on 24-bit uniforms cuts the normal off at 5.77σ, which would make gaps *shallower*, not deeper.
- The −2.74 z on the linear gap has no mechanism behind it that I can find. With 20 tests, the chance that the largest |z| reaches 2.74 is about 12 %, so the report's "chance" reading is fair.

**Gaps that can be fixed in place:**
- `gp_from` (`:44–47`) silently drops any `Params` field it does not know, so a new behaviour parameter would make the GPU run a different model.
- The cap flag is only returned (`:291`), so a hit counts as an error only if the caller checks it. `b1b_timing.jl:28` checks it; a B3 objective might not.
- There is no non-finite check, unlike `fit.jl:76`.
- There is no `cascade = false` ablation on the GPU. That is acceptable if documented.

## Fixes

1. **`BatchGPU.jl:44`.** Before `gp_from`, add:
   ```julia
   const KNOWN_PARAMS = (:K, :w_c, :w_m, :w_l, :N_c, :N_m, :N_l, :D_median, :s_D, :sell_frac, :reentry,
       :β, :h_min, :h_max, :θ, :L_median, :s_L, :m0, :m1, :close_hazard, :reopen_delay, :β_l,
       :funding_c, :funding_max, :σ_ε, :λ0, :κ, :λmax_mult, :φ, :ρ, :σbar, :impact, :q0)
   ```
   Make the first line of `gp_from`:
   ```julia
   Set(fieldnames(typeof(p))) == Set(KNOWN_PARAMS) || error("Params changed; update BatchGPU before use")
   ```
2. **`BatchGPU.jl:291`.** Replace with:
   ```julia
   Array(flag)[1] != 0 && error("cascade cap bound on the GPU (a bug, never data)")
   Array(dC), Array(dL)
   ```
   Then drop `hit` from `b1b_timing.jl:27–28` and from the docstring.
3. **Any GPU objective in B3.** Before `fullvec`, add `any(!isfinite, c) && return fill(NaN, length(MD))` and map that to J = Inf, as `fit.jl:76` does.
4. **`BatchGPU.md`, Scope.** Add: "This holds only while no price rule reads cash, liquidity-provider books or the loss fund. A liquidity-provider capacity limit, wealth-dependent sizing or a `cascade = false` ablation needs the kernel extended and the gate re-passed. Speed-up was measured under linear impact only."
5. **B1b report, l.45.** Replace "about what chance alone produces" with: "With 20 tests, the chance that the largest |z| reaches 2.74 is about 12 %, and no mechanism for a GPU-side bias was found (review, Cath). If the GPU drives calibration, repeat the gap comparison on 4,000 fresh paths."

## Not checked

I did not rerun the gate or the GPU check, and I did not check the RNG's statistical quality beyond the points above.

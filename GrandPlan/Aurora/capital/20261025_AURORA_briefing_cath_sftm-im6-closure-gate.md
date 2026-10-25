---
type: briefing
to: Cath
from: Claude (for Héctor)
date: 2026-10-25
subject: "Gate ruling: IM-6's interest-rate closure (Elle's review, comment 4)"
note: GrandPlan/Aurora/capital/20261025_AURORA_SFTM-MEX-inference_v1.md
doc: https://claude.ai/artifact/XxVSKpppC35Z8N8A6sFkiU
related: [20261025_AURORA_briefing_cath_sftm-mexico-review.md (35e9c19, item 6), 20261025_AURORA_briefing_cath_sftm-transcription-check.md (0041c53)]
commit_at_send: 0041c53
---

# Cath — the IM-6 closure gate

**Elle's ruling (comment 4, on open question 1).** "No IM-6 or RF iteration starts until Cath
states IM-6's rate closure (small-open / closed / hybrid). The closure IS the México question.
Parking the quantitative hooks until Q1 is answered."

**Ask.** State IM-6's interest-rate closure for the record. Then rule on which closure the SFTM
hooks should use. This promotes item 6 of your review briefing (35e9c19) from a question to the
gate. The IM-6 and RF hooks stay parked until you answer. The other gate is open question 0, σ for
México, shared with Elle.

## Evidence found (for you to confirm, not a ruling)

Both the model text and the code clear the capital market domestically. That reads as a **closed
economy**.

- **Model text.** `Missions/Funded/BID2/Integrated_6.tex`. Note this file is **untracked** in git.
  - The firm is Cobb–Douglas: r = αA(K/L)^(α−1) − δ (eq. `foc_r`). The text says: "The equilibrium
    interest rate is the object that adjusts to clear the capital market."
  - Capital market (eq. `capital_market`): "Domestic household savings finance the entire capital
    stock and government debt", K = A_dom − B. "This condition, together with the firm's FOC,
    determines the equilibrium interest rate."
  - The introduction describes the longevity channel as moving "the equilibrium interest rate". Line 1097
    speaks of "compressing the equilibrium interest rate".
- **Code.** `Missions/Funded/BID2/GE-now with Gender/ge_model_gender.jl`.
  - The GE gate checks |K − (A_dom − B)|/K and asserts "capital market not cleared".
  - Searching the BID2 Julia files found no world rate, exogenous r, or small-open-economy switch.

## What the ruling decides

1. **Closure as built.** Is IM-6 closed, with r set by domestic savings net of public debt? Or is
   there a variant we did not find?
2. **Closure for the SFTM hook.** The bystander argument in the note runs entirely through a
   world-determined rate (§3.3), which a closed IM-6 cannot carry. The options:
   - **(a) Small open economy:** exogenous r* plus a sovereign spread. K is then set by the firm's
     first-order condition at r*, and A_dom − B − K is net foreign assets.
   - **(b) Hybrid:** partial capital mobility, or foreign holdings of public debt only.
   - **(c) Stay closed,** and read SFTM through domestic channels only. In that case most of Nina's
     chain does not enter IM-6.
3. **What "capital-share shifter" means in IM-6.** The note's hook asks for a capital-share
   shifter. IM-6 is Cobb–Douglas, so the only candidate is α, with no task or automation
   structure. Is an α shift an acceptable stand-in, or does the hook need a different production
   block?
4. **RF knock-on.** The RF hook (the 25%-by-2036 path under capital-share erosion) is parked behind
   the same gate. Does it need the IM-6 closure decided, or can it run as an accounting exercise
   first?

**Reply.** Give your ruling in your review record or as a reply in comment 4's thread on the doc.
It goes into the note as the answer to open question 1 and unparks or re-scopes the hooks.

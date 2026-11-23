# Crypto (BTC, ETH) Brunnermeier-Reis Regime Monitor

Aurora · standalone exercise · created 2026-11-16 at Héctor's request.
Brief: [`../Aurora_Nina_CRYPTO_BR_Spec_ClaudeCode_202611.md`](../Aurora_Nina_CRYPTO_BR_Spec_ClaudeCode_202611.md), Part A.
Adapted from the SPCX board (`../spcx_monitor/`). The code is copied, not imported, so the two boards change independently.
Build instruction: `_crossrefs/_build_instructions/2026-11-16_aurora_crypto_board_and_abm_b0.md` (PROTO-RAG-001 provenance).

## What this is, and is not

It is a regime-identification board for bitcoin and ether. Its only outputs are mechanism states (GREEN / AMBER / RED / INERT), the observable that drove each state, and the next escalation trigger.

It has no price target, no fair value, no buy/sell and no expected return. An output of that kind means the board has failed its brief.

**Firewall (brief §0).** Nina's agent-based model (brief Part B) lives outside this board. No ABM output is ever written into `state/*.json`. An ABM result can change this board only through a ruling by Héctor, recorded with provenance in the state text and the run log.

**Classification is an analyst act.** The daily automation carries values forward, fetches spot and macro, and renders. It never classifies. Mechanisms stay `UNSET` until Héctor, or an analyst he explicitly delegates, sets them on a manual pass.

## Rulings

- **2026-11-16 (Héctor, brief §7, proposed defaults accepted):**
  - Q1: BTC and ETH only.
  - Q2: the LatAm stablecoin-dollarization hook on Currency Mismatch stays greyed out; it activates only by ruling.
  - Q3: AGGREGATOR-grade derivatives data (open interest, funding, liquidations) may drive a Fire Sales leg when **two independent sources** agree; press still escalates nothing.
  - Q4: the board runs as step 3c inside `~/.local/bin/spcx_render.sh`, not on its own timer.
  - Q5: board first; the ABM design note (B0) comes after.
- **2026-11-23 (Héctor, proposed defaults accepted):**
  - P1 peg band: a break is a USDT or USDC daily close below 0.995 on two venues (Kraken, Coinbase); a close below 0.998 on two venues supports AMBER.
  - (l): a realised liquidation cascade above the volume bar counts toward Fire Sales AMBER for 10 sessions after it ends (read as 10 UTC daily closes).
  - (m): "debt coming due" under mNAV ≤ 1 means a holder put or a maturity within 12 months.
- **Not yet ruled:** the liquidation-volume bar (RED, and the (l) trigger) and the funding/open-interest levels that count as "stretched". Until they are ruled, the threshold text is qualitative, and a pass that wants to escalate must propose the band as a question.

## Source grades

Every observable's text starts with its grade and date:

| Grade | Examples | Can escalate? |
|---|---|---|
| FILED | SEC filings (treasury companies' 10-Q/8-K, miners' 8-K, ETF prospectuses), issuer reserve attestations | Yes |
| MARKET | Coinbase UTC daily closes; ETF shares outstanding from the issuer's daily file | Yes |
| AGGREGATOR | Perpetual-futures open interest, funding, liquidations; on-chain exchange reserves | Only with two independent sources (Q3) |
| PRESS | News reports | No — until filed |

No fabricated numbers: an unavailable value renders as "— unset / manual".

## Manual-pass checklist

1. **Spot.** `python3 crypto_monitor.py fetch-spot <date>` pulls the Coinbase BTC-USD / ETH-USD UTC daily close. It refuses until that UTC day has ended (00:00 UTC = 18:00 CST).
2. **Runs.** Compute ETF net flows from each issuer's shares-outstanding history (IBIT, ETHA and peers): Δshares × NAV, dated. Record stablecoin supply (USDT, USDC), peg deviation from $1.00, and the date of the latest reserve attestation.
3. **Fire Sales.** Read open interest, funding and liquidations from two independent aggregators and record both. Read treasury companies' latest filings: holdings, market value relative to holdings, debt maturities and conversion terms. Record miners' debt and hashprice, and the ETH liquid-staking discount.
4. **Interconnections.** Record ETF custodians (prospectus), stablecoin issuers' T-bill holdings (attestations), and miners' AI-hosting contracts (8-K). For corporate holders, record filed only. The SpaceX holding (18,712 BTC) is owned by the SPCX board (`issuer_crypto_holdings`); cite it here, don't copy it.
5. **Macro.** Run `fetch-macro` (FRED: TIPS 10y, VIX, Fed upper bound). If FRED times out, enter values by hand from the Treasury real-yield CSV and Cboe. The rotation gauge is the SPCX board's gauge (its README item 6); copy the reading with its date.
6. **Blind spots.** Re-read `known_blind_spots` on each live panel and date any change.
7. **Classify, or leave UNSET.** An AMBER or RED needs a non-empty `driving_observable`; the tool refuses it otherwise. Prepend new text and keep the old as `|| PRIOR (date): ...`, as on the SPCX board.

Commit drafts **before 18:00**: the cycle's `reset --hard main` destroys uncommitted state edits. Check `systemctl --user status spcx-render.service` before editing. Use `python3`; `python` is not on the bare zsh path.

## Automation

Step 3c of the SPCX daily cycle (`~/.local/bin/spcx_render.sh`; backup of the previous script `spcx_render.sh.bak-20261116`) runs, non-fatally:

```
new <today>        # only if state/<today>.json is absent (no clobber)
fetch-macro <today>
fetch-spot  <today>
render
```

The cycle then commits `crypto_monitor/` together with the SPCX and NVDA folders and pushes. It shares the cycle so the jobs never race for the git index on boot catch-up. The worktree's sparse-checkout includes `GrandPlan/Aurora/crypto_monitor` (added 2026-11-16). If you tear the folder down, remove step 3c in the same change.

## Files

- `taxonomy.py` — the single source of truth for mechanisms, observables and thresholds; the rulings are in its docstring.
- `crypto_monitor.py` — `new`, `render`, `status`, `fetch-macro`, `fetch-spot` (stdlib only).
- `state/YYYY-MM-DD.json` — one reading per day; the source of truth.
- `dashboard.html`, `run_log.md` — generated by `render`; never edit by hand.

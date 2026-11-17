# CryptoAdapter — bitcoin instance (B1)

Companion to `CryptoAdapter.jl`. It implements design note B0 v1.2, §3.1 and §4.

## Units
- Holdings and orders are in BTC as a share of the float.
- Cash is in the numéraire, with p₀ = 1.
- Perp and spot trade at one price (instant arbitrage assumed).

## Classes
| Class | Rule | Forced? |
|---|---|---|
| `Conviction` | Holds. Once the drawdown from its own peak reaches D_i (log-normal across agents), it sells `sell_frac` of its holding. It is then flagged until it has fully re-entered, buying back once the drawdown is under D_i/2. | Yes: fires once per crossing |
| `Momentum` | Target (w_m/N_m)·tanh(β·z_h), with z_h = h-day log return / (σ̄√K·√h), adjusted at speed θ per sub-step | No |
| `Leveraged` | Opens with injected equity, so \|q\| = w_l/N_l and leverage is L_i. Direction comes from trend plus noise. It is liquidated when equity < m(σ̂)·\|q\|·p, closes at random, and pays or receives funding every K/3 sub-steps against the liquidity provider. A shortfall goes to `LossFund`. | Yes: liquidation |
| `NoiseFlow` | σ_ε·ε_s, with ε_s ~ N(0, 1/K): the instance's only exogenous input | No |

`build_world(params, rng)` assembles one market and the classes. Classes with zero share are left out. `load_coinbase_csv` reads the snapshot CSVs.

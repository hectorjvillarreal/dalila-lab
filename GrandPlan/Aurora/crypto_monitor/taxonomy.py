"""Crypto (BTC, ETH) Brunnermeier-Reis regime taxonomy — static specification.

Encodes the five amplification mechanisms from Brunnermeier & Reis,
*A Crash Course on Crises* (Princeton UP, 2023), as applied to bitcoin and
ether in the Aurora build brief
(../Aurora_Nina_CRYPTO_BR_Spec_ClaudeCode_202611.md, Part A, §2).

This module is the SINGLE SOURCE OF TRUTH for what each mechanism is, whether
it is structurally live for BTC/ETH, which observables feed it, and the
threshold logic that maps observables to GREEN / AMBER / RED.

Discipline (brief §0): this taxonomy produces *regime states and escalation
triggers* only. It contains no price target, no directional view, no expected
return. INERT mechanisms are retained, not omitted.

FIREWALL (brief §0): no output of Nina's ABM (brief Part B) is ever written
into a state file. An ABM result reaches this board only through a ruling by
Héctor, recorded with provenance.

Rulings of 2026-11-16 (Héctor accepted the proposed defaults, brief §7):
  Q1 scope BTC and ETH only · Q2 LatAm stablecoin-dollarization hook greyed
  out · Q3 AGGREGATOR-grade derivatives data may drive a Fire Sales leg when
  two independent sources agree (press still escalates nothing) · Q4 runs as a
  step inside the 18:00 SPCX cycle · Q5 board first, ABM design note after.
Numeric bands (peg band, liquidation-volume bar, etc.) are NOT yet ruled; the
threshold text below is qualitative until they are.
"""

# State vocabulary. Order matters for severity comparisons.
STATES = ["GREEN", "AMBER", "RED"]
SEVERITY = {"UNSET": -1, "INERT": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

# The three LIVE mechanisms whose *simultaneous* RED is the self-reinforcing
# crash configuration the taxonomy exists to catch.
CRASH_CONFIG_SET = ["runs", "fire_sales", "interconnections"]

# Source grades (brief §3). Every observable's text should start with one.
SOURCE_GRADES = ["FILED", "MARKET", "AGGREGATOR", "PRESS"]

MECHANISMS = [
    {
        "id": "runs",
        "number": 1,
        "name": "Runs",
        "status": "LIVE",
        "definition": (
            "A coordination failure in which holders rush to exit because they "
            "expect others to exit, making the exit self-fulfilling. Applies to "
            "any claim redeemable or sellable faster than the underlying can absorb."
        ),
        "rationale": (
            "Three run objects: spot-ETF holders (IBIT, ETHA and peers) whose "
            "redemptions hit spot; stablecoin holders (USDT, USDC) whose redemptions "
            "force the issuer to sell reserves; exchange depositors."
        ),
        "observables": [
            "etf_net_flows",                 # MARKET: derived from issuers' daily shares-outstanding files
            "stablecoin_supply_change",      # MARKET/FILED: USDT, USDC circulating supply
            "stablecoin_peg_deviation",      # MARKET: distance from $1.00
            "stablecoin_reserve_attestations",  # FILED/published, dated
            "exchange_reserves",             # AGGREGATOR (on-chain)
            "known_blind_spots",
        ],
        "thresholds": {
            "GREEN": "ETF flows mixed; stablecoin pegs at par.",
            "AMBER": "Persistent ETF outflows on falling price, or a peg deviation "
                     "beyond the ruled band (band not yet ruled).",
            "RED": "Outflows accelerating together with a peg break or a halt on "
                   "redemptions.",
        },
    },
    {
        "id": "fire_sales",
        "number": 2,
        "name": "Fire Sales / Leverage",
        "status": "LIVE",
        "definition": (
            "Asset-price declines force deleveraging by holders who financed "
            "positions with debt or hold obligations collateralized by the asset; "
            "forced selling depresses prices further, in a reflexive loop."
        ),
        "rationale": (
            "Perpetual futures liquidate automatically at known margins; treasury "
            "companies hold coins financed with convertibles or preferred stock; "
            "miners carry debt against hashprice; ETH liquid-staking tokens can trade "
            "at a discount that forces levered unwinds."
        ),
        "observables": [
            "perp_open_interest",            # AGGREGATOR: two independent sources (ruling Q3)
            "perp_funding_rates",            # AGGREGATOR: two independent sources (ruling Q3)
            "liquidation_volume",            # AGGREGATOR: two independent sources (ruling Q3)
            "treasury_company_mnav_and_debt",  # FILED: 10-Q / 8-K of corporate holders
            "miner_debt_and_hashprice",      # FILED + AGGREGATOR
            "eth_liquid_staking_discount",   # MARKET: staking-token price vs ETH
            "known_blind_spots",
        ],
        "thresholds": {
            "GREEN": "Leverage moderate; no treasury company near a financing wall.",
            "AMBER": "Elevated open interest with stretched funding, or a treasury "
                     "company trading below its holdings with debt coming due.",
            "RED": "A liquidation cascade in progress (volume bar not yet ruled), "
                   "or a filed forced sale by a treasury company.",
        },
    },
    {
        "id": "interconnections",
        "number": 3,
        "name": "Interconnections",
        "status": "LIVE",
        "definition": (
            "The network of cross-exposures through which distress at one node "
            "propagates to others. The vulnerability is the topology of "
            "dependencies, not any single balance sheet."
        ),
        "rationale": (
            "Exchange-custodians hold the ETFs' coins; stablecoin issuers hold large "
            "T-bill books (the Duffie-Reis money-market link); miners are moving into "
            "AI hosting (links to the Nvidia/CoreWeave/SPCX web); corporate holders "
            "carry coins on their balance sheets (SpaceX: 18,712 BTC, filed)."
        ),
        "observables": [
            "etf_custodian_concentration",   # FILED: ETF prospectuses / 10-K
            "stablecoin_issuer_tbill_holdings",  # FILED/published attestations
            "miner_ai_hosting_links",        # FILED: miners' 8-K / 10-Q
            "corporate_holders",             # FILED only; SpaceX row is owned by the SPCX board
            "known_blind_spots",
        ],
        "thresholds": {
            "GREEN": "No node under stress.",
            "AMBER": "Stress at one node (custodian incident, attestation delay, "
                     "miner default).",
            "RED": "Simultaneous stress at connected nodes.",
        },
    },
    {
        "id": "currency_mismatch",
        "number": 4,
        "name": "Currency Mismatch",
        "status": "INERT",
        "definition": (
            "Vulnerability from holding liabilities in one currency and "
            "assets/revenue in another; original-sin dynamics, dollar-denominated "
            "debt against local-currency revenue."
        ),
        "rationale": (
            "BTC and ETH are not issuers and carry no liabilities: no asset-level "
            "mismatch. Considered and ruled out. Dormant hook (ruling Q2, 11-16, greyed "
            "out): dollar-stablecoin use as a dollarization channel in Latin America "
            "(Argentina, Mexico) — USD claims held against peso incomes. Activates "
            "only by ruling."
        ),
        "observables": [],
        "thresholds": {},
    },
    {
        "id": "inflation_deflation",
        "number": 5,
        "name": "Inflation-Deflation Spiral",
        "status": "INERT",
        "definition": (
            "The fiscal-monetary channel — monetization, the fiscal theory of the "
            "price level, the debt-deflation interaction."
        ),
        "rationale": (
            "A non-issuer asset does not generate an inflation-deflation spiral — inert "
            "at the asset level. The macro hook (real rates, rotation, liquidity, and "
            "stablecoin T-bill demand) lives in the context panel, not as a trigger."
        ),
        "observables": [],
        "thresholds": {},
    },
]

# Macro-backdrop context panel. NOT an escalation trigger — a gauge.
MACRO_BACKDROP = {
    "id": "macro_backdrop",
    "name": "Macro Backdrop (context — not a crypto trigger)",
    "observables": [
        "tips_10y_real_yield",       # FRED DFII10
        "vix_level",                 # FRED VIXCLS
        "fed_funds_target_upper",    # FRED DFEDTARU
        "vix_trend",
        "narrative_vs_cashflow_rotation",  # same gauge as the SPCX board (README item 6 there)
        "broad_risk_on_off",
        "stablecoin_tbill_share",    # stablecoin T-bill holdings vs the bill market (Duffie-Reis link)
    ],
    "note": (
        "Conditions belief-driven assets but does not by itself escalate any crypto "
        "mechanism."
    ),
}

# Convenience lookups.
BY_ID = {m["id"]: m for m in MECHANISMS}
LIVE_IDS = [m["id"] for m in MECHANISMS if m["status"] == "LIVE"]
INERT_IDS = [m["id"] for m in MECHANISMS if m["status"] == "INERT"]

"""SPCX Brunnermeier-Reis regime taxonomy — static specification.

Encodes the five amplification mechanisms from Brunnermeier & Reis,
*A Crash Course on Crises* (Princeton UP, 2023), as applied to SPCX in the
Aurora build brief (Aurora_Nina_SPCX_BR_Spec_ClaudeCode_202606.md, §2).

This module is the SINGLE SOURCE OF TRUTH for what each mechanism is, whether
it is structurally live for SPCX, which observables feed it, and the threshold
logic that maps observables to GREEN / AMBER / RED.

Discipline (brief §0, §4): this taxonomy produces *regime states and escalation
triggers* only. It contains no price target, no directional view, no expected
return. INERT mechanisms are retained, not omitted — knowing what was ruled out
is half the discipline.
"""

# State vocabulary. Order matters for severity comparisons.
STATES = ["GREEN", "AMBER", "RED"]
SEVERITY = {"UNSET": -1, "INERT": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

# The three LIVE mechanisms whose *simultaneous* RED is the self-reinforcing
# crash configuration the taxonomy exists to catch (brief §3.5).
CRASH_CONFIG_SET = ["runs", "fire_sales", "interconnections"]

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
        "spcx_rationale": (
            "The relevant 'run' is a coordinated exit by belief-driven holders. "
            "The vulnerability is holder-base composition — fast, sentiment-driven "
            "capital vs. locked-up or conviction-held stock."
        ),
        "observables": [
            "lockup_restricted_share_pct",   # Class B / founder / employee float under lockup
            "free_float_classA_pct",
            "next_lockup_expiry_date",
            "next_lockup_expiry_size_pct",   # step-change in free float at that date
            "turnover_ratio",                # daily volume / free float
            "holder_concentration",          # retail / institutional / crossover-belief mix
            "etf_passive_inclusion_status",
        ],
        "thresholds": {
            "GREEN": "High lockup share, low turnover, stable holder base.",
            "AMBER": "Approaching a lockup expiry; turnover rising; sentiment softening.",
            "RED": "Lockup expiry coincident with negative sentiment shift; "
                   "turnover spike on falling price.",
        },
    },
    {
        "id": "fire_sales",
        "number": 2,
        "name": "Fire Sales / Balance-Sheet Channel",
        "status": "LIVE",
        "definition": (
            "Asset-price declines force deleveraging by holders who financed "
            "positions with debt or hold obligations collateralized by the asset; "
            "forced selling depresses prices further, in a reflexive loop."
        ),
        "spcx_rationale": (
            "SPCX carries a concrete version via stock-denominated obligations. If "
            "SPCX falls, obligations priced in SPCX stock reprice simultaneously and "
            "can force selling or trigger contingent payments."
        ),
        "observables": [
            "cursor_acq_stock_component",    # large Class A stock component; termination/deferred fees
            "valor_equipment_lease_exposure",
            "margin_lending_against_spcx",
            "insider_pledged_shares",
            "counterparties_holding_spcx_as_asset",
            "convertible_or_stock_settled_instruments",
            "nearest_stock_price_trigger",   # price level at which an obligation/margin strains
        ],
        "thresholds": {
            "GREEN": "Obligations well-covered at current price; ample headroom "
                     "above any stock-price triggers.",
            "AMBER": "Price approaching levels where stock-settled obligations or "
                     "margin become strained.",
            "RED": "Price below trigger levels forcing contingent payments, margin "
                   "calls, or pledged-share liquidation.",
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
        "spcx_rationale": (
            "SPCX sits at the center of a dense web: xAI (absorbed subsidiary), "
            "Anthropic (compute customer at Colossus/Memphis), Valor (board-linked "
            "lessor, ~$20B exposure), Cursor (pending acquisition), and the "
            "TD-frontier IPO pipeline (OpenAI/Anthropic reportedly watching)."
        ),
        "observables": [
            "counterparty_web_status",
            "compute_revenue_dependency",    # SPCX revenue depends on AI-sector demand,
                                             # which depends on the same sentiment cycle (reflexive)
            "ipo_pipeline_status",           # a failed OpenAI/Anthropic listing reprices the narrative
            "vendor_customer_concentration",
        ],
        "thresholds": {
            "GREEN": "Counterparty web stable; no node under stress.",
            "AMBER": "Stress at one node (AI-sector capex slowdown, IPO-pipeline wobble).",
            "RED": "Simultaneous stress across multiple connected nodes; reflexive "
                   "compute-revenue/sentiment loop turning negative.",
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
        "spcx_rationale": (
            "SPCX is USD-denominated, USD-listed, USD-revenue. No first-order "
            "currency mismatch at the asset level. Considered and ruled out — not "
            "overlooked. Dormant hook: any future FX-denominated revenue or "
            "obligation could reactivate this."
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
        "spcx_rationale": (
            "A single equity does not generate an inflation-deflation spiral — inert "
            "at the asset level. Retains a MACRO-LIQUIDITY hook: the backdrop "
            "conditioning belief-driven assets (real rates, capital rotation, "
            "liquidity appetite) lives here as context, not as an SPCX trigger. "
            "Bridge to Nina's wider monetary regime (Duffie-Reis balance-sheet "
            "transition, real-rate level)."
        ),
        "observables": [],
        "thresholds": {},
    },
]

# Macro-backdrop context panel (brief §2.5). NOT an escalation trigger — a gauge.
MACRO_BACKDROP = {
    "id": "macro_backdrop",
    "name": "Macro Backdrop (context — not an SPCX trigger)",
    "observables": [
        "tips_10y_real_yield",       # FRED DFII10 — opportunity cost anchor for non-cash-flow assets
        "vix_level",                 # FRED VIXCLS
        "vix_trend",
        "narrative_vs_cashflow_rotation",  # bitcoin vs. cash-flow assets — the canary
        "broad_risk_on_off",
    ],
    "note": (
        "Conditions belief-driven assets but does not by itself escalate any SPCX "
        "mechanism. Supplied as a backdrop gauge per brief §2.5 / §5."
    ),
}

# Convenience lookups.
BY_ID = {m["id"]: m for m in MECHANISMS}
LIVE_IDS = [m["id"] for m in MECHANISMS if m["status"] == "LIVE"]
INERT_IDS = [m["id"] for m in MECHANISMS if m["status"] == "INERT"]

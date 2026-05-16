"""
Mexico population through 2050 — simple practice plot.

Data: UN WPP 2024 medium-variant projections, via OWID's
`population-long-run-with-projections` dataset (combines historical + UN
WPP 2024 projections through 2100).

Confidence band: ILLUSTRATIVE only — a growing-with-horizon ±X% envelope,
not a real prediction interval. UN WPP 2024 publishes 80% and 95% PIs in
its probabilistic projections (separate Excel files); use those if a real
PI band is needed.

Run from the dalila env:
    ~/miniforge3/envs/dalila/bin/python mex_population_2050.py
"""

import io
from pathlib import Path
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

URL = "https://ourworldindata.org/grapher/population-long-run-with-projections.csv"
HERE = Path(__file__).parent
OUT_PNG = HERE / "mex_population_2050.png"


def fetch_owid():
    print(f"Fetching {URL} ...")
    with urllib.request.urlopen(URL, timeout=60) as resp:
        raw = resp.read()
    df = pd.read_csv(io.BytesIO(raw))
    print(f"  {len(df):,} rows")
    return df


def filter_mexico(df: pd.DataFrame) -> pd.DataFrame:
    mex = df[df["Code"] == "MEX"].copy()
    # OWID splits historical (Population column) and projection
    # (Population (projections) (Projected) column). Coalesce into one series.
    proj_col = next(c for c in mex.columns if "projection" in c.lower())
    hist_col = "Population"
    mex["pop"] = mex[hist_col].combine_first(mex[proj_col])
    mex["is_projected"] = mex[hist_col].isna() & mex[proj_col].notna()
    mex = mex[["Year", "pop", "is_projected"]].dropna(subset=["pop"])
    mex = mex[(mex["Year"] >= 1950) & (mex["Year"] <= 2050)].sort_values("Year")
    return mex


def illustrative_band(years: np.ndarray, mid: np.ndarray, anchor_year: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Return (lo, hi) for an illustrative uncertainty envelope that opens
    from ±0% at `anchor_year` to ±10% at 2050. Linear in horizon.

    Not a statistical PI. Stand-in until UN WPP 2024 probabilistic Excel
    is wired in.
    """
    horizon = np.clip(years - anchor_year, 0, None)
    max_horizon = max(2050 - anchor_year, 1)
    pct = 0.10 * (horizon / max_horizon)
    lo = mid * (1 - pct)
    hi = mid * (1 + pct)
    return lo, hi


def main():
    df = fetch_owid()
    mex = filter_mexico(df)

    years = mex["Year"].to_numpy()
    pop = mex["pop"].to_numpy() / 1e6  # millions
    proj_mask = mex["is_projected"].to_numpy()
    anchor_year = int(mex.loc[mex["is_projected"], "Year"].min())  # first projected year

    # Build illustrative band only over the projected portion
    lo, hi = illustrative_band(years, pop, anchor_year)

    fig, ax = plt.subplots(figsize=(10, 6))
    # Historical: solid line
    ax.plot(years[~proj_mask], pop[~proj_mask], color="#1f3a5f", linewidth=2.0, label="Historical (UN WPP)")
    # Projection: dashed line + band
    ax.plot(years[proj_mask], pop[proj_mask], color="#1f3a5f", linewidth=2.0, linestyle="--",
            label="UN WPP 2024 medium variant")
    ax.fill_between(years[proj_mask], lo[proj_mask], hi[proj_mask], color="#1f3a5f", alpha=0.15,
                    label="Illustrative ±0–10% band")

    # Annotate key years
    for y in (anchor_year, 2030, 2040, 2050):
        if y in years:
            v = pop[years == y][0]
            ax.annotate(f"{v:.1f}M", xy=(y, v), xytext=(0, 8),
                        textcoords="offset points", ha="center", fontsize=9, color="#1f3a5f")

    ax.set_title("Mexico — Total population through 2050\n(UN WPP 2024 medium variant; illustrative uncertainty band)",
                 fontsize=13, loc="left")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population (millions)")
    ax.set_xlim(1950, 2050)
    ax.set_ylim(0, max(pop) * 1.10)
    ax.grid(alpha=0.25)
    ax.legend(loc="lower right", framealpha=0.95)

    ax.text(0.01, -0.16,
            "Data: OWID, citing UN WPP 2024 (medium variant). Illustrative band ≠ statistical PI; for true 80/95% PIs use\n"
            "UN WPP 2024 probabilistic projections (separate Excel release).",
            transform=ax.transAxes, fontsize=8, color="#555")

    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    print(f"Wrote {OUT_PNG}")

    # Print a small table for the record
    table = mex[mex["Year"].isin([2024, 2025, 2030, 2035, 2040, 2045, 2050])]
    print()
    print("Mexico — selected years (millions):")
    for _, row in table.iterrows():
        tag = "proj" if row["is_projected"] else "obs"
        print(f"  {int(row['Year'])}  {row['pop']/1e6:7.2f}M  [{tag}]")


if __name__ == "__main__":
    main()

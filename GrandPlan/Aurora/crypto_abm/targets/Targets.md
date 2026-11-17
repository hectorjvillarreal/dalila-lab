# Targets — note §1 from the committed snapshot

Companion to `Targets.jl` and `fetch_snapshot.py`.

## Snapshot
`data/` holds Coinbase candles fetched on 2026-11-16, checked against `SHA256SUMS`.

| File | Rows | Coverage |
|---|---|---|
| BTC-USD daily | 2,877 | 2019-01-01..2026-11-16 |
| ETH-USD daily | 2,877 | 2019-01-01..2026-11-16 |
| BTC-USD hourly | 24,998 | 2024-01-10..2026-11-16; 10 hours missing overall, 2 non-consecutive pairs inside the post-ETF window |

`fetch_snapshot.py` documents how the data was fetched. The committed CSVs, not the script, are the source of truth.

## Functions
- `verify_snapshot()`: checks the SHA-256 sums.
- `window_stats(product, a, b; exclude)`: reproduces every §1.1 cell. A test checks the key ones.
- `sigma_bar_hourly()`: σ̄ = **0.502 % per hour**, the RMS of hourly log returns over the post-ETF window. It is a fixed constant per note §2 R2.
- `intraday_gap(k = 10)`: on the 10 largest post-ETF down days, prior-close→low averages −11.0 % and close→close −7.9 % (simple). That is a gap of **−3.09 points**, the intraday target. The open equals the prior close within 1e-6 on 5 of 10 days, and within 0.006 % on all ten; the target measures from the prior close by definition (Fina, B1a sign-off fix 7).

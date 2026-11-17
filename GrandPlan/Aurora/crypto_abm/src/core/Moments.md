# Moments — calibration statistics

Companion to `Moments.jl`. Conventions are those of design note B0 v1.2, Appendix A.

- s.d. uses ddof = 1. Skewness and excess kurtosis are standardised by that s.d.
- ACF as in Appendix A.
- Hill index on the top 5 % of |r|.
- 3σ-day share uses a 90-day trailing s.d.
- `big_day_share` counts days whose simple return is beyond 10 %.

`moment_vector` returns the note §5 vector, in the order of `MOMENT_NAMES`. **Calibration convention:** the 3σ share in `moment_vector` uses a trailing s.d. *within* the series. That gives 1.58 % for post-ETF BTC data, so data and model are measured the same way. Note §1.1 reports the full-history convention (1.92 %); both values are in note Appendix A.

"""
Targets: recompute design note B0 v1.2 §1 from the committed snapshot (targets/data/),
after checking it against SHA256SUMS. Conventions: note Appendix A.
"""
module Targets
using SHA, Dates, Statistics
using ..CryptoABM.Moments
using ..CryptoABM.CryptoAdapter: load_coinbase_csv

const DATA = joinpath(@__DIR__, "data")

function verify_snapshot()
    for ln in readlines(joinpath(DATA, "SHA256SUMS"))
        h, name = split(ln, "  ")
        got = bytes2hex(open(sha256, joinpath(DATA, name)))
        got == h || error("checksum mismatch for $name")
    end
    true
end

udate(t) = Date(unix2datetime(t))

"Daily log returns with their dates (date of the later close)."
function daily_returns(product)
    d = load_coinbase_csv(joinpath(DATA, "$(product)_daily.csv"))
    dates = udate.(d.unix)
    all(diff(d.unix) .== 86400) || error("gap in daily $product")
    r = diff(log.(d.close))
    (dates = dates[2:end], r = r, d = d, alldates = dates)
end

"Window statistics as in note §1.1 (returns formed within the window; 3σ trailing s.d. on full history)."
function window_stats(product, a::Date, b::Date; exclude::Union{Nothing,Date} = nothing)
    R = daily_returns(product)
    idx = findall(t -> a < t <= b && t != exclude, R.dates)
    x = R.r[idx]
    (n = length(x), sd = sdev(x), sd_ann = sdev(x) * sqrt(365), skew = skewness(x), exkurt = exkurt(x),
     acf_abs1 = acf(abs.(x), 1), hill = hill(x), three_sigma = three_sigma_share(R.r, idx),
     big10_log = mean(abs.(x) .> 0.10), big10_simple = big_day_share(x), moments = moment_vector(x))
end

const PRE = (Date(2019, 1, 1), Date(2023, 12, 31))
const POST = (Date(2024, 1, 11), Date(2026, 11, 16))

"σ̄: RMS of hourly BTC log returns over the post-ETF window, consecutive hours only (fixed constant)."
function sigma_bar_hourly()
    h = load_coinbase_csv(joinpath(DATA, "BTC-USD_hourly.csv"))
    t0 = datetime2unix(DateTime(POST[1])) ; t1 = datetime2unix(DateTime(POST[2] + Day(1)))
    r = Float64[]; gaps = 0
    for k in 2:length(h.unix)
        (h.unix[k-1] >= t0 && h.unix[k] < t1) || continue
        if h.unix[k] - h.unix[k-1] == 3600
            push!(r, log(h.close[k] / h.close[k-1]))
        else
            gaps += 1
        end
    end
    (σbar = sqrt(mean(abs2, r)), n = length(r), gaps = gaps)
end

"Intraday target: on the `k` largest post-ETF down days, mean (prior close→low) and (close→close), simple."
function intraday_gap(; k = 10)
    R = daily_returns("BTC-USD"); d = R.d
    idx = findall(t -> POST[1] < t <= POST[2], R.dates)
    order = sort(idx; by = i -> R.r[i])[1:k]
    low = Float64[]; cc = Float64[]; open_ok = 0
    for i in order                       # return i is close[i] / close[i-1] in the d arrays: day index i+1
        j = i + 1
        push!(low, d.low[j] / d.close[j-1] - 1); push!(cc, d.close[j] / d.close[j-1] - 1)
        isapprox(d.open[j], d.close[j-1]; rtol = 1e-6) && (open_ok += 1)
    end
    (days = R.dates[order], mean_low = mean(low), mean_close = mean(cc), gap = mean(low) - mean(cc), open_equals_prior_close = open_ok)
end
end

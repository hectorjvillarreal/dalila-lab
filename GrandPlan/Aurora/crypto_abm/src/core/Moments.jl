"""
    Moments

Statistics used as calibration targets (design note B0 v1.2, §1 and Appendix A).
Asset-agnostic: the functions take vectors of log returns.

Conventions (Appendix A): s.d. with ddof = 1; skewness and excess kurtosis standardised
by the ddof = 1 s.d.; ACF(k) = Σ(x_t − x̄)(x_{t+k} − x̄)/Σ(x_t − x̄)²; Hill index on the
k = ⌊0.05·n⌋ largest |r|; 3σ day: |r_t| > 3·s.d.(r_{t−90..t−1}) on the full history passed.
"""
module Moments

using Statistics

export sdev, skewness, exkurt, acf, hill, three_sigma_share, big_day_share, moment_vector, MOMENT_NAMES

sdev(x) = std(x; corrected = true)
function skewness(x)
    s = sdev(x); m = mean(x)
    mean(((x .- m) ./ s) .^ 3)
end
function exkurt(x)
    s = sdev(x); m = mean(x)
    mean(((x .- m) ./ s) .^ 4) - 3.0
end
function acf(x, k::Int)
    m = mean(x)
    num = 0.0; den = 0.0
    @inbounds for t in eachindex(x)
        d = x[t] - m
        den += d * d
        t + k <= lastindex(x) && (num += d * (x[t+k] - m))
    end
    num / den
end
function hill(x; q = 0.05)
    a = sort(abs.(x); rev = true)
    k = floor(Int, q * length(a))
    1.0 / mean(log.(a[1:k] ./ a[k+1]))
end
"""
    three_sigma_share(r, idx; win = 90)

Share of t in `idx` with |r[t]| > 3·s.d.(r[t−win:t−1]); `r` is the full history, so the
trailing window may reach before the first index counted (note Appendix A).
"""
function three_sigma_share(r::AbstractVector, idx; win::Int = 90)
    hits = 0; n = 0
    for t in idx
        t <= win && continue
        n += 1
        abs(r[t]) > 3.0 * std(view(r, t-win:t-1)) && (hits += 1)
    end
    hits / n
end
three_sigma_share(r::AbstractVector; win::Int = 90) = three_sigma_share(r, eachindex(r); win)
"Share of days whose simple return exceeds `thr` in absolute value."
big_day_share(r; thr = 0.10) = mean(abs.(exp.(r) .- 1.0) .> thr)

const MOMENT_NAMES = [:sd, :acf_r1, :acf_abs1, :acf_abs5, :acf_abs20, :hill, :three_sigma, :skew, :big10]
"The calibration moment vector of note §5 (without the intraday gap, computed separately)."
function moment_vector(r::AbstractVector)
    a = abs.(r)
    [sdev(r), acf(r, 1), acf(a, 1), acf(a, 5), acf(a, 20), hill(r), three_sigma_share(r), skewness(r), big_day_share(r)]
end

end # module

"""Bayesian bootstrap helpers shared by the BID2 inference scripts.

Rubin (1981); Andrews, Moon and Shapiro (2026), "In Praise of the Bayesian Bootstrap",
JEP 40(4), 137-158. One Exp(1) weight per cluster (primary sampling unit), multiplied into
the survey expansion factor; every statistic is then recomputed on the reweighted sample.
No observation is ever dropped, and the replicate distribution approximates a posterior.
"""
import numpy as np


def cluster_codes(ids):
    """Integer codes 0..G-1 for an array of cluster labels (any hashable dtype)."""
    _, codes = np.unique(np.asarray(ids), return_inverse=True)
    return codes


def replicate_weights(rng, codes, base, reps):
    """Yield `reps` weight vectors: base weight x Exp(1) draw of the unit's cluster."""
    g = codes.max() + 1
    for _ in range(reps):
        yield base * rng.exponential(size=g)[codes]


def normal_cdf(x, mu, sd):
    from math import erf, sqrt
    x = np.asarray(x, dtype=float)
    return 0.5 * (1 + np.vectorize(erf)((x - mu) / (sd * sqrt(2))))


def pp_distance(draws, mu, sd):
    """Andrews and Shapiro (2026): largest positive plus largest negative gap between the
    bootstrap CDF and the normal CDF on the p-p plot (0 = identical)."""
    xs = np.sort(draws)
    gap = np.arange(1, len(xs) + 1) / len(xs) - normal_cdf(xs, mu, sd)
    return float(max(gap.max(), 0) + max(-gap.min(), 0))


def summarize(draws, point, se_normal=None, digits=4):
    x = np.asarray(draws, dtype=float)
    x = x[~np.isnan(x)]
    half = len(x) // 2
    q = lambda a, lo, hi: [round(float(np.quantile(a, lo)), digits), round(float(np.quantile(a, hi)), digits)]
    out = {"point": round(float(point), digits), "mean": round(float(x.mean()), digits), "sd": round(float(x.std()), digits),
           "ci95": q(x, 0.025, 0.975), "ci80": q(x, 0.10, 0.90),
           "split_half": {"first": q(x[:half], 0.025, 0.975), "second": q(x[half:], 0.025, 0.975)},
           "n_draws": int(len(x))}
    if se_normal:
        out["normal"] = {"se": se_normal,
                         "ci95": [round(float(point - 1.96 * se_normal), digits), round(float(point + 1.96 * se_normal), digits)],
                         "pp_distance": round(pp_distance(x, point, se_normal), 3),
                         "sd_ratio_bb_over_normal": round(float(x.std() / se_normal), 2)}
    return out


def tail_prob(draws, value):
    """Two-sided posterior tail probability of `value` under the replicate distribution."""
    x = np.asarray(draws, dtype=float)
    p = float((x <= value).mean())
    return round(2 * min(p, 1 - p), 4)


def mahalanobis_check(draws, model):
    """Joint check of a model moment vector against the replicate cloud: squared Mahalanobis
    distance of `model` from the replicate mean, and its posterior tail probability (share of
    replicates at least as far from the mean)."""
    X = np.asarray(draws, dtype=float)
    mu, S = X.mean(0), np.cov(X, rowvar=False)
    Si = np.linalg.pinv(S)
    d_model = float((model - mu) @ Si @ (model - mu))
    d_reps = np.einsum("ij,jk,ik->i", X - mu, Si, X - mu)
    return {"d2_model": round(d_model, 3), "d2_q95_replicates": round(float(np.quantile(d_reps, 0.95)), 3),
            "tail_prob": round(float((d_reps >= d_model).mean()), 4), "k": int(X.shape[1])}

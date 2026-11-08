#!/usr/bin/env python3
"""Bayesian bootstrap credible intervals for the Phase 0 metrics, document as the cluster.

    python -I src/bootstrap_eval.py [--reps 4000] [--seed 20261108]

Reads the same inputs as evaluate.py (out/stage2, silver/, eval/episode_match.csv) and
writes eval/intervals.json, eval/intervals_<date>.md and eval/figures/bb_metrics.png.

Method (Rubin 1981; Andrews, Moon and Shapiro 2026, JEP 40(4), 137-158). Each document
receives an Exp(1) weight per replicate and every metric is a ratio of weighted document
sums, so no document is ever dropped and the replicate distribution approximates a
posterior. Documents are the unit because Phase 1 adds documents, not episodes, and
because episodes within a document share the model's reading of it. Intervals are the
2.5 and 97.5 percent quantiles. Precision, schema validity and anything constant across
documents come out degenerate on purpose: the bootstrap reports that the data cannot
move them, which is the point.
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script directory
from evaluate import DDMMYYYY, EXCLUDED, MMYYYY, MULTI, SINGLE, jaccard, load_model, load_silver, month_year  # noqa: E402
from validate import NEM, ROOT, quote_report, source_text, uncovered  # noqa: E402

FIELDS = SINGLE + MMYYYY + DDMMYYYY + MULTI


def tallies(model, silver):
    """One row per document with the numerators and denominators every metric needs."""
    rows = list(csv.DictReader(open(os.path.join(ROOT, "eval", "episode_match.csv"), encoding="utf-8")))
    pairs = [(r["doc_id"].zfill(2), int(r["silver_idx"]), int(r["model_episode"])) for r in rows if r["model_episode"]]
    docs = sorted(set(silver) | set(model))
    t = {d: {"n_silver": 0, "n_core": 0, "n_model": 0, "matched_s": 0, "matched_core": 0, "matched_m": 0,
             "fsum_all": 0.0, "fn_all": 0, "fsum_inf": 0.0, "fn_inf": 0,
             "quotes": 0, "quotes_bad": 0, "records": 0, "uncovered": 0,
             "fields": {f: [0.0, 0, 0.0, 0] for f in FIELDS}} for d in docs}
    for d in docs:
        if d in EXCLUDED:
            continue
        t[d]["n_silver"] = len(silver.get(d, []))
        t[d]["n_core"] = sum(e["core"] for e in silver.get(d, []))
        t[d]["n_model"] = len(model.get(d, []))
    for d, s, m in pairs:
        if d in EXCLUDED:
            continue
        t[d]["matched_s"] += 1
        t[d]["matched_core"] += silver[d][s - 1]["core"]
        t[d]["matched_m"] += 1
        gold = silver[d][s - 1]["record"]
        rec = next((x.get("record") for x in model[d] if x["episode"] == m), None)
        if rec is None:
            continue
        for f in FIELDS:
            if f in MULTI:
                v, inf = jaccard(gold[f], rec[f]), gold[f] != [NEM]
            elif f in DDMMYYYY:
                v, inf = float(month_year(gold[f]) == month_year(rec[f])), gold[f] != NEM
            else:
                v, inf = float(gold[f] == rec[f]), gold[f] != NEM
            cell = t[d]["fields"][f]
            cell[0] += v
            cell[1] += 1
            t[d]["fsum_all"] += v
            t[d]["fn_all"] += 1
            if inf:
                cell[2] += v
                cell[3] += 1
                t[d]["fsum_inf"] += v
                t[d]["fn_inf"] += 1
    for d, eps in model.items():  # quote and coverage checks cover every model document, as in evaluate.py
        src = source_text(d)
        for e in eps:
            if not e["valid"]:
                continue
            q, bad, _ = quote_report(e["record"], src)
            t[d]["quotes"] += q
            t[d]["quotes_bad"] += len(bad)
            t[d]["records"] += 1
            t[d]["uncovered"] += bool(uncovered(e["record"]))
    return docs, t


def ratio(w, num, den):
    """Weighted ratio per replicate; nan where the weighted denominator is zero."""
    n, d = w @ num, w @ den
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(d > 0, n / d, np.nan)


def summarize(draws, point, se_normal=None):
    x = draws[~np.isnan(draws)]
    half = len(x) // 2
    q = lambda a, lo, hi: [round(float(np.quantile(a, lo)), 3), round(float(np.quantile(a, hi)), 3)]
    out = {"point": round(float(point), 3), "mean": round(float(x.mean()), 3), "sd": round(float(x.std()), 3),
           "ci95": q(x, 0.025, 0.975), "ci80": q(x, 0.10, 0.90),
           "split_half": {"first": q(x[:half], 0.025, 0.975), "second": q(x[half:], 0.025, 0.975)},
           "degenerate": bool(x.std() < 1e-9)}
    if se_normal is not None and se_normal > 0:
        # Andrews and Shapiro (2026) distance: largest positive plus largest negative gap on the p-p plot.
        from math import erf, sqrt
        xs = np.sort(x)
        f_bb = np.arange(1, len(xs) + 1) / len(xs)
        f_n = np.array([0.5 * (1 + erf((v - point) / (se_normal * sqrt(2)))) for v in xs])
        gap = f_bb - f_n
        out["normal_approx"] = {"se": round(float(se_normal), 3),
                                "ci95": [round(float(point - 1.96 * se_normal), 3), round(float(point + 1.96 * se_normal), 3)],
                                "pp_distance": round(float(max(gap.max(), 0) + max(-gap.min(), 0)), 3)}
    return out


def docs_for_halfwidth(halfwidth_now, d_now, targets=(0.10, 0.05)):
    """Documents needed for a target 95 percent half-width, if new documents disperse like these."""
    return {str(h): int(np.ceil(d_now * (halfwidth_now / h) ** 2)) for h in targets}


def figure(results, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    surface, ink, ink2, blue = "#fcfcfb", "#0b0b0b", "#52514e", "#2a78d6"
    panels = [("recall_all", "Exhaustividad, todos los episodios"),
              ("recall_core", "Exhaustividad, episodios núcleo"),
              ("quote_share_failing", "Citas que fallan la verificación")]
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.7), facecolor=surface)
    for ax, (key, title) in zip(axes, panels):
        r = results["metrics"][key]
        x = np.array(r["_draws"])
        ax.set_facecolor(surface)
        ax.hist(x, bins=30, density=True, color=blue, alpha=0.85, edgecolor=surface, linewidth=0.6)
        if "normal_approx" in r:
            se = r["normal_approx"]["se"]
            g = np.linspace(max(0, r["point"] - 4 * se), min(1, r["point"] + 4 * se), 200)
            ax.plot(g, np.exp(-0.5 * ((g - r["point"]) / se) ** 2) / (se * np.sqrt(2 * np.pi)),
                    color=ink2, linestyle="--", linewidth=1.6)
        ax.axvline(r["point"], color=ink, linewidth=1.2)
        lo, hi = r["ci95"]
        ax.annotate("", xy=(lo, 0), xytext=(hi, 0), xycoords=("data", "axes fraction"),
                    arrowprops=dict(arrowstyle="|-|", color=ink, lw=1.2, shrinkA=0, shrinkB=0, mutation_scale=3))
        if key == "quote_share_failing":
            title += f"\n{len(results['documents_quote_check'])} documentos con registros"
        ax.set_title(title, fontsize=10, color=ink, loc="left", va="bottom")
        ax.set_xlim(0, 1)
        ax.set_yticks([])
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.spines["bottom"].set_color(ink2)
        ax.tick_params(colors=ink2, labelsize=9)
        ax.text(0.98, 0.95, f"{r['point']:.2f}  [{lo:.2f}, {hi:.2f}]", transform=ax.transAxes,
                ha="right", va="top", fontsize=9, color=ink)
    handles = [Patch(color=blue, label="Bootstrap bayesiano, documento como conglomerado"),
               Line2D([], [], color=ink2, linestyle="--", label="Aproximación normal, unidades independientes"),
               Line2D([], [], color=ink, label="Estimación puntual e intervalo de credibilidad 95 %")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=8.5, labelcolor=ink)
    reps = f"{results['replicates']:,}".replace(",", " ")
    fig.suptitle(f"MX-SSRD Fase 0: incertidumbre de las métricas, {results['documents']} documentos evaluados, "
                 f"{reps} réplicas", fontsize=11, color=ink, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0.08, 1, 0.94))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=160, facecolor=surface)
    plt.close(fig)


MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
         "noviembre", "diciembre"]


def fecha_es(d):
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def write_md(res, path):
    m = res["metrics"]
    L = [f"# MX-SSRD Fase 0: intervalos de credibilidad para las métricas", "",
         f"{fecha_es(dt.date.today())}. Addendum a `report_20261031.md`. Bootstrap bayesiano "
         f"(Rubin 1981; Andrews, Moon y Shapiro 2026) con el documento como unidad de muestreo: "
         f"{res['documents']} documentos evaluados, {res['replicates']} réplicas, semilla {res['seed']}. "
         "Cada documento recibe un peso Exp(1) por réplica; ningún documento se descarta. Intervalos: cuantiles 2.5 y 97.5 %. "
         "Figura: `eval/figures/bb_metrics.png`. Código: `src/bootstrap_eval.py`.", "",
         "## Métricas principales", "",
         "| Medida | Puntual | IC 95 % bayesiano | IC 80 % | Normal ingenua (episodios independientes) | Distancia p-p |",
         "|---|---|---|---|---|---|"]
    names = {"recall_all": "Exhaustividad, todos", "recall_core": "Exhaustividad, núcleo", "precision": "Precisión",
             "field_mean_all": "Exactitud por campo, todos", "field_mean_informative": "Exactitud por campo, con contenido",
             "quote_share_failing": "Citas que fallan la verificación", "share_uncovered": "Registros con campos sin cita ni marca"}
    for k, name in names.items():
        r = m[k]
        if r["degenerate"]:
            ci95 = ci80 = "degenerado"
        else:
            ci95, ci80 = f"[{r['ci95'][0]:.2f}, {r['ci95'][1]:.2f}]", f"[{r['ci80'][0]:.2f}, {r['ci80'][1]:.2f}]"
        na = r.get("normal_approx")
        ncol = f"[{na['ci95'][0]:.2f}, {na['ci95'][1]:.2f}]" if na else ""
        pp = f"{na['pp_distance']:.2f}" if na else ""
        L.append(f"| {name} | {r['point']:.2f} | {ci95} | {ci80} | {ncol} | {pp} |")
    L += ["", "La distancia p-p es la de Andrews y Shapiro (2026): suma de la mayor desviación positiva y la mayor negativa "
          "entre la función de distribución del bootstrap y la de la aproximación normal; 0 es coincidencia exacta.", "",
          "## Chequeo de réplicas suficientes (regla de mitades del artículo)", "",
          "| Medida | IC 95 %, primera mitad | IC 95 %, segunda mitad |", "|---|---|---|"]
    for k in ("recall_all", "recall_core", "field_mean_informative", "quote_share_failing"):
        sh = m[k]["split_half"]
        L.append(f"| {names[k]} | [{sh['first'][0]:.2f}, {sh['first'][1]:.2f}] | [{sh['second'][0]:.2f}, {sh['second'][1]:.2f}] |")
    L += ["", "## Tamaño de la Fase 1", "",
          "Documentos necesarios para que la semianchura del IC 95 % baje al valor indicado, si los documentos nuevos "
          "dispersan como estos diez. La regla es la escala 1/√D de la varianza posterior; es una aproximación y, como el "
          "prompt de Etapa 1 se ajustó dentro de muestra, es optimista.", "",
          "| Medida | Semianchura hoy | D para ±0.10 | D para ±0.05 |", "|---|---|---|---|"]
    for k in ("recall_all", "recall_core", "field_mean_informative"):
        s = res["phase1_sizing"][k]
        L.append(f"| {names[k]} | ±{s['halfwidth_now']:.2f} | {s['docs_needed']['0.1']} | {s['docs_needed']['0.05']} |")
    L += ["", "## Por campo, casos con contenido en *silver*", "",
          "| Campo | n | Puntual | IC 95 % bayesiano |", "|---|---|---|---|"]
    for f, r in sorted(res["fields_informative"].items(), key=lambda kv: kv[1]["point"] if kv[1]["point"] is not None else 9):
        if r["point"] is None:
            L.append(f"| `{f}` | 0 | | |")
        else:
            ci = "degenerado" if r["degenerate"] else f"[{r['ci95'][0]:.2f}, {r['ci95'][1]:.2f}]"
            L.append(f"| `{f}` | {r['n']} | {r['point']:.2f} | {ci} |")
    L += ["", "## Lectura", ""] + res["reading"]
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=4000)
    ap.add_argument("--seed", type=int, default=20261108)
    a = ap.parse_args()
    model, silver = load_model(), load_silver()
    docs, t = tallies(model, silver)
    ev = [d for d in docs if d not in EXCLUDED]  # metric documents
    col = lambda key, ds: np.array([t[d][key] for d in ds], dtype=float)
    rng = np.random.default_rng(a.seed)
    w_ev = rng.exponential(size=(a.reps, len(ev)))
    w_all = rng.exponential(size=(a.reps, len(docs)))
    one_ev, one_all = np.ones((1, len(ev))), np.ones((1, len(docs)))

    def metric(key_num, key_den, ds, w, one, se=None):
        num, den = col(key_num, ds), col(key_den, ds)
        draws = ratio(w, num, den)
        point = ratio(one, num, den)[0]
        r = summarize(draws, point, se)
        r["_draws"] = draws[~np.isnan(draws)].round(5).tolist()
        return r, num.sum(), den.sum()

    def binom_se(k, n):
        p = k / n
        return float(np.sqrt(p * (1 - p) / n)) if n > 0 else None

    res = {"date": dt.date.today().isoformat(), "replicates": a.reps, "seed": a.seed, "documents": len(ev),
           "documents_evaluated": ev, "documents_quote_check": [d for d in docs if t[d]["records"] > 0], "metrics": {}}
    specs = [("recall_all", "matched_s", "n_silver"), ("recall_core", "matched_core", "n_core"),
             ("precision", "matched_m", "n_model"), ("field_mean_all", "fsum_all", "fn_all"),
             ("field_mean_informative", "fsum_inf", "fn_inf")]
    for name, kn, kd in specs:
        k, n = col(kn, ev).sum(), col(kd, ev).sum()
        se = binom_se(k, n) if name in ("recall_all", "recall_core", "precision") else None
        r, _, _ = metric(kn, kd, ev, w_ev, one_ev, se)
        res["metrics"][name] = r
    k, n = col("quotes_bad", docs).sum(), col("quotes", docs).sum()
    res["metrics"]["quote_share_failing"], _, _ = metric("quotes_bad", "quotes", docs, w_all, one_all, binom_se(k, n))
    k, n = col("uncovered", docs).sum(), col("records", docs).sum()
    res["metrics"]["share_uncovered"], _, _ = metric("uncovered", "records", docs, w_all, one_all, binom_se(k, n))

    res["fields_informative"] = {}
    for f in FIELDS:
        num = np.array([t[d]["fields"][f][2] for d in ev]); den = np.array([t[d]["fields"][f][3] for d in ev])
        if den.sum() == 0:
            res["fields_informative"][f] = {"n": 0, "point": None}
            continue
        r = summarize(ratio(w_ev, num, den), num.sum() / den.sum())
        r["n"] = int(den.sum())
        res["fields_informative"][f] = r

    res["phase1_sizing"] = {}
    for kname in ("recall_all", "recall_core", "field_mean_informative"):
        lo, hi = res["metrics"][kname]["ci95"]
        hw = (hi - lo) / 2
        res["phase1_sizing"][kname] = {"halfwidth_now": round(hw, 3), "docs_needed": docs_for_halfwidth(hw, len(ev))}

    m = res["metrics"]
    ra, rc, fi, qs = m["recall_all"], m["recall_core"], m["field_mean_informative"], m["quote_share_failing"]
    res["reading"] = [
        f"- **La exhaustividad no está medida, está acotada.** Con diez documentos el IC 95 % de la exhaustividad va de "
        f"{ra['ci95'][0]:.2f} a {ra['ci95'][1]:.2f} (núcleo: {rc['ci95'][0]:.2f} a {rc['ci95'][1]:.2f}). El intervalo normal "
        f"que trata los {int(col('n_silver', ev).sum())} episodios como independientes casi coincide (distancia p-p "
        f"{ra['normal_approx']['pp_distance']:.2f}); la diferencia es la forma: la posterior es asimétrica a la derecha y su "
        "piso es más alto. Aquí el conglomerado por documento no ensancha, pero tampoco había razón para esperar que lo "
        "hiciera: la variación entre documentos (de 0 de 4 en el 09 a 1 de 1 en el 05) ya es la que domina.",
        f"- **Donde la normal sí engaña: las citas.** La proporción de citas que fallan la verificación literal es "
        f"{qs['point']:.2f} con IC bayesiano [{qs['ci95'][0]:.2f}, {qs['ci95'][1]:.2f}]; la normal sobre "
        f"{int(col('quotes', docs).sum())} citas independientes da [{qs['normal_approx']['ci95'][0]:.2f}, "
        f"{qs['normal_approx']['ci95'][1]:.2f}] y la distancia p-p es {qs['normal_approx']['pp_distance']:.2f}. Las citas "
        "fallan por documento, no por cita: las elisiones se concentran en unos pocos registros largos. Es el caso del "
        "ejemplo A del artículo, en el que el intervalo que se debe reportar es el del bootstrap.",
        f"- **Lo que sí sobrevive al intervalo.** Ni el límite superior de la exhaustividad ({ra['ci95'][1]:.2f}) ni el de la "
        f"exactitud por campo con contenido ({fi['ci95'][1]:.2f}) alcanzan un nivel útil para construir la base; la cota "
        f"inferior de citas que fallan ({qs['ci95'][0]:.2f}) sigue por encima del límite de paro de 0.10. La recomendación "
        "«ajustar» se sostiene con incertidumbre explícita; «parar» no se puede descartar ni afirmar con esta muestra.",
        "- **Precisión 1.00 es degenerada, no precisa.** Cada episodio del modelo emparejó con alguno de *silver* en todos los "
        "documentos, así que el bootstrap no puede moverla. Es el aviso del artículo: el bootstrap cuantifica el muestreo, "
        "no el diseño del emparejamiento, que ya el reporte llamó generoso.",
        "- **Los campos de juicio no tienen muestra.** Dirección del pasivo, cobertura y beneficios tienen entre 1 y 8 casos "
        "con contenido; sus intervalos cubren casi todo el rango o son degenerados. Las cifras 0.13, 0.00 y 0.25 del reporte "
        "son ilustrativas, no estimaciones.",
        f"- **Tamaño de la Fase 1.** Para que la exhaustividad tenga una semianchura de ±0.10 hacen falta del orden de "
        f"{res['phase1_sizing']['recall_all']['docs_needed']['0.1']} documentos; para ±0.05, "
        f"{res['phase1_sizing']['recall_all']['docs_needed']['0.05']}. Eso dimensiona el *silver* fuera de muestra que "
        "piden Beth y Héctor en el punto 4 de «Qué ajustar».",
    ]
    os.makedirs(os.path.join(ROOT, "eval", "figures"), exist_ok=True)
    figure(res, os.path.join(ROOT, "eval", "figures", "bb_metrics.png"))
    for r in res["metrics"].values():
        r.pop("_draws", None)
    json.dump(res, open(os.path.join(ROOT, "eval", "intervals.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    md = os.path.join(ROOT, "eval", f"intervals_{res['date'].replace('-', '')}.md")
    write_md(res, md)
    for k in ("recall_all", "recall_core", "precision", "field_mean_informative", "quote_share_failing"):
        r = res["metrics"][k]
        print(f"{k:24s} {r['point']:.3f}  ci95 {r['ci95']}  normal {r.get('normal_approx', {}).get('ci95')}  "
              f"pp {r.get('normal_approx', {}).get('pp_distance')}")
    print("sizing", res["phase1_sizing"])
    print("wrote", md)
    return 0


if __name__ == "__main__":
    sys.exit(main())

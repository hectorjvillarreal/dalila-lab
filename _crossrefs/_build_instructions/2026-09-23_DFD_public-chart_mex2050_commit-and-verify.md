---
type: build_instruction
build_type: commit_and_verify
status: executed
executed: 2026-09-23
project_scope: [DFD]
date_added: 2026-09-23
added_by: Anne
endorsed_by: Anne
executor: Claude Code (Dalila)
requested_by: Héctor
governing_instructions:
  - _crossrefs/protocols/PROTO-RAG-001.md
output_dir: GrandPlan/DFD/outputs/public/2026-09_mexico_2050/
embeds: [mex2050_projection.py]
title: "Commit, re-run and verify the public chart 'México en 2050: no serán 149 millones' — script embedded verbatim"
---

# Build instruction — public chart, México 2050: commit, re-run, verify

## What this is

A public-facing chart produced in the Demographics chat on 2026-09-23 for Héctor
(`mexico_2050_fecundidad_realista_v2.png`). It projects Mexico's population to 2050 from the
INEGI EIC 2025 count under three fertility levels (1.5, 1.23, falling to 0.9), against the UN
WPP 2024 medium variant. **It is a communication product, not a corpus artifact and not a DFD
scenario:** it does not use the v1.6 scenario table, IM-6, or the EIC-rebased skeleton. Its only
claim to standing is that it is reproducible — which is what this instruction secures. The
script and its inputs exist only in the chat sandbox until this runs.

The script is embedded below in full (Appendix). It downloads its UN inputs, validates itself
against the UN medium variant, and regenerates the chart and results from scratch.

## Step 1 — Commit the script

Write the Appendix block, fences excluded, byte for byte, to
`GrandPlan/DFD/outputs/public/2026-09_mexico_2050/mex2050_projection.py`.
Its SHA-256 must be `8e3d947b9b3c1047ead6c6f6309726fa6c5c97bce9ec968bda9e72e3eaead1f9`; if not, the copy is corrupted — stop and report. Record it in the README (Step 4). Do not edit it in this step.

## Step 2 — Run it and check against the expected values

`cd` to `output_dir`, run `python3 mex2050_projection.py`. First run downloads five UN files
(~290 MB) to `data/`. **Add `data/` to `.gitignore`**; the inputs are not committed — their
hashes are (Step 4).

**Acceptance — all must hold:**

| Check | Expected |
|---|---|
| `results/validation.txt` | UN base + UN TFR → 2050 = **148.71 M**; UN published **148.95 M**; 0–14 in 2050 = **26.14 M** |
| Script exits | 0 (it exits non-zero if validation misses by > 0.5 M) |
| `sube_1.5` pop 2025 / 2035 / 2050 | 130.9 / 135.7 / 136.9 |
| `observada_1.23` pop 2025 / 2035 / 2050; 0–14 in 2050 | 130.9 / 132.9 / 130.1; 16.7 |
| `baja_0.9` pop 2025 / 2035 / 2050 | 130.9 / 131.5 / 124.2 |
| Input SHA-256 (`results/inputs_sha256.txt`) | as listed below |
| `results/scenarios.csv` SHA-256 | `7e521a134f8ede0add7c27816a4d7181c10b9656e16f1b25b67b5ee0608626f6` |

Input hashes from the chat run (UN files downloaded 2026-09-23):
```
a04d7d1486a5eb2832cc812d599448f0a71e8ac9e1e7e6fa4066673d6a2487cd  WPP2024_PopulationByAge5GroupSex_Medium.csv.gz
c0d3b5b7e992902df3be1980cfa86c440c1cd673ecec9d4826142a03aece04ec  WPP2024_Fertility_by_Age5.csv.gz
286ac36bb1415e2e1ade03acfef0a29f0e4c087e2f78e38c48f50c5df89082bc  WPP2024_Demographic_Indicators_Medium.csv.gz
3aa9b324ba654ae61e292889be0677d30d97061a30c2c05a0ecc86cc2c5c8159  WPP2024_Life_Table_Abridged_Medium_2024-2100.csv.gz
66b84489fd7875b62de9b40d960b803b8c8439367c98deab89c2f770970925b9  WPP2024_TotalPopulationBySex.csv.gz
```

**If an input hash differs,** the UN has re-issued a file. Do not stop: re-run, compare the
acceptance values, and report every value that moved by more than 0.1 M. The PNG hash is *not*
an acceptance criterion (it depends on the matplotlib and font versions); check the PNG visually
against the chat version instead.

## Step 3 — Verify the two EIC inputs against the source

The script hard-codes three EIC figures: total **130,911,314**, share 0–14 **21.6 %**, share 65+
**10.1 %**. The total is from RR 37/26. The two shares came from the EIC-rebased graphs work, not
from a table reference — the same class of defect as the BID2 attribution. Recompute both from
the EIC 2025 open-data tabulado (total population by five-year age group) and record the table
name and access date in the README.

- If both match to one decimal: no change; note "verified".
- If either differs: update `EIC_SHARES` in the script (the only permitted edit), re-run, and
  report old vs new values for every row of the acceptance table. The chart text reads its
  numbers from the run, except the "(21.6 % … 10.1 % …)" in the method note — update that string
  too, and log both edits.

## Step 4 — README (provenance)

Write `output_dir/README.md`, in Spanish with a short English header, containing: what the
chart shows and what it is not (not a forecast, not a DFD scenario, not IM-6); the method in
five lines; the script SHA-256; the five input hashes and download date; the EIC table
reference from Step 3; the validation line; a pointer to this instruction; and the known
limitations, verbatim:

1. The EIC 65+ share exceeds CONAPO's conciliación by ~1.2 M at mid-2025; this is unresolved
   (Q4 gate). It barely moves total population to 2050 but would matter for any dependency
   chart built on this base.
2. Net migration is the UN medium's, not the EIC-observed −230 k/yr; using the EIC flow would
   lower every line.
3. The EIC 2025 reference date (15 Oct) is treated as the 2025 start without a time shift.
4. The UN line starts ~1 M above INEGI's count; the gap in 2050 is fertility *and* base.

## Step 5 — Housekeeping

- Delete `mexico_poblacion_2050_variantes_onu.png` wherever it appears (C1 error: wrong UN
  low-variant fertility) — already ordered in the commit-endorsements instruction; confirm.
- Inbox line to Anne: acceptance table results, Step 3 outcome, any value moved.

## Not to do

- Do not publish or copy the PNG outside `output_dir`. Publication is Héctor's decision.
- No edits to the script beyond `EIC_SHARES` and the one method-note string (Step 3).
- Do not feed these numbers into the corpus, the scenario table, the nota, or IM-6.

## Optional — independent check

Anne built and checked this method; the UN replication is a strong test, but it is self-review.
If Héctor wants a second reader before publication, Cath or a fresh Claude Code session
re-derives the three 2050 values from the method description in the README alone, without
reading the script. Agreement within 0.5 M closes it.

---

# Appendix — `mex2050_projection.py` (verbatim)

~~~~python
"""
mex2050_projection.py — Mexico total population 2025–2050 under alternative fertility levels.

Purpose
    Reproduce the public chart "México en 2050: no serán 149 millones" (Sept 2026).
    Cohort-component projection, 5-year age groups x 5-year steps. Only the fertility LEVEL
    differs across scenarios; mortality, net migration and the age pattern of fertility are
    UN WPP 2024 medium. Base 2025 = INEGI EIC 2025 total, with EIC broad-age shares.
Inputs  (downloaded from population.un.org on first run, cached in ./data/, SHA-256 logged)
    WPP2024_PopulationByAge5GroupSex_Medium.csv.gz, WPP2024_Fertility_by_Age5.csv.gz,
    WPP2024_Demographic_Indicators_Medium.csv.gz, WPP2024_Life_Table_Abridged_Medium_2024-2100.csv.gz,
    WPP2024_TotalPopulationBySex.csv.gz
Outputs
    results/scenarios.csv, results/validation.txt, results/inputs_sha256.txt,
    figures/mexico_2050_fecundidad_realista.png
Assumptions
    EIC 2025 total 130,911,314 at 15 Oct 2025 treated as the 2025 start (no 3.5-month shift).
    EIC shares: 0–14 = 21.6 %, 65+ = 10.1 %; UN 2025 age-sex structure rescaled within the
    three broad groups to match. SRB 1.05. Net migration: UN medium annual totals, fixed
    age-sex profile (MIGPROF). Survival from UN abridged life tables at the step midpoint.
Validation
    With UN base and UN medium TFR the method must reproduce UN medium 2050 within 0.5 M
    (observed 148.7 vs 148.9). The script fails loudly otherwise.
Dependencies
    Python >= 3.10, matplotlib. Authors: Anne (method), Claude (code), Sept 2026.
"""
import csv, gzip, hashlib, json, os, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA, RES, FIG = (os.path.join(HERE, d) for d in ("data", "results", "figures"))
BASE_URL = "https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/CSV_FILES/"
FILES = ["WPP2024_PopulationByAge5GroupSex_Medium.csv.gz", "WPP2024_Fertility_by_Age5.csv.gz",
         "WPP2024_Demographic_Indicators_Medium.csv.gz", "WPP2024_Life_Table_Abridged_Medium_2024-2100.csv.gz",
         "WPP2024_TotalPopulationBySex.csv.gz"]
EIC_TOTAL = 130_911.314          # thousands, INEGI EIC 2025, RR 37/26
EIC_SHARES = {"young": 0.216, "old": 0.101}
SRB = 1.05
MIGPROF = {0:.03,5:.03,10:.03,15:.10,20:.20,25:.20,30:.14,35:.10,40:.07,45:.04,50:.03,55:.02,60:.01}
AGES = list(range(0, 101, 5))

def fetch():
    os.makedirs(DATA, exist_ok=True); log = []
    for f in FILES:
        p = os.path.join(DATA, f)
        if not os.path.exists(p):
            print("downloading", f); urllib.request.urlretrieve(BASE_URL + f, p)
        log.append(f"{hashlib.sha256(open(p,'rb').read()).hexdigest()}  {f}")
    return log

def load_mex():
    cache = os.path.join(DATA, "mex_extract.json")
    if os.path.exists(cache): return json.load(open(cache))
    def rows(f, keep, cond=lambda r: True):
        out = []
        with gzip.open(os.path.join(DATA, f), "rt", encoding="utf-8-sig") as h:
            for r in csv.DictReader(h):
                if r.get("ISO3_code") == "MEX" and cond(r): out.append({k: r[k] for k in keep})
        return out
    D = {"pop": rows(FILES[0], ["Time","AgeGrpStart","PopMale","PopFemale"]),
         "asfr": rows(FILES[1], ["Variant","Time","AgeGrpStart","PASFR"], lambda r: r["Variant"]=="Medium"),
         "ind": rows(FILES[2], ["Time","TFR","NetMigrations"]),
         "lt": rows(FILES[3], ["Sex","Time","AgeGrpStart","Lx"]),
         "tot": rows(FILES[4], ["Variant","Time","PopTotal"], lambda r: r["Variant"]=="Medium")}
    json.dump(D, open(cache, "w")); return D

D = None
def popvec(year):
    m = {a: 0.0 for a in AGES}; f = {a: 0.0 for a in AGES}
    for r in D["pop"]:
        if int(r["Time"]) == year:
            a = min(int(r["AgeGrpStart"]), 100); m[a] += float(r["PopMale"]); f[a] += float(r["PopFemale"])
    return m, f
def surv(year, sex):
    L = {int(r["AgeGrpStart"]): float(r["Lx"]) for r in D["lt"] if int(r["Time"]) == year and r["Sex"] == sex}
    G = {0: L[0] + L[1], **{a: L[a] for a in range(5, 101, 5)}}
    T100 = sum(v for a, v in L.items() if a >= 100)
    S = {a: G[a+5] / G[a] for a in range(0, 95, 5)}
    S[95] = T100 / (G[95] + T100); S["birth"] = G[0] / (5 * 100000.0)
    return S
def pasfr(year): return {int(r["AgeGrpStart"]): float(r["PASFR"])/100 for r in D["asfr"] if int(r["Time"]) == year}
def tfr_un(year): return next(float(r["TFR"]) for r in D["ind"] if int(r["Time"]) == year)
def netmig(year): return next(float(r["NetMigrations"]) for r in D["ind"] if int(r["Time"]) == year)

def eic_base():
    m, f = popvec(2025)
    grp = lambda a: "young" if a < 15 else ("old" if a >= 65 else "work")
    tot = {"young": 0.0, "work": 0.0, "old": 0.0}
    for a in m: tot[grp(a)] += m[a] + f[a]
    tgt = {g: EIC_SHARES[g] * EIC_TOTAL for g in EIC_SHARES}; tgt["work"] = EIC_TOTAL - sum(tgt.values())
    k = {g: tgt[g] / tot[g] for g in tot}
    return {a: m[a]*k[grp(a)] for a in m}, {a: f[a]*k[grp(a)] for a in f}

def project(tfr_fn, base, end=2050):
    m, f = base; y = 2025; out = {y: (m.copy(), f.copy())}
    while y < end:
        Sm, Sf, P = surv(y+2, "Male"), surv(y+2, "Female"), pasfr(y+2)
        tfr = (tfr_fn(y) + tfr_fn(y+5)) / 2
        nm = {a+5: m[a]*Sm[a] for a in range(0, 95, 5)}; nf = {a+5: f[a]*Sf[a] for a in range(0, 95, 5)}
        nm[100] = (m[95]+m[100])*Sm[95]; nf[100] = (f[95]+f[100])*Sf[95]
        B = sum(5*(tfr*P[a]/5)*(f[a]+nf.get(a, 0))/2 for a in P)
        nm[0] = B*SRB/(1+SRB)*Sm["birth"]; nf[0] = B/(1+SRB)*Sf["birth"]
        M = sum(netmig(y+k) for k in range(1, 6))
        for a, p in MIGPROF.items(): nm[a] = nm.get(a, 0)+M*p*0.55; nf[a] = nf.get(a, 0)+M*p*0.45
        m, f = nm, nf; y += 5; out[y] = (m.copy(), f.copy())
    return out

tot  = lambda mf: (sum(mf[0].values()) + sum(mf[1].values())) / 1000
kids = lambda mf: (sum(x for a, x in mf[0].items() if a < 15) + sum(x for a, x in mf[1].items() if a < 15)) / 1000

SCEN = {"sube_1.5": lambda y: 1.5, "observada_1.23": lambda y: 1.23,
        "baja_0.9": lambda y: 1.5 if y <= 2025 else (1.0 if y == 2030 else 0.9)}

def main():
    global D
    os.makedirs(RES, exist_ok=True); os.makedirs(FIG, exist_ok=True)
    shas = fetch(); open(os.path.join(RES, "inputs_sha256.txt"), "w").write("\n".join(shas) + "\n")
    D = load_mex()
    val = project(tfr_un, popvec(2025))
    un2050 = next(float(r["PopTotal"])/1000 for r in D["tot"] if int(r["Time"]) == 2050)
    msg = f"Validation: UN base + UN medium TFR -> 2050 = {tot(val[2050]):.2f} M; UN published {un2050:.2f} M; 0-14 in 2050 = {kids(val[2050]):.2f} M"
    open(os.path.join(RES, "validation.txt"), "w").write(msg + "\n"); print(msg)
    if abs(tot(val[2050]) - un2050) > 0.5: sys.exit("VALIDATION FAILED")
    runs = {k: project(fn, eic_base()) for k, fn in SCEN.items()}
    with open(os.path.join(RES, "scenarios.csv"), "w", newline="") as h:
        w = csv.writer(h); w.writerow(["scenario", "year", "pop_millions", "pop_0_14_millions"])
        for k, r in runs.items():
            for y, mf in r.items(): w.writerow([k, y, f"{tot(mf):.3f}", f"{kids(mf):.3f}"])
        for y in (2025, 2030, 2035, 2040, 2045, 2050):
            v = next(float(x["PopTotal"])/1000 for x in D["tot"] if int(x["Time"]) == y); w.writerow(["onu_media_publicada", y, f"{v:.3f}", ""])
    for k, r in runs.items(): print(k, {y: round(tot(mf), 1) for y, mf in r.items()}, "0-14 2050:", round(kids(r[2050]), 1))
    draw(runs, kids(val[2050]))

def draw(runs, un_kids_2050):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    yrs = [2025, 2030, 2035, 2040, 2045, 2050]
    un = {int(r["Time"]): float(r["PopTotal"])/1000 for r in D["tot"] if 2020 <= int(r["Time"]) <= 2050}
    ux = sorted(un); uv = [un[y] for y in ux]
    g = lambda k: [tot(runs[k][y]) for y in yrs]
    GREY, GREEN, AMBER, RED = "#6d6d6d", "#2a9d8f", "#e08a00", "#c8102e"
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(7.2, 10.4), dpi=150); fig.patch.set_facecolor("white")
    ax = fig.add_axes([0.11, 0.43, 0.83, 0.39])
    ax.plot(ux, uv, color=GREY, lw=2.6, ls=(0, (5, 2.5)))
    ax.text(2050.5, uv[-1], f"{uv[-1]:.0f}", va="center", fontsize=14, color=GREY, fontweight="bold")
    ax.text(2034.5, 146.4, "ONU: supone 1.89 hijos por\nmujer, bajando a 1.70", fontsize=10, color=GREY, ha="center")
    for k, c, w in [("sube_1.5", GREEN, 2.8), ("observada_1.23", AMBER, 3.6), ("baja_0.9", RED, 2.8)]:
        v = g(k); ax.plot(yrs, v, color=c, lw=w, marker="o", ms=5)
        ax.text(2050.5, v[-1], f"{v[-1]:.0f}", va="center", fontsize=14, color=c, fontweight="bold")
    ax.text(2044.5, 139.2, "Si sube a 1.5", fontsize=11, color=GREEN, ha="center", fontweight="bold")
    ax.text(2045.0, 133.9, "Si se queda en 1.23,\nlo que midió el INEGI", fontsize=11, color=AMBER, ha="center", fontweight="bold")
    ax.text(2037.6, 126.2, "Si sigue bajando\nhasta 0.9", fontsize=11, color=RED, ha="center", fontweight="bold")
    ax.plot([2025], [EIC_TOTAL/1000], "o", color="white", mec="black", mew=2.2, ms=12, zorder=7)
    ax.annotate("INEGI, 2025:\n130.9 millones", (2025, EIC_TOTAL/1000), xytext=(2021.4, 122.6), fontsize=10.5,
                fontweight="bold", arrowprops=dict(arrowstyle="-", color="black", lw=1.2))
    ax.set_xlim(2020, 2053.5); ax.set_ylim(120, 152); ax.set_xticks(range(2020, 2051, 5)); ax.tick_params(labelsize=12)
    ax.set_ylabel("Millones de habitantes", fontsize=12); ax.grid(axis="y", color="#ececec"); ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.05, 0.97, "México en 2050: no serán 149 millones.", fontsize=20, fontweight="bold", va="top")
    fig.text(0.05, 0.925, "La ONU llega a esa cifra suponiendo que cada mujer tendrá entre 1.7\ny 1.9 hijos. El INEGI acaba de medir 1.23.",
             fontsize=11.5, color="#444", va="top", linespacing=1.4)
    o = runs["observada_1.23"]; peak = max(yrs, key=lambda y: tot(o[y]))
    txt = (f"Si las mujeres en México siguen teniendo en promedio 1.23 hijos, el país dejará\n"
           f"de crecer a mediados de la década de 2030, con unos {tot(o[peak]):.0f} millones de habitantes,\n"
           f"y en 2050 seremos alrededor de {tot(o[2050]):.0f} millones.\n\n"
           f"Aunque la fecundidad subiera a 1.5, no llegaríamos a 140. Y si siguiera bajando,\n"
           f"como ya ocurre en Chile (0.99) y Colombia (1.01), en 2050 seríamos {tot(runs['baja_0.9'][2050]):.0f} millones.\n\n"
           f"Donde más se nota es en los niños: la ONU espera {un_kids_2050:.0f} millones de menores de\n"
           f"15 años en 2050. Con la fecundidad de hoy serían unos {kids(o[2050]):.0f} millones.")
    fig.text(0.05, 0.365, txt, fontsize=11.3, va="top", linespacing=1.5, bbox=dict(boxstyle="round,pad=0.8", fc="#f7f3ec", ec="none"))
    src = ("Cómo se hizo: partimos de la población que contó el INEGI en octubre de 2025 (130.9 millones; 21.6 % menores de 15 años y "
           "10.1 % de 65 y más) y la proyectamos cada cinco años. La mortalidad, la migración y la distribución de los nacimientos por "
           "edad de la madre son las de la ONU; sólo cambia cuántos hijos tiene cada mujer. Con la población y la fecundidad de la ONU, "
           "este método reproduce su cifra para 2050 (148.7 frente a 148.9 millones).\n"
           "Son escenarios, no pronósticos. La cifra de 1.23 viene de una encuesta y puede quedarse algo corta; aun así, está muy lejos de "
           "lo que supone la ONU.\nFuentes: INEGI, Encuesta Intercensal 2025. ONU, World Population Prospects 2024. Registros civiles de "
           "Chile y Colombia, 2025. Elaboración propia.")
    fig.text(0.05, 0.022, src, fontsize=7.6, color="#555", va="bottom", linespacing=1.4, wrap=True)
    fig.savefig(os.path.join(FIG, "mexico_2050_fecundidad_realista.png"), dpi=150, facecolor="white")

if __name__ == "__main__": main()
~~~~

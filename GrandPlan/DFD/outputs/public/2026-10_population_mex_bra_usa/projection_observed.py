"""
projection_observed.py — Total population 2025–2050 for Mexico, Brazil and the United States
from the latest observed national data ("if current trends hold").

Method
    Cohort-component projection, 5-year age groups x 5-year steps, the engine of
    ../2026-09_mexico_2050/mex2050_projection.py generalized to three countries.
    National sources set every LEVEL: base population, fertility, mortality, net migration.
    UN WPP 2024 supplies only age PATTERNS (age structure where no national one is loaded,
    the age pattern of fertility, the age pattern of mortality and its improvement path).
Scenarios
    central  latest observed TFR held flat
    low/high TFR -0.2 / +0.2, phased in linearly 2025 -> 2035, then flat
    UN medium is carried as a reference line only.
Mortality
    UN abridged mx scaled by one factor per sex so that e0 in the anchor year equals the
    national value; the factor is then held, so the UN improvement path is kept.
Validation
    For each country, UN base + UN TFR + UN mortality + UN net migration must reproduce the
    UN 2050 total within 1 %. The script fails loudly otherwise.
Inputs
    UN files cached in ../2026-09_mexico_2050/data/ (same downloads, SHA-256 logged);
    US Census Bureau Vintage 2025 age-sex file in data/; national figures in COUNTRIES below.
Outputs
    results/projections.csv, results/validation.txt, results/assumptions.json,
    results/inputs_sha256.txt, figures/*.png
Authors: Claude (code), for Héctor, Oct 2026. Method as in the Sept 2026 public chart (Anne).
"""
import csv, gzip, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
UNDATA = os.path.join(HERE, "..", "2026-09_mexico_2050", "data")
DATA, RES, FIG = (os.path.join(HERE, d) for d in ("data", "results", "figures"))
UNFILES = {"pop": "WPP2024_PopulationByAge5GroupSex_Medium.csv.gz",
           "asfr": "WPP2024_Fertility_by_Age5.csv.gz",
           "ind": "WPP2024_Demographic_Indicators_Medium.csv.gz",
           "lt": "WPP2024_Life_Table_Abridged_Medium_2024-2100.csv.gz",
           "tot": "WPP2024_TotalPopulationBySex.csv.gz"}
US_AGESEX = os.path.join(DATA, "census_nc-est2025-agesex-res.csv")
EIC_MIG = os.path.join(HERE, "..", "..", "briefs", "2026-09_EIC2025_nota", "data",
                       "eic2025_emigrants_age_sex_grafica9.csv")
AGES = list(range(0, 101, 5))
SRB = 1.05
MIGPROF = {0:.03,5:.03,10:.03,15:.10,20:.20,25:.20,30:.14,35:.10,40:.07,45:.04,50:.03,55:.02,60:.01}
T0, T1 = 2025, 2050


def mex_mig(y):
    """INEGI EIC 2025 net emigration, thousands/yr: -230 to 2030, taper to -134 by 2040 (MEX instructions v1.7 queue)."""
    if y <= 2030: return -230.0
    if y >= 2040: return -134.0
    return -230.0 + (y - 2030) * (96.0 / 10)


COUNTRIES = {
    "MEX": dict(name="Mexico", base_total=130_911.314,
                base_note="INEGI Encuesta Intercensal 2025 count (15 Oct 2025), UN 2025 age-sex structure rescaled to EIC shares 0-14 = 21.6 %, 65+ = 10.1 %",
                base_shares={"young": 0.216, "old": 0.101},
                tfr=1.23, tfr_note="INEGI EIC 2025, TGF for 2024 (survey direct estimate; registry-based figures run higher)",
                e0=(2026, 72.75, 79.24), e0_note="CONAPO, 2026 (projection-year value)",
                mig=mex_mig, mig_note="INEGI EIC 2025 net emigration: -230k/yr to 2030, tapering to -134k/yr by 2040 (midpoint of the 107-161k CPV 2020 range); EIC age-sex profile",
                migprof="eic"),
    "BRA": dict(name="Brazil", base_total=213_400.0,
                base_note="IBGE population estimate, 1 Jul 2025 (213.4 M), UN 2025 age-sex structure rescaled proportionally",
                tfr=1.48, tfr_note="IBGE TFR 2023 (1.57) scaled by the 2024 fall in births (2,376,901 vs 2,523,267, -5.8 %, IBGE Registro Civil 2024), women 15-49 assumed flat",
                e0=(2024, 73.3, 79.9), e0_note="IBGE Tábuas Completas de Mortalidade 2024",
                mig="un", mig_note="UN WPP 2024 net migration path (exception: no national estimate published; IBGE's 2024 revision identifies net emigration as its largest correction)",
                migprof="generic"),
    "USA": dict(name="United States", base_total=None,
                base_note="US Census Bureau Vintage 2025, resident population by single year of age and sex, 1 Jul 2025 (341.8 M)",
                tfr=1.576, tfr_note="CDC/NCHS final 2025 age-specific rates (Data Brief 571), summed: 5 x 315.2 / 1000",
                e0=(2024, 76.5, 81.4), e0_note="CDC/NCHS, Mortality in the United States 2024",
                mig=lambda y: 321.0, mig_note="Census Bureau Vintage 2025: net international migration 321k in 2026 'if current trends continue', held constant",
                migprof="generic"),
}
SENS_US_MIG = 1000.0  # thousands/yr, sensitivity: roughly the pre-2022 average


# ---------------------------------------------------------------- UN data
def load_un():
    cache = os.path.join(DATA, "un_extract_mex_bra_usa.json")
    if os.path.exists(cache): return json.load(open(cache))
    keep = set(COUNTRIES)
    spec = {"pop": (["Time", "AgeGrpStart", "PopMale", "PopFemale"], None),
            "asfr": (["Time", "AgeGrpStart", "PASFR"], ("Variant", "Medium")),
            "ind": (["Time", "TFR", "NetMigrations", "LExMale", "LExFemale"], None),
            "lt": (["Sex", "Time", "AgeGrpStart", "AgeGrpSpan", "mx", "ax", "Lx"], None),
            "tot": (["Time", "PopTotal"], ("Variant", "Medium"))}
    D = {iso: {k: [] for k in spec} for iso in keep}
    for k, (cols, cond) in spec.items():
        with gzip.open(os.path.join(UNDATA, UNFILES[k]), "rt", encoding="utf-8-sig") as h:
            for r in csv.DictReader(h):
                iso = r.get("ISO3_code")
                if iso in keep and (cond is None or r[cond[0]] == cond[1]) and 2024 <= int(r["Time"]) <= 2055:
                    D[iso][k].append({c: r[c] for c in cols})
    json.dump(D, open(cache, "w")); return D


class UN:
    def __init__(self, d):
        self.d = d
        self._lt = {}
        for r in d["lt"]:
            if r["Sex"] in ("Male", "Female"):
                self._lt.setdefault((int(r["Time"]), r["Sex"]), []).append(
                    (int(r["AgeGrpStart"]), int(r["AgeGrpSpan"]), float(r["mx"]), float(r["ax"]), float(r["Lx"])))
        for v in self._lt.values(): v.sort()

    def popvec(self, year):
        m = {a: 0.0 for a in AGES}; f = {a: 0.0 for a in AGES}
        for r in self.d["pop"]:
            if int(r["Time"]) == year:
                a = min(int(r["AgeGrpStart"]), 100); m[a] += float(r["PopMale"]); f[a] += float(r["PopFemale"])
        return m, f

    def pasfr(self, year): return {int(r["AgeGrpStart"]): float(r["PASFR"]) / 100 for r in self.d["asfr"] if int(r["Time"]) == year}
    def tfr(self, year): return next(float(r["TFR"]) for r in self.d["ind"] if int(r["Time"]) == year)
    def netmig(self, year): return next(float(r["NetMigrations"]) for r in self.d["ind"] if int(r["Time"]) == year)
    def total(self, year): return next(float(r["PopTotal"]) for r in self.d["tot"] if int(r["Time"]) == year) / 1000

    def lx_table(self, year, sex, k=1.0):
        """Abridged L(x) from UN mx scaled by k; returns ({age: L}, e0)."""
        l, L = 100000.0, {}
        rows = self._lt[(year, sex)]
        for i, (a, n, mx, ax, _) in enumerate(rows):
            m = k * mx
            if i == len(rows) - 1:
                L[a] = l / m if m > 0 else 0.0; break
            q = min(1.0, n * m / (1 + (n - ax) * m)); d = l * q
            L[a] = n * (l - d) + ax * d; l -= d
        return L, sum(L.values()) / 100000.0

    def surv(self, year, sex, k=1.0):
        L, _ = self.lx_table(year, sex, k)
        G = {0: L[0] + L[1], **{a: L[a] for a in range(5, 100, 5)}}
        T100 = sum(v for a, v in L.items() if a >= 100)
        S = {a: G[a + 5] / G[a] for a in range(0, 95, 5)}
        S[95] = T100 / (G[95] + T100); S["birth"] = G[0] / (5 * 100000.0)
        return S

    def solve_k(self, year, sex, target):
        lo, hi = 0.2, 5.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if self.lx_table(year, sex, mid)[1] > target: lo = mid
            else: hi = mid
        return (lo + hi) / 2


# ---------------------------------------------------------------- bases and profiles
def us_base():
    m = {a: 0.0 for a in AGES}; f = {a: 0.0 for a in AGES}
    for r in csv.DictReader(open(US_AGESEX)):
        age = int(r["AGE"])
        if age == 999 or r["SEX"] == "0": continue
        g = min(age // 5 * 5, 100); v = int(r["POPESTIMATE2025"]) / 1000
        (m if r["SEX"] == "1" else f)[g] += v
    return m, f


def base_for(iso, un):
    c = COUNTRIES[iso]
    if iso == "USA": return us_base()
    m, f = un.popvec(2025)
    if "base_shares" in c:
        grp = lambda a: "young" if a < 15 else ("old" if a >= 65 else "work")
        tot = {"young": 0.0, "work": 0.0, "old": 0.0}
        for a in m: tot[grp(a)] += m[a] + f[a]
        tgt = {g: c["base_shares"][g] * c["base_total"] for g in c["base_shares"]}
        tgt["work"] = c["base_total"] - sum(tgt.values())
        k = {g: tgt[g] / tot[g] for g in tot}
        return {a: m[a] * k[grp(a)] for a in m}, {a: f[a] * k[grp(a)] for a in f}
    s = c["base_total"] / (sum(m.values()) + sum(f.values()))
    return {a: v * s for a, v in m.items()}, {a: v * s for a, v in f.items()}


def eic_profile():
    """Shares of net migration by 5-year group and sex from EIC 2025 Gráfica 9 (sum to 1)."""
    pm, pf = {}, {}
    for r in csv.DictReader(open(EIC_MIG)):
        a = int(r["band"].split("-")[0].rstrip("+"))
        a = min(a, 100)
        pm[a] = pm.get(a, 0) + float(r["men_pct"]); pf[a] = pf.get(a, 0) + float(r["women_pct"])
    s = sum(pm.values()) + sum(pf.values())
    return {a: v / s for a, v in pm.items()}, {a: v / s for a, v in pf.items()}


def generic_profile():
    return {a: p * 0.55 for a, p in MIGPROF.items()}, {a: p * 0.45 for a, p in MIGPROF.items()}


# ---------------------------------------------------------------- engine
def project(un, base, tfr_fn, mig_fn, prof, kM=1.0, kF=1.0):
    m, f = base; y = T0; out = {y: (dict(m), dict(f))}
    pm, pf = prof
    while y < T1:
        Sm, Sf, P = un.surv(y + 2, "Male", kM), un.surv(y + 2, "Female", kF), un.pasfr(y + 2)
        tfr = (tfr_fn(y) + tfr_fn(y + 5)) / 2
        nm = {a + 5: m[a] * Sm[a] for a in range(0, 95, 5)}; nf = {a + 5: f[a] * Sf[a] for a in range(0, 95, 5)}
        nm[100] = (m[95] + m[100]) * Sm[95]; nf[100] = (f[95] + f[100]) * Sf[95]
        B = sum(5 * (tfr * P[a] / 5) * (f[a] + nf.get(a, 0)) / 2 for a in P)
        nm[0] = B * SRB / (1 + SRB) * Sm["birth"]; nf[0] = B / (1 + SRB) * Sf["birth"]
        M = sum(mig_fn(y + k) for k in range(1, 6))
        for a, p in pm.items(): nm[a] = nm.get(a, 0) + M * p
        for a, p in pf.items(): nf[a] = nf.get(a, 0) + M * p
        m, f = nm, nf; y += 5; out[y] = (dict(m), dict(f))
    return out


tot = lambda mf: (sum(mf[0].values()) + sum(mf[1].values())) / 1000


def tfr_path(level, delta):
    return lambda y: level + delta * min(1.0, max(0.0, (y - 2025) / 10))


def main():
    os.makedirs(RES, exist_ok=True); os.makedirs(FIG, exist_ok=True)
    shas = [f"{hashlib.sha256(open(os.path.join(UNDATA, f), 'rb').read()).hexdigest()}  {f}" if os.path.exists(os.path.join(UNDATA, f))
            else f"(not present; cached extract used)  {f}" for f in UNFILES.values()]
    shas.append(f"{hashlib.sha256(open(US_AGESEX, 'rb').read()).hexdigest()}  {os.path.basename(US_AGESEX)}")
    shas.append(f"{hashlib.sha256(open(EIC_MIG, 'rb').read()).hexdigest()}  {os.path.basename(EIC_MIG)}")
    open(os.path.join(RES, "inputs_sha256.txt"), "w").write("\n".join(shas) + "\n")
    raw = load_un()
    rows, val, assume = [], [], {}
    for iso, c in COUNTRIES.items():
        un = UN(raw[iso])
        # validation: everything UN
        v = project(un, un.popvec(2025), un.tfr, un.netmig, generic_profile())
        err = tot(v[2050]) / un.total(2050) - 1
        val.append(f"{c['name']}: UN inputs -> 2050 = {tot(v[2050]):.2f} M; UN published {un.total(2050):.2f} M ({100*err:+.2f} %)")
        if abs(err) > 0.01: sys.exit("VALIDATION FAILED: " + val[-1])
        # observed inputs
        yr, eM, eF = c["e0"]
        kM, kF = un.solve_k(yr, "Male", eM), un.solve_k(yr, "Female", eF)
        base = base_for(iso, un)
        prof = eic_profile() if c["migprof"] == "eic" else generic_profile()
        mig = un.netmig if c["mig"] == "un" else c["mig"]
        runs = {s: project(un, base, tfr_path(c["tfr"], d), mig, prof, kM, kF)
                for s, d in (("central", 0.0), ("low", -0.2), ("high", 0.2))}
        if iso == "USA":
            runs["central_mig_1M"] = project(un, base, tfr_path(c["tfr"], 0.0), lambda y: SENS_US_MIG, prof, kM, kF)
        for s, r in runs.items():
            for y, mf in r.items(): rows.append([c["name"], s, y, f"{tot(mf):.3f}"])
        for y in range(T0, T1 + 1, 5): rows.append([c["name"], "un_medium", y, f"{un.total(y):.3f}"])
        assume[c["name"]] = {"base_2025_millions": round(tot(runs["central"][2025]), 3), "base": c["base_note"],
                             "tfr_central": c["tfr"], "tfr_range": [round(c["tfr"] - 0.2, 3), round(c["tfr"] + 0.2, 3)],
                             "tfr_source": c["tfr_note"],
                             "e0_anchor": {"year": yr, "male": eM, "female": eF, "source": c["e0_note"],
                                           "un_e0_same_year": [round(un.lx_table(yr, 'Male')[1], 2), round(un.lx_table(yr, 'Female')[1], 2)],
                                           "mx_scale": [round(kM, 4), round(kF, 4)]},
                             "net_migration": c["mig_note"], "un_tfr_2025": round(un.tfr(2025), 3),
                             "un_2025_millions": round(un.total(2025), 3)}
        print(val[-1]); print("  ", {s: round(tot(r[2050]), 1) for s, r in runs.items()})
    with open(os.path.join(RES, "projections.csv"), "w", newline="") as h:
        w = csv.writer(h); w.writerow(["country", "scenario", "year", "pop_millions"]); w.writerows(rows)
    open(os.path.join(RES, "validation.txt"), "w").write("\n".join(val) + "\n")
    json.dump(assume, open(os.path.join(RES, "assumptions.json"), "w"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()

---
type: corpus_entry
tier: working_note
doc_id: SFTM-MEX-inference-v1
project_scope: [Aurora, DFD, RF, IM-6, BDH, fiscal_dominance_paper]
authors: [Fernández-Villaverde, Jesús]
year: 2026
title: "Saving for the Machines"
venue: "Working paper, University of Pennsylvania; first draft dated 2026-10-20 (74 pp. incl. Online Appendix); NBER WP version expected"
doi: "none yet; PDF held locally at GrandPlan/Aurora/capital/Saving_Machines.pdf"
date_added: 2026-10-25
added_by: Claude          # drafted in the Elle / Cath / Nina / Anne lenses of the build instruction
endorsed_by: Elle         # partial, per section; see endorsement_record
endorsement_record:
  - {section: "§2 What the paper says", by: Elle, date: 2026-10-25, status: endorsed, note: "internal checks hold (ρ, γ, g → r* = 5.1%; wage-premium reciprocity; yield ordering); §8.3-derived figures ride on Cath's §3.2 check"}
  - {section: "§3.1 Participant/bystander, energy capital", by: Elle, date: 2026-10-25, status: endorsed}
  - {section: "§1 Synthesis", by: Elle, date: 2026-10-25, status: held, note: "option (b): endorse once Cath, Nina and Anne return and the comment-3 flags clear; keep '2097 likely late, size unknown' aligned with Anne's §3.4 ruling"}
  - {section: "§3.2 Fiscal structure", by: Cath, status: pending}
  - {section: "§3.3 Macro-financial transmission", by: Nina, status: pending}
  - {section: "§3.4 Demographic realism", by: Anne, status: pending}
# Elle accepted the BKY correction (2097 = BKY's 2024 vintage, not 2017) on 2026-10-25.
# Source: Elle's doc comment of 2026-10-25 (Claude Doc XxVSKpppC35Z8N8A6sFkiU).
build_instruction: "20261025_BUILD-AURORA_saving-for-the-machines_mexico_v1.1.md"
---

# Saving for the Machines — México inference note (SFTM-MEX-inference-v1)

**Reading key.** Every claim carries a tag:
- **[M]** — the paper's model or text, with section, proposition, table or equation.
- **[C]** — another entry already in the Dalila corpus.
- **[I]** — our inference for México. The paper does not study México.

**Closure.** The paper's economy is **closed** (§2), so its interest rate is set at home. Any
statement about a world rate is [I] under a small-open-economy closure that we add.

**Conditional on σ (read first; added after Elle's review, 2026-10-25).** The severe reading rests
on strong task complementarity, and σ here is a U.S. calibration.
- The 11.7%-vs-2.2% gap opens only below σ ≈ 0.31. At σ = 1, a fixed 23% saving rate still gives
  6.5% growth in 2045 (Table 4A, Cor. 2).
- Every downstream use of σ = 0.2 in this note is conditional on México's σ being low. That covers
  the depreciation figures in the energy channel (§1) and the wage-below-trend-by-2032 timing
  (§3.2, item 4).
- México's σ is unestimated. It is gating open question 0 (§4).

## One-line summary

Fernández-Villaverde shows that in a standard task model the **size** of an automation growth boom
is set by how elastically capital is supplied, while the task structure sets its **duration** and
the path of wages. México does not choose its capital supply the way the paper's household does.
Its margins are which machines it hosts, who owns them, and what a higher world rate does to its
sovereign. On each of those, the inference runs against México unless it hosts the machine capital
and the generation that powers it.

---

## 1. Elle — synthesis (top)

**What the paper establishes [M].** A technology path can deliver double-digit growth or almost
none. In the σ = 0.2 economy, the difference is whether saving is free to respond (Table 4A: 11.7%
vs 2.2% growth in 2045). The saving rate rises because automation moves income to capital, not
because households become more patient (Prop. 10–11).

**What it does not establish [M].** The model has no rest of the world, no government, no debt
and no life cycle. Its household is infinitely lived, and in the long run its capital supply is
perfectly elastic. The author calls this one of "two polar cases" (Introduction) and says
heterogeneity, financial frictions and "limited physical resources" would cap that elasticity
(Conclusion).

**The México reading [I], in four steps.**

1. **The paper's lever is not México's lever.** The paper's optimistic margin is a domestic
   household that saves up to 57% of output because it owns the machines and earns their returns.
   México's capital supply is mostly the world's, priced at a world rate plus a sovereign spread.
   So the useful question for México is not whether it saves enough. It is which machines get
   located in México, under whose ownership, and at what cost of funds.
2. **Three channels, one direction.**
   - **Rate (Nina).** If frontier economies save for the machines, world long real rates rise.
     México's financing cost rises before any domestic benefit arrives.
   - **Tax base (Cath).** The tax base shifts toward capital income México cannot reach at
     source. The paper's comfortable compensation arithmetic depends on a domestic output boom
     that a bystander does not get.
   - **Demography (Anne).** México's working-age population starts falling in 2036, and old age
     is financed by transfers rather than assets. So domestic capital supply weakens just as the
     paper says capital supply is what matters.
3. **Two countervailing forces, both already in the corpus.**
   - **Aging lowers world rates [C].** Aging raises asset demand and lowers r* (Auclert et al.
     2025). Whether the world rate rises depends on which wins: machine asset supply or aging
     asset demand.
   - **Labour scarcity speeds adoption [C].** Benzell–Kotlikoff–Ye (2026) find México never
     automates under BAU, because its labour is too cheap. It adopts only under 2024 demographics
     combined with accelerating AI, and then in 2097. Aging makes labour scarcer and pulls that
     date forward. That is the optimistic read: automation filling in for the missing cohort.
   - **Seam: the 2097 date uses stale demographics (Elle's review, 2026-10-25).**
     - **[C]** BKY's 2097 rests on WPP 2024, with México's TFR near 1.7 in 2050. Current data are
       lower: EIC 2025 TFR 1.23, and the 15–64 population falling from 2036 (§3.4).
     - **[C]** BKY's own vintage switch already points the same way. Lower fertility moved México
       from never adopting (2017 vintage) to adopting in 2097 (2024 vintage).
     - **[I]** By BKY's mechanism, earlier labour scarcity pulls adoption forward. So 2097 is
       likely late on current demographics, by an amount we cannot size without re-running the
       model (open question 8).
4. **The bottom line [I].** The paper's ideas carry over to México; its optimism does not. For a
   bystander, what plays the part of the paper's saving response is **hosting**. That means
   machine capital and power generation physically in México, taxed at source on
   location-specific rents. Hosting is the only route by which part of the capital share lands
   in México's tax base.

**Energy-capital channel [M→I].**
- **[M] Anchors in the paper:**
  - Power plants are on the list of capital the build-out needs (Introduction).
  - Data-centre capital depreciates at about 12% a year, blending six-year computing equipment
    with twenty-year buildings and power plants.
  - At δ = 20% and σ = 0.2, growth falls from 11.6% to 4.6%. The household saves 79% of output,
    because replacing machines alone takes 64% of it. A fixed 23% saving rate does not even cover
    depreciation, and output in 2045 is half its trend (Online Appendix A, Table A.1). With σ = 1
    the same depreciation leaves 14.9% growth, so the severe version is conditional on low σ (open
    question 0).
- **[I] For a bystander,** generation is the part of machine capital that cannot be imported as a
  service. A data centre hosted in México needs power generated in México. So the energy
  build-out is where México is a participant, if it is one at all.
- **[I] In the Energy chat's terms,** AI capital demand pulls toward abundance. In México the
  pull lands on a power sector in which the state is a large investor. Generation built for
  hosted machines either competes for fiscal space as public investment or brings in private
  capital at the world rate.

**Participant ↔ bystander [I].** Three positions, not two:

| Position | What México gets | What it pays | Fit for México today |
|---|---|---|---|
| **Host-participant.** Foreign-owned machines and generation located in México | Construction, land and energy rents. Source-taxable location rents. Some employment | Capital income accrues abroad, so GDP rises more than GNI. Public generation investment | Partial and plausible. Data-centre nearshoring is real but not quantified in the corpus (Aurora-Energy hook) |
| **Importer of automation services.** Tasks done by machines owned and located abroad | Cheaper services | Wage pressure up to México's premium over machine-cost parity (§3.2), with no domestic capital income | Likely for services that can be traded |
| **Non-adopter** (Benzell–Kotlikoff–Ye) | Wages not displaced early | Mobile capital competed away. Falling share of world GNI (2.1% → 1.3% by 2100 under 2017-vintage demographics [C]) | The baseline in the only corpus model with a Mexico region |

**Honest answer to v1.1 §4 (Elle) [I].** México is mainly a price-taker on world capital. It
hosts part of the frontier capital, mostly generation and sites, not the ownership of the
machines. That leaves almost none of the paper's optimistic margin available to México. The
margin México does have is the location-rent and energy margin.

---

## 2. What the paper says — model-internal record

### 2.1 Mechanism and levers [M]

**Production (§2–3).**
- Output is a CES aggregate over a continuum of tasks with elasticity σ (eq. 1).
- Within each task, machines and labour are perfect substitutes: Y_i = ψ_ki·K_i + ψ_ℓi·L_i (eq. 2).
- Automation means the set of automatable tasks A(t) expands. It never shrinks.

**Common comparative advantage (Assumption 1).** ψ_ki = φ·ψ_ℓi, which gives two regimes
(Prop. 2):
- **Cost parity**, K ≤ K̄. Y = ψ_k·K + ψ_ℓ·L. Factor prices are pinned by technology: R = ψ_k and
  w = ψ_ℓ, for any σ.
- **Capital cheaper**, K > K̄. Diminishing returns apply: R < ψ_k and w > ψ_ℓ.

**Levers.**

| Margin | Parameter | Role | Calibration (Table 1–2) |
|---|---|---|---|
| Task structure | α(t) via a(t) = ā[3ζ² − 2ζ³] over T years | Path of automatable tasks | ā = 1 (full) or 0.85 (partial); T = 20 (2025–2045) |
| Task structure | σ | Complementarity across tasks. Sets the 2025 automated share and the ceiling ψ_k0 | 1, 0.5, 0.2. α0 = 0.33 / 0.61 / 0.76 |
| Task structure | q | Machine cost relative to labour in tasks already automated. Pins ψ_k0 | 0.10 (from Imas–Moll), tested at 0.05 and 0.20 |
| Task structure | ψ̂_k, ς | Machine improvement, and dispersion of comparative advantage | 0 or 0.0162; ς = 0, 0.25, 0.5 |
| Capital supply | γ (inverse IES), ρ | Saving response | γ = 2, ρ = 0.019 (from r* = 5.1%) |
| Capital supply | fixed s | Solow counterfactual | 23% (the 2025 BGP rate, not targeted) |
| Both | δ | Depreciation | 0.06 baseline; 0.12 and 0.20 in robustness |

**Capital-share dynamics [M].**
- **Saving-rate identity (Prop. 10, eq. 57):** s = s_K · (g_K + δ)/R. The second factor is the
  plow-back ratio.
- **Optimal saving.** The plow-back ratio stays near 1/γ. In the simulations it moves only from
  0.69 to about 0.55 while R climbs from 11% to 52%. The saving rate therefore follows the capital
  share, which rises from 1/3 toward 1 under full automation.
- **Fixed saving.** The plow-back ratio has to fall in proportion as the capital share rises.
- **Comparative statics (Prop. 11(ii)).** Across BGPs that differ in α, the saving rate moves one
  for one with the capital share.

**Duration vs size [M].**
- **Full automation.** The economy becomes AK. Technology sets r = ψ_k − δ, and preferences set
  growth (Prop. 8, 13).
- **Partial automation with σ = 0.2.** The boom ends. Growth is back to 2.2% by 2065. The capital
  share goes 1/3 → 0.96 → 0.42, and the wage rises to 8.9 times trend in the long run (Ricardian
  scarcity rents on the tasks only labour can do, §6.2).

**Closure [M].**
- Closed economy (§2). The real bond is in zero net supply.
- r = ρ + γ·g_C (Euler) = R − δ (no-arbitrage) (Prop. 13).
- At cost parity, causality runs from R to r to g_C. That is why "a return of 45% can last".
- There is no government sector anywhere except the tax-and-transfer exercise of §8.3.

### 2.2 Verification of the build instruction's §1 claims [M]

| Claim | Verdict | Exact form in the paper |
|---|---|---|
| ~11.7% with optimal saving | **Confirmed, with conditions** | GDP growth **in 2045**, σ = 0.2, full automation, constant machines, γ = 2 (Table 4A). Limit 11.6% (Table 3). With σ = 1 the corresponding figure is 21.9% |
| ~2.2% with saving fixed at the U.S. level | **Confirmed, with conditions** | Same economy with s fixed at the 2025 pre-announcement rate of **23%** ("Solow 2045", Table 4A). Drifts to 1.6%. The fixed rate clears the growth-boom threshold only for σ above about 0.31 (Cor. 2) |
| Saving rises with the capital share, not thrift | **Confirmed** | Prop. 10–11. §7: "the large movements in the saving rate follow the capital share, not the household's thriftiness" |
| Policy edge: power plants | **Confirmed** | Introduction, list of capital. Online Appendix A, depreciation blend |
| Policy edge: inducing saving strains public finances / "bystander economies" | **Not in the draft** | No section on public finance, open economies or government debt. Carried as Aurora's framing (build instruction v1.1, point 2) |

**What the inference inherits.** The 11.7% vs 2.2% contrast holds **only under strong task
complementarity (σ = 0.2)**. With σ = 1, a fixed 23% saving rate still gives 6.5% growth in 2045.
It is a statement about the **U.S. calibration**: q, ψ̂_ℓ = 1.62%, K/Y = 3, r* = 5.1%. None of
those has been calibrated for México.

### 2.3 Further model-internal results used below [M]

- **Distribution (§8.2, Table 6).** Hand-to-mouth households (share θ) lose the equivalent of
  40–41% of consumption with σ = 1 and 65–66% with σ = 0.2. They lose as much when the saving
  rate is fixed. Owners gain more than the representative household.
- **Compensation and tax (§8.3).** See §3.2 below.
- **Yields (§9.2).** The short rate does not move on impact. The ten-year real yield goes from
  5.1% to 13.6% (σ = 1) or 9.3% (σ = 0.2). The thirty-year yield goes to 33.0% or 19.6%. With
  θ = 0.5, the ten-year yield goes to 14.8% or 13.3%. The faster the automation, the bigger the
  jump: with σ = 1, the ten-year yield is 28% if automation takes ten years, 8% if forty, and 14%
  at the baseline of twenty (§10, Table A.1).
- **Human wealth (Prop. 15).** About two-thirds of the value of the labour force is lost on
  impact. "The start of the automation path does to the labor force what a rate hike does to a
  long bond, except that this hike is permanent."
- **Wages (§6.2–6.3).** Under common comparative advantage and full automation, the wage falls
  to its cost-parity level: 28–46% of trend. The ratio of the 2025 wage to its cost-parity level,
  w0/ψ_ℓ0, is 2.15–3.57 (Table 2), and it sets how far the wage falls. With dispersion of
  comparative advantage, the wage recovers.
- **Observable implications (§11):**
  - The saving rate should track the capital share.
  - Long real yields should jump on impact while short rates stay put.
  - Current long rates show no such pricing (Chow et al. 2025).

---

## 3. México lenses

### 3.1 Elle — participant / bystander, energy capital *(domain authority: Elle)*

Held in §1. One more point for the Energy chat **[I]**:
- The paper's depreciation results are an energy-capital result in disguise. The faster the
  machine stock wears out, the more the boom depends on financing, and the more a fixed saving
  rate fails (output at half its trend in 2045 at δ = 20%).
- For a host country, the long-lived part of the stack is power plants (twenty years in the
  paper's blend). It is the part most likely to be on the public balance sheet. The short-lived
  part, computing at six years, is the part most likely to be foreign-owned.
- So a host's fiscal exposure is to the long-lived, low-return slice of the machine stock.

### 3.2 Cath — fiscal structure and the tax base *(domain authority: Cath)*

**Model-internal baseline [M]** (§8.3, full automation, constant machines):
- **Compensation transfer.** The transfer that keeps labour income on its no-automation trend
  peaks at **4% / 11% / 20% of GDP** (σ = 1 / 0.5 / 0.2). It is below 4% of GDP by 2055 in all
  twelve economies. It is small "because output grows much faster than wages fall".
- **Flat 25% tax on net capital income.**
  - It raises τ(1 − δ/ψ_k0), which is **20–22% of GDP** in the limit economy.
  - Limit growth falls 21.9 → 16.2% (σ = 1) and 11.6 → 8.5% (σ = 0.2), permanently.
  - The paper calls it "a blunt instrument".
- **Balanced-budget tax** compensating the hand-to-mouth households:
  - With θ = 0.5, it peaks at **3.5% / 22% of net capital income** (σ = 1 / 0.2), then fades.
    The transfer itself peaks at 2.9% of GDP in 2042 (σ = 1) or 16% in 2035 (σ = 0.2).
  - The largest growth cost is **1.1 / 3.3 points**, falling to zero in the long run.
  - With θ = 0.3, the peak tax is 1.7% / 11%.
- **Incidence.**
  - Under full automation, the wage is pinned at the cost of the machines that replace labour.
    The tax "cannot be shifted to labor" and lowers growth.
  - Under partial automation, the after-tax return returns to ρ + γg*. Then "labor ends up
    paying for its own compensation".
- **Scope.** With a representative household, the compensation calculation is "an illustrative
  accounting exercise". Capital is immobile because the economy is closed.

**México inference [I].** The closure here is a small open economy with a world-determined
required return plus a sovereign spread.

1. **The compensation arithmetic does not carry over.**
   - **[M]** The transfer fades in the paper because the denominator, domestic output, explodes.
   - **[I]** For a bystander, the boom's output accrues mostly where the machines are owned and
     located. Any compensation need in México has no exploding denominator under it, so as a
     share of GDP it does not fade the way the paper's does.
   - **[I]** How large that need is depends on México's wage premium over machine-cost parity
     (the paper's w0/ψ_ℓ0, 2.15–3.57 for the U.S.). Benzell–Kotlikoff–Ye's finding that México's
     labour is too cheap to automate [C] suggests the premium is lower in México. That makes the
     wage hit smaller, but the lack of fade is the structural point.
2. **The base shifts to where México can least reach it.**
   - **[M]** In the paper's limit economy, capital income is almost all of output, which is why
     a 25% tax raises 20–22% of GDP.
   - **[I]** For México, capital income on machines owned and located abroad is outside the
     source base altogether. Residence-based taxation reaches only what Mexican residents own,
     and the corpus already records México's shallow capital markets and concentrated holdings
     (Auclert et al. note, gap 2 [C]).
   - **[I]** The bases México does reach are labour income and consumption. These are exactly
     the ones the paper says are compressed: the wage share falls toward zero under full
     automation, and the hand-to-mouth households, who consume their labour income, lose 40–66%
     of consumption.
3. **The incidence result flips under mobility.**
   - **[M]** In the closed economy, a capital-income tax under full automation falls on capital
     and growth.
   - **[I]** In a small open economy with a world-determined after-tax return, a source tax on
     mobile capital is shifted to immobile factors: labour and land. This is the standard result
     (Gordon 1986, *AER* 76(5)).
   - **[I]** So for México, the paper's partial-automation case, where "labor pays for its own
     compensation", is the relevant one even under full automation. The exception is
     **location-specific rents** that cannot leave without leaving the rent behind: grid-adjacent
     sites, generation, spectrum, land. These are where a source capital-tax base exists.
4. **RF: harder and more necessary.**
   - **[C]** México's tax pressure is 17% of GDP (2025 base). The RF target is 25% by 2036,
     **+8 points in eleven years** (`GrandPlan/RF/_index.md`).
   - **[I]** The target is harder because the bases it would rely on (labour income,
     consumption) are the ones the mechanism erodes, and the growing base is mobile.
   - **[I]** It is more necessary because both the compensation need and the debt-service
     burden (below) grow.
   - **[I]** Timing: the paper's automation wave runs 2025–2045, and with σ = 0.2 the wage falls
     below trend by 2032 [M]. That timing holds only with σ = 0.2 (open question 0). If anything like that timing applied, the RF horizon would sit in
     the early, most painful part of the transition. That is a big if. The U.S. calibration is
     not a México forecast.
5. **Government budget constraint.** This is qualitative, and it is the IM-6 calibration hook.
   - With debt ratio d and primary balance pb, the stabilising primary balance is
     pb* = d·(r − g)/(1 + g).
   - **[M]** Inside the paper's own economy under full automation, r − g_C = (1 − 1/γ)·r + ρ/γ
     (Prop. 15, eq. 70). At γ = 2, every point on r adds half a point to r − g. Even a
     *participant* government with debt would face sharply worse debt dynamics, offset by a tax
     base that is exploding.
   - **[I]** A bystander faces the r without the g. Higher world r raises r − g one for one,
     with no exploding base to set against it.
   - **[C]** The Mexican public sector's interest cost (costo financiero) is **3.4% of GDP in 2024**
     (SHCP, Q4 2024 public-finance report, via the CAF_DEM correction) and **4.0% in PPEF 2027**
     (CIEP with SHCP data, SobreMéxico 2026-10-22 deck). So the starting point is already high.
   - **[I]** Each 1-point rise in r − g raises pb* by about d points of GDP. The pass-through
     speed depends on maturity and on the fixed vs indexed mix (Nina, §3.3).
   - **Hook → IM-6:** a world-rate shifter and a capital-share shifter, with the fiscal response
     read off the OLG government budget (§4).
6. **Optimal-tax tension, stated not resolved [I].** Two results pull against each other:
   - The paper's best instrument is a temporary, balanced-budget tax on capital income. It costs
     little growth and fades.
   - For a bystander, the capital income worth taxing is mostly not at home, and taxing at
     source what is at home is shifted to labour or drives hosting away.

   The tension is between taxing where the rents are (location: energy, sites) and keeping the
   hosting that creates them. Related corpus work: the RF minimum-tax comparative report
   (`GrandPlan/RF/impuesto_minimo/20260719_RF_turnover-minimum-tax_intl-comparative_REPORT_v1.md`).
   This note does not evaluate it.

### 3.3 Nina — macro-financial transmission *(domain authority: Nina)*

**Closure first.** Everything below except the [M] items assumes México is a small open economy
facing a world real rate r^w plus a sovereign spread. The paper does not model this.

**Model-internal baseline [M]** (§9.2, Prop. 14–15):
- **Repricing at the long end.** Long yields price the growth boom on impact while the short rate
  cannot move. 10y: 5.1% → 13.6% (σ = 1) or 9.3% (σ = 0.2). 30y: 33.0% or 19.6%.
- **Discrete repricing.** The jump happens when the automation path "becomes known", that is,
  when beliefs update. It is not a gradual drift.
- **Current long rates are far below** anything the model predicts. The paper reads this as
  markets assigning little probability to these paths (Chow et al. 2025).
- **Stock market.** Market value equals the capital stock and does not jump. The P/E falls from
  20 to 2–4 by 2045 (Prop. 16).

**The bystander chain [I].**
1. Frontier economies save for the machines. World long real rates reprice upward. In
   Auclert et al.'s language this is a private asset-supply shock: **reverse crowding-out**, in
   which rising private asset supply raises r and crowds out fiscal space [C].
2. México's sovereign real financing cost rises, **long end first**, mirroring the paper's
   yield-curve result. A sovereign that funds long pays more on new issuance immediately, even
   if Banxico's policy rate does not move.
3. Debt service rises from an already high base (3.4% of GDP in 2024, 4.0% in PPEF 2027 [C]).
   It rises as fast as debt rolls over: slowly for long fixed-rate debt, faster for short or
   indexed debt.
4. Fiscal space shrinks. **Fiscal-dominance signals** to watch for a middle-income economy:
   - interest cost rising as a share of revenue (a low revenue base of 17% of GDP amplifies it);
   - issuance shortening in maturity, or shifting toward floating or inflation-indexed debt;
   - widening spreads over U.S. real yields;
   - FX depreciation feeding inflation;
   - pressure on Banxico to lean against the long end.

**What pushes back [C]:**
- Aging raises asset demand and lowers r* (Auclert et al. 2025). Whether the world rate rises is
  the outcome of a race: the machines' asset supply against aging's asset demand.
- The paper's own observation that long rates are not pricing the boom means the chain is
  **conditional on beliefs updating**.

**Brunnermeier–Reis lens: drift or run? [M→I]**
- **[M]** In the paper, the long-end jump is a jump: a discrete repricing on news.
- **[I]** For a capital importer whose local-currency bonds are partly held by foreign investors,
  a sudden repricing of world long real yields toward machines earning 25–46% [M] is a textbook
  trigger for capital-flow reversal.
- **[I]** That holds even when the sovereign borrows in its own currency. Foreign holders' FX
  losses reproduce original-sin dynamics in local-currency debt, the "original sin redux"
  argument (Carstens & Shin 2019).
- **[I]** Hard-currency exposure sits mainly with state energy-sector issuers. This is general
  knowledge, not sourced in the corpus; verify before use.
- **[I] Reading:** the regime is **run-prone at the moment beliefs update and drift-like after**.
  The danger lies in the speed of the update, not in the eventual level. The paper's speed
  results sharpen this: the faster the automation, the bigger the jump on impact (10y yield 28%
  if automation takes ten years [M]).

**Funded pensions vs sovereign sustainability (flag only; do not resolve) → IM-6 / BDH.**
- **[I] For funded individual accounts (AFORE):**
  - Higher real returns help account balances over time.
  - AFORE portfolios hold a lot of domestic sovereign paper, so the jump on impact is a
    mark-to-market loss.
  - **[M]** Under full automation the contribution base (wages) shrinks toward the cost of the
    machines.
- **[I] For the sovereign:** worse r − g. The transition-generation PAYG liabilities are
  unaffected by returns and fall on the budget.
- The net sign depends on cohort, portfolio duration and how far automation goes. **Hook →
  IM-6 / BDH (Nina / Beth).**

### 3.4 Anne — demographic realism *(consult; domain authority: Anne)*

**Model-internal baseline [M].**
- The household is infinitely lived. Labour supply is fixed and grows only in efficiency units,
  at 1.62%. There is no life cycle, no aging and no dissaving cohort.
- The paper's literature review places its result as **the opposite benchmark to OLG**. In OLG
  models "saving comes out of wages, so automation that depresses wages chokes off investment".
  It cites Sachs & Kotlikoff 2012 and Benzell et al. 2015 (immiseration), and Gasteiger &
  Prettner 2022 (AK may fail to deliver growth).
- In the paper's own hand-to-mouth extension, the transition slows. With σ = 0.2 and θ = 0.5,
  the aggregate saving rate on impact falls from 30% to 21% (§8.2).
- The paper's result is therefore an **upper bound** on the saving response. DFD's framework (an
  OLG model) sits at the other end by construction.

**México trajectory [C].** Source: the endorsed Nota EIC 2025 v1.0, Anne + Cath (23b74a0), Central
scenario, built on national data:
- TFR 1.23 (EIC 2025).
- The total dependency ratio reaches its minimum of 45.0 in 2030. It stays within one point of
  that minimum over 2027–2035.
- The 15–64 population grows 0.37% a year over 2025–2035 and **first falls in 2036 in every
  scenario**. It falls 0.48% a year over 2035–2050.
- The old-age ratio rises from 14.6 to 33.1 by 2050.
- The PAYG-equivalent contribution rate needed to hold the replacement rate rises from **11.6% to
  26.2% of the wage bill** (2025 → 2050).

**The bind [I].**
1. **Saving capacity peaks now and then declines.** The demographic window is open until about
   2035. That is when the share of prime-age savers is highest. After 2036 the labour force
   shrinks and the old-age ratio more than doubles.
   - **[I]** On life-cycle grounds, the domestic saving margin is strongest in exactly the
     decade the paper's automation wave begins (2025–2045 [M]).
   - **[I]** It weakens across the decade in which the paper's boom would need financing most.
2. **México finances old age through transfers, not assets.**
   - **[I]** In NTA terms, a second demographic dividend requires old-age consumption to be
     funded by accumulated assets. Those assets supply capital.
   - **[C]** México's old age is substantially financed by transfers: transition-generation PAYG
     liabilities, and a non-contributory pension with constitutional rank, which is "fiscally
     uncapped and demographically fully exposed" (Auclert et al. note, gap 1).
   - **[I]** Aging therefore raises **transfer demand on the budget** rather than **asset demand
     that funds capital**. This is the opposite of the channel that buys fiscal space in the U.S.
     case.
   - Only the framing is kept here. The full NTA treatment is not opened.
3. **Highest need, lowest capacity.**
   - The shrinking workforce is what makes machines valuable: in the paper's partial-automation
     case, tasks only labour can do earn scarcity rents [M].
   - Aging also raises México's wage relative to machine cost. That is the force that turns
     México into an adopter in Benzell–Kotlikoff–Ye [C].
   - The domestic capacity to save for those machines falls on the same timetable. The capital
     has to come from abroad at the world rate, which is Nina's chain.
   - **The optimistic read:** automation fills in for the missing cohort.
   - **The constraint:** financeability. If world long rates reprice (§3.3), the optimistic path
     can be shut off by the cost of funds, not by technology. This is the paper's own lesson that
     the bottleneck is capital, not technology, moved to a country that does not control its
     capital supply.

**For Anne's review.**
- **The hand-to-mouth share.** The paper's θ for the U.S. is 0.3. México's equivalent, given
  informality and low financial inclusion, is unmeasured here. It matters twice: it lowers
  aggregate saving on impact [M], and it sets who bears the consumption loss.
- **Measuring it** needs ENIGH plus NTA and belongs to the DFD/BDH hook, not to this note.

---

## 4. Open methodological questions and hooks

**Open questions surfaced.** Any of these could be promoted to a watch item. Two of them gate the
next iteration. Question 0 gates every severe figure, and question 1 gates the IM-6 hook.

0. **σ for México (gate; added after Elle's review).** How complementary are México's tasks? The
   severe reading needs σ below about 0.31. At σ = 1, a fixed saving rate still gives 6.5% growth.
   Every σ = 0.2 figure in this note waits on it. *(Elle / Cath)*
1. **Which closure for México? (gate)** The paper is closed-economy. Before IM-6 can carry a world-rate
   shifter, someone has to establish IM-6's own interest-rate closure: small open economy with
   exogenous r, closed, or hybrid. The DFD RAG summary of IM-6 does not state it. *(Cath)*
2. **México's wage premium over machine-cost parity**, the analogue of w0/ψ_ℓ0. It sets how far
   wages can fall under automation and how large any compensation need is.
   Benzell–Kotlikoff–Ye's non-adoption result suggests it is low. That would be a smaller hit and
   a later adoption. *(Cath / Anne)*
3. **The race for the world rate.** Machine asset supply against aging asset demand
   (Auclert et al.). Which wins, and on what timetable, sets the sign of Nina's chain. *(Nina)*
4. **Evidence on hosting.** Data-centre and generation investment located in México: size,
   ownership, power-purchase arrangements, public vs private generation share. None of this is in
   the corpus. *(Elle, Aurora-Energy)*
5. **Source of the "bystander economies" framing.** Cite it if it exists (slides, talk). Otherwise
   it stays Aurora's framing. *(Elle)*
6. **Hand-to-mouth share θ for México** (ENIGH), for the distributional transfer. *(Anne / Beth)*
7. **Monitoring.** The paper's observable implications are a long-end jump with the short rate
   unchanged, and investment tracking the capital share. Both could be added to Aurora's existing
   watch infrastructure (U.S. real long yields and Udibono long yields side by side). *(Nina)*
8. **México's automation-adoption date on current demographics (added after Elle's review).**
   BKY date it at 2097 on WPP 2024. On EIC 2025 (TFR 1.23, 15–64 falling from 2036) the date is
   likely earlier. Re-derive it, or keep the seam flagged. *(Anne / Nina)*

**Hooks (from the build instruction §5, kept; not in scope now):**
- **IM-6:** a world-rate shifter and a capital-share shifter, reading the OLG fiscal response.
  Prerequisite: open question 1. *(Cath)*
- **RF:** the 25%-by-2036 path under a capital-share-erosion scenario. The bases are labour
  income and consumption; the source capital base is limited to location rents (§3.2). *(Cath)*
- **DFD / BDH:** the sign for funded pensions and health financing under a higher world rate
  (§3.3). *(Nina / Beth)*
- **Aurora-Energy:** hosted machine-and-generation capital as the participant scenario. The
  paper's depreciation rows are the quantitative anchor. *(Elle)*

---

## 5. Ingestion record (build instruction §3)

- **Whole-document read.** The full 74-page text was read in this session (pdftotext). The
  §2.2 verification cites table and section numbers from that reading.
- **Local-model baseline.** `qwen3.5:9b` via ollama was run on the whole document in one prompt
  (62,556 prompt tokens, num_ctx 65,536, 578 s, split 31% CPU / 69% GPU). Questions:
  `_ingestion/qwen_ingest_questions.md`. Answers: `_ingestion/qwen_ingest_answers.md`. Script:
  `_ingestion/qwen_ingest.py`.

### 5.1 Local-model comparison

| Question | Local model | Verdict |
|---|---|---|
| Q1 Production structure | CES aggregator written as ∫ω_i Y_i^σ with exponent 1/(σ−1). Machine-assignment condition inverted. Automation parameters α, a(t), ā, T, q not named | **Misread equations** (eq. 1, eq. 17) |
| Q2 Closure | Closed economy, rate set at home, Prop. 13 quoted | Correct |
| Q3 Headlines | 11.7% / 2.2% / 23%, tied to σ = 0.2, Table 4A | Correct, though it first says the figures "hold generally" |
| Q4 Saving identity | Prop. 10, eq. 57, capital share not thrift | Correct |
| Q5 Yields | Short rate fixed on impact; 10y 5.1 → 13.6 / 9.3 | Correct |
| Q6 Tax instruments | Gives the flat 25% tax the balanced-budget tax's temporary costs (1.1 / 3.3 points, zero in the long run). Misses the flat tax's permanent cost (5.7 / 3.1 points), its 20–22%-of-GDP revenue, the transfer peaks, and the incidence result | **Misread §8.3** |
| Q7 Open economy, bystander, debt, power plants | All "NOT IN TEXT"; power plants noted once in the Introduction | Correct on scope. Misses the Appendix A depreciation mention |
| Q8 Wages, hand-to-mouth | 28% of trend; −40–41% / −65–66% | Correct |

**Escalation (Elle's standing fallback rule).** The local model misread the model's equations and
the tax section, which is the input to Cath's lens. That triggers escalation. The reading of record
for this note is the full-text reading in the Claude Code session, with section, table and
equation citations in §2. The local run is retained as the baseline. It is a useful check on
closure, headlines, yields and distribution, but not on equations or §8.3.

---

## 6. Citation

Fernández-Villaverde, Jesús (2026). "Saving for the Machines." Working paper, University of
Pennsylvania, CEPR, NBER. First draft dated 20 October 2026, 74 pp. including Online Appendix.
JEL E21, E22, E43, O33, O41.

Other works cited in the inferences, with full references in the cited corpus entries or standard:
- Auclert, Malmberg, Rognlie & Straub (2025), NBER WP 34470.
- Benzell, Kotlikoff & Ye (2026), NBER aging conference.
- Gordon, R. H. (1986), "Taxation of Investment and Savings in a World Economy," *AER* 76(5).
- Carstens, A. & H. S. Shin (2019), "Emerging Markets Aren't Out of the Woods Yet," *Foreign Affairs*.
- Brunnermeier, M. & R. Reis (2023), *A Crash Course on Crises*.

## 7. Cross-references

- → Build instruction: `_crossrefs/_build_instructions/20261025_BUILD-AURORA_saving-for-the-machines_mexico_v1.1.md`
  (supersedes v1, filed alongside it). Filed by Héctor's decision of 2026-10-25.
- → Source PDF: `GrandPlan/Aurora/capital/Saving_Machines.pdf` (kept untracked: unpublished draft)
- → Claude Doc rendering of this note (private until shared): https://claude.ai/artifact/XxVSKpppC35Z8N8A6sFkiU
- → Ingestion record: `GrandPlan/Aurora/capital/_ingestion/`
- → `GrandPlan/DFD/docs/corpus/auclert_et_al_2025_rag.md`: asset race, reverse crowding-out,
  México structural gaps.
- → `GrandPlan/DFD/aging_macro_nber_2609/2026-09-17_global-transition-demographics-ai.md`:
  Benzell–Kotlikoff–Ye, Mexico region, non-adoption, mobile capital.
- → `GrandPlan/DFD/aging_macro_nber_2609/2026-09-17_aging-realignment-world-trade.md`: Kopecky,
  the open BKY-vs-Kopecky question for Anne and Cath.
- → `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/` (Nota EIC 2025 v1.0, endorsed): México
  demographic and contribution-rate path.
- → `_crossrefs/corpus/demographics/2026-08-13_fernandez-villaverde-norrick_terra-incognita.md`:
  same author. The paper's ψ̂_ℓ = 1.62% target comes from Fernández-Villaverde & Norrick (2026).
- → `GrandPlan/Aurora/Aurora_Nina_MonetaryFoundation_202604.md`: Nina's Brunnermeier–Reis
  amplification framing for Aurora.
- → `GrandPlan/RF/_index.md`: 17% → 25% tax-pressure target.
- → `Missions/Funded/CAF_DEM/caf-dem-entregable-final/CAF_DEM_P4_correccion_intereses_Mexico_reporte.md`:
  SHCP interest cost 3.4% of GDP (2024).

# Briefing for Beth — what the motivation build is worth as research, after a novelty check

**From:** Héctor (discussion run on Dalila, 2026-08-09)
**Mission:** BID2 · health-refocused paper → post-paper research agenda
**Supersedes nothing.** Extends `20260808_BID2_briefing_beth_motivation.md` (the
build itself) and revises the Track 2 agenda parked with Debb in
`20260808_BID2_briefing_debb_agenda_split.md`.
**Track discipline unchanged:** nothing here is actionable before the
September 2 objective. This note exists so the agenda survives contact with the
literature rather than evaporating or, worse, being written up as new.

---

## How this note was produced

Beth was asked to judge the six parked findings as an economist and to say what
was missing. Independently and in parallel, a literature check tested the five
central claims for novelty. The check contradicted Beth's top two rankings; she
was shown the contradictions and asked to revise rather than defend. What
follows is the revised position, with the disagreements kept visible.

The single most consequential result is negative, so it goes first.

## The 2020 episode is largely already published

Serván-Mori et al., *Journal of Global Health* 2023, "Increase of catastrophic
and impoverishing health expenditures in Mexico associated to policy changes and
the COVID-19 pandemic" — ENIGH 2018 vs 2020, 162,204 households, two-stage
probit — reports households with **any** health spending up 17.2 percent while
mean spending among positive spenders **fell** 7.5 percent. That is our
participation-versus-intensity finding, same sign, already in print. The paper
attributes it to the Seguro Popular / INSABI dismantling plus budget cuts, and
states explicitly that it cannot separate pandemic from policy. México Evalúa
has the 2018–2024 decile series (+41.4 percent overall, +83 percent in the
poorest decile), close to our own numbers.

This does not damage the *paper*: the motivation section uses the episode as
evidence, and evidence that others have also found is stronger evidence, not
weaker. It damages the *research agenda*, where item 1 was ranked "plausibly the
strongest of the six" on the assumption that the finding was ours.

What survives, on Beth's revised accounting, is narrower and real:

1. **Persistence through 2022 and 2024.** A two-wave design cannot see it, and
   it is the discriminant between a transitory epidemic and an institutional
   change.
2. **The state-level INSABI adherence design** — separating INSABI from COVID
   using the convenio that some states signed and roughly a dozen did not, which
   is precisely the separation Serván-Mori state they cannot perform.
3. **Provider-composition mechanism** via ENIGH's `servmed` place-of-care codes.

Her verdict: a comment-plus-design paper in a policy or regional journal, not a
lead paper — and worth doing only if the adherence first stage is visible in the
data. Otherwise fold the persistence fact into the financial-protection line as
validation and drop the rest.

## A contradicting paper, and a vulnerability in our own numbers

Lara & Serio, *Value in Health Regional Issues* 2024, find **reduced** Mexican
household health spending during COVID — dental, laboratory and diagnostic
studies. Opposite sign to ours.

Beth's reading is that the most likely reconciliation is the **deflator**, and
that this is our exposure rather than theirs. We deflate with the **general**
INPC because the INEGI open-data indicator file ships no health subindex, a
decision recorded in `provenance.md` and repeated in every figure note. Mexican
health prices rose materially faster than the general index in 2020. Under a
health-specific deflator our +36 percent conditional-on-positive in decile 1
shrinks, and could plausibly change sign at the top — which would reconcile the
two papers. The second candidate is composition: their declining categories are
discretionary and facility-based, exactly what a lockdown suppresses, while
medicines and consultations rose.

Two checks, in order, both cheap and both on data already downloaded:

- Rebuild the 2018→2020 deflation with the INPC **health subindex** (present in
  the full INPC concept series, absent from the indicator file we used) and
  re-run `scripts/11_pandemic_jump.R`.
- Decompose the jump by clave. 2018 and 2020 both use the J001–J072 scheme, so
  composition *is* comparable across that pair — unlike 2018 vs 2024 — and the
  question is whether dental, optical and laboratory claves fell while medicines
  and consultations rose.

**This is a decision for Héctor, not an action taken.** The drafted section
states the +76/+29 percent figures as real changes and names the general INPC in
every figure note, so it is honest as it stands. But if the health-deflated
numbers are materially smaller, we would rather know before a referee does. The
rerun is minutes of compute; the question is whether it counts as a Track 1
violation. My reading is that it is a robustness check on a number already in
the draft rather than new analysis, and therefore allowed — but the call is
yours.

## The revised top three

**1. ENIGH zeros reinterpreted through measured unmet need.** Unchanged at the
top, and the novelty check strengthened it: the hurdle/zeros literature is
mature and Mexican unmet-need measurement exists, but no work was found linking
ENSANUT unmet need to reinterpret ENIGH zeros. The proposal is not a new
estimator; it is that the zero regime can be *identified* rather than assumed.
The concrete output is a financial-protection indicator net of rationing —
catastrophic spending ∪ cost-related unmet need — which should reorder deciles
and plausibly states. Everything needed is downloaded. Two to three months, and
directly serviceable as an IDB technical note under BDH, which is why it leads.

**2. The wealth gradient in the spending response to health decline.** Promoted
from a calibration moment to the lead empirical paper. The literature check
found frailty-index mortality prediction in MHAS well established, frailty × OOP
done, and OOP by social-security status published — but nothing
De Nardi–French–Jones-shaped for Mexico on the *response* margin. Our object is
that spending after a frailty decline of at least 0.10 rises 10,819 pesos in the
bottom wealth tercile against 21,230 in the top (`fig10_spending_response_by_wealth.csv`).
Target the ratio, ≈1.96, never the levels. Three to four months.

**3. The 2020 episode as an extension**, on the terms above.

## Kill list, and one correction of our own record

- **The middle-tercile mortality anomaly is nothing. Kill it.** Post-decline
  mortality is 17.4 / 20.1 / 10.5 percent with standard errors of 3.7 / 5.0 /
  3.0 points. The T1–T2 difference the item is named after is 2.8 points against
  a difference standard error near 6.2 — a coin, not a fact. It also has a
  mechanical explanation running the wrong way: non-death attrition is *highest*
  in the top wealth tercile (7.7 vs 5.0 percent, `VERIFICATION.md` §5), and
  unobserved deaths among attriters push top-tercile mortality down. With no age
  adjustment in a 50+ panel where wealth and age co-move, there is no residual.
- **"The reconstruction outperforms the published index" rests on a false
  premise.** Pseudo-R² 0.167 against 0.142 is computed on a different and larger
  sample (16,702 vs 14,867; 1,525 vs 1,229 deaths). Deviance pseudo-R² is not
  comparable across samples. Nothing has been outperformed. This is an email to
  Judy asking for the deficit list and the sample restriction, not a methods
  note — and the Debb briefing should be corrected on this point.
- **Curative-versus-preventive is established.** SHA 2011 already provides
  HC.6 (preventive care) × HF.3 (household out-of-pocket), with OECD
  supplementary guidance and a documented COICOP correspondence; OECD puts
  Mexican prevention at 3.6 percent of current health expenditure, consistent
  with our ~2 percent of out-of-pocket. Our hand-built classification is
  contestable *because* SHA exists. It stays as an auditable appendix supporting
  the paper's argument; it is not a research line. One thing to verify: whether
  GHED publishes HC.6 × HF.3 for Mexico.
- **The GHED reconciliation is probably not what we thought.** Mexico's GHED
  out-of-pocket figure appears to come from DGIS/SICUENTAS *Gasto Privado en
  Salud*, which is likely built **from ENIGH** with expansion factors. If so,
  "surveys undercapture" is vacuous and the reconciliation paper dies. What
  survives is sharper and smaller: the 0.217→0.320 jump at 2020 would then be a
  jump in DGIS's own adjustment factor inside a headline financial-protection
  statistic — a short methodological note. One document settles it: the
  DGIS/SICUENTAS methodological note for *Gasto Privado en Salud*. Its server
  certificate has expired; request it through CIEP, who use these series, or via
  INEGI's Cuenta Satélite del Sector Salud methodological annex.

## What the agenda was missing: the fragmentation questions

This is Beth's domain and the part the current framing underuses. "Public
provision" is being treated as one object. It is four — IMSS, ISSSTE, the
non-contributory pillar that changed architecture twice in five years, and
private — with different financing and different failure modes. Three questions
nobody had listed:

1. **Entitlement without access.** ENSANUT's bypass battery asks people entitled
   to a scheme why they did not use it, including "they make me pay for
   consultations and medicines"; ENIGH pairs entitlement with place of care. The
   gap between nominal coverage and realized use, by scheme and income, is
   directly measurable, is the central policy fact for the IDB, and has not been
   computed here.
2. **Procyclical insurance.** IMSS entitlement is lost with the formal job, so
   coverage disappears exactly when it is needed. Our own forgone-care numbers
   already show the uninsured worst off on both margins (18.1 vs 9.9 percent
   against IMSS in 2024). This is a social-security question rather than a
   health one, which is why it belongs to Beth and not to the current draft.
3. **What in-kind provision is worth.** The 2020 participation margin gives a
   bounded lower estimate of the transfer value of free care: the outlay newly
   incurred by households that previously spent nothing. Small in pesos at the
   bottom, enormous in budget share — roughly +76 percent against total
   expenditure +9.9 percent in the poorest decile. That contrast is the welfare
   point.

**An asset nobody was using.** The ENIGH `poblacion` file — already downloaded,
all four waves — carries per person: entitlement, whether a health problem
occurred, whether care was sought and received, **where** (including the INSABI
and IMSS-Bienestar codes and pharmacy-adjacent consultorios), whether the person
paid, and why they went untreated, including *falta de dinero*. Unmet need,
provider, entitlement, payment, income and out-of-pocket spending are therefore
all in one survey, design-based, across four waves spanning Seguro Popular →
INSABI and pandemic → IMSS-Bienestar. Nothing in the parked six used it. It is
what makes line 1 cheap and it is the reason the ranking changed.

## The structural bridge — which findings are moments and which are scenery

The novelty check does not touch this section, and it is the part with the most
direct value to DFD.

*Genuine identifying moments.* The type-specific response to a health shock
(ratio ≈1.96, never the levels) identifies the tightness of the type-specific
budget constraint. The extensive margin — 45.5 percent zeros in the poorest
decile against 27.9 in the richest among under-65 households — identifies the
free in-kind quantity plus any fixed access cost; no model with a smooth
interior choice produces 45 percent zeros. Inequality inside the age profile
(top/bottom tercile ratio 3.3 at ages 75–84) identifies the income elasticity of
restoration. Rationing probability by type maps to the forgone-care gradient —
use the total gradient, 19.2 against 8.9 percent, not the cost-attributed one,
which is too thin at 3.5 to 0.1 percent to calibrate against.

*Validation, not targets.* Catastrophic incidence by decile is a nonlinear
function of moments already used and makes a good over-identification check. The
2020 episode is the best out-of-sample test available: set the free in-kind
quantity to zero for one period in a model calibrated to normal times and see
whether it reproduces +76 percent at the bottom and +29 at the top with a 13–15
point collapse in zeros. It should not be a target.

*Motivating only, and we should say so in print.* The age–sex profile **levels**;
the preventive share, whose 2–46 percent bracket spans the entire economically
interesting range and therefore disciplines nothing; and the mortality gradient,
which should not touch survival — Anne's WPP/Brass primitives are the right
source.

## Sequencing: publish the moment, then spend it

Beth's answer to whether the wealth gradient should be a reduced-form paper or a
calibration target is: both, in that order, never in parallel. A moment embedded
in a structural paper receives no independent scrutiny and earns no citation,
and this one carries caveats — differential attrition, the provisional frailty
index, ENASEM levels three to four times ENIGH's — that would be buried in a
calibration table and fatal if a referee surfaced them later. Publishing the
ratio first converts those caveats into stated robustness and gives DFD a
citable target rather than an unexamined one. The empirical paper claims the
fact; the structural paper claims what the fact identifies.

## What would falsify the lead line

For the financial-protection line: if cost-related unmet need in ENIGH turns out
to be small and *flat* across deciles once measured in the same survey as the
spending, the adjusted indicator will not move the ranking and there is no paper
— only a footnote. And if the adjusted indicator turns out to be a monotone
transform of the poverty rate, it is not an indicator, it is income measured
twice.

For the 2020 extension: a pre-trend, if ENIGH 2016→2018 already shows real
out-of-pocket rising and zeros falling in the poorest deciles at a comparable
rate; or a null on provider composition, if place-of-care shares show no shift
away from public providers between 2018 and 2020 while spending rose — in which
case the story is prices or self-medication and the insurance-value framing is
simply wrong.

## What I am asking

1. **Ratify or contest the demotion of the 2020 episode.** You own the
   health-financing judgment; if you think the persistence-plus-adherence design
   is a lead paper rather than a comment, say so.
2. **Rule on the deflator rerun** — whether re-deflating 2018→2020 with the INPC
   health subindex counts as a permitted robustness check before September 2.
3. **Take the fragmentation questions**, which are yours and which the current
   agenda does not contain.

Everything else can wait until after September 2, per the two-track rule.

## Pointers

Canonical work: `Missions/Funded/BID2/motivation/` on branch
`p3-correcciones-tex` — `output/READTHIS.md` first, `output/NUMBERS.md` for any
number quoted here, `output/tables/` for the sources. The drafted section is
`draft/motivation_section.tex`, with a compilable Overleaf project in
`overleaf_motivation/`. Prior briefings: `_crossrefs/team/{anne,beth,debb,fina,judy}/`.

Named literature in this note came from a search-based check, not from our
files. Sources that were actually retrieved are named; where the check reported
a prior about a literature rather than a specific paper, that is said in place.
Three things it could not verify and that should be confirmed before anything is
built on them: the DGIS construction of Mexico's GHED out-of-pocket figure
(dead link), whether GHED publishes HC.6 × HF.3 for Mexico, and the magnitude of
the ENIGH `noatenc` unmet-need battery, which was read in the dictionary but not
tabulated.

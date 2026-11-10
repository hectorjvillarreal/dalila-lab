---
type: corpus_entry
tier: foundational_text
project_scope: [RF, DFD, FISCUS, teaching_MEK_FP2026]
authors: [Bénassy-Quéré, Agnès; Cœuré, Benoît; Jacquet, Pierre; Pisani-Ferry, Jean]
year: 2019
title: "Economic Policy: Theory and Practice — Chapter 4, Fiscal Policy"
venue: "Oxford University Press, 2nd edition, pp. 148–236"
doi: "https://global.oup.com/academic/product/economic-policy-9780190912109"
date_added: 2026-11-09
added_by: Claude Code (drafted for Debb)
endorsed_by:
build_instruction: "2026-11-09_fiscal_policy_corpus_initial.md"
source_copy: "Héctor's purchased hardcover; photographed 2026-11-09; PDF at Teaching/MEK_FP2026/benassy_quere_cap4_fiscal_261109/benassy_quere_cap4_fiscal_policy.pdf"
transcription_status: transcribed_2026-11-09 — local VLM (qwen3.5:9b); all box equations and ~30 pages of prose checked against page images by Claude Code; Cath review 2026-11-09 items A1–A4 and B1–B5 applied; awaiting Cath's re-check of A1 and endorsement
confidentiality: personal study copy — do not redistribute
---

# Bénassy-Quéré et al. (2019), Chapter 4 — Fiscal Policy

## Status

Photographed PDF complete, pp. 148–236 (44 spreads + final page). Markdown transcription below, produced 2026-11-09 by the local vision model `qwen3.5:9b` (ollama) from the photographed pages, one page at a time, and merged by Claude Code.

**Verification done:** every display equation in Boxes 4.2, 4.5, 4.9, 4.10, 4.11, 4.12, 4.13, 4.14 and equations (4.1)–(4.2), plus Boxes 4.15 and 4.20 and Table 4.2, compared symbol by symbol with the page images: all exact. Prose compared on pp. 149, 152, 163, 165, 177, 180–181, 184–185, 189, 192, 194–195, 199–203, 212–213, 219, 224–225: near-verbatim; a handful of skipped or duplicated lines were corrected.

**Cath's review (2026-11-09) applied:** (B4.13.6) misprint confirmed on the page image and annotated; (B4.5.4)–(B4.5.5) now carry the printed $\cong$; Box 4.14 first paragraph restored from the image; duplicated half-line in Box 4.5 removed; all placeholder footnotes deleted and box footnotes re-lettered (`[^b4-Na]`); `<!-- end Box 4.x -->` markers added for all 20 boxes; equation tags normalised to the printed form; box anchors `box-4-17/18/19` added with an extended misprint note; chart descriptions carry an inline marker; p. 200 clipped paragraphs marked paraphrase-only; Team notes 1–2 (Cath) inserted under Boxes 4.5 and 4.13. Verified on the images: (B4.14.1)–(B4.14.2) are printed with $D_t$ and no $dt$, as transcribed.

**Known limitations:**
- p. 200, two lower paragraphs: the right margin is clipped in the photo; the last words of each line were inferred by the model. Marked inline as paraphrase-only.
- Chart descriptions under **Figure** captions are model-generated readings of the plot, not book text; each carries an inline marker. Verify against the PDF before citing numbers.
- Chapter end-notes (pp. 228–230) are transcribed under `## Notes`. In-text note numbers are as the model read them and have not been individually re-checked against the images, except that 35 of the 37 end-notes are referenced exactly once; notes 13 and 25 have no in-text marker (dropped by the model). Box footnotes are lettered `[^b4-Na]`.
- Box ends are marked `<!-- end Box 4.x -->`; the book interrupts one sentence on p. 152 with Box 4.1 (the sentence resumes after the box on p. 153).
- Pages before 148 (none in this chapter) and the book's index are out of scope.

Page markers `<!-- p. NNN -->` precede each page's text for citation.

## Chapter map (from the photographed pages; to be completed with the transcription)

| Book page | Content observed |
|---|---|
| 148–149 | Chapter opener; allocation, redistribution and stabilisation as the three fiscal functions |
| 150–151 | Post-2008 stimulus; stacked-bar figure on fiscal packages |
| 152–153 | Box 4.1 budget process; financial balance = primary balance − interest payments |
| 154–155 | Cyclical sensitivity of revenues and spending; structural balance shortcomings post-2008 |
| 156–159 | Decomposition into cyclical and structural primary balance (CAPB); Box 4.3 cyclically adjusted deficits in the EU; public debt accumulation identity |
| 160–161 | Perimeter of government debt; Box 4.4 the market for government debt; gross financing needs; seigniorage and monetisation |
| 162–165 | c) Public debt dynamics; Figure 4.5 contributions to the change in debt/GDP 2007–2014 (US, France, Italy, Greece); Box 4.5 debt dynamics algebra, debt-stabilising primary balance; d) shades of liabilities, Maastricht definition |
| 166–181 | Sustainability, crises, default and restructuring (incl. Greek debt saga, pp. 176–179) |
| 182–197 | Theories: IS-LM / policy mix (p. 183), Ricardian equivalence (p. 186), automatic stabilisers, fiscal space (p. 198) |
| 198–205 | Box 4.14 public debt and fiscal policy effectiveness; multipliers; Box 4.15 Mundell–Fleming (p. 204) |
| 206–215 | Policies: rules and institutions (p. 206), deficit bias explanations, Box 4.18 fiscal rules and institutions (p. 213), Greek restructuring and CACs (p. 214) |
| 216–227 | Sovereign borrowing in a monetary union (p. 216–219), the euro-area fiscal framework (p. 222), Box 4.20 fiscal policy spillovers within a monetary union (p. 224), policy coordination (p. 226) |
| 228–236 | Conclusion: old vs new consensus on fiscal policy; notes; references |

## Why this chapter matters to the team

- **RF**: supplies the standard vocabulary for classifying fiscal events (discretionary vs automatic, rules vs discretion, consolidation episodes) in the 2000–2025 Mexican narrative.
- **DFD**: the debt-dynamics block (Box 4.5) is the reference form for the OLG/DSGE government budget constraint and the r − g discussion.
- **FISCUS**: the definitions of balances, debt perimeters and rules are the conceptual layer the natural-language interface must translate faithfully.
- **Teaching**: core reading for the MEK_FP2026 fiscal policy sessions.

## Transcription

*Source: Bénassy-Quéré, Cœuré, Jacquet & Pisani-Ferry (2019), Economic Policy: Theory and Practice, 2nd ed., Oxford University Press, Chapter 4, pp. 148–236. Personal study copy transcribed from Héctor's own book. Not for redistribution.*

---

<!-- p. 148 -->

# 4 Fiscal Policy

**Contents**

- **4.1 Issues**
    - 4.1.1 What is it all about?
    - 4.1.2 Lessons from history
- **4.2 Theories**
    - 4.2.1 Demand-side effects
    - 4.2.2 Public debt sustainability
    - 4.2.3 Open economy dimensions
- **4.3 Policies**
    - 4.3.1 Fiscal rules and institutions
    - 4.3.2 Sovereign debt crises resolution
    - 4.3.3 Fiscal policy in the euro area
    - 4.3.4 Conclusion: Old and new views on fiscal policy
- **Notes**
- **References**

The government budget simultaneously fulfills the three functions of allocation, redistribution, and stabilization analyzed in Chapter 1: governments build infrastructure, invest in research, and provide public services such as education; they levy progressive taxes and provide means-related transfers; and they let the budget balance oscillate with the cycle in order to smooth out economic fluctuations.

Even though these functions are intricately intertwined, *fiscal policy* (also called *budgetary policy* in Europe) nowadays mainly refers to stabilization. It consists in all decisions concerning government spending and taxation that are taken in order to influence aggregate demand and to steer the economy toward equilibrium. The decision may be to adjust spending or taxes (in which case we refer to *discretionary fiscal policy*) or to let them evolve automatically depending on growth and inflation (in which case we refer to *automatic stabilizers*).

Fiscal policy is a relative novelty. In the nineteenth and the early twentieth centuries, the primary economic role of a government was to build and maintain roads and other infrastructure, as well as to provide education and postal <!-- p. 149 --> services (law and order, or defense being arguably not primarily economic functions). Allocation therefore came first.

Redistribution has in a way always been a dimension of fiscal policy because disputes over the distribution of the burden started with the first levies; social policies also emerged early—in Rome, bread consumption started being subsidized in 140 BC. But it is only in the late nineteenth century, with the introduction of the progressive income tax (in 1842 in the United Kingdom and 1862 in the United States) and with the creation of social insurance (in Germany in 1889) that the redistributive state started to take shape.

The idea that management of the government budget can stabilize the economy—that is, that it can help to keep unemployment close to its equilibrium value and avoid the build-up of deflationary or inflationary pressures—was a twentieth-century invention. It owed considerably to John Maynard Keynes and disciples such as Paul Samuelson. In the highly stylized world of macroeconomics, the fiscal decision-maker handles the budget in the same way that the monetary decision-maker handles the interest rate, and their parallel actions make it possible to achieve both low unemployment and price stability.

Stabilization, however, does not only result from decisions. The macroeconomic role of the state owes at least as much to the secular rise of the share of public expenditures in gross domestic product (GDP) that resulted from the generalization of old-age and health insurance, as well as from welfare and publicly funded education programs. In the United States, for example, total government expenditure as a proportion of GDP rose from 2% before World War I to 10% on the eve of World War II, 20% in the 1950s, and 30% in the 1970s. It fluctuated between 30% and 40% until the Great Recession, which made it pass the 40% mark. In Europe, it started from a higher level (about 10% in France and the United Kingdom, and 20% in Germany before World War I) and has reached higher levels (roughly between 45% and 55% of GDP).[^1] Within the course of half a century, governments have thus been transformed from irrelevant macroeconomic players into major contributors to aggregate demand.

The consensus on stabilization policy has never been complete. In post-World War II Germany especially, it has almost always been regarded with suspicion. Even in countries where it was more widely accepted, such as the United States or the United Kingdom, empirical and theoretical doubts surfaced in the late twentieth century about the effectiveness of active fiscal policy. The 1970s first witnessed its ineffectiveness in response to an oil shock. Then, the 1980s saw the emergence of theoretical challenges (or the reemergence of old ones). And in the 1990s, experiences with failed fiscal expansions and a few cases of painless consolidations prompted a reassessment of the growth effects of a fiscal stimulus. By 2000, faith in fiscal activism had been shattered: the consensus among policymakers was that, beyond the automatic stabilization


<!-- p. 150 -->

provided by the public budget (e.g., by keeping stable expenditures in a downturn), there was not much room for active policies.

A few years later, the global financial crisis brought fiscal policy back to the forefront. In 2009–2010, in response to the fall in GDP, virtually all the largest advanced and emerging countries undertook a major stimulus effort that helped contain the global recession. In the following years, the effectiveness of fiscal policy was positively reassessed in a context of depressed demand, deflationary pressures, and near-zero interest rates. Under such conditions it was found to be both more effective and more necessary.

Already in 2010, however, several sovereign debtors, starting with Ireland and Greece, began having difficulty borrowing on the debt market because of concerns over solvency—an old issue that had come to be regarded as a concern of the past in the advanced world (though not in the emerging and developing world). This triggered renewed discussions on whether fiscal expansions are effective when public debt reaches a high level.

Hence, consensus views about fiscal policy have changed over time and will continue to evolve. It should be noted, however, that structural changes such as the opening up of most economies, the development of financial markets, or different monetary arrangements have also changed the channels and trade-offs of fiscal policy and justified observed evolutions in the making of fiscal policy.

---

## 4.1 Issues

### 4.1.1 What is it all about?

#### a) Budgets, surpluses, and deficits

A public budget is a document that specifies the origin and volume of both income (“receipts”) and intended spending over a certain time horizon (usually a year). Receipts consist of income from direct and indirect taxation, social insurance contributions, revenues from public assets, sale of public services, and, possibly, the disposal of public assets. Spending is made on core sovereign activities (such as police, justice, foreign policy, and defense), the provision of public services (education, health care), indirect or direct support to the economy and society (infrastructure, research), social transfers, and interest on public debt.

Budgets are established autonomously by different public entities such as the central government, public agencies, and state and local governments. Budgeting practices are generally broadly similar across subcomponents of government. For international comparison and overall monitoring purposes, statisticians aggregate their account into that of the *general government*.

Although there has been a general trend away from centralization, the degree of fiscal decentralization still varies considerably across countries (see figure 4.1). In 2016, central government spending represented 91% of total spending in the United Kingdom and 28% in Germany. Also, social insurance

**Figure 4.1**

*Fiscal decentralization across selected countries in 2016.*

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart displays the share of subnational (state/local) government spending as a percentage of total government spending for various countries. The United Kingdom shows very low decentralization (~9%), while Germany exhibits moderate levels (~72%). Other countries like Canada, Australia, and Brazil show intermediate values between 30% and 60%. Data source: OECD National Accounts database.

<!-- p. 151 -->

**Figure 4.1** Distribution of spending by level of government, 2016 (in percent of total general government spending). OECD, *Government at a Glance* statistics, 2017.

can either be an integral part of the central (or partially state and local) government or financed separately from specific contributions.[^2]

Familiar budget categories include *capital expenditures* (investment on infrastructure and, since recent revisions of national account systems, also spending on research and development) and *current expenditures* (all other items). Interest charges on the public debt depend on the debt level and on long-term interest rates, two variables that, in the short run at least, are beyond the control of the government. Therefore, a useful concept to assess the evolution of spending is that of *primary expenditures* (all spending except interest on public debt). Conditional financial assistance programs negotiated by the International Monetary Fund (IMF) generally specify targets for primary expenditures.

Government accounting rules differ across countries, but the European Union has put in place a harmonized system of public accounts. All accounts are now recorded on an *accrual basis* rather than on a *cash basis* (meaning that transactions are recorded when economic value is created or when claims arise rather than when payments are made). European procedures also distinguish exceptional, or *one-off expenditures*, from *recurring expenditures*.

The preparation of the draft budget, its discussion, and its adoption by parliament are important stages of economic policy decision-making. Organization, procedures, and the time frame vary substantially from country


<!-- p. 152 -->

to country. A typical sequence includes the preparation of economic and government receipts forecasts; the setting of expenditure ceilings by sectors; the preparation, by the government departments, of their own draft budgets; cabinet discussions and the consolidation of the whole budget; and discussions and final vote in parliament. The overall process requires at least six months (see the US federal budget process in box 4.1). in parliament. The overall process requires at least six months (see the US federal budget process in box 4.1).

The fiscal (or budgetary) balance, also called financial balance or net government lending, is the difference between income and expenditure. There is a fiscal (or budget) surplus when the balance is positive and a fiscal (or budget) deficit when the balance is negative. The primary spending concept translates

#### Box 4.1 The US Federal Budget Process

The federal budget process begins each year with the submission of the President's budget proposal to Congress on the first Monday of February. By early April, the House and Senate budget committees (which may or may not draw on the President's proposal) submit their draft resolutions to the floor for adoption. Differences between the two chambers are resolved by a conference committee.

For the next phase, a distinction is made between mandatory and discretionary spending. The first refers to spending that is not subject to current congressional approval (for example, it may result from entitlements and other effects from laws enacted in the past—services votes to use the telling French expression). Discretionary spending, however, requires an appropriation bill. Both chambers work in parallel on 12 categories of spending, each of which is assigned to a different subcommittee. Bills are then passed in each chamber and differences are ironed out in a conference. The appropriation bills are expected to be signed into law by the President, at the latest on October 1. If not, Congress passes a continuing resolution to finance the government on a short-term basis and avoid a shutdown (as happened for example in 2013).

Meanwhile, mandatory spending is reviewed by authorizing committees that are also in charge of determining whether additional revenues are needed to finance it. The budget committee consolidates the authorizing plans into an omnibus package that is sent to the floor for vote and then to the President for signature.

The parliamentary process therefore takes eight months and often more if it is not concluded by October 1.[^b4-1a]

[^b4-1a]: See www.cbpp.org/research/policy-basics-introduction-to-the-federal-budget-process, and http://budget.house.gov/budgetprocess/budgettimetable.htm

<!-- end Box 4.1 -->


<!-- p. 153 -->

into a primary balance concept, to which we will return because it is useful for determining the dynamics of public debt:

Financial balance (net lending) = primary balance - interest payments on the debt

Figure 4.2 displays the evolution since 1960 of the financial balance and the primary balance for Italy, a country that has, for a quarter-century, struggled with public debt at or above 100% of GDP. It is apparent that the difference between the two concepts (corresponding to interest payments, represented as bars on the graph) was insignificant in the 1960s and the early 1970s, a period when both public debt ratios and interest rates were low. The gap then gained in importance as a consequence of both high interest rates and recurrent deficits leading up to public debt increases. Primary surpluses only returned in the 1990s, as a consequence of fiscal consolidation and a stronger macroeconomic environment. The peak was reached in 1997, when Italy qualified for the euro by reducing its deficit to 3% of GDP. Interestingly, interest payments also decreased markedly in the second half of the 1990s, again because of both lower interest rates and somewhat lower debt levels.

Fiscal balances tend to rise when economic activity is buoyant and to decline when it is depressed. This is because tax receipts fluctuate in line with

**Figure 4.2** Financial and primary balance in percentage of gross domestic product (GDP), Italy, 1960–2016. Authors’ calculations with OECD data.

<!-- p. 154 -->

economic activity (for instance, value-added tax [VAT] revenues depend on household consumption and corporate income tax receipts on corporate profits), whereas public spending does not vary accordingly or, for specific items such as unemployment benefits or transfers, rises in economic downturns. This spontaneous variation of the fiscal balance has a stabilizing effect on aggregate demand and the private sectors' net income (hence the notion of automatic stabilizers). For this reason, countries with larger governments tend to exhibit more aggregate macroeconomic stability.[^3]

In order to capture changes in fiscal policy, it is useful to calculate a cyclically adjusted balance that measures what the financial balance should be, would output be at its potential level (cf. box 4.2). The change in the cyclically adjusted balance from one period to next is traditionally regarded as providing a measure of the fiscal impulse or fiscal stance because, in contrast to

#### Box 4.2 Measuring Structural Deficits

The structural (or cyclically adjusted) public balance is usually defined as the public balance that would be obtained, were GDP at its potential level. To calculate it, the first step is to estimate the output gap; that is, the percentage difference between actual production and its potential level (see Chapter 1). Then, the average sensitivity of the financial balance $s$ (measured as a percentage of GDP) to a variation of the output gap is estimated. If $y$ is the logarithm of output and $\bar{y}$ that of potential output, this sensitivity is given by:

$$ \varepsilon = \frac{ds}{d(y - \bar{y})} > 0 \tag{B4.2.1} $$

where $d$ is the differentiation operator. The final step is to subtract the cyclical component $\varepsilon(y - \bar{y})$ from the financial balance $s$ to get the cyclically adjusted, or structural, balance $s^*$:

$$ s^* = s - \varepsilon(y - \bar{y}) \tag{B4.2.2} $$

The value of $s^*$ naturally depends on the method used to calculate potential output, and it is affected by the uncertainties surrounding it (cf. Chapter 1). It furthermore depends on the accuracy and stability of the sensitivity parameter $\varepsilon$.

Mourre et al. (2013) review the methodology in use in the EU for measuring $\varepsilon$. They find that its average value in the EU (or euro area) is slightly above 0.5, meaning that a 1 percent deviation of GDP from its potential level results in a 0.5 percentage point deviation of the budget balance. Because of differences in the size of government and the structure of revenues and expenditures, it is higher for some countries (0.65 for Denmark) and lower in others (0.43 for Spain).

<!-- p. 155 -->

Structural balances have shortcomings, which have been highlighted in the turbulent post-2008 environment: potential output is a notoriously fragile notion whose estimates are subject to changes over time and are cyclically sensitive (Coibion, Gorodnichenko, and Ulate, 2017); real-time revisions (Tereanu, Tuladhar, and Simone, 2014); and the elasticity of tax receipts with respect to variations in the tax base are unstable over time, which results in the instability of the sensitivity parameter. For these from real-time estimates.

Another issue is whether the change in the CAPB correctly measures the fiscal stance. Whereas it is often used for this purpose, the corresponding yearly estimates (generally dubbed *top-down* because they are derived from overall elasticities) may be far from what results from the aggregation of taxation and spending decisions by governments (*bottom-up* approach). Following Romer and Romer (2010), time series based on the aggregation of estimates of individual policy decisions have been built, notably by the IMF (Devries et al., 2011). Because it relies on actual fiscal moves rather than on an *ex post* reconstruction, this *narrative approach* is arguably better suited to measuring discretionary fiscal policy.

The bottom-up measurement of the fiscal effort is, however, not without flaws. It requires relying on an accurate costing of fiscal measures: for example, an evaluation of the budgetary impact of tax reforms. Estimates provided on the occasion of new legislations may be inaccurate, either by mistake or because the government has an incentive to underestimate the budgetary cost of new legislations.

<!-- end Box 4.2 -->

changes resulting from the automatic stabilizers, it is supposed to result from *discretionary fiscal policy decisions*.

The evolution of the financial balance can thus be decomposed into a cyclical component and a discretionary component, equal to the variation of the cyclically adjusted balance:

Financial balance (net lending) = cyclical balance + cyclically-adjusted balance

The cyclically adjusted balance is often also called the *structural balance*. In the EU fiscal framework, however, there is a slight difference between the two concepts: the structural balance is also purged from one-off receipts or expenditures, such as proceeds from asset sales or bank recapitalizations:

Structural balance = cyclically-adjusted balance – one-off net receipts

<!-- p. 156 -->

The same decomposition applies to the primary balance, which can therefore be split into a cyclical component and the structural primary balance, also called the *cyclically adjusted primary balance* (CAPB):

$$ \text{Primary balance} = \text{cyclical primary balance} + \text{CAPB} $$

A decomposition of the primary budget balance into the structural and cyclical primary balances indicates that the latter accounts for a large part of the short-term fluctuation (figure 4.3). Over the longer term, however, variations of the structural balance are key.

The structural deficit is the main indicator used by international organizations such as the IMF, the Organization for Economic Cooperation and Development (OECD) and the European Commission to monitor budgetary developments and formulate policy recommendations. However, it is not directly observable, and its measurement raises a host of technical difficulties. Two major pitfalls are, first, that the output gap is not measured with accuracy and, second, the instability of the estimated sensitivity of government expenditures and receipts to the level of economic activity (see box 4.2).

As a consequence, estimates of the structural balance vary across institutions and are subject to significant revisions. A particularly striking case is that of Ireland in 2007: it was initially assessed by the European Commission to be in safe structural surplus territory, yet successive revisions led to a reversal of the initial assessment (figure 4.4).

**Figure 4.3** Decomposition of the aggregate budget balance of the euro area, 1991–2016 (in percent of potential gross domestic product [GDP]). Authors’ calculations based on OECD Economic Outlook data.

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart displays the decomposition of the aggregate budget balance of the euro area from 1991 to 2016. The vertical axis represents the percentage of potential gross domestic product (GDP), ranging from -4% to +4%. The horizontal axis shows years from 1991 to 2016. Three series are plotted:

- **Cyclical primary balance (including exceptional transactions)**: represented by hatched bars.
- **Structural primary balance (excluding exceptional transactions)**: represented by solid black bars.
- **Primary balance**: shown as a line connecting the total values.

The cyclical component fluctuates significantly over time, reflecting economic cycles, while the structural component remains relatively stable but shows some shifts. The primary balance combines both components and reflects overall fiscal performance.

<!-- p. 157 -->

Another problem is that whereas the change from one year to the next in the cyclically adjusted balance is meant to represent discretionary policy actions, it often does not match estimates based on actual tax and spending decisions, with the difference being sometimes wide (see box 4.3). The concept of structural balance is therefore both an important one for policy discussions and a far from reliable one for policy decisions. Its use for budgetary surveillance is a cause for concern and a potential matter for disputes.

For 10 years, between 2005 and 2015, the EU gradually increased its emphasis on structural balance indicators (see box 4.3). Especially, the Treaty on Stability, Coordination and Governance (TSCG) of 2013 (also called *fiscal compact*) commits the signatories to keeping structural deficits below 0.5% of GDP over the medium term and mandates the setting of this objective in national laws (Germany introduced such a constitutional rule already in 2009, with a structural deficit limit set at 0.35% of GDP). The resulting fiscal framework has proved perplexing. Since the mid-2010s, doubts have grown in the EU over the wisdom of micromanaging fiscal positions on the basis of unobservable data.

#### b) Public debt

Receipts, expenditures, and balances are economic flows. They are generated in each period. Government assets and liabilities are instead stocks that are

**Figure 4.4** Successive evaluations of Ireland’s primary structural balance for the year 2007 (in percent of potential gross domestic product [GDP]). Authors’ calculations based on the European Commission’s economic forecasts.

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The bar chart displays successive evaluations of Ireland's primary structural balance for the year 2007, expressed as a percentage of potential GDP. The vertical axis ranges from -1 to 3, while the horizontal axis marks time periods from Spring 2007 through Spring 2011. Positive bars indicate surplus estimates, and negative bars show deficit projections. Values start high in Spring 2007 (around 3%), decline over subsequent years, and turn negative by Fall 2009 onward.

<!-- p. 158 -->

#### Box 4.3 The Use of Cyclically Adjusted Deficits in the EU

The Maastricht Treaty establishing EMU and the initial Stability and Growth Pact (SGP), the secondary legislation that sets out the operational framework for fiscal surveillance, made no room for cyclical corrections. Following the 2005 SGP reform and the decisions taken in the aftermath of the euro area crises, the framework was made more reliant on cyclically adjusted variables. Only the 3% threshold for deciding whether a country is in excessive deficit remained couched in headline terms.

By 2017, there were two main indicators in use.

**The Structural Balance**

The structural balance is the main indicator used for setting country-specific medium-term objectives under the “preventive arm” of the SGP and for deciding what fiscal adjustment Member States in excessive deficit positions under the “corrective arm” of the SGP should carry out (Mourre et al., 2013).

**The Discretionary Fiscal Effort**

Changes in the cyclically-adjusted primary balance (CAPB) or the structural deficit provide imprecise measures of the fiscal effort. Building on the action-based approach, the Commission has developed a new bottom-up indicator called the *discretionary fiscal effort*. On the revenue side, the discretionary fiscal effort aggregates the budgetary impact of individual tax decisions. On the expenditure side, the effort is based on the difference between potential output growth and the growth of public spending. Whereas the change in the structural deficit is meant to measure an outcome, the discretionary fiscal effort provides an indicator of the adequacy of the measures implemented to reduce the structural deficit (Carnot and de Castro, 2015). The discretionary fiscal effort is used in the “corrective arm” of the EU economic governance instituted to monitor national policies.

<!-- end Box 4.3 -->

transmitted from period to period: their value at the beginning of each year equals that at the end of the previous year, as for private assets and liabilities or a capital stock (see Chapter 1). For example, the *public*, or *government debt*—the total financial liabilities of the government—on January 1 equals that on December 31 of the previous year. From one year-end to the next, a deficit increases the debt, while a surplus can be used to pay it down or to buy financial assets.

<!-- p. 159 -->

Public debt accumulation arises because deficits must be financed through borrowing on the bond market or through loans from international organizations.[^4] In a simplified setting where the government finances itself by issuing a single type of bond, the relationship between the public deficit and the public debt is:

Debt at end of period $(t) = \text{Debt at end of period } (t-1)$

$+ \text{Financial deficit of period } (t)$

Formally, if $D$ represents the deficit and $B$ (for Bonds) the debt:

$$
B_t = B_{t-1} + D_t \tag{4.1}
$$

Debt therefore increases as long as there are deficits. In this typical stock-flow relationship, debt is measured in nominal terms (disregarding changes in its market valuation) and it is assumed that the government does not sell assets to finance its deficit nor borrow to invest in financial assets. From an accounting standpoint, however, these dimensions should be taken into account. In particular, *gross debt* should be distinguished from the debt net of government assets, which is called *net debt*: for example, the 234% of GDP gross debt government figure for Japan in 2015 is misleading because it neglects the fact that a large part of this debt is held by government agencies; debt net of financial assets is a still high but less frightening 126% of GDP.[^5] However, the concept of gross debt is generally used because government assets can be illiquid (see Section 4.1.1.d).

The previous equation can be rewritten, distinguishing the primary deficit and the interest on debt outstanding:

Debt at end of period $(t) = \text{Debt at end of period } (t-1)$

$+ \text{Interest payment on debt at end of period } (t-1)$

$+ \text{Primary deficit of period } (t)$

Formally, if $P$ is the primary balance (the opposite to the primary deficit) and $i$ the interest on public bonds,

$$
B_t = (1 + i) B_{t-1} - P_t \tag{4.2}
$$

Debt increases if interest payments on the outstanding stock exceed the primary balance. This is why the latter is a key target variable for overindebted countries.

Debt here represents the liabilities of the government or the public sector. Like for the deficits, alternative perimeters can be considered, from the narrow <!-- p. 160 --> confines of the central government's budgetary functions to the much more broadly encompassing public sector, which includes government agencies, social insurance institutions, local governments, and public entities benefiting from government guarantees. Differences in perimeter matter: in Canada for example, public debt at end 2010 varied from 39% to 67% of GDP depending on the definition chosen.

The old maturing debt securities need to be replaced throughout the year by new ones at prevailing interest rates, while additional debt is issued to finance the deficit. Total securities issuance over the year (i.e., the sum of maturing debts and deficit) is called *gross financing need*. The larger these are, the more difficult it is to tap into the market. If a country loses market access and is forced to rely on official assistance from the IMF and/or the European Stability Mechanism (ESM), the volume of assistance is determined by these needs, which explains the central role of this concept for the design of assistance programs (IMF, 2013):

$$
\text{Gross financing needs of } (t) = \text{Maturing debt of period } (t) + \text{Deficit of period } (t)
$$

Public debt (also called *sovereign debt* when the borrower is the central government) should not be confused with *external debt*, which represents the liabilities of all domestic agents—public as well as private—vis-à-vis the rest of the world. Of course, both concepts have a common component: government borrowing often results in the accumulation of liabilities vis-à-vis the rest of the world. But some countries, like Italy, exhibit both high levels of public debt and low levels of external debt.

In practice, there are several ways to finance a deficit and therefore several types of financial liabilities. The bulk of them consist in debt securities (long-term bonds and short-term bills) that give the creditors the right to payments in capital and interest, as specified by the associated debt contract (see box 4.4). But governments can also receive loans from banks or international organizations such as the IMF. Or they can incur debt in a hidden form: in situations of stress, they often delay payments to suppliers or even to public employees and pensioners. According to IMF research on a sample of 61 countries, bonds amount to 68% of total debt of the median country, whereas loans represent 22.5% and payables 8.4% (Dippelsman, Dziobek, and Gutiérrez Mangas, 2012).

An alternative to open indebtedness is for the government to finance itself through the national central bank (which amounts to creating money). The counterpart to this *monetization of the deficit* is an increase in the money supply. This practice originates in the capacity (called *seignorage*, see Chapter 5) of kings to finance expenses by printing money, and it used to be common, particularly to finance wars. Deficit monetization amounts to letting the requirements of the public Treasury, rather than the economy's needs, determine the pace of money creation; when sustained, it has proved

<!-- p. 161 -->

#### Box 4.4 The Market for Government Debt

In advanced economies, governments fund their financing needs by issuing securities. The amount issued within a given year has to cover the deficit of the year and the reimbursement of debt coming to maturity. This task is performed by ministries of finance or by separate agencies called *debt management offices*. Debt securities can be either short-run (*Treasury bills*, for example with a three-month or a one-year maturity) or long-run (*government bonds*, up to a 50-year maturity). The interest rate paid on debt is usually fixed. It can also be variable: in particular, some countries issue inflation-protected bonds (the return of which is indexed on inflation).

In advanced countries, the average maturity of public borrowing typically lies between 5 and 10 years, but it is somewhat shorter in the United States and longer in the United Kingdom. Governments in advanced countries generally borrow in their domestic currency, while those of emerging countries with less-developed financial markets often borrow in US dollars and, to a lesser extent, in euros. Foreign-currency borrowing may be cheaper but carries an exchange rate risk since the repayment is heavier if the home currency depreciates. Its repayment is also made riskier due to the material impossibility for the central bank to act as a lender of last resort to the government (the central bank only lends its own currency).

Government bonds are traded by investment banks and eventually purchased by institutional investors such as asset managers and pension funds (which manage household savings), insurance companies, central banks, and sovereign wealth funds.

Governments are usually considered more solvent than any private agent, and the interest rate that they pay on their debt is thus considered as the *risk-free interest rate*, on the basis of which all financial securities are valued. However, not all governments are equal, and their borrowing costs depend on their *credit quality*; that is, the likelihood assigned by investors that they will remain able to repay their debt in full. Investors often rely on the assessments provided by rating agencies, independent institutions which evaluate the creditworthiness of borrowers[^b4-4a]. A government’s borrowing rate includes a *risk premium* that depends on its rating and compensates the bond holder for the risk incurred.

Central banks typically hold treasury bonds as one of the counterparts of money; they buy (or accept as collateral in repurchase agreements; see Chapter 5) government securities from banks in exchange for providing them with liquidity. This mechanism differs from an outright monetization of the deficit to the extent that the government does not mandate the central bank to buy these securities. Amounts bought by independent central banks derive from monetary rather than fiscal policy considerations.

[^b4-4a]: The market for ratings is dominated by three agencies: Standard and Poor’s, Moody’s, and Fitch Ratings.

<!-- end Box 4.4 -->

<!-- p. 162 -->

#### c) Public debt dynamics

Most governments post significant public debt. Few record positive net financial wealth: this mainly applies to countries that hold foreign exchange reserves as an insurance against sudden capital outflows (see Chapter 7) or to countries that produce oil or raw material and intend to spread the benefits from extraction over several generations.[^6]

There can be good as well as bad reasons for a government to go into debt. Debt may fluctuate as a consequence of automatic or discretionary stabilization (but this is not a motive for sustained increase as the effects of booms normally offset those of recessions). For a country that must fight a war, ward off catastrophes, or undertake massive public investments, public borrowing is a way to spread the corresponding burden over several generations. In the case of war, it would be morally disputable to require the same generation that pays the price of blood to defend the nation against an aggressor to shoulder the corresponding financial effort. In the same way, a case could be made for partially financing action against climate change through debt: it would be a way to make the future generations pay for the milder climate they will benefit from. But public borrowing that repeatedly finances current expenditures is highly disputable. It is essentially a way to make the future generations pay for the consumption of the current one, and there are no plausible equity arguments to justify such behavior.

Debt, however, does not need to be repaid entirely because, unlike households, the public sector is not expected to die. Debt can be passed from one generation to the next. Furthermore, debt must be assessed in comparison to the country's national income. It is not the nominal amount of debt that matters, but its size in proportion to GDP as a broad measure of the tax base.

An identical rate of debt accumulation does not have the same consequences in a country whose nominal GDP grows at a fast pace and in a country where it stagnates. Nominal GDP growth resulting from real growth and inflation diminishes the burden of past debt and therefore makes deficits more sustainable. This can be illustrated by a comparison between the United States and three European countries: France, Italy, and Greece over 2007–2014 (figure 4.5). While the increase in nominal debt was higher in the United States than in the three European countries (Greece included!), it was in significant part offset by nominal GDP growth. In contrast, Italy did not record any nominal GDP growth effect, and, in Greece, the decline in nominal GDP was so large that its adverse impact on the debt ratio was almost twice as large as the opposite impact of the 2012 debt restructuring.

**Figure 4.5** *(figure appears on p. 162; caption and description on p. 163)*

<!-- p. 163 -->

**Figure 4.5** Contributions to the change in the public debt ratio, 2007–2014 (in percent of initial gross domestic product [GDP]).

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The graph gives a decomposition of the variation of the debt-to-GDP ratio into three effects: (a) the numerator effect resulting from the increase in nominal debt as a consequence of accumulated deficits, (b) the denominator effect resulting from nominal GDP growth, and (c) in the case of Greece, the impact of the 2012 debt restructuring on the 2014 debt stock.

Authors’ calculations based on IMF World Economic Outlook data.

As explained in more details in box 4.5, the dynamics of the public debt ratio can be described as a horse race between debt accumulation and nominal GDP growth: if the financial deficit remains below a threshold called the *debt-stabilizing deficit*, which is equal to the debt ratio times the nominal grow rate, the debt ratio diminishes; if it is above this threshold, it increases. This sheds light on the debt limit (60% of GDP) and the deficit limit (3% of GDP) set by the European treaty of Maastricht. It was at the time (1992) assumed that countries would grow at 5% annually (3% real growth and 2% inflation), which implied that $3\% = 5\% \times 60\%$ was the corresponding debt-stabilizing deficit.

The financial deficit ratio is, however, not the best variable to assess debt sustainability because it results in part from the interest payments on public debt, which are largely beyond the control of the current government. It is therefore preferable to write down the debt stabilization condition for the primary balance.

<!-- p. 164 -->

#### Box 4.5 Public Debt Dynamics

Let $\Delta$ be the primary public deficit, $B$ the public debt at year-end, both in euro, and $i$ the nominal interest rate. We neglect cash revenues and disbursements (such as asset sales and purchases) that may affect public debt for a given public deficit. We also suppose that debt is measured at face value and not at current market value, thus ignoring valuation effects. Such assumptions are common but not innocuous: in emerging countries, part of the public debt is US dollar-denominated, and exchange rate movements also influence debt dynamics (see Chapter 7).

The debt dynamics can be written as (with the $-1$ subscript denoting the end of the previous year):

$$B = (1+i)B_{-1} + \Delta \tag{B4.5.1}$$

If lowercase letters denote the ratios of the corresponding variables to GDP, $n$ is the nominal growth rate (growth in volume + inflation), $g$ the real growth rate, $\pi$ the rate of inflation, and $r$ the real *ex post* interest rate, we have:

$$n = g + \pi \tag{B4.5.2}$$

and

$$i = r + \pi \tag{B4.5.3}$$

Debt dynamics can thus be expressed as:

$$b = \frac{1+i}{1+n}b_{-1} + \delta \cong (1+i-n)b_{-1} + \delta = (1+r-g)b_{-1} + \delta \tag{B4.5.4}$$

or, equivalently:

$$b - b_{-1} \cong (i-n)b_{-1} + \delta \tag{B4.5.5}$$

The debt ratio increases if the interest rate is higher than the nominal GDP growth rate and there is not a sufficient offsetting primary surplus. Equation (B4.5.5) also gives the primary deficit that stabilizes the debt ratio:

$$\tilde{\delta} = (n-i)b \tag{B4.5.6}$$

A country whose nominal growth rate exceeds its nominal interest rate can run a primary deficit without seeing its debt-to-GDP ratio increase.

<!-- end Box 4.5 -->

> **Team note 1 — under Box 4.5 (Cath, 2026-11-09)**
>
> *Book notation → RF/DFD notation.* Let $pb_t \equiv -\delta_t$ be the primary surplus ratio and $d_t \equiv b_t$ the end-of-year debt ratio. The **exact** accumulation identity is
> $$d_t = \frac{1+i_t}{1+n_t}\,d_{t-1} - pb_t + sfa_t ,$$
> and the exact debt-stabilising primary surplus is
> $$pb^* = \frac{i-n}{1+n}\,d = \frac{r-g}{1+g}\,d \quad (\text{with } 1+i=(1+r)(1+\pi),\ 1+n=(1+g)(1+\pi)).$$
> The book's (B4.5.4)–(B4.5.6) use the first-order approximation $pb^* \approx (i-n)d$ (the book prints $\cong$). At Mexican nominal growth of 8–10% the approximation overstates $pb^*$ by a factor of about $1+n$, roughly 8–10%. RF uses the exact form.
>
> *Mexico.* The book sets aside valuation effects (its first paragraph). In Mexico they are first order. With share $\alpha$ of debt in foreign currency, peso depreciation $\varepsilon_t$ and foreign rate $i^f_t$:
> $$d_t = \frac{(1-\alpha)(1+i_t) + \alpha(1+i^f_t)(1+\varepsilon_t)}{1+n_t}\,d_{t-1} - pb_t + other_t .$$
> The debt aggregate is **SHRFSP**, and $pb$ is the RFSP primary balance. The gap between $\Delta$SHRFSP and RFSP is $sfa$ (valuation plus other) and must be reported, not absorbed. The timing convention (end-of-period stock) matches the DFD budget constraint. Nina to confirm the index alignment in the Julia code.


Other things being equal, primary deficits and interest payments on the outstanding stock of public debt increase the debt ratio, whereas primary surpluses and positive nominal GDP growth reduce it. When the nominal GDP growth rate is higher than the interest rate (or, equivalently, when the real GDP growth rate is higher than the real interest rate), a stable debt ratio is compatible with a permanent primary deficit. Conversely, when the interest rate is higher than the <!-- p. 165 --> growth rate, there must be a primary surplus to stabilize the ratio of debt to GDP, and the larger the (positive) difference between the interest rate and the growth rate, the larger the necessary primary surplus[^7].

The debt dynamics equations help explain why, in the second half of the 1980s, public debt became an issue for advanced countries: the combination of disinflation, lower growth, and higher real interest rates suddenly brought it to the fore after two decades during which governments could afford to overlook debts and deficits. In the same way, the no growth–no inflation environment of the mid-2010s resulted in public debt becoming a serious cause for concern in spite of the record low interest rates.

The approach presented here can be tweaked for assessing the debt situation of developing and emerging countries that are often obliged to borrow in foreign currency. This “original sin” of emerging-country financing adds a currency risk dimension, and, for this reason, it is generally assessed that the limits to their debt are significantly lower than for countries that borrow in their own currency[^8].

#### d) Shades of liabilities

Government accounts are generally much less comprehensive and sophisticated than the accounts of private companies. Assets are sparsely recorded and part of the liabilities is unrecorded, and there is generally no distinction between different types of debt securities.

Assets are hard to value because many are illiquid. The Japanese government, for example, can sell its shares in the *Japan Post*, but would have more difficulty selling the golden shrine in Kyoto. In Greece, privatization receipts have been miserable during the debt crisis of the 2010s despite suggestions that there would be wealthy buyers for the country’s many islands. Net debt ratios are therefore partial images of the government’s financial position, and they sometimes give an excessively favorable picture of its financial situation.

Financial liabilities are generally recorded accurately. In the EU, definitions have been standardized and the so-called *Maastricht definition of public debt* includes not only bonds and loans but also *contingent liabilities*, such as the guarantees provided to state-owned companies. Financial debt is generally reported at nominal value. Unlike private companies, governments do not mark their assets and liabilities to market, despite the fact that their debt is being traded and that its value depends on both interest rates and the perceived probability of insolvency.

In addition to financial debt, governments are liable for payments such as pensions to civil servants and other agents entitled to receiving transfers. They also act as insurers in case of major disasters or systemic bank failures. These commitments form what are called *off balance sheet liabilities*.

Off-balance sheet liabilities can be of four sorts, depending on whether they are (i) contractual or implicit and (ii) certain or contingent (table 4.1). For example, civil servants’ pensions are both certain and contractual. Bank

<!-- p. 166 -->

Table 4.1

Examples of off balance sheet liabilities

|          | Certain                     | Contingent                  |
|----------|-----------------------------|-----------------------------|
| Contractual | Civil servants’ PAYGO pensions | Credit guarantees           |
| Implicit   | Old-age dependency costs    | Bail-outs of banks          |
|            |                             | Natural disasters           |

Source: Adapted from Polackova (1999).

bail-outs are neither contractual nor certain, but they nevertheless result in huge public finance costs: Argentina in the 1980s, Korea in the late 1990s, and Ireland in the 2010s all suffered fiscal costs amounting to 30–60% of GDP (Laeven and Valencia, 2012).

Several governments produce comprehensive financial statements that provide the public with a more complete image of their financial situation. These comprise a description and valuation of government assets and liabilities and of some off balance sheet claims and liabilities. There are, however, several reasons why governments cannot fully emulate private financial reporting. First, they do not terminate their operations overnight. It is therefore unclear whether their balance sheet should be evaluated on the basis of market or historical prices. Second, many government assets are intangible and difficult to evaluate. Finally, and most importantly, governments can change the very laws under which they operate, blurring the notion of a government “liability.” For example, a reform of a pay-as-you-go pension system often amounts to a legal default on previous implicit liabilities. Nevertheless, these nonfinancial liabilities are crucial for evaluating the sustainability of public finances (see Section 4.2). In the United States, for example, accounting for pension provisions increases the gross liabilities of the federal government by nearly 50%.

### 4.1.2 Lessons from history

#### a) Public spending: A centennial perspective

As already indicated, the rise of government as an economic player was a major transformation that took place mainly in the second half of the twentieth century. Figure 4.6, which gives the evolution of US federal spending since the end of the nineteenth century, shows the temporary spikes associated with wartime defense spending and the two major steps that led to secular increases in nondefense spending: President Roosevelt’s New Deal in the late 1930s and President Johnson’s Great Society in the 1960s.

Similar trends can be observed in most other economies, albeit at different times and to different extents (see figures 4.7a and 4.7b). In Europe,

<!-- p. 167 -->

**Figure 4.6** US federal government receipts and spending, 1899–2016 (in percent of gross domestic product [GDP]). Authors’ calculations based on US Office of Management and Budget data.

government spending was already higher than in the United States at the beginning of the twentieth century—especially in Germany where Chancellor Bismarck had introduced social security to undercut the socialist movement. Its rise has not been uniform, as indicated by the example of Spain, where it only started after the transition to democracy in 1975. Though government spending as a proportion of GDP is markedly higher in Europe than elsewhere in the world, it has stabilized (or, in the case of Sweden, has decreased after the financial crisis of the early 1990s). In the emerging countries, government spending is lower, but a clear upward trend can be observed.

Most of the increase in public spending has resulted from the rise of social spending—pensions, healthcare, income support, and unemployment insurance. Transfers to individuals and the provision of public health services have increased massively. At the same time, most governments have withdrawn from sectors such as manufacturing, telecoms, postal services, transportation, and, except for the temporary nationalizations of ailing banks in the aftermath of the 2008 crisis, financial services. Overall, global privatization receipts from 1988 to 2014 amounted to nearly 3 trillion US dollars[^9]. State subsidies are also on the retreat, although they remain high in energy and agriculture.

A conclusion from these observations is that the conservative revolution launched in the early 1980s by Margaret Thatcher, the British Prime Minister, and US President Ronald Reagan did not succeed in reducing the size of the state, but contributed to redefining its scope: in the advanced and a large


<!-- p. 168 -->

Economic combination of state-owned enterprises with private ones suited scholars to shed light on the policy enhancement.

The authors argue that as academic institutions in Europe offer design and fiscal policies, term growth, the welfare institution shows help positive stake highlight (how the new be possible which judge constr obstacle on the provid the m text, w

This notion is important for the Global South and the European Union.

**Selected advanced European economies (Germany, Spain, Sweden)**

**Figure 4.7** General government spending, 1900–2011 (in percent of gross domestic product [GDP]). Authors' calculations based on IMF Public Finances in Modern History Dataset, see Mauro et al. (2013).

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart displays the general government spending as a percentage of GDP for Germany, Spain, and Sweden from 1900 to 2011. The x-axis represents the years from 1900 to 2010, while the y-axis shows the percentage of GDP ranging from 0 to 80. Each country is represented by a different line style: Germany with a solid line, Spain with a dashed line, and Sweden with another solid line. The graph illustrates trends in government spending over time for these three countries.

**Selected emerging countries (Chile, India, South Korea)**

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart also includes data for Chile, India, and South Korea from 1900 to 2011. Similar to the previous chart, the x-axis represents the years from 1900 to 2010, and the y-axis shows the percentage of GDP ranging from 0 to 80. Each country is represented by a different line style: Chile with a dashed line, India with a solid line, and South Korea with another solid line. The graph illustrates trends in government spending over time for these three emerging countries.

part of the emerging and developing countries, governments nowadays are enforcers of the economic rules of the game, providers of universal services, and social insurers, but they are much less manufacturers, bankers, and venture capitalists than they once were. However, this assessment does not apply <!-- p. 169 --> to China, Russia, or the Gulf countries where state-owned companies are powerful economic players. State capitalism remains a strong force in a world where economic power is shifting.

#### b) Fiscal policy in practice

There is no fiscal policy to speak of in the absence of a significant budget. But the opposite is not true: a country can record a high government budget and refrain from fiscal activism. Fiscal stabilization policy is a creation of the second half of the twentieth century. It was made official policy under US president John Kennedy in the early 1960s, and its influence gradually extended to Europe (though Germany only briefly endorsed it around 1970). By the late 1970s, it was already subject to controversies: it shared the discredit of policy activism that resulted from inflation and the failure to revive high growth after the oil shocks; it was accused of focusing too much on the demand side, whereas economic difficulties mainly arose from the supply side; its effectiveness was questioned because budgetary decisions must go through a lengthy parliamentary process; it was criticized for being much less nimble than monetary policy, which only requires a decision by the central bank to change the interest rate; and, from a political economy standpoint, it was accused of providing an easy excuse to governments that are politically unable to balance their budget.

Writing at the turn of the century, Stanford professor (and former economic advisor to President George W. Bush) John Taylor (2000) assessed that “empirical evidence suggests that monetary policy has become more responsive to the real economy, suggesting that fiscal policy could afford to become less responsive” (p. 35) and that it seems “best to let fiscal policy have its main countercyclical impact through the automatic stabilizers” (p. 34). Despite these criticisms, though, US presidents never relinquished fiscal policy entirely. It was mainly the political deadlock with Congress over federal spending and federal taxes that made fiscal policy increasingly difficult to rely on.

The fate of fiscal policy should have been more favorable in Europe because, under a fixed exchange rate (until 1998) and monetary union (from 1999 onward), monetary policy was not available at a national level as a stabilization instrument. This should have led governments to rely more on fiscal policy. But failed fiscal reflation attempts after the oil shocks, high levels of public debt and an adverse doctrinal climate made them increasingly cautious. When the monetary union was negotiated in the late 1980s, the focus of Germany was on preventing excessive deficits and a potential monetization of excessive public debts rather than on ensuring that there would be sufficient scope for fiscal stabilization. Its views prevailed, and significant constraints to fiscal activism were introduced in the EU treaty. Most small-country governments had little appetite for it at any rate because, in small open economies, the cost of a stimulus is borne by national taxpayers in the form of higher public debt, whereas <!-- p. 170 --> a large part of the benefits of higher demand accrue to the country's neighbors. In the end, Europe has remained more reluctant to embrace fiscal activism than the United States.

The one country where fiscal stimulus was lastingly endorsed has been Japan. In the 1990s, the Japanese government launched a series of stimulus packages to counter the effect of its financial crisis and lift off the economy. Partly because the private economy had been severely affected by the crisis and bank restructuring and recapitalization was a condition for the economy to gain momentum, and partly because action lacked decisiveness, the results were disappointing (see box 4.6).

However, fiscal policy was never removed from the policy toolkit. When the global crisis hit in 2008, the Group of Twenty[^10] was quick to endorse IMF proposals for a coordinated stimulus. In London in April 2009, the leaders of the G20 committed to "deliver the scale of sustained fiscal effort necessary to restore growth."[^11] Data indicate that they actually did deliver. In 2009, the breadth of the concerted stimulus was unprecedented: both emerging and advanced countries participated (see figure 4.8). Already in 2011, however, their stances started to diverge: fiscal policy remained

#### Box 4.6 Fiscal Policy in Japan in the 1990s

During the 1990s, the Japanese government repeatedly tried to raise the level of GDP growth and inflation through two significant fiscal stimulus programs: one from August 1992 to September 1995, and one from April 1998 to October 2000. In the first round, the fiscal impulse (measured as the change in the cyclically adjusted budget balance) averaged 1.5% of GDP per year, while the second impulse was smaller in magnitude and duration. Both phases of fiscal expansion focused on public investment, mainly infrastructure projects, while most of the remainder was allocated toward purchases of land and to financial and housing loans. The government included a large tax reduction in the first stimulus, with the expectation of compensating the reduction in income taxes with a later rise of value-added tax (VAT) rates. Over the 1990s, government debt doubled as a share of GDP, and the cyclically adjusted budget balance declined from 2% to -6% of potential GDP.

Although it had some positive short-term macroeconomic effects, the fiscal stimulus policy of the 1990s failed to bring back previous growth rates of the Japanese economy (Bayoumi, 2001). Part of the failure can be attributed to factors beyond the immediate control of the authorities (the Asian financial crisis and population aging). But the "lost decade" was also related to the failure of the government to swiftly clean up the banking sector. The resulting "zombie banks" failed to provide credit to stimulate private investment.

<!-- end Box 4.6 -->



<!-- p. 171 -->

**Figure 4.8** The concerted 2009 stimulus (change in the structural primary deficit in percent of potential gross domestic product [GDP]). Authors' calculations with IMF Fiscal Monitor data.

supportive in the United States and China, whereas Europe embarked on an early retrenchment.

#### c) Sovereign debt, solvency, and debt crises

Historically, sovereign debt has often been the consequence of wars. Figure 4.9, which depicts its evolution since 1800 in the United States and the United Kingdom (two countries for which continuous time series are available), illustrates the point vividly: in both countries, debt peaks correspond to wars (the Napoleonic wars, World Wars I and II for the UK; the Civil War, and World Wars I and II for the US).

Wars, however, are not the only reason why governments incur debt. Peacetime debt also increases, as a result of three types of developments:

- Protracted public deficits over and above the level corresponding to the stability of the debt ratio (see box 4.5). This has, for example, been the case of Italy (see figure 4.2), Belgium and France in the last decades of the twentieth century;
- Major recessions leading to a collapse of government revenues. In Spain, for example, government revenues dropped suddenly from 40.9% of GDP in 2007 to 34.8% in 2009[^12]. This quickly resulted in a significant increase in the debt ratio;


<!-- p. 172 -->

**Figure 4.9** Gross public debt-to- gross domestic product (GDP) ratios in the United States and the United Kingdom, 1800–2011 (in percent of GDP). IMF Historical Public Finances Dataset. See Mauro et al. (2013).

The materialization of contingent liabilities. As indicated in table 4.1, the government guarantees depositors (explicitly) and some other creditors of the banks (explicitly or implicitly). Losses in the banking sector translate into public debt if these guarantees are called. This comes on top that of the deep recessions generally triggered by banking crises. Ireland in the 2010s provides a clear case of the potential threat a large banking sector can represent for public finances: in 2007, its debt ratio was 24% of GDP; by 2012 it had reached 122% of GDP, a 98 percentage point increase in five years.

Figure 4.9 may suggest that public debt can reach multiples of GDP without much damage: although its sovereign debt ratio twice exceeded 250% of GDP, the United Kingdom always met its financial commitments, as did the United States, with debt peaking at 121% of GDP in 1946.[^14] Comprehensive research by Carmen Reinhart and Kenneth Rogoff (Reinhart and Rogoff, 2014) has shown, however, that these two cases are more the exception than the rule: *debt default*—that is, inability to meet one’s debt obligations on time, see box 4.7—has in fact been very common in history. Since 1800, there have been several waves of sovereign default associated with wars and economic crises. In the second half of the twentieth century advanced countries met their obligations, but emerging and developing countries experienced debt crises that ended in *debt restructuring* or at least *rescheduling* (see box 4.7). Overall, the proportion of countries in default each year has often been above one-third (figure 4.10).

<!-- p. 173 -->

#### Box 4.7 Debt Default, Restructuring, and Rescheduling

A borrower is in *default* vis-à-vis its private creditors as soon as it does not meet a financial commitment enshrined in its debt contracts. It can be in default because it has not repaid the principal on time or because it has not paid interest. A default is a *credit event* (an incident in the payment of debt obligations) that entails two consequences: first, the rating of all tradable debt securities issued by the same borrower is downgraded by rating agencies to D (for *defaulted*) and stop being accepted as collateral by central banks for the provision of liquidity to commercial banks (see Chapter 5); second, after decision by the International Swaps and Derivatives Association (ISDA), the default triggers derivative contracts such as *credit-default swaps* (CDSs), which provide insurance against default risk. For these reasons a default is inevitably a major financial shock.

These provisions apply to relationships to private creditors. Arrears in repayments to official creditors such as the IMF do not have immediate market implications. For example, Greece missed a payment to the IMF in July 2015, but Greek sovereign bonds were not downgraded to D.

Rather than to default, a sovereign borrower can renegotiate its debt with its creditors to obtain a rescheduling of the repayments, a reduction in the interest rate, or an outright reduction of the principal. Negotiations with official creditors take place within the *Paris club* (or, at euro area level, within the Eurogroup of finance ministers). As far as bank loans are concerned, they take place under the auspices of the Institute for International Finance (IIF), the major international banks’ association. Negotiations with bondholders are more difficult to organize because they are more dispersed. It is normally incumbent on the borrower to convene a negotiation with its creditors and to ensure that it involves a sufficient proportion of them. An agreement reached with a majority of the bondholders can, however, be challenged in courts by a minority of *holdout creditors* (see Section 4.3.2). For this reason, bond contracts increasingly include *collective action clauses* (CACs) specifying that agreements approved by a qualified majority of the bondholders apply to all.

From an economic viewpoint, an important criterion is whether the renegotiation results in a reduction of the net present value of future payments (of the principal and the interest). There can be such *debt relief* without a reduction of the principal if the interest rate is reduced or if the borrower is granted a grace period (Greece in the 2010s has benefitted from such a relief on official loans extended by the ESM, see box 4.8). A renegotiation resulting in a postponement of repayments without a change in the present value of future obligations is usually called a *debt rescheduling*. There is *debt restructuring* if the present value is reduced.

<!-- end Box 4.7 -->

<!-- p. 174 -->

**Figure 4.10** Percentage of countries in default on their external debt, 1800–2006. Because of the lack of systematic data on domestic default, only default on external debt is recorded. Reinhart and Rogoff, 2014.

These facts raise three questions: first, how did the United States, the United Kingdom, and a few other countries succeed in reducing their debt levels? Second, why and how are countries driven into insolvency? Third, what are the consequences of it?

As suggested by Equation (B4.5.5) of box 4.5, there are several ways to exit from excessively high debt. A country can:

a. Adjust by recording consistently high primary surpluses;

b. Inflate by devaluing nominal debt outstanding through inflation;

c. Grow out of debt by recording high real growth rates;

d. Repress debt holders by keeping the long-term interest rate artificially low;

e. And finally, default on its commitments.

The United States and the United Kingdom after World War II essentially relied on a combination of (b), (c), and (d). In a rather high nominal growth context, maintaining low bond rates through central bank policy helped keep the debt burden low.

Answering the second question is more demanding. It is relatively easy to determine when a household or a private firm is insolvent, but the same does not hold for a government. Unlike households, governments are assumed to have an infinite lifetime, so their debt never requires to be redeemed.[^15] To be more precise, expiring debt will be paid off through new borrowing because it


<!-- p. 175 -->

is reasonable to think that future generations will be willing, when their turn comes, to continue investing part of their wealth in government securities.

Is there no limit to the state’s borrowing capacity? Asking this question amounts to assessing the state’s *solvency*; that is, the availability of resources allowing it to meet its commitments. At first sight, the capacity of a state to ensure the service of its debt could appear unlimited since it has the power to raise taxes or, if the central bank is not independent, to monetize the deficit (which is another way of taxing since inflation reduces the real value of money balances and fixed-income securities such as standard bonds). However, there are political limits to the citizens’ willingness to pay. As illustrated by many historical episodes, from *Ancien Régime* crises to the Greek crisis of the 2010s, bankruptcy occurs when citizens no longer accept a further reduction of their income and wealth to the profit of the state’s creditors. In the words of former senior IMF official John Boorman:

Debt can almost always be serviced in some abstract sense, through additional taxation and through the diversion of yet more domestic production to exports to generate the revenue and foreign exchange needed to service the debt. But there is a political and social, and perhaps moral, threshold beyond which policies to force these results become unacceptable. (Boorman, 2002, p. 3)

Determining these political, social, and moral thresholds is a daring exercise. The Greek debt saga of the 2010s illustrated this uncertainty vividly: whether or not Greece was able to repay its debt was a matter of constant controversies within and between international institutions (see box 4.8). The political dimension of the issue became even more prominent after the leftist coalition led by Aléxis Tsipras won the general election in January 2015, as this change of majority signaled a seriously diminished tolerance for fiscal adjustment on the part of the Greek citizens.

*Solvency* characterizes the situation where, at a given moment in time, the government is able to meet all its financial obligations by raising taxes, selling assets, and issuing new debt. If resources exist but cannot be mobilized immediately (for example, in the case of state-owned companies that cannot be sold immediately due to lack of purchasers), or if they are available but can dry up at short notice (in the case of short-term credit extended by foreign banks), there is a risk of a *liquidity crisis* whereby the government is unable to meet the exact schedule of its obligations. Finally, public finance is said to be *unsustainable* if, on the basis of the current economic policy and of available forecasts, the expected development of the public debt leads to a situation of insolvency. Fiscal policy can therefore be unsustainable without solvency problems arising immediately. Nonetheless, this policy will have to be modified in the future.

Public finance sustainability is especially important in a monetary union where the central bank is independent and does not have the mandate to serve

<!-- p. 176 -->

#### Box 4.8 The Greek Debt Saga

In the 2000s, Greece recorded very large and in part hidden deficits, reaching a 15.5% of GDP deficit and a 127% of GDP debt ratio in 2009. In spite of an exceptionally large fiscal adjustment, estimated by the IMF at 19% of potential GDP between 2009 and 2013 (IMF, 2017); a significant debt reduction negotiated with private creditors in 2012; and favorable borrowing conditions granted by the euro area partners, remaining deficits and the nominal GDP contraction resulted in the public debt reaching 177% of GDP at end-2014. The IMF subsequently assessed that Greek debt was not sustainable unless a primary surplus in excess of 3.5% could be sustained, which was considered politically unrealistic. However, the euro area creditors (partners countries through the European Stability Mechanism (ESM), the financing vehicle set up in 2012 to provide conditional financial assistance to countries in crisis) were willing to provide favorable financing conditions but unwilling to write off nominal debt. Germany, especially, insisted that debt forgiveness was illegal because Article 125 of the European Treaty (known as the *no bail-out clause*) states that “The Community shall not be liable for or assume the commitments of central governments … of any Member State.” In net present value terms, Greece has benefited from a substantial reduction of its official debt burden, but—at the time of writing at least—in nominal terms there has been no debt relief.

<!-- end Box 4.8 -->

as a lender of last resort for sovereigns. This issue has been a matter of lengthy and controversial discussion in the euro area. We return to it in Section 4.3.

Another major difference between a state and a private entity has to do with the consequences of insolvency. When a company goes bankrupt, a competitor buys it up or it is liquidated, in which case its assets are seized by the creditors. A household may similarly lose its assets (e.g., its house). But there is no collateral for sovereign debt. If a state defaults on its commitments, neither domestic nor foreign creditors can seize its assets (unless the latter invade the country).[^16] An indebted state’s attitude toward its creditors therefore depends on its willingness to pay as well as on its ability to pay. Default can be the outcome of a rational decision not to repay the creditors (in which case it is called strategic default),

This brings us to the third question: What are the benefits and costs of a strategic default? The benefits result from writing off the debt and the corresponding interest burden, while the costs are mainly reputational: the state may be cut off from financial markets or at least pay a higher risk premium on future borrowings because markets will price the risk of another default (see box 4.9). An overindebted country faces a choice: either to strive to meet its obligation and gradually reduce its debt ratio through fiscal adjustment, or to negotiate a debt relief with its creditors. In the first case it preserves its reputation, but, before it succeeds in putting its debt ratio on a convincingly


<!-- p. 177 -->

#### Box 4.9 The Risk Premium and the Valuation of Public Debt

There are two main reasons why the market valuation of sovereign debt varies over time and across issuers.

First, the value of a fixed-rate government bond on the secondary market depends on the relative level of its interest rate and the current interest rate for assets of the same maturity and risk. Since interest rates vary continuously, bonds carrying different interest rates coexist. Arbitrage by market participants leads the expected return on these bonds to equalize through variation in their value. Assume for example that the government issues a bond carrying a 1% interest rate. Nobody would buy if another bond from the same government carrying 2% can be bought unless the value of the second increases up to the point where both provide the same return. This mechanism is continuously at work on bond markets.

Second, bonds of the same maturity are not equally risky. For riskier ones to be bought, they must carry a higher interest rate. Suppose, for example, that a government issues a $100 one-year bill and that the *risk-free* interest rate is $i$. If the probability that the government will entirely fail to honor its obligation is $\pi$, the expected value of the reimbursement of the principal of nominal value 100, E(P), is[^b4-9a]:

$$E(P) = (1 - \pi) \times 100 + \pi \times 0 \quad \text{(B.4.9.1)}$$

To take this risk, lenders will require to be rewarded with an additional return called *risk premium* $\rho$ such that:

$$(1 - \pi i)(1 + i)(1 + \rho) = (1 + i) \quad \text{(B.4.9.2)}$$

The risk premium corresponding to the insolvency probability $\pi$ is therefore:

$$\rho = \frac{\pi}{1 - \pi} \quad \text{(B.4.9.3)}$$

It is an increasing function of the probability of default $\pi$. As a judgment on debt sustainability fundamentally relies on one’s assessment of the willingness of domestic taxpayers to meet their sovereign’s obligations, the probability of default envisaged by financial markets is quite volatile. This may generate self-fulfilling crises: if markets suddenly revise the probability of default upward, this increases the risk premium, hence the interest rate on new borrowing, making the debt unsustainable.

[^b4-9a]: For simplicity, we have assumed that, in case of default, the lender does not recover anything. The computation can easily take into account the probability of partial reimbursement.

<!-- end Box 4.9 -->

declining path, it is likely to be facing high borrowing costs; in the second case, its solvency will be improved, but it may suffer lasting reputational damages.

Careful analysis of twentieth-century debt restructuring episodes yields two important lessons. First, reputational damages are limited: markets tend <!-- p. 178 --> to forgive debt restructurings. More precisely, they do not punish renegotiation or restructuring per se: after an agreement has been reached with the creditors, governments regain market access, and future bonds spreads are correlated to the size of the restructuring (Cruces and Trebesch, 2013). Second, significant debt reliefs are positive for growth, especially when accompanied by reductions in the face value of the debt instead of a mere reduction of the present value (Reinhart and Trebesch, 2016). The upshot is that when a country struggles with unsustainable debt, a debt restructuring may be desirable. The quality of the negotiation process matters, however: markets punish unilateral defaults. Ultimately, the decision will depend on the level of the primary deficit since a defaulting country will be unable to finance its primary deficit in the short term after the credit event. It will also depend on the damage created by a default on the domestic financial sector (since domestic banks may hold large amounts of domestic sovereign debts) and on the dissemination of the debt along domestic households.

Since governments suspected of not being able or willing to repay their debt carry a higher interest rate, there is a risk of vicious circle: as detailed in box 4.5, the higher the interest rate, the higher the required primary surplus for debt stabilization, hence the lower the willingness of domestic taxpayers to continue the fiscal adjustment. Such vicious circles were at the core of the European debt crises of 2010–2012 (figure 4.11): interest-rate spreads (or

**Figure 4.11** Sovereign spreads vis-à-vis Germany, selected euro area countries, 1997–2017 (differences in 10-year sovereign interest rates in percentage points). OECD.

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart displays the evolution of sovereign bond spreads for France, Ireland, Italy, and Spain relative to Germany from 1997 to 2017. The vertical axis represents the spread in percentage points, ranging from -1 to 9. The horizontal axis shows dates from January 1999 to February 2017. Four lines represent different countries: France (dashed), Ireland (solid thin), Italy (solid thick), and Spain (dash-dot). Spreads remain low until around 2008, then rise sharply for all countries during the European debt crisis, peaking between 2011 and 2012 before declining again.

<!-- p. 179 -->

differences) vis-à-vis Germany increased from being negligible to levels that exceeded eight percentage points for Ireland and five for Spain. None of these countries defaulted, but Ireland and Portugal (as well as Spain for the financing of bank rescue) were forced to apply for support from the IMF and the ESM. What these developments suggest is that the interplay between market expectation of default and actual borrowing conditions is at the core of sovereign debt crises. We return to the issue in the next section to understand how solvency can be more precisely defined.

## 4.2 Theories

### 4.2.1 Demand-side effects

#### a) The basic toolkit

Since its publication in 1936, John Maynard Keynes’s *General Theory of Employment, Interest and Money* has provided an essential conceptual framework for analyzing the influence of fiscal policy on aggregate demand. Here, we first briefly sketch the Keynesian theory and the main criticisms it has been subject to.

As indicated in Chapter 1, the standard Keynesian model assumes price stickiness in the short term. The supply of goods and services is supposed to be elastic, and the level of aggregate demand determines output. When demand is insufficient, this results in the underemployment of labor and capital. A fundamental role of macroeconomic policy—be it fiscal or monetary—is to ensure that aggregate demand is such that the economy remains at or close to a level corresponding to equilibrium employment. In response to a negative demand shock, this can be done by increasing public spending or by cutting taxes.

This framework rests on two key assumptions: that because of price stickiness, the macroeconomic balance is not reached through changes in prices and that the response of private spending does not offset the rise in public spending. In the elementary Keynesian model, nominal rigidity and the income-demand relationship are simply postulated. An exogenous increase in aggregate demand (a demand shock) results in an increase in the level of output. The ratio between output variation and the initial exogenous variation of aggregate demand is called the *Keynesian multiplier* (box 4.10).

The Keynesian framework can be represented within the aggregate supply, aggregate demand (AS–AD) model introduced in Chapter 1. The price stickiness assumption implies that the aggregate supply (AS) curve is upward-sloping but not vertical in the short run. In the elementary model, the slope of AS is low, so that production can increase without having a major impact on prices. The aggregate demand curve is downward-sloping due to the negative impact of inflation on demand for goods and services, either through a wealth effect or because of the impact of a rise of the interest rate engineered by the

The Keynesian multiplier

...

<!-- p. 180 -->

#### Box 4.10 A Primer on the Keynesian Multiplier

Suppose that household consumption $C$ is a linear function of current income $Y$:

$$ C = aY + b \quad \text{with } a, b > 0 \tag{B4.10.1} $$

The parameter $a$ is the *marginal propensity to consume* (meaning that out of one additional euro of disposable income, the representative household spends $a$ and saves $1-a$). Let us assume, for example, that households consume 80% of any additional unit of income, so that $a=0.8$, and that households own companies, so that any profit is treated by them as income.

Suppose that supply is perfectly elastic, so that output adjusts to the level of aggregate demand at constant prices. The closed economy product market equilibrium is given by:

$$ Y = C + \overline{I} + \overline{G} \tag{B4.10.2} $$

where $\overline{I}$ is aggregate investment and $\overline{G}$ is government demand. Both are assumed to be exogenous.

Suppose the government increases by one unit public spending while keeping taxes constant. This will initially lift output, and thus income distributed to households, by one euro. Out of this additional unit, 80 cents will be consumed and will lift output—thus disposable income—further. At the end of the process, the total increase in output is:

$$ \begin{aligned} 1 + a + a^2 + a^3 + \dots &= 1 + 0.8 + 0.8 \times 0.8 + 0.8^3 + \dots \\ &= 1 / (1 - a) = 1 / (1 - 0.8) = 5. \end{aligned} $$

The same result can be obtained by solving the two-equation system directly, leading to:

$$ \Delta Y = \frac{\Delta \overline{G}}{1 - a} \tag{B4.10.3} $$

In this example, the multiplier is excessively large, and fiscal policy is therefore implausibly powerful. There are, however, many factors that may lower the multiplier:

First, not all the additional income accrues to consumers because a fraction of it is taxed away by the government. So Equation (B4.10.1) needs to be rewritten $C = a(1-t)Y + b$, where $t$ is the tax rate. The multiplier becomes $1 / [1 - a(1-t)]$.

Second, in an open economy, an additional euro of disposable income leads households to consume more of both domestic and imported products and firms to import more intermediate goods. Assuming that the marginal propensity to import is $m$ (meaning that an additional unit of income will lead to $m$ units of imports), the Keynesian multiplier becomes $1 / [1 - a(1-t) + m]$.

<!-- p. 181 -->

**Third**, the assumption of complete price rigidity is extreme. If prices adjust upward, part of the increase in demand does not result in an increase of the volume of products consumed but in an increase in their price. This especially applies over time, as prices adjust gradually.

**Fourth**, the central bank may respond to an increased demand for products by an increase in the interest rate. In this case investment (from firms) declines because firms compare the yield of investment projects with the financing cost or with the return to financial investments. A *crowding-out effect* appears: part of the increase in public demand results in lower private investment (due to the interest rate increase, private investment is crowded out by public demand). Conversely, an interest rate reduction by the central bank in response to a public spending cut partially offsets its negative impact—unless there is no room for cutting the policy rate because it has already reached the “zero lower bound” (see Chapter 5).

All these factors weaken the impact of fiscal expansion on aggregate demand and income.

<!-- end Box 4.10 -->

**Figure 4.12** Effect of a Keynesian fiscal expansion in an AS-AD framework.

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart shows an upward-sloping aggregate supply (AS) curve and two downward-sloping aggregate demand curves, AD and AD′. Price is on the vertical axis and production on the horizontal axis. AD meets AS at $E_1$; the rightward shift to AD′ gives a new intersection $E_2$, with higher output and a somewhat higher price level.

central bank. A fiscal expansion (either a rise in public spending or an exogenous cut in taxes) results in the demand curve moving to the right: production increases. If the slope of the supply curve is low, the adjustment takes place through a variation in the level of output (movement of $E_1$ to $E_2$ in figure 4.12).

Here, we have simply postulated the AD curve that summarizes the demand side of the economy. It can be derived from the IS-LM model introduced by Hicks (1937) and Hansen (1953) to formalize Keynes’s *General Theory*. This model, which has been widely used ever since, consists of two curves that relate output and the interest rate: the IS curve describes the product market

<!-- p. 182 -->

**Figure 4.13** Effect of a Keynesian fiscal expansion in an IS-LM framework.

equilibrium and the LM curve the money market equilibrium, both *for a given product price* (figure 4.13):

- The IS curve gives the combination of output and interest rate that results in a product market equilibrium. It is downward-sloping since a higher interest rate results in a lower demand for products;
- For a given money supply, the LM curve gives the combination of output and interest rate that results in money market equilibrium. With a fixed money supply, the positive relationship between output and the interest rate relies on the demand for money, which is supposed to be an increasing function of output (as output grows, more money is needed for transactions) and a decreasing function of the interest rate (as the interest rate grows, private agents prefer to hold interest-bearing assets rather than cash).

In an IS-LM model, a fiscal expansion is represented by a shift of the IS curve to the right (because of the additional demand for goods, output is larger at any given interest rate). This fiscal expansion entails an increase in the interest rate, which reduces the interest-sensitive components of private demand: there is partial *crowding-out* of private demand by public demand.

As we will see in Chapter 5, modern analysis of interest rate formation no longer starts from the assumption that the central bank targets money supply. Rather, the interest rate is supposed to be set by it in response to economic developments in order to ensure price stability (or more generally macroeconomic stability) in the medium run. In other words, most central banks nowadays do not follow a money supply rule, but rather an interest-rate rule. This has led to several reformulations of the IS-LM framework that result in <!-- p. 183 --> substituting for the LM curve an interest-rate reaction function (Romer, 2000; Bofinger, Mayer, and Wollmerhäuser, 2002). However, such reformulations generally result in representations that make the interest rate dependent on the level of output, as in the LM curve.

Because monetary and fiscal policies are to a certain extent substitutable, the Keynesian approach naturally leads to thinking in terms of *policy mix* (i.e., in terms of the combination of monetary and fiscal policies). Fiscal policy is indeed more effective when supported by monetary policy. At the limit, a perfectly accommodative monetary policy that keeps the interest rate constant in response to a fiscal expansion results in a maximum multiplier effect[^17]. This may lead governments to put pressure on the central bank so that it contributes to maximizing fiscal expansion and possibly to submitting monetary policy to *fiscal dominance* (a concept we further explain in Chapter 5). When the central bank is independent, however, it may choose not to accommodate the effects of fiscal policy if it perceives it as potentially inflationary. In figure 4.13, the LM curve does not shift to the right, so the interest rate increases.

This does not imply that an independent central bank always reacts to a fiscal expansion. For example, monetary policy can have hit the “zero lower bound” (see Chapter 5) where the policy-determined interest rate remains at or near zero, whereas the economic situation would justify setting it at a significantly negative level. In such a situation, monetary policy does not respond to a fiscal expansion and is therefore fully accommodative without being subject to fiscal dominance. A context of this sort magnifies the impact of fiscal policy because, instead of resulting in a policy-induced increase in the real interest rate, a fiscal expansion results in its lowering (since the nominal interest rate stays constant while price inflation accelerates)[^18]. Another case where the interest rate may not react to a fiscal expansion can be found within a monetary union, when the country carrying out the fiscal expansion is small enough to have negligible impact on the aggregate inflation rate (see Chapter 7).

#### b) Intertemporal optimization

The preceding presentation was based on an ad hoc assumption as regards household behavior: they are supposed to set their spending plans on the basis on their current income. This implicitly assumes that households cannot smooth spending over time by resorting to the credit market: when facing a temporary drop in income, they do not borrow from banks to maintain their consumption.

Suppose instead that households have unlimited access to credit. They can maximize their intertemporal utility, which depends both on their present and their future consumption, subject to their intertemporal budget constraint. In this polar case, current consumption does not depend on current income but on the present value of future earnings. If the discount rate equals the interest rate, a temporary income shock does not affect household behavior at all. There is no need for stabilization policy.



<!-- p. 184 -->

Furthermore, fiscal stabilization would be ineffectual under such conditions, as supporting current income through temporarily lower taxes (offset by higher taxes later) has no effect on consumption. The reason is that the intertemporal budget constraint of the state requires it to raise taxes in the future to repay public debt, a temporary tax cut raises the households' current disposable income, but not their intertemporal disposable income; consumption therefore does not change (box 4.11). Similarly, in the case of an increase in public expenditure, households lower their consumption because expected future taxes reduce their intertemporal income. Assuming again that their discount rate is equal to the interest rate, the decline in private consumption exactly offsets the increase in public spending, so that aggregate demand does not change. There is total crowding-out of private spending by public spending, and output is not affected.

The neutrality of fiscal policy is called *Ricardian equivalence* (see box 4.11). The intuition for it can be found in earlier reference to David Ricardo's classical discussion of the alternative ways to pay for a war (Ricardo, 1820). It was first formalized by Robert King Louis XVI of France (Mirabeau, 1787).

#### Box 4.11 Ricardian Equivalence

Consider an infinitely lived individual who can freely lend and borrow at interest rate $r$. At each period $t$, she receives an income $Y_t$, consumes $C_t$ and invests (or borrows) $Y_t - C_t$ at rate $r$. The intertemporal budget constraint, which states that the present value of all earnings equals the present values of all expenditures, can be written as:

$$ \sum_{i=0}^{\infty} \frac{Y_{t+i}}{(1+r)^i} = \sum_{i=0}^{\infty} \frac{C_{t+i}}{(1+r)^i} \tag{B4.11.1} $$

Subject to this constraint, the individual maximizes her intertemporal utility $U_t$ which can be written as the present value of future utility at each period (we assume it separable):

$$ U(t) = \sum_{i=0}^{\infty} \frac{u(C_{t+i})}{(1+\rho)^i} \tag{B4.11.2} $$

Where $\rho$ is the discount rate that measures the individual's preference for the present, and $u$ is a concave function. The first-order condition of this maximization program leads to the following behavior:

$$ \frac{u'(C_{t+i})}{u'(C_{t+i-1})} = \left( \frac{1+\rho}{1+r} \right) \tag{B4.11.3} $$

<!-- p. 185 -->

Knowing that $u^{\prime}(\cdot)$ is a decreasing function, we can derive the optimal consumption path of the consumer. When the interest rate coincides with the discount rate $(r=\rho)$, consumption is kept constant over time; when $r>\rho$, consumption grows over time; when $r<\rho$, it decreases. In all cases, consumption at any point of time depends not on current income, but on intertemporal income as defined in Equation (B4.11.1). A temporary fluctuation of income (a recession, followed by a boom) is smoothed out and does not affect consumption. However, a *permanent* fall of income over the life cycle (for example, due to a productivity shock or a pension reform) reduces consumption even if current income remains unchanged.

Let us now introduce a government that spends $G_{t}$ and receives lump sum taxes $T_{t}$. We assume that the level of public spending does not enter the individual's utility function (the government does not spend on the provision of public services). First, assume that the government maintains fiscal balance $G_{t}=T_{t}$ at all times. The intertemporal budget constraint of the individual becomes:

$$
\sum_{i=0}^{\infty}\frac{Y_{t+i}-T_{t+i}}{(1+r)^{i}}=\sum_{i=0}^{\infty}\frac{C_{t+i}}{(1+r)^{i}} \tag{B4.11.4}
$$

The first-order condition of the utility maximization program is unchanged: public spending financed by lump-sum taxation does not change the shape of the optimal consumption path of the individual (but the level of consumption at each period falls).

Let us now suppose that the government, while preserving its spending program, decides to reduce taxes at time $t=0$ by an amount $B$, and floats securities for this amount $B$ with a maturity of $M$ years at interest rate $r$. It is further assumed that interest payments on debt $B$, as well as the repayment of capital, will be financed by lump-sum taxation. The individual's utility maximization program is unchanged: during the initial period, a part $B$ of her income is used to acquire public debt securities, but taxes also fall by $B$; during the following periods, until $t=M$, additional income $rB$ is received on securities held, but additional taxes $rB$ are paid as a result of the need to finance the government debt service; finally, at period $t=M$, the principal $B$ is repaid to the households, but taxes rise by the same amount. The level of consumption remains unchanged at each period. The variable that changes is savings, the difference between disposable income and consumption.

This result is the Ricardian equivalence theorem. It expresses the idea that debt is deferred taxation. It also suggests that the central government's concern should be to determine the level and nature of public expenditures more so than its financing method (through debt or through taxation).

<!-- end Box 4.11 -->

<!-- p. 186 -->

The assumptions behind the Ricardian equivalence theorem may seem unrealistic: rational expectations, infinitely lived consumers (or, equivalently, full solidarity across generations), the unproductive character of public expenditure (or their lack of impact on consumers’ utility or on business productivity), and the absence of credit constraints (households enjoy unlimited access to credit regardless of their debt ratios).

Several of these assumptions are indeed questionable: few households master the complex arithmetic of intertemporal public finances; many have short horizons; a large part of them is constrained by credit; and some public expenditures, notably for research or education, have positive effects on future incomes (see Chapter 9). The joint validity of these assumptions is actually contradicted by empirical evidence (Mankiw, 2000).

However, it is true that as an economy grows, private wealth increases and credit markets develop, and increasingly fewer households are subject to the liquidity constraint postulated by the Keynesian model. In the United States in particular, household can post increases in the value of their property as collateral for credit, which makes them able to turn a capital gain into disposable income. This mechanism, known as “mortgage equity withdrawal,” funded 3% of household consumption between 2001 and 2005 (Greenspan and Kennedy, 2007). Even with not fully rational expectations, imperfect access to credit, and finite horizons, part of the households’ consumption plans is based on intertemporal calculation, and this affects the Keynesian multiplier. In fact, most empirical tests reject full Ricardian equivalence but confirm partial Ricardian effects that reduce the effectiveness of fiscal policy[^19].

These observations have led to the development of micro-founded models that combine two types of households: unconstrained optimizers and liquidity-constrained *hand-to-mouth consumers*. Macroeconomic consumption results from the aggregation of these two types of behavior (Campbell and Mankiw, 1989; Gali, López-Salido, and Vallés, 2007), possibly in varying proportions. Combined with price rigidity assumptions, such a representation leads to Keynesian properties (hence they are called *new-Keynesian models*). Another technique is to model a household as belonging to overlapping generations, each of which has a finite horizon. If each generation cares about its offspring, the model exhibits Ricardian properties, but if each generation is only interested in its own fate, fiscal policy gains effectiveness as an instrument to smooth out fluctuations in activity (Blanchard, 1985).

Even when the Ricardian equivalence applies, there is a rationale for the government to allow the budget to be in deficit in a recession or as a consequence of outside events such as wars or natural disasters. The reason is that balancing the budget in any circumstance would entail fluctuation in the tax rate that would adversely affect the supply side of the economy. This theory of tax smoothing results in a policy recommendation that does not differ markedly from the Keynesian prescription. In both settings, th


<!-- p. 187 -->

government should refrain from increasing taxes in a recession or from cutting them in a boom. It should let automatic stabilizers play in full. Where the two approaches differ is as regards the use of discretionary fiscal policy. Stimulating the economy in a recession, over and above the spontaneous impact of automatic stabilizers, is potentially useful in a Keynesian setting but useless in a Ricardian setting.

#### c) Fiscal controversies

Other arguments have been put forward against the Keynesian approach. The three main ones are:

- **Financial crowding-out**: After a fiscal expansion, the deterioration of the public balance and the corresponding savings shortfall may cause a rise in the long-term interest rate that depresses private demand. This financial crowding-out can arise independently of the central bank's reaction to an increase in public spending, as a consequence of the change in the savings–investment balance. In the AS–AD model, this leads the demand curve not to shift in response to a fiscal shock: only its composition is modified by the substitution of private demand by public demand;
- **Supply rigidity**: The relative price adjustment can be sufficiently quick for the goods–market equilibrium to be supply-determined. If the demand curve moves to the right but the supply curve is very steep, private demand is penalized *ex post* by the rise in prices;
- **Supply-side effects**: In the long run, a permanent increase in public spending must be financed by an equivalent amount of taxes. As such taxes may negatively affect supply (for example, through reducing labor supply in response to taxes on labor income, see Chapter 8), more public spending may pave the way for permanently higher taxes and thereby lower potential output. This may reduce the households’ intertemporal income and lead them to cut consumption.

The first argument is in contradiction with the Ricardian critique: it posits that a rise in public spending results in a shortfall of savings and thereby a rise in interest rates, whereas Ricardian equivalence posits that the rise in private savings will offset public dissaving (because households adapt consumption in the expectation of future taxes). Both views are more likely to apply in an economy where public debt is considered not sustainable, hence the probability of defaulting on the debt becomes non-negligible (see Section 4.2.2).

The second argument raises an empirical question: What is the slope of the supply curve? Available estimates suggest that it is upward-sloping but not vertical in the short run, which leaves room for fiscal policy effectiveness. All depends, in fact, on the time horizon: within a period of a few months or <!-- p. 188 --> quarters, prices are sticky; within a few years, they adjust. Fiscal policy effectiveness (like that of monetary policy, as discussed in Chapter 5) is therefore limited in time.

The third argument about possible negative supply effects cannot be decided upon *in abstracto*. Its validity depends on the nature of public spending (especially on the division between current and capital expenditure) and on the nature of future taxes, which can be more or less distorting (see Chapter 8). The economic literature has built on these distinctions to highlight the importance of the mix of taxation and spending measures that a fiscal expansion or a fiscal retrenchment relies on (what economists call *composition effects*; see Alesina and Ardagna, 2010). Indeed, the supply-side argument for expenditure-based adjustments is that because they signal lower taxes in the future, they may elicit a positive private-sector response that reduces the adverse effect of the adjustment. It should be noted that the demand-side argument would lead to the opposite conclusion: in a simple Keynesian setting, an expenditure-based adjustment has more direct and immediate effects on demand than a tax-based one whose effects can be smoothed by a reduction in private saving[^20].

#### d) Empirical methodologies

Given ambiguities and theoretical controversies, the effectiveness of fiscal policy as a stabilization instrument is ultimately an empirical issue. To assess its effects, different types of approaches have been used in the literature. The three main ones are simulations with macroeconomic models, empirical estimates with reduced forms (mainly structural vector autoregressive [VAR] models), and systematic analyses of fiscal action episodes.

Simulations have the advantage of taking into account, within the same model, of a series of transmission channels such as household behavior, firm behavior, and cross-country interactions. They also make it possible to specify the policy impulse precisely (for example, whether it consists of a cut in public expenditure, and of which expenditure, or in an increase in taxes, and which taxes), whether the impulse is permanent or temporary, and the context in which it operates (depending on the response of monetary policy and the cross-country context). Finally, beyond the multiplier, they provide estimates of the impact of fiscal policy on a series of variables such as inflation, the fiscal and external balances, or employment. They have, however, the disadvantage of being model-dependent: they rely on a representation that can be disputed.

Empirical estimates based on reduced forms have the advantage of relying on few *a priori* assumptions and the drawback of being comparatively rough. Blanchard and Perotti (2002) first used structural VAR models to assess fiscal policy in the United States (box 4.12). Similar approaches have been replicated for other countries. The limitation of this method is that it necessarily relies on a limited set of variables (three for Blanchard and Perotti: taxes, public spending, and GDP).


<!-- p. 189 -->

#### Box 4.12 Vector Autoregressive Empirical Evaluations of Fiscal Policy

Blanchard and Perotti (2002) assess the effects of fiscal policy on the basis of a minimum set of a priori restrictions. They start from a simple VAR model:

$$Y_t = A(L) Y_{t-1} + U_t \tag{B4.12.1}$$

where $Y_t = [T_t, G_t, X_t]'$ is a vector whose three dimensions are taxes ($T$), public expenditures ($G$), and GDP ($X$), all expressed in real per capita terms and in log. $A(L)$ is a polynomial lag operator and $U_t = [t_t, g_t, x_t]'$ is the vector of residuals.

Residuals in $U_t$ are not a priori independent. To account for their correlation and isolate an uncorrelated error vector, one writes:

$$
\begin{aligned}
t_t &= a_1 x_t + a_2 e_t^g + e_t^t \\
g_t &= b_1 x_t + b_2 e_t^t + e_t^g \\
x_t &= c_1 t_t + c_2 g_t + e_t^x
\end{aligned} \tag{B4.12.2}
$$

where, for example, $a_1$ describes the instantaneous impact of GDP on tax revenues and $a_2$ the instantaneous impact of spending shocks $e_t^g$ on these revenues. This simple structure makes it possible to isolate shocks $e_t^t, e_t^g$ and $e_t^x$ that can be assumed uncorrelated with each other.

To estimate the parameters of the system, Blanchard and Perotti impose a number of restrictions. For example, they assume that fiscal policy reacts only with a lag to changes in GDP (which is reasonable in view of the delays involved in parliamentary decision and the implementation of legislation). This implies that $b_1 = 0$ and that $a_1$ represents the mechanical effects of changes in GDP on tax revenue, which can be evaluated on the basis of detailed tax elasticities.

These various restrictions result, without imposing significant theoretical priors, in a model whose remaining parameters can be estimated (this is what is called *model identification*). There is no restriction on the sign or the value of the expenditure multiplier.

Once estimated with quarterly data over the period 1960–1997, the model is used to study the response of GDP, public spending, and taxes to an exogenous shock, such as a shock on public spending. In the first period, it reflects the economic impact of the public spending shock on growth. From the second period onward, it also reflects the typical reactions of fiscal policy to the economy.

Blanchard and Perotti find that, in the short term, both public spending and tax multipliers are close to unity: an additional dollar of public spending raises GDP by about a dollar; an additional dollar of taxes reduces it by about a dollar.

<!-- end Box 4.12 -->

<!-- p. 190 -->

The third approach is based on the analysis of significant and lasting fiscal episodes. Building on the case study of large-scale fiscal consolidation episodes (such as those of Denmark and Ireland in the 1980s), Alesina and Ardagna (2010) run a cross-country study in which they retain all years during which the structural primary balance varied by a minimum of $\pm 1.5$ percentage point of GDP. The underlying idea is that, unlike what linear models implicitly assume, the multiplier is not constant across fiscal policy initiatives because a major program of debt deleveraging or a sustained expenditure contraction effort will change the expectations and behaviors of private agents.

The narrative approach initiated by Romer and Romer (2010) provides the basis for another attempt to disentangle the analysis of fiscal policy from the hypotheses built into structural models without falling into the extreme simplifications of the VAR approach. As explained in box 4.2, action-based fiscal data have the advantage of being independent from unreliable estimates of the structural balance. They can furthermore be used in model-free assessments of the impact of fiscal policy. In the 2010s, the narrative approach has increasingly been used (IMF, 2010; Guajardo, Leigh, and Pescatori, 2014; Alesina et al., 2017).

A variant of the same approach relies on episodes of war, which have the (econometric) advantage of being exogenous and unrelated to prevailing macroeconomic conditions. Analysis of such true fiscal shocks can yield unbiased estimates of the multiplier (though monetary policy may well respond to war-induced changes in government spending).[^21] In the same vein, Nakamura and Steinsson (2014) use the differentiated regional impacts of military buildups to evaluate state-level multipliers.

#### e) The multiplier in practice

Batini et al. (2014) and Mineshima et al. (2014) provide a survey of recent results. The main lessons from research are the following:

1. **The average expenditure multiplier is close to one in large, moderately open economies.** As far as structural models are concerned, Coenen et al. (2012) find that, with similar initial conditions and in response to identical shocks, multipliers are remarkably close: for the United States, they range between 0.9 and 1.3, for example, in the case of a temporary public investment increase with endogenous monetary policy response; they are also around 1 in the case of a coordinated stimulus in Europe, under the same conditions. The VAR approach of Blanchard and Perotti (2002) and the narrative approach of the IMF (2010) yield similar results. This is also the conclusion from the survey of several narrative analyses by Batini et al. (2014).
2. **The characteristics of the economy affect the fiscal multiplier.** It depends on trade openness (negatively) and therefore on the size of the economy (positively), labor market rigidity (positively),


<!-- p. 191 -->

3. The degree of monetary support strongly affects the fiscal multiplier. Coenen et al. (2012) provide a thorough comparative analysis of seven models in use in central banks or international organizations. They find that, for a two-year temporary fiscal expansion, the multiplier is significantly larger when monetary policy is fully accommodative (no change in nominal policy rate) than when it responds endogenously to fiscal action. In particular, fiscal policy is significantly more effective when monetary policy is constrained by the zero lower bound—a result confirmed by a variety of studies based on different methodologies[^22].

4. The impact of fiscal policy varies over time depending on the overall economic conditions. Consistent with the Keynesian approach, Auerbach and Gorodnichenko (2012) find evidence that the US expenditure multiplier varies between zero in boom years and 1.5 in recession years. Consequently, the output cost of fiscal consolidations is higher in bad times and lower in good times[^23].

5. The short-term impact of a temporary stimulus varies significantly depending on the choice of the fiscal instrument (figure 4.14). Model simulations consistently indicate that the short-term multiplier is larger for public spending on goods and services than for transfers to households or for tax cuts. They are the lowest for corporate income tax cuts. However, a permanent increase in public spending financed by debt has substantially less favorable short-term effects and has long-term negative effects.

6. Expenditure-based fiscal consolidations tend to have milder adverse effect on GDP, whereas tax-based consolidations do have a strongly negative impact (Alesina et al. 2017). The two forms of consolidation differ in their impact on private expectations (hence on private investment) and, in some cases, in the endogenous reaction of monetary policy.

7. The fiscal multiplier tends to be lower for countries whose fiscal position is weak (high debt ratio). Consistent with partial Ricardian equivalence, a fiscal expansion that threatens debt sustainability may trigger precautionary saving behavior on the part of private agents. The evidence on the relationship between sustainability and the fiscal multiplier is, however, disputed: Auerbach and Gorodnichenko (2017) find that when economic conditions are weak, fiscal stabilization is effective even for high-debt countries.

Summing up, recent research provides empirical support for using fiscal policy for stabilization purposes, but it also highlights its limitations and the potential for misguided action. The main conclusions is, perhaps, that there is



<!-- p. 192 -->

**Figure 4.14** Alternative estimates of the impact multiplier (no monetary accommodation).

The stimulus is supposed to last for two years and then be discontinued. The models referred to are those used by major institutions in the United States, the euro area, and Canada. The monetary policy response is endogenously determined by the central bank's reaction function. Each dot corresponds to a particular simulation with a particular model: EC for European Commission, IMF for International Monetary Fund, ECB for European Central Bank, FRB for Federal Reserve Board, SIG for Federal Reserve System SIGMA model (the Board of Governors of the Federal Reserve System uses two models, FRB-US and SIGMA), and BOC for Bank of Canada.

Authors, on the basis of simulations reported in Coenen et al. (2012).

no such thing as a reliable “fiscal instrument” whose impact could be regarded as independent from the context in which it is used and the specific design of fiscal action. We return to these issues in Section 4.3.

### 4.2.2 Public debt sustainability

There is no universal criterion for assessing public debt sustainability. A first, very rough one relies on the stability of the debt-to-GDP ratio. Consistently, the observed primary balance is compared to the debt-stabilizing benchmark introduced in Section 4.1. This simple exercise has the merit of recalling that as far as sustainability is concerned, the appropriate level of the fiscal balance depends on the growth rate and the inflation rate (and that the appropriate level of the primary balance depends in addition on the long-term interest <!-- p. 193 --> rate). The problem with this approach is that the observed debt-to-GDP ratio may not correspond to an optimal, long-run level. If the observed level of debt is too high or possibly too low, targeting its stability provides inadequate guidance to debt sustainability.

#### a) Concept and indicators

The key to defining sustainability is to allow for a government to remain permanently in debt (because it is infinitely long-lived) while excluding “pushing the debt ahead” as in the speculative chains or Ponzi games[^24]. The technique has been known for a long time: Lewis Carroll pleasantly illustrates it in *Sylvie and Bruno*:

“Ah, well, I can soon settle his business,” the Professor said to the children, “if you’ll just wait a minute. How much is it, this year, my man?” The tailor had come in while he was speaking.

“Well, it’s been a doubling so many years, you see,” the tailor replied, a little gruffly, “and I think I’d like the money now. It’s two thousand pound, it is!”

“Oh, that’s nothing!” the Professor carelessly remarked, feeling in his pocket, as if he always carried at least that amount about with him. “But wouldn’t you like to wait just another year, and make it four thousand? Just think how rich you’d be! Why, you might be a King, if you liked!”

“I don’t know as I’d care about being a King,” the man said thoughtfully. “But it does sound a powerful sight o’ money! Well, I think I’ll wait—”

“Of course you will!” said the Professor. “There’s good sense in you, I see. Good-day to you, my man!”

“Will you ever have to pay him that four thousand pounds?” Sylvie asked as the door closed on the departing creditor.

“Never, my child!” the Professor replied emphatically. “He’ll go on doubling it, till he dies. You see it’s always worthwhile waiting another year, to get twice as much money!” (Carroll, 1889, quoted by Keynes, 1931)

The rigorous definition of debt sustainability builds on the intuition that public finances are sustainable if the state meets its intertemporal budget constraint; that is, if spending is actually financed—be it today, tomorrow, or the day after tomorrow—because expected future tax receipts cover expected future primary spending and the interest charges on outstanding debt. This can be shown to be equivalent to saying that the present value (at time 0) of the expected debt ratio at time $t$ tends toward zero as $t$ tends toward infinity, a condition known as the transversality condition (box 4.13). Intuitively, this means that the future debt can be high but cannot grow faster than the difference between the real interest rate and the real growth rate of the economy. This is also equivalent to saying that the sum of the current debt and the present value of future primary expenditures equals the present value of future receipts.


<!-- p. 194 -->

#### Box 4.13 Sustainability and the Government’s Intertemporal Budget Constraint

Since states do not have a predefined, finite lifetime, there is no need for the net public debt to fall to zero at any given date in the future. Rather, debt sustainability implies that the present value (at time 0) of debt at time $t$ tends toward zero as $t$ tends toward the infinite. This condition, called the *transversality condition*, is equivalent to the equality between the present value over time of the government’s future income and expenditure streams.[^b4-13a]

We start with the continuous-time equivalent to the debt accumulation equation (B4.5.4) of box 4.5:

$$ \frac{db_t}{dt} = (i-n)b_t + \delta_t = (r-g)b_t + \delta_t \tag{B4.13.1} $$

The variation of the debt ratio $b_t$ over time $t$ is a function of the interest rate ($i$ in nominal terms, $r$ in real terms), of the growth rate ($n$ in nominal terms, $g$ in real terms), and of the primary deficit ratio $\delta_t$. For the sake of simplicity, we assume that the real interest rate and the growth rate are constant. Denoting by $b_0$ the initial debt ratio, the debt ratio at time $t$ can be obtained by integrating Equation (B4.13.1) over time:

$$ b_t = b_0 e^{(r-g)t} + \int_0^t \delta_s e^{(r-g)(t-s)} ds \tag{B4.13.2} $$

The present value of $b_t$ at $t=0$ is obtained by multiplying both sides of this equation by $e^{-(r-g)t}$. The discount rate $(r-g)$ allows taking into account the dampening effect of growth on the debt ratio:

$$ b_t e^{-(r-g)t} = b_0 + \int_0^t \delta_s e^{-(r-g)s} ds \tag{B4.13.3} $$

When $t$ tends to infinity, the present value of the debt ratio must tend toward zero, which implies that the right-hand side of the equation also tends toward zero:

$$ \lim_{t\to\infty} b_t e^{-(r-g)t} = 0 \text{ implies } b_0 = -\int_0^\infty \delta_s e^{-(r-g)s} ds \tag{B4.13.4} $$

The first condition is called the *transversality condition*. If $r > g$, it is necessary and sufficient to fulfil it that the debt ratio increases at a lesser pace than the discount rate $r-g$. If $r < g$, the government can finance the debt service through new borrowing while remaining solvent. This was the situation of the 1970s, a period when public debt problems were benign[^b4-13a].


<!-- p. 195 -->

and it has become the case again in the 2010s for many countries. But for advanced countries, real interest rates were higher than the growth rates of the economy from the 1980s to the 2000s.

The second condition implies that the present value of future primary surpluses (the opposite of the primary deficits) “repays” the initial debt. Writing $\delta = x + h - \tau$, where $x$ designates expenditure on goods and services, $h$ public transfers, and $\tau$ taxes and levies, the condition becomes:

$$
b_0 + \int_{0}^{\infty} (x+h)_s e^{-(r-g)s} ds = \int_{0}^{\infty} \tau_s e^{-(r-g)s} ds \tag{B4.13.5}
$$

It states that the sum of the initial debt and of the present value of future expenditures must equal the present value of future income. This is the *intertemporal budget constraint* of the government.

Blanchard (1993) takes the sequence of public expenditures and transfers as given in terms of GDP, and calculates the constant tax rate $\tau^*$—which he calls the *sustainable tax rate*—that ensures debt sustainability:

$$
\tau^* = (r-g) \left[ b_0 + \int_{0}^{\infty} (x_s - h_s) e^{-(r-g)s} ds \right] \tag{B4.13.6}
$$

*[Editorial note: the book prints $(x_s - h_s)$ in (B4.13.6) (verified on the page image, p. 195). This is inconsistent with the box's own definition $\delta = x + h - \tau$ and with (B4.13.5); the correct form is $(x_s + h_s)$. Kept as printed; see Team note 2 below.]*

Taxing income at rate $\tau$ is sufficient to service (at rate $r-g$) the sum of the initial debt and of the present value of the future stream of primary expenditures.

The gap between the sustainable tax rate $\tau^*$ and the observed tax rate $\tau$, called the *tax gap*, provides an indicator of sustainability. If $\tau < \tau^*$, the long-term sustainability of public debt requires either a rise in taxes or a cut in expenditures.

As a simple finite-horizon benchmark for assessing sustainability, Blanchard also proposes to calculate the constant tax rate necessary to restore the initial level of the ratio of public debt after a given number $N$ of years. However, finite-horizon benchmarks are necessarily more arbitrary.

Consistently, the sustainability of public finance can be assessed by comparing the current tax rate with the *sustainable tax rate* that would ensure debt sustainability if kept constant in the future (box 4.13). The difference between the two is called the *tax gap*. A positive tax gap signals that fiscal policy is unsustainable and that either the level of taxation or the expenditure level will need to be adjusted in the future.

[^b4-13a]: The layman’s version of the transversality condition is a famous remark by Herbert Stein, the former chairman of the Council of Economic Advisers under president Nixon, according to whom “if something cannot go on forever, it will stop.”

<!-- end Box 4.13 -->

> **Team note 2 — under Box 4.13 (Cath, 2026-11-09)**
>
> *Correct form of (B4.13.6)* (the book prints a minus; see the editorial note above): with $\delta = x + h - \tau$,
> $$\tau^* = (r-g)\Big[b_0 + \int_0^\infty (x_s + h_s)\,e^{-(r-g)s}\,ds\Big], \qquad r > g .$$
> *Discrete-time counterpart used in DFD:* $d_0 = \sum_{t\ge1} pb_t \prod_{s=1}^{t}\frac{1+g_s}{1+r_s}$, given $\lim_{T\to\infty} d_T \prod_{s=1}^{T}\frac{1+g_s}{1+r_s} = 0$.
>
> *Regime caveat.* For $r \le g$, both $\tau^*$ and the present-value form lose their meaning: the discount factor no longer discounts. The book notes the case but does not develop it. This is the open watch item (`../watch_items/debt-stabilising-primary-balance-under-r-lt-g.md`).
>
> *Why this box matters for RF.* Blanchard's sustainable tax rate and the **tax gap** $\tau^* - \tau$ formalise RF's target. RF can **derive** a sustainability-consistent revenue path instead of asserting 25% by 2036. Feed the spending path $x + h$, including Beth's pension and health profiles, and Anne's demography, into either the infinite-horizon form or Blanchard's finite $N$-year benchmark (end of the box). This is the same logic as the EU's S2 indicator (p. 196). Mexico caveat: $\tau$ here means *all* non-debt revenue. Oil revenue therefore belongs in $\tau$ for sustainability, but not in the OECD tax-pressure headline. This is the same separation the Contabilidad de la Muerte makes.


<!-- p. 196 -->

This approach is used in the EU to monitor the fiscal position of member countries. To this end, the European Commission has defined two indicators:^[25]^

* S1, the *medium-term fiscal sustainability indicator*, gives the improvement in the government structural primary balance that must be carried out over a five-year period to reach, by 2030, a 60% public debt-to-GDP ratio (the EU Treaty reference value), taking into account the financing for any future additional expenditure arising from an aging population. It is a finite-horizon indicator that relies on an *a priori* target for the debt ratio;
* S2, the *long-term fiscal sustainability indicator*, gives the upfront adjustment to the current structural primary balance (assuming it will thereafter be kept at the adjusted value) required to stabilize the debt-to-GDP ratio over the infinite horizon, taking into account the effect of aging on future public spending. Like the tax gap presented in box 4.13, of which it provides an empirical implementation, S2 does not incorporate any specific target for the debt ratio.

This approach, of course, is fragile. First, it relies on long-term projections of growth, interest rates, and public expenditures. Second, it assumes that, provided future revenues match future expenditures, *any* level of public debt can be sustained and financed on the bond market. Third, it provides a global assessment of sustainability but does not specify what the adjustment path should be. Fourth, the sustainable tax rate can vary abruptly (“jump”) in response to a change of economic policy scenario—for example, a rise in interest rates or a pension reform that reduces future government spending. Fifth, the long-term sustainability indicator ignores possible short-term financing constraints.[^26]

#### b) Fiscal space

According to the intertemporal budget constraint approach, any level of debt can be sustained provided the adequate primary surplus can be maintained permanently. However, large and sustained primary surpluses amount to making the living generation pay for the fiscal excesses of the previous ones, and they are not sustainable politically. Zheng (2014) finds that, over a 50-year period, only 11 out of 87 countries recorded primary surpluses in excess of 5% of GDP for five years or more. For the assessment of Greek solvency in the 2010s, similar benchmarks were used for determining if there was a high probability that the country would service its debt. When carrying out debt sustainability analyses, the IMF (2013) considers that “closer scrutiny” is called for when a country is projected to maintain a cyclically adjusted primary surplus in excess of 3.5% of GDP over a three-year period.



<!-- p. 197 -->

Building on such observations, Ghosh et al. (2011) depict the fiscal behavior of indebted countries in a stylized graph (figure 4.15). The solid S-shaped line depicts the typical response of the primary balance to variations in the debt ratio. For low debt ratio levels, sustainability is not a concern, and the primary balance does not respond to debt increases. As the debt ratio rises, however, such concerns emerge, resulting in a policy-induced increase in the primary balance[^27]. However, when the primary surplus gets large, this response weakens for political economy reasons, and eventually it becomes muted. This response pattern results in the S-shaped policy response curve.

The dashed straight line gives the primary surplus that is required for stabilizing the debt ratio. As discussed previously, its slope is the difference between the real interest rate and the real growth rate. When the S-shaped line is below the dashed line, the debt ratio increases, and vice versa when it is above. To simplify the analysis, we consider the interest rates and growth rates as exogenous.

It is apparent that there are two equilibria for the debt ratio, each of which corresponds to an intersection between the S-shaped and the straight dashed lines. The first $d^*$ corresponds to a stable equilibrium. The second $d^{**}$ is unstable because any increase of the debt level above that threshold results in an unstoppable rise of the debt ratio. For this reason, $d^{**}$ is the maximum possible debt ratio. The *fiscal space* can therefore be defined by the difference $d^{**} - d$ between the maximum and the actual debt level[^28].

The S-curve can be estimated in a panel regression with country fixed effects, resulting in estimates for the difference between the maximum and the current debt ratios. In 2015, the methodology (which has been adopted

**Figure 4.15** Debt sustainability and fiscal space.

From Ghosh et al. (2011).

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart illustrates the relationship between the primary balance ($s$) and the debt-to-GDP ratio ($d$). The vertical axis represents the primary balance, while the horizontal axis shows the debt/GDP ratio. Two curves are plotted: a solid S-shaped curve labeled "Primary balance $s$" and a dashed straight line labeled "Interest burden $(r-g)d$". The intersection points of these lines indicate stable and unstable equilibria for the debt ratio.

<!-- p. 198 -->

by Moody's, the rating agency) generally put the maximum debt level in the vicinity of 200–250% of GDP.

As indicated in figure 4.15, the fiscal space depends on $(r-g)$: the higher the difference between the real interest rate and the growth rate, the narrower it is. It is also smaller for countries participating in a monetary union. This is because expectations of insolvency result in a higher interest rate on the public debt $r$, which in turn pushes $d$ to the left. As shown by Paul De Grauwe (2011), this opens the possibility of self-fulfilling debt crises. This risk can be controlled if the central bank is able to step in and prevent speculation from pushing the sovereign into insolvency. But there are limitations to what the central bank of a monetary union can do. In the euro area, especially, direct financing of governments by the European Central Bank (ECB) or the national central bank is prohibited by treaty, and, although purchase of government bonds on the secondary market is authorized, large-scale central bank intervention on a particular bond market has distributional consequences that may give it a fiscal, rather than monetary character. The euro crisis of 2010–2012 led many to realize that the absence of a lender of last resort for sovereigns results in making individual governments more vulnerable to speculative attacks. ECB interventions on particular markets initiated in 2010 through the Securities Markets Program quickly engendered controversy and led it to create the Outright Monetary Transactions (OMT) program, access to which is conditioned on fiscal adjustment and economic reforms, to be negotiated between the government and the European institutions (see Chapter 5).

#### c) Sustainability and the effectiveness of fiscal policy

Whether or not fiscal policy is regarded as sustainable is bound to affect its effectiveness. Intuitively, economic agents may spend more in response to a fiscal stimulus if they do not perceive it as endangering the sustainability of public debt, but the same agents may respond by spending less if they expect unsustainability to lead to a policy reversal and the stimulus to be quickly followed by a consolidation.

Sutherland (1997) formalized this intuition in a model that captures the possibility of debt-induced changes in the value of the Keynesian multiplier. The reason is uncertainty regarding the distribution of future taxes across generations. In his overlapping-generations model, presented in box 4.14, consumers have a finite horizon; agents behave in a Keynesian way as long as the public debt remains low enough for the burden of fiscal adjustment to be safely transmitted to future generations; they become increasingly anti-Keynesian (contracting their spending in reaction to a fiscal stimulus) as the likelihood increases that they themselves will have to bear that burden. The same fiscal action can therefore lead to opposite results depending on the level of public debt. Such models rest on somewhat ad hoc assumptions, but they help to describe situations of fiscal crisis during which expectations take a prominent role.


<!-- p. 199 -->

#### Box 4.14 Public Debt and Fiscal Policy Effectiveness

Sutherland (1997) proposes a simple model where fiscal expansion has the traditional Keynesian effect at moderate public debt levels, but where the multiplier turns negative when debt reaches very high levels.

The representation of households' behavior is based on an overlapping-generation model. At any date, two generations coexist, the "young" and the "old." Fiscal policy is represented by a primary deficit $D$ (per capita) that takes the form of a (non-distortionary) lump-sum transfer to/from the consumers. Denoting $r$ the constant interest rate, the dynamics of the per capita public debt $B$ at time $t$ is given by:

$$dB_t = rB_t dt + D_t \quad \text{(B4.14.1)}$$

where the deficit $D$ includes a stochastic component. Under these conditions, a series of shocks to the deficit can make the debt explosive.

To fulfill the intertemporal budget constraint, Sutherland imagines a discrete adjustment process: when debt per capita reaches an exogenous ceiling $U$, a lump-sum tax $T$ is levied on each individual, which reduces the debt to $U-T$; when it reaches an (intuitively negative) floor $L$, a per capita lump-sum transfer $T$ is paid to each individual, which increases public debt to $L+T$.

Consumers have finite life, with a constant death probability $\theta$. Each individual consumes a quantity $c$ of the same homogeneous good, freely exchanged at a fixed price, and derives from it an instantaneous utility $u(c)$, where $u$ is quadratic. In each period, all individuals receive a fixed income $y$, plus income $(r+\theta)A$ from their wealth $A$ (wealth is placed with insurance companies that inherit when the individual dies, hence the risk premium $\theta$). The consumer's budget constraint is therefore described by:

$$dA_t = \left[y - c_t + (r+\theta)A_t\right]dt + D_t \quad \text{(B4.14.2)}$$

The individual maximizes expected utility:

$$E_t \int_t^\infty u[c_\tau] e^{-(r+\theta)(\tau-t)} d\tau \quad \text{(B4.14.3)}$$

Which results in consumption $c_t$:

$$c_t = y + (r+\theta)\left[A_t - E_t \int_t^\infty \delta_\tau T e^{-(r+\theta)(\tau-t)} d\tau\right] \quad \text{(B4.14.4)}$$

where $\delta_\tau$ is equal to 1 when at time $\tau$ the debt reaches the ceiling $U$ and a crisis occurs that implies a debt reduction; -1 when debt reaches the floor $L$ and individuals receive a transfer; and zero otherwise.

<!-- p. 200 -->

Individuals therefore consume their income net of the present value (discounted at rate $r+\theta$) of expected future taxes. The results of the model depend on the term:

$$S_{t}=E_{t} \int_{t}^{\infty} \delta_{\tau} T e^{-(r+\theta)(\tau-t)} d \tau \tag{B4.14.5}$$

Sutherland shows that $S$ is an increasing function of $B$ and that $\partial S / \partial B$ is close to zero when $B$ is low (in absolute value), but larger than unity when $B$ (in absolute value) approaches the thresholds $L$ or $U$. When $B$ is low, a fiscal expansion (a rise in $D$ in Equation (B4.14.2)) increases consumption in accordance with the traditional Keynesian effect. But when $B$ approaches $U$, a deficit $D$ triggers expectations of an impending adjustment and causes a reduction of consumption in preparation for the upcoming tax increase: the fiscal expansion exhibits an anti-Keynesian effect and leads to a contraction of output.

<!-- end Box 4.14 -->

*[Paraphrase only — never quote: the right margin of p. 200 is clipped in the photo and the last words of each line in this and the next paragraph were inferred by the model.]* Empirical investigations confirm that debt sustainability, or the lack thereof, significantly affects the fiscal multiplier. Corsetti et al. (2013) investigate the effectiveness of fiscal policy in a model where the interest rate on public debt depends on the level of government indebtedness. A higher probability of sovereign debt restructuring increases the risk premium demanded by lenders. As long as the central bank does not lose control of the interest rate, it can lower the policy rate to offset the rise on this risk premium. However, when it is constrained by the zero lower bound, it cannot use the same lever anymore, which means that countries at risk of default see that risk magnified by interest rate inertia. The fact that the central bank has hit the zero lower bound therefore both increases the fiscal multiplier (for countries in good shape) and reduces it (for countries in trouble).

### 4.2.3 Open-economy dimensions

#### a) The Mundell-Fleming model

The Keynesian approach can easily be extended to the open economy, in particular with the *Mundell-Fleming* model, developed independently by Robert Mundell and Marcus Fleming in the early 1960s.[^29] This open-economy extension of the IS-LM model introduces the exchange rate regime as a determinant of the Keynesian multiplier. In a flexible exchange rate regime, the fiscal multiplier is lowered—even nullified if capital is perfectly mobile across relatively small countries—by the appreciation of the exchange rate.

<!-- p. 201 -->

that follows a fiscal expansion. Conversely, the multiplier is larger in a fixed exchange rate regime because there is little crowding out (see box 4.15 and Chapter 7 for the definition of exchange rate regimes).

The main results of the Mundell-Fleming model are summarized in table 4.2. Given its simplicity, the model remains a widely used reference by international economy practitioners. For example, it provides a simple framework to think about the consequences of fiscal policy in the euro area. Monetary

#### Box 4.15 The Mundell-Fleming Model

The canonical Mundell-Fleming model studies macroeconomic policy effectiveness in a small country under *perfect capital mobility* (and under the Keynesian assumption of underemployment of resources). Perfect capital mobility implies that the interest rate cannot deviate from the world interest rate (otherwise capital would flow in or out in search of yield, see Chapters 5 and 7). This is represented by a horizontal interest rate arbitrage condition schedule. At the same time, the internal equilibrium is represented by the IS and LM curves, representing respectively product- and money-market equilibrium. Equilibrium in the model results from the simultaneous fulfilment of three conditions, rather than two in the standard closed economy framework. Which of these conditions endogenously adjusts to the equilibrium determined by the other two depends on the exchange rate regime.

**Floating Exchange Rate**

Consider first the case of a *floating exchange rate* regime. Assume that the central bank keeps money supply constant and that the exchange rate is market determined. By shifting the IS curve to the right, a fiscal expansion triggers an increase in output and income, thereby leading to an increase in money demand and—with constant money supply—to an upward pressure on the interest rates. Capital flows in, causing an exchange rate appreciation (a loss of export competitiveness). The IS curve thus shifts back to the left as the demand for the country’s products diminishes. Since the open-economy equilibrium is determined by the intersection of LM and the international interest rate arbitrage condition, the only solution is that the exchange rate appreciates up to the point where aggregate demand returns to its original pre-fiscal expansion level (figure B4.15.1). The IS curve and thus fiscal policy play no role in the determination of the output: an increase in public demand simply crowds out the nonresidents’ net demand for the country’s exports.

<!-- p. 202 -->

**Fixed Exchange Rate**

Alternatively, suppose that the exchange rate is *fixed*, meaning that the central bank intervenes on the foreign exchange market through buying and selling foreign currency. Capital inflows consecutive to a fiscal expansion result in the central bank selling the domestic currency for the foreign one, and thereby in an accumulation of foreign exchange reserves by the central bank. If not sterilized (see Chapter 7), this reserve accumulation increases money supply and makes the LM curve move to the right. This endogenous monetary expansion leads to a positive fiscal multiplier (figure B4.15.2). Fiscal policy is powerful and monetary policy is ineffective.

**Figure B4.15.2** Fiscal expansion in a fixed exchange rate context.

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart shows an IS-LM model under a fixed exchange rate regime. The vertical axis represents the national interest rate, and the horizontal axis represents output. Initially, the economy is at equilibrium point E where the IS curve (goods market equilibrium) intersects the LM curve (money market equilibrium). An exogenous fiscal expansion shifts the IS curve to the right, leading to a new intersection with the original LM curve at point E'. However, due to capital inflows and central bank intervention, the LM curve also shifts to the right, resulting in a final equilibrium at point E''. The diagram illustrates how fiscal policy can be effective under fixed exchange rates, as both fiscal and monetary policies contribute to increasing output.

**Figure B4.15.1** Fiscal expansion in a floating exchange rate context.

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The chart depicts an IS-LM model under a floating exchange rate regime. The vertical axis represents the national interest rate, and the horizontal axis represents output. Initially, the economy is at equilibrium point E where the IS curve (goods market equilibrium) intersects the LM curve (money market equilibrium). An exogenous fiscal expansion shifts the IS curve to the right, leading to a new intersection with the original LM curve at point E'. However, due to capital outflows and central bank non-intervention, the LM curve remains unchanged, resulting in a final equilibrium at point E''. The diagram illustrates how fiscal policy can be less effective under floating exchange rates, as monetary policy adjusts automatically to maintain equilibrium.

<!-- p. 203 -->

**The Case of No Capital Mobility**

When capital is *not mobile*, results are partially reversed: Under a *floating* exchange regime, the deterioration of the current account balance induced by fiscal expansion (because of the increase in import demand) leads to an exchange rate depreciation and to an improvement of export competitiveness, strengthening the initial demand impact of the fiscal expansion. Under *fixed* exchange rates, the current account deterioration results in a reserve loss and in a monetary contraction that counters the initial expansion. Ultimately, the current account must balance—which means that output is determined by what is compatible with the external constraint. Differences in capital mobility and exchange rate regimes thus explain why similar fiscal policies can have contrasting effects on output.

<!-- end Box 4.15 -->

**Table 4.2**

Short-term effectiveness of fiscal policy in a small open economy: the basic results

| | High capital mobility | Low capital mobility |
|---|---|---|
| Floating exchange rates | Ineffective | Very effective |
| Fixed exchange rates | Very effective | Partially effective |

union as a whole behaves like a country in a floating exchange rate regime: if capital is fully mobile, fiscal policy is relatively ineffective (unless monetary policy is constrained by the zero lower bound). However, for any given member of the zone, fiscal policy is effective because crowding-out effects are diluted within the zone. Hence, the Mundell-Fleming model suggests that fiscal policy should be used by individual member states hit by asymmetric shocks, but less so as a collective response to a symmetric shock because, in the latter case, the exchange rate adjustment would tend to offset its stabilizing effect (this is only true, however, to the extent that the interest rate responds to the fiscal loosening; at the zero lower bound, this does not hold, implying that fiscal policy can be effective at union level).

Note, however, that the Mundell-Fleming framework does not incorporate two key elements that may strongly modify the impact of a fiscal expansion. First, it is a static model where market expectations play no role. Second, there is no debt, hence no concern over debt sustainability and no risk premium. It is ill-suited to discuss the impact of fiscal policy in a highly indebted country.

<!-- p. 204 -->

#### b) Fiscal policy spillovers

The reason why fiscal policy is ineffective in a Mundell-Fleming world of high capital mobility and floating exchange rates is that its effects are fully transmitted to the trade partners, leading to what is called a *fiscal spillover effect*.

Spillovers also exist between countries in a fixed exchange rate regime or in a monetary union. In the latter case, the fiscal expansion increases both the demand for goods and the common interest rate, hence the net effect on partner countries is ambiguous: it may be expansionary for some because the trade channel dominates the monetary policy channel and contractionary for others because they are in the opposite situation. Think, for example, of the effects of a Spanish fiscal expansion within the European Monetary Union (EMU): it is likely to benefit significantly Portugal and France, whose exports to Spain are significant, but much less so Austria, Finland, and Estonia because they export little to Spain but are affected by the interest rate increase resulting from the ECB’s reaction to a demand-side expansion within the euro area. They could even be hurt. Furthermore, as a fiscal expansion in one country of significant size appreciates the common exchange rate, exports by the monetary union partners may suffer. For this reason, the Mundell-Fleming model indicates that fiscal spillovers within a monetary union are a matter for empirical investigation.

The issue was the matter for heated debates in the context of weak post-euro area crisis recovery in the 2010s. International organizations called upon Germany to support growth through fiscal expansion, but German officials denied that domestic reflation could significantly boost growth in partner countries and, especially, alleviate the woes of peripheral countries. Model-based estimates by the Deutsche Bundesbank (2016) do not find that spillover effects from a German fiscal expansion could be significant: assuming endogenous monetary policy reactions, a 1% of GDP investment boost in Germany would increase German GDP by 0.45% and Dutch GDP by 0.2% after two years, but it would only increase Greek GDP by 0.05% and Spanish GDP by 0.02%. Such normal-times estimates are however disputable because they do not apply in a situation where monetary policy is constrained by the zero lower bound. In the latter situation, a fiscal expansion in the core euro area countries does not result in a rise in the interest rate, and peripheral countries benefit from both higher demand and higher inflation in the core countries. Blanchard, Erceg, and Lindé (2017) find that, under the zero-lower bound, the impact of a core expansion is about half as large in peripheral countries as in core countries.

The upshot is that in the same way the effectiveness of fiscal policy is state-dependent in a single-country context, spillovers onto partner countries are both system-dependent (because they are heavily affected by the exchange <!-- p. 205 --> rate regime and the degree of capital mobility) and context-dependent (because they depend on whether monetary policy is constrained by the zero lower bound).

## 4.3 Policies

Fiscal choices everywhere top the policy agenda and are a matter for heated policy debates. Controversies about the proper budgetary stance, fiscal laxity and austerity, debt accumulation, and, in some countries, debt restructuring are the bread and butter of economic policy discussions. Major policy successes or failures are often attributed to fiscal decisions. Doctrines also vary over time: fiscal policy was regarded as the ultimate policy tool in the 1970s, only to fall out of fashion in the 1980s and the 1990s. The global recession of 2009 and the limits encountered by conventional monetary policy in the 2010s have resulted in a significant revival, yet the sovereign debt crises undergone by several European countries have also highlighted the risks involved in testing the limits of the fiscal space.

The debate has been particularly vivid in Europe, where it has focused on the fiscal consequences of forming a monetary union. On the one hand, governments deprived of independent monetary policies are naturally prone to rely more on the fiscal instrument for stabilization purposes. On the other hand, participation in an inflation-adverse monetary union has resulted in the removal of the debt monetization option: as highlighted by the 2010–2012 European sovereign crises, debt has become much riskier after the locking-in of exchange rates. For these reasons, the euro area has provided a rich laboratory for assessing fiscal policy effectiveness, decentralization, and coordination.

Changes in the approach to fiscal policy have not only been a matter of doctrine. Whereas fiscal choices used to be essentially discretionary, they are now increasingly shaped by fiscal rules, such as deficit limits, and by institutions, such as independent fiscal councils. Governments and parliaments remain everywhere in charge of the final decision, but room for discretionary decisions is more limited than in the 1990s. Whether or not such frameworks represent an improvement is a matter for fierce controversies.

We start by presenting and discussing the rules and institutions that constitute the current framework for fiscal policy. Next, we address the resolution of sovereign debt crises. We then analyze the specific case of the euro area. We end with a discussion of the “old” and “new” views of fiscal policy.

### 4.3.1 Fiscal rules and institutions

As noted already, “fiscal policy” should not be assimilated to “discretionary fiscal policy.” In many countries—though not in all—decisions are increasingly <!-- p. 206 --> shaped by policy rules and institutions that contribute to limiting the scope for discretionary choices. The design of rules and the choice of a mandate for institutions determine a country’s fiscal regime and contribute to the quality of its policy.

#### a) Fiscal rules

In the late 1980s, very few countries were equipped with fiscal rules: according to the IMF (Lledó et al., 2017), only Germany, Indonesia, Japan, Malaysia, Singapore, and, surprisingly, the United States[^30]. By 2015, no less than 93 countries had such rules. Many of them had put in place a framework consisting of several guidelines governing the budget balance, the level of expenditure, revenues, or the public debt. The euro area has been at the forefront of this trend toward rules-based fiscal policy, but it is by no means the only region of the world where such a move was apparent.

Fiscal rules are legal provisions that impose constraints on fiscal policy through numerical limits on budgetary aggregates. They can target the deficit, the debt, or public expenditures. They can be couched in nominal terms (such as absolute limits for the financial deficit, the primary deficit, or the saving-investment balance of the public sector), in real terms (such as benchmarks for the real growth rate of public spending), or in structural terms (such as thresholds for and minimum annual improvements of the cyclically adjusted balance). They can apply *ex ante* (to the budget submitted to vote) or *ex post* (to the observed results). They can relate to the general government as a whole or to sub-entities (the federal sector or individual states). They can, as in the EU, result from an international treaty and secondary supranational legislation, as well as be part of the national constitution, or simply national law.

Rules generally aim at correcting distorted incentives that arise from the political economy process and result in overspending and departures from fiscal responsibility. Four main explanations have been put forward to justify them. The first arises from the political business cycle: because voters are ill-informed or perhaps irrational, governments are prone to deficit spending and tend to overstimulate the economy ahead of election years (Nordhaus, 1975); rules help correct the resulting tendency to excessive debt accumulation. The second relies on the consequences of electoral competition: partisanship and disagreements over the allocation of public spending result in a tendency for each camp to overspend on its preferred policies while in power (Tabellini and Alesina, 1990); unlike the previous one, this explanation does not rest on the voters’ failure to grasp the consequences of budget deficits but on the division and the strategic use by each camp of the budget deficit. In this setting, a balanced budget rule is socially optimal. The third explanation—developed in Section 4.3.3—is that, in a currency union, national governments do not fully internalize the cost of budget deficits because part of it falls on partner countries; budget rules help correct this coordination failure. But not least, public debt accumulation affects intergenerational equity.


<!-- p. 207 -->

fourth explanation is that because the future generations are not represented in parliament, there is a tendency to transfer the cost of servicing it onto the yet-to-be-born citizens.

Most rules are therefore geared toward fiscal prudence. They could conceptually also help correct excessive caution and a failure to provide adequate fiscal stimulus when needed. There is less of a contradiction than it seems between the two aims: the more governments are prudent in good times, the more aggressively they can pivot to stimulus in bad times.

Research has attempted to account for the spread of fiscal rules. Elbadawi, Schmidt-Hebel, and Soto (2015) find that a higher GDP per capita, democratic institutions, a federal structure, the existence of checks and balances, and political stability all contribute to their adoption. Rules are also more likely in countries characterized by a high old-age dependency ratio, a fixed exchange rate regime or an inflation-targeting regime, and financial openness.

In their landmark article on the design of fiscal frameworks, Kopits and Symansky (1998) identify eight criteria for an “ideal” fiscal rule:

*   a clear definition,
*   transparent public accounts,
*   simplicity,
*   flexibility—in particular regarding the capacity to react to exogenous shocks,
*   policy relevance in view of the objectives pursued,
*   capacity of implementation with possibility of sanctioning nonobservance,
*   consistency with the other objectives and rules of public policies,
*   accompaniment by other effective policies.

This simple list suggests potentially delicate trade-offs, for example, between simplicity and relevance or between clarity and flexibility. Indeed, rules aim at safeguarding sound government finances in a credible and sustainable way while preserving the contribution of fiscal policy to contra-cyclical output stabilization. However, whether or not they succeed in achieving these objectives is a matter of design and enforcement. Good rules can improve policy, but bad ones can worsen it.

The evolution of the European fiscal framework (see box 4.19 in Section 4.3.3) is a case in point. The original *Stability and Growth Pact* (SGP), the set of fiscal rules and procedures established in the mid-1990s to avoid “excessive deficits”, relied exclusively on thresholds and benchmarks for the government financial balance. As such, it did not take cyclical developments into account: a country whose balance had improved because of a cyclical boom was considered compliant with the pact, irrespective of its actual decisions (and a country whose deficit had deteriorated in a recession was considered in breach of the pact, again irrespective of its decisions). A decade later, the SGP was reformed to make room for consideration of the cyclically adjusted deficit, and it was further amended in the wake of the euro crisis <!-- p. 208 --> so that cyclically adjusted behavior took center stage in the assessment of national policies. It emerged almost immediately, however, that reliance on an unobservable variable was a source of complexity, incoherence over time, and dispute.

Rules that apply to state and local governments play an important role in decentralized systems. They can be part of an overall framework designed to ensure that subnational entities comply with fiscal discipline—especially if state and local governments can apply for support from the center in case of trouble. They can alternatively result from self-imposed discipline. This is the case in the United States, where states are responsible for their own fiscal affairs. The federal constitution grants them a very large degree of fiscal autonomy, and they cannot expect to be bailed out if they lose access to financial markets (see box 4.19 for a historical perspective on the issue). All states but Vermont have enshrined balanced budget requirements in their constitution or their legislation. Rules can mandate an $ex\text{-}ante$ balance (in which case the state account can exhibit a deficit in case of unfavorable economic developments) or a more stringent $ex\text{-}post$ balance, often called a no-carryover provision. The downside to such provision is that states may be forced to behave pro-cyclically in recessions. This is indeed the case in the United States: although most states have put in place rainy-day funds they can draw on in bad times, there are sharp limitations to what such funds can achieve. In 2009, most US states would have been forced to cut social expenditures in response to the recession, had the stimulus program enacted in 2009 not included federal transfers to state and local governments of the order of magnitude of $0.3\%$ of GDP over a year. More generally, the US policy system assigns the main responsibility for fiscal stabilization to the federal level.

In practice, fiscal rules can be specified in various forms (table 4.3): public debt ceilings, fiscal (financial or primary, headline or structural, overall or on current expenditures) budget balance commitments, rules governing spending targets, and assignment rules for fiscal surpluses. Each has merits and drawbacks.

The balanced budget principle is sometimes expressed as a requirement that current expenditures be financed by current receipts: this is the so-called golden rule of public finance. This rule, which was enshrined at the end of the 1960s in the German constitution until it was reformed in 2009, authorizes the use of debt to finance capital expenditures only, unless there is a “disturbance of the macroeconomic equilibrium.” The rationale is that debt allows spreading out of the financing of an investment over its lifetime and that, if outstanding government liabilities are matched by (presumably profitable) government assets, this preserves government net wealth. Golden rules have supporters among economists, but they do not prevent debt from becoming unsustainable (if the counterpart of debt accumulation consists in assets of limited marketability and/or low value). Another problem is that the definition of public investment is open to criticism. A narrow definition tends to introduce a disputable bias in favor of brick-and-mortar spending at the expense of investment in human capital, but a broad definition may render the rule ineffective.

<!-- p. 209 -->

**Table 4.3**

Alternative fiscal rules

| Target variable | Pros | Cons |
| :--- | :--- | :--- |
| Public debt ratio | Direct link to sustainability<br>Easy to communicate and monitor | Can be pro-cyclical (especially in low-inflation environment)<br>Debt-deficit relation can be affected by one-off developments |
| Financial balance | Clear operational guidance<br>Easy to communicate and monitor | Often pro-cyclical<br>May lead governments to cut growth-enhancing investment spending |
| Structural balance | Clear operational guidance<br>Good stabilization properties | Structural deficit is measured with uncertainty<br>Complex to communicate and monitor |
| Current balance (Golden rule) | Preserves incentive to invest | No direct link to sustainability<br>Often pro-cyclical<br>May favor brick-and-mortar spending |
| Primary balance | Easy to communicate and monitor in the context of sustainability concerns | Partial link to sustainability<br>Often pro-cyclical |
| Public expenditure (nominal or real) | Clear operational guidance<br>Easy to communicate and monitor<br>Good stabilization properties | No direct link to sustainability<br>Interferes with allocation decisions<br>May lead governments to substitute tax expenditures to spending |

Source: Adapted and expanded from Schaechter et al. (2012) and Fall et al. (2015).

Additionally, the focus on gross rather than net investment is disputable since only net investment benefits future generations.

In 2009, Germany replaced the golden rule by a tighter rule whereby net structural borrowing is limited to $0.35\%$ of GDP per annum for the federal government; the *Länder* will no longer be allowed to run any structural deficit starting in 2020. These limits on structural deficits may be violated only under exceptional events such as natural disasters or severe economic crises, in which case the government is required to provide an amortization plan to parliament. Under the new German rule, the cyclical component of the deficit also falls under close scrutiny, based on the same methodology as for the Stability and Growth Pact. Finally, any implementation deviation is recorded on a control account and must be netted out over time (see Bundesfinanzministerium, 2009).

<!-- p. 210 -->

Countries with a high public debt often choose to target the primary deficit, which is more directly under the control of the government as interest payments on the public debt depend on market-determined interest rates. So did, for example, Belgium, which adopted a primary surplus floor of 6% of GDP at the end of the 1990s. The adjustment programs that the IMF negotiates with countries in financial stress also include primary balance targets.

Standard deficit rules are not adequate for countries facing a high volatility of revenues, such as the commodity producers. For them, the issue is to ensure that temporary revenues arising from exceptional circumstances, such as commodity price booms are saved rather than spent. Furthermore, a major policy issue is how to allocate revenues from the exploitation of natural resources: Should they be assigned to the building of infrastructure and human capital, or rather be invested financially so that revenues from the corresponding assets benefit future generations, as Chile (a copper producer) and Norway (an oil producer) have decided (box 4.16)?

#### Box 4.16 Fiscal Rules in Chile and Norway

Chile and Norway are both commodity producers whose tax revenues are largely determined by the volume of sales and the price of the raw material they are endowed with. For this reason, they have adopted fiscal rules that aim at avoiding pro-cyclicality and at ensuring intergenerational fairness.

The Chilean rule adopted in 2001 specifies that actual government expenditure should be determined by cyclically adjusted revenues net of the target for the cyclical adjustment balance (Schmidt-Hebbel, 2012). There are two adjustments for the cyclicity of revenues: one, based on the output gap, for nonmining revenues, and one, based on the difference between actual and trend mineral prices, for mining revenues. Both are determined by independent committees. The second implies that commodity price windfalls are saved. They jointly imply that government spending is acyclical.

The Norwegian rule, also adopted in 2001, goes further. All revenues from oil extraction are transferred to the government's Oil Fund (officially called "Pension Fund Global"), which is managed by the central bank and invests on global financial markets. The Fund's assets amounted to €850 billion in mid-2017, about twice the Norwegian GDP, and it is one of the largest sovereign funds in the world. The return on invested capital is used to fund the structural, non-oil budget deficit. This is meant, as in Chile, to insulate fiscal policy from fluctuations in oil revenues, to make room for automatic stabilization, but also to ensure intergenerational fairness as oil reserves are expected to be depleted over time. A major concern for the Norwegian authorities was also to avoid the "Dutch Disease" often experienced by countries experiencing commodity booms, when the commodity sector crowds out the other industries.

<!-- p. 211 -->

**Experience with the Norwegian rule is regarded as positive:** the fiscal rule has given an anchor to policy, it has helped avoid pro-cyclicality, and it has preserved intergenerational fairness. Its application has not been without problems, however: because of the size of the fund and financial market volatility, year-on-year fluctuations of the real return are significant; furthermore, fluctuations in oil prices affect the expected real return path. While the Fund provides a major buffer, it does not fully insulate fiscal policy from the consequences of fluctuations on commodities markets (Norwegian Expert Commission, 2015).

<!-- end Box 4.16 -->

Several countries have adopted expenditure rules, either as a substitute or as a complement to deficit and debt rules. Such rules that limit discretion in the evolution of nominal or real public expenditures have desirable stabilization properties: they prevent governments from increasing spending in response to a temporary surge in revenues and from cutting it in a recession. Whereas expenditure rules do not by themselves take care of ensuring sustainability, they can be coupled with “debt brakes”, so that the expenditure target is set at a level that fosters convergence to a certain debt level in the medium term (see Bénassy-Quéré et al., 2018, for an application to the euro area).

#### b) Fiscal institutions

Many governments, especially in Europe, value the disciplining character of a rule and are convinced that its advantages exceed its disadvantages. Yet all rules have shortcomings. When economic conditions change, sticking to the rule can lead to suboptimal policies: for example, there is no reason why the target for the financial balance should remain unchanged irrespective of lasting variations of the long-term interest rate. But departures from the rules or changes in the rules undermine their credibility. And to make room for particular situations results in complexity (the 2017 *vade mecum* on the EU Stability and Growth Pact is already 224 pages long).

In a landmark article, Wyplosz (2005) observed that the quest for an ideal budgetary rule was reminiscent of the quest for an ideal monetary rule in the 1980s. As far as monetary policy is concerned, this quest proved to be elusive, and the eventual response was to endow well-designed, specific institutions with the responsibility of independently setting interest rates. Building on this precedent, he advocated that an independent fiscal policy committee be in charge of fixing annual fiscal balance targets, leaving to government and parliament full discretion as regards the level and composition of revenues <!-- p. 212 --> and expenditures. The yearly fiscal balance targets would be set ahead of the budget preparation process so that the committee would be in charge of the macro stance and political government of the micro choices.

The proposal was not taken up by EU governments and is unlikely to be applied any time soon: the choice of a fiscal balance is too political and it involves, indirectly at least, too many distributional choices to be delegated to an independent institution (see box 2.13 of Chapter 2). However, several countries have put in place *independent fiscal councils* that do not have decision-making power but provide real-time assessments of the macroeconomic underpinnings and adequacy of the draft budget. In 1945, the Netherlands was the first country to introduce such an institution. At end-2016, the IMF reckoned that 39 countries were equipped with fiscal councils (Debrun, Zhang, and Lledo, 2017). Their mandates, however, vary widely (Fall et al., 2015): in Austria, for example, the council is in charge of preparing economic and budgetary forecasts, of assessing compliance with fiscal rules, and of providing long-term projections of the public debt; in France its mandate is confined to assessing the realism of the economic forecasts underpinning the budget and the medium-term fiscal plans; whereas in Germany, it includes the assessment of compliance with fiscal rules. In the United States, the Congressional Budget Office is responsible for forecasts, sustainability assessment, and the costing of measures submitted to Congress.

Even when their mandate is narrowly defined, fiscal councils improve the transparency of the budgetary process and help limit the government’s tendency to exploit its informational advantage to use budgetary policy for political ends. Broader mandates that include expenditure and revenue forecasts, the costing of policy measures, and debt sustainability assessments further constrain the government’s informational advantage while preserving its room for discretionary decisions.

According to Calmfors and Wren-Lewis (2011), fiscal councils are complements rather than substitutes to fiscal rules since they help monitor whether complex rules are actually respected and assess possible deviations. How to combine rules, independent oversight, and democratic decision-making is, however, a delicate issue. The United Kingdom provides a telling example of the subtleties this may imply (box 4.17).

Overall, empirical evidence suggests that fiscal frameworks—whether based on rules, or institutions, or a combination of both—are useful: the adoption of balanced budget rules tends to reduce the deficit, the coexistence of several rules (that target different variables) tends to reduce both the deficit and public spending, and the combination of rules and fiscal councils also has an effect (Fall et al., 2015). However, such estimates do not control for the endogeneity of the fiscal frameworks: it may well be that countries with a preference for fiscal discipline adopt such frameworks more often.[^31]


<!-- p. 213 -->

<a id="box-4-17"></a>

#### Box 4.18 Fiscal Rules and Institutions in the United Kingdom

*[Editorial note (anchor `box-4-17`): the book's box numbering slips here. This box is printed "4.18" (p. 213) but the text on p. 212 calls it box 4.17; the euro-area box (p. 219, anchor `box-4-18`) is also printed 4.18 and the p. 219 text calls it 4.18; the p. 207 text sends the reader to "box 4.19" for the European framework, while the box printed 4.19 (p. 222, anchor `box-4-19`) covers the US states, as the p. 221 text correctly says. Printed labels are kept; use the anchors for cross-references.]*

Fiscal rules were first introduced in the United Kingdom in 1997 by Gordon Brown, then chancellor of the Exchequer in Prime Minister Tony Blair’s first government. The government committed itself to abiding by the *golden rule* of public finances, which required the public sector to borrow only for public investment, and the *sustainable investment rule*, which required the government to ensure that public debt at the end of the economic cycle would not exceed 40% of GDP. The golden rule was met until the global financial crisis, but the sustainable investment rule was arguably only met because the government’s own assessments relied on excessively favorable medium-term economic forecasts. It was suspended in the wake of the crisis.

The fiscal framework was reformed in 2010 under PM David Cameron and Chancellor George Osborne in the context of an acute post-crisis worsening of the fiscal situation. The government set two new targets, first to bring the structural deficit below 2% of GDP and, second, to put, by 2020–21, the public debt ratio on a declining path. They also created a new independent institution, the Office for Budget Responsibility (OBR).

The OBR has no role in setting the rules, which belong to the remit of the government. But it is in charge of (1) producing the economic and budgetary forecasts that accompany the government’s budget statements, (2) assessing whether the government has a greater than 50% chance of meeting its targets, (3) assessing the long-term sustainability of public finances, (4) evaluating fiscal risks, and (5) scrutinizing the government’s costing of individual tax and welfare spending measures. To perform these tasks, the OBR has access to government departments and agencies, from whom it may commission specific forecasts. The OBR’s work involves significant interaction with the government, both at technical and political levels, but it retains the ultimate responsibility for its published assessments. Its methodologies are made public.

<!-- end Box 4.17 -->

### 4.3.2 Sovereign debt crises resolution

#### a) Context

As discussed in the first part of this chapter, sovereign states regularly experience insolvency crises and have to undergo a restructuring of their public debt. For several decades after World War II, such *sovereign debt crises* were deemed a sad privilege of developing countries. In 2011, Lorenzo Bini Smaghi, then a member of the board of the ECB, famously declared that a debt restructuring in Greece would be “like the death penalty which we have abolished.”[^32] A little more than year later, however, Greece reached agreement with its creditors


<!-- p. 214 -->

on a restructuring of its public liabilities that resulted in a debt forgiveness amounting to about €100bn in present value terms, or 50% of the 2012 GDP (Zettelmeyer, Trebesch, and Gulati 2013). Five years later, discussions on a further Greek debt restructuring, this time of the loans from the official sector, were again on the agenda. In the meantime, Ireland, Portugal, and Cyprus had lost and regained market access.

In most countries, a company that is unable to meet a financial obligation enters negotiation with its creditors within the framework of legal provisions that protect the rights of the various stakeholders (essentially creditors, shareholders, and employees) and provide a venue for negotiation, while temporarily ensuring the continuation of operations. Rather than seize the debtor’s assets and liquidate the company, it is in the collective interest of creditors to aim at a settlement that preserves as much as possible the value of their claims—which implies that the company is offered a chance to reorganize. Individually, however, each creditor has an interest in being reimbursed as fast as possible. Such a “grab race” is against the creditors’ common interest. This contradiction signals a collective action problem that bankruptcy procedures aim at solving.

In the United States, these procedures are governed by what is called “Chapter 11” of the Bankruptcy Code. It permits the debtor to remain in control of its business as a “debtor in possession” under the control of the courts until a settlement is reached. In the meantime, the procedure ensures a standstill on litigations: it prevents “any act to collect, assess, or recover” a claim against the debtor that arose before its commencement. At the end of the procedure, the company may be liquidated, be taken over, or resume normal business operation after reorganization and financial settlement. For example, American Airlines operated under Chapter 11 between end-2011 and end-2013.

The idea of applying bankruptcy principles to sovereign states goes back at least to Adam Smith. But it is since the Mexican crisis of 1982 that a “Chapter 11 for sovereign states” has been a matter for policy discussions.[^33] It was first proposed by then-Harvard economist Jeffrey Sachs (1995) and taken up a few years later in a proposal by the IMF (Krueger, 2002). The idea suffered considerable pushback, however, from the financial industry and it failed to be adopted. Agreement was only reached on the inclusion in foreign currency–denominated sovereign bonds of collective action clauses (CACs) that make it possible for bond holders to decide on a settlement with the debtor by qualified majority.

The issue reemerged in the context of the European debt crisis after Chancellor Merkel of Germany and President Sarkozy of France agreed in October 2010 in a meeting in Deauville that financial assistance to euro area members would only be provided to solvent countries. Those deemed insolvent would first need to agree on a restructuring with their creditors. To this end, collective action clauses would be introduced in all new euro-denominated bond contracts from 2013 onward.

The Deauville agreement elicited considerable criticism, first for having acknowledged the possibility of sovereign insolvency in the euro area and, second, <!-- p. 215 --> for sending a confusing message about future restructuring and the relative treatment of old and new creditors. It was subsequently watered down: the 2012 Treaty establishing the ESM only mentions the need to assess whether the public debt of a country that applies for assistance is sustainable, without spelling out the consequences of this assessment. It largely subcontracts the debt sustainability assessment to the IMF (“Wherever appropriate and possible, such an assessment is expected to be conducted together with the IMF”; Article 13.1.b of the ESM Treaty). This has strong implications because access to Fund lending requires that the country’s debt is assessed sustainable “with a high degree of probability.” If it is not the case, IMF policy prescribes prior debt restructuring—as it did for Greece in 2015–2017, with the consequence that disagreements between the Fund and European institutions contributed to a protracted impasse in negotiations with the Greek authorities[^34].

#### b) Issues in the design of sovereign restructuring procedures

There are three main issues that a procedure for sovereign debt restructuring must address. The first is the need to set the incentives right for all parties. Debt restructurings are repeated games: each step in a country’s negotiation with its creditors and each decision by a court are carefully scrutinized by other debtors and creditors because they create precedents. It is important that debt restructurings do not violate the creditors’ rights, that they are not excessively delayed, and that they do not impose unnecessary hardship to the population. To make restructuring too costly for the debtor country would not only involve welfare costs for the citizens, it could also lead to postponing it excessively and, ultimately, it could reduce the country’s ability to repay[^35]. But to make it too easy would give an incentive for governments to overborrow, and it would give to creditors an incentive to impose high default risk premia. This is why the institutional set-up should be designed to help find the right balance between conflicting interests (Buchheit et al., 2013).

The second issue arises from the collective action problem created by the multiplicity of lenders. In the 1980s, when lenders were a few international banks, the problem was relatively easily to solve: negotiations could take place with all major banks simultaneously, and authorities such as the IMF and national supervisors could apply moral suasion. From the 1990s onward, the development of disintermediated borrowing made the situation radically different: bonds are now bought by a variety of investment funds and even private individuals; furthermore, they are continuously traded, with the consequence that the identity of creditors changes over time. The problem is meant to be addressed by the introduction of collective action clauses in the bond contracts, but difficulties remain, especially as majority rules only apply to the holders of a particular bond issuance. The combination of separate bonds contracts and a legal obligation to treat all borrowers equally (this is called the *pari passu* clause) involves considerable procedural hardship.

<!-- p. 216 -->

The third issue results from the peculiarities of sovereign borrowing. As discussed already in Section 4.1 of this chapter, sovereign debt is less enforceable than private debt because there is little collateral that can be seized by creditors: most assets are located inside the national borders, and assets held abroad are often protected by sovereign immunity. This makes it possible for a debtor to walk away and suffer little more than reputational damage. At the same time, the fact that states are infinitely long-lived implies that their debts are not easy to get rid of: until a settlement is reached, creditors retain the legal right to insist on repayment. Companies can go bankrupt and their owners can start a new business. But, absent an agreement with its creditors, there is no such thing as a fresh start for a sovereign borrower.

Since the 1990s onward, the problem has been made more acute by the emergence of so-called *holdout funds* that buy sovereign debt at distressed prices on the secondary market and specialize in suing the sovereign to obtain full repayment. Argentina in the 2000s lost its legal battle against holdouts, as a US federal judge (bonds had been issued under US law) prohibited negotiated repayment to the 93% of creditors that had agreed on restructuring unless the holdout creditors were repaid in full. The ruling, which was based on an extreme interpretation of the *pari passu* clause, forced the Argentine government to agree in 2016 on settling the lawsuit initiated by the holdouts.

Hopes that a statutory solution to these issues could be found through the creation of an international bankruptcy court, or more modestly what the IMF once called a *sovereign debt restructuring mechanism* (SDRM) whose decisions would be binding for all parties involved, were abandoned in the early 2000s and are unlikely to be revived in the context of suspicion for multilateralism that has developed since the mid-2010s.

Initiatives for mitigating the holdout problem have rather been based on provisions ensuring better consistency in the treatment of bond series. With conventional collective action clauses as initially introduced, a debtor seeking a settlement with its creditors needed to obtain the agreement of a qualified majority of them for each bond series. This made it possible for holdouts to concentrate their purchases on the smaller series and block the restructuring. This is why the International Capital Market Association, a self-regulatory body, issued in 2014 model clauses that make decisions by a supermajority of all bondholders binding on the holders of any particular series. The generalization of such “onelimb” CAC clauses would eventually eliminate the holdout problem (Gelpern, 2014). However, they are not mandatory and will at any rate spread gradually only as their introduction affects new issuances, not the outstanding debt stock.

#### c) Debt crises resolution in the euro area

The issue of sovereign debt crisis resolution within the euro area arose when Greece proved insolvent. It involves three peculiar features.

First, the bulk of public debt is issued under national law instead of foreign law, as it is the case for emerging countries. This makes it possible for a state to set by itself the terms of the restructuring, as Greece did in 2012: parliament <!-- p. 217 --> passed a law stating that if holders of two-thirds of the Greek law-governed bonds approved a restructuring, the result would apply to all bondholders (Zettelmeyer et al., 2013). It is to be noted that Greece did not use its legal powers to change unilaterally the value of its sovereign bonds, but rather to make the outcome of the negotiation with a supermajority of the creditors binding on all of them.[^36]

Second, public debt is partially held by public entities—the central bank as a consequence of its bond purchase program or the ESM and the IMF as a consequence of their lending. In the case of Greece, by mid-2017, more than two-thirds of government debt was owed to official creditors. For this reason, but also because of the precedent it would set for other countries, restructuring is subject to quasi-statutory procedures. Between 2015 and 2018, the issue of a second Greek restructuring (called for by the deteriorating economic situation and the consequences of domestic deflation on the debt ratio) was the matter for permanent discussions within the Eurogroup of finance ministers. Furthermore, two major official creditors insisted that they should not take part in any restructuring: the IMF because of its preferred status and the ECB because it claimed that this would violate the prohibition of monetary financing.

Third, the importance of sovereign bonds in the balance sheets of the banks makes sovereign restructuring even more delicate: in compliance with the post-crisis regulatory standards, a loss on the banks’ sovereign bonds portfolio would have to be borne by their shareholders and creditors. Alternatively, the banks would need to be recapitalized by the defaulting state, as was done in Greece. However, this was one of the channels of the banks-sovereign “doom loop” that threatened stability in the euro area, especially since domestic sovereign bonds were massively used to get refinancing from the Eurosystem, but with varying haircuts (see Chapter 5 and Chapter 6).

Whether or not principles for eventual debt restructuring should be spelled out in the euro area remains a divisive and fiercely debated issue. Part of the policymaking community, especially in France and southern Europe, strongly advocate retaining a significant enough degree of ambiguity to make room for case-by-case, discretionary decisions, and it has rejected academic proposals for a policy framework that would make debt restructuring a possible, if last-resort option (Bénassy-Quéré et al., 2018).

### 4.3.3 Fiscal policy in the euro area

Many fiscal policy issues are common to all advanced countries. The euro area, however, stands apart: it is the only monetary union that is not equipped with a central (or, equivalently, federal) budget. This has two major consequences. First, in times of financial stress, governments cannot rely on having access to the financing of their national central banks, which strengthens (or at least should strengthen) *ex ante* fiscal discipline but also makes states more fragile *ex post*; although euro area states borrow in their own currency, market constraints <!-- p. 218 --> resemble those faced by those that borrow in a foreign currency. Second, the absence of both national monetary policies and a common budget puts the burden of stabilization on national fiscal policies. There is therefore a built-in tension between the fiscal prudence inherent to participating in a monetary union and the demand for fiscal activism resulting from the lack of other stabilization instruments. In principle, the solution to this conundrum is to equip the union with credible fiscal rules that provide sufficient room for maneuver in downturns. This was the principle underpinning the Maastricht system, but implementation has proved to be fraught with considerable difficulty.

The problem is best illustrated by a comparison with the United States, where states know that they cannot rely on being bailed-out by the Federal Reserve or the federal government but can abstain from playing a part in macroeconomic stabilization because this role belongs to the remit of the federal government. The US government contributes to cushioning both state-specific shocks (through the automatic stabilizers and discretionary action) and country-wide shocks (through automatic stabilizers and discretionary action).

In what follows, we present and discuss in turn fiscal discipline, fiscal federalism, and fiscal policy coordination.

#### a) Fiscal discipline

The main argument for fiscal discipline in a monetary union is that spillovers from fiscal imprudence are large. When Greece found itself on the verge of bankruptcy in 2010, banks in other member countries that held Greek debt in their portfolio were affected, and states in weak fiscal positions suffered from contagion as market participants started to worry about sovereign risk in the euro area.

It is precisely to prevent such risks that fiscal discipline has been, since its inception, a key tenet of the EMU (see Eichengreen and Wyplosz, 1998). The Maastricht Treaty precludes public securities being directly purchased by central banks on the primary market where they are initially issued (which is of little effect as it does not prohibit buying them on the secondary market where they are subsequently traded). However, the central bank's policy can be affected even if it does not purchase any bond from sovereigns in trouble. A government that faces difficulty tapping financial markets tends to borrow through short-term instruments (because private investors are reluctant to lend long term for fear of default), and the central bank may soon face a dilemma: either it brings the government to the brink of a failure through a relatively high interest rate, or it departs from its price stability mandate and sets a low interest rate to preserve the government's capacity to pay. The central bank can also be led to intervene in the name of financial stability, as banks that hold debt of a struggling government (most frequently the banks headquartered in the same country) themselves face difficulty accessing the market and are soon forced to rely on ECB liquidity (see Chapter 5).

One of the defining features of the euro area crisis of 2010–2012 was indeed the strong correlation between the risk premia affecting sovereign and banks. It was visible on bond markets as well as in the market for credit default swaps.

<!-- p. 219 -->

where bond holders can get an insurance against a possible default. This correlation, which could not be observed in the United States or other countries when banks were under severe financial stress, was indicative of the fragility of the monetary union (see Chapters 5 and 6).

There are basically two ways to address this problem. One, adopted in the EU, is to monitor and enforce fiscal discipline so that no state finds itself in a situation where its solvency can be put in question. This is the purpose of the “avoidance of excessive deficits” and the possibility of levying fines on states in breach of fiscal rules enshrined in the Maastricht Treaty of 1992, as well as of the secondary legislation built on its basis. Over the years, the EU has put in place an elaborate apparatus of fiscal rules and procedures whose aim is to enforce fiscal discipline while at the same time leaving some room for stabilization action at the national level (see box 4.18).

<a id="box-4-18"></a>

#### Box 4.18 Fiscal Rules and Procedures in the Euro Area

During the negotiation of the European Economic and Monetary Union in the early 1990s, it was agreed that Member States must avoid “excessive deficits” (Article 126 of the Treaty on the Functioning of the EU) and should face sanctions if this discipline went unobserved. Reference thresholds of 3% of GDP for the deficit of the general government and 60% of GDP for gross public debt were defined and laid down in the protocol on the excessive deficit procedure annexed to the Treaty. However, the Treaty did not specify the procedure for implementing sanctions.

On the eve of the introduction of the euro, Germany demanded that the fiscal discipline commitments and procedures be detailed. The resulting Stability and Growth Pact includes:

*   **A preventive arm.** Each Member State is to adopt a medium-term objective for its cyclically adjusted budgetary position that is consistent with the overall objective of being close to balance or in surplus and leaves room for stabilization of normal cyclical fluctuations without breaching the 3% threshold. It prepares a three-year stability program that is updated every year and is submitted to the assessment of the Commission and to the approval of the Eurogroup of finance ministers. The program describes the adjustment path toward the medium-term objective, taking as a benchmark a 0.5 percentage point improvement in cyclically adjusted terms per year.
*   **A corrective arm.** Except if “exceptional and temporary,” the headline (financial, i.e., noncyclically adjusted) fiscal deficits of Member States should never exceed 3% of GDP. When the deficit threatens to reach, or exceeds, the 3% threshold, a specific surveillance procedure (the excessive deficit procedure) is set in motion according to a <!-- p. 220 --> predetermined timetable of increasing pressures: Steps include early warning, identification of an excessive deficit, recommendation to implement corrective actions, obligation to make a non-interest bearing deposit with the Commission, and conversion of the deposit into a fine. The eventual fine includes a fixed component of 0.2% of GDP and a variable component linked to the size of the deficit, within an annual limit of 0.5%.

Corresponding decisions are made by the Eurogroup (i.e., the group of the finance ministers of the euro area), on the basis of recommendations by the European Commission.

After extensive criticism of the SGP, the failure of several member states to comply with it, and a subsequent 2003 decision by the Eurogroup to put the pact “in abeyance” instead of simultaneously stepping up its corrective procedures against France and Germany, a substantial reform of the SGP was adopted in 2005. The goal was to “enhance the economic rationale of the budgetary rules to improve their credibility and ownership”. In addition to an emphasis on cyclically adjusted balances instead of headline balances, the medium-term budgetary objective (MTO) of keeping the budget “close to balance or in surplus” was replaced by individual MTOs that recognize the specific economic characteristics of each Member State.

In 2010–2011, the euro area crisis prompted a reexamination of the system of fiscal rules. Neither for Greece (because it had cheated) nor for Ireland or Spain (where the problem came from banks) could the crisis be attributed to a breach of the rules, but the focus was nevertheless on strengthening the fiscal framework. Changes included:

- A new set of legislative provisions (the six-pack) that redefined decision procedures, made earlier sanctions possible, introduced a debt reduction criterion alongside the deficit criterion, and mandated the creation of national fiscal councils.[^b4-18b]
- Another set of legislative provisions (the two-pack) that aimed at strengthening the *ex ante* monitoring of budgetary decision. It makes it possible for the Eurogroup to request that a country reconsiders a draft budget deemed in infringement of the rules.
- A new Treaty (the Treaty on Stability, Coordination, and Governance—TSCG) that gives stronger legal status to the main provisions of the six-pack and mandates the adoption in each member country of a binding, preferably constitutional balanced budget rule limiting the structural deficit to 0.5% of GDP (unless public debt is below 60% of GDP, in which case the threshold is set at 1% of GDP). The fiscal provisions of the TSCG (or *fiscal compact*) also commit all euro area members to supporting Commission recommendations as regards a


<!-- p. 221 -->

country in breach of the deficit criterion, unless there is a qualified majority to reject them. This provision amounts to changing the voting rule for recommendations from qualified majority to reverse into the sanction procedure.

It was meant to introduce a dose of automaticity into the sanction procedure.

In 2015, the European Commission issued a recommendation emphasizing that the existing rules leave room for flexibility in implementation, especially for countries willing to undertake investments or structural reforms (European Commission, 2015).

The alternative approach is to rely instead on market discipline. In this model, states do not behave prudently because they are instructed to behave, but because they know that no one will come to their rescue if they lose market access, hence the interest rate on their debt reflects their fiscal position. Such market discipline requires that the threat of letting a state default be credible, which in turn necessitates that the financial system be protected from the fallout of a state bankruptcy. This is basically the solution adopted in the United States, where, for nearly two centuries, the federal government has consistently refused to bail out insolvent states (box 4.19).

The euro area has gone as far as it could go in the direction of monitoring and directing the individual Member States’ fiscal behavior through a set of rules and procedures—short of what former ECB president Jean-Claude Trichet (2013) once called “federalism by exception”: direct administration by the EU institutions of a country unwilling to abide by its fiscal commitment and whose behavior threatens the stability of the euro area as a whole. The fiscal framework nevertheless suffers from a series of shortcomings (see, for example, Bénassy-Quéré and Ragot, 2015; Pisani-Ferry, 2015):

* Procedures are excessively complex and ownership by national decision-makers is often lacking;
* Enforcement mechanisms are weak and the credibility of sanctions is questionable;
* The benchmarks of the reformed Stability and Growth Pact are based on unobservable variables, such as the structural deficit, whose measurement is open to controversy;
* The adequacy of the fiscal recommendations that result from the implementation of the rules is questionable from a macroeconomic standpoint;

[^b4-18a]: See the Presidency Conclusions of the March 22–23, 2005, European Council, Annex II.

[^b4-18b]: The Six-Pack also introduced a procedure for the prevention and reduction of current account imbalances (it is called the *macroeconomic imbalances procedure*).

<!-- end Box 4.18 -->

<!-- p. 222 -->

The framework does not provide sufficient incentives to investment and growth-enhancing reforms; flexibilities introduced to leave room for intelligent assessment opened the door to undue politicization.

The alternative of relying on market discipline, as in the United States, would, however, raise a host of new issues, if only because the debt of US states, even the largest ones, is an order of magnitude lower than that of the major euro area countries. First, it would require establishing procedures to restructure sovereign debts. Second, it would require national banking systems be

<a id="box-4-19"></a>

#### Box 4.19 The States' Fiscal Regime in the United States

The US federal system went through an early test of the fiscal rules of the game in the immediate aftermath of the War for Independence.[^b4-19a] The war effort had left individual states heavily indebted, and some were effectively bankrupt. A fierce debate on the treatment of the public debt followed, with on one side the Secretary of the Treasury, Alexander Hamilton, who argued that because debt had been incurred for a common purpose it had to be assumed by the newly established federal government, and on the other side Thomas Jefferson, the Secretary of State, who opposed debt mutualization. In the end Hamilton prevailed: the debt was transferred to the federal government and swiftly restructured; states were charged on a per capita basis so that the burden of the revolutionary war would be distributed evenly.

A consequence of this early episode was that a precedent was set, whereby the federal government would bail-out insolvent states. Moral hazard was therefore substantially present, until eight states that had over-borrowed to finance infrastructure defaulted in 1840. British and Dutch creditors, who held the bulk of the debt, argued that the federal government's guarantee, while not explicit, had been implied. In the event of a default, another war with Britain was regarded a possibility. However, Congress rejected the assumption of state debt, thereby establishing a new 'no bail-out' norm.

The norm was upheld in the aftermath of the Civil War, through a wave of local defaults in the 1930s, and again on the occasion of a series of municipal bankruptcies in the 1970s. The only exception regarded the District of Columbia, arguably not an ordinary state, whose government was taken over by Congress in the 1990s.

A consequence of the establishment of a no bail-out norm has been the adoption by individual states of balanced-budget rules: the first wave took place precisely in the 1840s after Congress rejected debt assumption.

[^b4-19a]: This box is based on Henning and Kessler (2012).

<!-- end Box 4.19 -->

<!-- p. 223 -->

protected against the fallout of state insolvency, especially through regulatory incentives to diversify sovereign bond holdings and the creation of a euro area safe asset (see Chapter 6 for details). Third, a fiscal capacity of significant enough firepower to ensure stabilization at the federal level would need to be created (see the discussion in the next section). Proposals along these lines to introduce a modicum of market discipline together with risk-sharing and a fiscal capacity were put forward by French and German academics (Bénassy-Quéré et al., 2018) but they were not endorsed by euro area member states.

#### b) Fiscal federalism

In federal states, the macroeconomic stabilization function is generally assigned to the federal level, while individual states are often subject, sometimes by their own will, to strict fiscal discipline. In the United States, when a state undergoes a negative income shock, its residents pay lower federal taxes but continue benefiting from federal spending (on public goods, transfers, etc.). The federal budget therefore functions as an automatic shock absorber. An early paper by Sachs and Sala-i-Martín (1992) found that up to 30–40% of economic shocks that affect the states are absorbed by the federal budget. This evaluation has been debated, and the current consensus is rather around 10–30% (European Commission, 2016), which is still non-negligible (see the methodology in Chapter 7, box 7.7). Furthermore, a federal budget tends to encourage labor mobility (through the portability of social entitlements) and capital mobility (through financial integration). In the United States, both channels are more stabilizing than the tax transfer channel (see Chapter 7, box 7.7).

In the euro area, the choice not to supplement the single currency with a federal budget was initially made for political reasons: monetary union was already a significant step toward a European federation, and that was the limit of what governments and public opinion could accept. Furthermore, as public spending is already high, the creation of a federal budget would have required transferring budgetary functions from the national to the European level (rather than the initiation of new functions at the federal level, as was the case in the United States). Whereas the MacDougall report of 1977, an early blueprint for EMU, had envisaged a federal budget of the order of 5–10% of GDP, as indicated in Chapter 3, monetary union was initiated without any federal fiscal leg. It was assumed that fiscally prudent Member States would retain sufficient stabilization power to be able to offset adverse economic developments, either individually in the case of country-specific shocks or jointly in the case of common shocks.

In 2012, the “Four Presidents’ Report” prepared jointly by the heads of the main European institutions, including that of the ECB in the aftermath of the sovereign debt crisis mapped out the future of the euro area (Van Rompuy et al., 2012) and floated the idea of a fiscal capacity that would “contribute to cushioning the impact of country-specific shocks and help <!-- p. 224 --> prevent contagion across the euro area and beyond.” The notion of a fiscal capacity was voluntarily kept fuzzy: it could mean a proper budget; an insurance fund designed to supplement cyclically sensitive components of national public spending, such as unemployment insurance; or a system of purely macroeconomic cyclical transfers based on relative deviations from potential output.

The key requirements for establishing such a mechanism is that it should have strong enough stabilization properties but no distributional bias. In other words, all countries should be able to receive net transfers in a downturn, but none should benefit from permanent transfers. Meeting these two goals at the same time is not easy: for example, topping up national unemployment insurance with a euro area component would result in permanent net transfers to the countries where structural unemployment is the highest. It would therefore result in subsidies from countries whose educational, labor market, and product market are efficient to countries where the same policies are inefficient. Solutions to address the problem do exist, for example, through the setting up of an unemployment reinsurance scheme that would only cover large temporary shocks (Bénassy-Quéré et al., 2018), but they raise delicate design issues. Furthermore, any proper euro area budget would need resources and would have to be enshrined in an institutional framework that ensures proper democratic accountability to a parliamentary body. The European parliament at present has no taxing power and no euro area chamber has been created within it.

Fears of a “transfer union” that would involve large and permanent transfers from Northern European states to Southern European ones have resulted in considerable caution, especially on the part of Northern Europe countries, toward projects for a fiscal capacity or a euro area budget.

#### c) Policy coordination

As discussed in Chapter 3, economic literature traditionally identifies two major reasons for nations to coordinate economic policies. The first, already discussed, is the provision of the international public goods that decentralized action will in general fail to produce. The second relates to the suboptimality of uncoordinated decisions in the presence of externalities, even for the pursuit of predominantly national objectives.

These two reasons apply in Europe and especially in the euro area. First, safeguarding financial stability can be viewed as an EU-wide public good. This justifies the prevention of unsustainable budgetary positions unless procedures are in place that protect the banking system against the fallout from sovereign bankruptcy.

Second, as noted in Section 4.2 of this chapter, participation in the monetary union gives rise to specific fiscal policy externalities (box 4.20).

<!-- p. 225 -->

#### Box 4.20 Fiscal Policy Spillovers Within a Monetary Union

Suppose two identical countries called A and B form a monetary union (U), and let us represent the equilibrium in the Mundell-Fleming diagram as in box 4.15. The three panels in figure B4.20.1 represent, respectively, equilibrium in country A, in country B, and in the monetary union U. The single interest rate is determined by the intersection of the IS and LM curves at the level of the Union (point E). The equilibrium in each country is then determined by the country-specific IS curve, given the single interest rate.

Now let us assume that country A carries out an expansionary fiscal policy, bringing its IS curve to the right. The IS curve of country B also moves (but to a lesser extent) toward the right because it benefits from increased exports to country A. The aggregate IS curve for the whole monetary union also shifts to the right. The common interest rate increases. Country B profits from increased exports, but suffers from a higher interest rate (equilibrium at E").

If the interest rate externality dominates, country B is likely to react with an expansionary fiscal policy. Output will then increase but at the price of a higher budget deficit, while a fall in the interest rate would have benefited the country's public finance.

Depending on the pair of countries involved, either the interest rate channel or the trade one dominates (see Bénassy-Quéré and Cimadomo, 2012). The externality involved in the latter case is being addressed by the fiscal discipline framework. There is no specific procedure to address the other one. This means that, short of ad hoc policy coordination, each country feels little incentive to implement a stabilizing fiscal expansion.

**Figure B4.20.1 Impact of a fiscal expansion in a monetary union.**

*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* The figure displays three panels showing the impact of a fiscal expansion in a monetary union. The left panel shows Country A with an IS curve shifting right due to fiscal expansion, moving from point E to E'. The middle panel shows Country B where the IS curve also shifts right but less than Country A, reflecting increased exports and higher interest rates, moving from point E to E'. The right panel shows the Union U with the aggregate IS curve shifting right, resulting in a higher common interest rate and output increase at point E'.

<!-- end Box 4.20 -->

<!-- p. 226 -->

An expansionary fiscal policy in one country creates a positive demand external- ity for the other members but—if the central bank responds by raising the interest rate—a negative interest-rate externality. This second, different justification for mutual surveillance of national budgetary policies was formalized early on by Beetsma and Bovenberg (1999) and identified as a rationale for common fiscal rules.

Should fiscal policies be coordinated to ensure that the aggregate fiscal stance of the euro area is adequate? As discussed earlier, the Mundell-Fleming model, under flexible exchange rates and perfect capital mobility (these assumptions are normally correct for the euro area as a whole) leads to the conclusion that fiscal policy is ineffective;[^37] the task of stabilizing the economy of the euro area accordingly falls primarily on monetary policy and the coordination of fiscal policies to stabilize output appears to be a second-best solution ranking below monetary policy. This conclusion must be questioned when monetary policy is constrained by the zero lower bound: the response to an adverse demand shock relies on fiscal policy, and, absent a coordinated stimulus, the combined policy reactions of individual Member States are bound to be inadequate (Draghi, 2014).

This discussion leads to the following policy assignment rule:

* The common monetary policy should respond to shocks affecting the whole area (symmetric shocks).
* National fiscal policies should respond to country-specific shocks or shocks affecting a group of countries in relation to others within the area (asymmetric shocks);
* Aggregate euro area-level fiscal policy may be called upon to complement monetary policy when the latter proves ineffective or insufficient, especially when the policy rate is at the zero lower bound.

The European institutional framework barely upholds this policy assignment. Whereas fiscal discipline is enshrined in the Stability and Growth Pact, fiscal coordination only rests on an interpretation of the very general clause of Article 121.1 of the Treaty on the functioning of the EU, according to which Member States “regard their economic policies as a matter of common concern and shall coordinate them within the Council.” Attempts to monitor the aggregate fiscal stance of the euro area and to strengthen coordination through the so-called European semester have been facing a harsh reality: national governments are accountable to national parliaments and, ultimately, national citizens only.

### 4.3.4 Conclusion: Old and New Views on Fiscal Policy

As noted already, the consensus on the role of fiscal policy has varied radically in recent decades. From the activism of the 1970s, when President Richard Nixon famously said “We are all Keynesian now” to the nona <!-- p. 227 --> consensus of the late twentieth century, and then to the post-2008 revival, changes have been wide. Divergences over the role of fiscal policy also have a spatial dimension: for decades, Germany has been the staunch advocate of fiscal discipline, whereas the United States has repeatedly called for making use of the fiscal lever.

The nonactivist consensus of the late twentieth century was well summarized in the already mentioned John Taylor (2000) paper. The core of his argument was that monetary policy dominates fiscal policy for stabilization purposes because its implementation lags are shorter and because it is nimble (the central bank can change course more easily than a parliamentary chamber). Furthermore, using monetary and fiscal policy in parallel and to the same end would complicate rather than facilitate the task of the central bank, because it would need to figure out what will be the reaction of the fiscal authorities. Further critics such as Martin Feldstein (2002) added that “deliberate ‘countercyclical’ discretionary fiscal policy has not contributed to economic stability and may have actually been destabilizing at particular times in the past.”

Fifteen years later, this view was still largely dominant in Europe, but the US consensus had reverted to activism. Jason Furman (2016), who was Chairman of the Council of US Economic Advisers under President Obama, contrasted the “old view” and the “new view” of the role of fiscal policy (table 4.4).

As developed in this chapter, which view is right at a given moment in time is largely a matter of macroeconomic conditions. The “old” view represented the consensus at a time when aggregate fluctuations were moderate (what Olivier Blanchard and John Simon, 2001, termed “The Great Moderation”) and when economic cycles were largely asynchronous, while long-term interest

Table 4.4

“Old” and “new” views on the role of fiscal policy

| | “Old” view | “New” view |
|---|---|---|
| Effectiveness | Limited by negative side effects (crowding-out of private investment) | Can be very effective (and even crowd in private investment) |
| Stabilization role | Normally dominated by monetary policy (except at zero lower bound) | Complement to monetary policy (especially at zero lower bound) |
| Fiscal space | Scarce. Hence, priority should be long-run fiscal balance | Larger than appreciated when real interest rates are low. Stimulus can be combined with long-run consolidation. |
| International coordination | Generally unnecessary | Can be effective |

Source: Adapted from Furman (2016).

<!-- p. 228 -->

rates were positive in real terms. The “new” view represents the consensus of a time when aggregate fluctuations are ample and synchronous, equilibrium real interest rates can be negative, and deflationary pressures weaken the effectiveness of monetary policy while threatening economic stability. If lasting, such changes in economic conditions must affect the prevalent view on economic policy and the institutions that underpin policymaking.

## Notes

[^1]: Data mentioned in this paragraph are from the International Monetary Fund’s *Public Finances in Modern History Database*. See Mauro et al. (2013).
[^2]: In Europe, collective schemes that provide unemployment, health, and old-age insurance are generally grouped under the heading *social security*, whereas in the United States, social security designates old-age insurance only.
[^3]: This finding holds after controlling for the biases in the estimation arising from the fact that, as argued by Rodrik (1998), countries facing more aggregate fluctuation risks (because of their geographic or sectoral specialization) may have developed an endogenous preference for larger governments. See Galí (1994), Fatas and Mihov (2001), and Debrun, Pisani-Ferry, and Sapir (2010).
[^4]: There are other ways to finance deficits. For example, poor developing countries also finance their deficits through receiving grants. Another possibility, the consequences of which are discussed later and in Chapter 5, is for the government to receive loans from the central bank.
[^5]: Source OECD, *Government at a Glance* data, 2017.
[^6]: Sovereign wealth funds have been established to this end. Examples include Singapore (Government of Singapore Investment Corporation, or GIC) and Norway (where oil income is invested in the Government Pension Fund of Norway). See Box 4.16.
[^7]: As discussed in the following sections, the interest rate cannot be regarded as independent from the debt level. For example, the large primary deficit of Greece in 2009 (8% of GDP) triggered a rise in the risk premium that worsened the outlook of its public finances.
[^8]: The concept of “original sin” was introduced by Eichengreen, Hausman, and Panizza (2005).
[^9]: Source: Privatization Barometer 2013–2014, KPMG and ENI-Enrico Mattei Foundation.
[^10]: The G20 includes the largest economies globally. It began meeting at heads of state and government levels in 2008, in response to the global crisis. It holds annual meetings.
[^11]: See the communiqué of the leaders’ meeting on www.g20.utoronto.ca/summits/2009london.html
[^12]: Source: European Commission, AMECO database.
[^13]: Source: European Commission, AMECO database.

<!-- p. 229 -->

[^14]: England however defaulted in the fourteenth century, as did individual U.S. states in the nineteenth century.

[^15]: There are examples of states that wind up and close their books, but legacy debt is then carried over to newly established countries. For instance, Czechoslovakian debt was split between the Czech Republic and Slovakia on January 1, 1993. There are also examples of governments that refuse to pay for their predecessors' debt because they deem it politically illegitimate. This famously happened after the Russian and Chinese revolutions. It has been proposed, as a form of sanction, to formally declare debts incurred by illegitimate dictatorship *odious debt*. But since political regime change cannot usually be foreseen, it is difficult to integrate it into *ex ante* sustainability analysis.

[^16]: To be more precise, they can seize some of its foreign assets but those generally amount to a small fraction of liabilities.

[^17]: On figure 4.14, the IS and LM curves shift simultaneously to the right.

[^18]: For example, Christiano, Eichenbaum and Rebelo (2011) find that in a benchmark, new-Keynesian model, the multiplier is lower than unity in normal conditions but significantly higher than unity at the zero lower bound.

[^19]: On a sample of 21 OECD countries, de Mello et al. (2004) find that a one percentage point drop in public saving results in a one-third to one-half percentage point rise in private saving.

[^20]: The so-called *Haavelmo theorem* (1945) states that in a simple Keynesian setting, a simultaneous reduction of public spending and taxes by a given amount reduces output.

[^21]: The approach was pioneered by Ramey and Shapiro (1998). See also Burnside, Eichenbaum, and Fisher (2004).

[^22]: Chodorow-Reich (2017) surveys the evidence on the value of regional multipliers and concludes that they are consistent with a zero lower bound national multiplier of 1.7 for the United States. Ramey and Zubairy (2017) find that it could be as high as 1.5 at the zero lower bound.

[^23]: The evidence, however, is disputed by Ramey and Zubairy (2017).

[^24]: From the name of a famous Boston crook in the 1920s, who used to entice savers with the promise of high returns, but who would pay them only with the amounts collected from new participants. Ponzi games were played on a large scale in Russia and Albania in the 1990s. The Madoff fraud uncovered in 2008 is another example.

[^25]: The European Commission indicators are published yearly in the Fiscal Sustainability Report prepared by DGECFIN.

[^26]: The European Commission has developed a short-term vulnerability indicator called S0 that relies on a series of *ad hoc* subcomponents. As for the IMF, it relies on gross financial needs (i.e., on the sum of the financial deficit and of debt redemptions over the year). Gross financial needs in excess of 15–20% of GDP are considered a threat. This alternative approach stresses that the same debt may be sustainable or not depending on its maturity structure.

[^27]: Bohn (1998) provides evidences of such behavior in the US case.

[^28]: In practice, the threshold of unsustainability is in fact lower and the fiscal space is smaller because as $d$ approaches $d^{**}$, financial markets become aware of the risk of <!-- p. 230 --> a shock pushing the debt ratio above that level into the insolvency zone. For this reason they will start pricing the insolvency risk at lower debt levels already.

[^29]: See Mundell (1968) and Fleming (1962).

[^30]: In the United States, the Gramm-Rudman-Hollings Balanced Budget Act of 1985 was temporarily operational.

[^31]: Osterba (1994), however, exploits the fact that budget rules in US states typically date back to the nineteenth century. He finds that their relative stringency had affected state responses to shocks in the 1980s.

[^32]: Interview with the *Financial Times*, May 29, 2011.

[^33]: The Mexican crisis marked the return of sovereign default at the forefront of the international agenda, after three decades with almost no sovereign crises.

[^34]: On the occasion of the Greek case, the IMF introduced a “systemic exemption” so as to be able to lend despite its assessment on the probability that the Greek debt was sustainable. This exemption was removed in January 2016.

[^35]: This was illustrated by the protracted deadlock of the interwar period over German war reparations and later by the Latin American debt crisis of the 1980s, until the Brady plan of 1989 cleared the way for a settlement.

[^36]: The law was challenged in various courts, including the European Court of Human Rights. It was upheld on the ground that the severe financial crisis facing Greece made the restructuring inevitable and that the procedure chosen to implement the restructuring had followed the CAC template adopted by all euro area sovereign issuers.

[^37]: Actually, even under the assumptions of the model, the inefficiency of fiscal policy holds only for a small country, which does not describe the euro area as compared to the rest of the world. For an open economy under flexible exchange rates, however, fiscal stimulus results in stimulating the trading partners’ economies.

## References

Alesina, A., and S. Ardagna (2010), “Large Changes in Fiscal Policy: Taxes Versus Spending,” in J. Brown, ed., *Tax Policy and the Economy* 24, pp. 35–68, Chicago University Press.

Alesina, A., Barbiero, O., Favero, C., Giavazzi, F., and M. Paradisi (2017), “The Effects of Fiscal Consolidations: Theory and Evidence,” *NBER Working Paper* 23385.

Auerbach, A., and Y. Gorodnichenko (2012), “Measuring the Output Responses to Fiscal Policy,” *American Economic Journal: Ec. Policy*, 4(2), pp. 1–27.

Auerbach, A., and Y. Gorodnichenko (2017), “Fiscal Stimulus and Fiscal Sustainability”, *NBER Working Paper*, No 23789, Sep.

Barro, R. (1974), “Are Government Bonds Net Wealth?” *Journal of Political Economy*, 81(6), pp. 1095–1117.

Batini, N., L. Eyraud, L. Forni, and A. Weber (2014), “Fiscal Multipliers: Size, Determinants, and Use in Macroeconomic Projections,” *Technical Note*, International Monetary Fund.

Bayoumi, T. (2001), “The Morning After: Explaining the Slowdown in Japanese Growth in the 1990s,” *Journal of International Economics* 53(2), pp 241-259.

[^29]: See Mundell (1968) and Fleming (1962).

[^30]: In the United States, the Gramm-Rudman-Hollings Balanced Budget Act of 1985 was temporarily operational.

[^32]: Interview with the *Financial Times*, May 29, 2011.

[^33]: The Mexican crisis marked the return of sovereign default at the forefront of the international agenda, after three decades with almost no sovereign crises.

[^34]: On the occasion of the Greek case, the IMF introduced a “systemic exemption” so as to be able to lend despite its assessment on the probability that the Greek debt was sustainable. This exemption was removed in January 2016.

[^35]: This was illustrated by the protracted deadlock of the interwar period over German war reparations and later by the Latin American debt crisis of the 1980s, until the Brady plan of 1989 cleared the way for a settlement.

[^36]: The law was challenged in various courts, including the European Court of Human Rights. It was upheld on the ground that the severe financial crisis facing Greece made the restructuring inevitable and that the procedure chosen to implement the restructuring had followed the CAC template adopted by all euro area sovereign issuers.

[^37]: Actually, even under the assumptions of the model, the inefficiency of fiscal policy holds only for a small country, which does not describe the euro area as compared to the rest of the world. For an open economy under flexible exchange rates, however, fiscal stimulus results in stimulating the trading partners’ economies.

<!-- p. 231 -->

Beetsma, R., and L. Bovenberg (1999), “Does Monetary Unification Lead to Excessive Debt Accumulation?” *Journal of Public Economics*, 74(3), pp. 299–325.

Bénassy-Quéré, A., and J. Cimadomo (2012), “Changing Patterns of Domestic and Cross-Border Fiscal Policy Multipliers in Europe and the US,” *Journal of Macroeconomics*, 34, 845–873.

Bénassy-Quéré, A., and X. Ragot (2015), “A Policy Mix for the Euro Area,” *Note of the French Conseil d’analyse économique*, 21 March.

Bénassy-Quéré, A., Ragot, X., and G. Wolff (2016), “Which Fiscal Union for the Euro Area?” *Note of the French Conseil d’analyse économique*, 29 February.

Bénassy-Quéré, A., et al. (2018), “Reconciling risk sharing with market discipline : A constructive approach to Eurozone reform”, *Centre for Economic Policy Research Policy Insight No 91*, January.

Blanchard, O. (1985), “Deficits, Debts, and Final Horizons,” *Journal of Political Economy*, 93(2), pp. 223–47.

Blanchard, O. (1993), “Suggestions for a New Set of Fiscal Indicators,” in H. Vergon and F. van Winden, eds., *The Political Economy of Government Debt*, Elsevier Science Publishers, pp. 307–25.

Blanchard, O., C. Erceg, and J. Linde (2017), “Jump-Starting the Euro Area Recovery: Would a Rise in Core Fiscal Spending Help the Periphery?” *NBER Macroeconomics Annual*, 31(1), pp. 103–82.

Blanchard, O., and R. Perotti (2002), “An Empirical Characterization of the Effects of Changes in Government Spending and Taxes on Output,” *Quarterly Journal of Economics*, 117(4), pp. 1329–68.

Blanchard, O., and J. Simon (2001), “The Long and Large Decline in US Output Volatility,” *Brookings Papers on Economic Activity*, 1, pp. 135–64.

Bofinger, P., Mayer, E., and T. Wollmershäuser (2002), “The BMW Model: Simple Macroeconomics for Closed and Open Economies: A Requiem for the IS/LM-AS/AD and the Mundell-Fleming Model,” *Würzburg Economic Papers No. 35*.

Bohn, H. (1998), “The Behavior of US Public Debt and Deficits,” *The Quarterly Journal of Economics*, 113(3), pp. 949–63.

Boorman, J. (2002), “Sovereign Debt Restructuring: Where Stands the Debate?” speech at Cato Institute-The Economist conference, New York, 17 October.

Buchheit, L. C., A. Gelpern, M. Gulati, U. Panizza, B. Weder di Mauro, and J. Zettelmeyer (2013), “Revisiting Sovereign Bankruptcy,” Committee on International Economic Policy and Reform, Brookings Institution Report, October.

Bundesfinanzministerium (2009), “Reforming the Constitutional Budget rules in Germany,” Public Finance and Economic Affairs Directorate, Deficit Rule Reform Team, August.

Burnside, C., M. Eichenbaum, and J. Fischer (2004), “Fiscal Shocks and their Consequences,” *Journal of Economic Theory*, 115(1), pp. 189–17.

Calmfors, L., and S. Wren-Lewis (2011), “What Should Fiscal Councils Do?” *Economic Policy*, 26(68), pp. 649–95.

Campbell, J., and N. G. Mankiw (1989), “Consumption, Income, and Interest Rates: Reinterpreting the Time Series Evidence,” in Blanchard, O., and S. Fischer, eds., *NBER Macroeconomics Annual 1989*, MIT Press, pp. 185–216.

<!-- p. 232 -->

Carnot, N., and F. de Castro (2015), “The Discretionary Fiscal Effort: An Assessment of Fiscal Policy and Its Output Effect,” *European Economy Economic Papers* 543, European Commission.

Carroll, L. (1899), *Sylvie and Bruno*, Macmillan.

Chodorow-Reich, G. (2017), “Geographic Cross-Sectional Fiscal Spending Multipliers: What Have We Learned?” mimeo, Harvard University, December.

Christiano, L., M. Eichenbaum, and S. Rebelo (2011), “When Is the Government Spending Multiplier Large?” *Journal of Political Economy*, 119(1), pp. 78–121.

Coenen, G., C. J. Erceg, C. Freedman, D. Furceri, M. Kumhof, R. Lalonde, D. Laxton, J. Linde, A. Mourougane, D. Muir, S. Mursula, C. de Resende, J. Roberts, W. Roeger, S. Snudden, M. Trabandt, and J. in’t Veld (2012), “Effect of Fiscal Stimulus in Structural Models,” *American Economic Journal: Macroeconomics*, 4(1), pp. 22–68.

Coibion, O., Y. Gorodnichenko, and M. Ulate (2017), “The Cyclical Sensitivity in Estimates of Potential Output,” NBER Working Paper 23580, July.

Corsetti, G., K. Kuester, A. Meier, and G. Müller (2013), “Sovereign Risk, Fiscal Policy and Macroeconomic Stability,” *The Economic Journal*, 123, pp. 99–132.

Cruces, J., and C. Trebesch (2013), “Sovereign Defaults: The Price of Haircuts,” *American Economic Journal: Macroeconomics*, 5(3), pp. 85–117.

De Grauwe, P. (2011), “Managing a Fragile Eurozone,” CESifo Forum, 12(2), pp. 40–45.

De Grauwe, P., and Y. Ji (2013), “Self-Fulfilling Crises in the Eurozone: An Empirical Test,” *Journal of International Money and Finance*, 34(C), pp. 15–36.

Debrun, X., J. Pisani-Ferry, and A. Sapir (2010), “Government Size and Output Volatility: Should We Forsake Automatic Stabilization,” in Buti, M., S. Deroose, V. Gaspar, and J. Nogueira Martins, eds., *The Euro: The First Decade*, Cambridge University Press, pp. 451–506.

Debrun, X., X. Zhang, and V. Lledo (2017), “The Fiscal Council Dataset: A Primer to the 2016 Vintage,” International Monetary Fund, March.

de Mello, L., P.-M. Kongsrud, and R. Price (2004), “Savings Behavior and the Effectiveness of Fiscal Policy,” OECD Economics Department Working Paper 397.

Deutsche Bundesbank (2016), “The International Spillover Effects of an Expansion of Public Investment in Germany,” *Monthly Report August* 2016, pp. 13–17.

Devries, P., J. Guajardo, D. Leigh, and A. Pescatori (2011), “A New Action-based Dataset of Fiscal Consolidation,” IMF Working Paper 11/128.

Dippelsman, R., C. Dziobek, and C. A. Gutiérrez Mangas (2012), “What Lies Beneath: The Statistical Definition of Public Sector Debt,” IMF Staff Discussion Note 12/09, July.

Draghi, M. (2014), “Unemployment in the Euro Area,” speech at the Jackson Hole Central Banking Symposium, 22 August.

Eichengreen, B., R. Hausmann, and U. Panizza (2005), “The Pain of Original Sin,” in Eichengreen, B., and R. Hausmann, eds., *Other People’s Money: Debt Denomination and Financial Instability in Emerging Market Economics*, University of Chicago Press, pp. 13–47.

Eichengreen, B., and C. Wyplosz (1998), “The Stability Pact: More than a Minor Nuisance?” *Economic Policy*, 13(26), pp. 65–104.

<!-- p. 233 -->

Elbadawi, I., K. Schmidt-Hebbel, and R. Soto (2015), “Why Do Countries Have Fiscal Rules?” in Caballero, R., and K. Schmidt-Hebbel, eds., *Economic Policies in Emerging-Market Economies Festschrift in Honor of Vittorio Corbo*, vol. 21, pp. 155–89, Banco Central de Chile.

European Commission (2016), “Cross-Border Risk Sharing After Asymmetric Shocks: Evidence from the Euro Area and the United States,” *Quarterly Report on the Euro Area*, 15(2), Directorate-General ECFIN.

European Commission (2015), “Making the Best Use of the Flexibility within the Existing Rules of the SGP,” Communication COM(2015), 12 January.

Fall, F., D. Bloch, J.-M. Fournier, and P. Hoeller (2015), “Prudent Debt Targets and Fiscal Frameworks,” *OECD Economic Policy Paper* 15.

Fatás, A., and I. Mihov (2001), “Government Size and Automatic Stabilisers: International and Intrnational Evidence,” *Journal of International Economics*, 55(1), pp. 3–28.

Feldstein, M. (2002), “The Role for Discretionary Fiscal Policy in a Low Interest Rate Environment,” *NBER Working Paper* 9203.

Fleming, J. M. (1962), “Domestic Financial Policies Under Fixed and Under Flexible Exchange Rates,” *IMF Staff Papers* 9(3), pp. 369–79.

Furman, J. (2016), “The New View of Fiscal Policy and Its Application,” speech at the conference *Global Implications of Europe’s Redesign*, New York, 5 October.

Gali, J. (1994), “Government Size and Macroeconomic Stability,” *European Economic Review*, 38(1), pp. 117–32.

Gali, J., J. D. López-Salido, and J. Vallés (2007), “Understanding the Effects of Government Spending on Consumption,” *Journal of the European Economic Association*, 5(1), pp. 227–270.

Gelpern, A. (2014), “A Sensible Step to Mitigate Sovereign Bond Dysfunction,” mimeo, Peterson Institute for International Economics, 29 August.

Ghosh, A., Kim, J., Mendoza, E., Ostry, J., and M. Qureshi (2011), “Fiscal Fatigue, Fiscal Space and Debt Sustainability in Advanced Economies,” *The Economic Journal* 123(566), pp. 4–30.

Greenspan, A., and J. Kennedy (2007), “Sources and Uses of Equity Extracted from Homes,” *Finance and Economics Discussion Series* 2007-20, Federal Reserve Board.

Guajardo, J., Leigh, D., and A. Pescatori (2014), “Expansionary Austerity? International Evidence,” *Journal of the European Economic Association* 12(4), pp. 949–968.

Haavelmo, T. (1945), “Multiplier Effects of a Balanced Budget,” *Econometrica*, 13(4), pp. 311–18.

Hansen, A. (1953), *A Guide to Keynes*, New York: McGraw Hill.

Henning, R., and M. Kessler (2012), “Fiscal Federalism: US History for Architects of Europe’s Fiscal Union,” *Bruegel Essays* 6, Bruegel, Brussels.

Hicks, J. (1937), “Mr. Keynes and the ‘Classics’: A Suggested Interpretation,” *Econometrica*, 5(2), pp. 147–59.

International Monetary Fund (2010), “Will It Hurt? Macroeconomic Effects of Fiscal Consolidation,” Chapter 3 of *World Economic Outlook*, October, pp. 93–124.

International Monetary Fund (2013), “Staff Guidance Note for the Public Debt Sustainability Analysis in Market-Access Countries,” mimeo, 9 May.

<!-- p. 234 -->

International Monetary Fund (2017), *IMF Fiscal Monitor: Achieving More with Less*, April.

Janket, J.-C., with D. Tusk, J. Dijsselbloem, M. Draghi, and M. Schulz (2015), *Completing Europe’s Economic and Monetary Union* (Five Presidents’ Report), European Commission, 22 June.

Keynes, J. M. (1931), *Essays in Persuasion*, Harcourt, Brace and Company.

Keynes, J. M. (1936), *The General Theory of Employment, Interest and Money*, Macmillan.

Kopits, G., and S. Symansky (1998), “Fiscal Policy Rules,” IMF Occasional Paper 162.

Krueger, A. (2002), *A New Approach to Sovereign Debt Restructuring*, International Monetary Fund.

Laeven, L., and F. Valencia (2012), “Systemic Banking Crisis Database: An Update,” IMF Working Paper 12/63, June.

Lledó, V., Y. Sungwook, F. Xiangming, M. Samba, and Y. Kim (2017), *Fiscal Rules at a Glance*, International Monetary Fund.

MacDougall, D. (1977), *Report of the Study Group on the Role of Public Finance in European Integration*, report to the European Commission.

Mankiw, N. G. (2000), “The Savers-Spenders Theory of Fiscal Policy,” *American Economic Review* (Papers and Proceedings), 90(2), pp. 120–25.

Mauro, P., R. Romeu, A. Binder, and A. Zaman (2013), “A Modern History of Fiscal Prudence and Profligacy,” IMF Working Paper 13/5.

Mineshima, A., M. Poplawski-Ribeiro, and A. Weber (2014), “Fiscal Multipliers,” in Cottarelli, C., P. Gerson, and A. Senhadji, eds., *Post-Crisis Fiscal Policy*, MIT Press, pp. 315–372.

Mirabeau H.-G. Riqueti, comte de (1787), *Lettres du comte de Mirabeau sur l’administration de M. Necker*, available on gallica.bnf.fr, French Bibliothèque nationale.

Mourre, G., G.-M. Isbasoiu, D. Paternoster, and M. Salto (2013), “The Cyclically-Adjusted Budget Balance Used in the EU Fiscal Framework: An Update,” *European Economy*, Economic Paper 478.

Mundell R. (1968), *International Economics*, Macmillan.

Nakamura, E., and J. Steinsson (2014), “Fiscal Policy in a Monetary Union: Evidence from US Regions,” *American Economic Review* 104(3), pp. 753–92.

Nordhaus, W. (1975), “The Political Business Cycle,” *The Review of Economic Studies*, 42(2), pp. 169–90.

Norwegian Expert Commission (2015), “Fiscal Policy in an Oil Economy: The Application of the Fiscal Rule,” *Official Norwegian Reports NOU*, 2015:9, Chapter I.

Pisani-Ferry J. (2015), “Rebalancing the Governance of the Euro Area,” in Dawson, M., H. Enderlein, and C. Jörges, eds., *Beyond the Crisis*, Oxford University Press, pp. 62–82.

Polackova H. (1999), “Contingent Government Liabilities: A Hidden Fiscal Risk,” *Finance and Development*, 36(1), pp. 46–49.

Poterba, J. (1994), “State Responses to Fiscal Crises: The Effects of Budgetary Institutions and Politics,” *Journal of Political Economy*, 102(4), pp. 799–821.

<!-- p. 235 -->

Ramey, V., and M. D. Shapiro (1998), “Costly Capital Reallocation and the Effects of Government Spending,” *Carnegie Rochester Conference Series on Public Policy*, 48, pp. 145–94.

Ramey, V., and S. Zubairy (2017), “Government Spending Multipliers in Good Times and Bad: Evidence from US Historical Data,” *Journal of Political Economy*, forthcoming.

Reinhart, C., and K. Rogoff (2014), “This Time Is Different: A Panoramic View of Eight Centuries of Financial Crises,” *Annals of Economics and Finance*, 15(2), 1065–1188.

Reinhart, C., and C. Trebesch (2016), “Sovereign Debt Relief and Its Aftermath,” *Journal of the European Economic Association*, 14(1), pp. 215–251.

Ricardo, D. (1820), “Essay on the Funding System,” in Sraffa, P., ed., *The Works and Correspondence of David Ricardo*, Cambridge University Press, 1951, pp. 143–200.

Rodrik, D. (1998), “Why Do More Open Economies Have Bigger Governments?” *Journal of Political Economy*, 106, pp. 997–1032.

Romer, C., and D. Romer (2010), “The Macroeconomic Effects of Tax Changes: Estimates Based on a New Measure of Fiscal Shocks,” *American Economic Review*, 100(3), pp. 763–801.

Romer, D. (2000), “Keynesian Macroeconomics Without the LM Curve,” *Journal of Economic Perspectives*, 14(2), pp. 149–69.

Sachs, J. (1995), “Do We Need an International Lender of Last Resort?” Frank D. Graham Lecture, Princeton University, 20 April.

Sachs, J., and X. Sala-i-Martin (1992), “Fiscal Federalism and Optimum Currency Areas: Evidence for Europe from the United States,” in Canzoneri, M., V. Grilli, and P. Masson, eds., *Establishing a Central Bank: Issues in Europe and Lessons from the US*, Cambridge University Press, pp. 195–219.

Schaechter, A., T. Kinda, N. Budina, and A. Weber (2012), “Fiscal Rules in Response to the Crisis—Toward the ‘Next-Generation’ Rules: A New Dataset,” *IMF Working Paper* 12/187.

Schmidt-Hebbel, K. (2012), “Fiscal Policy for Commodity-Exporting Countries: Chile’s Experience,” *Documento de Trabajo* 415, Banco Central de Chile.

Sutherland, A. (1997), “Fiscal Crises and Aggregate Demand: Can High Public Debt Reverse the Effects of Fiscal Policy?” *Journal of Public Economics*, 65(2), pp. 147–62.

Tabellini, G., and A. Alesina (1990), “Voting on the Budget Deficit,” *American Economic Review*, 80(1), pp. 37–49.

Taylor, J. (2000), “Reassessing Discretionary Fiscal Policy,” *Journal of Economic Perspectives*, 14(3), pp. 21–36.

Tereanu, E., Tuladhar, A., and A. Simone (2014), “Structural Balance Targeting and Output Gap Uncertainty,” *IMF Working Paper* 14/107.

Trichet, J.-C. (2013), “International Policy Coordination in the Euro Area: Toward an Economic and Fiscal Federation By Exception,” *Journal of Policy Modeling*, 35(3), pp. 473–81.

Van Rompuy, H., with J.-M. Barroso, J.-C. Juncker, and M. Draghi (2012), *Towards a Genuine Economic and Monetary Union* (Four Presidents’ Report), European Council, 5 December.

<!-- p. 236 -->

Wyplosz, C. (2005), “Fiscal Policy: Institutions Versus Rules,” *National Institute Economic Review*, 191, pp. 70–84.

Zettelmeyer, J., C. Trebesch, and M. Gulati (2013), “The Greek Debt Restructuring: An Autopsy,” *Economic Policy*, 28 (75), pp. 513–63.

Zheng, L. (2014), “Determinants of the Primary Fiscal Balance: Evidence from a Panel of Countries,” in Cottarelli, C., P. Gerson, and A. Senhadji, eds., *Post-Crisis Fiscal Policy*, MIT Press, pp. 67–96.

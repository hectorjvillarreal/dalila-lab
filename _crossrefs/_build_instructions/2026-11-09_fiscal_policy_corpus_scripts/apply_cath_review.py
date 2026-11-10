import re, sys
F="/home/hectorjuan/Dalila/_crossrefs/corpus/fiscal_policy/foundational/benassy-quere_2019_ch4_fiscal_policy.md"
s=open(F).read(); orig=s
def rep(old,new,count=1,label=""):
    global s
    n=s.count(old); assert n>=1, f"MISSING anchor [{label}]: {old[:70]!r}"
    if count==1: assert n==1, f"anchor not unique [{label}] ({n}x): {old[:70]!r}"
    s=s.replace(old,new) if count!=1 else s.replace(old,new,1)

# ---------- A. page-image checks ----------
# A1 B4.13.6: book prints (x_s - h_s) -> keep as printed, add editorial note
rep(r"\tau^* = (r-g) \left[ b_0 + \int_{0}^{\infty} (x_s - h_s)", r"\tau^* = (r-g) \left[ b_0 + \int_{0}^{\infty} (x_s - h_s)", label="A1 presence")
i=s.index(r"(x_s - h_s)"); j=s.index("$$", i)+2
s=s[:j]+"\n\n*[Editorial note: the book prints $(x_s - h_s)$ in (B4.13.6) (verified on the page image, p. 195). This is inconsistent with the box's own definition $\\delta = x + h - \\tau$ and with (B4.13.5); the correct form is $(x_s + h_s)$. Kept as printed; see Team note 2 below.]*"+s[j:]
# A2 B4.5.4-5: book prints ≅ (approximately equal), not ≡
rep(r"b = \frac{1+i}{1+n}b_{-1} + \delta \equiv (1+i-n)b_{-1} + \delta = (1+r-g)b_{-1} + \delta \tag{B4.5.4}",
    r"b = \frac{1+i}{1+n}b_{-1} + \delta \cong (1+i-n)b_{-1} + \delta = (1+r-g)b_{-1} + \delta \tag{B4.5.4}", label="A2a")
rep(r"b - b_{-1} \equiv (i-n)b_{-1} + \delta \tag{B4.5.5}", r"b - b_{-1} \cong (i-n)b_{-1} + \delta \tag{B4.5.5}", label="A2b")
# A3 p199 scrambled paragraph -> restored from image
m=re.search(r"The representation of households' behavior is based on an overlapping-the \"old\" generation model\.[^\n]*\n", s)
assert m, "A3 anchor"
s=s.replace(m.group(0), "The representation of households' behavior is based on an overlapping-generation model. At any date, two generations coexist, the \"young\" and the \"old.\" Fiscal policy is represented by a primary deficit $D$ (per capita) that takes the form of a (non-distortionary) lump-sum transfer to/from the consumers. Denoting $r$ the constant interest rate, the dynamics of the per capita public debt $B$ at time $t$ is given by:\n")
# A4 p164 duplicated half-line
rep("We also suppose that debt is measured at debt for a given public deficit. ", "", label="A4")
# stray line p198 (not on the page image)
rep("An overlapping-generations model with Keynesian features\n", "", label="stray p198")

# ---------- B1/B2. footnotes ----------
s=re.sub(r"^\[\^[^\]]+\]: Footnote marker[^\n]*\n", "", s, flags=re.M)        # placeholders
s=re.sub(r"^\[\^1\]: Footnote marker for the reference[^\n]*\n", "", s, flags=re.M)
for junk in ["[^10]: Group of Twenty\n", "[^11]: IMF proposals for a coordinated stimulus\n"]:
    rep(junk, "", label="junk note "+junk[:6])
# Box 4.1 note a (p152)
rep("[^1] See www.cbpp.org", "[^b4-1a]: See www.cbpp.org", label="box4.1 note")
rep("often more if it is not concluded by October 1", "often more if it is not concluded by October 1", label="b4.1 marker presence")
# Box 4.13 Stein note: drop the colon-less copy, re-letter the definition
s=re.sub(r"^\[\^1\] The layman’s version[^\n]*\n\n?", "", s, flags=re.M)
rep("[^1]: The layman’s version of the transversality condition", "[^b4-13a]: The layman’s version of the transversality condition", label="stein")
rep("income and expenditure streams.[^a]", "income and expenditure streams.[^b4-13a]", label="stein marker")
# p221 duplicates (colon-less copies) and placeholder [^b]
s=re.sub(r"^\[\^a\] See the Presidency Conclusions[^\n]*\n\n?", "", s, flags=re.M)
s=re.sub(r"^\[\^b\] The Six-Pack also introduced[^\n]*\n\n?", "", s, flags=re.M)
rep("[^a]: See the Presidency Conclusions", "[^b4-18a]: See the Presidency Conclusions", label="p221 a")
rep("[^b]: The Six-Pack also introduced", "[^b4-18b]: The Six-Pack also introduced", label="p221 b")
# Box 4.4 / 4.9 / 4.19 letter notes
rep("[^a]: The market for ratings is dominated", "[^b4-4a]: The market for ratings is dominated", label="b4.4 def")
rep("[^a]: For simplicity, we have assumed that, in case of default", "[^b4-9a]: For simplicity, we have assumed that, in case of default", label="b4.9 def")
rep("[^1]: This box is based on Henning and Kessler (2012).", "[^b4-19a]: This box is based on Henning and Kessler (2012).", label="b4.19 def")
rep("aftermath of the War for Independence.^{1}", "aftermath of the War for Independence.[^b4-19a]", label="b4.19 marker")

# ---------- B3. box-end markers ----------
ENDS = {
 "4.1":  ("[^b4-1a]: See www.cbpp.org", "after-line"),
 "4.2":  ("budgetary cost of new legislations.", "after-line"),
 "4.3":  ("instituted to monitor national policies.", "after-line"),
 "4.4":  ("[^b4-4a]: The market for ratings", "after-line"),
 "4.5":  ("can run a primary deficit without seeing its debt-to-GDP ratio increase.", "after-line"),
 "4.6":  ("failed to provide credit to stimulate private investment.", "after-line"),
 "4.7":  ("if the present value is reduced.", "after-line"),
 "4.8":  ("in nominal terms there has been no debt relief.", "after-line"),
 "4.9":  ("[^b4-9a]: For simplicity", "after-line"),
 "4.10": ("All these factors weaken the impact of fiscal expansion on aggregate demand and income.", "after-line"),
 "4.11": ("This result is the Ricardian equivalence theorem.", "after-line"),
 "4.12": ("Blanchard and Perotti find that, in the short term,", "after-line"),
 "4.13": ("[^b4-13a]: The layman’s version", "after-line"),
 "4.14": ("exhibits an anti-Keynesian effect and leads to a contraction of output.", "after-line"),
 "4.15": ("explain why similar fiscal policies can have contrasting effects on output.", "after-line"),
 "4.16": ("(Norwegian Expert Commission, 2015).", "after-line"),
 "4.17": ("Its methodologies are made public.", "after-line"),
 "4.18": ("[^b4-18b]: The Six-Pack also introduced", "after-line"),
 "4.19": ("[^b4-19a]: This box is based on Henning and Kessler (2012).", "after-line"),
 "4.20": ("The figure displays three panels showing the impact of a fiscal expansion in a monetary union.", "after-line"),
}
for box,(anchor,_) in ENDS.items():
    i=s.find(anchor); assert i>=0, f"box end anchor {box}"
    assert s.find(anchor, i+1)<0, f"box end anchor not unique {box}"
    j=s.index("\n", i)
    s=s[:j]+f"\n\n<!-- end Box {box} -->"+s[j:]

# ---------- B4. equation tags ----------
s=s.replace(r"\tag{B.4.13.", r"\tag{B4.13.")

# ---------- B5. box anchors + extended editorial note ----------
rep("#### Box 4.18 Fiscal Rules and Institutions in the United Kingdom\n\n*[Editorial note: printed as \"Box 4.18\" on p. 213 although the text on p. 212 refers to it as box 4.17; the euro-area box on p. 219 is also printed as 4.18. Kept as printed.]*",
    "<a id=\"box-4-17\"></a>\n\n#### Box 4.18 Fiscal Rules and Institutions in the United Kingdom\n\n*[Editorial note (anchor `box-4-17`): the book's box numbering slips here. This box is printed \"4.18\" (p. 213) but the text on p. 212 calls it box 4.17; the euro-area box (p. 219, anchor `box-4-18`) is also printed 4.18 and the p. 219 text calls it 4.18; the p. 207 text sends the reader to \"box 4.19\" for the European framework, while the box printed 4.19 (p. 222, anchor `box-4-19`) covers the US states, as the p. 221 text correctly says. Printed labels are kept; use the anchors for cross-references.]*", label="B5 note")
rep("#### Box 4.18 Fiscal Rules and Procedures in the Euro Area", "<a id=\"box-4-18\"></a>\n\n#### Box 4.18 Fiscal Rules and Procedures in the Euro Area", label="anchor 4.18")
rep("#### Box 4.19 The States' Fiscal Regime in the United States", "<a id=\"box-4-19\"></a>\n\n#### Box 4.19 The States' Fiscal Regime in the United States", label="anchor 4.19")

# ---------- C3. figure descriptions: inline marker; fix 4.12; drop duplicate 4.5 ----------
rep("**Figure 4.5**\n\nComparison of public debt dynamics between the United States and three European countries", "**Figure 4.5** *(figure appears on p. 162; caption and description on p. 163)*\n\nComparison of public debt dynamics between the United States and three European countries", label="fig4.5 dup locate")
i=s.index("Comparison of public debt dynamics between the United States and three European countries"); j=s.index("\n", i)
s=s[:i]+s[j+1:]
s=s.replace("**Figure 4.5** *(figure appears on p. 162; caption and description on p. 163)*\n\n\n", "**Figure 4.5** *(figure appears on p. 162; caption and description on p. 163)*\n\n")
rep("The chart shows an Aggregate Supply (AS) curve sloping upward and an Aggregate Demand (AD) curve intersecting it at two points, $E_1$ and $E_2$. The horizontal axis represents Production and the vertical axis Price. A rightward shift of the AD curve from its initial position to a new position results in movement from equilibrium point $E_1$ to $E_2$, indicating increased output under a Keynesian fiscal expansion scenario.",
    "The chart shows an upward-sloping aggregate supply (AS) curve and two downward-sloping aggregate demand curves, AD and AD′. Price is on the vertical axis and production on the horizontal axis. AD meets AS at $E_1$; the rightward shift to AD′ gives a new intersection $E_2$, with higher output and a somewhat higher price level.", label="fig4.12")
MARK="*[Chart description generated from the image by the local model — not book text; verify against the PDF before citing any number.]* "
lines=s.split("\n"); out=[]; k=0
for idx,l in enumerate(lines):
    if re.match(r"^(The chart|The graph|The figure displays|The bar chart|The diagram)", l) and not l.startswith(MARK):
        l=MARK+l; k+=1
    out.append(l)
s="\n".join(out); assert k>=12, f"only {k} chart descriptions marked"

# ---------- C3. p200 clipped paragraphs ----------
rep("Empirical investigations confirm that debt sustainability, or the lack thereof, significantly affects the fiscal multiplier.",
    "*[Paraphrase only — never quote: the right margin of p. 200 is clipped in the photo and the last words of each line in this and the next paragraph were inferred by the model.]* Empirical investigations confirm that debt sustainability, or the lack thereof, significantly affects the fiscal multiplier.", label="p200 mark")

# ---------- D. Cath's team notes ----------
NOTE1 = """
> **Team note 1 — under Box 4.5 (Cath, 2026-11-09)**
>
> *Book notation → RF/DFD notation.* Let $pb_t \\equiv -\\delta_t$ be the primary surplus ratio and $d_t \\equiv b_t$ the end-of-year debt ratio. The **exact** accumulation identity is
> $$d_t = \\frac{1+i_t}{1+n_t}\\,d_{t-1} - pb_t + sfa_t ,$$
> and the exact debt-stabilising primary surplus is
> $$pb^* = \\frac{i-n}{1+n}\\,d = \\frac{r-g}{1+g}\\,d \\quad (\\text{with } 1+i=(1+r)(1+\\pi),\\ 1+n=(1+g)(1+\\pi)).$$
> The book's (B4.5.4)–(B4.5.6) use the first-order approximation $pb^* \\approx (i-n)d$ (the book prints $\\cong$). At Mexican nominal growth of 8–10% the approximation overstates $pb^*$ by a factor of about $1+n$, roughly 8–10%. RF uses the exact form.
>
> *Mexico.* The book sets aside valuation effects (its first paragraph). In Mexico they are first order. With share $\\alpha$ of debt in foreign currency, peso depreciation $\\varepsilon_t$ and foreign rate $i^f_t$:
> $$d_t = \\frac{(1-\\alpha)(1+i_t) + \\alpha(1+i^f_t)(1+\\varepsilon_t)}{1+n_t}\\,d_{t-1} - pb_t + other_t .$$
> The debt aggregate is **SHRFSP**, and $pb$ is the RFSP primary balance. The gap between $\\Delta$SHRFSP and RFSP is $sfa$ (valuation plus other) and must be reported, not absorbed. The timing convention (end-of-period stock) matches the DFD budget constraint. Nina to confirm the index alignment in the Julia code.
"""
NOTE2 = """
> **Team note 2 — under Box 4.13 (Cath, 2026-11-09)**
>
> *Correct form of (B4.13.6)* (the book prints a minus; see the editorial note above): with $\\delta = x + h - \\tau$,
> $$\\tau^* = (r-g)\\Big[b_0 + \\int_0^\\infty (x_s + h_s)\\,e^{-(r-g)s}\\,ds\\Big], \\qquad r > g .$$
> *Discrete-time counterpart used in DFD:* $d_0 = \\sum_{t\\ge1} pb_t \\prod_{s=1}^{t}\\frac{1+g_s}{1+r_s}$, given $\\lim_{T\\to\\infty} d_T \\prod_{s=1}^{T}\\frac{1+g_s}{1+r_s} = 0$.
>
> *Regime caveat.* For $r \\le g$, both $\\tau^*$ and the present-value form lose their meaning: the discount factor no longer discounts. The book notes the case but does not develop it. This is the open watch item (`../watch_items/debt-stabilising-primary-balance-under-r-lt-g.md`).
>
> *Why this box matters for RF.* Blanchard's sustainable tax rate and the **tax gap** $\\tau^* - \\tau$ formalise RF's target. RF can **derive** a sustainability-consistent revenue path instead of asserting 25% by 2036. Feed the spending path $x + h$, including Beth's pension and health profiles, and Anne's demography, into either the infinite-horizon form or Blanchard's finite $N$-year benchmark (end of the box). This is the same logic as the EU's S2 indicator (p. 196). Mexico caveat: $\\tau$ here means *all* non-debt revenue. Oil revenue therefore belongs in $\\tau$ for sustainability, but not in the OECD tax-pressure headline. This is the same separation the Contabilidad de la Muerte makes.
"""
rep("<!-- end Box 4.5 -->", "<!-- end Box 4.5 -->\n"+NOTE1, label="note1")
rep("<!-- end Box 4.13 -->", "<!-- end Box 4.13 -->\n"+NOTE2, label="note2")

# ---------- frontmatter + status ----------
rep("transcription_status: transcribed_2026-11-09 — local VLM (qwen3.5:9b); equations in all boxes verified against page images by Claude Code; prose spot-checked on 12 pages; p. 236 re-photographed and read directly (verified)",
    "transcription_status: transcribed_2026-11-09 — local VLM (qwen3.5:9b); all box equations and ~30 pages of prose checked against page images by Claude Code; Cath review 2026-11-09 items A1–A4 and B1–B5 applied; awaiting Cath's re-check of A1 and endorsement", label="fm status")
rep("""**Known limitations:**
- p. 200, last paragraph: the right margin is clipped in the photo; the final words of each line were inferred by the model and read as plausible.
- Chart descriptions under each **Figure** caption are model-generated readings of the plot, not book text. Treat them as aids, verify against the PDF before citing numbers.
- Box boundaries: box titles are headings (`#### Box 4.x`); the end of a box is not marked. The PDF shows the frames.
- Chapter end-notes (pp. 228–230) are transcribed as a list; in-text note markers appear as `[^n]` or superscripts as the model rendered them.
- Pages before 148 (none in this chapter) and the book's index are out of scope.""",
"""**Cath's review (2026-11-09) applied:** (B4.13.6) misprint confirmed on the page image and annotated; (B4.5.4)–(B4.5.5) now carry the printed $\\cong$; Box 4.14 first paragraph restored from the image; duplicated half-line in Box 4.5 removed; all placeholder footnotes deleted and box footnotes re-lettered (`[^b4-Na]`); `<!-- end Box 4.x -->` markers added for all 20 boxes; equation tags normalised to the printed form; box anchors `box-4-17/18/19` added with an extended misprint note; chart descriptions carry an inline marker; p. 200 clipped paragraphs marked paraphrase-only; Team notes 1–2 (Cath) inserted under Boxes 4.5 and 4.13. Verified on the images: (B4.14.1)–(B4.14.2) are printed with $D_t$ and no $dt$, as transcribed.

**Known limitations:**
- p. 200, two lower paragraphs: the right margin is clipped in the photo; the last words of each line were inferred by the model. Marked inline as paraphrase-only.
- Chart descriptions under **Figure** captions are model-generated readings of the plot, not book text; each carries an inline marker. Verify against the PDF before citing numbers.
- Chapter end-notes (pp. 228–230) are transcribed under `## Notes`. In-text note numbers are as the model read them and have not been individually re-checked against the images; box footnotes are lettered `[^b4-Na]`.
- Box ends are marked `<!-- end Box 4.x -->`; the book interrupts one sentence on p. 152 with Box 4.1 (the sentence resumes after the box on p. 153).
- Pages before 148 (none in this chapter) and the book's index are out of scope.""", label="status block")

open(F,"w").write(s)
print("applied; words", len(s.split()), "| end markers", s.count("<!-- end Box"), "| chart marks", s.count(MARK), "| placeholder lines left", len(re.findall(r"Footnote marker", s)))

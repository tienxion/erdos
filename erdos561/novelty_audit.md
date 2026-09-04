# Novelty audit for Erdős problem 561

4 September 2026. This is a literature audit, not a proof of priority. The full conjecture remains unresolved by our work. The two-star proof is in `notes.md`; subsequent sufficient conditions are recorded separately by the other research agents.

## Assessment

**Correction from the final live-forum check:** [rickyc's comment of 6 August 2026](https://www.erdosproblems.com/forum/thread/561#post-8384) already contains the simultaneous-suffix property, its vertex-deletion implication, exactly the same parity/minimum-size distinction, and the bound

\[
\widehat r(F(A),F(B))\ge S-\sum_{k=2}^{s+t-1}\eta_k,
\]

where each non-good nonfinal diagonal contributes one to the deficit. The earlier audit missed this comment. **Those ingredients must not be claimed as new.** The remaining candidate contribution is the strengthened induction on equality-host degrees and the local gap criterion which eliminates these deficits. The manuscript now cites the comment explicitly. Its first example improves this specific prior bound by one edge; the arbitrary-h family improves it by h edges. These comparisons follow directly from the number of non-good diagonals in the displayed families. The live thread contained no matching gap-criterion proof when checked on 4 September 2026.

The formula for **two arbitrary stars against two arbitrary stars** was not found as a stated theorem in the primary papers read. Much of that parameter space is already covered by earlier theorems. Its proof also uses the one-star equality classification of Davoodi–Javadi–Kamranian–Raeisi in a fairly direct way, so presenting the entire two-star formula as a large new advance would overstate what has been established.

The subsequent criterion involving gaps between diagonal maxima and odd maximizing pairs is a stronger candidate contribution. An explicit family below has an unbounded additive improvement over the direct all-odd rounding lower bound; this comparison is not a claim about the best lower bound obtainable from all prior literature. It supplies explicit infinite families outside the hypotheses of the theorem statements checked below, including families with arbitrarily many components, repeated nontrivial stars, and single-edge components. This supports the precise claim **“not covered by these stated earlier results.”** It does not yet establish that nobody has proved the condition, a stronger condition, or a short equivalent corollary elsewhere.

Two material literature limitations remain: I could not retrieve the full original Győri–Schelp 2002 paper, and I could not retrieve Cheng's complete 2010 thesis. The modern published restatement of the former was read, and the institutional abstract of the latter was read. These limitations should be disclosed before claiming a completed novelty audit or submission readiness.

## Notation

Write $F(A)=\bigsqcup_{i=1}^s K_{1,a_i}$ for a positive nonincreasing sequence $A$, and similarly $F(B)$. Set

\[
L_k=\max_{i+j=k}(a_i+b_j-1),\qquad
S(A,B)=\sum_{k=2}^{s+t}L_k.
\]

The conjecture is $\widehat r(F(A),F(B))=S(A,B)$.

## Primary literature checked

### Burr–Erdős–Faudree–Rousseau–Schelp, 1978

**“Ramsey-minimal graphs for multiple copies,”** *Indagationes Mathematicae (Proceedings)* 81, 187–195. [Original scan](https://www.renyi.hu/~p_erdos/1978-38.pdf); [DOI](https://doi.org/10.1016/S1385-7258(78)80009-2). Full paper read. A local scan is `literature/BEFRS1978.pdf`.

Theorem 1 gives

\[
\widehat r(mK_{1,k},nK_{1,l})=(m+n-1)(k+l-1)
\]

for positive parameters, together with an extremal-host classification subsequently corrected by DJKR. The second section concerns how many disjoint copies a Ramsey host must contain. The final questions explicitly formulate the arbitrary-star-forest conjecture. There is no unequal two-stars-per-side theorem or diagonal-gap theorem in this paper.

### Burr–Erdős–Faudree–Rousseau–Schelp, 1981

**“Ramsey-minimal graphs for star-forests,”** *Discrete Mathematics* 33, 227–237. [Original scan](https://www.renyi.hu/~p_erdos/1981-24.pdf). Full paper read, including its single-edge-component results.

This paper concerns **Ramsey-finiteness**: whether there are finitely many hosts minimal under subgraph inclusion. This is different from determining their minimum edge count. Lemma 6 gives the star-forest construction underlying the conjectured upper bound. Theorems 9–12 concern finiteness/infinity, including forests with appended matching components. They do not state the two-star size formula or the new gap criterion. Its title alone is therefore misleading evidence for overlap.

### Győri–Schelp, 2002

**“Two-edge colorings of graphs with bounded degree in both colors,”** *Discrete Mathematics* 249, 105–110. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X01002382); [DOI](https://doi.org/10.1016/S0012-365X(01)00238-2).

The original full text could not be retrieved: publisher PDF requests returned HTTP 403, and the public publisher API supplied metadata only. Its abstract concerns decomposing a graph of maximum degree $k+l$ into subgraphs of maximum degrees $k,l$, with a bound on the number of vertices of maximum degree. It applies the result to star forests.

The precise published restatement in **DJKR 2025, Theorem 1.4**, is:

\[
\binom{L_k}{2}>\sum_{i=k}^{s+t}L_i
\quad\text{for every }2\le k\le s+t
\quad\Longrightarrow\quad
\widehat r(F(A),F(B))=S(A,B).
\tag{GS}
\]

The inequality is **strict** in the published DJKR PDF and its 2021 preprint. Fu–Luo–Ni v3's introduction instead prints a weak inequality. The distinction cannot be settled by treating either quotation as the original theorem. All explicit non-overlap examples below fail even the weak version, so their comparison does not rely on this discrepancy.

### Yen-Jen Cheng, 2010

**“Size Ramsey Numbers of Star Forests,”** master's thesis, National Taiwan University, advisor Gerard Jennhwa Chang. [Institutional record](https://scholars.lib.ntu.edu.tw/entities/publication/44c55546-025c-43b7-8f29-11a62827cc84); [thesis record](https://www.airitilibrary.com/Article/Detail/U0001-0408201016042700); [DOI](https://doi.org/10.6342/NTU.2010.00349).

Both primary records describe its scope as

\[
a_i=b_j=1\quad(i\ge2,\ j\ge2),
\]

namely one potentially nontrivial star plus a matching on each side. Consequently it is a serious prior-art lead for the two-star case $b=d=1$. **The abstract says it studies this case; that is not enough to assert it completely solves it.**

The indexed [full-thesis URL](https://tdr.lib.ntu.edu.tw/jspui/bitstream/123456789/10630/1/ntu-99-1.pdf) repeatedly timed out. The institutional attachment advertised as a 23.53 KB PDF is actually an HTML redirect to Airiti. The Airiti record supplies no authorized full text. No theorem number or exact resolved parameter range from the thesis has therefore been verified.

### Lortz–Mengersen, 2021

**“Size Ramsey Results for the Path of Order Three,”** *Graphs and Combinatorics* 37, 2315–2331. [Publisher](https://link.springer.com/article/10.1007/s00373-021-02398-3); [PDF](https://link.springer.com/content/pdf/10.1007/s00373-021-02398-3.pdf). Full paper retrieved and read; local `literature/LM2021.pdf` and `.txt`.

Theorem 7 states, for all $m\ge1,n_1\ge n_2\ge1$,

\[
\widehat r(K_{1,m},K_{1,n_1}\sqcup K_{1,n_2})
=2m+n_1+n_2-2.
\]

Thus the **one-star versus two-stars formula including single-edge components is already explicit prior art**. Remark 1 compares it with Győri–Schelp and observes that the latter leaves small parameter cases. No two-stars-versus-two-stars result is stated. Most of the paper concerns $P_3$ versus graphs on five vertices.

### Davoodi–Javadi–Kamranian–Raeisi, 2025

**“On a conjecture of Erdős on size Ramsey number of star forests,”** *Ars Mathematica Contemporanea* 25(2), P2.09. [DOI](https://doi.org/10.26493/1855-3974.3081.d6c); [published PDF repository](https://repozitorij.upr.si/IzpisGradiva.php?id=21994&lang=eng&print=); [2021 preprint](https://arxiv.org/html/2111.02065). The full published version and preprint were read. Local published version: `literature/DJKR2025.pdf` and `.txt`.

The relevant results are:

* Theorem 2.2: uniform forests, including corrected equality cases.
* Theorem 2.3: one star $K_{1,n}$ versus $F(m_1,\ldots,m_t)$, **$m_t\ge2$**; exact formula and equality-host classification.
* Theorem 2.4: two **equal** stars $2K_{1,n}$ versus $F(m_1,\ldots,m_t)$, **$m_t\ge2$**.
* Theorem 2.5: the conjecture when **every component size in both forests is odd**, with positive sizes including 1.
* Theorem 2.6: $sK_{1,n}$ versus $F(m_1,\ldots,m_t)$, **$m_t\ge2$**, where $n,m_1$ are odd.

These hypotheses are unchanged in the published version. The matching-deletion size argument in Theorem 2.3 works also for $m_t=1$, although its stated equality classification does not. Our general one-star formula is consequently a direct extension of their existing argument, not a strong novelty claim.

### Fu–Luo–Ni, current v3, July 2026

**“Size Ramsey minimal graphs for uniform star forests,”** [arXiv:2606.04439v3](https://arxiv.org/html/2606.04439v3), revised 4 July 2026. The full current paper was checked. Its Theorem 1.5 classifies extremal hosts for **uniform** star forests in multiple colours. The arbitrary-star-forest formula remains Conjecture 1.1.

The June 3 v1 had claimed the full conjecture, but that result is absent from v2 and v3. Search engines and some secondary sites still quote v1. The false deletion lemma from v1 is discussed in `notes.md`. Neither an obsolete abstract nor a secondary summary establishes that #561 is solved.

The multicolour uniform formula quoted as Theorem 1.4 is due to Zhang, **“A note on the size Ramsey number for stars,”** *JCMCC* 11 (1992), 209–212. [Publisher record](https://combinatorialpress.com/jcmcc-articles/volume-011/a-note-on-the-size-ramsey-number-for-stars/). It does not concern unequal components within a colour.

## Exact overlap for our two-star theorem

For $A=(a,b), B=(c,d)$, put

\[
x=a+c-1,\quad y=\max(a+d-1,b+c-1),\quad z=b+d-1.
\]

The published restatement (GS) covers exactly those tuples satisfying its three numerical tests

\[
z\ge4,\qquad \frac{y(y-3)}2>z,\qquad
\frac{x(x-3)}2>y+z.
\]

These equivalences follow by subtracting the leading term from each tail. A convenient sufficient range is $z\ge4,y\ge6,x\ge8$. This is only a sufficient range, not a characterization of everything known in 2002.

DJKR already covers all-odd tuples and, when $b,d\ge2$, either $a=b$ or $c=d$. Cheng's thesis potentially covers $b=d=1$, with its exact conclusions still unverified. The infinite strip

\[
(a,1)\quad\text{versus}\quad(c,2),\qquad a\ge2, c\ge3,
\]

is outside all these **stated** formula hypotheses: its final diagonal maximum is 2, one side has a size-2 component, and neither forest is uniform. It is outside Cheng's stated scope because $2\ne1$. This is a concrete candidate for the part of the two-star formula not explicitly covered by the sources inspected. It is not yet proof of priority.

## Newer criterion: concrete non-overlap examples

The current research theorem permits diagonal plateaus when a maximizing pair has both component sizes odd, or one component size 1; at the remaining nonterminal diagonals it imposes a drop of at least 3, or a drop of 2 followed by another drop of at least 2. The proof and exact formulation belong in the separate theorem document. The following comparisons require only its stated examples.

1. $A=(6,3^r,1^m)$, $B=(5,1)$, $r,m\ge1$, where superscripts mean repeated entries. Its diagonal maxima are

   \[
   (10,\underbrace{7,\ldots,7}_{r},\underbrace{5,\ldots,5}_{m},1),
   \qquad S=11+7r+5m.
   \]

   It fails even the weak GS test at its final diagonal, $0<1$. Both forests are nonuniform, $A$ contains an even component, and $A$ has at least two nontrivial components. It therefore lies outside the stated uniform, all-odd, one-star, equal-two-star, and Cheng-scope hypotheses. Rounding the 6 down to 5 makes both forests all odd and gives the already-known lower bound $10+7r+5m$; thus this particular family improves that elementary comparison by **one edge**. Its value is an infinite exact result, but the one-edge nature of this example should not be hidden.

2. $A=(6,3,1^r)$, $B=(7,3)$, $r\ge3$, has

   \[
   (L_2,\ldots,L_{s+t})=(12,9,\underbrace{7,\ldots,7}_{r},3),
   \qquad S=24+7r.
   \]

   At the first 7, the tail sum is $7r+3\ge24>\binom72=21$. Consequently this family fails even the weak GS condition **away from the terminal diagonal**. It is nonuniform, contains an even component, and has more than one nontrivial star on each side. This avoids attributing all non-overlap merely to a terminal single edge.

3. The separated-gap case $A=(6,4,2), B=(5,3,1)$ has maxima $(10,8,6,4,2)$, summing to 30. It has three unequal stars on each side and mixed parity; it fails the GS test at the final value 2. Arbitrary-length progressions with common difference 2 and opposite parity give the same type of comparison.

None of these checks proves that the full new criterion cannot be deduced from an unquoted lemma of an earlier paper. They rigorously establish that it is not a direct instance of the listed theorem statements.

### An unbounded improvement over direct all-odd rounding

Fix $h\ge1$, integers $r_1,\ldots,r_h\ge1$, and $m\ge1$. Let $B=(5,1)$ and form $A$ by concatenating, for $j=h,h-1,\ldots,1$, the block

\[
(4j+2,\underbrace{4j-1,\ldots,4j-1}_{r_j}),
\]

then append $m$ entries equal to 1. The new criterion gives

\[
\widehat r(F(A),F(B))
=2h^2+8h+\sum_{j=1}^{h}r_j(4j+3)+5m+1. \tag{U}
\]

Here is an independent check of the comparison arithmetic. Every adjacent difference of $A$ is at most 3. Thus, with $s=|A|$, the diagonal sequence against $B=(5,1)$ is

\[
(a_1+4,a_2+4,\ldots,a_s+4,1).
\]

Each exceptional even entry contributes $4j+6$ and each repeated odd entry contributes $4j+3$. Summing gives (U), since $\sum_{j=1}^h(4j+6)=2h^2+8h$. Lowering every even entry by one preserves the ordering and the same diagonal-maximizer pattern; it lowers the sum by exactly $h$. The rounded forests have all component sizes odd, so DJKR Theorem 2.5 and monotonicity give the known comparison lower bound equal to the right-hand side of (U) minus $h$.

Consequently the improvement over **that direct rounding comparison** is unbounded. No assertion is made that this rounding argument is the strongest possible use of all previous work. The family fails the weak and strict GS tests at its terminal value 1, is nonuniform, and has at least two nontrivial components in $A$, placing it outside Cheng's stated thesis scope. Its many even entries also exclude DJKR's all-odd hypothesis. The formula arithmetic was checked symbolically above and independently on finite parameter ranges by two agents.

## What can be claimed in a draft

A defensible introduction can say that the paper proves a new **candidate** sufficient criterion, supplies its complete proof, and exhibits infinite families outside the hypotheses of BEFRS's uniform theorem, DJKR's stated results, and the numerical Győri–Schelp condition quoted by DJKR. The actual mathematical mechanism to emphasize is the strengthened induction controlling the maximum-degree vertices of equality hosts. The star-union upper bound, ordinary deletion, matching deletion, Vizing's theorem, and Fournier's theorem are existing inputs.

Before asserting unqualified novelty or suitability for a journal submission, the original Győri–Schelp paper and Cheng thesis should be obtained and compared with the final exact statement. An independent human review should also assess whether the criterion is a short known consequence and whether the contribution is substantial enough for the intended venue. No external posting, submission, or author contact was performed in this audit.

The coordinating user subsequently reported having mathematically reviewed the argument and finding it accurate. This is a human review report, not a claim of external expert peer review. A carefully qualified forum post as proposed partial progress is distinct from journal readiness or a claim to have solved problem 561.

## Subsequent submission and improvements, 4 September 2026

The reviewed version 1 was subsequently submitted as a **partial** proof claim by **tienxion**, with the user's supplied summary, explicit AI disclosure, and direct credit to Ricky Cipollini. The site displayed **Awaiting moderator approval**. Exact text and the public PDF hash are in [submission_record.md](submission_record.md). The preceding statement that no submission occurred describes the earlier audit stage only.

The existing claim and its linked Overleaf manuscript were inspected before submission. Its displayed theorem is the diagonal sum minus the bad-diagonal count, and its proof uses simultaneous tails and parity splitting. The present manuscript credits these ingredients. The author is identified on the claim as Ricky Cipollini (username rickyc).

Subsequent work, kept outside that public PDF, gives a universal recursive refinement, matching-based recovery at additional gaps of two and one, and a complete mixed two-edge-star theorem. Full proofs and their audit status are in [improvement_recursive.md](improvement_recursive.md), [improvement_gap.md](improvement_gap.md), and [improvement_plateaus.md](improvement_plateaus.md). These are additional results from this research session; that description is not a claim of established priority.

A search located another possible Cheng thesis URL at <https://tdr.lib.ntu.edu.tw/bitstream/123456789/10630/1/ntu-99-1.pdf>. Repeated repository timeouts prevented retrieval; no full-text comparison is claimed. The original Győri–Schelp paper likewise remains unavailable. The novelty qualification therefore persists.

## Excluded false leads

* arXiv:2506.10477 is **“The Ramsey number of the 4-cycle versus a book graph,”** not a star-forest size-Ramsey paper; the catalogue association is erroneous.
* Ordinary Ramsey results on unions of two stars are different from size Ramsey results.
* Connected double stars are different from disjoint unions of two stars.
* Ramsey-finiteness is different from the size Ramsey number.
* The unavailable Cheng attachment was an HTML redirect; it is preserved as `literature/Cheng_download_redirect.html`, and must not be described as the retrieved thesis.

# Erdős problem 295: source and novelty audit

**Reading order:** the later addenda correct the initial historical upper-bound comparison by deriving the classical \(O(\sqrt N)\) bound from Vose. Candidate theorem formulations evolved during the research; the final formulations are in [the consolidated note](quantitative_obstructions.md), and historical “proposed coefficient” passages below are not the final theorem statements.

The final internal proof establishes the coefficient \(\mathcal C(B-1)\) under \(M\le N^{B+o(1)}\), and a stronger multiplicity coefficient under subquadratic ceilings. Its quantitative component argument bounds a positive incident reciprocal sum both above and below after cancelling component primes. These final statements were independently reviewed mathematically. The search findings about their arithmetic antecedents and unestablished novelty still apply; the later refinements do not repair the missing full-text access or amount to a new exhaustive literature search.

Checked 4 September 2026. This is a research audit, not a claim that the literature search is exhaustive. The exponential-max-denominator proposition in `prime_obstruction.md` has not been established as novel or suitable for submission.

## Findings that affect the research direction

1. The stated problem and the bound
   \[
   (e-1)N-c<k(N)<(e-1)N+c'N/\log N
   \]
   are confirmed directly in Erdős and Graham's 1980 monograph, printed p. 35.
2. The main ingredients of the present note are classical: harmonic extremality, divisibility restrictions on reciprocal sums, and exponential growth of least common multiples. Closely related reduced-denominator growth is recorded on printed p. 34 of the same monograph.
3. With a fixed linear denominator cap \(M\leq BN\), the methods of Croot and Martin give a stronger necessary excess of order \(N\log\log N/\log N\). Merely proving divergence in that case is therefore not new progress.
4. No inspected primary source states the exact implication
   \[
   |A|\leq(e-1)N+C\quad\Longrightarrow\quad
   \log\max A\gg_C N
   \]
   or the uniform tradeoff suggested by the present proof. This negative search result does **not** establish novelty. In particular, two historically relevant full texts remain unchecked.

## Primary sources

### Erdős and Graham, 1980: directly inspected

P. Erdős and R. L. Graham, *Old and New Problems and Results in Combinatorial Number Theory*, Monographies de L'Enseignement Mathématique 28, Geneva, 1980. [Author-hosted scan](https://mathweb.ucsd.edu/~ronspubs/80_11_number_theory.pdf).

Printed p. 35 defines \(U_n\) as the least number of distinct reciprocals summing to one with smallest denominator at least \(n\). It states the present divergence conjecture and attributes the displayed bounds above to Erdős and Straus [Er-Str (71) a]. The bibliography on printed p. 113 identifies that reference as the *Monthly* solution, volume 78, pp. 302–303.

Printed p. 34 states that the reduced denominator of the sum of \(n\) consecutive reciprocals is at least a function of order \(e^{n+o(n)}\), and mentions arithmetic progressions as well. Printed p. 35 excludes certain small multiples of prime powers from being the largest denominator of a representation.

These statements provide direct historical support and prior-art warnings. They do not, as written, assert the present bounded-excess proposition.

The scan's PDF page numbers differ from its printed numbers: PDF pages 30 and 31 are printed pp. 34 and 35. These pages were rendered and read visually; the scan has no usable text layer.

### Ruderman–Erdős–Straus, 1971: bibliographic record inspected; proof inaccessible

H. D. Ruderman, P. Erdős and E. Straus, “E2232”, *American Mathematical Monthly* **78** (1971), 302–303. [DOI](https://doi.org/10.2307/2317539), [journal contents](https://www.jstor.org/stable/i315024).

The issue contents and Crossref record agree on title, authors, pages, and DOI. Direct JSTOR article and PDF requests returned a client challenge, not article content. The original proof has therefore **not** been audited. The 1980 monograph independently confirms the claimed theorem and its attribution, but does not remove the need to inspect the 1971 proof before making a novelty claim about its refinements or denominator restrictions.

### Croot, 2001: journal theorem and lower-bound argument inspected

E. S. Croot III, “On unit fractions with denominators in short intervals”, *Acta Arithmetica* **99** (2001), 99–114. [Journal record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/99/2/83061/on-unit-fractions-with-denominators-in-short-intervals), [journal PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83061), [1999 preprint](https://arxiv.org/abs/math/9904181).

The main theorem, p. 100, represents each fixed positive rational \(r\) using distinct denominators in
\[
(N,(e^r+O_r(\log\log N/\log N))N],
\]
and proves the error's order optimal. The lower-bound proof on pp. 105–106 shows that any prime divisor of a denominator is at most \((1+o_r(1))M/\log M\), where \(M\) is the largest denominator. It then counts forbidden integers with large prime factors. For a linear cap, this prime restriction combined with harmonic loss gives the stronger excess in item 3. For \(M=N^B\), \(B>1\), that prime cutoff exceeds the initial interval, so this particular deduction does not apply.

The journal text was checked separately from the preprint: their organization and constants differ.

### Martin, 2000: journal results and obstruction inspected

G. Martin, “Denser Egyptian fractions”, *Acta Arithmetica* **95** (2000), 231–260. [Journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa95/aa9533.pdf), [author's description](https://personal.math.ubc.ca/~gerg/index.shtml?abstract=DrEF), [1998 preprint](https://arxiv.org/abs/math/9811112).

Theorem 1, p. 232, determines the minimum possible largest denominator for exactly \(t\) terms representing fixed \(r>0\):
\[
M_t(r)=\frac{t}{1-e^{-r}}+
\Theta_r\!\left(\frac{t\log\log t}{\log t}\right).
\]
Here the positive lower error follows from Proposition 5 and equation (7). This minimizes the largest denominator without prescribing a lower bound on every denominator. It must not be confused with problem 295.

Lemma 8, pp. 237–238, proves \(p\ll M/\log M\) by writing the terms divisible by \(p\) as \(pm_i\), clearing their least common multiple, and bounding the resulting positive multiple of \(p\). Proposition 5 bounds the possible cardinality when the largest denominator is prescribed. These provide explicit prior art for the arithmetic and extremal methods, but no inspected statement gives the present exponential-max tradeoff.

### Burshtein, 2005: abstract and metadata only

N. Burshtein, “On distinct unit fractions whose sum equals 1”, *Discrete Mathematics* **300** (2005), 213–217. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X05000889), [DOI](https://doi.org/10.1016/j.disc.2004.11.007).

The abstract concerns additional requirements on denominators, including their being large, odd, or even. The full text was not obtained. ScienceDirect returned HTTP 403; the Elsevier API supplied metadata, while its FULL view required authorization. The paper cannot responsibly be excluded as relevant prior art on that basis.

There is a bibliographic trap: a ResearchGate record combines the 2005 volume/pages with the DOI and abstract of Burshtein's distinct 1973 paper having the same title. Those records must not be used to describe the 2005 results.

### Burshtein, 2007: explicit classical congruence lemma located

N. Burshtein, “The equation \(\sum_{i=1}^{9}1/x_i=1\) in distinct odd integers has only the five known solutions”, *Journal of Number Theory* **127** (2007), 136–144. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0022314X07000510), [DOI](https://doi.org/10.1016/j.jnt.2007.01.007).

The article text available through an [author-uploaded research copy](https://www.researchgate.net/publication/317035370_The_equation_of_9_distinct_reciprocals_with_odd_integers_whose_sum_equals_1_has_only_the_five_known_solutions) includes Lemma 1 and its corollaries on p. 137. If the maximal power \(p^\alpha\) occurs in denominators \(p^\alpha m_1,\ldots,p^\alpha m_s\), then \(p\) divides the elementary symmetric polynomial of degree \(s-1\) in the \(m_i\). In particular \(s\geq2\). The prime-duplication observation in the present note is therefore not a new lemma.

## Later checks and limits of the audit

Graham's 2013 [survey](https://mathweb.ucsd.edu/~ronspubs/13_03_Egyptian.pdf) was checked for the relevant topics and references. It discusses Croot, Martin, and restrictions on denominator factorizations; no additional theorem yielding the present tradeoff was located there.

Searches for the problem number, the defining excess, and exponential denominator restrictions found no later primary theorem resolving problem 295. A recent [computational report](https://erdosproblemaday.com/day/295-k17-exact) explicitly leaves the asymptotic question open. Its search results have not been independently verified and are not mathematical support for the present research claim. A 2026 [preprint on reciprocal subsum approximation](https://arxiv.org/abs/2607.04157) concerns a different Erdős–Graham question and is not a solution to 295.

## Assessment

The existing proposition is a valid-looking necessary-condition result whose proof was audited separately. This source audit gives no basis for presenting it as substantial new research suitable for submission. Its ingredients are established, and its restricted cases partly overlap stronger classical results. The precise subexponential-denominator conclusion may be an unstated corollary or a modest refinement; the search cannot distinguish those possibilities while the 1971 and 2005 proofs remain unread.

Any stronger candidate should state its exact distinction from the known linear-cap results, and should be reviewed mathematically before a novelty claim. A full resolution would have to exclude the exponentially large outlier denominators that the current proof allows.

### Follow-up: proposed polynomial-cap coefficient

The parent research task proposed a sharper lower bound of the form
\[
|A|-(e-1)N\geq(c_{\lfloor B\rfloor}-o(1))N/\log N
\quad\text{when }\max A\leq N^B,\quad B>1,
\]
using a weighted optimization between omitting the small multiples of a prime and assigning that prime to a superlinear denominator. No statement with this polynomial-cap dependence or its proposed coefficient was found in the sources inspected or in focused searches for polynomially bounded denominators and bounded excess. The Croot and Martin statements described above do not imply it directly. This is a distinction in formulation, not a conclusion of novelty or a verification of the proposed proof.

## Addendum: classical upper bounds and the polynomial-cap comparison

The focused follow-up found an important correction to the historical comparison above: the unrestricted estimate
\[
k(N)\leq(e-1)N+O(\sqrt N)
\]
is an immediate corollary of Vose's classical theorem. It should not be presented as new research or confused with the proposed lower bound under a polynomial cap.

### Vose's result: verified through later primary papers

M. D. Vose, “Egyptian fractions”, *Bulletin of the London Mathematical Society* **17** (1985), 21–24, [DOI](https://doi.org/10.1112/blms/17.1.21). The original publisher PDF request led back to an abstract/access page, so the original proof remains unread.

Two later primary papers explicitly state the uniform result needed here. G. Tenenbaum and H. Yokota, “Length and denominators of Egyptian fractions, III”, *Journal of Number Theory* **35** (1990), 150–156, [author-hosted PDF](https://tenenb.perso.math.cnrs.fr/PPP/Egyptian.pdf), define expansions with strictly increasing denominators on p. 150 and state in equation (2), p. 151, that the maximum minimal length over all numerators with denominator \(b\) is \(O(\sqrt{\log b})\), uniformly for \(b\geq3\), citing Vose. Their own theorem simultaneously achieves length \((1+o(1))\log b/\log\log b\) and maximum denominator at most \(4b(\log b)^2\log\log b\). These bounds concern the denominator of the input rational, which need not be polynomial in the minimum denominator in problem 295.

W. van Doorn and Q. Tang, “The smallest denominator not contained in a unit fraction decomposition of 1 with fixed length”, [arXiv:2512.22083v2](https://arxiv.org/abs/2512.22083), revised 24 May 2026, restate Vose's theorem as Lemma 2.2, pp. 3–4. Distinctness, applicability to every \(a/b\in(0,1)\), and the absolute bound \(C\sqrt{\log b}\) are explicit. Section 3, p. 6, identifies this as the current best uniform bound. Searches for later improvements found no primary counterexample to that description. This is a checked contemporary statement, not an exhaustive guarantee about all unpublished work.

### The elementary corollary for problem 295

Let \(q\) be the least integer for which \(\sum_{n=N}^{q}1/n\geq1\). Harmonic estimates give \(q=eN+O(1)\). If equality holds, the displayed upper bound is already satisfied. Otherwise put
\[
R=1-\sum_{n=N}^{q-1}\frac1n=\frac ab,
\qquad 0<R<\frac1q.
\]
Its reduced denominator divides \(\operatorname{lcm}(1,\ldots,q-1)\), so \(\log b=O(N)\). Vose gives a representation of \(R\) with \(O(\sqrt N)\) distinct positive unit fractions. Each such denominator exceeds \(q\), since each individual term is at most \(R<1/q\). Thus they are disjoint from the initial block, proving the corollary. This deduction uses only the classical theorem and the standard least-common-multiple estimate.

### A simultaneous exponential cap follows from Vose's divisor sequence

H. Yokota, “On a sum of divisors”, *Canadian Mathematical Bulletin* **35** (1992), 423–430, [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/422DDD1972CEF8DC6A7DF98EB7060A79/S0008439500010882a.pdf/on_a_sum_of_divisors.pdf), p. 424, specifies Vose's sequence
\(Q_j=2^{2\alpha j^2}\prod_{i=2}^{j}p_i^2\), with \(\log p_i\asymp i\), and proves in Corollary 1 that every integer below \(Q_j\) is a sum of \(O(\sqrt{\log Q_j})\) distinct divisors of \(Q_j\). This also confirms that Yokota's “improvement” does not improve Vose's uniform length bound: it proves the matching lower bound for the divisor problem on this sequence.

Here is a further elementary deduction from that result. Choose \(Q_{j-1}<b\leq Q_j\); then \(\log Q_j=\log b+O(\sqrt{\log b})\). Write \(aQ_j=b\ell+r\), \(0\leq r<b\), and expand both \(\ell\) and \(r\) into distinct divisors of \(Q_j\). The resulting denominators in \(\ell/Q_j\) are at most \(Q_j\); those in \(r/(bQ_j)\) exceed \(Q_j\), since each divisor used is at most \(r<b\). Therefore the two groups are disjoint, with total length \(O(\sqrt{\log b})\) and maximum at most
\[
bQ_j\leq b^2\exp(O(\sqrt{\log b})).
\]
Applied to the residual above, this gives maximum \(\exp(O(N))\) simultaneously with excess \(O(\sqrt N)\). This quantitative cap is a deduction from the inspected divisor-sequence result, not a quotation from the inaccessible Vose article.

### Significance of the proposed coefficient

The concrete proposed constants are \(c_1\approx1.7903394414\), \(c_2\approx1.0953373458\), and \(c_t=e\log(1+1/t)\) for \(t\geq3\). The initial proposal used \(t=\lfloor B\rfloor\); a subsequent proposal under independent proof review improves the integer endpoints to \(t=\lceil B\rceil-1\) even for \(\max A\leq K N^B\), with fixed \(K>0\). No inspected primary result supplies those constants or directly implies either polynomial-cap theorem. The arithmetic mechanism and harmonic optimization have substantial classical precedent, however, so the available evidence supports neither an assertion of novelty nor an assertion that this constitutes substantial publishable progress.

For each fixed \(B>1\), Croot's interval construction does supply a polynomial-cap upper excess \(O(N\log\log N/\log N)\), since its maximum is \(O(N)<N^B\) eventually. Thus the proposed \(\Omega_B(N/\log N)\) lower bound would leave a factor \(\log\log N\) between the available constrained upper and lower orders. The 1971 \(O(N/\log N)\) unrestricted upper estimate cannot be used as a matching polynomial-cap construction without checking its denominators. The residual constructions above permit exponential denominators, and the original 1971 proof remains unchecked. Claiming order-sharpness under a polynomial cap is consequently unsupported by this audit.

### Prime-support component refinement: bounded follow-up search

The endpoint proposal uses a hypergraph whose vertices are large prime divisors and whose edges are denominator supports. Focused searches for Egyptian fractions, prime supports, graphs, hypergraphs, and connected components found no matching primary lemma. Two nearby primary sources were inspected enough to distinguish their statements and methods:

- S. Butler, P. Erdős and R. Graham, “Egyptian fractions with each denominator having three distinct prime divisors”, *Integers* **15** (2015), A51, [journal PDF](https://math.colgate.edu/~integers/p51/p51.pdf). Its existence theorem uses intervals in subset sums of products of primes and Olson's residue theorem; its quantitative estimate concerns the represented integer, not a minimum-denominator asymptotic. Neither its theorem nor Lemma 1 provides the proposed component/arity obstruction.
- J. Machacek, “Egyptian fractions and prime power divisors”, *Journal of Integer Sequences* **21** (2018), Article 18.3.7, [preprint](https://arxiv.org/abs/1706.01008). The inspected introduction and main statements concern prime-power pseudoperfect numbers, Giuga numbers, and recursions among special factorizations. They do not give the proposed quantitative cap theorem.

This is a bounded search result. It is not a claim that the component argument has never appeared, and it does not verify the proposed endpoint proof.

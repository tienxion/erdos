# Follow-up source access and posting assessment

Read-only audit on 4 September 2026. No login, posting, messaging, or contact with authors was attempted. No credentials were used or stored. This file supplements `literature_audit.md`; it does not certify novelty or a solution of problem 295.

## Outcome

The original E2232 solution (1971) and Burshtein (2005) remain unread. The alternate-source search recovered more specific information about Burshtein's 2005 results from his later primary papers, but it did not recover either original full text. Those access limits should remain explicit in any account of the literature search.

The Vose observation is mathematically suitable in substance for a concise, attributed literature remark: it updates the unrestricted upper-bound comparison, without claiming to resolve problem 295 or constitute a new theorem. Whether it should be posted now additionally depends on the user independently understanding/checking it and whether the live discussion already contains the observation. Neither condition can be certified by this agent. The live problem and forum routes returned access errors in this environment, and the browser tool reported that no browser was available.

## E2232: alternate archive and citation search

H. D. Ruderman, P. Erdős and E. G. Straus, “E2232”, *American Mathematical Monthly* **78** (1971), 302–303, [DOI](https://doi.org/10.2307/2317539).

The [Rényi Institute Erdős archive](https://www.renyi.hu/~p_erdos/Erdos.html) was searched by problem identifier and page numbers, and its 1971 entries were inspected. No E2232 entry or linked copy was found. The archive does list Erdős–Straus, “Some number theoretic results”, *Pacific Journal of Mathematics* **36** (1971), 635–646; that is a different paper and must not be substituted for the Monthly solution.

Exact-title, identifier, author, and page-number searches found the [JSTOR issue contents](https://www.jstor.org/stable/i315024), bibliographic citations, and a recent computational report linking back to JSTOR. No legitimate alternate full text was located. The previously unsuccessful JSTOR article/PDF requests were not repeated. The directly inspected Erdős–Graham 1980 monograph, p. 35, remains the primary confirmation of the historical bounds and their attribution; it does not reveal the 1971 construction's denominator cap.

## Burshtein 2005: specific results recovered indirectly

N. Burshtein, “On distinct unit fractions whose sum equals 1”, *Discrete Mathematics* **300** (2005), 213–217, [publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X05000889), [DOI](https://doi.org/10.1016/j.disc.2004.11.007).

The author-profile/repository and citation searches did not locate the original full text. The ResearchGate record still conflates the 2005 bibliographic data with the 1973 DOI and abstract, and is explicitly marked as having no full text. It is not reliable evidence about the 2005 paper's complete contents. The earlier blocked publisher/API requests were not repeated.

The following later primary papers narrow the picture:

- Burshtein, “An improved solution of \(\sum 1/x_i=1\) in distinct integers when \(x_i\nmid x_j\) for \(i\ne j\)”, *Notes on Number Theory and Discrete Mathematics* **16**(2) (2010), 1–4, [journal PDF](https://nntdm.net/papers/nntdm-16/NNTDM-16-2-01-04.pdf). Its introduction explicitly attributes a 68-term divisibility-antichain example to reference [4], the 2005 paper. Its own example has 52 terms. Its proof groups terms by prime multiples and cancels the corresponding prime in each partial sum; this is further prior art for the basic congruence mechanism.
- Burshtein, “Improving solutions of \(\sum 1/x_i=1\) with restrictions as required by Barbeau respectively by Johnson”, *Discrete Mathematics* **306** (2006), 1438–1439, [publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X06002779). The abstract independently attributes the 68-term antichain example to the 2005 article, while distinguishing it from the 79-term 1973 example.
- Burshtein, “On distinct integers the sum of whose reciprocals equals 1, 2, 3”, *Annals of Pure and Applied Mathematics* **20**(1) (2019), 13–19, [author-uploaded text](https://www.researchgate.net/publication/334721075_On_Distinct_Integers_the_Sum_of_Whose_Reciprocals_Equals_1_2_3). Its introduction, pp. 13–14, attributes to reference [7] (2005) two all-odd examples with smallest denominator 5 and lengths 21 and 23. It also attributes small all-even examples to that reference. The journal PDF was indexed but not retrievable; the author-uploaded text and its bibliography were inspected.

Other inspected citing papers concerned finite semiprime examples or reciprocal identities allowing repeated denominators. They did not supply an asymptotic excess/max-denominator theorem. None of these partial reconstructions allows us to conclude that Burshtein 2005 contains no relevant additional result.

## Public contribution rules: verified statements and access limits

The current forum homepage could not be fetched directly: the [policy link](https://www.erdosproblems.com/forum/) from the public guidance wiki returned HTTP 403. A later focused search recovered the official homepage's four rules from an indexed copy crawled about two months earlier. Rule 1 says: “The contents of all comments, including any mathematical claims, should be independently verified by a human before posting here.” It also requires disclosure of AI assistance. Rule 2 prohibits posting mathematics the user does not understand. Rule 3 directs long proofs and partial proofs to an external PDF, with the same requirements that the human user read and understand it. Rule 4 points proposed AI solvers to the guidance wiki. This is direct evidence of the site's published rules from the indexed copy; it is not a live September 2026 verification.

The following public statements by the site's moderators were also available through indexed copies:

- Thomas Bloom, 13 May 2026, 12:50, [AI Contributions thread](https://www.erdosproblems.com/forum/thread/AI%20Contributions), says AI-generated solutions remain permitted when the user has understood the proof or it has been formalized. Such announcements should be brief and link to an external PDF. An explanatory summary is encouraged only when written by the user after understanding the proof. The same post discourages dumping AI critiques and low-effort AI replies into the discussion.
- Terence Tao, 15 March 2026, [problem 709 discussion](https://www.erdosproblems.com/forum/thread/709), reiterates AI disclosure and favors shorter, human-written summaries. Bloom, 3 May 2026, [problem 881 discussion](https://www.erdosproblems.com/forum/thread/881?order=newest), asks for clear disclosure of how AI contributed, including when the proof was entirely generated by GPT.
- Tao's [18 October 2025 MathOverflow Meta answer](https://meta.mathoverflow.net/questions/6285/proposal-to-permit-verified-numerical-ai-output-as-a-component-to-a-mathoverflow) reproduces the then-current site policy: disclosure, independent checking by the user, and reasonable length were conditions for AI-assisted comments. This is historical corroboration from a site moderator, not a substitute for the complete current policy.
- The public [guidance wiki](https://github.com/teorth/erdosproblems/wiki/What-to-do-when-I-think-I-managed-to-get-AI-to-solve-an-Erd%C5%91s-problem%3F), last updated 30 June 2026 and now marked as no longer maintained, recommends understanding the proof and its context, reading primary literature, and checking how the method differs from prior work before announcing a solution. It separately recommends avoiding rushed announcements.

These statements do not impose a blanket ban on AI-assisted mathematics. They do place responsibility for understanding, checking, attribution, and disclosure on the posting user. Independent AI reviews are not evidence that a human has checked or understood the result.

## Assessment of a separate Vose literature remark

The factual observation is
\[
k(N)\leq(e-1)N+O(\sqrt N),
\]
as a classical corollary of Vose's uniform short-expansion theorem. The proof and primary-source verification are already given in `literature_audit.md`: take the consecutive harmonic block immediately before its sum reaches one; its positive residual has reduced denominator \(b\) with \(\log b=O(N)\); Vose expands that residual into \(O(\sqrt N)\) distinct unit fractions, each beyond the initial block. The equality case requires no residual.

This is directly relevant to problem 295, correctly attributed, and compact enough for a literature discussion. It says nothing about a polynomial cap and does not prove that the excess diverges. The mathematical content can therefore stand separately from the proposed new constrained theorem, whose novelty remains uncertain.

A responsible contribution would identify Vose 1985, point to the accessible primary restatements (especially Tenenbaum–Yokota 1990, p. 151, equation (2)), explain the short residual deduction, and disclose the AI-assisted source search and derivation. It should not be labeled a solution or novel improvement. The user should formulate the actual comment after checking the sources and argument themselves, consistent with the moderator statements above.

The indexed June 2026 page showed no comments on problem 295, but that is insufficient to establish the current discussion state. No claim is made that the site presently omits the observation; a live check is still needed before any submission. This audit recommends keeping the proposed theorem private for further work and treating the Vose observation, if eventually posted, only as a modest attributed literature correction.

## Nearlinear denominator caps: a known subrange and the remaining comparison

The proposed new statement under review is that, for a representation with minimum denominator at least \(N\), maximum at most \(N\exp G\), and excess \(D=k-(e-1)N\),
\[
D\geq(1-o(1))\frac{N}{\log N}\log\!\left(\frac{\log N}{G+\log\log N}\right)
\]
when the expression in parentheses tends to infinity. This audit has not checked its proof.

There is an important classical overlap. Croot, *On unit fractions with denominators in short intervals*, [journal PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83061), p. 105, proves that a prime dividing any denominator is at most \((1+o(1))M/\log M\), where \(M\) is the maximum denominator. His Lemma 4, pp. 106–107, explicitly estimates the missing reciprocal mass associated with prime divisors above \(N/\log^\alpha N\), for fixed \(\alpha>0\) and on any fixed interval \((N,cN)\). If \(M\leq N(\log N)^A\) with fixed \(0<A<1\), these results already imply the order
\[
D\gg_A N\log\log N/\log N.
\]
This is a deduction from the cited results, not a theorem stated in that form by Croot. For example, use the forbidden denominators in \((N,cN)\) with any fixed \(1<c<e\); replacing their reciprocals with denominators beyond the initial block loses a fixed positive fraction of their reciprocal mass. Croot's linear-interval construction supplies the matching upper order. Therefore an order-of-growth claim for this subrange should be described as a classical corollary. The proposed coefficient 1, as opposed to a coefficient depending on \(1-A\), requires the stronger proposed argument.

The same cutoff becomes ineffective for excluding core denominators once \(M/\log M\) is comparable with or exceeds \(N\), which includes fixed \(A\geq1\), as well as \(G=(\log N)^\beta\) with \(0<\beta<1\). Neither Croot's stated interval theorem nor Martin's stated maximum-denominator/cardinality theorem directly gives the proposed lower bounds in these larger ranges. The focused indexed search located no primary statement of that wider cap/excess relation. This is limited negative search evidence, not a novelty determination; the unread 1971 and 2005 sources remain material gaps. The proof also uses the same classical positive-numerator cancellation underlying Croot and Martin, with additional control of the number of selected prime multiples.

For the two specific cap families \(N(\log N)^A\) and \(N\exp((\log N)^\beta)\), Croot's construction fits eventually and would give the matching upper order if the proposed lower bound is valid. Do not state a matching upper bound for every \(G\geq0\) in the general displayed range: very small caps, including \(G=0\), need not admit any representation at all.

## Prime elimination in the proposed upper construction: explicit primary prior art

The recursive prime-power cancellation is an established method. Martin, *Denser Egyptian fractions*, [journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa95/aa9533.pdf), §5, pp. 248–252, explicitly attributes its supporting lemmas to Croot. In Martin's formulation, Lemmas 14–15 choose two distinct cofactors \(m_1,m_2\in[(q-3)/2,q)\), with \(p\nmid m_1m_2\), for an odd prime power \(q=p^e\geq5\), so their reciprocal sum has any prescribed residue modulo \(p\). Subtracting \(1/(qm_1)+1/(qm_2)\) then decreases the largest prime power of the residual denominator. Lemma 16 handles small prime powers with one fraction. Proposition 7 iterates the process, and distinctness between stages follows from the largest prime power of each newly used denominator. These are concrete antecedents, not merely a resemblance in terminology.

The cited source is E. S. Croot III, *On some questions of Erdős and Graham about Egyptian fractions*, *Mathematika* **46** (1999), 359–372, [publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0025579300007828), [author PDF](https://ecroot.math.gatech.edu/erdos_graham.pdf). Its author copy was obtained and visually inspected. The main theorem concerns which integers are representable with all denominators up to \(x\); it is a different extremal problem. The recursive cancellation is explicit in the proof of Proposition 1, author-copy pp. 7–8. Lemma 2, stated on p. 4, is the antecedent of the two-cofactor device; Martin's proof is the clearer formulation for the present adaptation.

The audit led to this useful deduction for independent review: scale the two-cofactor construction by a power of two \(2^t\asymp K N^2/q^2\), with \(K\) a sufficiently large fixed constant. Each correction denominator then has order \(N^2\), regardless of \(q\leq eN+O(1)\), and each correction has reciprocal mass \(O(N^{-2})\). At most \(O(N/\log N)\) stages are needed, so the total correction mass is \(o(1/N)\). Ordering only the odd prime powers keeps any newly introduced odd prime powers smaller than the current one; the power of two does not obstruct this descent. The final power of two in the residual denominator remains \(O(N^2)\). Combined with the independently developed trick of reserving the largest power of two in the initial harmonic block, this suggests an \(O(N/\log N)\) excess construction with maximum \(O(N^2)\). This is an adaptation of explicit classical lemmas, not a theorem located verbatim in the literature. Its proof and the parent task's further refinement to the exact cap \(N^2\) are being checked separately.

For comparison, Eppstein's *Egyptian fractions with denominators from sequences closed under doubling*, *Journal of Integer Sequences* **24** (2021), Article 21.8.8, [journal PDF](https://cs.uwaterloo.ca/journals/JIS/VOL24/Eppstein/eppstein2.pdf), uses the older binary remainder method, attributed there to Stewart 1954. Its theorem concerns productive sequences closed under doubling; it does not provide the present cap/excess estimate. Bleicher–Erdős, *Denominators of Egyptian fractions*, *Journal of Number Theory* **8** (1976), 157–168, [author archive](https://renyi.hu/~p_erdos/1976-09.pdf), studies the least possible maximum denominator as a function of the input fraction's reduced denominator, using divisor constructions. Its stated bounds likewise do not give the desired polynomial cap in the minimum denominator of a representation of one.

Focused searches for quadratic caps, \(k(N)\), minimum versus maximum denominator, and the alternate descriptive title “Representation of 1 by Egyptian fractions” found no primary statement of the simultaneous quadratic-cap/excess estimate. No claim of novelty follows. In particular, the unread two-page Erdős–Straus 1971 solution remains an especially plausible source for a short elementary construction of this kind. The defensible description at this point is an explicit constrained consequence of classical methods, with the precise earlier occurrence unresolved.

# Polynomial-cap constructions with excess of order N/log N

Research derivation, 4 September 2026. The constructions below are proved here, but their novelty has not been established. In particular, the original 1971 Erdős--Straus proof remains inaccessible in the current source audit and may contain these constructions or equivalent denominator estimates. This document must not be presented as a new solution of Erdős problem 295 or as submission-ready work.

The final section improves the initial cubic construction to the exact quadratic ceiling \(M\le N^2\), using the classical Croot--Martin two-fraction lemma. It gives upper coefficient \(4-(e/2)\log2\). The initial cubic proof is retained because it is elementary and records the earlier construction accurately. No corresponding order-matching construction for every \(1<B<2\) has been established here.

## The construction theorem

For every sufficiently large integer \(N\), there is a finite set \(A\) of distinct integers such that
\[
N\le a\le N^3\quad(a\in A),
\qquad
\sum_{a\in A}\frac1a=1,
\]
and
\[
\boxed{
|A|\le(e-1)N+(e+o(1))\frac N{\log N}.
} \tag{1}
\]
The argument is constructive using rational arithmetic and modular inverses. Its asymptotic count uses the prime number theorem. No numerical search or unverified cancellation step is required.

Together with the independently proved lower bound in [the consolidated note](quantitative_obstructions.md), this establishes
\[
k_3(N)-(e-1)N=\Theta(N/\log N), \tag{2}
\]
where \(k_3(N)\) denotes the minimum length with all denominators in \([N,N^3]\). More precisely, the available lower coefficient is
\(c_2=1.0953373458\ldots\), while (1) gives upper coefficient \(e\). The order statement likewise holds for every fixed ceiling \(N^B\), \(B\ge3\), using its corresponding positive lower coefficient. The constants are not matched.

## 1. Reserve the denominators needed for a final binary expansion

Let \(L\) be the unique endpoint immediately before the harmonic sum first reaches or exceeds one:
\[
\sum_{n=N}^{L}\frac1n<1,
\qquad
\sum_{n=N}^{L+1}\frac1n\ge1.
\]
Standard harmonic estimates give \(L=eN+O(1)\). In particular, \(L>2N\) for large \(N\). Let \(d\) be the largest power of two not exceeding \(L\). Then \(d\ge N\).

Start with
\[
A_0=([N,L]\cap\mathbb Z)\setminus\{d\},
\qquad S_0=\sum_{a\in A_0}\frac1a.
\]
The missing mass \(R_0=1-S_0\) satisfies
\[
\frac1d<R_0\le\frac1d+\frac1{L+1}<\frac2d.
\tag{3}
\]
In particular, \(R_0>1/L\). Removing \(d\) is essential to the distinctness argument: it reserves the first possible denominator of the final binary expansion, while every larger power of two already exceeds \(L\).

## 2. Remove odd prime factors of the reduced denominator

Process the odd primes \(p\le L\) in descending order. At any stage, write the current positive reciprocal sum in lowest terms as
\[
S=\frac uv.
\]
If \(p\nmid v\), move to the next prime. Otherwise let \(p^a\parallel v\), and write \(v=p^a v_0\), with \(p\nmid uv_0\).

For this prime, choose a power of two \(Q_p\) satisfying
\[
\frac{N^3}{4Lp}\le Q_p<\frac{N^3}{2Lp}.
\tag{4}
\]
Such a power exists by taking the least power of two at least the left endpoint. The same \(Q_p\) may be used for every step at this prime.

Because \(p\) is odd, there is a unique integer \(c\in\{1,\ldots,p-1\}\) such that
\[
cQ_p\equiv-v_0u^{-1}\pmod p.
\tag{5}
\]
Put \(m=cQ_p\), and add the new unit fraction
\[
\frac1{p^a m}.
\]
The new sum is
\[
S+\frac1{p^a m}
=\frac{um+v_0}{p^a v_0m}.
\]
Its numerator is divisible by \(p\), while \(p\nmid v_0m\). Therefore the exponent of \(p\) in its reduced denominator drops by at least one.

Every odd prime factor of \(m\) divides \(c<p\). Consequently no prime already processed is reintroduced. Continue at \(p\) until it disappears from the reduced denominator, then proceed to the next odd prime.

## 3. The invariant controlling denominator size and termination

At every stage, every odd prime power dividing the current reduced denominator is at most \(L\). This is true initially because its denominator divides \(\operatorname{lcm}(1,\ldots,L)\). For the induction step, the new denominator is \(p^a cQ_p\):

- Its \(p\)-power is the already present \(p^a\le L\).
- Every other odd prime power divides \(c<p\le L\).
- \(Q_p\) is a power of two.

Taking a least common multiple and then reducing cannot increase the maximum prime power beyond these bounds. Thus the invariant is preserved.

Each odd prime requires at most \(\lfloor\log L/\log p\rfloor\) additions, and no larger prime returns after its elimination. The procedure therefore terminates, leaving a sum with denominator a power of two.

From (4) and \(c<p\),
\[
m=cQ_p<\frac{N^3}{2L}.
\]
Using \(p^a\le L\), every added denominator satisfies
\[
\boxed{p^a m<\frac{N^3}{2}.} \tag{6}
\]
Also,
\[
p^a m\ge pQ_p\ge\frac{N^3}{4L}>L
\tag{7}
\]
for sufficiently large \(N\). Hence no new denominator collides with the initial block.

The power of two in every new denominator is at most \(m<N^3/(2L)\); the initial power of two is at most \(L\). Thus the final reduced dyadic denominator is at most
\[
\max\{L,N^3/(2L)\}=O(N^2).
\tag{8}
\]
The factor \(c\) may itself be even, which is why (8) accounts for its two-adic valuation as well as that of \(Q_p\).

## 4. The total added mass stays below the reserved mass

At a fixed prime \(p\), the exponents \(a\) used by the procedure are distinct positive integers and decrease strictly. Since \(m\ge Q_p\), the total mass added at this prime is at most
\[
\frac1{Q_p}\sum_{a\ge1}\frac1{p^a}
=\frac1{Q_p(p-1)}
\le\frac{4Lp}{N^3(p-1)}.
\]
Therefore the total mass \(\Delta\) added while eliminating odd primes satisfies
\[
\Delta\le\frac{4L}{N^3}
\sum_{\substack{p\le L\\p\text{ odd}}}\frac p{p-1}
\le\frac{6L\pi(L)}{N^3}
=O\!\left(\frac1{N\log N}\right)
=o(1/L). \tag{9}
\]
Here the prime number theorem suffices; a standard elementary estimate \(\pi(L)=O(L/\log L)\) would also suffice for positivity.

In view of (3), the final residual after all odd-prime eliminations is
\[
R=1-S_0-\Delta>0,
\qquad R<R_0<2/d.
\tag{10}
\]
In particular, the running sum never reaches or crosses one during the procedure, since all additions are positive and their entire mass is already bounded by (9).

## 5. Finish with distinct powers of two

The number \(R\) in (10) is a positive dyadic rational whose reduced denominator satisfies (8). Expand it in its finite binary expansion:
\[
R=\sum_{j\in J}2^{-j},
\]
using distinct powers of two. Since \(R<2/d\) and \(d\) is itself a power of two, every denominator \(2^j\) in this expansion is at least \(d\), and therefore at least \(N\).

These denominators are disjoint from the initial block: its largest power of two was \(d\), which was removed, and every larger power of two exceeds \(L\). They are also disjoint from all fractions added during odd-prime elimination, each of which has an odd prime divisor. Their largest denominator is \(O(N^2)\), hence at most \(N^3\) for large \(N\).

Finally, the odd-prime additions are mutually distinct. Their largest odd prime is exactly the prime \(p\) being processed. Fractions added at different primes therefore have different denominators. At the same prime, their exact \(p\)-adic exponents are the different values \(a\), since \(p\nmid m\). This handles every possible collision.

The final set consequently consists of distinct integers in \([N,N^3]\), and its reciprocal sum is exactly one.

## 6. Count the terms

The initial block contributes \(L-N\) terms. The number of odd-prime additions is at most
\[
\begin{aligned}
\sum_{p\le L}\left\lfloor\frac{\log L}{\log p}\right\rfloor
&=\sum_{j\ge1}\pi(L^{1/j})\\
&=\pi(L)+O(\sqrt L\log L)\\
&=(e+o(1))\frac N{\log N}.
\end{aligned} \tag{11}
\]
Including the prime two in this upper estimate only enlarges it. The finite binary expansion in Section 5 has \(O(\log N)\) terms by (8). Since \(L=eN+O(1)\), these counts prove (1).

## What this settles and what remains uncertain

This is a complete upper construction with a cubic ceiling, and closes the order gap between the proved lower and upper bounds for every fixed exponent \(B\ge3\). It does not match the lower constants. The construction as proved does not supply the corresponding \(O_B(N/\log N)\) upper bound for every \(1<B<3\).

The unrestricted excess still need not diverge merely because its cubic-cap version does. This construction is consistent with the stronger classical unrestricted upper bound obtained from Vose's theorem.

The mathematical derivation here resulted from combining a descending prime-elimination scheme, powers of two chosen before solving the congruence, and a removed power of two reserved for the final expansion. These are elementary Egyptian-fraction techniques with substantial historical precedent. The earlier source audit did not inspect the original 1971 proof or every related upper-construction theorem. Accordingly, even though the proof is complete, the cubic cap and its coefficient must not be advertised as novel until that gap in the literature audit is resolved.

## Quadratic improvement using a classical two-fraction lemma

The following improvement supersedes the preceding restriction to exponents at least three.

**Theorem.** For every sufficiently large integer \(N\), there is a set of distinct integers \(A\subseteq[N,N^2]\) whose reciprocals sum to one and such that
\[
\boxed{
|A|\le(e-1)N+
\left(4-\frac e2\log2+o(1)\right)\frac N{\log N}.
} \tag{12}
\]
The upper coefficient is \(3.057915307318\ldots\). Together with the quadratic lower coefficient \(c_1=1.790339441409\ldots\) proved in the consolidated note, this gives
\[
(c_1-o(1))\frac N{\log N}
\le k_2(N)-(e-1)N
\le\left(4-\frac e2\log2+o(1)\right)\frac N{\log N},
\tag{13}
\]
where \(k_2(N)\) imposes the exact ceiling \(N^2\). Thus the order is determined for every fixed polynomial exponent \(B\ge2\). This is an order statement, not a matching-constant statement or a claim of novelty.

### A. The classical input and its elementary justification

We use the following form of the two-fraction device in G. Martin, *Denser Egyptian fractions*, Acta Arithmetica 95 (2000), Lemmas 14--15, printed pp. 249--250. Martin explicitly credits the underlying lemmas to Croot. The [journal text](https://matwbn.icm.edu.pl/ksiazki/aa/aa95/aa9533.pdf) was inspected in the saved local copy; the related [author preprint](https://arxiv.org/abs/math/9811112) is also available. The inverses in the statement below are modular inverses; their overbars are lost in the local plain-text extraction of the journal PDF.

If \(q=p^a\ge5\) is an odd prime power and \(t\) is any residue modulo \(p\), there are distinct integers \(m_1,m_2\), both coprime to \(p\), satisfying
\[
\frac{q-3}{2}\le m_1<m_2<q,
\qquad
m_1^{-1}+m_2^{-1}\equiv t\pmod p.
\tag{14}
\]
In particular, each \(m_i\ge q/5\), and every odd prime power dividing \(m_i\) is less than \(q\).

For completeness, when \(p\ge5\), take the \((p+3)/2\) integers just below \(q\). They are pairwise distinct and nonzero modulo \(p\). Their inverses form a set \(X\) with \(|X|=(p+3)/2\), so \(X\cap(t-X)\) has at least three elements. At most one corresponds to an equal pair, because \(2x=t\) has at most one solution. An unequal pair gives (14). Its members are at least \(q-(p+3)/2\ge(q-3)/2\). When \(p=3\), one has \(q\ge9\); the pairs
\[
(q-2,q-1),\quad(q-4,q-1),\quad(q-5,q-2)
\]
give inverse sums \(0,1,2\), respectively. This verifies the version needed here without treating the two-fraction mechanism as a new lemma.

### B. Select a core whose odd prime powers are at most N

Call an integer *eligible* if every odd prime power dividing it is at most \(N\). Powers of two are all eligible. For \(X\ge N\), define
\[
F_N(X)=\sum_{\substack{N\le n\le X\\n\text{ eligible}}}\frac1n.
\]
For \(X=eN+O(N/\log N)<3N\), the ineligible integers arising from primes exceeding \(N\) are exactly
\[
p\quad(N<p\le X),
\qquad
2p\quad(N<p\le X/2).
\]
All other ineligible integers have a divisor \(p^a>N\), with odd \(p\) and \(a\ge2\). There are \(O(\sqrt N\log N)=o(N/\log N)\) of these integers, because there are that many candidate higher prime powers below \(3N\), each having at most two multiples below \(3N\). Their reciprocal mass is \(o(1/\log N)\).

Set
\[
\mu=1+\frac12\log\frac e2
=\frac32-\frac12\log2,
\qquad
\nu=\frac{3e}{2}-2.
\]
The prime number theorem and partial summation give, uniformly for fixed real \(C\),
\[
\begin{aligned}
F_N\!\left(eN+C\frac N{\log N}\right)
&=\sum_{N\le n\le eN+CN/\log N}\frac1n
 -\sum_{N<p\le eN+CN/\log N}\frac1p\\
&\quad-\frac12\sum_{N<p\le(eN+CN/\log N)/2}\frac1p
 +o(1/\log N)\\
&=1+\frac{C/e-\mu+o(1)}{\log N}.
\end{aligned} \tag{15}
\]
Floors in the real endpoint affect only the error term.

In particular, eligible reciprocal sums cross one near this endpoint: choosing fixed \(C>e\mu\) makes (15) exceed one, while choosing \(C<e\mu\) makes it less than one. Thus define \(L+1\) to be the **first eligible denominator** at which the cumulative sum reaches or exceeds one. Equivalently, \(L\) is the integer immediately before the first crossing. Bracketing with \(C=e\mu\pm\eta\), then letting \(\eta\downarrow0\), proves
\[
L=eN+(e\mu+o(1))\frac N{\log N}.
\tag{16}
\]
This argument establishes existence directly. It does not invoke divergence of the reciprocal series over eligible integers, which for fixed \(N\) need not diverge.

Let \(d\) be the largest power of two at most \(L\), and take as the initial core all eligible integers in \([N,L]\), except \(d\). For large \(N\), \(L>2N\), so \(d\ge N\) and is an eligible core member before removal. The residual \(R_0\) satisfies
\[
\frac1d<R_0\le\frac1d+\frac1{L+1}<\frac2d.
\tag{17}
\]
The integer-endpoint definition avoids any assumption about gaps between consecutive eligible denominators: \(L+1\) is the next crossing term by definition.

The number of integers excluded by the large primes is
\[
\pi(L)+\pi(L/2)-2\pi(N)
=(\nu+o(1))\frac N{\log N}.
\]
The higher-power exclusions and the removed power of two contribute only \(o(N/\log N)\) further terms. Hence the core has size
\[
\begin{aligned}
k_0
&=(e-1)N+(e\mu-\nu+o(1))\frac N{\log N}\\
&=(e-1)N+\left(2-\frac e2\log2+o(1)\right)
                      \frac N{\log N}.
\end{aligned} \tag{18}
\]

### C. Eliminate the largest odd prime power

At each stage let \(q=p^a\) be the largest odd prime power dividing the reduced denominator of the running reciprocal sum \(S\). Initially all such prime powers are at most \(N\), by eligibility.

For \(q\ge5\), choose the dyadic integer \(Q\) as follows. If \(N^2/(2q^2)\le1\), take \(Q=1\). Otherwise take the least power of two at least \(N^2/(2q^2)\). Because \(q\le N\), this guarantees
\[
\frac{N^2}{2}\le Qq^2\le N^2. \tag{19}
\]
The upper bound is strict in the second case.

Write \(S=u/v\) in lowest terms and \(v=qv_0\), so \(p\nmid uv_0\). The residue of \(qS\) modulo \(p\) is well-defined and equals \(uv_0^{-1}\). Apply (14) with target
\[
t\equiv-Q(uv_0^{-1})\pmod p.
\tag{20}
\]
Add the two unit fractions
\[
\frac1{Qqm_1}+\frac1{Qqm_2}.
\]
Indeed,
\[
q\left(S+\frac1{Qqm_1}+\frac1{Qqm_2}\right)
\equiv uv_0^{-1}+Q^{-1}(m_1^{-1}+m_2^{-1})
\equiv0\pmod p.
\]
Thus the exponent of \(p\) in the reduced denominator drops. All odd prime powers introduced by \(m_1,m_2\) are smaller than \(q\), and \(Q\) is dyadic. The largest odd prime power in the reduced denominator therefore decreases strictly.

Every added denominator obeys the exact bounds
\[
\boxed{
\frac{N^2}{10}\le Qqm_i<N^2.
} \tag{21}
\]
The lower bound uses \(m_i\ge q/5\) and (19); the upper bound uses \(m_i<q\).

If the remaining largest odd prime power is \(q=3\), take \(Q\) to be the largest power of two at most \(N^2/6\). Choose \(a\in\{1,2\}\) so that
\[
a^{-1}\equiv-Q(3S)\pmod3,
\]
and add \(1/(3Qa)\). The target is nonzero because the current reduced denominator has exact three-adic exponent one, so such \(a\) exists. This removes the final odd prime factor, and
\[
N^2/4<3Qa\le N^2. \tag{22}
\]

There are at most \(\pi^*(N)\) stages, where \(\pi^*(N)\) counts prime powers at most \(N\): the largest odd prime power drops strictly at each stage. In particular, the process terminates. It uses at most
\[
2\pi^*(N)=(2+o(1))\frac N{\log N}
\tag{23}
\]
new terms. Their total reciprocal mass is
\[
\Delta\le\frac{20\pi^*(N)+4}{N^2}
=O\!\left(\frac1{N\log N}\right)=o(1/L).
\tag{24}
\]
Consequently the residual remains positive by (17), and is still less than \(2/d\).

### D. Distinctness, the binary finish, and the count

Each new denominator in a stage labeled \(q=p^a\) has largest odd prime-power divisor exactly \(q\): the factor \(q\) remains to its original exponent because \(p\nmid m_i\), and every other odd prime power in \(m_i\) is smaller. Thus different stages produce disjoint denominator sets. The two denominators within a stage are distinct because \(m_1\ne m_2\). Their lower bound \(N^2/10\) makes them larger than the core endpoint \(L\) for large \(N\).

After elimination, expand the positive dyadic residual in its finite binary expansion. As in the cubic construction, every binary denominator is at least the reserved \(d\), so it is at least \(N\) and disjoint from the initial core. It is disjoint from all added terms because they have odd prime divisors. Its denominator is at most \(N^2\): the maximum two-adic prime power among the initial and added denominators is at most their maximum, which is at most \(N^2\), and taking a least common multiple cannot increase that two-adic prime power.

This binary expansion uses only \(O(\log N)\) terms. Combining (18), (23), and this count proves (12), with every denominator between \(N\) and \(N^2\).

### E. Independent audit verdict

The filtered-core endpoint and its two leading constants, the sign and multiplier in (20), the exact quadratic cap, strict decrease of the maximal odd prime power, reciprocal-mass estimate, and all distinctness conditions have been checked. No mathematical gap was found.

The existence of the core was proved by the prime number theorem near \(eN\), without assuming divergence of the eligible reciprocal series. The integer endpoint \(L=(\text{first crossing denominator})-1\) also avoids any unjustified estimate on gaps in eligible denominators.

The pair lemma is classical and explicitly credited to Croot and Martin. The exact adaptation to this denominator ceiling and its constant may also have antecedents. A complete proof here is not a novelty certificate, and the missing historical full texts still prevent a confident priority assessment.

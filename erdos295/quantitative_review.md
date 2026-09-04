# Independent review of the strengthened prime obstruction

This is an internal proof audit, dated 4 September 2026. The argument below is mathematically valid subject to the stated asymptotic hypotheses. This review does not establish novelty or suitability for publication, and the argument does not settle Erdős problem 295.

## Verdict

Let \(A_N\) be a finite set of distinct integers at least \(N\), with reciprocal sum one. Write
\[
k=|A_N|,
\qquad D=k-(e-1)N,
\qquad b=\frac{e-1}{2},
\qquad M=\max A_N.
\]
If \(D=o(N/\log N)\), then the proposed product bound is correct:
\[
\liminf_{N\to\infty}\frac1N
 \log\prod_{\substack{a\in A_N\\a>N^2}}a\ge e. \tag{1}
\]
Also,
\[
\#\{a\in A_N:a>N^2\}
\le D+b+O\!\left(\frac{(D+1)^2}{N}\right). \tag{2}
\]
Consequently,
\[
\liminf_{N\to\infty}
\frac{(D+b)\log M}{N}\ge e. \tag{3}
\]
The last statement is slightly cleaner than introducing an unspecified additive \(o(D+1)\) in its coefficient. The proof below explains why removing that error is valid even when \(\log M/N\) is unbounded.

Here and below limits can be taken along any sequence of integers for which the indicated representations exist. A bounded-above \(D\) is a special case; the elementary harmonic estimate bounds \(D\) below.

## Exact finite inequalities

Put
\[
L=N+k-1=eN+D-1,
\quad I=[N,L]\cap\mathbb Z,
\quad \delta=\sum_{j=N}^{L}\frac1j-1.
\]
The ordering of the denominators implies \(\delta\ge0\). If
\(H=I\setminus A_N\) and \(E=A_N\setminus I\), then \(|H|=|E|\) and
\[
\delta=
\sum_{h\in H}\left(\frac1h-\frac1L\right)
+\sum_{a\in E}\left(\frac1L-\frac1a\right). \tag{4}
\]
All terms on the right are nonnegative.

Fix
\[
0<\varepsilon<1,
\qquad 0<\eta<e-2,
\qquad T>e,
\qquad u=(e-\eta)N.
\]
For sufficiently large \(N\), \(u<L<TN<N^2\). Equation (4) gives
\[
|H\cap[N,u]|\le
\frac{\delta}{1/u-1/L},
\qquad
s_T:=|A_N\cap(TN,\infty)|\le
\frac{\delta}{1/L-1/(TN)}. \tag{5}
\]

For a prime \(p\in(\varepsilon N,u]\), let
\(h_p=p\lceil N/p\rceil\). If \(p<N\), then \(N\le h_p<N+p<2N<u\). If \(p\ge N\), then \(h_p=p\le u\). Thus \(h_p\in I\) and lies uniformly away from its upper endpoint. Distinct primes in this range yield distinct \(h_p\) for large \(N\): a common value would be divisible by their product, which exceeds \(\varepsilon^2N^2>u\). Consequently, at most the first quantity in (5) of these primes have \(h_p\notin A_N\).

For each remaining prime, there is a selected denominator divisible by \(p\) in \([N,TN]\). In fact there must also be a selected denominator divisible by \(p\) above \(TN\). To prove this, let
\[
K=\lfloor T/\varepsilon\rfloor,
\qquad B=\operatorname{lcm}(1,\ldots,K).
\]
The sum of the reciprocals of all selected denominators at most \(TN\) divisible by \(p\) is
\[
\frac1p\sum_{m\in S}\frac1m=\frac{t}{pB},
\qquad \varnothing\ne S\subseteq\{1,\ldots,K\},
\]
where \(t\) is a positive integer bounded above by
\(B\sum_{m=1}^{K}1/m\), independently of \(N\). For large \(N\), \(p\) exceeds this bound and \(K\). Hence \(t/(pB)\) has reduced denominator divisible by \(p\). If no selected denominator above \(TN\) were divisible by \(p\), the sum of all other selected reciprocals would have denominator coprime to \(p\). Their sum could not be the integer one. This proves the claim.

Writing \(\vartheta(x)=\sum_{p\le x}\log p\), the product of denominators above \(TN\) therefore satisfies
\[
\log\prod_{a\in A_N\cap(TN,\infty)}a
\ge\vartheta(u)-\vartheta(\varepsilon N)
-\frac{\delta\log u}{1/u-1/L}. \tag{6}
\]
The denominators in \((TN,N^2]\) contribute at most \(2s_T\log N\) to the logarithm of this product. Thus, with
\(Q=\prod_{a\in A_N,\ a>N^2}a\),
\[
\boxed{
\log Q\ge\vartheta(u)-\vartheta(\varepsilon N)
-\frac{\delta\log u}{1/u-1/L}
-\frac{2\delta\log N}{1/L-1/(TN)}.
} \tag{7}
\]
Moreover, again directly from (4),
\[
\boxed{
r:=|A_N\cap(N^2,\infty)|
\le\frac{\delta}{1/L-1/N^2}.
} \tag{8}
\]
These finite inequalities isolate every loss in the proof. A global bound on the number of holes, such as \(|H|=O(\sqrt N)\) for bounded \(D\), is unnecessary.

## Harmonic expansion and uniformity

For \(|D|=o(N)\), the Euler--Maclaurin expansion gives
\[
\delta=\frac{D+b}{eN}
+O\!\left(\frac{(|D|+1)^2}{N^2}\right). \tag{9}
\]
This follows, for example, by subtracting
\(H_{N-1}=\log N+\gamma-1/(2N)+O(N^{-2})\)
from
\(H_L=\log L+\gamma+1/(2L)+O(L^{-2})\).

The condition \(\delta\ge0\) first rules out \(D\to-\infty\) while \(|D|=o(N)\), and then yields \(D\ge-b+O(N^{-1})\). In particular, \(D+1\) is bounded below by a positive constant for large \(N\), and \(|D|+1\) can be replaced by \(D+1\) in big-O estimates.

For each fixed \(\varepsilon,\eta,T\), both error terms on the right side of (7) are
\(O_{\varepsilon,\eta,T}((D+1)\log N)\). Under \(D=o(N/\log N)\), they are \(o(N)\). The prime number theorem gives
\[
\log Q\ge(e-\eta-\varepsilon-o(1))N.
\]
Take the lower limit first, and then let \(\eta,\varepsilon\downarrow0\), to obtain (1). There is no need to assert a numerator bound uniform as \(\varepsilon\downarrow0\): \(\varepsilon\) remains fixed during the limit in \(N\).

Substituting (9) into (8), using
\[
\frac1{1/L-1/N^2}=\frac L{1-L/N^2},
\]
gives (2). Equation (1) implies \(r\ge1\) eventually. If \(D\) stays bounded on a subsequence, (2) then gives \(D+b\ge1-o(1)\); if \(D\) is large, that lower bound is automatic. Thus \(D+b\) is bounded away from zero throughout the sequence for large \(N\). The error in (2) is consequently \(o(D+b)\). Finally,
\[
(e-o(1))N\le\log Q\le r\log M
\le(D+b)(1+o(1))\log M,
\]
which proves (3) by division. One should use this argument instead of dropping an \(o(1)\log M\) term without controlling its size.

The assertions are uniform over \(D\le d(N)\) for any specified function \(d(N)=o(N/\log N)\), with the harmonic lower bound understood. An unqualified common error function for every possible unspecified little-o rate is neither needed nor asserted.

## Discrete strengthening for bounded excess

Equation (1) implies that at least one denominator exceeds \(N^2\). Equation (2) therefore proves
\[
\boxed{\liminf D\ge1-b=\frac{3-e}{2}.} \tag{10}
\]
For a fixed upper bound \(D\le C\), define
\[
q=\lfloor C+b\rfloor.
\]
Since \(r\) is an integer, (2) implies \(r\le q\) for all sufficiently large \(N\), including when \(C+b\) is itself an integer. Therefore no such sequence exists when \(q<1\), and otherwise
\[
\boxed{\liminf\frac{\log M}{N}\ge\frac e q.} \tag{11}
\]
This is stronger than the continuous bound \(e/(C+b)\) whenever \(C+b\) is not an integer. It is a direct consequence of the same proof, not a distinct method.

## Scope and research significance

The argument gives a materially sharper necessary condition than the original constant 132 estimate: almost all prime logarithmic mass up to \(eN\) must occur in a bounded number of denominators above \(N^2\). The extension to \(D=o(N/\log N)\) is also valid.

Nevertheless, these are conditional size and divisibility constraints. A single unrestricted denominator can contain all required primes, and the original problem permits such denominators. The product lower bound and the known exponential upper bounds on denominators for a fixed number of remaining terms are consistent. Neither (10) nor (11) proves that \(D\to\infty\).

The constant \(e\) reflects the prime mass up to the endpoint \(L\sim eN\), so improving the original numerical constant by this method is conceptually natural. It should not be presented as submission-quality new progress until a primary-literature audit establishes novelty and a suitable independent contribution. This review verifies the argument; it makes no priority claim.

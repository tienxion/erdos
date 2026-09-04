# Independent audit: subquadratic denominator improvement

Date: 4 September 2026.

**Verdict:** the proposed multiplicity argument and the resulting integral lower bound are valid. This audit verifies the mathematics; it does not establish novelty. No literature search was performed for this subtask.

## Statement

Let \(A_N\subseteq[N,\infty)\) be finite sets of distinct integers with
\[
\sum_{a\in A_N}\frac1a=1,
\qquad k_N=|A_N|,
\qquad D_N=k_N-(e-1)N,
\qquad M_N=\max A_N.
\]
Fix \(1<B<2\) and \(K>0\), and suppose \(M_N\leq K N^B\). Set
\[
s=\left\lceil\frac1{B-1}\right\rceil,
\qquad
w(x)=\sum_{\substack{m\geq1\\1\leq mx\leq e}}
\left(\frac1{mx}-\frac1e\right),
\]
and define
\[
d_s=e\int_0^e\min\!\left(w(x),\frac se\right)\,dx.
\]
Then
\[
\liminf_{N\to\infty}\frac{D_N\log N}{N}\geq d_s.
\]
In particular \(s\geq2\), so this improves the corresponding constant \(d_1\).

A slightly more general conclusion holds: for any fixed integer \(s\geq2\), the condition
\[
M_N=o\!\left(N^{1+1/(s-1)}\right)
\]
implies the same lower bound with \(d_s\). In particular, \(M_N=o(N^2)\) is enough for \(d_2\).

## 1. Reduction to near-minimal length

It suffices to prove the result along any subsequence on which \(D_N\log N/N\) is bounded above. Otherwise the lower bound is immediate. The consecutive harmonic comparison gives \(D_N\geq-O(1)\), so on such a subsequence
\[
D_N=O(N/\log N).
\]
Put
\[
L=N+k_N-1=eN+D_N-1,
\quad I=[N,L]\cap\mathbb Z,
\quad H=I\setminus A_N,
\quad E=A_N\setminus I.
\]
Let
\[
\delta=\sum_{n=N}^{L}\frac1n-1\geq0.
\]
The exact identity \(|H|=|E|\) gives
\[
\delta=\sum_{h\in H}\left(\frac1h-\frac1L\right)
+\sum_{a\in E}\left(\frac1L-\frac1a\right).
\tag{1}
\]
All summands are nonnegative. Uniform harmonic estimates give
\[
\delta=\frac{D_N+(e-1)/2}{eN}
+O\!\left(\frac{D_N^2+|D_N|+1}{N^2}\right),
\]
so
\[
\delta=\frac{D_N}{eN}+o(1/\log N).
\tag{2}
\]
Also \(L/N\to e\).

## 2. A selected core prime requires at least s tail multiples

Fix \(\varepsilon>0\) and \(T>e\). Call a prime \(p\in(\varepsilon N,L]\) covered if some member of \(A_N\cap I\) is divisible by \(p\). Consider a covered prime.

Since \(B<2\), for all sufficiently large \(N\),
\[
p^2>M_N.
\tag{3}
\]
Thus every selected denominator divisible by \(p\) has valuation exactly one. Separate all such denominators into those at most \(TN\) and those above \(TN\). The first group contributes to their p-multiplied reciprocal sum a rational number
\[
\frac UV=\sum_{\substack{a\in A_N\\p\mid a,\ a\leq TN}}\frac1{a/p}>0
\]
in lowest terms. Here \(U,V\) are positive and bounded by a constant depending only on \(T,\varepsilon\): all quotients \(a/p\) are positive integers at most \(T/\varepsilon\). Coverage ensures the group is nonempty. Additional selected multiples between \(L\) and \(TN\) are included, which causes no problem and is necessary for the congruence.

Write the remaining multiples as \(p x_1,\ldots,p x_r\). Then
\[
x_i\leq\frac{M_N}{p}\leq\frac K\varepsilon N^{B-1}.
\tag{4}
\]
Multiplying the full reciprocal identity by \(p\), and reducing modulo \(p\), yields
\[
\frac UV+\sum_{i=1}^r\frac1{x_i}\equiv0\pmod p.
\]
All relevant denominators are invertible modulo \(p\), by (3), and the nonmultiples of \(p\) contribute zero after multiplication by \(p\).

Consequently, \(p\) divides the positive integer
\[
F=U\prod_{i=1}^r x_i
+V\sum_{i=1}^r\prod_{j\ne i}x_j.
\tag{5}
\]
It is not necessary for this numerator to be reduced. If \(r=0\), the empty-product convention gives \(F=U>0\), while the second sum is zero.

If \(r\leq s-1\), then
\[
r(B-1)<1
\]
by the definition of \(s\), including when \(1/(B-1)\) is an integer. Equations (4) and (5) give
\[
0<F=O\!\left(N^{r(B-1)}\right)=o(N)<p
\]
for sufficiently large \(N\), a contradiction. Therefore every covered prime has at least \(s\) selected multiples above \(TN\).

For the more general little-o hypothesis, the same conclusion follows from
\[
F=O\!\left(1+(M_N/(\varepsilon N))^{s-1}\right)=o(N)
\]
whenever \(r\leq s-1\). That hypothesis also implies (3).

## 3. Prime multiplicities convert into harmonic loss

No denominator can contain two distinct primes exceeding \(\varepsilon N\), because their product exceeds \(\varepsilon^2N^2>M_N\) for sufficiently large \(N\). Thus tail denominators assigned to different covered primes are disjoint. If \(q\) is the number of covered primes and \(r_T=|A_N\cap(TN,\infty)|\), then
\[
r_T\geq sq.
\tag{6}
\]
The same disjointness applies to members of the core interval.

For a prime in the chosen range define
\[
W_N(p)=\sum_{\substack{m\geq1\\N\leq mp\leq L}}
\left(\frac1{mp}-\frac1L\right).
\]
If the prime is uncovered, all these multiples are holes. If it is covered, its \(s\) distinct assigned tails each cost at least \(1/L-1/(TN)\) in (1). It follows that
\[
\delta\geq\sum_{\varepsilon N<p\leq L}
\min\!\left(W_N(p),s\left(\frac1L-\frac1{TN}\right)\right).
\tag{7}
\]
No cost is counted twice.

For fixed \(\varepsilon,T\), the prime number theorem and \(L/N\to e\) now give
\[
\liminf_{N\to\infty}(\log N)\delta
\geq\int_\varepsilon^e
\min\!\left(w(x),s\left(\frac1e-\frac1T\right)\right)\,dx.
\tag{8}
\]
There are only finitely many multiplier boundaries on \([\varepsilon,e]\). Away from small neighborhoods of these points, \(N W_N(p)\) converges uniformly to \(w(p/N)\); the bounded integrands and the prime number theorem control the neighborhoods. Thus integer endpoints introduce no extra assumption.

Combining (2) and (8), then taking \(T\to\infty\) and \(\varepsilon\downarrow0\), proves the statement. The final integrand is bounded by \(s/e\), so the limit at zero is harmless.

## 4. Size and numerical checks of the constant

As \(x\downarrow0\), harmonic summation gives
\[
\sum_{1\leq mx\leq e}\frac1m=1+O(x),
\qquad
|\{m:1\leq mx\leq e\}|=\frac{e-1}{x}+O(1).
\]
Hence
\[
w(x)=\frac1{ex}+O(1).
\]
Since \(z\mapsto\min(z,s)\) is 1-Lipschitz,
\[
d_s=\int_0^e\min(1/x,s)\,dx+O(1)
=\log s+O(1),
\]
with the implied constant independent of \(s\). Also \(d_s\) is strictly increasing: on a sufficiently small positive interval, both caps are active, so increasing \(s\) increases the integral strictly.

A numerical sanity check, integrating the reciprocal-linear pieces between multiplier breakpoints and cap crossings, gives
\[
\begin{array}{c|c}
s&d_s\\\hline
1&1.790339441409\\
2&2.595167411913\\
3&3.020349046705\\
4&3.314510100658
\end{array}
\]
These decimals are not required by the proof; the integral defines the constants exactly.

## Limits of this audit

This proves a lower bound for representations under a specified restriction on their largest denominator. It neither bounds the unrestricted function \(k(N)\) from below by \(d_sN/\log N\) nor excludes the exponential tails allowed in problem 295. Novelty requires a separate literature comparison.


## 5. Exact evaluation of d2

The following calculation verifies the headline constant without reliance on numerical quadrature:
\[
\boxed{
\begin{aligned}
d_2=e\biggl[&\frac{19}{20}\log\frac{20}{19}
+\frac{77}{60}\log3
+\frac{13}{12}\log\frac{15}{13}\\
&+\frac73\log\frac43+\log2\biggr]-\frac{11}{2}.
\end{aligned}}
\tag{9}
\]
It gives \(d_2\approx2.595167411912779\).

### Excluding an infinite collection of small-x pieces

For \(1/(m+1)<x<1/m\), the lower multiplier is \(m+1\). While this multiplier remains fixed, \(w(x)\) decreases as \(x\) increases. At an upper-multiplier boundary \(x=e/j\), the disappearing summand is zero, so there is no jump there. At \(x=1/m\), including the new lower multiplier produces an upward jump. Therefore the left limit at \(1/m\) supplies a lower bound on this entire open interval:
\[
w(x)\geq m\sum_{j=m+1}^{\lfloor em\rfloor}\frac1j
-\frac{\lfloor em\rfloor-m}{e}.
\]
The summand \(m/t-1/e\) is nonnegative and decreasing for \(m+1\leq t\leq em\), so integral comparison gives the lower bound
\[
g(m)=\int_{m+1}^{em}\left(\frac mt-\frac1e\right)dt
=\frac{m+1}{e}-m\log(1+1/m).
\]
For real \(m\geq4\),
\[
g'(m)=\frac1e-\log(1+1/m)+\frac1{m+1}
>\frac1e-\frac1{m(m+1)}>0.
\]
Moreover,
\[
g(4)=\frac5e-4\log(5/4)>\frac5e-1>\frac2e,
\]
using \(\log(5/4)<1/4\) and \(e<3\).

For \(m=3\), direct evaluation gives
\[
3\sum_{j=4}^{8}\frac1j-\frac5e
=\frac{743}{280}-\frac5e>\frac2e,
\]
because \(e>8/3\) implies \(7/e<21/8=735/280\). This proves
\[
w(x)\geq2/e\qquad(0<x\leq1/3).
\]
Values at the lower-multiplier endpoints also satisfy the inequality because the jump is upward.

### The seven uncapped pieces

On \(x>1/3\), the remaining multiplier breakpoints are finite. Directly summing the available multipliers shows that, except for immaterial endpoints,
\[
\{x\in(0,e):w(x)<2/e\}
=\left(\frac{19e}{120},\frac12\right)
\cup\left(\frac{13e}{60},1\right)
\cup\left(\frac{3e}{8},e\right).
\tag{10}
\]
On each row below, \(w(x)=A/x-n/e\):

| Left endpoint \(a\) | Right endpoint \(b\) | \(A\) | \(n\) |
|---|---|---:|---:|
| \(19e/120\) | \(e/6\) | \(19/20\) | 4 |
| \(e/6\) | \(1/2\) | \(47/60\) | 3 |
| \(13e/60\) | \(e/4\) | \(13/12\) | 3 |
| \(e/4\) | \(e/3\) | \(5/6\) | 2 |
| \(e/3\) | \(1\) | \(1/2\) | 1 |
| \(3e/8\) | \(e/2\) | \(3/2\) | 2 |
| \(e/2\) | \(e\) | \(1\) | 1 |

For completeness, the omitted parts of \((1/3,e)\) are above the cap. Before \(e/7\), the lower multiplier is 3 and the endpoint minima at \(e/8,e/7\) are respectively \((131/35)/e\) and \((53/20)/e\), both above \(2/e\). On \((e/7,19e/120)\), the expression \((19/20)/x-4/e\) decreases to the cap. On \((1/2,e/5)\), the minimum at \(e/5\) is \((29/12)/e>2/e\); on \((e/5,13e/60)\), the next expression decreases to the cap. Finally, on \((1,3e/8)\), the expression \((3/2)/x-2/e\) decreases to the cap. The ordering of these endpoints follows, for example, from the elementary bounds \(8/3<e<11/4\).

Using the capped value as a baseline,
\[
d_2=2e+\sum_{\text{seven rows}}
\left[eA\log(b/a)-(n+2)(b-a)\right].
\]
The sum of the linear terms \((n+2)(b-a)\) is
\[
\frac{11}{2}+\frac{43e}{60}.
\]
The logarithmic terms are
\[
e\left[
\frac{19}{20}\log\frac{20}{19}
+\frac{77}{60}\log(3/e)
+\frac{13}{12}\log\frac{15}{13}
+\frac73\log\frac43+\log2
\right].
\]
Since \(\log(3/e)=\log3-1\), substituting these expressions yields (9).

## 6. Stability under a subpower factor in the height bound

The fixed-power conclusion remains valid under the more general hypothesis
\[
M_N\leq N^{B+o(1)},\qquad 1<B<2.
\]
For fixed \(\varepsilon,T\), one still has \(p^2>M_N\), and the quotients in (4) satisfy
\[
x_i\leq N^{B-1+o(1)}.
\]
If \(r\leq s-1\), then the positive numerator in (5) is at most
\[
N^{r(B-1)+o(1)}=o(N),
\]
because \((s-1)(B-1)<1\) has a fixed strict gap. All subsequent arguments are unchanged. Thus the main theorem can equivalently use this more general height condition.

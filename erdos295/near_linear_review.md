# Independent review of the near-linear ceiling theorem

Date: 4 September 2026.

Reviewed: [near_linear_ceiling.md](near_linear_ceiling.md).

**Verdict: the proof is valid as written. No mathematical correction is required.** In particular, the growing cofactor bound, the prime cancellation argument, the full harmonic charge, and the uniform prime-number-theorem step remain valid for arbitrarily slowly growing \(\tau\). The quantification is along each fixed ceiling function, as stated in the note. This review verifies the mathematical deduction, not novelty or the cited construction's literature priority.

## Statement checked

Let \(G\geq0\), \(G=o(\log N)\), and
\[
\tau=\frac{\log N}{G+\log\log N}.
\]
For a set of distinct integers \(A\subseteq[N,\infty)\) with reciprocal sum 1, put \(D=|A|-(e-1)N\) and \(M=\max A\). Under \(M\leq N\exp(G)\), the proof establishes
\[
D\geq(1-o(1))\frac{N\log\tau}{\log N}.
\]

## 1. Scales and the contradiction subsequence

Write \(\ell=\log N\). Since \(G+\log\ell=o(\ell)\), one has \(\tau\to\infty\); also \(\tau\leq\ell/\log\ell\). For
\[
z=\frac{\tau}{(\log\tau)^2},\qquad y=N/z,
\]
all the claimed limits follow without monotonicity assumptions on \(G\):
\[
z\to\infty,\quad z=o(\tau),\quad z=o(\ell),\quad
\log z\sim\log\tau,\quad
\frac{z\log(z+2)}\tau\to0.
\]
Moreover,
\[
\log\frac{y^2}{M}\geq\ell-G-2\log z=(1-o(1))\ell\to\infty.
\]
Thus every selected denominator contains at most one prime above \(y\), and that prime occurs only to the first power.

A subsequence violating the lower bound has \(D=O(N\log\tau/\ell)\), since harmonic comparison already bounds \(D\) below by a constant. In that range \(D=o(N)\) and \(L/N\to e\). If \(Q_N=N\log\tau/\ell\), the harmonic expansion error satisfies
\[
\frac{(D+1)^2/N+1}{Q_N}
=O\!\left(\frac{\log\tau}{\ell}\right)+o(1)=o(1).
\]
Hence the use of \(eN\delta=D+o(Q_N)\) is justified even when \(\tau\) tends to infinity very slowly.

## 2. Growing cofactors and the positive numerator

With \(T=4\) and \(K=\lceil4z\rceil\), all low selected multiples of a covered prime \(p>y\) are included. Their coefficient is \(U/V\), where
\[
V=\operatorname{lcm}(1,\ldots,K),\qquad 1\leq U\leq VH_K.
\]
The nonempty low group is guaranteed by coverage. The Chebyshev estimate is uniform in growing \(K\): \(\log V=O(z)\). Also \(p>K\), since \(N/z\gg z\). Thus \(p\nmid V\).

For all tail multiples \(px_i\), one has \(p\nmid x_i\) and \(x_i<X=z\exp G\). The integer
\[
Z=U\prod_i x_i+V\sum_i\prod_{j\ne i}x_j
\]
is strictly positive. Reduction of the full reciprocal identity modulo \(p\), after multiplication by \(p\), implies \(p\mid Z\). No reduced-numerator assumption is needed.

For \(r=0\), the conventions give \(Z=U>0\), so this case is included. For every integer \(0\leq r\leq\tau/4\),
\[
Z\leq V(H_K+r)X^r.
\]
Here \(\log(H_K+r)=O(\log\tau)\), \(\log V=O(z)=o(\ell)\), and
\[
r\log X\leq\frac\tau4(G+\log z)
\leq\frac\tau4(G+\log\ell)=\frac\ell4.
\]
It follows that \(\log Z\leq(1/4+o(1))\ell\), whereas
\(\log p>\ell-\log z=(1-o(1))\ell\). The positive numerator is smaller than \(p\), a contradiction. Each covered prime therefore requires more than \(\tau/4\) tail multiples.

## 3. No double counting in the full prime loss

Two distinct primes above \(y\) cannot occur in the same selected denominator, and cannot occur in the same core integer. Hence missing core multiples for different uncovered primes are disjoint, and the tail terms required by different covered primes are also disjoint.

Since \(\alpha_N=1/L-1/(4N)\sim(1/e-1/4)/N\), the harmonic-loss identity gives
\[
\delta\geq\sum_{y<p\leq L}
\min\{W_N(p),\tau\alpha_N/4\}.
\]
Uniformly in this prime range,
\[
W_N(p)\leq H_K/p\leq zH_K/N
=O(z\log(z+2)/N)=o(\tau/N).
\]
The comparison is with a positive fixed multiple of \(\tau/N\), so the minimum equals \(W_N(p)\) for every prime in the sum once \(N\) is sufficiently large. No assumption that the covered primes were actually omitted is being made.

## 4. Uniform PNT evaluation, including slow tau

Retaining \(m\leq\lfloor z/2\rfloor\) is valid: every resulting prime satisfies \(p\geq N/m\geq2y>y\), and all the discarded terms are nonnegative.

Here is explicit error bookkeeping for the only potentially delicate uniformity step. Put \(x=N/m\) and \(\lambda=L/N\). For all relevant \(m\),
\[
x\geq2N/z\geq N/\ell,\qquad
\log x=\ell+O(\log\ell),
\]
and eventually \(2\leq\lambda\leq3\). Define
\[
\rho_N=\sup_{t\geq N/\ell}
\left|\frac{\pi(t)\log t}{t}-1\right|\longrightarrow0.
\]
Partial summation uniformly gives
\[
\sum_{x\leq p\leq\lambda x}
\left(\frac1p-\frac1{\lambda x}\right)
=\frac{\log\lambda-1+1/\lambda
+O(\rho_N+1/\log x+(\log x)/x))}{\log x}.
\]
An included prime at the lower endpoint contributes at most \(O(1/x)\), which is contained in this error. Consequently, after the factor \(1/m\), each inner sum is
\[
\frac{1/e+O(E_N)}{m\ell},
\]
where one can take
\[
E_N=\rho_N+\frac{\log\ell}{\ell}
+|\lambda-e|+\frac{\ell^2}{N}\longrightarrow0.
\]
The same \(E_N\) works for every multiplier. Thus summation gives a **relative** \(o(1)\) error:
\[
\delta\geq\frac{1/e-O(E_N)}\ell
\sum_{m\leq z/2}\frac1m
=(1/e-o(1))\frac{\log z}\ell.
\]
There is no need for \(E_N\log z\to0\), for \(E_N=o(1/\log z)\), or for any effective PNT rate tied to \(\tau\). Since \(z\to\infty\), the \(O(1)\) error in the harmonic sum is negligible relative to \(\log z\), however slowly the latter grows. This establishes the stated constant 1 after the harmonic-budget conversion.

## 5. Consequences and required fixes

For fixed \(A_0>0\), substituting \(G=A_0\log\log N\) gives \(\log\tau\sim\log\log N\). For fixed \(0<\beta<1\), substituting \(G=(\log N)^\beta\) gives \(\log\tau=(1-\beta+o(1))\log\log N\). Both displayed consequences follow.

Given the independently checked Croot construction with maximum \((e+o(1))N\) and excess \(O(N\log\log N/\log N)\), it lies below either example ceiling eventually. The stated order comparisons are therefore valid; they do not assert matching leading constants.

**Required fixes: none.** The explicit uniform error calculation above may be useful explanatory detail, but the existing explanation is mathematically sufficient. This theorem still restricts the largest denominator and supplies no growing lower bound for the unrestricted problem.

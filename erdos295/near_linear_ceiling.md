# Near-linear denominator ceilings for problem 295

Continuation note, 4 September 2026. **This is a restricted theorem, not a solution of Erdős problem 295. Novelty remains under investigation.** This proof is supplied for independent review. No posting or submission follows from this document.

Let \(A\) be a finite set of distinct integers at least \(N\), with
\[
\sum_{a\in A}\frac1a=1,\qquad D=|A|-(e-1)N,\qquad M=\max A.
\]

## Theorem and consequences

Let \(G=G(N)\ge0\) satisfy \(G=o(\log N)\), and set
\[
\tau=\frac{\log N}{G+\log\log N}.
\]
Every sequence of representations with \(M\le N\exp(G)\) satisfies
\[
\boxed{D\ge(1-o(1))\frac N{\log N}\log\tau.} \tag{1}
\]
The assertion is along each specified ceiling function \(G\) and sequence of representations; no rate uniform over all unspecified little-o functions is asserted.

In particular:

- \(M\le N(\log N)^{A_0}\), for fixed \(A_0>0\), forces
  \[
  D\ge(1-o(1))N\log\log N/\log N. \tag{2}
  \]
- \(M\le N\exp((\log N)^\beta)\), for fixed \(0<\beta<1\), forces
  \[
  D\ge(1-\beta-o(1))N\log\log N/\log N. \tag{3}
  \]

Croot's classical construction, whose maximum is \((e+o(1))N\), fits under either ceiling and gives the upper excess \(O(N\log\log N/\log N)\). Thus the minimum excess under either displayed family of ceilings has order \(\Theta(N\log\log N/\log N)\). This matches orders, not leading constants. The upper bound is established background; see [the literature audit](literature_audit.md).

The fixed \(0<A_0<1\) case already follows in order from Croot's prime cutoff, although that deduction gives a smaller coefficient. The wider ranges \(A_0\ge1\) and (3) are not immediate from the inspected prime-cutoff statements. That distinction is not an assertion of novelty.

## 1. Harmonic budget and scales

Write \(\ell=\log N\), and choose
\[
z=\frac{\tau}{(\log\tau)^2},\qquad y=\frac Nz.
\]
Then
\[
\tau,z\to\infty,\quad z=o(\tau),\quad z=o(\ell),\quad
\log z\sim\log\tau,\quad \log z\le\log\ell,
\]
and
\[
\frac{y^2}{N\exp(G)}
=\exp(\ell-G-2\log z)\to\infty. \tag{4}
\]
A selected denominator therefore contains at most one prime greater than \(y\), to the first power.

It suffices to consider
\[
D=O\left(\frac N\ell\log\tau\right): \tag{5}
\]
a sequence violating (1) has this upper bound, while harmonic comparison bounds \(D\) below by an absolute constant. In this range \(D=o(N)\). Put
\[
L=N+|A|-1=eN+D-1,\quad I=[N,L]\cap\mathbb Z,\quad
H=I\setminus A,\quad E=A\setminus I.
\]
The exact identity and its harmonic expansion are
\[
\begin{aligned}
\delta&:=\sum_{n=N}^{L}\frac1n-1\\
&=\sum_{h\in H}\left(\frac1h-\frac1L\right)
+\sum_{a\in E}\left(\frac1L-\frac1a\right)\ge0,\\
eN\delta
&=D+\frac{e-1}{2}
+O\left(\frac{(|D|+1)^2}{N}\right)
=D+o\left(\frac N\ell\log\tau\right).
\end{aligned} \tag{6}
\]
The last error estimate follows from (5). Fix \(T=4\), so \(L<TN\) eventually, and call denominators above \(TN\) tail denominators.

## 2. Each selected large prime requires many tail terms

Let \(y<p\le L\) be prime, dividing a selected denominator in \(I\). Include all selected multiples of \(p\) at most \(TN\). Their reciprocal sum is
\[
\frac1p\sum_{m\in J}\frac1m=\frac U{pV},
\]
where \(J\) is a nonempty subset of \(\{1,\ldots,K\}\),
\[
K=\lceil Tz\rceil,\quad V=\operatorname{lcm}(1,\ldots,K),
\quad 1\le U\le VH_K.
\]
Here \(H_K\) is a harmonic number. The standard Chebyshev bound gives
\[
\log V=O_T(z),\qquad \log U=O_T(z+\log\log(z+2)). \tag{7}
\]
Also \(p>K\) eventually.

Write all tail multiples of \(p\) as \(px_1,\ldots,px_r\). By (4), \(p\nmid x_i\), and
\[
x_i\le M/p<z\exp(G)=:X.
\]
Combining all terms divisible by \(p\) gives the positive numerator
\[
Z=U\prod_{i=1}^{r}x_i+
V\sum_{i=1}^{r}\prod_{j\ne i}x_j. \tag{8}
\]
For \(r=0\), interpret \(Z=U\). All remaining selected denominators are coprime to \(p\), so \(p\mid Z\).

If \(r\le\tau/4\), then \(X>1\) and
\[
\begin{aligned}
\log Z
&\le\log V+\log(H_K+r)+r\log X\\
&\le O_T(z)+O(\log\tau)+\frac{\tau}{4}(G+\log z)\\
&\le(1/4+o(1))\ell,
\end{aligned} \tag{9}
\]
since \(\tau(G+\log z)\le\tau(G+\log\ell)=\ell\).
But \(\log p>\ell-\log z=(1-o(1))\ell\). This contradicts \(0<Z<p\). Thus every selected core prime greater than \(y\) has more than \(\tau/4\) tail multiples.

## 3. Charging the prime's core multiples

For \(y<p\le L\), define
\[
W_N(p)=\sum_{\substack{m\ge1\\N\le mp\le L}}
\left(\frac1{mp}-\frac1L\right).
\]
Let \(\mathcal U\) be the primes with no selected core multiple, and \(\mathcal V\) the others.

The core multiples of each prime in \(\mathcal U\) are holes. Their sets are disjoint because \(y^2>L\). By (4), each tail contains at most one prime greater than \(y\), so, with \(r_T=|A\cap(TN,\infty)|\),
\[
r_T\ge(\tau/4)|\mathcal V|.
\]
Each tail costs at least
\[
\alpha_N=1/L-1/(TN)\sim(1/e-1/T)/N>0
\]
in (6). Therefore
\[
\delta\ge
\sum_{p\in\mathcal U}W_N(p)+|\mathcal V|\tau\alpha_N/4
\ge\sum_{y<p\le L}\min\{W_N(p),\tau\alpha_N/4\}. \tag{10}
\]
Uniformly,
\[
W_N(p)\le H_{\lceil Tz\rceil}/p
=O(z\log(z+2)/N)=o(\tau/N).
\]
Here \(z\log(z+2)/\tau=O(1/\log\tau)\to0\). Consequently
\[
\delta\ge\sum_{y<p\le L}W_N(p) \tag{11}
\]
eventually. This charges selected primes through their required tails; it does not assert that all primes in the sum were omitted.

## 4. Evaluating the prime loss

Retain only multipliers \(m\le\lfloor z/2\rfloor\). Since \(N/m\ge2y\), (11) gives
\[
\delta\ge
\sum_{m\le z/2}\ \sum_{N/m\le p\le L/m}
\left(\frac1{mp}-\frac1L\right). \tag{12}
\]
Put \(\lambda=L/N\to e\), \(x=N/m\). Uniformly over these \(m\),
\(x\ge2N/z\to\infty\), \(\log x\sim\ell\), and \(\lambda\) stays in a fixed compact subinterval of \((1,\infty)\). Partial summation and the prime number theorem give
\[
\begin{aligned}
\sum_{N/m\le p\le L/m}\left(\frac1{mp}-\frac1L\right)
&=\frac1m\sum_{x\le p\le\lambda x}
\left(\frac1p-\frac1{\lambda x}\right)\\
&=\frac{\log\lambda-1+1/\lambda+o(1)}{m\log x}\\
&=\frac{1/e+o(1)}{m\ell}.
\end{aligned} \tag{13}
\]
The errors are uniform: all \(x\ge N/\ell\), so the eventual relative-error bound in the prime number theorem applies to every interval before partial summation.

Summing gives
\[
\delta\ge(1/e-o(1))\frac{\log z}{\ell}
=(1/e-o(1))\frac{\log\tau}{\ell}.
\]
Together with (6), this proves (1).

For \(G=A_0\log\log N\),
\[
\log\tau=\log\log N-\log\log\log N-\log(A_0+1)
\sim\log\log N.
\]
For \(G=(\log N)^\beta\), one has
\(\log\tau=(1-\beta+o(1))\log\log N\).
These prove (2) and (3).

## Limitation

The argument requires \(G=o(\log N)\). It does not exclude exponential denominators in \(N\), and it provides no growing lower bound for the unrestricted problem. Independent mathematical review and a literature search are separate from a claim of novelty or readiness to post.

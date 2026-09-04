# Independent audit of the order limit for the 2/4/8 family

> This is an AI-agent proof review, not independent human peer review.

4 September 2026.

This checks the proposed extension of `F_n` obtained by allowing the
105 transitive extraspecial groups of order 32 on each eight-point
block. The independent group-theoretic count is in
[audit_extraspecial.md](audit_extraspecial.md). Here `N=n-(n mod 2)` and `m=N/2`.

The proposed coefficient is

$$
B_N=[z^N]\exp(z^2/2+z^4/6+z^8/384).
$$

Let $\rho>0$ be the solution of

$$
\rho/2+\rho^2/3+\rho^4/96=m.
$$

Take independent Poisson variables $A,B_0,B_1,C$ with means

$$
\lambda_A=\rho/2,\quad
\lambda_0=\rho^2/24,\quad
\lambda_1=\rho^2/8,\quad
\lambda_C=\rho^4/384.
$$

Condition on

$$
T=A+2B_0+2B_1+4C=m.
$$

These are exactly the weighted profile counts: pairs, regular
Klein-four blocks, dihedral blocks, and extraspecial blocks. The
conditioning has a lattice constraint, so it is important to specify
which marginals approach their unconditioned laws.

## A conditioning lemma with the lattice issue made explicit

As $m\to\infty$, the conditional marginal law of $(B_0,B_1)$
converges in total variation to the independent Poisson law just given.
Also, under the conditioning,

$$
A-\lambda_A=O_{\Pr}(\sqrt\rho).
$$

Proof. Write $q_*=(2\pi\lambda_C)^{-1/2}$. Stirling's formula for
Poisson probabilities gives, uniformly over integral arguments
$j=\lambda_C+o(\sqrt{\lambda_C})$,

$$
\Pr(C=j)=q_*(1+o(1)).
$$

It also gives the global bound $\max_j\Pr(C=j)\leq Kq_*$ for an
absolute constant $K$ and large $m$.

Restrict $B_i$ to
$|B_i-\lambda_i|\leq\rho\log\rho$, and restrict $A$ to
$|A-\lambda_A|\leq\sqrt\rho\log\rho$. Each restriction has
unconditioned probability tending to one. For any values in those
windows satisfying the necessary congruence modulo four, the required
value of $C$ differs from its mean by
$O(\rho\log\rho)=o(\sqrt{\lambda_C})$. It is positive for large
$m$. Thus its mass is $q_*(1+o(1))$, uniformly in all such values.

The roots-of-unity filter for a Poisson variable gives

$$
\Pr(A\equiv r\pmod4)=\frac14+O(e^{-c\rho})
$$

uniformly in $r$. Removing the stated window for $A$ changes
this probability by $o(1)$. Averaging over $A$ therefore proves

$$
\Pr(T=m\mid B_0,B_1)=\frac{q_*}{4}(1+o(1))
$$

uniformly in the displayed $B$-windows. Everywhere, this
conditional probability is bounded by $Kq_*$. Integrating with
respect to the unconditioned $B$ variables proves

$$
\Pr(T=m)\sim q_*/4.
$$

Consequently the Radon-Nikodym weight of the conditioned $B$
marginal relative to the independent Poisson law tends uniformly to
one on windows of probability tending to one, and is globally bounded.
This proves convergence in total variation.

For every event $E$ determined by $A$, the global maximum bound
also gives

$$
\Pr(E\mid T=m)
\leq \frac{Kq_*}{\Pr(T=m)}\Pr(E)
\leq K'\Pr(E).
$$

The usual Poisson variance bound now proves the asserted conditional
concentration of $A$. This completes the lemma.

**The joint law including $A$ is not close in total variation to
the independent Poisson law.** It satisfies the congruence
$A+2B_0+2B_1\equiv m\pmod4$ with probability one, whereas the
unconditioned law satisfies it with probability tending to one
quarter. The argument above uses only the correct marginal statement.

## Order central limit theorem

Let $K$ be the quotient subspace rank. Before the exponentially
unlikely surjectivity rejection, its law is the uniform-subspace law
on $\mathbf F_2^m$; in particular $K-m/2=O_{\Pr}(1)$. After
rejection the same statement holds. The product of the orbit
projections' derived groups has order $2^{B_1+C}$. Therefore

$$
\begin{aligned}
L:=\log_2|H|
 &=K+B_1+C\\
 &=\frac{3N}{8}+(K-m/2)+\frac{B_1-B_0}{2}-\frac A4.
\end{aligned}
$$

The independent Poisson difference has mean
$\lambda_1-\lambda_0=\rho^2/12$ and variance
$\lambda_1+\lambda_0=\rho^2/6$. Its ordinary central limit theorem,
transferred through the total variation lemma, gives

$$
\boxed{
\frac{L-\mu_N}{\rho/\sqrt{24}}
\ \Longrightarrow\ \mathcal N(0,1),\qquad
\mu_N=\frac{3N}{8}+\frac{\rho^2}{24}-\frac\rho8.
}
$$

The $A$ fluctuation is $O_{\Pr}(\sqrt\rho)=o_{\Pr}(\rho)$,
and the rank fluctuation is $O_{\Pr}(1)$, so both vanish at this
scale. The centering term $-\rho/8$ is of the same order as the
standard deviation and must be retained. Surjectivity rejection is
exponentially small uniformly over all profiles, so it does not affect
the limit.

As $\rho\asymp N^{1/4}$, this also proves
$L/n\to3/8$ in probability within the stated family. It says
nothing by itself about the unrestricted random subgroup measure.

## Targeted novelty check

The primary
[Roney-Dougal–Tracey preprint](https://arxiv.org/abs/2503.05416), whose
arXiv record lists only the March 2025 version when checked, proves the
quadratic leading term and an unspecified positive coefficient in its
$n\log n$ lower bound. Inspection of its Section 7 lower-bound
construction shows disjoint prime-length cycles; no extraspecial
construction or explicit $7/8$ coefficient was located there.

[Kovács–Praeger](https://msp.org/pjm/1989/136-2/pjm-v136-n2-p05-s.pdf)
identifies the efficient degree-eight extraspecial constituent in its
equality classification. It is a structural input, not an enumeration
or an order limit theorem for the present family.

Targeted searches for the $7/8$ coefficient and the extraspecial
construction in subgroup enumeration did not locate a prior statement.
This is **not an exhaustive novelty determination**. The safe current
description is an explicit proved refinement obtained here, with
priority still to be checked.

## Review of the assembled third note

After the argument above, I read [progress_v3.md](progress_v3.md) in full. I found no
fatal gap. In particular, I checked its coefficient estimate, the
linear term in the abelian-to-`Q_n` ratio, the expansion
`rho^2=sqrt(48N)-16+O(N^(-1/4))`, and the odd-degree `R_n` extension.
All constants agree with independent algebra. The exact order
polynomial and the subgroup recovery argument agree with the separate
extraspecial audit.

The minor requested editorial corrections were: make the multiplier of
the standard deviation explicit in the conditioning window; use the
actual Roney-Dougal–Tracey paper title; and justify the plus-type name
with the explicit central-product construction if retaining that name.
The mathematical enumeration and limit theorem do not rely on the
plus-type name.

# Independent adverse audit of the exact-order spectrum bound

> This is an AI-agent proof review, not independent human peer review.

4 September 2026. Scope: order_spectrum.md. This audit is independent
of the proof's author and of the earlier finite verification programs.

**Conclusion:** The theorem and finite bound are correct on their
stated domains. The lower bound is uniform over every integer
$\lfloor n/4\rfloor\leq j\leq\lfloor n/2\rfloor$. The cited
Roney-Dougal–Tracey theorem supplies the asserted uniform upper bound
for actual labelled subgroups. No novelty claim is established.

## Parity, endpoints, and the exact order

Write $n=4q+s$, $s\in\{0,1,2,3\}$.

| $s$ | $m$ | $f$ | $a$ | $\delta$ | Choice of $k$ |
|---|---:|---:|---:|---:|---|
| 0 | $2q$ | $q$ | 0 | 0 | $q$ |
| 1 | $2q$ | $q$ | 0 | 1 | $q$ |
| 2 | $2q+1$ | $q$ | 1 | 0 | $q$, except $k=q+1$ at $j=2q+1$ |
| 3 | $2q+1$ | $q$ | 1 | 1 | $q$, except $k=q+1$ at $j=2q+1$ |

In every case $k(m-k)=\lfloor m^2/4\rfloor$, and $z=j-k$
runs through integers between zero and $f$. The exceptional top
endpoint in the last two rows has $z=f$, so it is covered rather
than omitted.

For $c=\min(z,f-z)$, $b=f-2c$, $d=z-c$:

- If $z\leq f/2$, then $c=z$, $b=f-2z$, $d=0$.
- If $z\geq f/2$, then $c=f-z$, $b=2z-f$, $d=b$.

Thus all parameters are nonnegative integers,
$a+2b+4c=m$, and $c+d=z$. At equality $z=f/2$, both
descriptions give $b=d=0$; no conflicting orbit assignment occurs.
The product of the prescribed orbit groups has binary quotient rank
$m$ and derived subgroup order $2^z$, so each constructed
preimage has exactly order $2^{k+z}=2^j$.

## The finite lower bound and distinctness

The displayed quotient factors have ranks at most four. Combining
surjections from one four-dimensional vector space produces a
subdirect image of dimension at most four. Since $n\geq16$ implies
$m\geq8$, this image can be enlarged to a four-dimensional $W$.
Since $k\geq4$, the desired $k$-subspaces containing $W$ exist.
Their number is exactly ${m-4\brack k-4}_2$.

The full preimage of any such subspace contains the entire ambient
derived subgroup and is onto each quotient factor. Therefore it
projects onto each original transitive orbit group. This can be seen
directly from the kernel and quotient, without needing a separate
Frattini theorem.

Distinct subspaces have distinct preimages. The resulting subgroup
recovers the labelled orbit partition, so groups from different
partitions are distinct even though only one embedded model was
chosen per block. Consequently (4) is a valid finite lower bound;
it does not require normalizer or conjugacy-class counts.

The Gaussian product formula yields
$$
{m-4\brack k-4}_2\geq
2^{(k-4)(m-k)}
=2^{\lfloor m^2/4\rfloor-4(m-k)}
=2^{n^2/16-O(n)}.
$$
The implied constant is absolute and independent of $j$.

## Uniformity of the triangular coefficient

In the partition factor, $a,\delta\in\{0,1\}$, and the logarithms
of the fixed block-size weights contribute only $O(n)$. The
identity
$$
b\log_2 b+c\log_2 c
=(b+c)\log_2 n+O(n)
$$
is uniform, including $b=0$ or $c=0$, by the bounded continuous
extension of $x\log x$ to $x=0$. Thus (6) follows uniformly.

The exact block-count identity is
$$
b+c=f/2+|z-f/2|.
$$
Since $z=j-k$, $f=n/4+O(1)$, and $k=f+O(1)$, the inequality
$\big||x|-|y|\big|\leq|x-y|$ gives
$$
n-b-c=7n/8-|j-3n/8|+O(1)
$$
with a constant independent of $j$. Multiplying its error by
$\log_2 n$ contributes $O(\log n)$, absorbed into the already
uniform $O(n)$ error. This verifies the triangular coefficient,
including both ends of the interval.

## Applicability of the published upper bound

Every subgroup of order $2^j$ is a 2-group, so its count is at most
the number of all actual 2-subgroups of $S_n$. Theorem 2 of
[Roney-Dougal–Tracey, arXiv:2503.05416](https://arxiv.org/html/2503.05416v1)
gives, for the fixed prime $p=2$,
$$
|\operatorname{Sub}_2(S_n)|
\leq2^{n^2/16+\beta_2n\log_2n}
$$
with an absolute constant $\beta_2$. The paper counts actual
subgroups, so there is no mismatch with conjugacy or isomorphism
classes. Its bound is independent of $j$. Combining it with the
proved lower bound gives (2) and the uniform quadratic logarithmic
limit for every allowed sequence $j(n)$.

The upper bound is a cited external theorem; the lower bound needs
only the explicit degree-eight factor and elementary vector-space
counting. Neither side establishes relative order probabilities under
uniform sampling from all subgroups.

## Restricted-family refinement

The appended matching estimate (8) for $q_{n,j}$, the count inside
$Q_n$, is also verified. For a general profile, both identities
$$
B-z=a+b-d\geq0,\qquad B-(m/2-z)=a/2+d\geq0
$$
are correct, giving the required lower bound on the number of
nontrivial blocks. The upper count uses only the factorial partition
count, fixed local choice factors of size $2^{O(n)}$, and a Gaussian
coefficient upper bound.

The substitution $u=k-m/2$ gives the stated profile exponent.
The possible benefit from moving $k$ away from its midpoint is
bounded by $-u^2+|u|\log_2n\leq(\log_2n)^2/4=O(n)$.
All parameter estimates and the polynomial profile sum are uniform.
The original lower construction belongs to $Q_n$, completing the
two-sided estimate with the asserted $O(n)$ error.

This sharper upper bound is explicitly restricted to $Q_n$, and
is not asserted for unrestricted counts or transferred solely by
total variation.

## Website version

The rewritten [submitted proof](proof.md) was read in full after its
prescribed-order-interval rewrite. Its theorem, finite construction,
explicit eight-point group, parity exception, partition count, and
Gaussian/Stirling estimates agree with the audited proof.

It accurately identifies the external upper theorem and classical
group ingredient, and makes neither a full-solution nor a novelty
claim. Its explicit AI-assistance disclosure is consistent with the
work performed. No substantive correction is needed before it is
used as a public partial-results note.

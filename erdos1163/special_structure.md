# Typical center, derived subgroup, and generator number

Research extension, 4 September 2026. Initially stated for `J_n` from
[extension_efficient_orbits.md](extension_efficient_orbits.md); it transfers to any larger class proved
to have total-variation distance `O(2^(-cn))` from `J_n`.

For uniform `H in J_n`, with probability `1-O(2^(-cn))`,

$$
Z(H)=H'=\Phi(H)
$$

is elementary abelian. Thus H is a special 2-group. Write
`N=n-(n mod 2)`, `m=N/2`. Its minimal generator number has the discrete
Gaussian law

$$
\Pr(d(H)-m/2=j)\longrightarrow
\frac{2^{-j^2}}{\sum_{t\in\mathbb Z+\epsilon}2^{-t^2}},
$$

along fixed parity of m, with `epsilon=0` or `1/2` accordingly. In
particular `d(H)=N/4+O_P(1)`.

Let rho solve `rho/2+rho^2/3+rho^4/96=N/2`. The center and derived
subgroup orders satisfy

$$
\frac{\log_2|H'|-N/8-\rho^2/24+\rho/8}{\rho/\sqrt{24}}
\Longrightarrow\mathcal N(0,1),
$$

and the same holds with H' replaced by Z(H). These are additional
structural conclusions for the specified sampling class, not for
uniform unrestricted subgroups of S_n.

## 1. The derived subgroup fills the ambient derived subgroup

By the already proved dominance result, it suffices to sample H from
`Q_n`, the saturated subfamily with the minimum number of fixed points.
For its ambient product D, put `Z=D'`, `dim Z=z=d+c`, where d is the
number of D8 factors and c the number of E8 factors. Put
`V=D/Z`, of dimension m. Let U be its subdirect k-dimensional subspace.

The coordinate commutator forms restricted to U are nonzero alternating
forms of rank two on D8 factors and rank four on E8 factors. Their
linear span has dimension `dim H'`. This follows by taking the
annihilator of the image-span of the vector-valued commutator map.

For a fixed rank-two alternating form, there are six ordered
representations by an independent coordinate pair. For a fixed rank-four
alternating form, there are 720 representations by an independent
ordered symplectic coordinate tuple: the polar radical recovers the
kernel of the coordinate map, and

$$
|\operatorname{Sp}_4(2)|=(15\cdot8)(3\cdot2)=720.
$$

Suppose the z forms have span dimension `z-h`, with `h>=1`. Choose a
basis subset of positions. Each remaining form has at most `2^(z-h)`
choices and at most 720 coordinate representations. It would otherwise
have at least `2^(2k)` coordinate choices. The same ordered-basis count
used in the efficient-orbit theorem bounds the number of U by

$$
C\binom zh720^h\sum_k
2^{k(m-k)-h(2k-z+h)}.
$$

Writing `j=k-m/2`, its exponent is

$$
\frac{m^2}{4}-(j+h)^2-h(m-z).
$$

The Gaussian k-sum is bounded by a constant times `S_m`, and `z<=m/2`.
Summing h gives, uniformly in every profile and choice of orbit groups,

$$
\#\{U:H'\ne Z\}
\leq C S_m\sum_{h\geq1}(720m)^h2^{-hm/2}
=S_m O(m2^{-m/2}).
$$

The subdirect U count is `S_m(1+O(n2^(-m/4)))`, so this is an
exponentially small relative exceptional set. It follows that `H'=D'`
with the asserted probability. All squares of H lie in D', hence
`H'<=Phi(H)<=D'`, so `Phi(H)=H'=D'` on the same event.

## 2. No additional central elements typically occur

Let `V_ab` be the direct sum of quotient coordinates from the abelian
orbit projections C2 and V4. Its dimension is
`ell=a+2b0`, where b0 is the number of V4 factors. Because U surjects
onto every nonabelian quotient factor, whose local commutator form is
nondegenerate, the radical of the vector commutator map on U is
exactly

$$
U\cap V_{\rm ab}.
$$

Indeed, if an element commutes with all of U, its projection on each
nonabelian factor pairs to zero with the whole local quotient and is
therefore zero. The converse is immediate. As H contains D', this
proves `Z(H)/D' = U intersect V_ab`.

For uniform k-subspaces of V, a union bound over nonzero vectors of
`V_ab` gives

$$
\Pr(U\cap V_{\rm ab}\ne0)
\leq(2^\ell-1)\frac{2^k-1}{2^m-1}
\leq2^{1+\ell+k-m}.
$$

The probability that `k>5m/8` is `O(2^(-c m^2))` by the Gaussian
coefficient bounds. The orbit-profile probability that `ell>m/4`
is `O(exp(-c m log m))`: in the Poisson representation from
[progress_v3.md](progress_v3.md), `ell<=A+2(B0+B1)`, with Poisson means of orders
`m^(1/4)` and `sqrt(m)`. A Chernoff bound gives the stated tail before
conditioning. Conditioning on
`A+2(B0+B1)+4C=m` multiplies any event probability involving A,B0,B1
by at most a constant, since
`sup_j Pr(C=j)/Pr(A+2(B0+B1)+4C=m)=O(1)`.

On the remaining event the intersection bound is at most `2^(1-m/8)`.
Conditioning the subspace on being subdirect changes total variation
only by `O(n2^(-m/4))`. This proves `Z(H)=D'` except for an exponentially
small proportion.

## 3. The limit laws

On the intersection of the two high-probability events,

$$
d(H)=\dim(H/\Phi(H))=\dim U=K,
\qquad \log_2|H'|=\log_2|H|-K.
$$

The discrete Gaussian limit for `K-m/2` and the central limit theorem
for `log_2|H|` are already proved for Q_n. Since `K-m/2=O_P(1)` and
the latter CLT scale tends to infinity like `n^(1/4)`, subtraction of K
changes the center by m/2 and leaves the normal limit unchanged. The
exponentially small total-variation changes to J_n preserve all these
conclusions.

The independent audit in [audit_special_structure.md](audit_special_structure.md) found no gap.
The dominance theorem in [extension_eight_point_projections.md](extension_eight_point_projections.md) transfers
all these conclusions to the full class `C_n` of 2-subgroups with class
at most two, exponent dividing four, and all orbit sizes at most eight.

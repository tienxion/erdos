# Erdős 1163: all abelian subgroups and an odd-degree obstruction

Second research pass, 4 September 2026

For the subsequent stronger bounds and completed subdirect-product
extensions, start with
[results.md](results.md).

**Status: stronger partial results; not a solution of Problem 1163 and
not yet a submission-ready manuscript.** This note extends
[the first research note](progress.md).
The proof of the abelian extension uses the classical Birkhoff subgroup
formula. Novelty of the resulting asymptotic theorem still needs a more
complete bibliographic check.

The two principal advances are:

1. The relative asymptotic count and discrete order law now hold for
   **all abelian subgroups** of `S_n`, not just elementary abelian ones.
   Consequently, for a uniform unrestricted subgroup H,

   \[
   \Pr(H\text{ is abelian})\leq 2^{-n/2+O(\sqrt n)}.
   \]

2. For odd n, the previously constructed family `F_n` has probability
   tending to zero under the uniform measure on `Sub(S_n)`. A new family
   with an `S_3` orbit is asymptotically `sqrt(n/24)` times larger.
   This proves that simply showing all other families negligible relative
   to `F_n` is impossible in odd degrees.

Neither result determines the unrestricted distribution of subgroup
orders. In particular, there is still no proof of the `7n/16` order law
for uniform unrestricted subgroups.

## 1. Definitions and inherited results

Let `Ab_n` be all abelian subgroups of `S_n`, and `E_n` all elementary
abelian 2-subgroups, including the trivial group. Put

\[
\delta=n\bmod2,\quad N=n-\delta,\quad m=N/2,
\]

\[
S_m=\sum_{k=0}^m{m\brack k}_2,\qquad
A_N(w)=[z^N]\exp(z^2/2+wz^4/24),\qquad
C_n(w)=\frac{n!}{\delta!}A_N(w).
\]

Write `E_n^*` for the elementary 2-subgroups with exactly delta fixed
points and all other orbits of length two or four. The first note proves

\[
|E_n^*|=C_n(1)S_m(1+O(n2^{-m/4})),                       \tag{1.1}
\]

and the uniform order law

\[
\Pr\!\left(\log_2|H|-m/2=j\right)
 \longrightarrow\frac{2^{-j^2}}{\sum_{t\in\mathbb Z+\epsilon}2^{-t^2}}.
                                                               \tag{1.2}
\]

Here n tends to infinity with fixed parity of m, `epsilon=0` for even m
and `epsilon=1/2` for odd m, and j is in that lattice.

The family `F_n` allows each four-point projection to be either regular
Klein-four or one of the three dihedral groups of order eight; each
subgroup contains the derived group of the product of its projections.
The first note proves

\[
|F_n|=C_n(4)S_m(1+O(n2^{-m/4})),                         \tag{1.3}
\]

\[
\log_2\frac{A_N(1)}{A_N(4)}=-N/2+O(\sqrt N).             \tag{1.4}
\]

## 2. A bound from the Birkhoff formula

Write a finite abelian p-group as

\[
A_p\cong\prod_i C_{p^{\lambda_i}},\qquad
r_j=\#\{i:\lambda_i\geq j\}.
\]

For a subgroup type with conjugate partition `(s_j)`, the classical
formula counts subgroups of that type by

\[
\prod_j p^{s_{j+1}(r_j-s_j)}
 {r_j-s_{j+1}\brack s_j-s_{j+1}}_p.                     \tag{2.1}
\]

This is the Birkhoff formula, not a new identity: see
[Birkhoff (1935)](https://doi.org/10.1112/plms/s2-38.1.385),
Butler, *Subgroup lattices and symmetric functions* (1994), Theorem 1.6.1,
or the displayed theorem in
[Maglione's proof](https://joshmaglione.com/2023/12/17/Birkhoff.html).

The Gaussian upper bound gives at most

\[
P_2^{-J_p}p^{\sum_j s_j(r_j-s_j)}
 \leq P_2^{-J_p}p^{\frac14\sum_jr_j^2},                 \tag{2.2}
\]

where `J_p` is the number of nonzero columns and
`P_2=product_(i>=1)(1-2^(-i))`. The exponent follows by adding
`s_(j+1)(r_j-s_j)` to the degree of the Gaussian coefficient in (2.1).

For a finite abelian group A, let `r_(p,j)` be these column ranks for its
Sylow p-subgroups and set

\[
\mathcal E(A)=\sum_{p,j}(\log_2p)r_{p,j}^2.
\]

If all ranks are at most n and J is their total number of nonzero
coordinates, then there are at most `(n+1)^J` possible subgroup types
(column arrays). Sylow components of a subgroup can be selected
independently. Thus

\[
|\operatorname{Sub}(A)|
 \leq [P_2^{-1}(n+1)]^J 2^{\mathcal E(A)/4}.             \tag{2.3}
\]

Only this upper bound from the classical formula is needed below.

## 3. Measuring the loss from nonoptimal abelian orbits

Every transitive faithful abelian action is regular. Therefore an abelian
subgroup H determines a unique ambient product A of its regular orbit
projections. H is a subdirect subgroup of A.

Call a nontrivial orbit projection **optimal** when it is `C_2` on two
points or `C_2^2` on four points. Call every other nontrivial regular
abelian orbit projection nonoptimal.

For a regular abelian group B of degree `ell=|B|`, define its rank vector

\[
v(B)_{p,j}=\sqrt{\log_2p}\,r_{p,j}(B).
\]

Vectors add under direct products, and `mathcal E(A)=||v(A)||²`.
An optimal projection contributes `(ell/2)e_(2,1)`.

### Lemma 3.1: two uniform local losses

Every nonoptimal B satisfies

\[
r_{2,1}(B)\leq 3\ell/8,\qquad
\|v(B)\|\leq 15\ell/32.                                \tag{3.1}
\]

Proof. In general `r_(2,1)(B)<=log_2 ell` and

\[
\|v(B)\|\leq\sum_{p,j}\sqrt{\log_2p}\,r_{p,j}(B)
 \leq\sum_{p,j}(\log_2p)r_{p,j}(B)=\log_2\ell.
\]

For `ell>=8`, the decreasing function `(log_2 ell)/ell` is at most
`3/8`. For `ell>=5`, it is at most `(log_2 5)/5<7/15<15/32`,
using `5³<2⁷`. The remaining nonoptimal cases for the norm are `C_3`
and `C_4`, with respective norms `sqrt(log_2 3)` and `sqrt(2)`, which
obey (3.1). For the first bound, odd degrees 3, 5, and 7 have zero
2-rank; `C_4` and the abelian group of order 6 have 2-rank one.
This verifies all remaining cases. QED.

Now fix an ambient product with f fixed points and nonoptimal blocks
`B_1,...,B_t`, whose total degree is B. All its other points lie in
optimal blocks. Set

\[
R=r_{2,1}(A),\quad D=m-R,\quad L=f-\delta+B.
\]

The remaining optimal degree is `N-L`. In particular L is even and

\[
D=L/2-\sum_i r_{2,1}(B_i).                              \tag{3.2}
\]

### Lemma 3.2: the defect controls the exceptional support

Unless the profile consists solely of optimal blocks and delta fixed
points, D is a positive integer and

\[
2D\leq L\leq8D,\qquad B\leq8D+1.                      \tag{3.3}
\]

Proof. The first inequality follows from (3.2). For the second,

\[
L-8D=-3(f-\delta)+\sum_i(8r_{2,1}(B_i)-3|B_i|).
\]

The sum is nonpositive by (3.1). If `f>=delta`, the claim follows.
The only remaining case is `delta=1,f=0`. There is then an odd-degree
nonoptimal orbit; its summand is at most `-9`, since its 2-rank is zero
and its degree at least three. This offsets `-3(f-delta)=3`.
Thus `L<=8D` in this case too. A nonoptimal profile has `L>0`, so D is
positive. Finally `B<=L+delta<=8D+1`. QED.

This parity check matters: an odd-degree action can have no fixed points
and an orbit of size three. Treating f as automatically at least delta
would be an error for general abelian subgroups.

### Lemma 3.3: a uniform quadratic loss

For `m>=416`, every nonoptimal profile satisfies

\[
\mathcal E(A)\leq m^2-\frac{mD}{32}.                    \tag{3.4}
\]

Proof. All coordinates other than `(2,1)` come from nonoptimal blocks.
By (3.1) and (3.3), their squared norm is at most
`(B/2)²<=25D²`. Hence

\[
\mathcal E(A)\leq(m-D)^2+25D^2
              =m^2-2mD+26D^2.                         \tag{3.5}
\]

For `D<=m/26` this is at most `m²-mD`.

For larger D, apply the triangle inequality to all blocks:

\[
\|v(A)\|\leq(n-f-B)/2+15B/32
 \leq n/2-(f+B)/32
 \leq m-D/16+15\delta/32.                              \tag{3.6}
\]

Here we used `f+B=L+delta>=2D+delta`. Since `D>m/26` and `m>=416`,
we have `D>=17`, so the last expression is at most `m-D/32`.
As `D<=m`,

\[
(m-D/32)^2\leq m^2-mD/32.
\]

This proves (3.4) in both ranges. The constants are deliberately loose.
QED.

## 4. Counting all nonoptimal abelian profiles

There are at most `10D` nonzero column coordinates for A. Indeed, apart
from the possible `(2,1)` coordinate, each nonzero coordinate comes
from the product of the nonoptimal B_i, and their number is at most

\[
\sum_i\log_2|B_i|\leq B\leq8D+1.
\]

All ranks are at most n. Consequently (2.3) and (3.4) give

\[
|\operatorname{Sub}(A)|
 \leq [P_2^{-1}(n+1)]^{10D}
       2^{m^2/4-mD/128}.                               \tag{4.1}
\]

We must also count the ambient products, rather than fix one.
For a specified abstract regular abelian group B on ell labelled points,
the number of embeddings as a subgroup is

\[
\ell!/(\ell|\operatorname{Aut}(B)|).
\]

This follows from the affine normalizer as in the first note; it is also
[Dixon (1971), Lemma 1](https://doi.org/10.4153/CJM-1971-045-7).

Fix f and the multiplicities `a_T` of the nonoptimal abstract types T,
and sum over the remaining optimal blocks. The number of ambient
products is exactly

\[
\frac{n!}{f!}
\prod_T\frac{1}{a_T!\,(|T||\operatorname{Aut}(T)|)^{a_T}}
A_{N-L}(1).                                            \tag{4.2}
\]

Appending `L/2` pairs to an optimal configuration shows

\[
A_{N-L}(1)/A_N(1)\leq n^{L/2}\leq n^{4D}.              \tag{4.3}
\]

All the other factors in (4.2), after division by `C_n(1)`, are at most
one, including when `delta=1,f=0`.

There are at most `(Cn)^(20D)` possible nonoptimal type profiles of
defect D, for an absolute C. Here are sufficient elementary bounds.
The number of abelian isomorphism types of order ell is at most ell:
use the classification by partitions of the prime exponents and
`p(e)<=2^e`. Hence there are at most `n²` such types of order at most n.
The exceptional support, including fixed points, is at most `8D+1`.
An ordered list of at most `8D+1` choices from these types and a
singleton symbol overcounts every profile. Its count is bounded by
the asserted expression, since `D<=n/2`.

Divide (4.1) times (4.2) by `C_n(1)S_m`, using
`S_m>=c_0 2^(m²/4)`. Summing over profiles and absorbing constants gives

\[
\frac{\#\{\text{abelian subgroups with a nonoptimal profile}\}}
 {C_n(1)S_m}
 \leq C_1\sum_{D=1}^m
       \left((C_2n)^{34}2^{-m/128}\right)^D
 =O(2^{-c n})                                          \tag{4.4}
\]

for some absolute `c>0`. The ratio inside the geometric sum tends to
zero exponentially. This counts every possible abelian subgroup;
subgroups failing surjectivity are only overcounted in the upper bound.

## 5. The abelian statistical theorem

### Theorem F

For some absolute `c>0`,

\[
\boxed{
|\mathrm{Ab}_n|
=C_n(1)S_m(1+O(2^{-cn})),\qquad
\frac{|\mathrm{Ab}_n\setminus E_n|}{|\mathrm{Ab}_n|}
=O(2^{-cn}).
}                                                       \tag{5.1}
\]

For a uniform abelian subgroup H, with probability `1-O(2^(-cn))`:

- H is elementary abelian of exponent two;
- it has delta fixed points and all other orbits of size two or four.

Its logarithmic order has the discrete Gaussian limit (1.2). In
particular,

\[
\log_2|H|=n/4+O_{\Pr}(1),\quad
v_2(|H|)=n/4+O_{\Pr}(1),\quad
\Pr\!\left(|H|/2^{v_2(|H|)}=1\right)=1-O(2^{-cn}).       \tag{5.2}
\]

Proof. Combine (1.1) and (4.4). Conditional on `E_n^*`, the uniform
measure is exactly the measure already analyzed in the first note.
The complement has exponentially small probability, so the two
measures differ in total variation by that amount. This proves the
order law and (5.2). QED.

### Corollary G: an unrestricted conclusion

For H uniform in all of `Sub(S_n)`,

\[
\boxed{\Pr(H\text{ is abelian})\leq2^{-n/2+O(\sqrt n)}.} \tag{5.3}
\]

Proof. Since `F_n` is a family of actual subgroups, this probability is
at most `|Ab_n|/|F_n|`. Apply (5.1), (1.3), and (1.4). QED.

The denominator in (5.2) is the number of abelian subgroups; the
denominator in (5.3) is the number of all subgroups. These are different
probability statements.

### A closed asymptotic formula

The coefficient in (5.1) can also be evaluated explicitly. For fixed
`w>0` and even N tending to infinity,

\[
A_N(w)\sim
\frac{e^{-3/(4w)}}{\sqrt{2\pi N}}
\exp\!\left(\sqrt{\frac{3N}{2w}}\right)
\left(\frac{ew}{6N}\right)^{N/4}.                       \tag{5.4}
\]

Here is a proof, including the potential parity issue in the coefficient
estimate. Set `m=N/2` and take the coefficient of `t^m` in
`exp(t/2+wt²/24)`. Let rho solve

\[
\rho/2+w\rho^2/12=m,
\qquad\rho=\frac{\sqrt{9+12wm}-3}{w}.
\]

For independent Poisson variables X and Y with means
`lambda_1=rho/2` and `lambda_2=w rho²/24`, respectively,

\[
A_N(w)=e^{\lambda_1+\lambda_2}\rho^{-m}
              \Pr(X+2Y=m).
\]

This integer-valued variable has mean m and variance
`V=lambda_1+4lambda_2=2m-rho/2`. Fourier inversion gives

\[
\Pr(X+2Y=m)\sim(2\pi V)^{-1/2}.                        \tag{5.5}
\]

To justify it, its centered characteristic function has logarithm
`-V theta²/2+O(m |theta|³)` near zero. On
`|theta|<=m^(-2/5)`, this gives the Gaussian integral with a relative
`o(1)` error. Outside that neighborhood and away from pi, the absolute
value is bounded using
`exp(lambda_2(cos(2theta)-1))`; the remaining integral is
`O(exp(-c m^(1/5)))`. Near pi, the first Poisson factor is at most
`exp(-c lambda_1)=exp(-c' sqrt(m))`. Thus the apparent second peak
from the even-valued variable `2Y` contributes negligibly, proving
(5.5) without a missing lattice factor.

Use `lambda_1+lambda_2=m/2+rho/4` and put `s=sqrt(12m/w)`. Then

\[
\rho=s-3/w+9/(2w^2s)+O(s^{-3}),\qquad
\log\rho=\log s-3/(ws)+O(s^{-3}).
\]

Substitution into (5.5) gives

\[
\log A_N(w)
=-\frac{3}{4w}-\frac12\log(2\pi N)
 +\sqrt{\frac{3N}{2w}}+\frac N4\log\!\left(\frac{ew}{6N}\right)+o(1),
\]

which proves (5.4).

Let `Theta_epsilon=sum_(j in Z+epsilon) 2^(-j²)`, with epsilon as in
(1.2). The Gaussian sum asymptotic for `S_m` in the first note now gives
the fully explicit equivalent

\[
\boxed{
|\mathrm{Ab}_n|\sim
\frac{\Theta_\epsilon}{P_2}
\frac{n!\,e^{-3/4}}{\delta!\sqrt{2\pi N}}
2^{N^2/16}
\exp\!\left(\sqrt{\frac{3N}{2}}\right)
\left(\frac{e}{6N}\right)^{N/4}.
}                                                       \tag{5.6}
\]

For example, the explicit ratio underlying (5.3) is

\[
\frac{|\mathrm{Ab}_n|}{|F_n|}
\sim e^{-9/16}\exp\!\left(\sqrt{\frac{3N}{8}}\right)2^{-N/2}.
                                                               \tag{5.7}
\]

## 6. A larger family with an odd factor in its order

Suppose n is odd, and write `N=n-1`, `m=N/2`. Define `G_n` using an
orbit partition with:

- one block of size three carrying the full symmetric group `S_3`;
- a two-point blocks, each carrying `C_2`;
- b four-point blocks, each carrying either regular Klein-four or one
  of the three dihedral groups of order eight;
- no fixed points.

Thus `a+2b=m-1`. Take the product D of these orbit projections and
the quotient

\[
\pi:D\longrightarrow D/D'
 \cong\mathbb F_2^{a+1}\times(\mathbb F_2^2)^b.
\]

Include every full preimage `pi^(-1)(U)` of a subspace U projecting
onto every displayed factor. Every subgroup recovers all its orbit
projections and its quotient subspace, so no duplicate counting occurs.

If k is the dimension of U and d of the four-point factors are
dihedral, then

\[
|H|=3\cdot2^{k+d}.                                     \tag{6.1}
\]

All members are nonnilpotent, since they have an `S_3` quotient. Their
odd part is exactly three.

Let `s_(a+1,b,k)` have the same meaning as in the first note: k-spaces
surjecting onto each factor of `F_2^(a+1) x (F_2²)^b`.

### Theorem H

The exact order polynomial is

\[
\sum_{H\in G_n}y^{v_2(|H|)}
=\sum_{a+2b=m-1}
 \frac{n!}{6\,2^a a!24^b b!}(1+3y)^b
 \sum_k s_{a+1,b,k}y^k.                                \tag{6.2}
\]

Moreover,

\[
|G_n|=\frac{n!}{6} A_{N-2}(4)S_m(1+O(n2^{-m/4})),       \tag{6.3}
\]

and

\[
\boxed{\frac{|G_n|}{|F_n|}\sim\sqrt{N/24}.}             \tag{6.4}
\]

Proof. For (6.2), use the labelled block count and the independent
choices of dihedral projections, exactly as for `F_n`. The commutator
kernel now has order `3*2^d`, which proves (6.1). The quotient rank is
`a+1+2b=m`, so the same uniform surjectivity estimate proves (6.3).

To evaluate its ratio to (1.3), consider optimal partitions of N with
weights one for pairs and four for four-element blocks. Their pair
count a satisfies

\[
\mathbb E[a]=\frac{A_{N-2}(4)}{2A_N(4)}
             \sim\sqrt{3N/8}.                          \tag{6.5}
\]

The identity marks one pair in the generating function. The asymptotic
follows from the ratio and moment estimates proved in §5 of the first
note. Thus (6.3)/(1.3) is asymptotic to
`(1/3)sqrt(3N/8)=sqrt(N/24)`. QED.

### Corollary I: the former family is negligible in odd degrees

For odd n and uniform unrestricted H,

\[
\Pr(H\in F_n)
 \leq\frac{|F_n|}{|F_n|+|G_n|}
 \leq(\sqrt{24}+o(1))n^{-1/2}.                         \tag{6.6}
\]

The disjointness follows because members of `F_n` are 2-groups, while
members of `G_n` have odd part three. This is an obstruction to any
claim that `F_n` contains almost all subgroups; such a claim was not
made in the first note.

For completeness, the central limit theorem of the first note also
holds for `log_2 |H|` when H is uniform in `G_n`, using the same
centering at `7N/16-(3/8)sqrt(3N/8)` and scaling `sqrt(3N/64)`.
Indeed, `K=m/2+O_P(1)`, `d|a,b,K` is `Binomial(b,3/4)`, and now
`b=(N-2)/4-a/2`. The extra terms in the earlier decomposition are
the constant `log_2 3-3/8` and an `o(sqrt(N))` change in the pair-count
centering. The proof therefore applies without a new estimate.

Consequently, for a uniform member of the explicitly enlarged family
`F_n union G_n`, the odd part equals three with probability tending to
one. This last statement is still about the enlarged family, not about
all subgroups of `S_n`.

## 7. Audit, checks, and the uncompleted comparison

The abelian theorem requires controlling both higher p-power layers and
odd Sylow factors. Lemmas 3.1-3.3 do that uniformly, including the
odd-n/no-fixed-point case. No unproved assertion about their rarity is
used in the count.

The classical source most directly relevant to novelty found in this
pass is [Dixon's 1971 paper](https://doi.org/10.4153/CJM-1971-045-7).
Its principal statistical results concern **maximal** abelian subgroups
and transitive abelian subgroups. Those sampling measures differ from
uniform sampling among all abelian subgroups here. This observation does
not establish novelty; the literature and citations still need checking.

The following checks have been run in `verify_abelian.py`:

- The Birkhoff formula agrees, order by order, with direct enumeration
  for 27 abelian p-group types.
- Direct enumeration finds 1, 2, 5, 21, 87, and 612 abelian subgroups
  for `S_1,...,S_6`, agreeing with
  [Naughton-Pfeiffer, Table 15](https://arxiv.org/abs/1211.1911).
- Both local inequalities were checked on all 244 nonoptimal regular
  abelian types of orders at most 128.
- The global defect inequalities were checked on 3,000 seeded profiles
  and separately on the odd-degree, no-fixed-point `C_3` edge case.

The separate `verify_odd_family.py` independently enumerates every
subgroup of `S_3` and `S_5`, recognizes `G_n` from the actual orbit
action and supported `C_3`, and checks (6.2). It also evaluates the exact
`G_n/F_n` ratios through `n=257`, and compares (5.4) against the exact
coefficient sums through `N=1024` for both `w=1` and `w=4`.

The computations are checks on the proof's algebra and indexing, not
substitutes for its asymptotic estimates.

The attempted dihedral reduction remains useful but incomplete. If H
is subdirect in a product with a `D_8` factor, `H intersection D_8` is
normal in that factor. Every nontrivial normal subgroup of `D_8`
contains its commutator subgroup. Therefore, if H omits that supported
commutator, `H intersection D_8=1`. Deleting the orbit embeds H into
the remaining points; H is the graph of an epimorphism from its image
onto `D_8`. The same statement holds for an omitted square subgroup on
a cyclic order-four orbit. This proves a reduction, but an adequate
uniform count of those epimorphisms has not been obtained.

The unrestricted problem still needs estimates for these subdirect
products and for larger orbits. The `S_3` construction shows that odd
factors must be incorporated into any plausible unrestricted model,
rather than simply declared negligible.

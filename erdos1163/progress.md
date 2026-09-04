# Erdős 1163: subgroup orders through binary quotients

Research note, 4 September 2026

**Later results:** [the second research pass](progress_v2.md)
extends the abelian count and order law to all abelian subgroups, gives
an explicit asymptotic formula, and proves that `F_n` is negligible
among all subgroups in odd degrees by constructing a larger family with
an `S_3` orbit. The results below remain valid on their stated domains.

**Status: substantial partial progress, not a solution of Problem 1163.**
The results below have self-contained proofs and exact computational checks.
Their novelty has not been established by an exhaustive literature review.
All counts concern actual subgroups of the labelled symmetric group, not
isomorphism types or conjugacy classes.

## 1. The question, the draft, and the results obtained

[Problem 1163](https://www.erdosproblems.com/1163) asks for a statistical
description of the arithmetic structure of subgroup orders in symmetric
groups. We adopt the uniform measure on `Sub(S_n)`. The problem's wording
does not specify a unique target limit theorem.

The relevant input from `Rezk_related_v2.pdf` (background draft, not included here) is §4.4, Theorem 4.5, and
Appendix A: counting finite abelian subgroup data through Gaussian
coefficients. The draft counts subgroups of a fixed-height divisible
abelian p-group. That is a different counting problem from `Sub(S_n)`.
Here we use the same elementary linear-algebra mechanism on binary
quotients, and prove all needed counting identities independently. The
geometric Witt-filtration recursion is not needed for these results.

[Roney-Dougal and Tracey, arXiv:2503.05416v1](https://arxiv.org/abs/2503.05416)
already prove `|Sub(S_n)| = 2^(n²/16+o(n²))` (Theorem 1), show that
nonnilpotent subgroups cannot be discarded along `n = 3 mod 4` (Theorem 4),
and give lower bounds for typical Sylow 2-subgroup size (Theorem 6).
We do not claim those results as progress made here.

The results proved in this note are:

1. A relative asymptotic formula for **all elementary abelian 2-subgroups**
   of `S_n`, and a discrete Gaussian limit for their logarithmic orders.
2. An exact order-generating polynomial and a relative asymptotic formula
   for a larger, explicitly defined family `F_n`, formed from two-point
   actions and four-point Klein-four/dihedral actions.
3. For uniform `H` in `F_n`, a central limit theorem for `log_2 |H|`, with
   first-order location `7n/16` and variance asymptotic to `3n/64`.
4. A consequence for the **full uniform measure on `Sub(S_n)`**:

   $$
   \Pr(H\text{ is elementary abelian of exponent }2)
       \leq 2^{-n/2+O(\sqrt n)}.
   $$

5. The explicit lower bound

   $$
   \log_2|\operatorname{Sub}(S_n)|
      \geq \frac{n^2}{16}+\frac34n\log_2n-O(n).
   $$

The unresolved step is to control subgroups outside `F_n`. No assertion
that `F_n` contains almost all subgroups is made or used. In particular,
the central limit theorem below is not a central limit theorem for a
uniform unrestricted subgroup of `S_n`.

## 2. Notation and binary subspace estimates

Put

$$
\delta=n\bmod 2,\qquad N=n-\delta,\qquad m=N/2.
$$

Write

$$
{r\brack k}_2
=\prod_{i=0}^{k-1}\frac{2^r-2^i}{2^k-2^i},
\qquad S_r=\sum_{k=0}^r{r\brack k}_2.
$$

A Gaussian coefficient outside its valid range is zero. Define

$$
P_2=\prod_{i=1}^{\infty}(1-2^{-i})>0.
$$

Counting ordered independent vectors and dividing by the number of bases
of a k-space proves that `{r choose k}_2` counts the k-dimensional
subspaces of `F_2^r`. Its product formula gives

$$
2^{k(r-k)}\leq {r\brack k}_2
\leq P_2^{-1}2^{k(r-k)}.                     \tag{2.1}
$$

Thus, with absolute positive constants,

$$
c\,2^{r^2/4}\leq S_r\leq C\,2^{r^2/4}.      \tag{2.2}
$$

For a uniform subspace `U` of `F_2^r`, its dimension `K` consequently
satisfies `K-r/2=O_P(1)`, with a Gaussian upper bound on the discrete tails.
More precisely, along either fixed parity of r,

$$
\Pr(K-r/2=j)\longrightarrow
\frac{2^{-j^2}}{\Theta_\varepsilon},\qquad
\Theta_\varepsilon=\sum_{t\in\mathbb Z+\varepsilon}2^{-t^2},
                                                        \tag{2.3}
$$

where `epsilon=0` for even r and `epsilon=1/2` for odd r, and j belongs
to that lattice. Also

$$
S_r\sim P_2^{-1}\Theta_\varepsilon 2^{r^2/4}. \tag{2.4}
$$

Indeed, for fixed j the product correction to
`2^(r²/4-j²)` tends to `P_2^(-1)`. Equation (2.1) gives summable domination
by a constant times `2^(-j²)`, proving both assertions.

### Surjectivity onto small coordinate factors

For `a+2b=m`, let `s_(a,b,k)` count k-spaces in

$$
V=\mathbb F_2^a\times(\mathbb F_2^2)^b
$$

that project onto every displayed factor. Define coefficients by

$$
(1-x)^a(1-3x+2x^2)^b=\sum_{t=0}^m c_t x^t.
$$

Then the exact formula is

$$
s_{a,b,k}=\sum_{t=0}^m c_t{m-t\brack k}_2.   \tag{2.5}
$$

To prove this, invert on the product of the subspace lattices of the
coordinate factors. A one-dimensional factor contributes the polynomial
`1-x`. A two-dimensional factor has three hyperplanes with Möbius value
`-1`, and its zero subspace has Möbius value `2`, giving `1-3x+2x²`.
An allowed product subspace of codimension t contains exactly
`{m-t choose k}_2` k-spaces. Summation proves (2.5).

There is also a useful uniform estimate. For a uniform k-space, the
probability of lying in a specified hyperplane is

$$
\frac{{m-1\brack k}_2}{{m\brack k}_2}
=\frac{2^{m-k}-1}{2^m-1}\leq 2^{1-k}.
$$

Failure of surjectivity is contained in a union of `a+3b` such events.
Since this number is at most n, (2.1) and a split at `k=m/4` give,
uniformly in a and b,

$$
\sum_k s_{a,b,k}=S_m(1+O(n2^{-m/4})).        \tag{2.6}
$$

For the split, ranks below `m/4` have total probability
`O(2^(-m²/16))`; ranks at least `m/4` have failure probability at most
`2n 2^(-m/4)`. Conditioning on successful projection also changes the
whole distribution by `O(n2^(-m/4))` in total variation.

## 3. All elementary abelian 2-subgroups

Let `E_n` be the set of all elementary abelian 2-subgroups of `S_n`,
including the trivial group. For fixed `w>0`, put

$$
A_N(w)=[z^N]\exp(z^2/2+wz^4/24),
\qquad C_n(w)=\frac{n!}{\delta!}A_N(w).
                                                        \tag{3.1}
$$

### Theorem A

As n tends to infinity,

$$
|E_n|=C_n(1)S_m\bigl(1+O(n^4 2^{-m/4})\bigr).             \tag{3.2}
$$

With probability tending to one, a uniform member of `E_n` has exactly
delta fixed points and every other orbit has size two or four. Its order
is `2^K`, and `K-m/2` has the discrete Gaussian limit (2.3).

#### Proof: the candidate dominant orbits

Every transitive elementary abelian permutation group is regular:
in an abelian transitive action, a point stabilizer fixes every point;
faithfulness of the induced action makes that stabilizer trivial.

An elementary abelian subgroup H therefore determines, on each orbit,
a regular elementary abelian projection. The product of those projections
is a uniquely determined ambient elementary abelian group. H is a
subdirect subgroup of that product. This uniqueness prevents overcounting.

There is one regular `C_2` on a specified two-element block, and one regular
`C_2^2` on a specified four-element block. For a partition into delta
singletons, a pairs and b four-element blocks, with `a+2b=m`, the ambient
rank is m and the number of labelled partitions is

$$
L_{n,a,b}=\frac{n!}{\delta!2^a a!24^b b!}.                \tag{3.3}
$$

Thus the exact rank-k count for this part of `E_n` is

$$
\sum_{a+2b=m} L_{n,a,b}s_{a,b,k}.                         \tag{3.4}
$$

Equations (2.6) and (3.1) give the claimed main term. They also show that
the rank distribution of this part differs from that of a uniform
subspace of `F_2^m` by `o(1)` in total variation.

#### Proof: excluding every other elementary orbit profile

Suppose H has f fixed points and `a_d` orbits of size `2^d`, for `d>=1`.
The rank of its uniquely determined ambient product is

$$
r=\sum_{d\geq1}d a_d.
$$

Write `f=delta+2t`. Since `d<=2^(d-1)`, the rank deficit is

$$
D=m-r=t+\sum_{d\geq3}(2^{d-1}-d)a_d.                    \tag{3.5}
$$

The excluded profiles have `D>=1`.

On a block of size `2^d`, the number of regular elementary abelian
subgroups is

$$
\frac{(2^d)!}{2^d|\operatorname{GL}(d,2)|}.              \tag{3.6}
$$

For completeness, all regular embeddings are conjugate. Their normalizer
consists of affine maps `x -> v+g(x)`, so has the denominator's order.
This proves (3.6).

Fix the bad data t and `(a_d)_(d>=3)` and sum over the remaining two- and
four-point blocks. Put

$$
B=2t+\sum_{d\geq3}2^d a_d.
$$

The number of possible ambient products is

$$
\frac{n!}{(\delta+2t)!}
\prod_{d\geq3}\frac{1}{a_d!\,(2^d|\operatorname{GL}(d,2)|)^{a_d}}
\ A_{N-B}(1).                                          \tag{3.7}
$$

Here `B<=8D`, because `2^d<=8(2^(d-1)-d)` for every `d>=3`.
If B is even, appending `B/2` pairs to each monomial configuration in
`A_(N-B)(1)` injects these configurations into those of `A_N(1)`.
The ratio of their weights is at most `n^(B/2)`. Hence

$$
A_{N-B}(1)/A_N(1)\leq n^{B/2}\leq n^{4D}.               \tag{3.8}
$$

Each such ambient product contributes at most `S_(m-D)` subgroups, and
by (2.2), for `1<=D<=m`,

$$
\frac{S_{m-D}}{S_m}
 \leq C2^{-D(2m-D)/4}\leq C2^{-mD/4}.                  \tag{3.9}
$$

There are at most `4^D` bad data of a given deficit D. To see this, the
weights `2^(d-1)-d` for `d>=3` are the distinct integers `1,4,11,...`.
They give a partition of D together with t extra parts of size one.
An ordinary partition admits at most `D+1` choices for the number of
those distinguished ones. There are at most `2^(D-1)` partitions of D,
and `D+1<=2^D`.

Divide the total bad count by `C_n(1)S_m`. All omitted factorial and
normalizer factors in (3.7) are at most one, so (3.8)-(3.9) bound this
ratio by

$$
C\sum_{D=1}^m\bigl(4n^4 2^{-m/4}\bigr)^D
   =O(n^4 2^{-m/4}).                                    \tag{3.10}
$$

This is a convergent geometric bound for all sufficiently large n.
Together with (3.4) and (2.6), it proves (3.2), the orbit claim, and the
rank limit. QED.

## 4. A larger family with an exact order polynomial

The regular Klein-four group is not the only useful group on four points.
There are also three dihedral subgroups `D_8` of order eight in `S_4`.
Each has derived subgroup of order two, and quotient `C_2^2`.

For an orbit partition as in (3.3), assign:

- `C_2` to each two-point block;
- either its regular `C_2^2`, or any one of its three `D_8` subgroups,
  to each four-point block.

Let D be the direct product of the assigned permutation groups. Its
abelianization is

$$
\pi:D\longrightarrow D/D'\cong
\mathbb F_2^a\times(\mathbb F_2^2)^b.
$$

For every subspace U projecting onto every displayed factor, include

$$
H=\pi^{-1}(U)
$$

in `F_n`. Equivalently, `F_n` consists of the subgroups with exactly
delta fixed points, the displayed orbit projections, and which contain
the derived subgroup of the product of their orbit projections.

This is an intrinsic, unambiguous family of actual subgroups. Each H
recovers its orbit partition, its projections, their product D, and U.
For `D_8`, the preimage projects onto `D_8` because U surjects onto its
abelianization and the preimage contains its entire derived kernel.
Thus all the stipulated blocks really are H-orbits.

If d of the b four-point projections are dihedral, then

$$
|D'|=2^d,\qquad \log_2|H|=\dim U+d.                    \tag{4.1}
$$

### Theorem B

The exact order-generating polynomial for `F_n` is

$$
\boxed{
\sum_{H\in F_n} y^{\log_2|H|}
 =\sum_{a+2b=m} L_{n,a,b}(1+3y)^b
       \sum_{k=0}^m s_{a,b,k}y^k.
}                                                       \tag{4.2}
$$

In particular,

$$
|F_n|=C_n(4)S_m(1+O(n2^{-m/4})).                         \tag{4.3}
$$

#### Proof

For each fixed partition, choosing d dihedral projections gives
`binom(b,d) 3^d` choices. There are `s_(a,b,k)` admissible k-spaces,
and (4.1) gives the exponent of y. No choices produce the same H by the
intrinsic recovery above. Summing gives (4.2). At `y=1`, use the uniform
estimate (2.6); the block weights are now one for pairs and four for
four-element blocks. This gives (4.3). QED.

For example, the exact polynomial for `F_4` is

$$
3y+4y^2+3y^3.
$$

The three order-two groups are generated by the double transpositions;
the four order-four groups are the four Klein-four subgroups; and the
three order-eight groups are the Sylow 2-subgroups of `S_4`.

## 5. An order central limit theorem inside F_n

### Theorem C

If H is uniform in `F_n`, then

$$
\frac{\log_2|H|}{n}\xrightarrow{\Pr}\frac7{16},          \tag{5.1}
$$

and the following more precise limit holds:

$$
\boxed{
\frac{\log_2|H|-\frac{7N}{16}
           +\frac38\sqrt{\frac{3N}{8}}}
      {\sqrt{3N/64}}
\ \Longrightarrow\ \mathcal N(0,1).
}                                                       \tag{5.2}
$$

Moreover, `Var(log_2 |H|) = 3N/64 + O(sqrt(N))`.

This is a theorem for `F_n`, not for unrestricted `Sub(S_n)`.

#### Proof: block statistics

Consider first the unconditioned construction that weights orbit
partitions by `L_(n,a,b) 4^b` and takes an arbitrary uniform subspace of
`F_2^m`. By (2.6), rejecting failed coordinate projections changes this
construction by `o(1)` in total variation, and yields uniform `F_n`.

More generally, under weights `L_(n,a,b) w^b`, the probability of a pair
count a is proportional to

$$
T_w(a)=\frac{w^{(m-a)/2}}
 {2^a a!24^{(m-a)/2}((m-a)/2)!},\qquad a\equiv m\pmod2.
$$

The consecutive ratio is

$$
\frac{T_w(a+2)}{T_w(a)}
 =\frac{3(m-a)}{w(a+1)(a+2)}.                           \tag{5.3}
$$

It is decreasing in a. For every fixed eta>0, it is bounded above by a
constant strictly less than one when
`a >= (sqrt(3/(2w))+eta) sqrt(N)`, and bounded below by a constant
strictly greater than one when
`a <= (sqrt(3/(2w))-eta) sqrt(N)` and this lower range is nonempty.

To turn this into concentration, compare a point beyond either cutoff
with one at a cutoff halfway to `sqrt(3N/(2w))`. There are a constant
times `sqrt(N)` steps between them, each with a geometric penalty
bounded away from one. The more distant tail is a geometric sum;
on the finite lower tail an additional factor `O(sqrt(N))` suffices.
Its probability tends to zero. Thus

$$
\frac a{\sqrt N}\xrightarrow{\Pr}\sqrt{\frac3{2w}}.
                                                        \tag{5.4}
$$

For `w=4`, this gives `a/sqrt(N) -> sqrt(3/8)`, and

$$
b=N/4-a/2,\qquad b/N\xrightarrow{\Pr}1/4.              \tag{5.5}
$$

#### Proof: dihedral choices and subgroup order

Conditional on the orbit partition and the chosen subspace U, the
dihedral count d is exactly `Binomial(b,3/4)`: each four-point block has
one Klein-four choice and three dihedral choices. These choices are
independent of U. Meanwhile, by (2.3) and (2.6),

$$
K=\dim U=m/2+O_{\Pr}(1).
$$

Conditional binomial characteristic functions, together with (5.5),
give

$$
\frac{d-3b/4}{\sqrt{3N/64}}\Longrightarrow\mathcal N(0,1).
                                                        \tag{5.6}
$$

One can see this directly by expanding the characteristic function of
each centered Bernoulli variable: its logarithm is
`-3t²/(32 sigma_N²)+O(sigma_N^(-3))`, where
`sigma_N²=3N/64`. Multiplication over b trials yields limit `-t²/2`.
The error is `O(N^(-1/2))`, uniformly for `b<=N/4`.

Finally, (4.1) gives

$$
\log_2|H|
 =\frac{7N}{16}-\frac{3a}{8}
   +(d-3b/4)+(K-m/2).
$$

Replace a by `sqrt(3N/8)` at an `o_P(sqrt(N))` cost using (5.4).
The rank term is `o_P(sqrt(N))`. Equation (5.6) proves (5.2), and
(5.1) follows. QED.

For the variance assertion, the same ratios give a moment bound as
follows. Their crossing of one locates a mode `a_0=sqrt(3N/(2w))+O(1)`.
In an interval `[c sqrt(N), C sqrt(N)]` containing this mode, the
logarithm of (5.3) decreases at a rate bounded above and below by
positive constants times `N^(-1/2)` per lattice step. Multiplying ratios
therefore bounds `T_w(a)/T_w(a_0)` above by
`C_1 exp(-c_1 (a-a_0)^2/sqrt(N))`. It bounds this ratio below by a
positive constant for `|a-a_0|<=c_2 N^(1/4)`, so the normalizing sum is
at least a constant times `N^(1/4) T_w(a_0)`. Outside that interval,
monotonicity gives geometric tails with total second moment
`O(N^2 exp(-c_3 sqrt(N)))`. Summing the central Gaussian bound now
gives `E[(a-a_0)^2]=O(sqrt(N))`, hence `Var(a)=O(sqrt(N))` and
`E[a]=O(sqrt(N))`. The exponentially small rejection probability
preserves these bounds, since `a<=n`.

Equation (2.1) and the uniformly positive acceptance probability also
give `E[(K-m/2)^2]=O(1)`. Conditional on a and K, d has variance
`3b/16` and mean `3b/4`. The law of total variance consequently gives

$$
\operatorname{Var}(K+d)
=\frac3{16}\mathbb E[b]+\operatorname{Var}(K-3a/8)
=\frac{3N}{64}+O(\sqrt N),
$$

where the covariance term is bounded by Cauchy-Schwarz. This proves
the additional moment assertion.

## 6. Consequences for unrestricted symmetric-group subgroups

These consequences use inclusions and counts, not a claim of dominance
for `F_n`.

### A coefficient estimate

Write `m=2q+e`, where `e` is zero or one. In the coefficient `A_N(w)`,
the possible pairs of counts are `a=e+2j`, `b=q-j`. If `T_0` is the
term with j zero, then

$$
T_0=\frac{w^q}{2^e e!24^q q!},\qquad
\frac{T_j}{T_0}
  =\left(\frac6w\right)^j\frac{(q)_j e!}{(e+2j)!}.
$$

Since `(q)_j<=q^j`,

$$
1\leq\frac{A_N(w)}{T_0}
 \leq \sum_{j\geq0}\frac{(6q/w)^j}{(2j)!}
 \leq \exp(\sqrt{6q/w}).                               \tag{6.1}
$$

For each fixed positive w, this proves

$$
\log A_N(w)=\log\!\left(\frac{w^q}{2^e e!24^q q!}\right)
             +O(\sqrt N),                              \tag{6.2}
$$

with natural logarithms in this display. In particular,

$$
\log_2\frac{A_N(1)}{A_N(4)}=-\frac N2+O(\sqrt N).       \tag{6.3}
$$

### Corollary D: a global exclusion theorem

For uniform H in `Sub(S_n)`,

$$
\Pr(H\in E_n)
 \leq\frac{|E_n|}{|F_n|}
 =2^{-N/2+O(\sqrt N)}
 =2^{-n/2+O(\sqrt n)}.                                 \tag{6.4}
$$

Proof: apply (3.2), (4.3), and (6.3). QED.

In fact, the same upper bound holds for the probability that H is
elementary abelian of **any** prime exponent. Here is the additional
estimate. If `p>=3`, every transitive elementary abelian p-projection
has degree `p^d` and rank d, with `d/p^d<=1/p`. Its total ambient rank
is therefore at most `n/p`. The Gaussian estimate over `F_p`, proved
as in (2.1), bounds its subgroup count by

$$
O(n) p^{n^2/(4p^2)}.
$$

For a fixed orbit profile, the number of ambient products is at most n!:
use the analogue of (3.6), whose factorials cancel the labelled block
denominators. There are at most `2^n` profiles and at most n primes.
Since `(log_2 p)/p²` decreases for `p>=3`, the total number for odd primes
is at most

$$
2^{(\log_2 3)n^2/36+O(n\log n)}.
$$

This is smaller than `|F_n|` by a quadratic exponential factor, so does
not change (6.4). The common trivial subgroup causes harmless overcounting.

### Corollary E: an explicit second-order lower bound

Equations (2.2), (4.3), (6.2), and Stirling's formula yield

$$
\log_2|F_n|
 =\frac{n^2}{16}+\frac34n\log_2n+O(n).                 \tag{6.5}
$$

Since `F_n` is contained in `Sub(S_n)`, this proves

$$
\log_2|\operatorname{Sub}(S_n)|
 \geq\frac{n^2}{16}+\frac34n\log_2n-O(n).
$$

The coefficient `3/4` comes from partitioning nearly all points into
four-element blocks: the label count is of size `n!/(4!^(n/4)(n/4)!)`.
Both `E_n` and `F_n` have this same `n log n` coefficient, while their
counts differ by an exponential factor of order `2^(n/2)`.

## 7. Exact independent checks

The accompanying [verify.py](verify.py) uses only the Python standard library.
It computes (2.5) and (4.2) with exact integers. The output is saved in
[verification.json](verification.json).

There is also an independent exact enumeration of all `E_n` by rank.
Let `h_j(n)` count homomorphisms from `C_2^j` to `S_n`. Looking at the
orbit of the label 1 gives

$$
h_j(0)=1,\qquad
h_j(n)=\sum_{\substack{0\leq d\leq j\\2^d\leq n}}
 \frac{(n-1)!}{(n-2^d)!}{j\brack d}_2 h_j(n-2^d).       \tag{7.1}
$$

There are `{j choose d}_2` kernels for a transitive action on `2^d`
points, and `(2^d-1)!` labelings for each kernel on a chosen block.
This explains every factor in (7.1).

Möbius inversion on the common kernel of the entire action then gives
the exact number of elementary rank-k subgroups:

$$
\frac{1}{|\operatorname{GL}(k,2)|}
 \sum_{j=0}^k{k\brack j}_2
 (-1)^{k-j}2^{\binom{k-j}{2}}h_j(n).                    \tag{7.2}
$$

The division is by the number of isomorphisms onto a fixed image.

The checks completed are:

- Enumerated every subspace of `F_2^m` for `0<=m<=6`, checking (2.5)
  for every possible pair `(a,b)` of that total rank.
- Independently generated actual elementary abelian permutation
  subgroups of `S_n` for `1<=n<=7`, and checked (7.2) rank by rank.
- Checked the small order polynomial for `F_4`.
- Independently enumerated all 2-subgroups of `S_4`, `S_5`, and `S_6`
  (20, 76, and 631 groups respectively), recognized membership in `F_n`
  directly from their permutation actions and supported commutators,
  and checked (4.2) order by order. For `F_6` this gives
  `15y + 105y² + 165y³ + 45y⁴`.
- Compared the exact unrestricted elementary count and the exact
  `F_n` count to the relative asymptotic formulas through `n=128`.

Representative exact-computation summaries (displayed values rounded):

| n | log2(|E_n|/|F_n|) | fraction of E_n with only optimal orbits | |E_n|/(C_n(1)S_m) | |F_n|/(C_n(4)S_m) |
|---:|---:|---:|---:|---:|
| 16 | -4.6407 | 0.761452 | 0.675699 | 0.489642 |
| 32 | -11.5756 | 0.934376 | 0.971816 | 0.902913 |
| 64 | -25.6451 | 0.998849 | 1.000358 | 0.999171 |
| 128 | -54.7463 | 1.000000 | 1.000000 | 1.000000 |

These finite checks support the formulas and catch indexing and
overcounting mistakes; the asymptotic conclusions rely on the proofs.

## 8. What remains to solve Problem 1163

The derived results rule out taking a uniform binary subspace in one
elementary abelian ambient group as a justified model for unrestricted
subgroups. That model suggests order about `2^(n/4)`, whereas the larger
family proved here has order about `2^(7n/16)`, and all elementary
abelian subgroups together are exponentially rare in `Sub(S_n)`.

There are three concrete missing comparisons:

1. Among 2-subgroups with orbit lengths at most four, control cyclic
   order-four projections and subdirect products that do not contain
   the entire product of the orbit projections' derived groups.
2. Control larger orbits at the relative-count scale, rather than only
   at the scale of the leading quadratic logarithm.
3. Count non-2-subgroups, including odd normal factors attached to
   binary quotients. These can affect arithmetic order statistics and
   cannot be discarded by nilpotence heuristics.

Proving any of those families negligible requires an actual counting
bound. None follows from the Gaussian coefficient identity in v2,
from (6.5), or from the known leading asymptotic for `Sub(S_n)`.

The next focused target is the first comparison: an order-refined
enumeration of all subdirect products of transitive 2-groups of degrees
two and four. This would determine whether the central limit theorem
for `F_n` extends to the full class of 2-subgroups with those orbit sizes.

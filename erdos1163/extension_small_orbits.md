# All 2-subgroups with orbits of size at most four

Independent extension, 4 September 2026.

This note proves that the family `F_n` in [progress.md](progress.md) is asymptotically
all 2-subgroups with orbits of size at most four. It does **not** assert
that those orbit sizes are typical among unrestricted 2-subgroups.

## Theorem

Let `B_n` be the set of all actual 2-subgroups of `S_n` whose orbits have
size 1, 2, or 4. Put `delta = n mod 2`, `N = n-delta`, and `m=N/2`.
There is an absolute constant `c_0>0` such that

$$
 |B_n\setminus F_n|/|F_n|=O(2^{-c_0n}).                 \tag{1}
$$

Consequently the relative asymptotic formula and order central limit
theorem previously proved for `F_n` hold for **all** of `B_n`:

$$
 |B_n|\sim n![z^N]\exp(z^2/2+z^4/6)\,S_m,
$$

and, for a uniform `H` in `B_n`,

$$
\frac{\log_2|H|-7N/16+(3/8)\sqrt{3N/8}}
     {\sqrt{3N/64}}
\ \Longrightarrow\ \mathcal N(0,1).                  \tag{2}
$$

Here `S_r` is the number of subspaces of `F_2^r`. The estimates
`S_r` comparable to `2^(r^2/4)` and
`|GL(k,2)| >= P_2 2^(k^2)` are used below; they were proved directly in
the earlier note. All constants below are absolute.

## 1. Exact class-two parametrization

The transitive 2-subgroups on a specified four-point set are its one
regular `V_4`, its three cyclic groups of order four, and its three
Sylow groups `D_8`. This follows directly from the three Sylow groups
and their subgroups, or by listing the elements of `S_4`.

Fix an orbit partition with `a` pairs and `b` four-point blocks. Suppose
`c` four-block projections are cyclic, `d` are dihedral, and `e` are
Klein-four, so `b=c+d+e`. Its unique product of orbit projections is

$$
 D=C_2^a\times C_4^c\times D_8^d\times V_4^e.
$$

Let `Z` be the product of the order-two square subgroups of the cyclic
and dihedral factors. It is central and has rank `z=c+d`; the quotient
`V=D/Z` is binary of rank

$$
 r=a+c+2d+2e=M-c,\qquad M=a+2b.
$$

The square map is a quadratic map `q:V -> Z`. Its coordinates are
`X_i^2` for a cyclic factor and `X_iY_i` for a dihedral factor; the two
coordinates on each dihedral factor are chosen to correspond to two
involutions generating that factor. The square of a lift of `v` is
independent of the lift because `Z` is central of exponent two.

Every subgroup `H` is described by

$$
 U=HZ/Z\leq V,\qquad W=H\cap Z\leq Z.
$$

If `dim U=k` and `codim_Z W=t`, such subgroups exist precisely when
`q(U) subset W`. In that case their number for fixed `(U,W)` is

$$
 2^{kt}.                                               \tag{3}
$$

Indeed, the preimage of `U` modulo `W` then has all squares trivial,
hence is an elementary abelian group of rank `k+t`. The desired
subgroups are its complements to `Z/W`, counted by the `2^(kt)` linear
maps from one complement to `Z/W`.

The condition that the subgroup projects onto each displayed orbit
group is exactly that `U` projects onto each displayed quotient factor.
For `C_4` and `D_8`, this uses the elementary fact that no proper
subgroup surjects onto their quotient by their Frattini subgroup.
It also follows by inspecting these two groups directly.

To count `U`, choose an ordered basis of it. Its embedding in `V` is
a full-rank `k by r` matrix. Divide the count by `|GL(k,2)|`. Each
dihedral coordinate pair is an independent pair of linear forms on
`F_2^k`; each cyclic coordinate is a nonzero linear form. Upper bounds
may discard the full-rank condition and the nonzero conditions.

Homogeneous quadratic polynomials in characteristic two are identified
here with their functions on the binary vector space. This is injective:
the monomials `x_i^2` give its linear terms and `x_ix_j` its distinct
quadratic terms. Evaluation at each basis vector recovers the square
coefficients; evaluation at each sum of two basis vectors then recovers
the mixed coefficients. Thus linear dependence of the quadratics can be tested
either as polynomials or as functions.

## 2. Nonsaturated dihedral factors without cyclic orbits

First let `c=0`, so `r=M=a+2b` and `Z` has rank `d`.
Write `q_i=X_iY_i`, for `1<=i<=d`, for the restricted dihedral square
forms on an ordered basis of `U`. They are nonzero products of distinct
linear forms. If their span has dimension `d-h`, an upper bound on
the number of ordered coordinate pairs is

$$
 2^{2kd}\binom dh 2^h
       2^{-h(2k-d+h)}.                                 \tag{4}
$$

Choose `d-h` positions forming a basis of the span. Their coordinate
pairs have at most `2^(2k(d-h))` choices. At each remaining position
the quadratic is in that span, with at most `2^(d-h)` choices, and a
nonzero product of distinct linear forms has exactly two ordered
factorizations. This proves (4), with harmless overcounting if there
is more than one possible basis subset.

The span of the values of the vector-valued quadratic map has the same
dimension `d-h`: its annihilator is the space of linear relations among
the coordinate quadratic functions. Hence there are
`[h choose t]_2` possible codimension-`t` spaces `W` containing `q(U)`.
Multiplying (4) by (3), the unrestricted choices for the other columns,
and the bound for this Gaussian coefficient gives the following upper
bound for the number with `t>=1`:

$$
 C\sum_{k=0}^r\sum_{h\geq t\geq1}
 2^{k(r-k)}\binom dh2^h
 2^{-h(2k-d+h)+t(h-t+k)}.                               \tag{5}
$$

The estimate is valid also when an ignored projection or full-rank
condition is impossible, since those terms only increase the bound.

Put `h=t+u` and `j=k-r/2`. The exponent in (5), excluding `binom(d,h)2^h`,
is exactly

$$
 \frac{r^2}{4}
 -(j+t/2+u)^2-\frac{3t^2}{4}
 -t(r/2-d)-u(r-d).                                    \tag{6}
$$

The sum over `k` of the first negative square is bounded absolutely.
Since `d<=r/2`, the sum over `u` is a bounded geometric series after
using `binom(d,t+u)2^(t+u) <= (2d)^(t+u)`. Thus, for sufficiently large
`r`, the number of nonsaturated subdirect subgroups of this one ambient
group is at most

$$
 C S_r\sum_{t\geq1}(2d)^t
      2^{-3t^2/4-t(r/2-d)}.                            \tag{7}
$$

If `d=0` this count is zero. For all `d<=r/2`, the expression is at
most `S_r 2^(O(log^2(r+2)))`; the negative quadratic in `t` proves this
by completing a square once more.

For each specified set of dihedral blocks there are `3^d` choices of
their embedded groups. Sum (7) over the block types, with weights
`binom(b,d)3^d`, and divide by `4^b S_r`. The resulting bound is

$$
 C\sum_{t\geq1}(2b)^t2^{-3t^2/4}
    2^{-ta/2}\left(\frac{3+2^{-t}}4\right)^b.           \tag{8}
$$

For every `t>=1`, the last factors are at most
`2^(-a/2)(7/8)^b`. Since `a+2b=r`, this is at most
`2^(-beta r/2)` where `beta=log_2(8/7)>0`. The remaining sum is
`2^(O(log^2(r+2)))`. Thus (8) is `O(2^(-c_1 r))` for an absolute
`c_1>0`, **uniformly in the orbit profile** `(a,b)`.

This proves that all the nonsaturated subdirects are exponentially
negligible after summing the cyclic-free projection types. No generic
assumption on the individual restricted quadratic forms was needed.

## 3. Cyclic four-point projections are negligible

Let `c>=1`. We prove a uniform bound for the total number of subdirect
subgroups of one ambient group with these projection types:

$$
 \#\{H\leq D\text{ subdirect}\}
       \leq C S_M 2^{-Mc/6}                            \tag{9}
$$

for all sufficiently large `M`, independently of `a,c,d,e`.

Use the alternating polar forms of the dihedral quadratics:
`B_i=X_i wedge Y_i`. If these `d` alternating forms have span of
dimension `d-h`, the counterpart of (4) is

$$
 2^{2kd}\binom dh6^h2^{-h(2k-d+h)}.                    \tag{10}
$$

The proof is identical, except that a nonzero decomposable alternating
form has exactly six ordered independent factorizations. Its two linear
factors form an ordered basis of its unique two-dimensional support,
and `|GL(2,2)|=6`. The support of a nonzero decomposable alternating
form B is intrinsically the space of linear forms u with `u wedge B=0`.

Let `T=W^perp <= F_2^c directsum F_2^d`. Put

$$
 p=\dim(T\cap\mathbb F_2^c),\quad
 q=\dim\operatorname{pr}_{\mathbb F_2^d}T.
$$

Thus `t=p+q`. Set `R=T intersect F_2^c` and let `Q` be its projection
onto the dihedral coordinates. Necessarily `Q` lies in the `h`-dimensional
relation space of the polar forms, so `q<=h`. There are at most

$$
 {c\brack p}_2{h\brack q}_2 2^{(c-p)q}                 \tag{11}
$$

choices for `R,Q,T`: the last factor counts graphs from `Q` to
`F_2^c/R`. The cyclic linear coordinate matrix must annihilate `R`,
so its number of choices is at most `2^(k(c-p))`. We discard all the
additional quadratic constraints imposed by the graph and thus retain
an upper bound.

Combine (3), (10), and (11), divide by `GL(k,2)`, and bound each Gaussian
coefficient by its leading power times `P_2^(-1)`. With `h=q+u` and
`j=k-r/2`, the exponent becomes exactly

$$
 \frac{r^2}{4}-(j+q/2+u)^2-\frac{3q^2}{4}
 -q(r/2-d-c+p)-u(r-d)+p(c-p).                         \tag{12}
$$

Here

$$
 r/2-d-c=a/2+e-c/2\geq-c/2,\qquad
 r-d\geq M/2.
$$

Replace `binom(d,q+u)6^(q+u)` by `(6d)^(q+u)`. Sum over `k` using
the negative square, and over `u` using a geometric series; the latter
has ratio at most `6M 2^(-M/2)` and is bounded for large `M`.
Bound `p(c-p)<=c^2/4` and sum over its at most `c+1` choices. Finally,
with `L=log_2(6M)`,

$$
 \sum_{q\geq0}2^{-3q^2/4+q(c/2+L)}
      \leq C2^{(c/2+L)^2/3}.
$$

If `d=0`, only `q=u=0` occurs and the same upper bound holds directly.
These estimates prove that the logarithm of the count is at most

$$
 \frac{M^2}{4}-\frac{Mc}{2}+\frac{7c^2}{12}
       +O(c\log M+\log^2 M).                         \tag{13}
$$

Because `1<=c<=M/2`, the first two correction terms satisfy
`-Mc/2+7c^2/12 <= -5Mc/24`. Uniformly for `c>=1`, the error in (13)
is at most `Mc/24` once `M` is sufficiently large. This proves (9),
using `S_M` comparable to `2^(M^2/4)`.

There are `binom(b,c)3^c4^(b-c)` ambient projection choices with exactly
`c` cyclic blocks. Relative to `4^b S_M`, summing (9) gives at most

$$
 C\sum_{c\geq1}\binom bc(3/4)^c2^{-Mc/6}
       =O(M2^{-M/6}).                                \tag{14}
$$

Together (8) and (14) show that for every fixed partition into `a` pairs
and `b` four-blocks, the number of all subdirect 2-subgroups is

$$
 4^b S_M(1+O(2^{-c_2 M})),\qquad M=a+2b,             \tag{15}
$$

uniformly in `a,b`. The main term comes precisely from the saturated
`V_4/D_8` family. Its count differs from `4^b S_M` by an exponentially
small relative amount by the elementary coordinate-surjectivity union
bound in the earlier note. After enlarging its constant, (15) also
implies a uniform upper bound `C4^b S_M` for every `M>=0`.

## 4. Extra fixed points

Every nontrivial orbit has even size, so the number of fixed points is
`f=delta+2s`, where `0<=s<=m`. For a fixed `f`, summing (15) over labelled
orbit partitions gives, for `m-s` large,

$$
 \frac{n!}{f!} A_{N-2s}(4)S_{m-s}
       (1+O(2^{-c_2(m-s)})),                          \tag{16}
$$

where `A_L(4)=[z^L]exp(z^2/2+z^4/6)`. The corresponding uniform upper
bound with an absolute constant holds also when `m-s` is small.

Appending `s` pair blocks to each coefficient contribution proves

$$
 A_{N-2s}(4)/A_N(4)\leq n^s.
$$

Also `S_(m-s)/S_m <= C2^(-ms/4)` for `s<=m`. After division by the
`s=0` main term, the total from extra fixed points is therefore at most

$$
 C\sum_{s\geq1}(n2^{-m/4})^s=O(2^{-c_3 n}).          \tag{17}
$$

For `s=0`, the non-family contribution is exponentially small by
(8) and (14). This proves (1). Uniform measure on `B_n` differs in total
variation by `O(2^(-c_0 n))` from uniform measure on its subset `F_n`;
therefore all previously proved distributional conclusions for `F_n`,
including (2), transfer immediately.

## Scope and review status

The theorem is a statement about an entire orbit-bounded class, rather
than only about a constructed family. It does not control 2-subgroups
with eight-point or larger orbits. In fact, separate work on an
eight-point extraspecial projection gives evidence that those cannot
be discarded when considering all 2-subgroups.

The proof above is new work within this research session. A separate
independent audit and a literature novelty check are still required
before claiming a publishable result. The exact class-two counting
formula is checked independently in [verify_small_orbits.py](verify_small_orbits.py).

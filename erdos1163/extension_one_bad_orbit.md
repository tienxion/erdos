# One arbitrary exceptional eight-point orbit is exponentially negligible

Research extension, 4 September 2026.

This result includes non-class-two orbit projections. It does not yet
count an arbitrary number of exceptional orbits.

**Further extension:** Section 5 below treats every number of exceptional
orbits up to `floor(log_2(n)/16)`, with a uniform error bound.

Let `J_n` be the class from `extension_efficient_orbits.md`: its
nontrivial orbit projections are `C_2` on pairs, regular `V_4` or
`D_8` on four points, and the efficient extraspecial group `E` on eight
points. Arbitrary fixed points and arbitrary subdirect products are
allowed. Let `Q_n` be its asymptotically dominant saturated subfamily.

Let `X_n` be the class obtained by requiring exactly one eight-point
orbit whose projection is any transitive 2-group **other than E**, with
all remaining nontrivial projections from the list defining `J_n`.
There is no restriction on the nilpotency class of the exceptional
projection or of the whole subgroup.

Then

\[
\boxed{
\frac{|X_n|}{|Q_n|}
\leq 2^{-n/4+O(\sqrt n+\log n)}.
}                                                     \tag{1}
\]

The argument uses a finite quotient inequality, verified independently
by enumerating subgroups of a Sylow 2-subgroup of `S_8`, and an
epimorphism bound from Roney-Dougal–Tracey. The asymptotic estimates
below are proofs, not numerical extrapolations.

## 1. A weighted moment bound for the efficient class

For fixed nonnegative real numbers `alpha,beta`, define

\[
M_{\alpha,\beta}(s)
=\sum_{L\in J_s}2^{\alpha d(L)+\beta\log_2|L'|},
\]

where `d(L)` is the minimal number of generators. Put
`delta=s mod 2`, `N=s-delta`, and `r=N/2`. Define

\[
B_N^{(\beta)}
=[z^N]\exp\!\left(
 \frac{z^2}{2}
 +\frac{(1+3\cdot2^\beta)z^4}{24}
 +\frac{2^\beta z^8}{384}\right).
\]

There is a constant depending only on `alpha,beta` such that

\[
M_{\alpha,\beta}(s)
\leq C_{\alpha,\beta}\,s!\,S_r\,2^{\alpha r/2}
 B_N^{(\beta)}.                                      \tag{2}
\]

In particular, using the coefficient estimate below,

\[
M_{\alpha,\beta}(s)
\leq s! B_N S_r\,
 2^{(\alpha/2+\beta/4)r+O_{\alpha,\beta}(\sqrt s)}.
                                                               \tag{3}
\]

### Proof of the weighted subgroup estimate

First fix the actual orbit partition with `a,b,c` blocks of sizes
`2,4,8`, so `r=a+2b+4c`. Choose `d` dihedral projections among the
four-point blocks, and put `z=d+c`. Write `Z=D'` for the ambient
central elementary abelian group of rank z.

For a subdirect subgroup L, let `U=LZ/Z`, `dim U=k`, and let
`W=L intersect Z` have codimension t. Let the restricted coordinate
square forms have span of dimension `z-h`. Thus `0<=t<=h<=z`.
As in the existing efficient-orbit proof,

\[
\Phi(L)=\langle q(U)\rangle,\qquad
d(L)=k+h-t,\qquad \log_2|L'|\leq z.                  \tag{4}
\]

The square-span equality holds because all commutators are polarizations
of squares in an exponent-four class-two group. The first equality
also shows exactly why the generator-rank defect is `h-t`.

The representation bound from `extension_efficient_orbits.md` gives,
after division by `|GL(k,2)|` and the choice of W and its complement,
an upper bound with prefactor
`C binom(z,h)72^h` and binary exponent

\[
\frac{r^2}{4}
 -(j+t/2+u)^2-\frac{3t^2}{4}
 -t(r/2-z)-u(r-z),                                  \tag{5}
\]

where `h=t+u` and `j=k-r/2`. This bound includes `t=h=0`.

Multiplying by the weight in (4) adds
`alpha(k+h-t)+beta z`. Completing the square transforms (5) into

\[
\begin{aligned}
 &\frac{r^2}{4}+\frac{\alpha r}{2}+\beta z
       +\frac{\alpha^2}{4}\\
 &\quad -(j+t/2+u-\alpha/2)^2-\frac{3t^2}{4}
       -t(r/2-z+\alpha/2)-u(r-z).                   \tag{6}
\end{aligned}
\]

The cancellation of the apparent `alpha u` cost is useful: weighting
by generator rank does not weaken the geometric decay in u.

Sum over k; the negative-square sum is bounded independently of all
profile parameters. Bound `binom(z,h)72^h` by `(72r)^(t+u)`. The u
sum is geometric with ratio at most `72r 2^(-r/2)`, so it is bounded
for large r. The remaining t sum has terms at most

\[
(72r)^t2^{-3t^2/4-t(r/2-z)}.
\]

Now sum over the dihedral choices with their multiplicities `3^d`
and the extra weight `2^(beta z)`. The natural normalization becomes
`(1+3*2^beta)^b (105*2^beta)^c`. Averaging the last negative factor
under these weights gives exactly

\[
2^{-t(a/2+c)}
\left(\frac{3\cdot2^\beta+2^{-t}}
{1+3\cdot2^\beta}\right)^b.                         \tag{7}
\]

For `t>=1`, this is at most `2^(-a/2-c) theta_beta^b`, where

\[
\theta_\beta=
\frac{3\cdot2^\beta+1/2}{1+3\cdot2^\beta}<1.
\]

Since `r=a+2b+4c`, the bound is `2^(-eta_beta r)` for some positive
constant `eta_beta`. The sum of `(72r)^t 2^(-3t^2/4)` is
`2^(O(log^2(r+2)))`, so all `t>=1` are harmless. The `t=0` term is
bounded as well. Enlarging the constant covers the finitely many small
r. This proves the fixed-partition bound

\[
C_{\alpha,\beta}\,S_r2^{\alpha r/2}
 (1+3\cdot2^\beta)^b(105\cdot2^\beta)^c.
\]

Summing over labelled partitions with the minimum number of fixed
points gives (2). Extra fixed points are handled exactly as before:
if their number is `delta+2v`, appending v pairs gives coefficient
ratio at most `s^v`, and
`S_(r-v)/S_r <= C 2^(-rv/4)`. The factor
`2^(alpha(r-v)/2)/2^(alpha r/2)` is at most one. Hence the sum over
`v>=1` is bounded and in fact exponentially small. This completes
the proof of (2).

### Coefficient comparison

For fixed positive w,v, elementary coefficient bounds give

\[
\log[z^N]\exp(z^2/2+wz^4/24+vz^8/384)
=-\frac N8\log N+
 \frac N8(1+\log v-\log48)+O_{w,v}(\sqrt N).         \tag{8}
\]

For the upper bound, evaluate the positive series at
`z=(48N/v)^(1/8)`. For the lower bound, retain the term with as many
eight-point blocks as possible and at most three pair blocks, then
use Stirling's formula. These bounds differ by `O(sqrt N)`.
Applying (8) at `v=2^beta` and `v=1` gives

\[
B_N^{(\beta)}/B_N
=2^{\beta N/8+O_\beta(\sqrt N)},
\]

which proves (3).

## 2. The finite quotient inequality

For every transitive 2-group `T<=S_8` other than the efficient
extraspecial class, and every quotient Q of T,

\[
\boxed{|Z(Q)|^2|Q'|\leq64.}                         \tag{9}
\]

The script `verify_bad_orbit_quotients.py` checks this without relying
on the transitive-group catalogue. It enumerates the 177 conjugacy
classes of subgroups of a Sylow 2-subgroup P of `S_8`, checks
transitivity on the eight labels, and then checks every normal
quotient. Every 2-subgroup of `S_8` is
conjugate into P, so this gives complete coverage.

The enumeration finds 35 transitive P-conjugacy classes: one efficient
class and 34 other classes. It checks all normal quotients of those
34 classes, including 448 having class at most two and exponent
dividing four, and (9) holds in every case. The independently generated
`degree8_groups.json` gives the same bound using the transitive-group
catalogue. Results are recorded in
`bad_orbit_quotient_verification.json`.

The excluded rank-four class is explicitly checked for `S_8`-conjugacy
to the E group built from even pair flips and regular permutations of
four pairs. Its elementary quotient of order 16 would
make (9) false, which is precisely the distinction required here.

Thus (9) is presently a finite computer-assisted lemma. Replacing this
finite check by a short structural proof would improve the presentation,
but no unchecked orbit class is omitted from the calculation.

## 3. Goursat and the epimorphism bound

Fix the exceptional eight-element set and its actual projection T.
For `H<=D_good x T`, let L be its projection to the remaining labels,
and put `K=H intersect T`. By subdirectness `K` is normal in T.
Goursat's lemma says that H is determined by K and an epimorphism

\[
L\longrightarrow T/K.
\]

The group L belongs to `J_(n-8)`, hence has class at most two and
exponent dividing four. Thus Q=`T/K` has those properties and satisfies
(9).

[Roney-Dougal–Tracey, Theorem 4.6](https://arxiv.org/html/2503.05416v1)
applied with `F=Q` and trivial auxiliary direct-product projection gives

\[
|\operatorname{Epi}(L,Q)|
\leq C_Q(1+n)^{c_Q}|Z(Q)|^{d(L)}|Q'|^{\log_2|L'|}.
                                                               \tag{10}
\]

To check its hypotheses, L lies in a product of groups of bounded order,
has class at most two, and every normal subgroup of `L'` is a vector
space of dimension at most `log_2|L'|`; it can be normally generated
by that many elements. All constants in that theorem are therefore
bounded uniformly over the finitely many Q here. The case of trivial
L or Q can be included by increasing the constants.

Put `alpha=log_2|Z(Q)|` and `beta=log_2|Q'|`. Equation (9) says
`2alpha+beta<=6`, or

\[
\alpha/2+\beta/4\leq3/2.
\]

Summing (10) over L and applying (3), with
`r=(N-8)/2=m-4`, gives an upper bound

\[
C(1+n)^c(n-8)!\,B_{N-8}S_{m-4}
                   2^{3(m-4)/2+O(\sqrt n)}.         \tag{11}
\]

There are finitely many T and normal subgroups K on a specified
eight-element set. Multiply (11) by `binom(n,8)` and absorb those
finite choices into C. Divide by
`|Q_n|~n! B_N S_m`. The coefficient injection gives
`B_(N-8)/B_N<=n^4`, and the Gaussian sum gives

\[
S_{m-4}/S_m\leq C2^{-2m+4}.
\]

The resulting exponent is
`-2m+3(m-4)/2+O(sqrt n+log n)`
`=-m/2+O(sqrt n+log n)`. This proves (1).

## 4. The initial obstruction and how far it can be removed

With a second arbitrary exceptional orbit, the projection after
deleting only one exceptional orbit need no longer have class two or
exponent four. Initially this obstructed the argument, because (9) had
only been checked for class-two exponent-four quotients. The stronger
finite check of **all** quotients removes that issue. Section 5 tracks
the necessary changing generator and derived-group weights and proves
a uniform extension to a logarithmic number of exceptional orbits.

Deleting all exceptional coordinates at once gives a class-two
efficient projection, but the common quotient is then a quotient of a
subdirect subgroup of the product of the exceptional orbit groups.
It is not necessarily a direct product of quotients of those groups.
A suitable bound for its centers, derived groups, and number of
possible kernels would extend the present method. Assuming such a
product structure would be an unjustified step.

The remaining difficulty is controlling these weights when the number
of exceptional orbits grows faster than a small multiple of `log n`.
The weighted coefficient then favors four-point dihedral blocks, whose
derived-group rank per point is twice that of the eight-point E blocks.
Treating the coefficient error as uniform in the weights would be
incorrect. Neither (1) nor Section 5 is the complete bounded-eight
theorem.

## 5. Uniformly excluding a logarithmic number of exceptional orbits

Let `X_(n,b)` require exactly b eight-point orbits with arbitrary
non-E transitive 2-group projections, with all other nontrivial orbit
projections efficient. For an absolute C and all sufficiently large n,

\[
\boxed{
\frac{|X_{n,b}|}{|Q_n|}
\leq2^{-bn/4+C(n^{5/8}+(\log_2 n)^2)},
\qquad 1\leq b\leq\lfloor(\log_2 n)/16\rfloor.
}                                                     \tag{12}
\]

In particular their union is exponentially negligible relative to
`Q_n`. For any fixed b, the sharper bound is

\[
|X_{n,b}|/|Q_n|
\leq2^{-bn/4+O_b(\sqrt n+\log n)}.                   \tag{13}
\]

### Tracking the epimorphisms

Fix an ordered list of the b exceptional blocks and their projections
`T_1,...,T_b`, and let `L_0` be the projection onto all remaining
labels. Write `L_i` for the projection after the first i exceptional
blocks are restored. Goursat gives a chain of epimorphisms

\[
L_{i-1}\longrightarrow Q_i=T_i/K_i,
\qquad K_i\triangleleft T_i.
\]

The choices of the `K_i` and actual `T_i` contribute at most a constant
to the power b for fixed ordered blocks.

Each factor lies in `S_8` and has order at most 128, derived subgroup
of order at most 16, and nilpotency class at most four. These bounds
follow from containment in a Sylow 2-subgroup of `S_8` (and are also
checked by the finite enumeration). The kernel of `L_i -> L_0` has
order at most `2^(7i)`. Also `L_i'` embeds in
`L_0' x T_1' x ... x T_i'`. Consequently

\[
d(L_i)\leq d(L_0)+7i,\qquad
\log_2|L_i'|\leq\log_2|L_0'|+4i.                   \tag{14}
\]

The general form of Roney-Dougal–Tracey Theorem 4.6 still applies with
`F=Q_i` and trivial auxiliary projection. The class of `L_i` is at
most four, so its constants are uniform. A normal subgroup of `L_i'`
can be normally generated by at most `log_2|L_i'|` elements, regardless
of its nilpotency class. Put

\[
\alpha_i=\log_2|Z(Q_i)|,\qquad
\beta_i=\log_2|Q_i'|,\qquad
\alpha=\sum_i\alpha_i,\quad\beta=\sum_i\beta_i.
\]

The finite inequality (9) and the size of a Sylow derived subgroup give

\[
2\alpha+\beta\leq6b,\quad
0\leq\alpha\leq3b,\quad0\leq\beta\leq4b.            \tag{15}
\]

Multiplication of the b epimorphism bounds, using (14), shows that for
each `L_0` the number of chains is at most

\[
2^{O(b^2+b\log n)}
 2^{\alpha d(L_0)+\beta\log_2|L_0'|}.               \tag{16}
\]

This argument does not assume the intermediate groups are class two.

### A uniform version of the weighted moment estimate

The proof of (2) can be tracked uniformly when
`alpha=O(log r)` and `0<=beta<=(1/2)log_2(r+2)`. Its only significant
extra factor is the explicit `2^(alpha^2/4)` in (6). Indeed, the
averaged `t>=1` terms are at most

\[
2^{O(\log^2(r+2))-c r2^{-\beta}},                    \tag{17}
\]

with absolute c, because `1-theta_beta` is bounded below by a
positive constant times `2^(-beta)`. Under the displayed parameter
range, (17) tends uniformly to zero. The u sum and the shifted
Gaussian sum have absolute bounds. Thus, for these parameters,

\[
M_{\alpha,\beta}(s)
\leq C s!S_r2^{\alpha r/2+\alpha^2/4}B_N^{(\beta)}.
                                                               \tag{18}
\]

Extra fixed points do not introduce a hidden lack of uniformity. If
they remove at most half of r, the same argument has
`r2^(-beta) >= c sqrt(r)`. If they remove more than half, the Gaussian
sum ratio loses `2^(c r^2)`, whereas the coefficient injection and the
crude weight bound together cost only `2^(O(r log r))` in this
parameter range.

The positive-series evaluation used in (8), now without hiding the
weight dependence, gives

\[
\frac{B_N^{(\beta)}}{B_N}
\leq 2^{\beta N/8+
 C(\sqrt N\,2^{\beta/2}+\log(N+2))}.                 \tag{19}
\]

The constant C is absolute for `beta>=0`. For clarity, at
`z=(48N/2^beta)^(1/8)` the fourth-degree term in the exponent is at
most `C sqrt(N) 2^(beta/2)`, the second-degree term is at most
`C N^(1/4)`, and the eighth-degree term is `N/8`. The denominator has
the lower bound from the single near-all-eight-block coefficient
term. This proves (19).

### Completing the comparison

Here `L_0` acts on `n-8b` labels, with binary rank parameter
`r=m-4b`. For `b<=floor(log_2(n)/16)`, (15) gives
`2^(beta/2)<=n^(1/8)`. Equations (18)–(19), followed by (15), therefore
bound the weighted sum in (16) by

\[
(n-8b)!B_{N-8b}S_{m-4b}
2^{(3/2)b(m-4b)+O(n^{5/8}+b^2)}.
\]

Choosing the ordered exceptional blocks costs
`n!/((n-8b)!(8!)^b)`. This overcounts their possible orders and is
sufficient for an upper bound. Divide by `|Q_n|~n!B_NS_m`, use

\[
B_{N-8b}/B_N\leq n^{4b},\qquad
S_{m-4b}/S_m\leq C2^{-2bm+4b^2},
\]

and include (16). The total exponent is at most

\[
-\frac{bm}{2}+O(n^{5/8}+b^2+b\log n),
\]

which is (12), since `m=(n-delta)/2`. Keeping b fixed in these same
estimates gives (13).

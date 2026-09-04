# Removing the saturation hypothesis for the efficient 2/4/8 projections

Independent extension, 4 September 2026.

Let `E` be the transitive plus-type extraspecial group of order 32 on
eight points constructed in `progress_v3.md`. Its center and derived
group coincide and have order two; `E/E'` has binary rank four. On a
specified eight-point block its conjugacy class has 105 members, as
proved in that note.

Define `J_n` to be all actual 2-subgroups of `S_n` with the following
orbit projections: `C_2` on each pair; regular `V_4` or `D_8` on each
four-point orbit; and one of these groups `E` on each eight-point orbit.
Any number of fixed points is allowed. **No condition is imposed on
containment of the supported derived subgroups.**

Let `Q_n` be the saturated family from `progress_v3.md`, with exactly
`delta=n mod 2` fixed points and with every supported orbit derived
subgroup contained in `H`. Then there is an absolute constant `eta>0`
such that

\[
 |J_n\setminus Q_n|/|Q_n|=O(2^{-\eta n}).              \tag{1}
\]

Thus all enumeration and order limit theorems already proved for
`Q_n` hold for uniform sampling from the entire class `J_n`. In
particular its logarithmic order has leading term `3n/8`, with the
centering and `n^(1/4)` fluctuation law given in the third research note.
This theorem does not include other possible transitive projections
on eight points or any larger orbits.

## 1. The representation bound for restricted square forms

For `D_8`, the square form on its binary quotient is `xy`. If a subgroup
projects onto `D_8`, the restricted coordinate linear forms `X,Y` are
independent. For a given resulting nonzero quadratic form, there are
exactly two ordered representations `XY` by independent linear forms.

For `E`, its square form is the nonsingular plus form

\[
 q_+(x_1,y_1,x_2,y_2)=x_1y_1+x_2y_2.                 \tag{2}
\]

This follows either from the central product of two `D_8` factors, or
by finding a hyperbolic basis for the explicit square map of the
eight-point construction. Surjectivity onto its quotient makes the
four restricted coordinate linear forms independent.

A given quadratic form on a binary `k`-space has at most **72** ordered
representations as (2) in four independent linear forms. To see this,
let `L` be the surjective map to `F_2^4` given by such forms. The kernel
of the polar form of the pullback quadratic is exactly `ker L`, since
the polar form of `q_+` is nondegenerate. Thus two representations have
the same kernel and differ by an isometry of `q_+`.

There are exactly 72 such isometries. Count ordered hyperbolic bases:
there are nine nonzero singular choices for the first vector, four
singular partners pairing to one with it, and two choices of ordered
hyperbolic basis for their two-dimensional orthogonal complement. The
product is `9*4*2=72`. The singular-vector count follows directly from
`q_+=x_1y_1+x_2y_2`: there are ten zeroes, including zero. For a fixed
nonzero singular vector, its eight vectors pairing to one are paired
by translation by that vector, and exactly one vector in each pair
is singular. The orthogonal complement of a hyperbolic plane in the
plus space is a hyperbolic plane.

Only the upper bound 72 is needed below.

## 2. Count nonsaturated subdirect subgroups

Fix a partition with `a` pair blocks, `b` four-point blocks, and `c`
eight-point blocks, and suppose exactly `d` four-point projections are
dihedral. Put

\[
 r=a+2b+4c,\qquad z=d+c.
\]

The ambient product `D` has elementary abelian derived group `Z=D'` of
rank z, and `D/Z` is binary of rank r. The square map is the vector of
`d` rank-two quadratics and `c` rank-four plus quadratics described
above. For a subdirect subgroup, let `U=HZ/Z`, `dim U=k`, and
`W=H intersect Z`, `codim_Z W=t`.

Exactly as in §1 of `extension_small_orbits.md`, for fixed `(U,W)` the
number of subgroups is `2^(kt)` if `q(U) subset W`, and zero otherwise.
That parametrization applies because the ambient product has exponent
four, nilpotency class at most two, and central derived group of
exponent two.

Suppose the `z` coordinate square forms restricted to an ordered basis
of U span a space of dimension `z-h`. Choose a basis subset among
the z positions. Each dependent coordinate quadratic has at most
`2^(z-h)` choices, and at most 72 coordinate representations. Its
unrestricted coordinate count would have been either `2^(2k)` or
`2^(4k)`. Replacing the latter saving by the smaller `2^(2k)` only
weakens the upper bound. Therefore the count of all full-rank coordinate
matrices with deficiency h is at most

\[
 2^{kr}\binom zh72^h2^{-h(2k-z+h)}.                  \tag{3}
\]

Dropping full-rank and other projection conditions in obtaining this
bound is harmless; independence of each dihedral or extraspecial
coordinate tuple is retained so that the representation bounds apply.

There are `[h choose t]_2` possible codimension-t spaces W containing
the span of the square values. Divide (3) by `|GL(k,2)|`, multiply by
`2^(kt)`, and use the Gaussian bound. Put `h=t+u` and `j=k-r/2`. The
exponent of two apart from `binom(z,h)72^h` is exactly

\[
 \frac{r^2}{4}-(j+t/2+u)^2-\frac{3t^2}{4}
             -t(r/2-z)-u(r-z).                       \tag{4}
\]

Here `z<=r/2`. Consequently summing over k and u gives the bound

\[
 C S_r\sum_{t\geq1}(72z)^t
          2^{-3t^2/4-t(r/2-z)}                       \tag{5}
\]

for nonsaturated subgroups of one ambient product. Indeed the k-sum
of the first negative square is bounded, and the u-sum is geometric
with ratio at most `72z 2^(-(r-z))`, which tends uniformly to zero.
Finitely many small r can be handled by enlarging the constants.

## 3. Average over the four-point choices

The number of ambient projection choices for the fixed partition is
`4^b 105^c`. Sum (5) with weights `binom(b,d)3^d 105^c` and divide by
`4^b 105^c S_r`. Bounding `72z` by `72r`, the relative nonsaturated
count is at most

\[
 C\sum_{t\geq1}(72r)^t2^{-3t^2/4}
       2^{-t(a/2+c)}
       \left(\frac{3+2^{-t}}4\right)^b.              \tag{6}
\]

For `t>=1`, the last factors are at most `2^(-a/2-c)(7/8)^b`.
Writing `beta=log_2(8/7)`,

\[
 a/2+c+\beta b\geq (\beta/2)(a+2b+4c)
                       =\beta r/2.
\]

The sum of the remaining factors is `2^(O(log^2(r+2)))`. Thus (6)
is `O(2^(-eta_1 r))` uniformly over all orbit profiles. As usual, the
subspaces failing to be onto one of the quotient factors contribute
only `O(r2^(-r/4))` of `S_r` by the hyperplane union bound. Therefore,
for this partition, **all** subdirect subgroups have count

\[
 4^b105^c S_r(1+O(2^{-\eta_2r})),                     \tag{7}
\]

and the error relative to the saturated subdirect count is exponentially
small. This proves the required uniform assertion before adding fixed
points.

## 4. Extra fixed points

With `N=n-delta` and `m=N/2`, use the coefficient

\[
 B_L=[z^L]\exp(z^2/2+z^4/6+z^8/384).
\]

If there are `delta+2s` fixed points, summing (7) over partitions gives
the upper bound

\[
 C\frac{n!}{(\delta+2s)!}B_{N-2s}S_{m-s}.
\]

Appending s pair blocks proves `B_(N-2s)/B_N<=n^s`; the Gaussian
subspace estimate gives `S_(m-s)/S_m<=C2^(-ms/4)`. Thus all `s>=1`
contribute at most `C sum_(s>=1)(n2^(-m/4))^s` relative to the
`s=0` saturated main term. This is exponentially small. Combining it
with (6) proves (1).

## Consequence for the research claim

The order law in the third research note now holds for every subgroup
with the specified full orbit projections, apart from an exponentially
small exceptional proportion. Saturation is a proved typical property
within this class, not a hypothesis of its uniform sampling model.
Other transitive eight-point projection types remain outside the claim.

The argument is self-contained given the explicit structure of E in
the third note. Independent proof auditing is recorded separately in
`audit_small_orbits.md` and its follow-up.

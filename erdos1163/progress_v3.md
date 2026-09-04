# Erdős 1163: eight-point factors and a stronger unrestricted bound

Third research pass, 4 September 2026.

**Status: proved partial results, with independent proof audits and finite
checks recorded separately. This is not a solution of the unrestricted
order-distribution problem. Novelty has not been established.**

The key additional factor is the extraspecial group of order 32 acting
transitively on eight points. Its elementary abelian quotient has rank
four. It therefore has the same quotient rank per point as the earlier
two- and four-point factors, while its larger orbits allow many more
labelled partitions. This factor and its extremal quotient property are
classical: see Kovács and Praeger, *Finite permutation groups with large
abelian quotients*, Pacific J. Math. 136 (1989), 283–292,
[publisher PDF](https://msp.org/pjm/1989/136-2/pjm-v136-n2-p05-s.pdf).

The resulting conclusions are:

$$
\log_2|\operatorname{Sub}(S_n)|
\geq n^2/16+(7/8)n\log_2n-O(n),                         \tag{0.1}
$$

$$
\Pr_{H\in\operatorname{Sub}(S_n)}(H\text{ abelian})
\leq 2^{-(n/8)\log_2n+O(n)}.                           \tag{0.2}
$$

Both apply to actual labelled subgroups, with uniform sampling in (0.2).
In addition, a precisely defined family has a central limit theorem for
its order, with leading term `log_2|H| ~ 3n/8` and fluctuations of size
`n^(1/4)`. This family theorem does **not** give the unrestricted order
law. The earlier four-point family's leading order `7n/16` is different,
and that earlier family is negligible relative to the new one.

## 1. The eight-point group and its 105 embeddings

Write the eight points as pairs `(i,e)`, where `i` runs through
`F_2^2` and `e` through `F_2`. Let `B=F_2^4` act by independently
flipping the four pairs. Let `V=F_2^2` act regularly by translation on
their four indices. Define

$$
B_0=\{b\in B:\textstyle\sum_i b_i=0\},\qquad
E=B_0\rtimes V.
$$

This group has order `8*4=32` and is transitive: V moves between the
pairs, and a flip in any chosen pair can be accompanied by a flip in
another pair to give an element of `B_0`.

Put `z=(1,1,1,1)` in B. Each nonidentity translation v exchanges two
disjoint pairs of indices. If b has even weight, the vector `b+v(b)`
has a common value on each exchanged pair, and those two values are
equal. Thus `b+v(b)` belongs to `<z>`, with equality to z possible.
Consequently

$$
E'=\langle z\rangle,\qquad E/E'\cong C_2^4.             \tag{1.1}
$$

Indeed `(b,v)^2=(b+v(b),0)` also lies in `<z>`. The center is exactly
`<z>`: an element centralizing all of `B_0` has trivial translation
part, and the V-invariant vectors of `B_0` are the constant vectors.
The subgroup B0 is elementary abelian of order eight, which specifies
the plus type of this extraspecial group. It is also realizable
as the central product of two dihedral groups of order eight. The
construction and (1.1), rather than that identification, suffice below.

The normalizer calculation is elementary. Since E has unique nontrivial
central element z, its normalizer in `S_8` lies in

$$
W=C_{S_8}(z)=C_2^4\rtimes S_4,
\qquad |W|=16\cdot24=384.
$$

Conversely E is normal in W. The even-weight subspace is invariant under
all coordinate permutations; the regular Klein-four group V is normal
in `S_4`; and conjugation of a translation v by any vector b in B adds
the even-weight vector `b+v(b)`. Thus

$$
N_{S_8}(E)=W,\qquad |E^{S_8}|=8!/384=105.              \tag{1.2}
$$

There is exactly one such conjugate for each perfect matching of the
eight points: its unique central involution determines that matching,
and its full matching stabilizer normalizes the group. This argument
does not depend on a computer classification.

## 2. A family with two-, four-, and eight-point orbits

Put `delta=n mod 2`, `N=n-delta`, and `m=N/2`. Define `Q_n` to consist
of the following actual permutation subgroups. Choose an orbit
partition with delta singleton blocks, a two-point blocks, b four-point
blocks, and c eight-point blocks, where

$$
a+2b+4c=m.
$$

On a two-point block use `C_2`. On a four-point block use either the
unique regular `V_4` or one of the three embedded `D_8` groups. On an
eight-point block use one of the 105 groups from §1. Let D be the product
of these orbit groups, and let

$$
\pi:D\longrightarrow D/D'
 \cong\mathbb F_2^a\times(\mathbb F_2^2)^b
                         \times(\mathbb F_2^4)^c.
$$

For each subspace U surjecting onto every displayed factor, include
`H=pi^(-1)(U)` in `Q_n`. Surjectivity and containment of D' guarantee
that H has the prescribed full projection on each orbit. The subgroup
therefore recovers its partition, orbit groups, D, and U. No subgroup
is counted twice.

If U has dimension k and exactly d four-point factors are dihedral,
then

$$
|H|=2^{k+d+c}.                                        \tag{2.1}
$$

All these groups have nilpotency class at most two and exponent dividing
four. Thus the lower bound (0.1) already holds for that class of groups.

Let `s_(a,b,c;k)` count the allowed k-subspaces. Möbius inversion in
each coordinate subspace lattice gives

$$
s_{a,b,c;k}=\sum_t q_t{m-t\brack k}_2,
$$

$$
\sum_tq_tx^t=(1-x)^a(1-3x+2x^2)^b
                 (1-15x+70x^2-120x^3+64x^4)^c.        \tag{2.2}
$$

The last factor is `product_(j=0)^3(1-2^j x)`. This is the same
Gaussian subspace mechanism used in the earlier notes; no additional
claim from the user's Witt-filtration draft is assumed.

The exact order polynomial is

$$
\boxed{
\sum_{H\in Q_n}y^{\log_2|H|}
=\sum_{a+2b+4c=m}
\frac{n!\,105^c}{\delta!\,2^aa!\,24^bb!\,(8!)^cc!}
y^c(1+3y)^b\sum_ks_{a,b,c;k}y^k.
}                                                     \tag{2.3}
$$

## 3. Relative enumeration and the lower bound

Write `S_m=sum_k {m choose k}_2`, and define

$$
B_N=[z^N]\exp(z^2/2+z^4/6+z^8/384).
$$

Uniformly over all profiles in §2,

$$
\sum_ks_{a,b,c;k}=S_m(1+O(n2^{-m/4})).                 \tag{3.1}
$$

To see this, a k-subspace failing to surject onto a fixed rank-e factor
lies in the inverse image of some hyperplane of that factor. There are
`2^e-1` such hyperplanes. Its probability of lying in a fixed ambient
hyperplane is

$$
\frac{{m-1\brack k}_2}{{m\brack k}_2}
=\frac{2^{m-k}-1}{2^m-1}\leq 2^{1-k}.
$$

The union bound is at most `(a+3b+15c)2^(1-k)`. The Gaussian coefficient
bounds from the first note imply that a uniform subspace has dimension
less than `m/4` with probability `O(2^(-m^2/16))`. This proves (3.1).
In particular

$$
\boxed{|Q_n|=\frac{n!}{\delta!}B_NS_m
                     (1+O(n2^{-m/4})).}              \tag{3.2}
$$

There is also a useful probabilistic formulation. Select an ambient D
with weight one for every actual choice, and independently select a
uniform subspace of `F_2^m`; then condition on all coordinate projections
being onto. Before conditioning the profile weight is

$$
\frac{1}{2^aa!\,6^bb!\,384^cc!},                     \tag{3.3}
$$

and d given b is `Binomial(b,3/4)`. Conditioning changes the entire
joint distribution by total variation `O(n2^(-m/4))`. The rank satisfies
`K-m/2=O_P(1)` and has the discrete Gaussian limit proved in the first
note.

For a coefficient equivalent, let rho be the positive solution of

$$
\rho/2+\rho^2/3+\rho^4/96=m,                         \tag{3.4}
$$

and put

$$
V=\rho/2+2\rho^2/3+\rho^4/24.
$$

Then

$$
\boxed{
B_N\sim
\frac{\exp(\rho/2+\rho^2/6+\rho^4/384)}
     {\rho^m\sqrt{2\pi V}}.
}                                                     \tag{3.5}
$$

Here is a proof retaining the lattice factor. For independent Poisson
variables A, B, C with means `rho/2`, `rho^2/6`, `rho^4/384`, let
`T=A+2B+4C`. Its mean is m and its variance is V. The coefficient is
exactly the numerator in (3.5), divided by `rho^m`, times `Pr(T=m)`.
At zero its centered characteristic function has logarithm
`-V theta^2/2+O(m|theta|^3)`. Integrating over
`|theta|<=m^(-2/5)` yields `(2pi V)^(-1/2)(1+o(1))`.
Away from neighborhoods of the fourth roots of unity, the C factor
has modulus at most `exp(-c m^(1/5))`. The potential peaks at
`theta=+/-pi/2` are suppressed by the B factor, whose mean is of order
`sqrt(m)`; the peak at pi is suppressed by the A factor, whose mean is
of order `m^(1/4)`. This proves the required local limit estimate and
(3.5).

Since `rho=(48N)^(1/4)(1+O(N^(-1/2)))`, (3.5) gives

$$
\log B_N=-\frac N8\log N
          +\frac N8(1-\log48)+O(\sqrt N).             \tag{3.6}
$$

Unmarked logarithms are natural; `log_2` is displayed explicitly.
Combining
Stirling's formula, (3.2), and `log_2 S_m=m^2/4+O(1)`, we obtain

$$
\log_2|Q_n|
=\frac{N^2}{16}+n\log_2 n-\frac N8\log_2 N
 -n\log_2e+\frac N8\log_2(e/48)+O(\sqrt n).           \tag{3.7}
$$

In particular (0.1) follows for all n. This sharpens the explicit
`n log n` coefficient of the construction in the first note. It is
not an asymptotic equality for the total number of subgroups.

The all-abelian theorem in
[progress_v2.md](progress_v2.md)
gives `|Ab_n|~(n!/delta!) A_N(1)S_m`. Consequently

$$
\log\frac{|\mathrm{Ab}_n|}{|Q_n|}
=-\frac N8\log N+\frac N8\log(4e/3)+O(\sqrt N).        \tag{3.8}
$$

Dividing by the larger set of all subgroups proves (0.2), with the
more precise linear term supplied by (3.8). Replacing `A_N(1)` by
`A_N(4)` shows also

$$
\frac{|F_n|}{|Q_n|}=2^{-(n/8)\log_2n+O(n)}\to0.        \tag{3.9}
$$

Thus the old family is negligible for both parities, not only in the
odd-degree situation of the second note.

## 4. Order central limit theorem in the new family

For rho from (3.4), set

$$
\mu_N=\frac{3N}{8}+\frac{\rho^2}{24}-\frac\rho8,
\qquad \sigma_N=\frac\rho{\sqrt{24}}.
$$

For uniform `H in Q_n`,

$$
\boxed{\frac{\log_2|H|-\mu_N}{\sigma_N}
                         \ \Longrightarrow\ N(0,1).} \tag{4.1}
$$

In particular

$$
\mu_N=\frac{3N}{8}+\sqrt{N/12}
                 -\frac{(48N)^{1/4}}8+O(1),
\qquad \sigma_N\sim(N/12)^{1/4}.                     \tag{4.2}
$$

This is an order law for `Q_n`, not for all subgroups or all 2-subgroups.

Proof. Split the four-point count into B0 Klein-four blocks and B1
dihedral blocks. By (3.3), their joint law with A and C is exactly that
of independent Poisson variables with means

$$
\lambda_A=\rho/2,\quad
\lambda_0=\rho^2/24,\quad
\lambda_1=\rho^2/8,\quad
\lambda_C=\rho^4/384,
$$

conditioned on `A+2(B0+B1)+4C=m`. The exponentially small change in
(3.3) can be ignored for convergence in law.

We need two consequences of this conditioning:

1. The conditional law of `(B0,B1)` has total variation tending to zero
   from the independent Poisson law with means `(lambda_0,lambda_1)`.
2. Conditionally, `A-lambda_A=O_P(sqrt(rho))`.

Here are details. On sets where each variable A, B0, B1 lies within
`rho^(1/8)` times its own standard deviation from its mean, the required
value of C differs from `lambda_C` by `O(rho^(9/8))=o(rho^2)`.
Stirling's formula therefore gives, uniformly on those sets and when
the congruence permits C,

$$
\Pr(C=(m-A-2B0-2B1)/4)
            =(2\pi\lambda_C)^{-1/2}(1+o(1)).
$$

The congruence is `A+2(B0+B1)=m mod 4`. The Poisson A has residue
probabilities `1/4+O(exp(-c rho))` by the roots-of-unity filter. For
fixed B0 and B1 in the indicated sets, summing over A therefore
multiplies the displayed local probability by `1/4+o(1)`.
The normalization is `Pr(T=m)~(2pi V)^(-1/2)`, and
`V~16lambda_C`. Their ratio tends to one. To control the discarded
sets, use the uniform bound
`sup_j Pr(C=j)=O(lambda_C^(-1/2))`; divided by `Pr(T=m)`, this is
bounded. Poisson tail bounds then apply uniformly. This proves the
first claim. The same bounded ratio applied to events involving A
proves the second claim, including tightness on its natural standard
deviation scale.

Now use `A+2(B0+B1)+4C=m` to rewrite (2.1) as

$$
L:=\log_2|H|
=\frac{3N}{8}+(K-m/2)+\frac{B1-B0}{2}-\frac A4.        \tag{4.3}
$$

The first two claims, together with the independent Poisson central
limit theorem, give

$$
\frac{(B1-B0)/2-\rho^2/24}{\rho/\sqrt{24}}
                       \Longrightarrow N(0,1).
$$

The terms `K-m/2=O_P(1)` and `A-lambda_A=O_P(sqrt(rho))` vanish on
this scale. Equation (4.3) proves (4.1). Finally, (3.4) gives
`rho^2=sqrt(48N)-16+O(N^(-1/4))`, which proves (4.2). QED.

## 5. Odd-degree extension

For odd n, replace the one singleton by a three-point `S_3` orbit,
reduce the remaining even support from N to `N-2`, and take the same
full preimages in the abelianization of the product. Call this family
`R_n`. The total binary quotient rank is still m: the new orbit adds
one binary coordinate. These groups have odd part exactly three and
are nonnilpotent because they have an `S_3` quotient.

The same uniformly valid surjectivity estimate gives

$$
|R_n|=\frac{n!}{6}B_{N-2}S_m(1+O(n2^{-m/4})).          \tag{5.1}
$$

The coefficient ratio is

$$
\frac{B_{N-2}}{B_N}\sim\rho.
$$

For example, marking a two-point block gives the ratio as `2E[A]`;
the conditional estimates in §4 give `E[A]~rho/2`. Uniform
integrability follows from the same bounded density estimate and
the second moment of the Poisson variable. Thus

$$
\boxed{\frac{|R_n|}{|Q_n|}\sim\frac{(48N)^{1/4}}6.}    \tag{5.2}
$$

In particular, `Q_n` itself cannot contain almost all unrestricted
subgroups along the odd degrees. Uniform members of `Q_n union R_n`
have odd part three with probability tending to one. The order CLT
(4.1) also holds for that union: for `R_n` use the conditional even
support `N-2`, the rank center remains `m/2`, and the additional
changes in centering, including `log_2 3`, are O(1).

## 6. Relation to existing work and the remaining problem

Roney-Dougal and Tracey, *Subgroups of symmetric groups: enumeration and
asymptotic properties*,
[arXiv:2503.05416](https://arxiv.org/abs/2503.05416), prove
`|Sub(S_n)|=2^(n^2/16+O(n^(3/2)))`. Their Proposition 7.3 constructs
many subgroups from disjoint p-cycles and supplies a positive
`n log n` lower-order term. The explicit `7/8` construction here uses
the classical eight-point factor instead. Neither comparison by
itself establishes that our lower bound or order-refined count is new.

Kovács–Praeger's equality classification explains the list of efficient
transitive binary-quotient factors. It does not imply that most
subgroups are full preimages from those factors. In particular, it
does not solve the problem of counting arbitrary subdirect products.

The next missing comparison concerns subgroups that omit some supported
commutator groups and those with larger orbits. The new construction
shows that this comparison must allow eight-point extraspecial orbits.
An order theorem for all of `Sub(S_n)` still requires such estimates.

## 7. The saturation assumption is now removed for these projections

Subsequent work in
[extension_efficient_orbits.md](extension_efficient_orbits.md)
proves the following strengthening. Let `J_n` contain all 2-subgroups
with orbit projections `C_2`, `V_4`, `D_8`, or the specified E on the
corresponding two-, four-, or eight-point orbits. Allow arbitrary fixed
points and impose no supported-commutator containment condition. Then

$$
|J_n\setminus Q_n|/|Q_n|=O(2^{-\eta n})
$$

for an absolute `eta>0`. Hence (3.2), (3.7), and the order CLT (4.1)
hold with `J_n` in place of `Q_n`. The proof counts dependencies among
the restricted square forms; each rank-four plus form has 72 possible
coordinate representations. It has passed an independent audit in
[audit_efficient_orbits.md](audit_efficient_orbits.md).

This resolves the omitted-commutator comparison for the displayed
projections. Other transitive eight-point groups and larger orbits
remain outside the theorem.

## 8. Verification record

The independent proof audits in [audit_extraspecial.md](audit_extraspecial.md) and
[audit_extraspecial_clt.md](audit_extraspecial_clt.md) check the group, normalizer, exact count,
coefficient constants, conditional Poisson argument, and odd extension.
[verify_extraspecial.py](verify_extraspecial.py) additionally performs the following finite
checks, recorded in [extraspecial_verification.json](extraspecial_verification.json):

- Constructs E as actual permutations, checks its order, derived group,
  center, and squares, and computes its normalizer by testing all of S8.
- Checks the rank-four Möbius formula against every binary subspace in
  ambient dimensions four through six for the relevant profiles.
- Checks that `Q_8` adds exactly 105 groups of order 32 to `F_8`, and
  computes exact order histograms through n=64.
- Evaluates the coefficient sum and profile moments through N=4096.
  At N=4096 the coefficient divided by (3.5) is 0.999840, the mean
  error divided by the CLT scale is 0.000916, and the variance divided
  by the proposed squared scale is 1.02880. These profile moments omit
  the independent O(1) rank fluctuation, which is asymptotically
  negligible on the stated scale.

The computations test indexing and finite behavior. The asymptotic
claims rest on the proofs, not on numerical extrapolation.

The original drafts remain unchanged. All new research, audits, and
computational checks are kept in this directory. No submission or
communication to third parties has been made.

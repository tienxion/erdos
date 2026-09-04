# All class-two exponent-four 2-subgroups with orbits of size at most eight

Research extension, 4 September 2026.

This note removes the remaining projection restrictions within the
class of 2-subgroups of nilpotency class at most two and exponent
dividing four, with orbit sizes at most eight. Its counting argument
extends the quadratic-dependency method of `extension_small_orbits.md`.
The finite local classification used in §1 is recorded explicitly;
it must be included as a checked input to the theorem.

## Theorem

Let `C_n` be all actual 2-subgroups of `S_n` with nilpotency class at
most two, exponent dividing four, and orbits of size at most eight.
Let `Q_n` be the saturated extraspecial family in `progress_v3.md`.
There is an absolute constant `eta>0` such that

\[
 |C_n\setminus Q_n|/|Q_n|=O(2^{-\eta n}).              \tag{1}
\]

Consequently the relative enumeration formula and order central limit
theorem proved for `Q_n` hold for **all** of `C_n`. In particular the
leading logarithmic order is `3n/8`, with fluctuations of order
`n^(1/4)` and the precise centering and limiting variance in the third
research note. No saturation condition or restricted list of orbit
projections is imposed in the definition of `C_n`.

The theorem does not include higher-class or exponent-eight groups,
even if their orbits all have size eight.

## 1. The finite local input and its models

A transitive projection of a group satisfying the two group identities
again has class at most two and exponent dividing four. Conversely,
a subgroup of a product of such projections satisfies both identities.
On two or four points the possibilities were listed in the preceding
notes. On eight points the possibilities, up to permutation conjugacy,
are the following nine entries of the degree-eight transitive group
classification:

| GAP transitive ID | Abstract description | Order | Binary generator rank | Frattini order |
|---|---|---:|---:|---:|
| 2 | `C_4 x C_2` | 8 | 2 | 2 |
| 3 | `C_2^3` | 8 | 3 | 1 |
| 4 | regular `D_8` | 8 | 2 | 2 |
| 5 | regular `Q_8` | 8 | 2 | 2 |
| 9 | `D_8 x C_2` | 16 | 3 | 2 |
| 10 | the group with square map `(Y^2,XY)` | 16 | 2 | 4 |
| 11 | `D_8` central product `C_4` | 16 | 3 | 2 |
| 18 | `V_4` wreath `C_2` | 32 | 3 | 4 |
| 22 | plus extraspecial `E` | 32 | 4 | 2 |

There are two reproducible finite checks. `classify_degree8.py`, with
results in `degree8_groups.json`, examines the degree-eight transitive
group library. Independently, `verify_degree8_classification.py` uses
only literal permutations and Python's standard library: it enumerates
all 544 class-two exponent-four subgroups of an explicit Sylow group
of order 128, finds 53 transitive ones, and supplies explicit
`S_8` conjugators matching them to exactly the nine models above.
The resulting certificate is `degree8_classification_certificate.json`.
Its exhaustive-algorithm proof is explained in
`degree8_classification_certificate.md`.
Every 2-subgroup of `S_8` is conjugate into that Sylow group, so this
second check certifies completeness without trusting the transitive
group library. The argument below depends only on this finite list
and the explicit models, not on any asymptotic estimates from a
computation.

For a group with Frattini subgroup of order two, that subgroup is
central; all squares and commutators belong to it. Its square map
on its binary Frattini quotient is scalar. In the nonabelian cases
its alternating polar form has rank two, except that E has rank four.
Extra radical coordinates, including a possible square term on the
radical, will be left unrestricted in our upper bound. In the abelian
case `C_4 x C_2`, the only nonzero square coordinate is a square of
one quotient linear form.

These rank facts also have a useful classification-free check. If
`|Phi(G)|=2`, write `g=dim G/Phi(G)` and let the polar rank be `2s`.
For a core-free point stabilizer P, `P intersect Z(G)=1`. Moreover P
is elementary abelian and its image in `G/Z(G)` is totally isotropic,
so `|P|<=2^s`. A faithful transitive action on eight points gives
`2^(g+1-s)<=8`, hence `g<=4`. Equality forces the nonsingular plus
quadratic form in dimension four: its stabilizer image is a totally
singular plane. Thus every non-E scalar-Frattini case has generator
rank at most three. An abelian transitive projection is regular.

The two nonscalar cases have particularly simple models.

**ID 18.** Write `G=V_4 wreath C_2=(C_2^2 x C_2^2) semidirect C_2`,
with the involution interchanging the two direct factors. Its Frattini
subgroup is central of rank two, and its binary quotient has rank
three. Suitable coordinates give its vector square map as

\[
 (XY,XZ),\qquad X,Y,Z\text{ independent}.             \tag{2}
\]

For example, take an interchange generator x and two commuting base
generators y,z. Their squares are trivial and their independent
commutators with x form a basis of the Frattini subgroup.

**ID 10.** Let u generate `C_4`, and let s,t be involutions generating
`D_8`. In `C_4 x D_8`, the subgroup generated by `(1,s)` and `(u,t)`
has order sixteen. Its square and commutator coordinates are
`(Y^2,XY)`, respectively. It is the index-two fiber product imposing
equality of the C4 quotient coordinate and the t-coordinate in
`D_8/D_8'`.

For an upper bound, replace this orbit projection by the **virtual
ambient product** `C_4 x D_8`. Every subgroup surjecting onto the
original ID10 group maps injectively into this product and surjects
onto each of its two factors. We discard the fiber-product equality.
The two central Frattini coordinates remain independent, whereas the
binary quotient rank increases from two to three. Its eight-point
budget is exactly the sum of the two virtual four-point budgets.
Thus the enlarged ambient still has a rank deficit of one, including
one cyclic square coordinate. This replacement is made for a fixed
orbit-projection choice, so there is no issue of counting an original
group more than once in the resulting upper bound.

This virtual enlargement avoids a circular counting argument involving
the two coordinate forms `Y^2` and `XY`; no independence of their
restricted values is assumed.

## 2. Defect bookkeeping for a fixed partition

Fix a partition into a pair blocks, ell four-point blocks, and e
eight-point blocks; put

\[
 M=a+2\ell+4e.
\]

Thus `2M` is its number of nonfixed points. Choose all orbit projections
from §1 and perform the virtual replacements for ID10.

Let b be the number of ID18 blocks. Let D be the total binary-rank
deficit of all other defective blocks after those replacements. The
defective scalar types contribute:

- a cyclic four-point orbit: deficit one;
- regular `C_4 x C_2`, `D_8`, or `Q_8` on eight points: deficit two;
- regular `C_2^3`, `D_8 x C_2`, or ID11 on eight points: deficit one;
- a virtual ID10 replacement: deficit one.

All efficient factors have zero deficit. The ambient binary rank is

\[
 r=M-D-b.
\]

Let c be its number of pure cyclic square coordinates, from actual
`C_4` or `C_4 x C_2` factors and virtual ID10 factors. Then

\[
 c\leq D,\qquad D+b\leq M/2.                         \tag{3}
\]

Let nu be the number of nonzero nonabelian polar coordinates: one
for each nonabelian scalar-Frattini factor and two for each ID18.
Let d count the dihedral four-point projections and let e_good count
the E projections. Set

\[
 A=a/2+(\ell-\#\text{cyclic four-blocks}-d)+e_{good}.
\]

The term in parentheses counts the genuine V4 four-point projections.
By summing contributions factor by factor,

\[
 r-\nu\geq M/4,\qquad
 r/2-\nu-c\geq A-(b+c)/2.                            \tag{4}
\]

For example, a virtual ID10 has binary rank three, one nonabelian
polar coordinate and one cyclic coordinate; its contribution to
`r/2-nu-c` is `-1/2`, which is paid for by its one cyclic coordinate.
An ID18 contributes `-1/2`, paid for by b. Every other unlisted
contribution to (4) is nonnegative.

## 3. The new local dependency estimate

Choose an ordered basis of a k-dimensional image U in the binary
quotient. Every nonabelian scalar factor contributes an alternating
form of rank two or four. A fixed rank-two form has six ordered
representations in two independent forms; a fixed rank-four
nonsingular alternating form has 720 symplectic coordinate
representations. Extra radical coordinates remain free. The number
720 follows by counting ordered symplectic bases: `15*8*3*2`.

For an ID18 block its two alternating forms are

\[
 X\wedge Y,\quad X\wedge Z,
\]

with X,Y,Z independent. Suppose a chosen basis subset of the global
polar span omits one or both of these coordinates, making them
dependent coordinates. Write s for the dimension of that global span.

- If neither is dependent, use the unrestricted `2^(3k)` choices.
- If exactly one is dependent, choose the two forms in the independent
  coordinate freely, at cost at most `2^(2k)`. The dependent wedge is
  in a fixed s-space, and for fixed nonzero X each wedge determines
  its other factor modulo X. Thus at most `2^(s+1)` further choices
  remain. Compared with `2^(3k)`, the saving is at least `k-s-1`.
- If both are dependent, choose their two values in the s-space.
  Their two support planes meet in the unique line spanned by X.
  Each of Y,Z is determined modulo X. There are at most four ordered
  representations, and the saving is at least `3k-2s-2`.

These choices are sequential: all independent-coordinate variables
are chosen first, making the span known before dependent coordinates
are filled in.

Suppose the nu polar coordinates have span dimension `nu-h`. Let v
be the number of ID18 blocks touched by the h dependent positions.
The preceding estimates and the scalar-factor representation bounds
give the matrix bound

\[
 2^{kr}\binom\nu h C^h
       2^{-h(2k-\nu+h)+kv},                          \tag{5}
\]

before imposing the cyclic relations, where C is absolute. For the
ID18 blocks, a touched block receives at most one extra `2^k` factor
relative to the generic `2k` saving per dependent coordinate. Also

\[
 0\leq v\leq b,\qquad v\leq h.                      \tag{6}
\]

The binomial coefficient overcounts possible basis subsets; this is
harmless. All statements concern surjective local projections, so
the coordinate tuples whose representation bounds are used are
independent, even though the global full-rank condition is discarded
in the upper bound.

## 4. Central kernels and completion of the square

The ambient product has central elementary abelian Frattini subgroup
Z of rank `c+nu`. For `W=H intersect Z` and `U=HZ/Z`, let
`T=W^perp`. Put

\[
 p=\dim(T\cap\mathbb F_2^c),\quad
 q=\dim\operatorname{pr}_{\mathbb F_2^{\nu}}T,
 \quad h=q+u.
\]

Thus `codim W=p+q`. As in the earlier polar argument, choose the
pure-cyclic relation space and the projected polar relation space,
then their graph. There are at most

\[
 {c\brack p}_2{h\brack q}_2 2^{(c-p)q}
\]

choices. The pure cyclic coordinate matrix annihilates a fixed
p-dimensional relation space, reducing its count by `2^(kp)`.
All further quadratic conditions are discarded. For each admissible
`(U,W)`, exactly `2^(k(p+q))` lifts are possible by the elementary
central-complement argument.

Combine this with (5), divide by `|GL(k,2)|`, and put

\[
 \delta=b-v,\quad R=r+v=M-D-\delta,\quad j=k-R/2.
\]

The exponent, apart from `binom(nu,h)C^h`, is exactly

\[
 \frac{R^2}{4}-(j+q/2+u)^2-\frac{3q^2}{4}
 -q(R/2-\nu-c+p)-u(R-\nu)+p(c-p).                  \tag{7}
\]

Here `R/2-nu-c >= A-(delta+c)/2` and `R-nu>=M/4`.
Let `L=D+delta`. Then `c<=D`, `L<=M/2`, and `delta+c<=L`.
Discarding the negative k-square and `-qp`, the remaining exponent
relative to `M^2/4` is at most

\[
 -ML/2+L^2/4+c^2/4-3q^2/4+qL/2-qA-uM/4.
\]

Use

\[
 -3q^2/4+qL/2\leq-q^2/2+L^2/4,
\]

and `L^2/2<=ML/4`, `c^2/4<=ML/8`. This proves the useful bound

\[
 -\frac{M(D+\delta)}8-\frac{q^2}2-qA-\frac{uM}4.    \tag{8}
\]

The constraint `v<=h` becomes

\[
 \delta+q+u\geq b.                                  \tag{9}
\]

Summing over k costs an absolute constant. The factor
`binom(nu,q+u)C^(q+u)` is at most `(CM)^(q+u)`.
Its q-part can be absorbed into half of `q^2/2`, at a total cost
`2^(O(log^2 M))`; its u-part can be absorbed into half of `uM/4`.
The p and v sums cost only polynomial factors. We retain

\[
 -M(D+\delta)/8-q^2/4-qA-uM/8                       \tag{10}
\]

in the exponent, besides the uniform `2^(O(log^2 M))` factor.

## 5. Uniform decay for defective projections

We claim that after averaging the efficient dihedral four-point
choices, every fixed defective configuration with `D+b>=1` has
relative contribution at most

\[
 2^{-\kappa(MD+M+b^2)+O(\log^2 M)}                   \tag{11}
\]

for some absolute `kappa>0`, relative to `4^ell 105^e S_M` after
the appropriate constant local projection weights are restored.

If `D>=1`, the term `MD/8` supplies both a constant multiple of MD
and a constant multiple of M. Equation (9) says that at least one
of delta, q, u is at least `b/3`. In the delta or u case, its
remaining linear penalty supplies a constant multiple of `Mb`,
hence of `b^2`, since `b<=M/4`; in the q case, its square penalty
supplies a constant multiple of `b^2`. Allocate fixed fractions of
the penalties to these requirements. The nonnegative A can simply
be discarded in this case.

If `D=0` and `b>=1`, any term with `delta+u>=1` has a penalty of
order M by integrality. Splitting its penalties into fixed fractions
and using (9) again also gives order `b^2`. It remains to consider
`delta=u=0`, in which case `q>=b>=1`.

In this remaining case there are no cyclic or other scalar defective
blocks. Average the `3^d` embedded dihedral choices versus one V4
choice on each four-point block. For fixed q,

\[
 \mathbb E(2^{-qA})
  =2^{-q(a/2+e_{good})}
          \left(\frac{3+2^{-q}}4\right)^\ell
  \leq2^{-\beta(M-4b)/2},
 \quad\beta=\log_2(8/7)>0.                           \tag{12}
\]

If `b<=M/8`, then `M-4b>=M/2`, so (12) supplies the M penalty while
`q^2/4` supplies the `b^2` penalty. If `b>M/8`, then for sufficiently
large M the `b^2` penalty alone bounds a constant multiple of
`M+b^2`. This completes the proof of (11).

## 6. Sum over all local projection choices

There are only finitely many actual transitive projection choices on
a specified block of size at most eight. Denote their fixed local
weight bounds by constants. If j is the number of scalar defective
blocks, then `D>=j`. On a fixed orbit partition, their placements
and choices are bounded by `(CM)^j`. The ID18 placements and choices
are bounded by `(CM)^b`. Hence summing (11) is bounded by

\[
 2^{-\kappa M+O(\log^2 M)}
 \sum_{j\geq0}(CM)^j2^{-\kappa Mj}
 \sum_{b\geq0}(CM)^b2^{-\kappa b^2}
   =O(2^{-\eta_1M}).                                \tag{13}
\]

The geometric j-sum is bounded, and the b-sum costs
`2^(O(log^2 M))`. Excluding the empty defective configuration only
improves the bound. All constants are uniform in the orbit partition.

When `D=b=0`, the already proved efficient-projection theorem says
that nonsaturated subgroups contribute exponentially little. Thus
for every partition the full count of allowed subdirect subgroups is

\[
 4^\ell105^e S_M(1+O(2^{-\eta_2M})).                  \tag{14}
\]

Summing labelled partitions with minimal fixed points yields the
`Q_n` main term. Finally, extra fixed points are handled exactly as
before: with `N=n-(n mod 2)`, `m=N/2`, and

\[
 B_L=[z^L]\exp(z^2/2+z^4/6+z^8/384),
\]

the contributions with `2s` extra fixed points have relative bound
`C n^s S_(m-s)/S_m <= C(n2^(-m/4))^s`. Their sum is exponentially
small. This proves (1).

## Verification and remaining boundary

The finite projection classification, the ID10 virtual embedding, and
the ID18 square model are separate finite inputs that can be checked
in the supplied scripts. `verify_eight_point_models.py` independently
checks the two models and the scalar polar ranks in GAP/Sage, with
results in `eight_point_model_verification.json`. The asymptotic proof
is the explicit counting argument above. Independent auditing of (5),
(7), (8), the uniform summation in §5, and the finite classification
found no substantive gap; see `audit_eight_point_projections.md`.

The next unresolved class consists of 2-subgroups with eight-point
orbits whose projections have class greater than two or exponent
eight. Nothing in this theorem discards those projections. The
unrestricted Erdős order-distribution problem also allows larger
orbits and non-2-groups.

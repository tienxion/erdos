# Independent proof audit of the elementary, dihedral, and S3 families

Audit date: 4 September 2026.

Scope: `progress.md` in full, together with Section 6 and the reduction in
Section 7 of `progress_v2.md`. This audit checks the arguments directly;
the existing Python outputs were not used as premises. The separate
all-abelian argument is outside this audit's scope.

## Finding

I found **no fatal mathematical gap** in the stated elementary-abelian
asymptotic, the exact enumeration and order limit theorem for `F_n`, or
the `S_3` family `G_n` and its comparison with `F_n`. The conclusions have
the restricted domains claimed in the notes. They do not establish an
order law for a uniform unrestricted subgroup of `S_n`.

There is one small presentation ambiguity in the probabilistic proof:
weights `L_(n,a,b) 4^b` belong to the **orbit profiles** `(a,b)`, not to
each individual labelled orbit partition. After choosing a profile with
those weights, choose a labelled partition uniformly and choose each
four-point projection uniformly from its four possibilities. That
procedure gives the uniform pre-rejection construction used in the
proof. The formulas in the notes use precisely this correct measure.

## Elementary-abelian subgroup count

1. **Uniqueness of the ambient group.** A transitive abelian permutation
   group is regular: every point stabilizer is the kernel of the action,
   because it is unchanged by conjugation in a transitive abelian group.
   For an actual subgroup `H <= S_n`, its orbits and its induced groups
   on those orbits are recoverable from `H`. Their direct product is
   therefore recoverable as well. Counting subdirect subgroups in that
   ambient group does not count the same `H` under two profiles.

2. **Four-point choices.** On a specified four-element set there is
   exactly one *regular* elementary abelian group of order four, the
   double-transposition Klein four. The other three Klein-four
   subgroups of `S_4` are intransitive and are recovered from the
   two-pair construction. This distinction is handled correctly.

3. **Subdirect subspace formula.** The product-lattice Möbius inversion
   gives `(1-x)^a (1-3x+2x^2)^b` because the Möbius values from a
   hyperplane and from the zero subspace of `F_2^2` to the full space
   are `-1` and `2`. Codimension `t` leaves a space of dimension `m-t`.
   Thus formula (2.5) is correct, including small and extreme ranks.

4. **Uniform projection estimate.** A specified factor fails to be
   surjected onto only if some nonzero functional on it annihilates
   `U`. There are `a+3b <= n` such functionals. For `k >= m/4`, the
   union bound gives the asserted error. For `k < m/4`, the Gaussian
   coefficient bounds give a discrete Gaussian tail bounded by an
   absolute constant times `2^(-m^2/16)`. There is no necessary extra
   factor of `m`: the terms in that tail decrease geometrically, with
   ratio decreasing as `m` grows. Conditioning changes total variation
   by at most the rejection probability.

5. **Bad-profile deficit.** Every nontrivial elementary orbit has
   even length, so the number of fixed points has the form
   `f=delta+2t` with `t>=0`. The ambient rank deficit is exactly
   `D=t+sum_(d>=3)(2^(d-1)-d)a_d`. The exceptional support satisfies
   `B<=8D`; equality in the local estimate is attained for an
   eight-point orbit. Thus this inequality covers the most economical
   nonoptimal orbit as well as all larger ones.

6. **Coefficient comparison.** Put `s=B/2`. Appending `s` pairs maps a
   coefficient summand with counts `(a,b)` injectively to `(a+s,b)`.
   The old weight divided by the new weight is
   `2^s (a+s)!/a! <= [2(a+s)]^s <= n^s`. This proves (3.8), with no
   assumption that the coefficients count unweighted configurations.

7. **Counting bad data.** The numbers `2^(d-1)-d`, `d>=3`, are distinct
   positive integers beginning `1,4,11`. One can encode the data by a
   partition of `D`, together with a choice of which of its unit parts
   contribute to `t`. This gives at most `(D+1)p(D) <= 4^D` data. The
   normalizer and fixed-point factors discarded in (3.7) are at most
   one after division by the main labelled factor.

8. **Summation.** The absolute-constant bound
   `S_(m-D)/S_m <= C 2^(-mD/4)` is uniform for `1<=D<=m`. Hence the
   geometric sum in (3.10) is valid and gives the claimed relative
   error, not merely a logarithmic asymptotic. Combining the negligible
   bad count with the uniform projection estimate transfers the entire
   rank law to all elementary abelian 2-subgroups.

The argument for elementary abelian groups of odd prime exponent also
checks: `d/p^d <= 1/p`, the Gaussian-product constant can be bounded
uniformly using `P_p >= P_2`, and all ambient products for a fixed
profile number at most `n!`. Its quadratic exponential separation from
`F_n` is sufficient for the global exclusion corollary.

## The dihedral family F_n

The intrinsic definition avoids overcounting. A full preimage contains
every supported derived subgroup; surjectivity of `U` to a factor's
abelianization then makes its projection to the full orbit group
surjective. Consequently the stipulated blocks are actual orbits, and
`H` recovers both the projection choices and its quotient subspace.

There are three transitive dihedral groups of order eight on a specified
four-element set. Their derived groups have order two. Thus each
dihedral choice multiplies the order by two while contributing three
possible projections, which is exactly the factor `(1+3y)^b` in (4.2).
There is no extra automorphism factor for the binary quotient: the
subspaces are counted within each actual quotient, not as isomorphism
classes of embeddings.

For the limit theorem, the ratio

`T_w(a+2)/T_w(a) = 3(m-a)/(w(a+1)(a+2))`

is correct. Its crossing of one is at
`a=sqrt(3N/(2w))+O(1)`, and it is monotone. The stated comparison of
ratios proves concentration at that scale. For the moment assertion,
on a fixed interval of constant multiples of `sqrt(N)` the decrement
of its logarithm per lattice step is bounded above and below by
positive multiples of `N^(-1/2)`. Multiplying the ratios gives the
claimed Gaussian envelope, including a normalization of order
`N^(1/4)` relative to a modal term. The tails beyond that interval are
geometric. This proves `Var(a)=O(sqrt(N))` and the needed uniform
integrability.

Conditional on the profile and quotient subspace, the number `d` of
dihedral choices is exactly `Bin(b,3/4)`. Rejection depends on the
subspace projections, not on which of the four projection choices was
made on each four-point block. That conditional binomial law therefore
remains exact after rejection. The logarithmic order identity is

`log_2 |H| = 7N/16 - 3a/8 + (d-3b/4) + (K-m/2)`.

The binomial characteristic-function argument and the stated
concentration give the displayed central limit theorem. The variance
calculation also checks: the conditional variance contributes
`3 E[b]/16`; the remainder has variance `O(sqrt(N))` because the
rank has bounded second moment about `m/2`, the pair count has variance
`O(sqrt(N))`, and Cauchy-Schwarz controls their covariance. Exponentially
small rejection cannot change these estimates for variables bounded by
a linear function of `n`.

## The S3 family G_n

The full symmetric group on a specified three-element set is unique,
its derived subgroup has order three, and its abelianization has rank
one over `F_2`. With `a+2b=m-1`, the total binary quotient rank is thus
`m`, the same as for `F_n`. The labelled block factor is
`n!/(6 2^a a! 24^b b!)`, and the derived kernel has order `3*2^d`.
This proves both the exact generating polynomial and the relative
coefficient asymptotic in Theorem H.

Marking one pair in the coefficient series gives exactly
`E[a]=A_(N-2)(4)/(2 A_N(4))`. The concentration and moment bounds already
proved imply `E[a]~sqrt(3N/8)`: convergence in probability alone would
not suffice, but the moment estimate supplies uniform integrability.
Therefore `|G_n|/|F_n|~sqrt(N/24)` is justified for both odd residue
classes modulo four.

The projection onto the three-point orbit is an `S_3` quotient, so
every member of `G_n` is nonnilpotent. Its odd part is exactly three.
The families are disjoint, and the global probability bound (6.6)
follows immediately by enlarging the denominator to their union. The
extension of the order CLT to `G_n` has only the stated constant shift
and the negligible change from `N` to `N-2` in the pair statistics.

The reduction concerning an omitted supported dihedral commutator is
also correct: an intersection with a direct factor is normal in that
factor by subdirectness; every nontrivial normal subgroup of `D_8`
contains its central commutator of order two. Trivial intersection
makes deletion of that orbit injective, producing a graph of a
surjection to `D_8`. This is a reduction only; its use in an asymptotic
count still needs a bound for the number of such surjections.

## What a submission would still require

The audited theorems can be presented as proved partial results, subject
to a literature review establishing what is new. Their logical status
does not depend on the geometric Witt-filtration assertions of the
user's draft; the common input used here is elementary Gaussian
coefficient counting. A paper should make that distinction explicit.

An asserted solution of Problem 1163 for the uniform unrestricted
measure would require a theorem controlling the complement of the
chosen families, or another direct theorem about that unrestricted
measure. In particular, the order center `7n/16` and the odd-part law
from `F_n union G_n` cannot be transferred to all subgroups by a lower
bound for the total number of subgroups. The present notes correctly
refrain from doing so.

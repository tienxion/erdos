# Counts and order laws for classes of subgroups of symmetric groups

Consolidated results, 4 September 2026.

**We have substantial partial results for Erdős 1163, not its
unrestricted order law.** The proofs have undergone independent agent
audits and finite checks. Literature searches have not established
novelty. This package is suitable for discussion and expert review as
partial results, without claiming that either Erdős 1162 or 1163 is
solved.

All counts are of actual subgroups of `S_n`, not conjugacy classes.
Every probability is uniform on the explicitly specified set. Put

\[
\delta=n\bmod2,\quad N=n-\delta,\quad m=N/2,
\quad S_m=\sum_k{m\brack k}_2,
\]

\[
A_N(w)=[z^N]\exp(z^2/2+wz^4/24),\qquad
B_N=[z^N]\exp(z^2/2+z^4/6+z^8/384).
\]

## Every exact order in a linear interval

Put `a_(n,j)=#{H<=S_n: |H|=2^j}`. Uniformly for all integers
`floor(n/4)<=j<=floor(n/2)`,

\[
\boxed{\log_2 a_{n,j}\geq n^2/16+
\left(7n/8-|j-3n/8|\right)\log_2 n-O(n).}             \tag{S1}
\]

Combining this construction with Roney-Dougal–Tracey's published
upper bound for all 2-subgroups proves, uniformly on that interval,

\[
\boxed{\log_2 a_{n,j}=n^2/16+O(n\log n).}              \tag{S2}
\]

This conclusion concerns unrestricted counts at each stated exact order.
The construction uses only class-two, exponent-four groups with orbits
of size at most eight. It is independent of our harder dominance and
classification arguments. Within the explicitly defined family `Q_n`
below, the right side of (S1) is also a matching estimate with error
`O(n)`; this sharper equality is not asserted for `a_(n,j)`.

Proof: [order_spectrum.md](order_spectrum.md).
Self-contained submission writeup:
[website_note_draft.md](website_note_draft.md).
Independent audit:
[audit_order_spectrum.md](audit_order_spectrum.md).

## All abelian subgroups

For an absolute `c>0`, the set `Ab_n` of all abelian subgroups satisfies

\[
|\mathrm{Ab}_n|=n!A_N(1)S_m(1+O(2^{-cn})).             \tag{A}
\]

With probability `1-O(2^(-cn))`, a uniform abelian subgroup is elementary
abelian of exponent dividing two, has delta fixed points, and has all
remaining orbits of size two or four. Its order law is

\[
\Pr(\log_2|H|-N/4=j)
\longrightarrow\frac{2^{-j^2}}{\sum_{t\in\mathbb Z+\epsilon}2^{-t^2}},
                                                               \tag{B}
\]

where `epsilon=0` for even m and `epsilon=1/2` for odd m. Take the limit
along either subsequence, with j on the indicated lattice. Thus its
binary logarithmic order has bounded fluctuations. The coefficient is
explicit:

\[
A_N(1)\sim\frac{e^{-3/4}}{\sqrt{2\pi N}}
e^{\sqrt{3N/2}}\left(\frac e{6N}\right)^{N/4}.
\]

Proof: [progress_v2.md](progress_v2.md),
§§2–5, using the Gaussian preliminaries of the first note.
Audit: [audit_abelian.md](audit_abelian.md).

## All 2-subgroups with orbits of size at most four

Let `T_n` contain **all** 2-subgroups with orbit sizes 1, 2, or 4. Then

\[
|T_n|=n!A_N(4)S_m(1+O(2^{-cn})),                       \tag{C}
\]

and, for uniform H in this entire class,

\[
\frac{\log_2|H|-7N/16+(3/8)\sqrt{3N/8}}
     {\sqrt{3N/64}}
\Longrightarrow\mathcal N(0,1).                      \tag{D}
\]

The new step counts all previously omitted subdirect products: cyclic
order-four orbit projections and omitted supported dihedral commutators
contribute an exponentially small fraction. The earlier saturation
assumption has been removed for this whole class.

Proof: [extension_small_orbits.md](extension_small_orbits.md).
Audit: [audit_small_orbits.md](audit_small_orbits.md).
The inherited CLT is proved in
[progress.md](progress.md), §5.

## Eight-point factors and a different order law

The classical transitive extraspecial group E of order 32 has
`E/E'=C_2^4` and exactly 105 conjugates in `S_8`. Its center determines
a perfect matching of the eight points; its normalizer is the matching
stabilizer of order 384.

Use two-, four-, and eight-point orbit projections `C_2`, `V_4` or
`D_8`, and E respectively, and take subgroups containing the supported
derived groups. The resulting family `Q_n` satisfies

\[
|Q_n|=n!B_NS_m(1+O(2^{-cn})).                          \tag{E}
\]

Let rho solve `rho/2+rho^2/3+rho^4/96=N/2`. For uniform H in `Q_n`,

\[
\frac{\log_2|H|-3N/8-\rho^2/24+\rho/8}{\rho/\sqrt{24}}
\Longrightarrow\mathcal N(0,1).                      \tag{F}
\]

The center is `3N/8+sqrt(N/12)-(48N)^(1/4)/8+O(1)`; the scale is
asymptotic to `(N/12)^(1/4)`. Both differ from (D).

The saturation assumption has now also been removed here. Let `J_n`
contain **all** subgroups with those specified full orbit projections,
allowing arbitrary fixed points and arbitrary subdirect products.
Then

\[
|J_n\setminus Q_n|/|Q_n|=O(2^{-cn}).
\]

Consequently (E) and (F) hold for the entire class `J_n` as well. This
includes all subdirect products for these projections, but excludes
other transitive groups on eight points. Proof:
[extension_efficient_orbits.md](extension_efficient_orbits.md).
Audit: [audit_efficient_orbits.md](audit_efficient_orbits.md).

Proof: [progress_v3.md](progress_v3.md),
§§1–4. Audits:
[group and count](audit_extraspecial.md),
[order law](audit_extraspecial_clt.md).

## The full class with class at most two, exponent at most four, and small orbits

Let `C_n` consist of **all** 2-subgroups of `S_n` with nilpotency class
at most two, exponent dividing four, and orbit sizes at most eight.
There is an absolute `c>0` such that

\[
|C_n\setminus Q_n|/|Q_n|=O(2^{-cn}).                  \tag{J}
\]

Thus the count (E) and order law (F) hold for this entire class, including
all nine transitive eight-point projection types satisfying these
restrictions and every subdirect product. The proof uses an exhaustive,
independently checked finite classification inside an explicit Sylow
2-subgroup of `S_8`.

Moreover, with probability `1-O(2^(-cn))` in `C_n`,

\[
Z(H)=H'=\Phi(H)
\]

is elementary abelian. Its minimal generator number satisfies
`d(H)=N/4+O_P(1)` with the discrete Gaussian law (B), while

\[
\frac{\log_2|H'|-N/8-\rho^2/24+\rho/8}{\rho/\sqrt{24}}
\Longrightarrow\mathcal N(0,1),
\]

also with `Z(H)` in place of `H'`.

Proofs:
[extension_eight_point_projections.md](extension_eight_point_projections.md),
[special_structure.md](special_structure.md).
Independent audits:
[eight-point theorem](audit_eight_point_projections.md),
[structural conclusions](audit_special_structure.md).

A separate extension allows exactly `b` arbitrary non-E eight-point
transitive 2-group projections, with all other projections in `J_n`.
Writing this set as `X_(n,b)`, uniformly for
`1<=b<=floor(log_2(n)/16)` we have

\[
|X_{n,b}|/|Q_n|
\leq2^{-bn/4+O(n^{5/8}+\log^2 n)}.                   \tag{K}
\]

For fixed b the error improves to `O_b(sqrt(n)+log n)`. This allows
some projections of higher class and exponent, but does not treat
arbitrarily many of them. Proof:
[extension_one_bad_orbit.md](extension_one_bad_orbit.md).
Audit:
[audit_bad_orbit_extension.md](audit_bad_orbit_extension.md).

## Consequences for unrestricted sampling

Equation (E) proves

\[
\boxed{\log_2|\operatorname{Sub}(S_n)|
\geq n^2/16+(7/8)n\log_2n-O(n).}                      \tag{G}
\]

This lower bound already holds for 2-groups of nilpotency class at most
two and exponent dividing four. Comparing (A) with (E) gives

\[
\boxed{\Pr_{H\in\operatorname{Sub}(S_n)}(H\text{ abelian})
\leq2^{-(n/8)\log_2n+O(n)}.}                         \tag{H}
\]

Comparing (C) with (E) also gives

\[
\boxed{\Pr_{H\in\operatorname{Sub}_2(S_n)}
(\text{every orbit has size at most four})
\leq2^{-(n/8)\log_2n+O(n)}.}                         \tag{I}
\]

Here `Sub_2(S_n)` denotes all 2-subgroups. Thus almost every 2-subgroup
has an orbit of size at least eight. No conjecture about typical orbit
sizes is assumed in this deduction.

For odd n, replacing the fixed point in `Q_n` by one `S_3` orbit gives
a disjoint family `R_n` with odd part exactly three and

\[
|R_n|/|Q_n|\sim (48N)^{1/4}/6.
\]

So `Q_n` itself cannot contain almost all unrestricted subgroups in odd
degrees. Formula (F) also holds for `Q_n union R_n`; that does not
establish it for unrestricted subgroups.

## What remains

The exact-order counts (S1)–(S2), complete-class theorems (A)–(D), the
count and order law (E)–(F) extended to `C_n`, the structural results
(J)–(K), and the unrestricted conclusions (G)–(I) are the strong
partial results obtained here. We do not have a matching total-count
upper bound, a typical unrestricted order, or a typical unrestricted
odd part. Additional orbit projections, larger orbits, and their
subdirect products remain to be controlled. The omitted-commutator
problem is resolved for the specified two-, four-, and eight-point
projections, and for the full class-two exponent-four class with all
orbit sizes at most eight.

The extraspecial factor, Gaussian identities, and Birkhoff formula are
classical. Roney-Dougal–Tracey already establish the leading `n^2/16`
exponent and a positive `n log n` lower term. Targeted searches did not
find the displayed explicit `7/8` construction or these relative order
laws, but that is not a novelty certificate. A submission should be
framed around partial results and checked against the relevant
literature, without claiming a solution of Erdős 1163.

The verification scripts pass. Their finite checks include actual
permutation subgroup enumeration, the Birkhoff formula, the class-two
subgroup parameterization, binary subspace enumeration, and coefficient
and moment calculations, an independent exhaustive degree-eight
classification, and 470 normal-quotient checks. Computations check the proofs' algebra and
indexing; they do not replace the asymptotic arguments.

The self-contained exact-order result (S1)–(S2) was submitted as a
partial proof to the Erdős 1163 website on 4 September 2026 and is
awaiting moderator approval. See
[submission_record.md](submission_record.md).
The original PDFs have not been changed.

# Audit record for the exceptional-orbit extension

> This is an AI-agent proof review, not independent human peer review.

4 September 2026.

The root agent independently reviewed the single-exception argument in
[extension_one_bad_orbit.md](extension_one_bad_orbit.md) before the logarithmic extension was added.
Its reported checks were:

- `Phi(L)=span q(U)` and `d(L)=k+h-t` in the weighted efficient-class
  count;
- the completion of the square in the generator-rank weight;
- the coefficient comparison;
- the application of Roney-Dougal–Tracey Theorem 4.6 with target
  `F=Q` and trivial auxiliary projection;
- the Goursat parametrization and final exponential comparison.

No gap was found in those steps. The requested strengthening of the
finite check has been implemented: the excluded group is explicitly
checked for `S_8`-conjugacy to the constructed E group, rather than
identified only by its order, center, and rank.

The revised finite check also tests **all** normal quotients, not only
the class-two exponent-four quotients. It enumerates 177 subgroup
conjugacy classes of a Sylow 2-subgroup, of which 35 are transitive.
The 34 non-E classes have 470 normal quotients in total; all satisfy
`|Z(Q)|^2 |Q'|<=64`. The 448 class-two exponent-four quotients are
recorded separately as a subset. The script also checks the ambient
Sylow group's order 128, derived-group order 16, and nilpotency class
four. All assertions pass.

The root agent also independently reviewed the extension to
`b<=floor(log_2(n)/16)` in Section 5 and found no gap. The checks were:

1. Intermediate groups need not be class two, but their extra kernel
   gives `d(L_i)<=d(L_0)+7i` and their commutator projection gives
   `log_2|L_i'|<=log_2|L_0'|+4i`.
2. The epimorphism product has parameters
   `alpha=sum log_2|Z(Q_i)|`, `beta=sum log_2|Q_i'|`, satisfying
   `2alpha+beta<=6b`, and an overhead `2^(O(b^2+b log n))`.
3. The weighted moment constant is tracked explicitly: its Gaussian
   factor is `2^(alpha^2/4)`, while the nonsaturation error is bounded
   by `2^(O(log^2 r)-c r 2^(-beta))`.
4. The coefficient error is bounded by
   `C sqrt(N) 2^(beta/2)+C log(N+2)`, rather than an unspecified
   constant depending on beta.
5. At `b<=log_2(n)/16`, these estimates yield the uniform error
   `O(n^(5/8)+log^2 n)` and the exponent `-bn/4`.

No extension to arbitrary b is claimed. In that regime the changing
weight can favor four-point dihedral profiles, so the fixed-weight
coefficient asymptotic cannot be reused without further analysis.

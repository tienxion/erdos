# Independent proof audit: abelian subgroup theorem

4 September 2026. Scope: Sections 2–5 of progress_v2.md, with the
Gaussian and surjectivity estimates in Sections 2–3 of progress.md
checked as dependencies. This is a mathematical audit, independent of
the verification programs; it does not establish bibliographic novelty.

**Conclusion:** I found no substantive gap or incorrect constant in the
abelian theorem, its explicit equivalent, or its consequence for the
unrestricted measure. The proof establishes the stated exponentially
small relative error for all abelian subgroups. It does not establish
an unrestricted order law.

## Details checked

1. **Birkhoff estimate.** The exponent contributed at column \(j\) is
   exactly
   \[
   s_{j+1}(r_j-s_j)
   +(s_j-s_{j+1})(r_j-s_j)=s_j(r_j-s_j).
   \]
   Thus the Gaussian upper bound gives the asserted quadratic estimate.
   There are at most \((n+1)^J\) admissible column arrays, and the factors
   for different primes multiply. This proves (2.3).

2. **Local norm losses.** For all \(\ell\geq8\),
   \(\log_2\ell/\ell\leq3/8\). For the norm estimate the same bound
   applies already for \(\ell\geq5\) with
   \(\log_2 5/5<7/15<15/32\). The remaining nonoptimal groups are
   \(C_3,C_4\), whose norms are respectively
   \(\sqrt{\log_2 3}\) and \(\sqrt2\). The exceptional small orders in
   the first-rank estimate are correctly handled. No classification
   assumption beyond the abelian invariant factors is missing.

3. **Defect and odd-degree case.** With \(L=f-\delta+B\),
   \(2D\leq L\leq8D\) holds. If \(\delta=1,f=0\), an odd nontrivial
   orbit necessarily occurs; its contribution at most \(-9\) to
   \(\sum(8r_{2,1}(B_i)-3|B_i|)\) more than offsets the \(+3\) fixed-point
   term. Every excluded profile has positive even \(L\), hence integer
   \(D\geq1\), and \(B\leq8D+1\).

4. **Quadratic loss.** The nonprincipal coordinates have norm at most
   \(B/2\leq5D\), giving
   \(\mathcal E(A)\leq m^2-2mD+26D^2\). This yields loss \(mD\)
   when \(D\leq m/26\). In the other range the triangle estimate is
   \[
   \|v(A)\|\leq m-D/16+15\delta/32\leq m-D/32.
   \]
   For \(m\geq416\) the latter implication is valid (indeed \(D\geq17\),
   while \(D\geq15\) would suffice). Since \(D\leq m\), squaring gives
   the weaker claimed loss \(mD/32\). All squaring occurs between
   nonnegative quantities.

5. **Ambient products and profile count.** A regular abelian projection
   is uniquely recovered from the action of \(H\) on its orbit. Its
   labelled multiplicity is \(\ell!/(\ell|\operatorname{Aut}B|)\).
   The resulting exponential-formula coefficient in (4.2) is therefore
   correct. Appending \(h=L/2\) pairs replaces a coefficient summand by
   its old weight divided by \(2^h(a+1)\cdots(a+h)\); this denominator
   is at most \(n^h\), proving (4.3) with no additional injection factor.
   There are at most \(n^2\) abstract abelian types of order at most \(n\),
   and the ordered-list bound on at most \(8D+1\) exceptional symbols is
   bounded by \((Cn)^{20D}\). The Birkhoff factor uses at most
   \(8D+2\leq10D\) coordinates. Their product gives the exponent \(34D\)
   in (4.4). The geometric ratio tends to zero exponentially in \(n\);
   an unspecified absolute \(c>0\) is therefore justified.

6. **Main term and order law.** The inherited main term counts
   subspaces surjecting onto every \(C_2\) or \(C_2^2\) projection.
   Failed surjectivity is covered by at most \(a+3b\leq n\) hyperplanes,
   with conditional failure at rank \(k\) at most \(2n2^{-k}\).
   Gaussian dimension tails justify the split at \(m/4\). The resulting
   total-variation error is uniform in the orbit profile. The factor
   \(P_2^{-1}\Theta_\epsilon\) for \(S_m\) follows by dominated
   convergence on the lattice \(\mathbb Z+\epsilon\). Thus the transfer
   from optimal elementary subgroups to all abelian subgroups is valid,
   including both parity classes of \(m\).

7. **Saddle constant and lattice factor.** Writing
   \(s=\sqrt{12m/w}\), the saddle satisfies the useful exact identity
   \[
   \log\rho=\log s-\operatorname{arsinh}(3/(ws)).
   \]
   Hence
   \(\rho=s-3/w+O(s^{-1})\) and
   \(\log\rho=\log s-3/(ws)+O(s^{-3})\). Substitution into
   \[
   A_N(w)\sim
   \frac{\exp(m/2+\rho/4)\rho^{-m}}
        {\sqrt{2\pi(2m-\rho/2)}}
   \]
   gives exactly the constant \(e^{-3/(4w)}\), the square-root exponent
   \(\sqrt{3N/(2w)}\), and the denominator \(\sqrt{2\pi N}\) in (5.4).
   In Fourier inversion, the neighborhood of \(\pi\) is suppressed by
   the \(X\)-Poisson factor \(e^{-\Omega(\sqrt m)}\); there is no missing
   factor of two. The stated small-neighborhood Taylor estimate and
   complementary exponential bounds suffice for the relative local
   limit. Formulas (5.6) and (5.7) then follow algebraically; in (5.7)
   the constant is indeed \(e^{-9/16}\).

## Editorial correction only

The sentence before (2.3), “each subgroup type has at most \((n+1)^J\)
possible column arrays,” should read “there are at most \((n+1)^J\)
possible subgroup types (column arrays).” A type is itself a column
array. This does not affect the bound or any subsequent argument.

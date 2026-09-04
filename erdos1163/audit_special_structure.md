# Independent audit: typical special-group structure

4 September 2026. Scope: special_structure.md.

**Conclusion:** The argument is correct. It proves that, within the
specified sampling class, \(Z(H)=H'=\Phi(H)\) with exponentially high
probability, and that the stated generator-number and center/derived
order laws hold. By the newly audited dominance theorem, these
conclusions also hold for the full class of 2-subgroups of class at
most two, exponent dividing four, and orbit sizes at most eight.

## The derived-group estimate

For the saturated construction, commutators depend only on \(U=H/D'\).
The annihilator of the span of their vector-valued outputs is precisely
the relation space of the coordinate alternating forms. Therefore the
dimension of their linear span is \(\dim H'\).

The representation counts six and 720 are correct. For a given
pulled-back alternating form, its radical recovers the kernel of the
surjective local coordinate map; two such maps differ by a symplectic
isometry. In dimension four the number is
\(15\cdot8\cdot3\cdot2=720\). This counts alternating-form
representations, so the orthogonal-group constant 72 from the
square-form argument would not suffice here.

The mixed rank-two/rank-four deficiency bound validly uses the smaller
saving \(2k\) per dependent coordinate. There are no central-complement
lift factors because each \(U\) defines exactly one saturated subgroup.
The exponent identity is
\[
k(m-k)-h(2k-z+h)
=m^2/4-(k-m/2+h)^2-h(m-z).
\]
Since \(z\leq m/2\), the shifted Gaussian sum and the remaining
geometric series give the claimed uniform
\(O(m2^{-m/2})\) relative error. The uniformly positive subdirect
acceptance probability preserves this estimate.

All squares of \(H\) lie in \(D'\), because \(D/D'\) is elementary
abelian. Thus \(H'=D'\) implies \(\Phi(H)=H^2H'=D'\).

## The center estimate

Surjectivity of \(U\) onto every nonabelian quotient factor and
nondegeneracy of its local polar form imply that an element in the
radical of the vector commutator map must have zero projection on
every such factor. Hence the radical is exactly
\(U\cap V_{\rm ab}\), proving
\[
Z(H)/D'=U\cap V_{\rm ab}.
\]
This equality does not require the preceding high-probability event
\(H'=D'\); saturation and local surjectivity are sufficient.

For each fixed \(V_{\rm ab}\) and \(k\), the union bound
\[
(2^\ell-1)\frac{2^k-1}{2^m-1}
\leq 2^{1+\ell+k-m}
\]
is correct. The cutoffs \(\ell\leq m/4\), \(k\leq5m/8\) leave
the stated exponential loss \(2^{1-m/8}\).

The orbit-profile tail is also justified: the relevant independent
Poisson means are \(O(m^{1/4})\) and \(O(m^{1/2})\), whereas the
threshold is linear in \(m\). A Chernoff bound gives
\(\exp(-\Omega(m\log m))\). Conditioning on the total degree
multiplies its probability by at most a constant, using the uniform
maximum of the \(C\)-Poisson mass and the already proved local limit
for the total.

If one wishes to state this stronger tail under the final subdirect
sampling measure itself, conditioning on acceptance costs at most
another constant, since its probability tends uniformly to one.
Using only total variation would give the weaker exponential tail,
which already suffices for the center theorem. Thus there is no
conditioning gap.

## The limit laws and their scope

On the common high-probability event,
\[
d(H)=K,\qquad \log_2|H'|=\log_2|H|-K.
\]
The discrete Gaussian law for \(K-m/2\) transfers to the minimal
generator number. Subtracting \(K=m/2+O_{\Pr}(1)\) from the known
order CLT shifts its center by \(m/2=N/4\), giving exactly
\[
N/8+\rho^2/24-\rho/8
\]
for the derived-group logarithm, with unchanged scale
\(\rho/\sqrt{24}\). Equality of center and derived subgroup supplies
the center law. Exponentially small total-variation changes preserve
all these distributional conclusions.

No substantive correction is required. This audit does not extend
the assertions to unrestricted subgroups of \(S_n\).

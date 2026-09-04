# Independent audit: removing saturation for efficient 2/4/8 projections

> This is an AI-agent proof review, not independent human peer review.

4 September 2026. This is a follow-up to audit_small_orbits.md and
audits the completed extension_efficient_orbits.md.

**Conclusion:** The extension is correct. It removes the supported
commutator-containment hypothesis from the sampling model on the
specified projection class, with an exponentially small error.
The resulting order law remains restricted to that class; other
transitive eight-point groups and larger orbits are not covered.

## The 72-representation bound

Let $q_+(x_1,y_1,x_2,y_2)=x_1y_1+x_2y_2$, and suppose a restricted
square form is $q_+\circ L$, where $L:\mathbb F_2^k\to\mathbb F_2^4$
is onto. The radical of its polar form is exactly $\ker L$.
Indeed, vanishing of its pairing with every vector is equivalent,
by surjectivity and the nondegeneracy of the target polar form, to
$Lx=0$.

Consequently any two such representations differ by one invertible
linear map of the four-dimensional target. Equality of their
quadratic functions says exactly that this map preserves $q_+$.
There are no additional choices outside its recovered four-dimensional
support.

The isometry group has order $9\cdot4\cdot2=72$, as counted in the
proof. For completeness, after choosing a nonzero singular vector,
the eight vectors pairing to one are paired by translation by that
vector, and exactly one of each pair is singular. This gives four
possible partners. Their hyperbolic plane has a hyperbolic
two-dimensional complement: the original form has ten zeros, and
the zero count in an orthogonal sum with a hyperbolic plane forces
the complement to have three zeros. Its ordered hyperbolic bases
number two. Thus the 72 bound is fully justified without relying on
an external orthogonal-group order formula.

## Mixed-factor deficiency estimate

If $J$ is the set of $h$ positions outside a chosen basis of the
coordinate square forms, each position has two or four coordinate
columns, according as its factor is $D_8$ or $E$.
For each such position its square form is selected from a space of
size $2^{z-h}$, followed by at most 72 representations. Relative
to unrestricted columns it therefore saves a factor at least
$2^{2k}$. Multiplying over positions gives
$$
2^{kr}\binom zh72^h2^{-h(2k-z+h)}.
$$
Using the smaller saving for the four-column factors is a valid
upper bound. The rank and projection conditions discarded elsewhere
do not invalidate this argument: the coordinate tuples whose
representation count is used remain independent.

The exact $2^{kt}$ central-complement count and the Gaussian
${h\brack t}_2$ factor then apply unchanged. Independently
completing the square yields
$$
\frac{r^2}{4}-(j+t/2+u)^2-\frac{3t^2}{4}
-t(r/2-z)-u(r-z),
$$
as in (4). Because $r-z\geq r/2$, the geometric bound in $u$
is uniform for large $r$, and the remaining shifted Gaussian sum
is uniformly bounded.

## Averaging and fixed points

Here $z=d+c$ and
$$
r/2-z=a/2+(b-d)+c.
$$
Summing over the $\binom bd3^d$ four-point projection choices
therefore gives exactly
$$
2^{-t(a/2+c)}
\left(\frac{3+2^{-t}}4\right)^b.
$$
The $105^c$ extraspecial embedding factor cancels from the relative
bound, as it should. For $t\geq1$, put $\beta=\log_2(8/7)$.
The inequality
$$
a/2+c+\beta b\geq\frac{\beta}{2}(a+2b+4c)
$$
is valid coefficient by coefficient. Thus the loss is exponential
uniformly in the orbit profile. The remaining
$2^{O(\log^2(r+2))}$ factor does not affect that conclusion.

The surjectivity union bound uses at most $a+3b+15c=O(r)$
hyperplanes. The argument for extra fixed points is identical to the
already audited coefficient-ratio and Gaussian-rank argument.
These facts prove the stated exponential relative bound, so the
earlier enumeration and order CLT transfer in total variation.

## Notation correction

At the time of this audit, the new projection class was called $R_n$.
That conflicts with the odd-degree $S_3$ family already called $R_n$
in progress_v3.md. The new class should use a different symbol, for
example $J_n$. This is a notation issue, not a defect in the proof.

No substantive mathematical correction was needed. This audit does not
certify novelty.

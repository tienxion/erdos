# Independent audit: all 2-subgroups with orbits at most four

> This is an AI-agent proof review, not independent human peer review.

4 September 2026. This audits extension_small_orbits.md, independently
of its verification program. No shared proof file was edited.

**Conclusion:** The proof establishes the stated theorem. I found no
substantive gap in the central-extension parametrization, deficiency
counts, completed-square identities, projection-type averaging, or
uniform estimates. Consequently the earlier count and order CLT for
$F_n$ do extend to the full class $B_n$ of 2-subgroups with orbits
of sizes $1,2,4$, with exponentially small total-variation error.
This conclusion concerns that restricted class; it does not assert
that its orbit restriction holds for unrestricted random subgroups.

## 1. Exact subgroup parametrization

For the prescribed product
$$
D=C_2^a\times C_4^c\times D_8^d\times V_4^e,
$$
the subgroup $Z$ of supported squares is central of exponent two,
contains $D'$, and makes $D/Z$ elementary abelian. Therefore
the square map is well-defined on $D/Z$.

For $U\leq D/Z$ and $W\leq Z$, the condition $q(U)\subseteq W$
is necessary. It is sufficient because the preimage of $U$, modulo
$W$, then has exponent two and is therefore abelian. Its dimension
is $k+t$, and $Z/W$ has dimension $t$. The complements to $Z/W$
are graphs of arbitrary linear maps from a fixed $k$-dimensional
complement into $Z/W$, giving exactly $2^{kt}$ subgroups.

Surjectivity onto each coordinate of $D/Z$ is equivalent to full
projection onto each original factor. This is immediate for the
elementary factors and follows from the Frattini property for $C_4$
and $D_8$. Thus these subgroups have precisely the stipulated orbits.
Their intrinsic orbit projections recover $D$, precluding duplicate
counting between different ambient products.

## 2. Factorization counts

The evaluation map from homogeneous quadratic polynomials over
$\mathbb F_2$ to functions on $\mathbb F_2^k$ is injective:
evaluation on the coordinate unit vectors recovers the coefficients
of $x_i^2$, and evaluation on their pairwise sums recovers the
coefficients of $x_ix_j$. Consequently unique factorization in the
polynomial ring applies to the restricted square functions.

A nonzero product of two distinct linear forms consequently has
exactly two ordered factorizations over $\mathbb F_2$. This verifies
the factor $2^h$ in (4).

A nonzero decomposable alternating form determines a unique
two-dimensional subspace of the dual vector space. Its ordered
independent decompositions are the six ordered bases of that
subspace. This verifies the factor $6^h$ in (10).

The coordinate-surjectivity conditions guarantee independence of
each dihedral pair and nonvanishing of each cyclic coordinate.
Discarding these conditions in subsequent bounds introduces only
overcounting. Choosing a subset that spans the quadratic or polar
forms can likewise overcount, but cannot omit any admissible matrix.
Division by $|\mathrm{GL}(k,2)|$ is valid because every embedded
$k$-space has exactly that many ordered bases.

## 3. Nonsaturated dihedral factors

For $c=0$, if the restricted square forms have relation space of
dimension $h$, the span of the vector-valued square map has
codimension $h$. The number of codimension-$t$ subspaces $W$
containing that span is exactly ${h\brack t}_2$.

I independently expanded the exponent in (5). With $h=t+u$ and
$j=k-r/2$, it is precisely
$$
k(r-k)-h(2k-d+h)+t(h-t+k)
=\frac{r^2}{4}-(j+t/2+u)^2-\frac{3t^2}{4}
 -t(r/2-d)-u(r-d).
$$
Thus (6) is correct. Since $r-d\geq r/2$, the sum over $u$ after
the combinatorial bound has ratio at most $2d\,2^{-r/2}$, uniformly
less than one for large $r$. The shifted discrete Gaussian sum
over $k$ is uniformly bounded, regardless of parity.

It is essential that the remaining bound is averaged over all
dihedral/Klein-four projection choices. This averaging is performed
correctly:
$$
4^{-b}\sum_{d=0}^b\binom bd3^d
 2^{-t(a/2+b-d)}
=2^{-ta/2}\left(\frac{3+2^{-t}}4\right)^b.
$$
For every $t\geq1$ this is at most
$2^{-a/2}(7/8)^b$, hence at most
$2^{-\beta r/2}$, where $\beta=\log_2(8/7)>0$ and $r=a+2b$.
The remaining sum over $t$ is bounded by
$2^{O(\log^2(r+2))}$; this subexponential factor is absorbed by the
uniform exponential loss. No claim of such a loss for every single
ambient product is required or made.

## 4. Cyclic factors and the annihilator decomposition

For $T=W^\perp\leq\mathbb F_2^c\oplus\mathbb F_2^d$, define
$R=T\cap\mathbb F_2^c$ and let $Q$ be the projection onto the second
summand. Put $p=\dim R$, $q=\dim Q$.

Every $Q$ is contained in the relation space of the dihedral polar
forms, because the cyclic square coordinates have zero polar form.
For fixed $R,Q$, the subspaces $T$ are precisely the graphs of
maps $Q\to\mathbb F_2^c/R$. This gives exactly the factor
$2^{(c-p)q}$ in (11). The cyclic coordinate matrix must annihilate
$R$, giving at most $2^{k(c-p)}$ choices. The additional conditions
coming from the graph are discarded in the proof; that is a valid
upper bound. No converse to this relaxed condition is being used.

Combining these factors gives the exponent
$$
k(r-k)-h(2k-d+h)
 +p(c-p)+q(h-q)+(c-p)q+kq.
$$
With $h=q+u$, completing the square yields exactly (12):
$$
\frac{r^2}{4}-(j+q/2+u)^2-\frac{3q^2}{4}
 -q(r/2-d-c+p)-u(r-d)+p(c-p).
$$
The inequalities $r/2-d-c\geq-c/2$ and $r-d\geq M/2$
are correct. Summing in the order used in the proof yields
$$
\frac{M^2}{4}-\frac{Mc}{2}+\frac{7c^2}{12}
 +O(c\log M+\log^2 M)
$$
as claimed. Because $1\leq c\leq M/2$, the first two correction
terms are at most $-5Mc/24$. Moreover
$$
\frac{c\log M+\log^2 M}{Mc}\longrightarrow0
$$
uniformly for $c\geq1$. Thus the claimed bound
$C S_M2^{-Mc/6}$ is justified uniformly; the logarithmic error
does not create an overlooked small-$c$ exception.

The case $d=0$ is correctly separated to avoid expressions with a
zero base, and extending sums beyond their feasible ranges only
increases the bound.

## 5. Projection types, fixed points, and transfer

The exact number of projection choices with $c$ cyclic blocks is
$\binom bc3^c4^{b-c}$. Summing the cyclic bound therefore gives
the binomial estimate (14). Combining it with the nonsaturated
dihedral estimate and the previously proved uniform surjectivity
bound yields (15). For small fixed $M$, an absolute upper-bound
constant exists because only finitely many parameter values occur.

Finally, all nontrivial orbit sizes are even, so $f=\delta+2s$.
The coefficient ratio from appending $s$ pairs and the Gaussian
bound $S_{m-s}/S_m\leq C2^{-ms/4}$ make the extra-fixed-point
sum geometrically small. This proves the theorem for every parity
and includes the all-fixed-points case.

The exponential relative bound immediately supplies the same
total-variation bound for the two uniform measures, so transferring
the earlier central limit theorem is rigorous. Polynomially bounded
order moments also transfer if desired.

## Review limits

This is proof verification, not a literature novelty certification.
No correctness correction to the mathematical argument was needed.
The injectivity and factorization explanations in Section 2 above
could usefully be added to a formal manuscript for completeness.

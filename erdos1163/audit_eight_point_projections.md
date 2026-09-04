# Independent audit: all class-two exponent-four groups with small orbits

4 September 2026. Scope: extension_eight_point_projections.md.

**Conclusion:** The mathematical argument passes independent audit.
Together with the independently exhaustive finite certificate in
degree8_classification_certificate.md, it proves that the saturated
family \(Q_n\) has exponentially small complement within the entire
class of 2-subgroups of class at most two, exponent dividing four,
and orbit sizes at most eight.

## The ID10 enlargement resolves the dependency issue

For a group with square map \((Y^2,XY)\), embedding it in
\(C_4\times D_8\) by identifying the cyclic quotient coordinate with
the second dihedral quotient coordinate is valid. The enlarged group
has independent central coordinates and one extra quotient coordinate.
Every original subdirect subgroup remains subdirect onto both virtual
factors. Thus the enlarged subgroup count is an upper bound, while
the physical eight-point budget retains a positive deficit of one.

This is preferable to a direct per-form argument: declaring \(Y^2\)
dependent while \(XY\) is a chosen basis form can produce coupled
constraints across blocks. The written proof avoids that issue
entirely. It does not use the earlier proposed stronger local saving.

## Local representations and sequential counting

For a scalar nonabelian square coordinate, fixing its alternating
form fixes the essential two- or four-dimensional support. There are
six rank-two representations and 720 rank-four symplectic
representations. Any radical coordinates can be chosen freely,
because further square constraints are being discarded.

For an ID18 block with forms \(X\wedge Y,X\wedge Z\), a basis subset
omitting exactly one coordinate leaves \(X\) and the other coordinate
variable known. Prescribing the missing wedge then determines its
remaining variable modulo \(\langle X\rangle\). If both coordinates
are omitted, their distinct support planes determine their common
line \(\langle X\rangle\), and each remaining variable is determined
modulo that line. This gives respectively the stated bounds
\(2^{2k+s+1}\) and \(4\cdot2^{2s}\).

The choice order is legitimate: each block's variables used by
independent polar coordinates are chosen first; missing variables
are not used by any other independent coordinate. Thus the global
span is known before the dependent coordinates are filled in.
Summing these bounds gives exactly
\[
2^{kr}\binom{\nu}{h}C^h
2^{-h(2k-\nu+h)+kv},
\]
with \(v\leq b,h\). Pure cyclic variables are independent of all the
polar-coordinate variables after the ID10 enlargement, so their
annihilator constraints genuinely save \(kp\) binary parameters.

## Defects and completed-square estimates

All the contribution inequalities in (3) and (4) check factor by
factor, including the virtual factor. In particular
\[
c\leq D,\quad D+b\leq M/2,\quad
r-\nu\geq M/4,\quad
r/2-\nu-c\geq A-(b+c)/2.
\]

The central-complement count remains exactly \(2^{k(p+q)}\).
Including the \(kv\) bonus is equivalent to replacing the linear
rank parameter \(r\) by \(R=r+v\), without changing the quadratic
term in \(k\). I independently expanded (7); it is correct.

With \(\delta=b-v\), \(L=D+\delta\), the estimates
\[
R=M-L,\qquad \delta+c\leq L,\qquad L\leq M/2
\]
justify the passage from (7) to (8). In detail, the cross term obeys
\[
-3q^2/4+qL/2\leq-q^2/2+L^2/4,
\]
and the positive terms satisfy \(L^2/2\leq ML/4\) and
\(c^2/4\leq ML/8\). These give exactly the loss
\[
-M(D+\delta)/8-q^2/2-qA-uM/4.
\]
The remaining polynomial and binomial factors can be absorbed with
uniform cost \(2^{O(\log^2M)}\), retaining (10).

## Uniform decay and summation

The constraint \(\delta+q+u\geq b\) supplies the needed \(b^2\)
penalty. For \(D\geq1\), the \(MD\) term supplies an additional
linear \(M\) loss. For \(D=0\), integrality supplies it whenever
\(\delta+u\geq1\).

In the remaining case, averaging the genuine four-point dihedral
choices gives precisely (12). The comparison with
\(\beta(M-4b)/2\) is valid because
\[
a/2+e_{\mathrm{good}}+\beta\ell
\geq \beta a/2+2\beta e_{\mathrm{good}}+\beta\ell,
\qquad 2\beta<1.
\]
If \(b\) is small this supplies a linear \(M\) loss; if \(b>M/8\),
its square penalty supplies both the required \(M\) and \(b^2\)
losses. Splitting fixed fractions of the penalties makes (11)
uniform in all cases.

Finally, every other defective block contributes at least one to
\(D\), while there are only fixed finite numbers of labelled local
choices. The placement bounds \((CM)^j,(CM)^b\), geometric \(j\)-sum,
and Gaussian \(b\)-sum give (13). Extending the upper sum to include
the empty defect configuration only increases its right-hand side.
The efficient configuration and extra fixed points are correctly
handled by the earlier audited estimates.

## Finite input and scope

The finite list no longer needs a bare appeal to the completeness of
the GAP transitive-group database. The separate standard-library
enumeration finds every relevant subgroup of an explicit Sylow
2-subgroup of \(S_8\), and provides verified conjugators to the nine
listed models. Their needed ranks and the ID10/18 square maps are
also independently verified from permutations.

No substantive correction to the written asymptotic proof was needed.
The resulting theorem is still restricted to class at most two,
exponent dividing four, and orbit sizes at most eight. In particular,
it does not control the higher-class or exponent-eight projection
types or larger orbits.

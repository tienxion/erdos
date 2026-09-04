# A real Grünbaum–Rigby incidence seed for the two-chain expansion

This is a point-line seed and a test for the leading convexity conditions in a
restricted construction attempt for Erdős #97. It is not a convex unit-distance
configuration, a deformation theorem, or a solution of #97.

## Primary sources and exact seed

Gévay, Kiss and Pisanski identify the Grünbaum–Rigby configuration with
\(\mathrm K(7;2,3)\). Their Section 2, Lemma 3 gives the regular-polygon
similarities used below; Theorem 6 ensures this case has no extra incidences.
[The Grünbaum–Rigby configuration as a special Kárteszi configuration](https://arxiv.org/html/2512.18872v1)

Berman, Gévay, Richter-Gebert and Tabachnikov prove that this configuration
belongs to a family with two nonprojective degrees of freedom. The formula
below is its symmetric member, not a parametrization of those motions.
[When Grünbaum meets Poncelet](https://arxiv.org/abs/2408.09203)
The authors also provide a [construction of a Poncelet heptagon](https://mathvisuals.org/Poncelet/widgets/7gonConstruction/7Gon.html),
a [configuration applet](https://mathvisuals.org/Poncelet/widgets/Configurator/Configurator.html),
and the companion paper [Explicit Constructions for Poncelet Polygons](https://arxiv.org/abs/2408.09225).

All indices below are modulo 7. Set
\[
\zeta=e^{2\pi i/7},\qquad
s_k=\frac{\cos(k\pi/7)}{\cos(\pi/7)},\qquad
\phi_k(z)=s_ke^{(k-1)\pi i/7}z.
\]
The 21 points are
\[
A_j=\zeta^j,\qquad D_j=\phi_2(A_j),\qquad B_j=\phi_3(A_j).
\]
The 21 lines, specified by their four incident points, are
\[
\begin{aligned}
L_j&:\quad A_j,\ A_{j+2},\ D_j,\ D_{j+1},\\
M_j&:\quad A_j,\ A_{j+3},\ B_j,\ B_{j+1},\\
N_j&:\quad B_j,\ B_{j+2},\ D_j,\ D_{j+3}.
\end{aligned}
\tag{1}
\]

These incidences can also be checked directly, without any numerical
calculation. The line through two unit-circle points of arguments
\(2j\pi/7\) and \((2j+2k)\pi/7\) has equation
\[
x\cos((2j+k)\pi/7)+y\sin((2j+k)\pi/7)=\cos(k\pi/7).
\]
Substitution gives the four incidences on \(L_j\) and \(M_j\).
For \(N_j\), applying \(\phi_3\) to \(L_j\) and \(\phi_2\) to \(M_j\)
produces the same line: its normal angle is \((2j+4)\pi/7\) and its
offset is \(\cos(2\pi/7)\cos(3\pi/7)/\cos(\pi/7)\).
Thus the displayed incidences are exact. Counting (1) gives degree four
at every point as well as on every line.

For implementation, the three line families have equations
\[
a x+b y=h,\qquad a=\cos\theta,\quad b=\sin\theta,
\]
with the following data.

| Family | \(\theta\) | \(h\) |
|---|---|---|
| \(L_j\) | \((2j+2)\pi/7\) | \(\cos(2\pi/7)\) |
| \(M_j\) | \((2j+3)\pi/7\) | \(\cos(3\pi/7)\) |
| \(N_j\) | \((2j+4)\pi/7\) | \(\cos(2\pi/7)\cos(3\pi/7)/\cos(\pi/7)\) |

## A finite projective chart

The regular seed has parallel line classes, so an affine chart cannot give
21 distinct line slopes. Use instead the exact rational projective map
\[
V=\frac{x+2y}{1+x/10+y/13},\qquad
W=\frac{3x+5y}{1+x/10+y/13}.
\tag{2}
\]
Its homogeneous matrix is
\[
H=\begin{pmatrix}1&2&0\\3&5&0\\1/10&1/13&1\end{pmatrix},
\qquad \det H=-1.
\]
All original points have norm at most one, so their denominators in (2)
are at least \(1-\sqrt{1/100+1/169}>0\).

For the line \(a x+b y=h\), define
\[
\beta=2a-b+\frac{8h}{65},\qquad
Y=\frac{5a-3b+7h/26}{\beta},\qquad C=\frac h\beta .
\tag{3}
\]
Then its equation in this chart is \(W=YV+C\).
Indeed, writing \(d=1+x/10+y/13\), the inverse relations are
\[
x=d(-5V+2W),\quad y=d(3V-W),\quad
d^{-1}=1+\frac7{26}V-\frac8{65}W,
\]
which give (3) by substitution.

The reproduction script is [grunbaum-rigby-seed.py](grunbaum-rigby-seed.py);
its numerical output is [grunbaum-rigby-seed.json](grunbaum-rigby-seed.json).
The JSON has original coordinates, chart point data \((V,W)\), line
data \((Y,C)\), and all 84 incidence pairs as
\([\text{line index},\text{point index}]\). The point order is
\(A_0,\ldots,A_6,D_0,\ldots,D_6,B_0,\ldots,B_6\); the line order is
\(L_0,\ldots,L_6,M_0,\ldots,M_6,N_0,\ldots,N_6\).

The script checks every one of the 441 point-line pairs in double precision.
For this chart the maximum incident residual was \(2.52\cdot10^{-15}\);
the minimum nonincident residual was \(0.04254\), the minimum difference
between point abscissae \(0.02688\), and the minimum difference between line
slopes \(0.005183\). These are numerical consistency checks, not interval
certificates. Exact incidences follow from the formulas above.

## Relation to the proposed unit-distance expansion

Give a line \((Y_i,C_i)\) and a point \((V_j,W_j)\) the lifted coefficients
\[
X_i=C_i+\frac{Y_i^2}{2},\qquad
U_j=W_j-\frac{V_j^2}{2}.
\]
Set
\[
\mathcal A_i=(-1/2+\epsilon^2X_i,\epsilon Y_i),\qquad
\mathcal B_j=(1/2+\epsilon^2U_j,\epsilon V_j).
\]
An exact calculation gives
\[
\|\mathcal B_j-\mathcal A_i\|^2-1
=\epsilon^2\bigl(2(U_j-X_i)+(V_j-Y_i)^2\bigr)
 +\epsilon^4(U_j-X_i)^2.
\]
The coefficient of \(\epsilon^2\) vanishes exactly when
\(W_j=Y_iV_j+C_i\). The generally nonzero \(\epsilon^4\) term remains.
Incidence preservation under a projective map therefore does not itself
produce a unit-distance deformation.

## Exact test for the two leading convex chains

The following test was derived independently within this investigation.
It applies to any fixed chart with distinct point abscissae and line slopes.
Write the standard second divided difference as
\[
[f_0,f_1,f_2]_{t_0,t_1,t_2}
=\frac{(f_2-f_1)/(t_2-t_1)-(f_1-f_0)/(t_1-t_0)}
 {t_2-t_0}.
\]
Sort the points by \(V\), the lines by \(Y\), and set
\[
\mathscr C=\max_j[W_j,W_{j+1},W_{j+2}]_{V_j,V_{j+1},V_{j+2}},
\qquad
\mathscr D=\min_i[C_i,C_{i+1},C_{i+2}]_{Y_i,Y_{i+1},Y_{i+2}}.
\]
Apply a further scaling \((V,W)\mapsto(aV,cW)\), where \(a,c>0\),
and put \(\lambda=c/a^2\). The largest point second divided difference
becomes \(\lambda\mathscr C\); the smallest dual one becomes
\(\mathscr D/\lambda\). Since the second divided difference of \(t^2/2\)
is \(1/2\), the lifted point chain \(U(V)\) is strictly concave and the
lifted line chain \(X(Y)\) is strictly convex exactly when
\[
\lambda\mathscr C<\frac12,\qquad
\frac{\mathscr D}{\lambda}>-\frac12.
\tag{4}
\]
For a genuine \(n_4\) configuration in such a chart one necessarily has
\(\mathscr C>0>\mathscr D\), as proved below. Consequently (4) is feasible
if and only if
\[
-4\mathscr C\mathscr D<1,
\qquad
-2\mathscr D<\lambda<\frac1{2\mathscr C}.
\tag{5}
\]
This gives a chart test, not a projectively invariant existence theorem:
each projective change must be followed by fresh ordering and calculation
of the two extrema.

To justify the strict signs, suppose \(\mathscr C\leq0\).
The piecewise linear interpolant of all points in increasing abscissa is
concave. Three collinear data points force this interpolant to be affine
on their full span: the nonincreasing consecutive slopes have equal
averages on the two subintervals and therefore are all equal.
Choose a configuration line with four points, and choose one of its two
middle points \(p\). Thus both immediate data neighbors of \(p\) lie on
that line. Any second configuration line through \(p\) has at least three
data points; its whole span is also affine. On at least one side of \(p\)
it contains an immediate neighbor of \(p\), forcing the two lines to be
identical. This contradicts four distinct configuration lines through
\(p\). Hence \(\mathscr C>0\).
If \(\mathscr D\geq0\), apply the same argument to the convex dual chain
\((Y_i,C_i)\): each original point gives the dual line
\(C=W_j-V_jY\), with four dual points. This gives the contradiction
and proves \(\mathscr D<0\).

No chart satisfying (5), and no exact positive-\(\epsilon\) unit-distance
lift, is asserted in this note.

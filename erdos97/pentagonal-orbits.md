# Regular pentagon orbit restrictions for Erdős problem 97

These are restrictions on one construction ansatz. They do **not** settle Erdős problem 97.

Let \(\zeta=e^{2\pi i/5}\), \(\phi=(1+\sqrt5)/2\), and
\[
 S=2\sin(\pi/5),\qquad L=2\sin(2\pi/5)=\phi S.
\]
Thus \(S^2=(5-\sqrt5)/2\), \(L^2=(5+\sqrt5)/2=1+\phi^2\), and
\[
 R=\sec(\pi/5)=2/\phi,\qquad R^2-1=(L-S)^2=5-2\sqrt5.
\]
Consider distinct orbits \(O(z)=\{z\zeta^k:0\leq k<5\}\) whose union is in strictly convex position. An orbit may choose either its short chord \(S|z|\) or its long chord \(L|z|\) as the distance to be repeated four times. Each choice already supplies two points of its own orbit.

## 1. The radius ratio

An outer regular pentagon of circumradius \(r_{\max}\) contains the closed disk of radius \(r_{\max}\cos(\pi/5)\). Consequently strict convexity implies
\[
 r_{\max}/r_{\min}<R.
\]
Equality is also forbidden: a vertex of the inner orbit would lie inside the outer pentagon or on one of its edges.

## 2. No short chord has an external match

Normalize one source orbit to \(O(1)\). Write another as \(O(re^{i\delta})\), with \(0<\delta<2\pi/5\), and put \(h=\pi/5\), \(\beta=\delta-h\). Aligned orbits cannot be distinct in a strictly convex union: all vertices of the smaller one lie in the larger pentagon.

Each source vertex must be outside the corresponding edge of the target pentagon, and conversely. The supporting lines give the necessary inequalities
\[
 r_-:=\frac{\cos h}{\cos\beta}<r<r_+:=\frac{\cos\beta}{\cos h}.
\]
The two target points of arguments \(\delta\) and \(\delta-2h\) will be called near points; the other three are far points.

At \(r=r_-\), each target vertex lies in the relative interior of a source edge. Both near points are on edges incident with 1, so their distances from 1 are strictly less than \(S\). Each far point has distance strictly greater than \(S\). Indeed, along the source edge from \(\zeta\) to \(\zeta^2\), squared distance from 1 strictly increases from \(S^2\): its initial derivative is positive because
\(\operatorname{Re}((\zeta-1)\overline{(\zeta^2-\zeta)})=S^2\cos(2h)>0\).
The reflected edge is the same. The remaining opposite edge has real coordinate \(-\cos h\), so its distance from 1 is at least \(1+\cos h>S\).

The cosine of the argument of each far point is at most \(\cos(2h)\), whereas \(r\geq r_-\geq\cos h>\cos(2h)\). Its squared distance
\(1+r^2-2r\cos\alpha\) therefore strictly increases with \(r\). All far points continue to have distance greater than \(S\).

At \(r=r_+\), the source point 1 lies on the edge joining the near target points. Rotating this edge by \(-\beta\), the two distances from 1 to its endpoints are
\[
 r_+\sin h\pm\sin\beta
 =\frac{\sin(h\pm\beta)}{\cos h}<\frac{\sin(2h)}{\cos h}=S,
\]
because \(0<h\pm\beta<2h<\pi/2\). For either fixed near argument, squared distance is convex in \(r\); since it is less than \(S^2\) at both endpoints of \([r_-,r_+]\), it remains less than \(S^2\) throughout that interval.

Thus no external point is at distance \(S\) from 1. Any successful construction in this ansatz must use the long chord in every orbit.

## 3. An external orbit supplies at most one long match

If two points of a target pentagon are equidistant from the source point 1, their arguments are negatives modulo \(2\pi\). The relative phase of the two pentagons is consequently either 0 or \(h\), modulo \(2h\). Phase 0 is impossible by strict convexity. At phase \(h\), the possible equal-distance pairs have arguments \(\pm h\) or \(\pm3h\).

For the pair at \(\pm h\), the long-distance equation is
\[
 r^2-\phi r-\phi^2=0,
\]
whose positive root is \(\phi^2>R\). For the pair at \(\pm3h\), it is
\[
 r^2+\phi^{-1}r-\phi^2=0.
\]
This polynomial is increasing for positive \(r\) and is negative at \(R=2/\phi\), since its value there is \((6-\phi^4)/\phi^2<0\). Its positive root also exceeds \(R\). Both contradict the radius ratio bound.

Hence each source needs matches in at least two distinct external orbits.

## 4. A fifth-power distance identity

For the now mandatory long choice, write \(t_i=|z_i|^2\), \(w_i=z_i^5\), and put
\[
 C=\frac{125+55\sqrt5}{2},\qquad
 Q(x,y)=x^2-\phi^{-1}xy+\phi^{-4}y^2.
\]
There is a directed match \(i\to j\) exactly when
\[
 |w_j-w_i|^2=Ct_i(t_i-t_j)^2Q(t_i,t_j). \tag{1}
\]
To verify this, set \(x=t_i,y=t_j,s=y-\phi^2x,u=xy\). The product of the five expressions
\(|z_i-\zeta^kz_j|^2-L^2x\) is
\[
 s^5-5us^3+5u^2s-2\operatorname{Re}(w_j\overline{w_i}).
\]
Factoring \(x^5+y^5-(s^5-5us^3+5u^2s)\) gives the right side of (1).

Swapping \(x,y\), the difference of the two right sides of (1) is
\[
 C(x-y)^3\bigl(x^2+(\sqrt5-2)xy+y^2\bigr). \tag{2}
\]
Thus two distinct orbits cannot have directed matches in both directions: (2) forces \(x=y\), and (1) then forces \(w_i=w_j\), which is the same orbit. In fact any matched pair of distinct orbits has unequal radii.

## 5. A triangle cannot have its largest orbit pointing to its smallest

For \(z>x>0\), define
\[
 M(z,x)=\sqrt C\,(z-x)\sqrt{zQ(z,x)}.
\]
By (1) and (2), the distance between the lifted points of any matched pair of squared radii \(x<z\) is at most \(M(z,x)\), with equality when the larger source points to the smaller.

The factor \(F(z,x)=\sqrt C\sqrt{zQ(z,x)}\) strictly increases with \(z\) and strictly decreases with \(x\) on \(z\geq x>0\). Indeed,
\[
 \partial_z(zQ)=3z^2-2\phi^{-1}zx+\phi^{-4}x^2>0,
\]
and
\[
 \partial_x Q=-\phi^{-1}z+2\phi^{-4}x<0.
\]
Consequently, for \(x<y<z\),
\[
 M(z,x)=(z-y)F(z,x)+(y-x)F(z,x)
 >M(z,y)+M(y,x).
\]
If all three orbit pairs are matched and the largest orbit points to the smallest, this contradicts the triangle inequality for their fifth-power lifts.

## 6. A triangle cannot have its smallest orbit pointing to both others

Normalize the smallest source to 1. A matched representative \(q=x+iy\) of a larger orbit satisfies
\[
 |q-1|=L,\qquad x=(|q|^2-\phi^2)/2,\qquad 1<|q|<R.
\]
The upper representatives trace a short arc \(\Gamma\) starting at \(\zeta^2\) as the radius increases from 1. The lower representatives are its reflection.

For every upper representative, \(q'=\zeta^{-2}q\) has real part greater than 1 and imaginary part less than 0. For a direct verification, this rotated arc lies on the circle centered at \(\zeta^{-2}\) of radius \(L\). That circle meets the line \(\operatorname{Re}q'=1\) only at 1 and \(1-iS\). The latter has squared norm \(1+S^2>R^2\). The arc leaves 1 into the right half-plane: differentiating \(q=x+i\sqrt{L^2-(x-1)^2}\) at \(q=\zeta^2\) gives \(\operatorname{Re}(\zeta^{-2}dq/dx)=1>0\). Its imaginary part is negative because the argument of \(q\) decreases from \(4\pi/5\). Reflection gives the corresponding upper-right point for every lower representative.

Two matched representatives on opposite arcs would therefore provide two rotated target vertices to the right of 1, one above and one below the real axis. Their connecting segment meets the real axis to the right of 1. Joining that intersection to
\(M=(\zeta^2+\zeta^3)/2=-\cos h\)
puts 1 in the convex hull of other vertices, a contradiction. All matches from the smallest source must consequently use the same arc; reflect to take it to be \(\Gamma\).

Let \(q_*\) be the upper endpoint at radius \(R\). The arc is shorter than a semicircle, so its diameter is its endpoint chord. The rotated real-part inequality proved above gives
\[
 |q_*-\zeta^2|^2=R^2+1-2\operatorname{Re}(\zeta^{-2}q_*)
 <R^2-1=(L-S)^2.
\]
Thus for any two representatives \(b,c\in\Gamma\),
\[
 |b-c|<L-S<(L-S)|b|. \tag{3}
\]
The representatives cannot be matched with rotation 0 or \(\pm1\), since
\[
 |c-\zeta^{\pm1}b|\leq|c-b|+S|b|<L|b|.
\]
For rotation \(k=\pm2\), the two circles centered at 1 and \(\zeta^kb\), of radii \(L\) and \(L|b|\), respectively, already have the two distinct intersections
\[
 b\quad\hbox{and}\quad E_k=-\phi^2\zeta^k.
\]
Indeed \(|b-\zeta^kb|=L|b|\), while
\(|E_k-\zeta^kb|=|b+\phi^2|=L|b|\), using \(|b-1|^2=L^2\); also \(|E_k-1|=L\). Their centers differ because \(|b|>1\). Hence there is no other intersection. The point \(E_k\) has norm \(\phi^2>R\), and \(c\ne b\). Thus \(b\to c\) is impossible. Interchanging \(b,c\) excludes the opposite direction as well.

## 7. Proposed reverse-cycle uniqueness lemma — pending independent audit

The following proof is recorded for independent algebraic and geometric audit. Do not use its conclusion in a claimed finite exclusion until that audit is complete.

Fix two orbits \(A,C\), with \(|A|<|C|\) and \(A\to C\). There is at most one orbit \(B\) with intermediate radius such that
\[
 A\to C\to B\to A
\]
and the three orbits have strictly convex union.

Normalize \(A=1\), and reflect so the matched representative \(q=x+iy\) of \(C\) is on the upper arc in Section 6. Set \(r=|q|\), \(a=\phi^{-2}\), \(T=La\), \(e=\sin h\), and \(d=\cos h=\phi/2\). Then
\[
 x=(r^2-\phi^2)/2,\qquad y=\sqrt{L^2-(x-1)^2},\qquad 1<r<R.
\]
Choose the representative \(b\) matched from \(q\). The other condition \(B\to A\) puts it on one of the five circles
\[
 |b-q|=Lr,\qquad |b+a\zeta^k|=T,\qquad 0\leq k<5. \tag{4}
\]

First, only \(k=2\) can yield an intersection. The argument of \(q\) lies strictly between \(3h\) and \(4h\). The lower bound follows from
\[
 \frac{x}{r}\leq\frac{R^2-\phi^2}{2R}
 =\frac{2-3\phi}{4\phi}< -\frac1{2\phi}=\cos(3h).
\]
Of the five center distances \(|q+a\zeta^k|\), the largest is therefore \(k=2\) and the second largest is \(k=1\). It suffices to prove
\[
 |q+a\zeta|<Lr-T.
\]
Put
\[
 H(r)=\frac{5\phi^2}{2}r^2-2L^2r+\frac{L^2}{2}.
\]
Expanding the squares, the claimed inequality is equivalent to
\(2\sin(2h)y<H(r)\). Now \(H(1)=\sqrt5/2>0\) and \(H\) increases for \(r\geq1\). Direct expansion gives
\[
\begin{aligned}
H(r)^2-4\sin^2(2h)y^2
  = (r-1)^2\bigg[&\frac{45+19\sqrt5}{2}(r-1)^2\\
                &+(40+18\sqrt5)(r-1)
                 +\frac{45+21\sqrt5}{2}\bigg]>0.
\end{aligned}
\]
This proves the strict separation of the other four circles.

For the remaining circle, rotate (4) by \(\zeta\). Its small center is
\(h_0=-a\zeta^3=a e^{ih}\), its radius is \(T\), and the large center is \(Q=\zeta q\), with radius \(Lr\). Write
\[
 h_0-Q=\nu e^{i\alpha},\qquad 0<\alpha<h.
\]
Indeed \(Q\) is in the third quadrant, and rotating \(h_0-Q\) by \(-h\) gives negative imaginary part because the argument of \(e^{ih}q\) is between \(4h\) and \(5h=\pi\).

Parametrize the small circle by \(s(t)=h_0+Te^{it}\). Its portion to the right of the line \(\operatorname{Re}s=1\) is exactly the open arc
\[
 -h/2<t<h/2,
\]
with endpoints \(s(-h/2)=1\) and \(s(h/2)=U=1+2iae\). Its interior has positive imaginary part.

The point 1 is strictly inside the large circle. To verify this, let
\(G(x)=|1-\zeta q|^2-L^2r^2\), viewing \(y=\sqrt{L^2-(x-1)^2}\). Then
\[
 G(-d)=0,\qquad
 G'(x)=-(2\phi^2+\phi^{-1})+2\phi e\frac{1-x}{y}.
\]
The derivative equals zero at \(x=-d\) and strictly decreases thereafter, since \((1-x)/y\) strictly decreases. Hence \(G(x)<0\) for the present \(x>-d\).

We also need the implication
\[
 \alpha\geq h/2\quad\Longrightarrow\quad
 F(x):=|U-Q|^2-L^2r^2>0. \tag{5}
\]
Here
\[
 \alpha\geq h/2\quad\Longleftrightarrow\quad
 u(x):=dx+ey\leq\frac1{2\phi^3},
\]
and
\[
 F(x)=10-7\sqrt5-3\sqrt5x+(5-\sqrt5)ey.
\]
The function \(u\) strictly increases in the relevant interval. At \(x_0=-3/5\), we have \(y_0^2=(25\sqrt5-3)/50\), and
\[
 e^2y_0^2-\left(\frac1{2\phi^3}+\frac{3d}{5}\right)^2
 =\frac{285\sqrt5-637}{200}>0.
\]
Both terms being compared before squaring are positive, so \(u(x_0)>1/(2\phi^3)\). Thus the left side of (5) implies \(x<x_0\).

Meanwhile \(F\) strictly decreases: its derivative at \(-d\) is \(5-3\sqrt5<0\), and the only nonconstant part of that derivative is a positive multiple of the decreasing function \((1-x)/y\). At \(x_0\),
\[
 (5-\sqrt5)^2e^2y_0^2-
 \left(\frac{26\sqrt5}{5}-10\right)^2
 =\frac{1171\sqrt5-2617}{10}>0.
\]
Again the compared quantities are positive, proving \(F(x_0)>0\), and hence (5). The two displayed strict radical inequalities can be checked by squaring positive integers: \(5\cdot285^2>637^2\) and \(5\cdot1171^2>2617^2\).

If the two circles intersect, the points of the small circle outside the large circle form an angular arc centered at \(\alpha\), say with half-length \(\psi\); tangency allows \(\psi=0\). Since \(s(-h/2)=1\) is strictly inside, the lower intersection parameter is
\[
 \ell=\alpha-\psi>-h/2.
\]
If \(\alpha<h/2\), then immediately \(\ell<h/2\). If \(\alpha\geq h/2\), (5) makes \(U=s(h/2)\) strictly outside, again giving \(\ell<h/2\). Thus at least one intersection lies on the open cap to the right of 1, with positive imaginary part.

That intersection is a rotated vertex of its candidate \(B\) orbit. Section 6 already supplies a rotated vertex of \(C\) to the right of 1 with negative imaginary part. Together with \((\zeta^2+\zeta^3)/2=-d\), they put 1 in the convex hull of other vertices. This candidate cannot be part of a strictly convex union. Since there were at most two circle intersections in total, at most one admissible \(B\) remains. This includes the tangent case, where the sole intersection is excluded.

## Consequences and limitations

In a triangle of pairwise matched orbits with squared radii \(a<b<c\), only the following two orientations can remain:

- \(b\to a,\ a\to c,\ b\to c\);
- \(b\to a,\ a\to c,\ c\to b\).

Any counterexample formed by the present pentagon ansatz needs at least six distinct orbits, hence at least 30 vertices. To see this, choose exactly two external outgoing matches from every orbit. There are no directed 2-cycles, so at least five orbits are needed. With exactly five, every unordered pair must carry one edge. Order the radii increasingly; all are distinct because every pair is matched. The largest orbit cannot point to any orbit other than its immediate predecessor, because an intermediate orbit would make a forbidden triangle from Section 5. Its required outdegree two is impossible.

No claim is made here that six or more pentagon orbits are impossible, or that these restrictions suffice for realization. The two triangle restrictions and reverse-cycle completion uniqueness give the same abstract necessary graph conditions obtained separately for equilateral orbits; any transfer of finite graph exclusions should explicitly check those conditions and the treatment of equal radii.

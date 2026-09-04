# Convex equilateral orbits: two local obstructions

These statements concern a restricted construction for Erdős problem #97. They do **not** settle that problem or exclude every finite configuration in this construction.

Let \(\omega=e^{2\pi i/3}\). An orbit is
\[
\mathcal O(z)=\{z,\omega z,\omega^2z\},\qquad z\ne0.
\]
Assume a finite union of distinct orbits is in strict convex position: every point is an extreme point of their convex hull. Write \(A\to B\) when some point of \(\mathcal O(B)\) is at distance \(\sqrt3|A|\) from \(A\). This is independent of the representative chosen for either orbit. The two other members of \(\mathcal O(A)\) are already at that distance from \(A\).

## Preliminary geometry

The ratio of the largest to smallest orbit radius is less than \(2\). Indeed, an equilateral triangle of circumradius \(R\) contains the closed disk of radius \(R/2\). A point of another orbit at distance at most \(R/2\) from the common center would therefore not be extreme.

Normalize an orbit to \(A=1\). Suppose \(A\to Q\), where \(1<|Q|<2\), and choose its representative \(q=x+iy\) satisfying \(|q-1|=\sqrt3\). Reflect the entire configuration if necessary to arrange \(y>0\). Set \(r=|q|\). Then
\[
1<r<2,\qquad x=\frac{r^2-2}{2}\in(-1/2,1),
\qquad y^2=3-(x-1)^2=-\frac{r^4}{4}+2r^2-1.
\tag{1}
\]
In particular \(\arg q\in(\pi/3,2\pi/3)\). Also
\[
y^2-3x^2=3y^2-(x+2)^2=-2(2x+1)(x-1)>0.
\tag{2}
\]
It follows that \(q'=\omega^2q\) satisfies
\[
\Re q'>1,\qquad \Im q'<0.
\tag{3}
\]
For the real part, use \(\sqrt3y>x+2\). For the imaginary part, use \(y>-\sqrt3x\), which is immediate when \(x\ge0\), and follows from (2) when \(x<0\). The reflected version says that a lower-half-plane match can be rotated into \(\Re z>1,\Im z>0\).

Consequently, if \(A=1\) has matches into two larger-radius orbits, their matched representatives must lie in the same half-plane. Otherwise the two rotated representatives lie strictly to the right of \(1\), on opposite sides of the real axis. Their segment crosses that axis to the right of \(1\). The point \(1\) then lies inside the triangle formed by these two points and \(-1/2=(\omega+\omega^2)/2\), contradicting extremality. This argument uses only points other than \(1\).

Distinct equal-radius orbits cannot have a match: after normalizing their common radius to \(1\), a matched representative must satisfy \(|q-1|=\sqrt3\) and \(|q|=1\), hence \(q=\omega\) or \(q=\omega^2\), the same orbit.

## Lemma 1: the smallest orbit cannot send to both other members of a triangle

Suppose three distinct orbits form an undirected triangle of matches. The smallest-radius orbit cannot send matches to both other orbits.

**Proof.** Normalize the smallest orbit to \(A=1\), and suppose \(A\to B\) and \(A\to C\). By the preceding observation their radii exceed \(1\), and they are less than \(2\). Their matched representatives \(b,c\) lie on the same half of the circle
\[
S=\{z:|z-1|=\sqrt3\}.
\]
Reflect to make that half the upper half-plane. Both representatives then lie in the open arc from \(\omega\) to \(E_+=1+i\sqrt3\). This arc subtends an angle of \(\pi/3\) at the center \(1\). Hence
\[
|b-c|<\sqrt3.
\]
This rules out a match between these representatives in either direction, because both source radii exceed \(1\).

For a rotated match from \(B\) to \(C\), equivalently \(c\) would belong to the circle centered at \(\omega b\) or \(\omega^2b\), with radius \(\sqrt3|b|\). The first of those circles intersects \(S\) exactly at \(b\) and \(E_-=1-i\sqrt3=-2\omega\). Indeed,
\[
|b-\omega b|=\sqrt3|b|,
\qquad |E_--\omega b|=|b+2|=\sqrt3|b|,
\]
where the last equality follows from \(|b-1|^2=3\). These are distinct intersection points since \(|b|<2=|E_-|\). The two circles have different centers, so there can be no third intersection. Similarly the circle centered at \(\omega^2b\) intersects \(S\) exactly at \(b\) and \(E_+\). Since \(C\) is a different orbit and \(|c|<2\), neither possibility allows a match. Interchanging \(b,c\) rules out the opposite direction as well. This contradicts the assumed triangle. \(\square\)

Together with the cubic-lift triangle inequality established separately, this leaves only two possible orientations for a triangle whose radii satisfy \(a<b<c\):
\[
b\to a,\quad a\to c,\quad b\to c;
\qquad\text{or}\qquad
b\to a,\quad a\to c,\quad c\to b.
\]
The first pattern does occur in strictly convex configurations, so it must not be discarded.

## Lemma 2: a convex reverse cycle has a unique completion between its extreme radii

Fix distinct orbits \(A,C\), with \(|A|<|C|\) and \(A\to C\). There is at most one orbit \(B\) satisfying
\[
|A|<|B|<|C|,\qquad A\to C\to B\to A,
\]
for which the union of these three orbits is in strict convex position.

**Proof.** Normalize \(A=1\). Choose \(q\in\mathcal O(C)\) as in (1), with \(|q-1|=\sqrt3\) and \(\Im q>0\). Choose the representative \(b\) so that \(|b-q|=\sqrt3r\). The relation \(B\to A\) says
\[
|b-\omega^k|=\sqrt3|b|\quad\text{for some }k\in\{0,1,2\},
\]
or equivalently
\[
\left|b+\frac{\omega^k}{2}\right|=\frac{\sqrt3}{2}.
\tag{4}
\]

Only \(k=1\) can occur. For \(k=0\), the squared distance between the centers \(q,-1/2\), minus the squared difference of their radii \(\sqrt3r,\sqrt3/2\), is
\[
-\frac32(r-1)^2<0.
\]
Thus those circles do not intersect. For \(k=2\), the same difference is
\[
H-\frac{\sqrt3y}{2},\qquad H=3r-\frac94r^2.
\]
For \(r\ge4/3\) this is negative immediately. For \(1<r<4/3\), we have \(H>0\), and
\[
\frac34y^2-H^2
=-\frac34(r-1)(7r^3-11r^2-r-1)>0,
\]
since \(7r^3-11r^2-r-1=r^2(7r-11)-r-1<0\). Hence the difference is negative also in this range.

Rotate \(b\) to \(b'=\omega b\). The candidate points are now intersections of
\[
S_0:\quad |z-h|=R,
\qquad h=\frac14+i\frac{\sqrt3}{4},\quad R=\frac{\sqrt3}{2},
\]
with the circle centered at \(Q=\omega q\) of radius \(\sqrt3r\). There are at most two intersections. We prove that at least one intersection, whenever intersections exist, makes \(A\) non-extreme.

Write
\[
h-Q=\nu e^{i\phi}.
\]
Its real and imaginary parts are
\[
\frac14+\frac{x}{2}+\frac{\sqrt3y}{2},
\qquad
\frac{\sqrt3}{4}-\frac{\sqrt3x}{2}+\frac y2.
\]
Both are positive, and \(0<\phi<\pi/3\). For the upper bound, the difference \(\sqrt3\Re(h-Q)-\Im(h-Q)\) equals \(\sqrt3x+y>0\), by (2) when needed.

Parametrize \(S_0\) by \(s(t)=h+Re^{it}\). We have
\[
s(-\pi/6)=1,
\qquad s(\pi/6)=U:=1+i\sqrt3/2.
\]
The point \(1\) lies strictly inside the \(Q\)-circle, since
\[
|1-Q|^2-3r^2=-\frac32r^2+\sqrt3y<0;
\]
the last inequality follows from \(9r^4/4-3y^2=3(r^2-1)^2>0\).

If the circles intersect properly, the arc of \(S_0\) outside the \(Q\)-circle has the form \(\phi-\psi<t<\phi+\psi\), where \(0<\psi<\pi\). Since \(s(-\pi/6)\) is strictly inside and \(0<\phi<\pi/3\), we obtain \(\psi<\phi+\pi/6\). Thus the lower intersection parameter \(L=\phi-\psi\) is greater than \(-\pi/6\).

We also have \(L<\pi/6\). This is immediate if \(\phi\le\pi/6\). If \(\phi>\pi/6\), direct comparison of the real and imaginary parts above gives \(x<1/4\), hence \(1<r^2<5/2\). In that range,
\[
|U-Q|^2-3r^2
=\frac94(1-r^2)+\frac{3\sqrt3}{2}y>0.
\]
To verify the inequality, put \(u=r^2\). The difference of squares of the positive quantities in question is
\[
y^2-\frac34(u-1)^2=-u^2+\frac72u-\frac74>0
\quad(1<u<5/2).
\]
This concave quadratic is positive at both endpoints. Therefore \(U\) lies outside the \(Q\)-circle, implying \(L<\pi/6\).

If the circles are tangent instead, the tangency point is \(s(\phi)\): strict containment of \(1\) rules out external tangency. The same calculation with \(U\) excludes \(\phi\ge\pi/6\), so the tangency point lies in the same open cap.

In either case, at least one candidate \(b'\) lies on
\[
\{s(t):-\pi/6<t<\pi/6\},
\]
so \(\Re b'>1\) and \(\Im b'>0\). By (3), \(q'=\omega^2q\) satisfies \(\Re q'>1\), \(\Im q'<0\). Their segment crosses the positive real axis strictly to the right of \(1\). Therefore \(1\) lies inside the triangle with vertices \(-1/2,q',b'\). Since \(-1/2=(\omega+\omega^2)/2\), this expresses \(1\) as a convex combination of other points in the three orbits, contradicting strict convexity.

At least one of the at most two candidates is forbidden. Thus at most one admissible orbit \(B\) remains. \(\square\)

## Limits of these results

These local lemmas constrain the directed graph of orbit matches. They do not by themselves exclude a directed graph of minimum outdegree two for every number of orbits. In particular, triangle-free graphs evade both triangle lemmas. A numerical near-solution or a graph satisfying these necessary conditions is not a geometric counterexample to Erdős #97.

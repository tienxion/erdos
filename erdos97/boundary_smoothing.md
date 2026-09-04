# Smoothing the boundary-contact construction: what follows and what does not

This note concerns Erdős #97 only. It does not construct a finite counterexample.

Primary input: [Bárány–Roldán-Pensado, A Question from a Famous Paper of Erdős, Discrete & Computational Geometry 50 (2013), 253–261](https://www.renyi.hu/~barany/cikkek/134.pdf). Theorem 1.1 and Section 3 supply a convex 15-gon K such that every P on its boundary is the center of a circle meeting the boundary in at least six distinct points. Section 4 defines transverse intersections and remarks that, in the absence of circular boundary arcs, the corresponding existence conditions agree. The smoothing and sampling arguments below are independent deductions from that input.

## Conclusion

There exists a real-analytic, strictly convex closed curve Γ of positive curvature such that **every P in Γ is the center of a circle meeting Γ in at least six differential-transverse points**. It can be chosen arbitrarily close to the published polygon, and with its threefold rotational symmetry.

This is stronger than retaining four boundary contacts, but it remains a boundary-contact assertion. It does not assert that the contact points belong to any prescribed finite vertex set.

## 1. Remove tangencies without losing the contact count

Fix a polygon K, a point P, and r>0 for which the circle S(P,r) meets ∂K in k distinct points. Parameterize ∂K continuously and consider its distance from P. A polygon has no circular arc, so the level set at r is finite.

At each level point the local distance function either crosses r, has a strict local minimum r, or has a strict local maximum r. Write the respective numbers as c,m,M, so k=c+m+M. Choose disjoint small parameter intervals around these points. For sufficiently small ε>0:

* the level r+ε has at least c+2m intersections in those intervals;
* the level r−ε has at least c+2M intersections there.

These statements follow directly from the signs of the distance minus the perturbed level at the endpoints and, for an extremum, at the original contact point. Consequently one of the two nearby levels has at least

\[
c+2\max(m,M)\ge c+m+M=k
\]

intersections. There are only finitely many vertex distances and edge-tangency distances from P. Choose ε avoiding all of them. Every intersection at the chosen radius is then in an edge interior and differential-transverse.

Applying this separately to every center P on the 15-gon gives at least six transverse contacts for each P. No continuity of the chosen radius as a function of P is required.

## 2. The six-contact property is uniformly stable

Fix one such center P and a circle of radius r with six transverse contacts. Choose six pairwise disjoint short angular arcs of the circle, one around each contact. On each arc choose endpoints z_j^- and z_j^+ with one strictly inside K and the other strictly outside K. All twelve endpoints have a positive distance from ∂K.

There is therefore η_P>0 such that the same inside/outside signs persist when:

1. the center moves by less than η_P;
2. the radius moves by less than η_P;
3. K is replaced by a convex body L with Hausdorff distance less than η_P.

For precision, inside points with a ball of radius δ contained in K remain inside L when d_H(K,L)<δ. This follows from the support-function inequality |h_K−h_L|≤d_H(K,L). Outside points at distance δ from K remain outside under the same restriction. The circle endpoints themselves move by at most the sum of the center and radius changes.

Each of the six angular arcs consequently still joins an inside point to an outside point, so each intersects ∂L. The arcs remain disjoint and provide six distinct contacts.

The neighborhoods B(P,η_P/2), with P ranging over ∂K, cover the compact set ∂K. Choose finitely many. A sufficiently small uniform Hausdorff bound then ensures that every P' on ∂L lies in one of the corresponding larger center neighborhoods B(P,η_P). Indeed the boundaries of sufficiently close full-dimensional convex bodies are close as well; this also follows from the preceding support-function argument. Hence every P' has a radius in a nonempty open interval for which all six witness arcs persist.

Thus the existence of six contacts at **every** boundary center survives sufficiently small convex Hausdorff perturbations.

## 3. Choose an analytic, positively curved perturbation

Let h be the support function of K, viewed as a 2π-periodic function of the outer-normal angle. Convolve h with the positive periodic heat kernel H_ε. The resulting h_ε is real analytic and converges uniformly to h as ε tends to zero. It is itself a support function: the convolution is a positive, normalized Minkowski average of rotations of K.

In the distributional sense, h+h'' is the positive curvature-radius measure of the polygon, with positive total mass. Therefore

\[
h_\varepsilon+h_\varepsilon''
=H_\varepsilon*(h+h'')>0.
\]

The support-function parameterization

\[
\gamma_\varepsilon(\theta)
=h_\varepsilon(\theta)(\cos\theta,\sin\theta)
+h_\varepsilon'(\theta)(-\sin\theta,\cos\theta)
\]

has derivative (h_ε+h_ε'')(-sinθ,cosθ). It describes a regular, real-analytic, strictly convex closed curve with positive curvature. Its body converges to K in Hausdorff distance. Convolution commutes with rotations, so the original 120-degree symmetry is preserved.

Choose ε small enough for the stability result. At any P' on the resulting curve, retain the six witness arcs and their open radius interval. The squared-distance function θ↦|γ_ε(θ)−P'|² is real analytic and nonconstant: it is zero at P' and positive elsewhere. Its derivative has finitely many zeros on the parameter circle, hence it has finitely many critical values. Choose a radius in the witness interval whose square is not a critical value. Every resulting circle/curve contact is differential-transverse, and at least six contacts are supplied by the witness arcs.

This proves the stated smoothing conclusion. We do not claim that the perturbed curve has N exactly six; the proof establishes N at least six.

## 4. Why arbitrarily fine polygon sampling does not solve #97

Choose the analytic perturbation above to be noncircular, which is possible since it approximates a noncircular polygon. For every δ>0 it has a finite δ-dense subset S for which **all unordered pairwise distances are distinct**.

Proof: cover Γ by finitely many short open arcs so that choosing a point in each makes a δ-net. Choose the points successively. At a new point X, equalities between |X−P_i| and |X−P_j| exclude the perpendicular bisector of P_iP_j. Equalities between |X−P_i| and any already-existing pair distance exclude finitely many circles. Also exclude the already-chosen points.

A line meets a strictly convex curve at most twice. Each of the finitely many circles meets Γ in finitely many points: otherwise analyticity gives an accumulation point and forces Γ to coincide with that circle, contrary to noncircularity. Thus the new open arc has only finitely many forbidden points, and the induction continues.

Every member of S is an extreme point of its convex hull. The resulting polygons can approximate Γ arbitrarily well, yet no vertex has even two other vertices equidistant from it. Therefore neither Hausdorff approximation nor fine sampling transfers boundary contacts into vertex contacts.

This is a rigorous failure of the naive discretization procedure, not a proof that some specially chosen finite closed subset cannot exist.

## 5. The exact finite closure problem

Write a regular analytic parameterization as γ(t). Near any transverse contact, the implicit function theorem gives a local contact branch u=F_j(t,r) satisfying

\[
|\gamma(F_j(t,r))-\gamma(t)|^2=r^2,
\qquad
\partial_r F_j=
\frac{r}{(\gamma(F_j)-\gamma(t))\cdot\gamma'(F_j)}.
\]

The denominator is nonzero by transversality. Locally there are at least six distinct branches. A finite counterexample on Γ would require a finite parameter set T and a positive radius r_t for every t∈T such that at least four distinct branch values F_j(t,r_t) also belong to T. The stability theorem does not establish these simultaneous closure equations.

Even continuous availability of six successor maps on a compact parameter circle does not, by itself, yield a finite closed subset. For example, six rotations t↦t+α_j, with 1,α_1,...,α_6 rationally independent, have no directed cycle: a cycle would give a nontrivial nonnegative integer relation among the α_j modulo one. Consequently no finite subset has even one available successor at every point. These rotations are only an abstract warning; they are not asserted to be Euclidean contact maps for Γ.

The separate [equilateral-orbits.md](equilateral-orbits.md) treats the proposed threefold finite-orbit gadget. That finite-incidence analysis is distinct from the boundary smoothing argument here.

## Source-search limit

Targeted searches of the primary paper and its authors' publication pages did not identify a published theorem converting this boundary construction into a finite vertex counterexample, nor a theorem proving that every such conversion is impossible. The 2013 paper explicitly treats the polygon-vertex conjecture as a separate question. The failure statement in Section 4 of this note is proved above and does not rely on a claimed literature result.

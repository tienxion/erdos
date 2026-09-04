# Stress audit for separated unit-distance deformations

This note concerns a particular deformation method for Erdős problem 97. It neither proves nor disproves the general problem.

## Exact equations and hypotheses

Let \(E\) be a finite bipartite incidence set between lines indexed by \(i\) and points indexed by \(j\). For \(t>0\), place the two vertex families at
\[
 A_i=(tX_i,\sqrt t\,Y_i),\qquad
 B_j=(1+tU_j,\sqrt t\,V_j).
\]
The unit-distance equation for \((i,j)\in E\) is exactly
\[
 F_{ij}=U_j-X_i+\tfrac12(V_j-Y_i)^2
                  +\tfrac t2(U_j-X_i)^2=0. \tag{1}
\]
Introduce incidence coordinates
\[
 b_i=X_i-\tfrac12Y_i^2,\qquad W_j=U_j+\tfrac12V_j^2.
\]
Then \(F=G+tH^2/2\), edge by edge, where
\[
 G_{ij}=W_j-b_i-Y_iV_j,\qquad
 H_{ij}=W_j-b_i-\tfrac12(Y_i^2+V_j^2).
\]
At the seed \(t=0\), assume \(G=0\): the point \((V_j,W_j)\) lies on the line of slope \(Y_i\) and intercept \(b_i\). No general-position hypothesis is needed for the identities below. Smooth lifts refer to smoothness in \(t\) of these rescaled coordinates.

Let \(J=DG\) at the seed. A left stress is an edge vector \(\omega\) with \(\omega^T J=0\). Equivalently,
\[
 \sum_j\omega_{ij}=\sum_j\omega_{ij}V_j=0\quad\text{for every line }i,
 \qquad
 \sum_i\omega_{ij}=\sum_i\omega_{ij}Y_i=0\quad\text{for every point }j. \tag{2}
\]

## First order is always compatible

A differentiable lift requires
\[
 Jz_1+\tfrac18(V_j-Y_i)^4=0. \tag{3}
\]
Its apparent stress condition is automatic. Indeed, (2) first gives
\[
 \sum_E\omega(V-Y)^4=6\sum_E\omega Y^2V^2.
\]
On every incidence, \(YV=W-b\), so
\[
 Y^2V^2=W^2-b^2-2bYV.
\]
All three terms have zero stress sum by (2). Thus there is no first-order obstruction for any exact incidence seed.

An explicit universal solution \(K\) of (3) is
\[
 \begin{array}{ll}
 K_b=(Y^4-6b^2)/8,&K_Y=-(Y^3+3bY)/2,\\
 K_W=-(V^4+6W^2)/8,&K_V=-V^3/2.
 \end{array} \tag{4}
\]
These formulas define an ambient polynomial vector field, not just values on the seed. In fact the exact polynomial identity
\[
 JK+\tfrac12H^2
 =-\frac{2V^2+YV+W+2Y^2+5b}{4}\,G \tag{5}
\]
holds on each edge, where \(J=DG\) is evaluated at the current coordinates.

For an implementation using (1), the same correction is
\[
\begin{aligned}
 K_X&=-3X^2/4-3XY^2/4+3Y^4/16,\\
 K_U&=-3U^2/4-3UV^2/4+3V^4/16,\\
 K_Y&=Y^3/4-3XY/2,\qquad K_V=-V^3/2.
\end{aligned} \tag{6}
\]

## The second-order condition

Write a prospective lift as \(z(t)=z_0+t z_1+t^2 z_2+o(t^2)\), and put \(z_1=K+v\). By (3), \(Jv=0\). The coefficient of \(t^2\) in the edge equation is
\[
 Jz_2+R(z_1),\qquad
 R(z_1)=-z_{1,Y}z_{1,V}+H_0\,DH(z_1),
 \quad H_0=-\tfrac12(V-Y)^2. \tag{7}
\]
Define
\[
 I_\omega=\frac3{16}\sum_E\omega(Y^4V^2+Y^2V^4)
         =\frac1{80}\sum_E\omega(V-Y)^6,
 \qquad
 Q_\omega(v)=\sum_E\omega v_Yv_V. \tag{8}
\]
Then the exact stress identity is
\[
 \omega^T R(K+v)=I_\omega-Q_\omega(v). \tag{9}
\]
Consequently a second-order formal lift exists **if and only if** some \(v\in\ker J\) satisfies
\[
 Q_\omega(v)=I_\omega\quad\text{for every left stress }\omega. \tag{10}
\]
The sufficiency here is only for the second-order jet: after choosing such a \(v\), linear algebra supplies \(z_2\). It does not assert convergence or a lift to positive \(t\).

For completeness, the algebra behind (9) is as follows. Substituting (4) into (7) and using \(W=b+YV\), its stress sum reduces to
\[
 \omega^T R(K)=\sum_E\omega\left[
 \tfrac3{16}(Y^4V^2+Y^2V^4)-Y^3V^3-\tfrac94bY^2V^2\right].
\]
The last two terms have zero stress sum: expand them using \(YV=W-b\), and note that \(b^2W=b^3+b^2YV\) is row-null, while \(bW^2=W^3-YVW^2\) is column-null. The same cancellations in the sixth-power expansion prove the equality in (8).

To treat a general \(v\), differentiate (5) in its direction at a seed with \(Jv=0\). This gives
\[
 G''(v,K)+J(DK\,v)+H_0DH(v)=0.
\]
The mixed terms in \(R(K+v)-R(K)\) are therefore \(-J(DK\,v)\); the remaining quadratic term is \(-v_Yv_V\). Pairing with a stress proves (9).

## Tangential choices, projective motions, and scale

If \(v\) is the velocity of a twice differentiable curve of exact incidence seeds, then \(Q_\omega(v)=0\) for every stress: this is the second derivative of \(G=0\). Thus integrable incidence motions cannot cancel a nonzero \(I_\omega\). If every vector of \(\ker J\) is integrable, second-order compatibility is independent of the chosen first correction and is precisely \(I_\omega=0\) for all stresses. A sufficient local hypothesis is that the incidence set is a smooth manifold whose tangent space is \(\ker J\).

Infinitesimal projective motions are integrable and satisfy a stronger assertion: their subspace lies in the common radical of every quadratic form \(Q_\omega\). Indeed, projective transformations preserve each incidence equation up to a nonzero scalar factor. For their infinitesimal generator \(p(z)\), \(Jp=cG\) edge by edge. Differentiating along any \(v\in\ker J\) at the seed and pairing with \(\omega\) gives
\[
 \sum_E\omega(p_Yv_V+v_Yp_V)=0.
\]
It follows that (10) descends to the quotient of \(\ker J\) by the projective tangent subspace. For an \((n_4)\) seed with Jacobian nullity 10 and projective orbit dimension 8, only two quotient directions can affect this second-order test. One must test their quadratic forms; a nonzero residual from a single minimum-norm correction is insufficient.

This is a statement about motions **through the fixed seed**. A finite projective change before starting the deformation changes the seed and must be tested separately. For example, the affine incidence transformation
\(V'=aV,\ W'=cW,\ Y'=(c/a)Y,\ b'=cb\)
changes (8), with the same stress vector, to
\[
 I'_\omega=\tfrac3{16}\left[
 c^2a^2\sum_E\omega Y^2V^4
 +\frac{c^4}{a^2}\sum_E\omega Y^4V^2\right].
\]
Thus arbitrary finite projective normalization is not covered by the infinitesimal invariance claim.

For an arbitrary fixed projective chart, there is an exact transformation rule. In homogeneous coordinates put
\[
 p_j=(V_j,W_j,1)^T,\qquad \ell_i=(-Y_i,1,-b_i)^T.
\]
Given \(M\in\mathrm{GL}_3(\mathbb R)\), assume
\(d_j=(Mp_j)_3\ne0\) and \(c_i=(M^{-T}\ell_i)_2\ne0\), so the transformed points are finite and the transformed lines are not vertical. Normalize
\[
 p'_j=Mp_j/d_j,\qquad \ell'_i=M^{-T}\ell_i/c_i.
\]
Then \(G'_{ij}=G_{ij}/(c_i d_j)\). At an incidence seed the transported stress is therefore
\(\omega'_{ij}=c_i d_j\omega_{ij}\), and
\[
 I'_{\omega'}=\frac1{80}\sum_E\omega_{ij}c_i d_j(V'_j-Y'_i)^6
 =\frac1{80}\sum_E\omega_{ij}
 \frac{\big[c_i(Mp_j)_1+d_j(M^{-T}\ell_i)_1\big]^6}
      {c_i^5d_j^5}. \tag{11}
\]
This formula tests finite chart changes without computing a new stress nullspace. In the affine example above one can retain the original stress vector because the common transformation factor is scalar; the zero/nonzero criterion is unaffected by that normalization.

The common physical rescaling \((Y,V)\mapsto s(Y,V)\), \((X,U)\mapsto s^2(X,U)\), with \(s\ne0\), corresponds to replacing \(t\) by \(s^2t\). It multiplies \(I_\omega\) by \(s^6\); it cannot turn a nonzero invariant into zero. A nondegenerate reparametrization of \(t\) likewise cannot remove an obstruction to a smooth lift.

## Nonautomatic nature of the second-order load

The second invariant does not vanish for all incidence seeds. The exact rational Pappus \((9_3)\) example in [verify-incidence-stress.py](verify-incidence-stress.py) has a nonzero stress with
\[
 \sum_E\omega(V-Y)^4=0,
 \qquad \sum_E\omega(V-Y)^6=66654/841\ne0.
\]
This example demonstrates only that the higher-order polynomial cancellation is not universal. It is not an \((n_4)\) construction or a resolution of problem 97.

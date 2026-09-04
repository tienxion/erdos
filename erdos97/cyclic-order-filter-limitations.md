# Why common-target alternation alone does not remove the K4,4 candidates

This is an obstruction to a proposed combinatorial filter, not a geometric construction or a solution of Erdős #97.

For an orbit-level directed edge \(i\to j\), let its rotation gain \(g_{ij}\) belong to \(\mathbb Z/3\mathbb Z\). The preferred neighbors of the full vertex \((i,k)\) are
\[
(i,k+1),\quad(i,k+2),\quad(j,k+g_{ij})\text{ for each orbit edge }i\to j.
\]
All indices in the second coordinate are modulo three. Each orbit has two outgoing edges, so every full vertex has four preferred neighbors.

Two full centers can share two targets only if their four endpoints alternate in the polygon's cyclic order. However, that necessary condition says nothing when every pair of centers shares at most one target.

## The eight-cycle orientation

Partition eight orbit labels into \(A_0,A_1,A_2,A_3\) and \(B_0,B_1,B_2,B_3\). Direct
\[
A_i\to B_i,B_{i+1}
\]
with indices modulo four, and direct every other cross-part pair from \(B\) to \(A\). The outgoing \(A\)-to-\(B\) edges form an eight-cycle, and every orbit has indegree and outdegree two.

**For every assignment of rotation gains**, every pair of full centers has at most one common preferred target:

1. Centers in the same orbit share their third orbit member. Their external targets have different rotation indices, so no external point is shared.
2. Centers in different orbits in the same part have at most one common outgoing target orbit, because the four outgoing two-subsets in either part are distinct and any two intersect in at most one orbit. Each center has only one target in that orbit, giving at most one shared point. Their internal targets belong to disjoint orbits, neither targeted externally by the other center.
3. Centers in opposite parts have no common external target orbit. Since the orbit pair has only one directed edge, at most one point can occur as an internal target of one and an external target of the other.

Thus both the common-predecessor bound and the alternation implication hold without restricting the cyclic order at all. In particular this filter cannot exclude this orientation, regardless of how accurately one encodes cyclic order.

## The two-four-cycle orientation

Partition the eight orbit labels into four groups \(X_0,X_1,X_2,X_3\), each containing two orbits, and direct every edge from \(X_i\) to \(X_{i+1}\), cyclically modulo four. This is the other indegree-two/outdegree-two orientation type of \(K_{4,4}\).

For the two source orbits \(p,q\) in a group and the two target orbits \(r,s\) in the next group, full centers from \(p,q\) share both target points exactly when
\[
g_{pr}-g_{qr}=g_{ps}-g_{qs}\pmod3. \tag{1}
\]
Indeed, a pair of centers \((p,k),(q,\ell)\) shares its target in orbit \(r\) precisely when \(\ell-k=g_{pr}-g_{qr}\), and similarly for \(s\).

One can make (1) fail in all four blocks, for example by using the gain matrix
\[
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\]
in every block. Then every pair of full centers again shares at most one preferred target. Centers in the same group are covered by (1); centers in different groups have either at most one internal/external shared target or none, as in the preceding argument.

This supplies abstract gain assignments for which alternation is vacuous in the second type as well. These assignments are **not asserted to satisfy any distance equations or strict-convexity conditions**.

## What further geometry would need to add

Radius ordering and angular separation constrain which gains can occur in an actual configuration. For example, a descending-radius edge has a unique possible rotation once the representatives' phase order is fixed. An ascending-radius edge has its matched angular separation in \((60^\circ,120^\circ)\) or \((240^\circ,300^\circ)\); choosing between those requires knowing phase differences relative to \(60^\circ\), not just the order within a \(120^\circ\) sector.

Nevertheless, merely adding the common-target alternation test to a geometric gain search will never reject an eight-cycle \(K_{4,4}\) candidate: that implication remains vacuous for every gain assignment. A stronger argument must use other consequences of convexity or the actual metric equations.

## An exact finite reduction of rotation-gain choices

Choose representatives with phases \(\theta_i\in[0,2\pi/3)\), and put \(\delta=\theta_j-\theta_i\). Let \(g_{ij}\in\{0,1,2\}\) mean that the target representative is rotated through \(2\pi g_{ij}/3\).

For an edge to a smaller-radius orbit,
\[
g_{ij}=\begin{cases}1,&\delta>0,\\2,&\delta<0.\end{cases}
\]
For an edge to a larger-radius orbit,
\[
g_{ij}=\begin{cases}
0,&|\delta|>\pi/3,\\
2,&0<\delta<\pi/3,\\
1,&-\pi/3<\delta<0.
\end{cases}
\]
To see this, write the radius ratio as \(\lambda=|z_j|/|z_i|\). The distance equation gives
\[
\cos\left(\delta+\frac{2\pi g_{ij}}3\right)
=\frac{\lambda^2-2}{2\lambda}.
\]
If \(\lambda<1\), the right-hand side is less than \(-1/2\), forcing the first case. If \(1<\lambda<2\), it lies strictly between \(-1/2\) and \(1/2\), forcing the second case. The bound \(\lambda<2\) follows from strict convexity of the orbit union, as proved in the local-lemmas note.

Thus, after specifying a nondecreasing radius order, gains are determined by the order of the reduced phases \(\theta_i\bmod(\pi/3)\) and a bit specifying which half of \([0,2\pi/3)\) contains each representative. Rotate globally so that \(\theta_0=0\). For eight orbits there are at most
\[
7!\,2^7=645120
\]
such chambers. Coincidences of reduced phases can be perturbed without changing gains on any edge: an edge cannot have \(\delta=0\), and an ascending edge cannot have \(|\delta|=\pi/3\); the descending gain is locally unchanged at \(|\delta|=\pi/3\). Therefore restricting to open chambers loses no possible edge-gain pattern.

This is a finite search reduction, not a claim that every chamber corresponds to feasible distances. It also does not overcome the vacuity of common-target alternation for the eight-cycle orientation.

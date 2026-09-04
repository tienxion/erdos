# A concrete limitation of local favorite-distance rules

This note concerns a failed general proof route for Erdős #97. It gives an abstract strict metric, not Euclidean coordinates or a convex polygon. No counterexample to #97 or claim of originality is asserted.

The conclusion is precise: strict triangle inequalities, the pairwise equidistance bounds used in the common-predecessor lemma, cyclic alternation of double intersections, and equal-radius rhombus implications do not, by themselves, force a vertex with fewer than four favorite-distance neighbors.

## A useful geometric comparison

For four vertices \(a,b,c,d\) in cyclic order in a strictly convex polygon, the diagonals meet properly. Applying strict triangle inequalities at their intersection proves
\[
|a-c|+|b-d|>|a-b|+|c-d|,
\qquad
|a-c|+|b-d|>|a-d|+|b-c|. \tag{1}
\]
These are the strict Kalmanson inequalities for the Euclidean distance matrix.

For example, if the favorite-distance graph contains
\[
a\to b,\quad a\to c,\quad b\to d,\quad c\to d,
\]
then the first inequality in (1) cancels the two equal distances from \(a\), giving
\[
r_b>r_c. \tag{2}
\]
Thus certain four-edge patterns impose strict radius orderings. The four underlying edges form a cycle of length four.

More generally, (1) says that for fixed target vertices, the difference of the distances to those targets is strictly monotone along each of the two open boundary arcs, with opposite directions on the two arcs. This supplies metric information beyond merely counting common predecessors.

## A four-regular graph with no local double intersections

Work over the field \(\mathbb F_3\). Represent each one-dimensional subspace of \(\mathbb F_3^3\) by its unique vector whose first nonzero coordinate is one. There are 13 such vectors:
\[
\begin{aligned}
&(0,0,1),(0,1,0),(0,1,1),(0,1,2),\\
&(1,0,0),(1,0,1),(1,0,2),\\
&(1,1,0),(1,1,1),(1,1,2),\\
&(1,2,0),(1,2,1),(1,2,2).
\end{aligned}
\]

Take 13 point labels \(P_v\) and 13 line labels \(L_w\), indexed by those vectors, and join \(P_v\) to \(L_w\) exactly when
\[
v\mathbin{\cdot}w=0\pmod3.
\]
Regard every edge as two reciprocal directed edges.

Every vertex has degree four. Indeed, the vectors perpendicular to a fixed nonzero vector form a two-dimensional subspace, containing eight nonzero vectors and hence four one-dimensional subspaces.

Two distinct point vertices have exactly one common line neighbor: their vectors are independent, and their simultaneous orthogonal complement has dimension one. Dually, two distinct line vertices have exactly one common point neighbor. A point vertex and a line vertex have no common neighbor, by bipartiteness. Thus every pair has at most one common neighbor, and the graph has no cycle of length four.

Give all vertices the same formal favorite radius. Under any cyclic ordering of the 26 labels:

- Every vertex has four favorite neighbors.
- Every pair has at most one common predecessor and at most one common target.
- The alternation rule for two common predecessors is vacuous.
- The equal-radius rhombus identity is vacuous, because no pair shares two targets.
- The four-edge radius-order pattern in (2) is absent.
- Reciprocal-edge consistency holds, because all formal radii agree.

This already shows a limitation of arguments based solely on those directed graph rules.

## An exact strict metric with no accidental equalities

The graph model can be strengthened to a metric model. Label its vertices \(0,\ldots,25\), using the listed point vectors first and the listed line vectors second. Give every unordered pair \(u<v\) a distinct integer rank \(h(u,v)\in\{1,\ldots,325\}\), in lexicographic order.

Define a symmetric distance function, with zero diagonal, as follows:
\[
d(u,v)=
\begin{cases}
2,&u,v\text{ are incident point and line vertices},\\
3+h(u,v)/100000,&u,v\text{ are both points or both lines},\\
4+h(u,v)/100000,&u,v\text{ are nonincident point and line vertices}.
\end{cases} \tag{3}
\]

Before the small perturbations, the off-diagonal values in (3) are the graph distances plus one. Two point vertices, or two line vertices, have graph distance two; nonincident point and line vertices have graph distance three. Therefore every triangle of distinct vertices has unperturbed triangle-inequality slack at least one. Each perturbation lies between zero and \(325/100000\), so even subtracting the largest possible right-hand perturbation leaves strictly positive slack. Thus every triangle inequality for distinct vertices remains strict.

At every vertex, its four incidence neighbors are at distance exactly two. All other distances are greater than three and are globally distinct: ranks are distinct within each of the disjoint intervals \((3,3.01)\) and \((4,4.01)\). Consequently the only repeated distance in any row is the favorite distance two.

Moreover, **every pair of vertices has at most one equidistant third vertex**, even when the third vertex is allowed an arbitrary radius. An equality between two distances at a third vertex can only involve two incidence edges of length two. Such a third vertex is a common graph neighbor, of which there is at most one.

The exact integer implementation in `verify-local-axioms-countermodel.py` multiplies (3) by 100000. It checks all strict triangle inequalities, all favorite-neighbor sets, all arbitrary-radius equidistant-center counts, and the absence of four-cycles. No numerical tolerance or floating-point arithmetic is used.

## The missing Euclidean information

The metric in (3) is not claimed to admit a planar Euclidean realization. It does not satisfy the strict Kalmanson conditions in the displayed cyclic order.

For a concrete violation, take the cyclically ordered labels
\[
P_{(0,0,1)},\quad P_{(0,1,0)},\quad
L_{(0,1,0)},\quad L_{(1,0,0)}.
\]
Both diagonal pairs are incident, so their distances sum to four. The two same-type opposite sides each have distance greater than three. Thus their sum exceeds six, contradicting the first inequality in (1).

The countermodel therefore blocks the specified local incidence and metric-triangle route. It does not block arguments using the full global Kalmanson inequalities, Euclidean distance-matrix rank, or actual circle geometry.

The same local graph obstruction exists at arbitrarily large sizes: replacing \(\mathbb F_3\) by \(\mathbb F_q\) for a prime \(q\ge3\) gives \(2(q^2+q+1)\) vertices, degree \(q+1\ge4\), and at most one common neighbor per pair. Small distinct rational perturbations of the nonedge distances again produce strict metric versions.

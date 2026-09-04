# A partial small-polygon obstruction for Erdős #97

**Scope.** The argument below excludes a counterexample on at most eight vertices. It does not settle Erdős #97, and no claim of originality is made. The last section gives an abstract nine-vertex directed graph showing a limitation of the combinatorial constraints; that graph is not a geometric counterexample.

Throughout, \(V\) is a finite planar set in strictly convex position: its points are precisely the vertices of their convex hull. In particular, no three points of \(V\) are collinear. Indices of polygon vertices are taken in their cyclic order.

## Common-predecessor lemma

Assign to each \(v\in V\) a positive radius \(r_v\), with no requirement that radii at different vertices coincide. Define the full directed neighbor set
\[
F(v)=\{w\in V\setminus\{v\}:|v-w|=r_v\}.
\]
For distinct \(x,y\in V\), call \(v\) a common predecessor if \(x,y\in F(v)\).

**Lemma.** Every pair \(x,y\) has at most two common predecessors. If there are two, \(a,b\), the segments \(ab\) and \(xy\) cross at the midpoint of \(xy\), in the relative interior of both segments. Thus their four endpoints alternate in the cyclic order. In particular, adjacent polygon vertices have at most one common predecessor.

**Proof.** Every common predecessor lies on the perpendicular bisector \(L\) of \(xy\). There cannot be three, because no three vertices are collinear.

Suppose there are two, \(a,b\). They are distinct from \(x,y\), since there are no loops in the directed graph. Write \(P=\operatorname{conv}(V)\). The intersection \(P\cap L\) is a segment. As \(a,b\) are extreme points of \(P\), they must be its two endpoints: an extreme point cannot lie in the relative interior of a segment contained in \(P\).

The midpoint \(t=(x+y)/2\) belongs to \(P\cap L=[a,b]\). It cannot equal \(a\) or \(b\), since it is a nontrivial convex combination of two other vertices. Therefore \(t\) lies in the relative interior of \(ab\), and it also lies in the relative interior of \(xy\). The chords cross properly, which in a convex polygon is equivalent to alternation of their endpoints. Adjacent vertices cannot be endpoints of a chord crossed properly by a chord between other vertices. This proves the last assertion. \(\square\)

The same alternation conclusion applies to any two centers sharing two targets. In particular, for centers \(a,b\), at most one common target lies in either open boundary arc between \(a\) and \(b\).

## Counting rules out fewer than eight vertices

Suppose, toward a counterexample to #97, that every vertex admits a radius with at least four other vertices at that distance. Choose one such radius per vertex, and use the **full** neighbor sets \(F(v)\) above, rather than arbitrarily truncating them to four targets.

Put \(n=|V|\), \(d_v=|F(v)|\ge4\), and let \(\nu(x,y)\) count the common predecessors of \(x,y\). Counting a vertex together with an unordered pair of its targets gives
\[
\sum_{v\in V}\binom{d_v}{2}
=\sum_{\{x,y\}\subset V}\nu(x,y).
\]
There are \(n\) adjacent pairs, each contributing at most one. Every other pair contributes at most two. Therefore
\[
6n\le\sum_v\binom{d_v}{2}
\le n+2\left(\binom n2-n\right)
=n(n-2).
\]
Consequently \(n\ge8\).

## The equality case rules out eight vertices

Now suppose \(n=8\). Both inequalities in the count must be equalities. Hence:

- Every full neighbor set has exactly four elements.
- Every adjacent pair has exactly one common predecessor.
- Every nonadjacent pair has exactly two common predecessors.

Write the vertices cyclically as \(v_0,\ldots,v_7\), with subscripts modulo eight. The pair \(v_{i-1},v_{i+1}\) is nonadjacent, so it has two common predecessors. By the lemma, one lies in each open boundary arc between the pair. The shorter arc contains only \(v_i\); therefore
\[
v_{i-1},v_{i+1}\in F(v_i).
\]
It follows that the two side lengths incident to \(v_i\) both equal \(r_{v_i}\). Following the sides around the polygon shows that **all side lengths and all chosen radii equal one positive number \(\ell\)**.

Let \(A\) be the adjacency matrix of the undirected graph whose edges are precisely the vertex pairs at distance \(\ell\). Because the neighbor sets were full and have cardinality four, \(A\) is a symmetric integer matrix, has zero diagonal, and every row sums to four.

Let \(C\) be the adjacency matrix of the boundary cycle \(C_8\), let \(J\) be the all-ones matrix, and let \(I\) be the identity matrix. The off-diagonal entry \((A^2)_{ij}\) counts common predecessors: it is one for boundary-adjacent vertices and two for all other distinct vertices. Its diagonal entry is four. Thus
\[
A^2=2J+2I-C. \tag{1}
\]

The cycle matrix \(C\) has eigenvalues \(2\cos(2\pi j/8)\), \(0\le j<8\), as follows by applying it to the usual Fourier vectors. The all-ones vector has \(C\)-eigenvalue two and \(J\)-eigenvalue eight; all the other Fourier vectors have \(J\)-eigenvalue zero. Equation (1) therefore gives the following spectrum, including multiplicities:
\[
\operatorname{spec}(A^2)
=\{16,\ 4,\ 2,\ 2,\ 2-\sqrt2,\ 2-\sqrt2,\ 2+\sqrt2,\ 2+\sqrt2\}. \tag{2}
\]

Since \(A\) is real symmetric, its eigenvalues are real and their squares give (2). Since \(A\) is an integer matrix, its characteristic polynomial belongs to \(\mathbb Z[x]\).

At least one eigenvalue of \(A\) has square \(2-\sqrt2\). Its minimal polynomial over \(\mathbb Q\) is
\[
P(x)=x^4-4x^2+2,
\]
which is irreducible by Eisenstein's criterion at two. Hence all four roots
\[
\pm\sqrt{2-\sqrt2},\qquad \pm\sqrt{2+\sqrt2}
\]
occur as eigenvalues of \(A\). They each occur exactly once, because their squared multiplicities already exhaust the corresponding entries of (2). Their sum is zero.

Likewise, an eigenvalue with square two forces the irreducible factor \(x^2-2\), so \(\sqrt2\) and \(-\sqrt2\) each occur exactly once. Their sum is also zero.

The remaining two eigenvalues are four and either two or minus two. The eigenvalue four is forced by the row sums; (2) leaves precisely one eigenvalue whose square is four. Consequently
\[
\operatorname{tr}(A)=4+2=6
\quad\text{or}\quad
\operatorname{tr}(A)=4-2=2.
\]
Both contradict the zero diagonal of \(A\). Thus eight vertices are impossible.

**Partial conclusion.** Any counterexample to Erdős #97 in strictly convex position must have at least nine vertices. This argument makes no assertion about existence or nonexistence from nine vertices onward.

## A nine-vertex abstract witness to the limitation

The common-predecessor bounds and alternation condition alone do not exclude nine vertices. They remain feasible even after adding the following necessary radius-consistency rule: reciprocal arcs force the chosen radii to agree, while a one-way arc between full neighbor sets forces them to differ.

Here is a directed graph on cyclically ordered labels \(0,1,\ldots,8\). Every row lists exactly four outgoing neighbors.

| Vertex | Outgoing neighbors | Radius class |
|---|---|---|
| 0 | 1, 2, 5, 8 | 0 |
| 1 | 0, 3, 4, 8 | 0 |
| 2 | 1, 4, 5, 7 | 1 |
| 3 | 0, 2, 5, 6 | 2 |
| 4 | 1, 3, 6, 8 | 0 |
| 5 | 2, 4, 7, 8 | 1 |
| 6 | 0, 3, 5, 7 | 2 |
| 7 | 0, 1, 4, 6 | 2 |
| 8 | 2, 3, 6, 7 | 3 |

The radius classes are equality labels, not numerical radii. The graph was found by a satisfiability search. Its stated finite properties can be checked without that solver using `verify-combinatorial-witness.py` and `nine-vertex-combinatorial-witness.json` in this directory.

**This is not a geometric counterexample.** No vertex coordinates, exact distances, or convex realization are asserted. It only shows that an exclusion for nine vertices or a general proof requires further geometric information beyond the verified combinatorial conditions.

## A further metric obstruction: equal-radius rhombi

There is an additional exact constraint not encoded in that verifier. Suppose two centers \(a,b\), whose chosen radii are equal, share two targets \(x,y\). The four cross-distances are equal. The common-predecessor lemma makes the quadrilateral convex, and it is a rhombus. Its diagonals bisect one another, giving the vector identity
\[
a+b=x+y. \tag{3}
\]
One can also obtain (3) directly from the equal-radius circle equations: the common chord is perpendicular to the center line and its midpoint is \((a+b)/2\).

This stronger constraint actually proves that the displayed abstract witness cannot be realized geometrically. Its vertices \(0,1,4\) have equal chosen radii. Centers \(0,4\) share targets \(1,8\), while centers \(1,4\) share targets \(3,8\). Consequently (3) would give
\[
v_0+v_4=v_1+v_8,
\qquad
v_1+v_4=v_3+v_8.
\]
Subtracting yields \(v_0+v_3=2v_1\), which puts one vertex at the midpoint of two other vertices and contradicts strict convexity.

Thus the witness establishes only the advertised limitation of the weaker combinatorial rules. Rhombus vector identities provide an additional exact way to reject some abstract graph candidates.

# Independent audit of the restricted orbit-graph exclusion

## Scope and conclusion

The audited argument concerns finite unions of distinct equilateral orbits
\[
O_i=\{z_i,\omega z_i,\omega^2z_i\},\qquad
\omega=e^{2\pi i/3},\qquad z_i\ne0,
\]
whose union is in strictly convex position. At each point of \(O_i\), the chosen equal-distance radius is specifically \(\sqrt3|z_i|\), the side length of its own orbit. The argument is not about arbitrary radius choices, arbitrary rotational configurations, or arbitrary convex polygons.

**Audit result:** no false pruning, missing graph case, or geometric gap was found in the inspected argument. The exact graph check excludes three through seven orbits separately. One and two orbits cannot supply two external neighbors. Consequently a counterexample within this specified construction would need at least eight orbits, hence at least 24 points. This is not a general 24-point lower bound for Erdős #97 and does not solve that problem.

## Inspected inputs

The source versions audited had these SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `search-orbit-graphs.cpp` | `40fd4c400132440d0ee6effc069222e39e78344a59e45867aaa5577254b91ac9` |
| `equilateral-orbits.md` | `1aee833809b7b293d92ccf0498a1514c71fef667480be35f03401abfcc0ea343` |
| `equilateral-cycle-completion.md` | `154cbe40c6c3af029c267f18d82568a2a8abab3e970ac5f50ecb282676163b27` |

Later textual revisions should be compared against these versions when reusing this audit.

## Geometric reduction

The following necessary conditions were checked against their written proofs.

1. An external orbit contributes at most one neighbor at the chosen internal-side radius. The only two-intersection possibilities after normalizing the source to one either put the source at a midpoint of other vertices, or reproduce the source orbit itself.
2. The cubic-lift identity
   \[
   i\to j\iff |z_j^3-z_i^3|^2
   =9|z_i|^2\bigl(|z_j|^2-|z_i|^2\bigr)^2
   \]
   follows from the product of the three real distance-equation factors, so both directions are valid. It excludes edges between distinct equal-radius orbits and excludes two-way edges.
3. In a complete underlying triangle ordered by increasing radius, the extreme edge must ascend. The written triangle-inequality comparison is strict because the intermediate radius is strictly between the extremes.
4. The smallest member of a complete triangle cannot send to both other members. The same-half-plane observation follows from strict extremality, and the two rotated-circle intersections used in the proof are explicitly identified and distinct. The resulting two allowed orientations are exactly the middle-source pattern and the reverse directed cycle.
5. A fixed ascending extreme edge has at most one intermediate-radius reverse-cycle completion. The proof's two circle-nonintersection calculations, remaining circle-intersection parameterization, and forbidden-cap argument were checked. In the proper-intersection case, the point one being strictly inside the larger circle gives \(\psi<\phi+\pi/6\), so the relevant outside arc does not introduce a wrapping ambiguity. In the tangency case, the same comparison at \(U\) applies also at the endpoint \(\phi=\pi/6\): the displayed quadratic is positive at \(r^2=5/2\). The forbidden cap makes the normalized source a convex combination of other orbit points.

Every valid configuration of the stated kind therefore induces an oriented orbit graph of minimum outdegree at least two satisfying those graph conditions.

### Radius ties

Ties may be ordered arbitrarily in the search. An actual edge cannot join two distinct tied orbits. Therefore every actual complete triangle has three distinct radii, and its index order is its strict radius order. Likewise, an actual reverse-cycle completion cannot tie an endpoint, since it is adjacent to both endpoints. No geometric restriction is incorrectly applied to a tied pair by passing to a total order.

### Deleting edges to obtain outdegree exactly two

For each vertex independently, retain exactly two outgoing edges. This preserves absence of two-way edges. It cannot create a complete underlying triangle that was absent before, and it leaves the directions of every retained triangle unchanged. It also cannot increase the number of retained reverse-cycle completions of an extreme edge. Thus the three necessary graph properties are hereditary under edge deletion. Searching outdegree exactly two is sufficient to exclude minimum outdegree at least two.

## Exhaustive-search audit

`search-orbit-graphs.cpp` assigns rows from largest index to smallest. In each row it considers every unordered pair of distinct possible outgoing targets, excluding the vertex itself and targets already having a reciprocal edge into that row. All selected edges are cleared on backtracking. Consequently each complete oriented graph of outdegree exactly two has one branch of the search, unless it has already violated a necessary condition.

The pruning is monotone:

- A two-way edge cannot be repaired by adding more edges.
- For \(i<j<k\), a completed triangle is rejected exactly when its extreme edge descends or its smallest vertex sends to both others. With two-way edges absent, the survivors are precisely the two allowed orientations.
- For each retained ascending edge \(i\to j\), the counter increments only for \(i<k<j\) with \(j\to k\to i\). Rejecting a second such completion implements the stated uniqueness condition exactly.

No test assumes that an unassigned edge will remain absent. It rejects only already present forbidden patterns, so valid completions are not lost. Array bounds and the terminal-depth counter are valid for the accepted range \(3\le n\le9\).

## Independent recompilation and exact finite results

The inspected C++ source was independently compiled with

```text
c++ -std=c++17 -O2 erdos97/search-orbit-graphs.cpp -o /tmp/erdos97-orbit-audit
```

The resulting executable was run without the optional first-solution flag for each size from three through seven. Every run reported zero solutions and `exhaustive=1`.

| Orbits | Recursive nodes | Consistent prefixes by assigned-row count |
|---|---:|---|
| 3 | 2 | 1, 1, 0, 0 |
| 4 | 5 | 1, 3, 1, 0, 0 |
| 5 | 26 | 1, 6, 15, 4, 0, 0 |
| 6 | 333 | 1, 10, 60, 162, 97, 3, 0 |
| 7 | 10,960 | 1, 15, 160, 1080, 3756, 4674, 1274, 0 |

These are exact Boolean/integer exhaustive computations over the audited search tree. The count includes the empty prefix. The zero final entry is the number of complete solutions. The exclusion for all smaller sizes is supported by separate runs; it is not inferred by padding a seven-vertex graph with isolated vertices.

## Separate solver cross-check

A second encoding was independently written in Python using Z3. It used one Boolean per directed edge, an exact-two outgoing-cardinality constraint at each vertex, and explicit formulas for the two allowed triangle orientations. For every ascending extreme edge and every pair of distinct intermediate vertices, it forbade the five-edge pattern consisting of that edge and two reverse-cycle completions.

Z3 **reported `unsat` separately for each size 3, 4, 5, 6, and 7**. No exported Z3 proof certificate was checked. This is a corroborating solver result, not a replacement for the audited exact exhaustive C++ computation and its completeness argument.

## Related small-polygon note

`small-polygon-obstruction.md` contains the separate, general exclusion of at most eight vertices. Its displayed abstract nine-vertex graph is not a geometric counterexample. The note now includes the additional equal-radius rhombus identity
\[
a+b=x+y
\]
for two equal-radius centers sharing two targets, and applies it to that graph to obtain \(v_0+v_3=2v_1\), contradicting strict convexity. The orbit exclusion above and that general small-polygon argument have different scopes.

# Erdős #97: sources and construction mechanisms

Checked 2026-09-04. No solution of #97 is claimed here.

## Current status and precise scope

[The problem page](https://www.erdosproblems.com/97) lists the $100 problem as open/falsifiable: does every convex polygon have a vertex from which no four other vertices are equidistant? Radii may depend on the vertex. A common-unit-distance construction with minimum degree four would suffice to disprove it, but is stronger than required.

The [June 2026 discussion](https://www.erdosproblems.com/forum/thread/97?embed=1) contains a conditional proposed reduction to nine vertices. Its author subsequently softened the claimed resolution. It is not an established reduction and is not used below.

## Danzer's threefold construction

Primary source: [Erdős, Some combinatorial and metric problems in geometry (1987), pp. 175–176](https://www.renyi.hu/~p_erdos/1987-27.pdf).

The cyclic order is

\[
A_1,B_1,C_1,A_2,B_2,C_2,A_3,B_3,C_3,
\]

with rotation by 120 degrees advancing the subscripts. The imposed equalities are

\[
|A_1A_2|=|A_1A_3|=|A_1B_3|,\quad
|B_1B_2|=|B_1B_3|=|B_1C_2|,\quad
|C_1C_2|=|C_1C_3|=|C_1A_3|.
\]

Begin with the Reuleaux triangle based on the equilateral A-orbit. Choose B1 close to A1 on the extension of the arc A3A1 beyond A1; rotate it to obtain B2 and B3. Choose C1 along the B-Reuleaux arc from B1 toward the midpoint of arc B1B2. The difference |C1C3|−|C1A3| changes sign between those endpoints, supplying the final equality by continuity.

This establishes three equal distances at every vertex. It supplies no fourth neighbor. Consequently a search using threefold equilateral orbits must add a substantive incidence condition beyond this existing mechanism.

## Fishburn–Reeds: reflected Petersen construction

Primary paper: [Fishburn and Reeds, Unit distances between vertices of a convex polygon, Computational Geometry 2 (1992), 81–91](https://doi.org/10.1016/0925-7721(92)90026-O). [Full text linked from Reeds's profile](https://www.academia.edu/88716261/Unit_distances_between_vertices_of_a_convex_polygon).

Their 20 points are A_i=(-x_i,y_i) and B_i=(x_i,y_i), i=1,...,10, with increasing y_i. Unit cross-distances satisfy (x_i+x_j)^2+(y_i−y_j)^2=1. They impose 15 symmetric equations in 19 variables (ten x-coordinates and nine y-gaps), leaving a four-dimensional family. Their final closure follows by changing a parameter until a continuous residual changes sign. Their minimality theorem concerns a line-separated cut with degree at least three on both sides, not every possible degree-three convex configuration.

The following is an **approximate, truncated numerical seed**, not exact certified coordinates:

| i | x_i | y_i |
|---|---:|---:|
| 1 | .469633821777 | −.092982777730 |
| 2 | .471414237018 | −.089969229800 |
| 3 | .473126180256 | −.087048665472 |
| 4 | .520000000000 | .030000000000 |
| 5 | .520996246864 | .033000000000 |
| 6 | .522000000000 | .036100000000 |
| 7 | .429872125856 | .342595442083 |
| 8 | .429224646090 | .344599064292 |
| 9 | .428539574537 | .346658610393 |
| 10 | .390440922261 | .417185267785 |

### Independently reconstructed graph

The cross-neighbor labels reconstructed from this table are

```
1:  6  9 10
2:  5  8 10
3:  4  7 10
4:  3  8  9
5:  2  7  9
6:  1  7  8
7:  3  5  6
8:  2  4  6
9:  1  4  5
10: 1  2  3
```

This symmetric quotient is the Petersen graph: an outer pentagon is (1,6,7,3,10), its corresponding inner labels are (9,8,5,4,2), and the inner edges join labels two positions apart. The 20-point cross-graph is therefore the bipartite double cover of the Petersen graph, also called the Desargues graph.

The approximate seed has minimum consecutive signed turn about 3.91e−8, minimum pair separation about .002106, and smallest nonedge squared-distance error from 1 about 1.37e−5. These are numerical diagnostics, not exact certificates. They show why tolerant equality/convexity tests would be dangerous here.

## Exact obstruction to upgrading this family through cross-edges

The following arguments are independent deductions from the displayed graph.

**Cut lemma.** A unit-distance graph across a line-separated convex cut cannot contain K_{2,2}.

Proof: suppose distinct a,a' on one side and b,b' on the other satisfy all four cross-unit equalities. The two points b,b' are the two intersections of the unit circles centered at a,a'. Thus segment bb' intersects segment aa' at their common midpoint. This contradicts separation of the convex hulls of the two sides. (Tangency supplies only one intersection, so cannot give distinct b,b'.)

**Ten-by-ten obstruction.** No such cut with ten vertices on each side can have minimum cross-degree four. Each of the ten A vertices would contribute at least six unordered pairs of B neighbors. K_{2,2}-freeness permits each B-pair at most once. This requires 60≤45, a contradiction. More generally, a 4-regular bipartite cut requires at least thirteen vertices on each side: the four neighbors of a fixed vertex have twelve other, all distinct, neighbors in its own side.

**Keeping the existing Petersen edges is even more restrictive.** Every nonadjacent pair of distinct vertices in the Petersen graph is connected by a three-edge path. One proof uses its pentagon-and-star presentation: its automorphisms are transitive on nonadjacent pairs, and 1–6–8–2 is such a path for the nonadjacent pair 1,2. Alternatively all thirty nonedges can be checked directly from the ten displayed adjacency lists. Adding a new off-diagonal quotient edge closes such a path into a forbidden four-cycle in the bipartite double cover.

The only possible new symmetric cross-edges are consequently diagonal ones, A_iB_i, requiring x_i=1/2. These diagonal additions can occur only at an independent set of quotient labels: adding both A_iB_i and A_jB_j for an existing Petersen edge ij produces a K_{2,2}. In particular they cannot upgrade every vertex to degree four. This rules out a cross-only upgrade for the entire reflected family retaining the existing edges, not just near the numerical seed.

At the published seed every same-side distance is below .526. This remains below one in a sufficiently small neighborhood. Hence there is **no nearby deformation that preserves the thirty known unit edges and attains minimum total unit-degree four**. This does not rule out large deformations that introduce same-side unit edges, constructions that discard existing unit edges, or vertex-dependent-radius counterexamples to #97.

## Excluding the thirteen-by-thirteen boundary case

These are partial results for the **common-unit-distance cut variant**, not a solution of #97.

### Independent spectral proof with reflection symmetry

Suppose there are thirteen reflected pairs A_i=(-x_i,y_i), B_i=(x_i,y_i), with x_i>0, all extreme vertices of a convex polygon, and every vertex has at least four cross-unit neighbors. Let M be the symmetric 13-by-13 zero-one cross-incidence matrix.

By the cut lemma, each pair of columns occurs together in at most one row. Thus

\[
78=13\binom42\le \sum_{i=1}^{13}\binom{d_i}{2}
\le\binom{13}{2}=78.
\]

Equality forces every row degree to be four and every pair of columns to occur together exactly once. Therefore M²=3I+J, and M has the eigenvalue 4 on the all-ones vector. On its twelve-dimensional perpendicular complement its eigenvalues are +sqrt(3) and -sqrt(3). If their multiplicities are r and 12-r, then

\[
\operatorname{tr}M=4+(2r-12)\sqrt3.
\]

Because M has integer entries, its trace is an integer; irrationality of sqrt(3) forces r=6. Hence exactly four diagonal entries of M equal one. Each such entry means |A_iB_i|=2x_i=1, so four B vertices lie on the line x=1/2. Even three collinear members contradict strict convex position. This rules out the reflected 13+13 case without invoking a computer enumeration or any further geometric lemma.

### General cut proof using a published finite extremal bound

The reflection hypothesis can be removed if we invoke Fishburn–Reeds Table 2: a 6-by-11 pattern-feasible matrix has at most **22** ones. Every convex unit-distance cut matrix is pattern feasible in their sense. This is a published finite extremal fact; its proof is not reconstructed here.

Let M now be any 13-by-13 cut matrix with all row and column degrees at least four. The same counting argument forces every degree to be four and every two columns to share exactly one incident row.

Choose any two columns and delete them, together with every row incident to either. They meet 4+4−1=7 rows, leaving six rows and eleven columns. None of the remaining rows met either deleted column, so each retains all four ones. The resulting 6-by-11 cut submatrix has 24 ones, contradicting the published bound 22.

Consequently **any convex line-separated unit-distance graph of minimum cross-degree four has at least fourteen vertices in each part, hence at least 28 vertices in total**. To check the last assertion without assuming balanced parts: K_{2,2}-freeness and minimum degree four imply at least thirteen vertices per part by the two-step-neighborhood argument. If one part has exactly thirteen vertices and the other has b vertices, pair counting in the thirteen-vertex part gives 6b≤78, hence b≤13; the excluded 13+13 case follows.

This lower bound places no restriction on configurations in which the four equal distances use vertex-dependent radii or in which some required unit neighbors are on the same side of the chosen line.

## Further primary results relevant to avoiding false proof routes

[Aggarwal, On Unit Distances in a Convex Polygon, arXiv:1009.2216; Discrete Mathematics 338 (2015), 88–92](https://arxiv.org/abs/1009.2216) proves additional forbidden cut patterns, including cycles with an intersection-free edge. Cross-distance matrices satisfy a strict diagonal inequality and an obtuse-angle restriction. However his Theorem 3 constructs abstract matrices satisfying both restrictions with a superlinear number of unit entries. Therefore those two matrix restrictions alone do not imply a linear bound, and pattern feasibility does not establish geometric realizability.

[Bárány and Roldán-Pensado, A Question from a Famous Paper of Erdős (2013)](https://www.renyi.hu/~barany/cikkek/134.pdf) construct a convex 15-gon whose boundary meets some circle centered at each boundary point in at least six points. Those intersections are boundary points, generally in edge interiors. This is a different problem: it provides neither a finite vertex set closed under the resulting circle intersections nor a counterexample to #97.

The accompanying [boundary_smoothing.md](boundary_smoothing.md) proves that this property survives analytic positive-curvature smoothing, and explains the exact finite closure still required. It also proves that arbitrarily fine finite samples can have all pairwise distances distinct, so ordinary discretization does not preserve the equalities.

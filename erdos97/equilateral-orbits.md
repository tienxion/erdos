# Equilateral-orbit restrictions for Erdős #97

**Status: partial results for a restricted construction.** These arguments do
not solve #97 and make no claim of originality. A hypothetical counterexample
need not have rotational symmetry or use the distances specified here.

Let \(\omega=e^{2\pi i/3}\). Consider distinct orbits
\[
O_i=\{z_i,\omega z_i,\omega^2z_i\},\qquad z_i\ne0,
\]
whose union is in strictly convex position. For each point in \(O_i\), use
the particular radius \(\sqrt3|z_i|\), the side length of its own equilateral
triangle. There are already two neighbors in its own orbit at that radius.
Write \(i\to j\) if an additional neighbor belongs to \(O_j\).

## One external orbit supplies at most one neighbor

Normalize the source to 1. If two distinct points \(u,v\) of a target orbit
both have distance \(\sqrt3\) from 1, they lie on a circle centered at 0 and
on the circle centered at 1. Consequently they are complex conjugates.
They also differ by a rotation of 120 or 240 degrees. Their angular
positions are therefore either \(\pm60^\circ\) or \(\pm120^\circ\).

In the first case, if their common modulus is \(r>0\), the distance equation
is \(r^2-r+1=3\), so \(r=2\). Their midpoint is 1, violating strict
convexity. In the second case the equation is \(r^2+r+1=3\), so \(r=1\).
The target orbit then coincides with the source orbit, contrary to its
being distinct. Thus each external orbit supplies at most one neighbor.

In particular, a counterexample within this construction requires minimum
outdegree at least two in the orbit graph.

## An exact cubic change of coordinates

Put \(t_i=|z_i|^2\) and \(w_i=z_i^3\). Then
\[
i\to j\quad\Longleftrightarrow\quad
|w_j-w_i|^2=9t_i(t_j-t_i)^2. \tag{1}
\]

To prove this, put \(A=t_j\), \(B=t_i\), and let \(\delta\) be the
angle from \(z_i\) to \(z_j\). The three possible distance equations are
\[
A-2B-2\sqrt{AB}\cos(\delta+2k\pi/3)=0,
\qquad k=0,1,2.
\]
Their product is
\[
(A-2B)^3-3AB(A-2B)-2\operatorname{Re}(w_j\overline{w_i}).
\]
Expanding and using \(|w_i|^2=B^3\), \(|w_j|^2=A^3\) gives
\[
|w_j-w_i|^2-9B(A-B)^2.
\]
The product vanishes exactly when at least one of its three real factors
vanishes, which proves both directions of (1).

Two consequences are useful. Distinct equal-radius orbits cannot be
adjacent: (1) would imply \(w_i=w_j\), hence identical orbits. Also, two
distinct orbits cannot have edges in both directions. Indeed, the two
versions of (1) imply \(9(t_i-t_j)^3=0\), reducing to the first case.

## A metric restriction on every triangle

Suppose three orbits form a complete underlying triangle. Their radii are
distinct; write their squared radii as \(a<b<c\). The extreme edge must
point from the orbit of radius \(\sqrt a\) to that of radius \(\sqrt c\).

For if it pointed the other way, (1) would give extreme distance
\(3\sqrt c(c-a)\) in the \(w\)-plane. The other two distances are at most
\(3\sqrt b(b-a)\) and \(3\sqrt c(c-b)\), respectively, regardless of
their directions. Their sum is strictly less than \(3\sqrt c(c-a)\),
contradicting the triangle inequality.

The same reasoning gives a more general path restriction. A descending
edge from squared radius \(t_k\) to \(t_0<t_k\) cannot coexist with an
underlying path through strictly increasing squared radii
\(t_0<t_1<\cdots<t_k\) of length at least two. Each path-edge distance is
at most \(3\sqrt{t_{j+1}}(t_{j+1}-t_j)\); the sum is strictly less than
the distance of the descending edge.

## At least six orbits are necessary in this construction

There are no loops or two-way edges. Minimum outdegree two therefore
requires at least five orbits. With exactly five, there must be ten
directed edges, one on every unordered pair, and every outdegree is two.
All five radii are distinct.

The largest-radius orbit cannot point to any orbit except the
second-largest: otherwise an orbit of intermediate radius would complete
a triangle with a forbidden descending extreme edge. Thus its outdegree
is at most one, a contradiction.

Consequently this construction needs at least six orbits, or 18 points.
This is **not** a general 18-vertex lower bound for #97.

Further restricted exclusions and their additional hypotheses are in
`equilateral-cycle-completion.md`. The independent finite graph checker
is `verify-orbit-graphs.cpp`.

## Exact finite exclusion through seven orbits

The two additional geometric lemmas in `equilateral-cycle-completion.md`
say that a complete triangle cannot have its smallest-radius orbit as a
source of two edges, and that any fixed extreme-radius edge has at most
one intermediate orbit completing a reverse directed triangle.

The integer-only backtracking program `search-orbit-graphs.cpp` exhausts
all graphs with exactly two outgoing edges per vertex subject to these
necessary conditions. This suffices for minimum outdegree at least two:
delete excess outgoing edges independently at each vertex, and all the
forbidden-pattern conditions are preserved. The graph is represented by
its complete list of row-neighbor pairs. The search tries every such
pair, rejects two-way edges, and prunes only when already present edges
contain a forbidden pattern. No addition of further edges can repair one.

Ordering by nondecreasing radius is sufficient, even with ties. Equal-radius
orbits cannot be adjacent, so every triangle in an actual graph has three
distinct radii. Allowing more graphs than those compatible with ties can
only weaken an exclusion.

On 2026-09-04 the exhaustive seven-orbit run returned zero solutions.
The counts of consistent prefixes after assigning 0 through 7 rows were
respectively

```
1, 15, 160, 1080, 3756, 4674, 1274, 0
```

The independent all-ternary-state checker `verify-orbit-graphs.cpp` also
returned zero through six orbits. Thus **this construction requires at
least eight orbits, or 24 points**, to give four neighbors at each orbit's
internal side length.

The eight-orbit search returned 30,879 labeled graphs satisfying the
tested local conditions. This is evidence of the limitations of these
conditions, not evidence that any of those graphs has a convex geometric
realization. One example, with vertices ordered by radius, is

```
0: 4 5
1: 4 5
2: 6 7
3: 0 1
4: 2 3
5: 2 3
6: 0 1
7: 0 1
```

Reproduce the finite checks with a C++17 compiler:

```
clang++ -std=c++17 -O3 search-orbit-graphs.cpp -o search-orbit-graphs
./search-orbit-graphs 7
./search-orbit-graphs 8
```

The separate filename `eight-orbit-graphs.jsonl`, when generated with the
`dump` option, contains one graph per line, encoded as eight outgoing-neighbor
bit masks. It contains no point coordinates.

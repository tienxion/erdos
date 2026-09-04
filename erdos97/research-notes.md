# Erdős #97 — research status

**Unsolved in this work. No full proof or counterexample has been obtained.**
The user requires a new solution to the open problem and has restricted
this task to #97 exclusively. Earlier work on other problems does not
constitute progress toward this fixed target.

## Target

[Erdős problem #97](https://www.erdosproblems.com/97), listed with a $100
prize, asks whether every finite nonempty set in strictly convex position
has a vertex from which no positive distance occurs at four other vertices.
The radius may depend on the vertex. A counterexample must give exact
coordinates or a rigorous existence proof, verify strict convexity, and
verify four equal distances from every vertex. Approximate equalities,
abstract graphs, special-case exclusions, and known three-neighbor
constructions do not meet that target.

## Verified partial results

- `small-polygon-obstruction.md`: a general argument excludes at most
  eight vertices. Its nine-vertex abstract graph only passes necessary
  combinatorial tests; a further rhombus identity excludes its realization.
- `equilateral-orbits.md` and `equilateral-cycle-completion.md`: exact
  geometric restrictions for unions of equilateral triples, when each
  orbit uses its own triangle's side length as the repeated radius.
  Exact graph enumeration excludes this construction through seven
  orbits (21 points). Eight-orbit abstract graphs survive.
- `literature.md`: primary-source review, the known Danzer and
  Fishburn–Reeds constructions, and restrictions on possible extensions.
  The 20-point reflected Petersen construction cannot be upgraded to
  minimum cross-degree four while keeping all its existing cross-edges.
  The circle-radius and convex-cut assumptions of those results are
  explicit in that file.

None of these is asserted to be original or to settle the general problem.

## Current direction

The immediate construction route examines the surviving eight-orbit graphs
using the actual circle incidences and strict convexity, beyond the local
triangle conditions. The 30,879 labeled graphs were grouped into 400
directed isomorphism classes using full directed-isomorphism checks.
Geometric searches on those representatives must allow every radius order.

A first heuristic pass tried two deterministic initializations per class,
with a cap of 250 least-squares function evaluations per initialization.
The files `metric-search-000-100.json` through `metric-search-300-400.json`
contain the best optimizer compromise retained for each class. Of these,
52 had all 24 points on the numerical convex hull and minimum separation
above 0.02. The smallest maximum original normalized squared-distance
error was about 0.0060143 (class 27), far from an exact solution. No
counterexample candidate passed the distance requirements. This is a
failed heuristic search, **not** an exclusion of the 400 graph types.
Its separation and convexity penalties are search choices and must not
be treated as necessary bounds on a possible counterexample.

A separate numerical search by a collaborator found very small distance
residuals in a K4,4 family but failed convexity. It is not a certificate
of an exact configuration. Such a point set must not be reported as a
counterexample. `cyclic-order-filter-limitations.md` explains why the
common-predecessor alternation test alone cannot eliminate those graphs.

If a candidate is found, the next required steps are an exact existence
certificate, a full convexity check, all required distance equalities,
and independent proof review. If the construction is ruled out, that
remains a restriction on one route, not a proof of #97.

## Reproduction

`verify-combinatorial-witness.py` uses the Python standard library.
The two C++ graph checkers use integer and Boolean operations only.
Numerical/symbolic experiments use a local `.venv` containing NumPy,
SciPy, SymPy, mpmath, and NetworkX; those packages are not needed for the
stated finite graph exclusions. Saved graphs encode incidence constraints,
not geometric solutions. The independent proof review is `orbit-audit.md`;
its recorded hashes match the audited geometric arguments and C++ source.

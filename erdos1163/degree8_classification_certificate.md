# Independent certificate for the finite degree-eight classification

4 September 2026. Run:

    python3 erdos1163/verify_degree8_classification.py

The verifier uses only the Python standard library. It does not use
GAP, Sage, or the completeness of a transitive-group catalogue.
Explicit candidate model generators are read from degree8_groups.json;
the database IDs serve only as labels. Their relevant invariants are
recomputed directly from their permutations.

## Exhaustiveness of the enumeration

Let
$$
P=\langle(12),(13)(24),(15)(26)(37)(48)\rangle\leq S_8.
$$
The script constructs all its elements and verifies $|P|=128$.
Since $v_2(8!)=7$, this is a Sylow 2-subgroup. Every 2-subgroup of
$S_8$ is conjugate into $P$.

Starting from the trivial subgroup, the script repeatedly adjoins a
generator to every retained subgroup. It uses one representative per
right coset $Hg$, since $\langle H,hg\rangle=\langle H,g\rangle$.
It keeps every resulting subgroup, with no quotient by conjugacy.
The retained property is nilpotency class at most two and exponent
dividing four. This property is inherited by subgroups, so every
target subgroup has a generator chain entirely inside the retained
class and must occur in this search.

The pruning criterion is exact. For a previous generating set and
one new element, it checks that all generators have fourth power
one, every generator commutator centralizes every generator, and
these commutators have order at most two. Such a group has class at
most two, and the class-two power formula gives exponent dividing
four. Conversely every target group satisfies these conditions.

The outputs are then checked independently using all their elements:
closure, fourth powers, the center, and containment of every
commutator in the center are verified. Transitivity is tested by the
orbit of the first point.

## Results and conjugacy witnesses

There are **544** retained subgroups of $P$, of which **53** are
transitive. The latter belong to exactly the following nine
permutation conjugacy classes:

| Model ID | Order | Copies inside $P$ |
|---|---:|---:|
| 2 | 8 | 10 |
| 3 | 8 | 2 |
| 4 | 8 | 14 |
| 5 | 8 | 2 |
| 9 | 16 | 10 |
| 10 | 16 | 6 |
| 11 | 16 | 6 |
| 18 | 32 | 2 |
| 22 | 32 | 1 |

For each candidate model, all permutations fixing the first point are
examined as conjugators. These suffice: any conjugator from a
transitive model can be composed with an element of that model so
that it fixes the first point, without changing the conjugate group.
All conjugates contained in $P$ are therefore found.

Every one of the 53 transitive groups is matched to exactly one model,
and the matches from distinct models are disjoint. For each group,
the certificate records a conjugating permutation and checks its
action on every model element. This proves completeness and
distinctness of the nine classes without assuming that the original
candidate list was complete.

The machine-readable certificate is
degree8_classification_certificate.json. It includes the full element
list of $P$, every retained subgroup as a 128-bit membership set and
generating set, and all transitive-group conjugators. It also records
the independently recomputed orders, Frattini orders, center orders,
derived orders, generator ranks, and scalar polar ranks.

Finally, the two nonscalar square maps have direct witnesses in the
certificate. For model 10 it supplies quotient lifts $x,y$, central
basis $y^2,[x,y]$, and verifies $q=(Y^2,XY)$ on all four quotient
vectors. For model 18 it supplies involutory lifts $x,y,z$ with
$[y,z]=1$, independent central commutators $[x,y],[x,z]$, and
verifies $q=(XY,XZ)$ on all eight quotient vectors.

This is a finite computational proof component with an explicit
exhaustive algorithm and witnesses. It is separate from the
asymptotic counting argument.

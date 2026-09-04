# Computational verification

Run the following commands **from the repository root**. The scripts write
JSON reports beside themselves. All counts concern actual labelled subgroups
unless a script explicitly says it is enumerating conjugacy classes as an
intermediate step.

## Python standard library

No third-party packages are needed for these six scripts:

```sh
python3 erdos1163/verify.py
python3 erdos1163/verify_abelian.py
python3 erdos1163/verify_odd_family.py
python3 erdos1163/verify_small_orbits.py
python3 erdos1163/verify_extraspecial.py
python3 erdos1163/verify_degree8_classification.py
```

| Script | Checks |
|---|---|
| [verify.py](verify.py) | Gaussian coefficients, binary subspaces, elementary abelian counts, and initial families |
| [verify_abelian.py](verify_abelian.py) | Birkhoff counting, actual abelian permutation subgroups, and defect calculations |
| [verify_odd_family.py](verify_odd_family.py) | Odd-degree $S_3$ construction and coefficient comparisons |
| [verify_small_orbits.py](verify_small_orbits.py) | Class-two subgroup parameterization and small permutation examples |
| [verify_extraspecial.py](verify_extraspecial.py) | The eight-point group and normalizer, counts, coefficients, and moments |
| [verify_degree8_classification.py](verify_degree8_classification.py) | Exhaustive classification inside an explicit Sylow 2-subgroup of $S_8$ |

The last script uses explicit generators from [degree8_groups.json](degree8_groups.json)
as candidate models, but independently proves completeness and checks their
invariants. See the [certificate explanation](degree8_classification_certificate.md)
and [machine-readable certificate](degree8_classification_certificate.json).

## SageMath / GAP

The following need SageMath with GAP's transitive-group data:

```sh
sage -python erdos1163/classify_degree8.py
sage -python erdos1163/verify_eight_point_models.py
sage -python erdos1163/verify_bad_orbit_quotients.py
```

They produce the initial model table, check the two nonscalar square maps,
and check all 470 normal quotients of the exceptional transitive subgroup
classes. They were originally run with SageMath 10.7.

These computations support the longer research notes. The [submitted proof](proof.md)
is a self-contained counting argument and requires no finite-group
classification or computational assumption. Finite checks do not establish
the asymptotic arguments by themselves.

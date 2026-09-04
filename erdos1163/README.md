# Erdős 1163 research

Start with [results.md](results.md).
It states the strongest theorems, their sampling measures, proof
locations, and the remaining unrestricted problem.

Status: substantial partial results with written proofs, independent
agent audits, and finite checks. This is not a solution of Erdős 1163.
Novelty has not been established. Any submission is explicitly a partial
result with AI disclosure, not a claim to solve the unrestricted problem.

## Files

- [order_spectrum.md](order_spectrum.md): uniform exact-order counts for every exponent between floor(n/4) and floor(n/2), and a sharper matching estimate inside Q_n.
- [website_note_draft.md](website_note_draft.md): self-contained proof of the exact-order result selected for submission.
- [extension_eight_point_projections.md](extension_eight_point_projections.md): all class-two exponent-four 2-subgroups with orbit sizes at most eight.
- [special_structure.md](special_structure.md): typical center, derived subgroup, Frattini subgroup, and generator number in that full class.
- [extension_one_bad_orbit.md](extension_one_bad_orbit.md): up to logarithmically many arbitrary exceptional eight-point projections.
- [progress.md](progress.md): elementary abelian asymptotics, the dihedral/Klein-four family, and its order central limit theorem.
- [progress_v2.md](progress_v2.md): all abelian subgroups, an explicit asymptotic formula, an unrestricted bound on abelian probability, and the odd-degree S3 obstruction.
- [extension_small_orbits.md](extension_small_orbits.md): all 2-subgroups with orbit sizes at most four, including arbitrary subdirects and cyclic projections.
- [extension_efficient_orbits.md](extension_efficient_orbits.md): arbitrary subdirects with the specified two-, four-, and eight-point projections.
- [progress_v3.md](progress_v3.md): eight-point factors, the explicit 7/8 lower bound, stronger unrestricted exclusion estimates, and the new order law.
- [verify.py](verify.py): exact binary and first-family checks.
- [verify_abelian.py](verify_abelian.py): Birkhoff, actual abelian permutation subgroup, and rank-defect checks.
- [verify_odd_family.py](verify_odd_family.py): independent S3-family checks and coefficient asymptotics.
- [verify_small_orbits.py](verify_small_orbits.py): exact class-two counts and actual permutation comparisons.
- [verify_extraspecial.py](verify_extraspecial.py): eight-point group and normalizer, exact order counts, and coefficient and moment checks.

The five original verification scripts above and
`verify_degree8_classification.py` use Python 3 without external packages.
The latter independently enumerates all 544 qualifying subgroups of an
explicit Sylow group and identifies its 53 transitive subgroups with nine
models. Its argument and certificate are explained in
`degree8_classification_certificate.md`.

`verify_eight_point_models.py`, `verify_bad_orbit_quotients.py`, and
`classify_degree8.py` run with SageMath (`sage -python filename.py`).
The quotient check includes all 470 normal quotients of the exceptional
transitive Sylow-subgroup classes. Each script writes a JSON report.

Independent proof reports are in `audit_abelian.md`, `audit_families.md`,
`audit_small_orbits.md`, `audit_extraspecial.md`,
`audit_extraspecial_clt.md`, `audit_efficient_orbits.md`,
`audit_eight_point_projections.md`, `audit_special_structure.md`,
`audit_bad_orbit_extension.md`, and `audit_order_spectrum.md`.

The exact-order result was submitted as a partial proof to the Erdős
1163 website on 4 September 2026 and is awaiting moderator approval.
The public writeup is at
https://erdos-1163-order-counts.groggorius-george.chatgpt.site.
See `submission_record.md` for the receipt and precise disclosures.
No drafts outside this research directory were modified.

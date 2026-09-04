"""Verify the finite quotient bound used for a single bad eight-point orbit.

Run with: sage -python research/erdos1163/verify_bad_orbit_quotients.py

This enumerates subgroups of a Sylow 2-subgroup of S8 rather than relying
on the transitive-group catalogue. Sylow conjugacy guarantees coverage
of every actual transitive 2-group in S8 up to S8-conjugacy.
"""
from sage.all import libgap
from pathlib import Path
import json


def run():
    symmetric = libgap.SymmetricGroup(8)
    sylow = symmetric.SylowSubgroup(2)
    assert int(sylow.DerivedSubgroup().Size()) == 16
    assert len(list(sylow.LowerCentralSeries())) - 1 == 4
    efficient = libgap.eval(
        "Group((1,2)(3,4),(1,2)(5,6),(1,2)(7,8),"
        "(1,3)(2,4)(5,7)(6,8),(1,5)(2,6)(3,7)(4,8))"
    )
    assert int(efficient.Size()) == 32
    classes = list(sylow.ConjugacyClassesSubgroups())
    checked = []
    excluded = []
    for cls in classes:
        group = cls.Representative()
        if not bool(libgap.IsTransitive(group, libgap(list(range(1, 9))))):
            continue
        order = int(group.Size())
        rank = (order // int(group.FrattiniSubgroup().Size())).bit_length() - 1
        if rank == 4:
            assert order == 32 and int(group.Center().Size()) == 2
            assert int(group.DerivedSubgroup().Size()) == 2
            assert bool(libgap.IsConjugate(symmetric, efficient, group))
            excluded.append(str(group.GeneratorsOfGroup()))
            continue
        lower = list(group.LowerCentralSeries())
        gamma3 = lower[2] if len(lower) > 2 else group.TrivialSubgroup()
        powers = libgap.Subgroup(group, libgap([g ** 4 for g in group.Elements()]))
        kill = libgap.ClosureGroup(gamma3, powers)
        tested = 0
        class2_tested = 0
        maximum = 0
        maximum_normal_rank = 0
        for kernel in group.NormalSubgroups():
            quotient = libgap.FactorGroup(group, kernel)
            center = int(quotient.Center().Size())
            derived = int(quotient.DerivedSubgroup().Size())
            assert center ** 2 * derived <= 64, (
                group, kernel, quotient, center, derived
            )
            maximum = max(maximum, center ** 2 * derived)
            tested += 1
            if bool(libgap.IsSubgroup(kernel, kill)):
                class2_tested += 1
            normal_frattini = libgap.ClosureGroup(
                kernel.FrattiniSubgroup(),
                libgap.CommutatorSubgroup(kernel, group),
            )
            normal_rank = (
                int(kernel.Size()) // int(normal_frattini.Size())
            ).bit_length() - 1
            maximum_normal_rank = max(maximum_normal_rank, normal_rank)
        assert maximum_normal_rank <= 3
        checked.append({
            "generators": str(group.GeneratorsOfGroup()),
            "order": order,
            "rank": rank,
            "normal_quotients_tested": tested,
            "class2_exponent4_quotients_tested": class2_tested,
            "max_center_squared_times_derived": maximum,
            "max_normal_generator_rank": maximum_normal_rank,
        })
    result = {
        "sylow_order": int(sylow.Size()),
        "sylow_derived_order": int(sylow.DerivedSubgroup().Size()),
        "sylow_nilpotency_class": len(list(sylow.LowerCentralSeries())) - 1,
        "sylow_subgroup_conjugacy_classes": len(classes),
        "transitive_bad_classes_checked": len(checked),
        "efficient_classes_excluded": len(excluded),
        "quotients_checked": sum(row["normal_quotients_tested"] for row in checked),
        "class2_exponent4_quotients_checked": sum(
            row["class2_exponent4_quotients_tested"] for row in checked
        ),
        "all_bounds_passed": True,
        "efficient_exclusion_verified_by_S8_conjugacy": True,
        "efficient_model_generators": str(efficient.GeneratorsOfGroup()),
        "rows": checked,
        "efficient_generators": excluded,
    }
    destination = Path(__file__).with_name("bad_orbit_quotient_verification.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print({k: v for k, v in result.items() if k not in ("rows", "efficient_generators")})


if __name__ == "__main__":
    run()

"""Check the finite square-map inputs to extension_eight_point_projections.md.

Run with: sage -python erdos1163/verify_eight_point_models.py
These are exact finite checks, not substitutes for the asymptotic proof.
"""
from sage.all import libgap, matrix, GF
from itertools import product
from pathlib import Path
import json


def group_from_cycles(cycles):
    return libgap.Group([libgap.eval(cycle) for cycle in cycles])


def product_of_powers(generators, bits):
    result = generators[0] ** 0
    for generator, bit in zip(generators, bits):
        if bit:
            result *= generator
    return result


def run():
    checks = []
    x10 = libgap.eval('(5,6)(7,8)')
    y10 = libgap.eval('(1,2,3,4)(5,7)')
    model10 = libgap.Group([x10, y10])
    source10 = libgap.TransitiveGroup(8, 10)
    assert int(model10.Size()) == 16
    assert libgap.IsomorphismGroups(model10, source10) != libgap.fail
    phi10 = model10.FrattiniSubgroup()
    z10 = libgap.Comm(x10, y10)
    square10 = y10 ** 2
    assert int(libgap.Group([square10, z10]).Size()) == 4
    assert libgap.Group([square10, z10]) == phi10
    assert int(libgap.Action(model10, [1, 2, 3, 4]).Size()) == 4
    assert int(libgap.Action(model10, [5, 6, 7, 8]).Size()) == 8
    for X, Y in product(range(2), repeat=2):
        element = product_of_powers([x10, y10], [X, Y])
        assert element ** 2 == square10 ** Y * z10 ** (X * Y)
    checks.append('ID10 is isomorphic to the specified C4 x D8 fiber product; '
                  'both virtual projections are onto and q=(Y^2,XY) exactly.')

    x18 = libgap.eval('(1,5)(2,6)(3,7)(4,8)')
    y18 = libgap.eval('(1,2)(3,4)')
    z18 = libgap.eval('(1,3)(2,4)')
    model18 = libgap.Group([x18, y18, z18])
    source18 = libgap.TransitiveGroup(8, 18)
    assert int(model18.Size()) == 32
    assert libgap.IsomorphismGroups(model18, source18) != libgap.fail
    p18 = libgap.Comm(x18, y18)
    q18 = libgap.Comm(x18, z18)
    assert libgap.Group([p18, q18]) == model18.FrattiniSubgroup()
    assert int(libgap.Group([p18, q18]).Size()) == 4
    for X, Y, Z in product(range(2), repeat=3):
        element = product_of_powers([x18, y18, z18], [X, Y, Z])
        assert element ** 2 == p18 ** (X * Y) * q18 ** (X * Z)
    checks.append('ID18 is isomorphic to V4 wreath C2, with independent central '
                  'Frattini coordinates and q=(XY,XZ) exactly.')

    scalar_rows = []
    for idx in [2, 3, 4, 5, 9, 11, 22]:
        group = libgap.TransitiveGroup(8, idx)
        generators = list(group.MinimalGeneratingSet())
        phi_order = int(group.FrattiniSubgroup().Size())
        one = generators[0] ** 0
        entries = [[0 if libgap.Comm(x, y) == one else 1
                    for y in generators] for x in generators]
        polar_rank = int(matrix(GF(2), entries).rank())
        assert polar_rank == {2: 0, 3: 0, 4: 2, 5: 2, 9: 2, 11: 2, 22: 4}[idx]
        assert phi_order in [1, 2]
        zero_squares = sum(product_of_powers(generators, bits) ** 2 == one
                           for bits in product(range(2), repeat=len(generators)))
        if idx == 22:
            assert zero_squares == 10
        scalar_rows.append(dict(transitive_id=idx,
                                generator_rank=len(generators),
                                frattini_order=phi_order,
                                polar_rank=polar_rank,
                                zeros_of_square_form=zero_squares))
    checks.append('All seven scalar-Frattini degree8 types have the asserted '
                  'polar ranks; E has exactly10 singular quotient vectors.')
    result = dict(checks=checks, scalar_projection_models=scalar_rows)
    destination = Path(__file__).with_name('eight_point_model_verification.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    for check in checks:
        print(check, flush=True)
    print(f'Saved {destination}')


if __name__ == '__main__':
    run()

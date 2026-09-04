"""Independent finite classification inside an explicit Sylow 2-group of S8.

Only the Python standard library is used. No transitive-group database is
used to enumerate or filter subgroups. The explicit candidate models are
read from degree8_groups.json; every retained subgroup is supplied with
a directly verified permutation conjugator to exactly one model.

Run: python3 erdos1163/verify_degree8_classification.py
"""

from collections import Counter, deque
from itertools import permutations
from pathlib import Path
import json
import re
import time

HERE = Path(__file__).resolve().parent
ONE = tuple(range(8))


def mul(a, b):
    return tuple(a[b[i]] for i in range(8))


def inverse(a):
    b = [0] * 8
    for i, j in enumerate(a):
        b[j] = i
    return tuple(b)


def cycle_perm(text):
    p = list(range(8))
    for cyc in re.findall(r"\(([^()]*)\)", text):
        if not cyc.strip():
            continue
        xs = [int(i.strip()) - 1 for i in cyc.split(",")]
        for a, b in zip(xs, xs[1:] + xs[:1]):
            p[a] = b
    return tuple(p)


def parse_generators(text):
    s = text.strip()[1:-1]
    parts, depth, start = [], 0, 0
    for i, c in enumerate(s):
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif c == "," and depth == 0:
            parts.append(s[start:i].strip())
            start = i + 1
    parts.append(s[start:].strip())
    return tuple(cycle_perm(p) for p in parts if p)


def permutation_group(gens):
    found = {ONE}
    queue = [ONE]
    for x in queue:
        for g in gens:
            y = mul(x, g)
            if y not in found:
                found.add(y)
                queue.append(y)
    return tuple(queue)


def commutator(x, y):
    return mul(mul(mul(inverse(x), inverse(y)), x), y)


def actual_model_invariants(gens, elements):
    comms = tuple(commutator(x, y) for x in gens for y in gens)
    derived = permutation_group(comms)
    phi = permutation_group(
        tuple(mul(x, x) for x in elements) + comms
    )
    center = [x for x in elements
              if all(mul(x, y) == mul(y, x) for y in elements)]
    quotient_size = len(elements) // len(phi)
    assert quotient_size & (quotient_size - 1) == 0
    central_quotient_size = len(elements) // len(center)
    return dict(
        order=len(elements),
        generator_rank=quotient_size.bit_length() - 1,
        frattini_order=len(phi),
        derived_order=len(derived),
        center_order=len(center),
        exponent=4 if any(mul(x, x) != ONE for x in elements) else 2,
        nilpotency_class=1 if len(derived) == 1 else 2,
        scalar_polar_rank=(
            central_quotient_size.bit_length() - 1
            if len(phi) == 2 else None
        ),
    )


def special_square_witness(model_id, gens, elements):
    """Explicit bases proving the two multi-coordinate square maps."""
    phi = set(permutation_group(
        tuple(mul(x, x) for x in elements)
        + tuple(commutator(x, y) for x in gens for y in gens)
    ))
    if model_id == 10:
        x, y = gens
        c, z = mul(y, y), commutator(x, y)
        assert mul(x, x) == ONE
        assert len({ONE, c, z, mul(c, z)}) == 4
        assert {ONE, c, z, mul(c, z)} == phi
        assert all(mul(w, g) == mul(g, w)
                   for w in (c, z) for g in gens)
        quotient_basis, central_basis = (x, y), (c, z)
        forms = ["Y^2", "X*Y"]
    elif model_id == 18:
        involutions = [x for x in elements
                       if x not in phi and mul(x, x) == ONE]
        witness = None
        for x in involutions:
            if witness:
                break
            for y in involutions:
                if witness:
                    break
                c = commutator(x, y)
                if c == ONE:
                    continue
                for z in involutions:
                    d = commutator(x, z)
                    if d in (ONE, c) or commutator(y, z) != ONE:
                        continue
                    if len(permutation_group((x, y, z))) == len(elements):
                        witness = x, y, z, c, d
                        break
        assert witness is not None
        x, y, z, c, d = witness
        assert {ONE, c, d, mul(c, d)} == phi
        assert all(mul(w, g) == mul(g, w)
                   for w in (c, d) for g in gens)
        quotient_basis, central_basis = (x, y, z), (c, d)
        forms = ["X*Y", "X*Z"]
    else:
        return None

    # Check every binary quotient vector, using these exact lifts.
    dim = len(quotient_basis)
    for v in range(1 << dim):
        lift = ONE
        for i, g in enumerate(quotient_basis):
            if v >> i & 1:
                lift = mul(lift, g)
        x = v & 1
        y = v >> 1 & 1
        z = v >> 2 & 1
        cs = (y, x & y) if model_id == 10 else (x & y, x & z)
        expected = ONE
        for bit, g in zip(cs, central_basis):
            if bit:
                expected = mul(expected, g)
        assert mul(lift, lift) == expected
    return dict(
        quotient_basis_lifts=[[i + 1 for i in p] for p in quotient_basis],
        central_basis=[[i + 1 for i in p] for p in central_basis],
        square_forms=forms,
        all_quotient_vectors_checked=1 << dim,
    )


def bits(mask):
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def run():
    started = time.monotonic()
    pgens = tuple(map(cycle_perm, [
        "(1,2)", "(1,3)(2,4)", "(1,5)(2,6)(3,7)(4,8)"
    ]))
    ps = permutation_group(pgens)
    assert len(ps) == 128 and ps[0] == ONE
    lookup = {p: i for i, p in enumerate(ps)}
    table = [[lookup[mul(x, y)] for y in ps] for x in ps]
    inv = [lookup[inverse(x)] for x in ps]
    square = [table[i][i] for i in range(128)]
    fourth = [square[square[i]] for i in range(128)]
    comm = [[table[table[table[inv[x]][inv[y]]][x]][y]
             for y in range(128)] for x in range(128)]
    allmask = (1 << 128) - 1

    def eligible(gens, g):
        """Exact generator criterion for class at most 2 and exponent <=4."""
        if fourth[g] != 0:
            return False
        # Previously central generator commutators must commute with g.
        for i, x in enumerate(gens):
            for y in gens[:i]:
                if comm[comm[x][y]][g] != 0:
                    return False
        # All new commutators must be central of exponent at most two.
        for x in gens:
            c = comm[x][g]
            if square[c] != 0 or comm[c][g] != 0:
                return False
            if any(comm[c][y] != 0 for y in gens):
                return False
        return True

    def closure_indices(gens, initial=1):
        mask = initial
        queue = bits(mask)
        for x in queue:
            row = table[x]
            for g in gens:
                y = row[g]
                bit = 1 << y
                if not mask & bit:
                    mask |= bit
                    queue.append(y)
        return mask

    # Every subgroup in the target class has a generator chain inside
    # that class. One representative per right H-coset suffices, since
    # <H,hg>=<H,g>. We retain all resulting groups, never only conjugacy
    # representatives.
    subgroups = {1: ()}
    pending = deque([1])
    attempted = 0
    while pending:
        hmask = pending.popleft()
        hgens = subgroups[hmask]
        hs = bits(hmask)
        remaining = allmask ^ hmask
        while remaining:
            bit = remaining & -remaining
            g = bit.bit_length() - 1
            coset = 0
            for h in hs:
                coset |= 1 << table[h][g]
            remaining &= ~coset
            attempted += 1
            if not eligible(hgens, g):
                continue
            gens = hgens + (g,)
            newmask = closure_indices(gens, hmask)
            if newmask not in subgroups:
                subgroups[newmask] = gens
                pending.append(newmask)

    # Check the outputs by an all-elements test independent of the
    # generator criterion used to prune the search.
    transitive = set()
    for hmask, hgens in subgroups.items():
        hs = bits(hmask)
        assert closure_indices(hgens) == hmask
        assert all(fourth[x] == 0 for x in hs)
        assert all(hmask & (1 << table[x][y]) for x in hs for y in hs)
        center = {x for x in hs if all(comm[x][y] == 0 for y in hs)}
        assert all(comm[x][y] in center for x in hs for y in hs)
        if len({ps[x][0] for x in hs}) == 8:
            transitive.add(hmask)

    print(f"Enumerated {len(subgroups)} class<=2 exponent<=4 subgroups "
          f"of P; {len(transitive)} transitive; {attempted} adjunctions.",
          flush=True)

    source = json.loads((HERE / "degree8_groups.json").read_text())
    models = [row for row in source
              if row["nilpotency_class"] <= 2 and row["exponent"] <= 4]
    coverage = {}
    model_data = []
    for row in models:
        model_id = row["transitive_id"]
        mgens = parse_generators(row["generators"])
        ms = permutation_group(mgens)
        assert len(ms) == row["order"]
        assert len({x[0] for x in ms}) == 8
        invariants = actual_model_invariants(mgens, ms)
        for key, value in invariants.items():
            if key in row:
                assert row[key] == value, (model_id, key, row[key], value)
        found = set()
        for tail in permutations(range(1, 8)):
            sigma = (0,) + tail
            sigma_inv = inverse(sigma)
            conjugate_gens = []
            for g in mgens:
                pg = mul(mul(sigma, g), sigma_inv)
                idx = lookup.get(pg)
                if idx is None:
                    break
                conjugate_gens.append(idx)
            else:
                hmask = closure_indices(tuple(conjugate_gens))
                assert hmask in transitive
                found.add(hmask)
                if hmask in coverage:
                    assert coverage[hmask]["model_id"] == model_id, (
                        "Candidate models are conjugate", model_id,
                        coverage[hmask]["model_id"])
                else:
                    # Verify the witness on every model element, not just
                    # the generators or its alleged database properties.
                    image = {lookup[mul(mul(sigma, x), sigma_inv)]
                             for x in ms}
                    assert image == set(bits(hmask))
                    coverage[hmask] = dict(
                        model_id=model_id,
                        conjugator=[i + 1 for i in sigma],
                    )
        assert found
        model_entry = dict(
            model_id=model_id, structure=row["structure"],
            generators=[[i + 1 for i in g] for g in mgens],
            copies_in_P=len(found), **invariants,
        )
        square_witness = special_square_witness(model_id, mgens, ms)
        if square_witness is not None:
            model_entry["square_map_witness"] = square_witness
        model_data.append(model_entry)
        print(f"Model {model_id}: order {len(ms)}, "
              f"{len(found)} conjugates inside P.", flush=True)

    assert set(coverage) == transitive, (
        "Unclassified transitive groups", len(transitive - set(coverage)))
    certificate = dict(
        method="standard-library exhaustive generator-adjoining in explicit P",
        degree=8,
        sylow_order=len(ps),
        sylow_generators=[[i + 1 for i in g] for g in pgens],
        sylow_elements=[[i + 1 for i in p] for p in ps],
        class2_exponent4_subgroup_count=len(subgroups),
        transitive_count=len(transitive),
        subgroup_counts_by_order=dict(sorted(Counter(
            mask.bit_count() for mask in subgroups).items())),
        transitive_counts_by_order=dict(sorted(Counter(
            mask.bit_count() for mask in transitive).items())),
        generator_adjunctions=attempted,
        models=model_data,
        all_subgroups=[
            dict(mask_hex=f"{mask:032x}", generators=list(subgroups[mask]),
                 transitive=mask in transitive,
                 **coverage.get(mask, {}))
            for mask in sorted(subgroups)
        ],
        elapsed_seconds=round(time.monotonic() - started, 3),
    )
    out = HERE / "degree8_classification_certificate.json"
    out.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"All {len(transitive)} transitive groups classified into "
          f"{len(models)} pairwise distinct conjugacy classes.")
    print(f"Certificate: {out}")
    print(f"Elapsed {certificate['elapsed_seconds']} seconds")


if __name__ == "__main__":
    run()

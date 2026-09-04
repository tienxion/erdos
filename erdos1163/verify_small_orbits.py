#!/usr/bin/env python3
"""Exact class-two checks for extension_small_orbits.md; standard library only.

No asymptotic assertion is inferred from these finite checks.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, factorial
from pathlib import Path
import json

from verify import all_binary_subspaces, brute_family_from_two_subgroups, family_counts


@lru_cache(None)
def spaces(rank):
    return tuple(all_binary_subspaces(rank))


@lru_cache(None)
def ambient_subdirect_counts(a, c, d, e, f=0):
    """Full projections in C2^a x C4^c x D8^d x V4^e x E8^f by log2 order.

    Enumerate the image U and the central kernel W independently. Test
    the exact condition q(U) <= W, then count 2^(dim U * codim W) lifts.
    """
    r = a + c + 2 * d + 2 * e + 4 * f
    z = c + d + f
    out = Counter()
    nonsaturated = Counter()
    factors = []
    cursor = 0
    for size in [1] * (a + c) + [2] * (d + e) + [4] * f:
        factors.append((cursor, size))
        cursor += size
    assert cursor == r

    def square(v):
        result = 0
        for j in range(c):
            result |= ((v >> (a + j)) & 1) << j
        for j in range(d):
            pair = (v >> (a + c + 2 * j)) & 3
            if pair == 3:
                result |= 1 << (c + j)
        for j in range(f):
            four = (v >> (a + c + 2 * d + 2 * e + 4 * j)) & 15
            if ((four & 3) == 3) ^ (((four >> 2) & 3) == 3):
                result |= 1 << (c + d + j)
        return result

    for u in spaces(r):
        if any(len({(v >> start) & ((1 << width) - 1) for v in u}) != (1 << width)
               for start, width in factors):
            continue
        k = len(u).bit_length() - 1
        values = {square(v) for v in u}
        for w in spaces(z):
            if not values.issubset(w):
                continue
            w_rank = len(w).bit_length() - 1
            t = z - w_rank
            count = 1 << (k * t)
            out[k + w_rank] += count
            if t:
                nonsaturated[k + w_rank] += count
    return dict(out), dict(nonsaturated)


def small_orbit_counts(n):
    out = Counter()
    with_cyclic = 0
    cyclic_free_nonsaturated = 0
    extra_fixed = 0
    for f in range(n % 2, n + 1, 2):
        m = (n - f) // 2
        for b in range(m // 2 + 1):
            a = m - 2 * b
            partitions = factorial(n) // (
                factorial(f) * 2 ** a * factorial(a) * 24 ** b * factorial(b))
            for c in range(b + 1):
                for d in range(b - c + 1):
                    e = b - c - d
                    choices = comb(b, c) * comb(b - c, d) * 3 ** (c + d)
                    hist, nonsat = ambient_subdirect_counts(a, c, d, e)
                    scale = partitions * choices
                    for k, count in hist.items():
                        out[k] += scale * count
                    if f > n % 2:
                        extra_fixed += scale * sum(hist.values())
                    elif c:
                        with_cyclic += scale * sum(hist.values())
                    else:
                        cyclic_free_nonsaturated += scale * sum(nonsat.values())
    return out, with_cyclic, cyclic_free_nonsaturated, extra_fixed


def run():
    # Independent elementary Goursat counts for small direct products.
    assert ambient_subdirect_counts(0, 0, 2, 0) == (
        {3: 8, 4: 6, 5: 9, 6: 1}, {3: 8})
    assert ambient_subdirect_counts(0, 2, 0, 0) == (
        {2: 2, 3: 1, 4: 1}, {2: 2})
    assert ambient_subdirect_counts(0, 1, 1, 0) == (
        {4: 3, 5: 1}, {})
    assert ambient_subdirect_counts(0, 0, 1, 0, 1) == (
        {6: 210, 7: 45, 8: 1}, {})
    def plus_form(v):
        return ((v & 3) == 3) ^ (((v >> 2) & 3) == 3)
    def linear_map(columns, v):
        result = 0
        for j, column in enumerate(columns):
            if (v >> j) & 1:
                result ^= column
        return result
    isometries = 0
    for columns in product(range(1, 16), repeat=4):
        if len({linear_map(columns, v) for v in range(16)}) != 16:
            continue
        if all(plus_form(linear_map(columns, v)) == plus_form(v) for v in range(16)):
            isometries += 1
    assert isometries == 72
    checks = [
        "D8 x D8: 24 subdirects, including 8 nonsaturated diagonal graphs.",
        "C4 x C4: 4 subdirects, including 2 nonsaturated diagonal graphs.",
        "C4 x D8: 4 subdirects, all saturated.",
        "D8 x E8: 256 subdirects, all saturated; order counts 210,45,1.",
        "Exactly 72 invertible binary 4 by 4 maps preserve the plus quadratic form."
    ]
    independently_enumerated = {}
    for n in [4, 5, 6]:
        count, _ = brute_family_from_two_subgroups(n)
        independently_enumerated[n] = count
    rows = []
    for n in range(1, 13):
        hist, cyclic, nonsat, fixed = small_orbit_counts(n)
        total = sum(hist.values())
        family = sum(family_counts(n)[0])
        assert total == family + cyclic + nonsat + fixed
        if n in independently_enumerated:
            assert total == independently_enumerated[n]
            checks.append(f"S_{n}: class-two count {total} matches independent permutation enumeration.")
        rows.append({
            "n": n,
            "total_with_orbits_at_most_four": total,
            "order_histogram": dict(sorted(hist.items())),
            "F_n": family,
            "cyclic_with_minimal_fixed_points": cyclic,
            "nonsaturated_cyclic_free_with_minimal_fixed_points": nonsat,
            "extra_fixed_points": fixed,
            "F_fraction": family / total,
        })
    result = {"checks": checks, "rows": rows}
    path = Path(__file__).with_name("small_orbit_verification.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    for check in checks:
        print(check)
    for row in rows:
        print(f"n={row['n']:2d} B_n={row['total_with_orbits_at_most_four']:12d} "
              f"F_n={row['F_n']:12d} F/B={row['F_fraction']:.6f}")
    print(f"Saved {path}")


if __name__ == "__main__":
    run()

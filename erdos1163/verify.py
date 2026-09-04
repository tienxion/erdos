#!/usr/bin/env python3
"""Exact checks for the accompanying Erdős 1163 research note.

Standard library only. Counts actual subgroups, not conjugacy classes.
The asymptotic theorems are proved in the note; these checks are not proofs.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations
from math import comb, factorial, log2, sqrt
from pathlib import Path
import json


@lru_cache(None)
def gaussian(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    if k == 0 or k == n:
        return 1
    return gaussian(n - 1, k) + (1 << (n - k)) * gaussian(n - 1, k - 1)


def convolve(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


@lru_cache(None)
def subdirect_counts(a, b):
    """Rank counts in F_2^a x (F_2^2)^b, onto every displayed factor."""
    coeff = [1]
    for _ in range(a):
        coeff = convolve(coeff, [1, -1])
    for _ in range(b):
        coeff = convolve(coeff, [1, -3, 2])
    m = a + 2 * b
    result = tuple(sum(c * gaussian(m - t, k) for t, c in enumerate(coeff))
                   for k in range(m + 1))
    assert all(x >= 0 for x in result)
    return result


def gl2(k):
    result = 1
    for j in range(k):
        result *= (1 << k) - (1 << j)
    return result


def elementary_counts(n):
    """Independent exact method: faithful E_k-actions / |GL(k,2)|.

    Count arbitrary actions by their labelled orbits, then invert on the
    subspace lattice of the common kernel.
    """
    m = n // 2
    hom = []
    for j in range(m + 1):
        h = [1] + [0] * n
        for s in range(1, n + 1):
            for d in range(j + 1):
                size = 1 << d
                if size > s:
                    break
                h[s] += (factorial(s - 1) // factorial(s - size)
                         * gaussian(j, d) * h[s - size])
        hom.append(h[n])
    result = []
    for k in range(m + 1):
        injections = sum(gaussian(k, j) * (-1) ** (k - j)
                         * (1 << ((k - j) * (k - j - 1) // 2)) * hom[j]
                         for j in range(k + 1))
        aut = gl2(k)
        assert injections >= 0 and injections % aut == 0
        result.append(injections // aut)
    return result


def family_counts(n):
    """Exact order counts for F_n and the elementary 2/4-orbit subfamily."""
    delta = n % 2
    m = n // 2
    full = [0] * (n + 1)
    elementary = [0] * (m + 1)
    weight4_ambient = 0
    weight1_ambient = 0
    pair_hist = Counter()
    for b in range(m // 2 + 1):
        a = m - 2 * b
        denom = factorial(delta) * (2 ** a) * factorial(a) * (24 ** b) * factorial(b)
        assert factorial(n) % denom == 0
        labelled = factorial(n) // denom
        ranks = subdirect_counts(a, b)
        weight1_ambient += labelled
        weight4_ambient += labelled * (4 ** b)
        pair_hist[a] += labelled * (4 ** b) * sum(ranks)
        for k, count in enumerate(ranks):
            elementary[k] += labelled * count
            for d in range(b + 1):
                full[k + d] += labelled * count * comb(b, d) * (3 ** d)
    return full, elementary, weight1_ambient, weight4_ambient, pair_hist


def all_binary_subspaces(m):
    """Independent brute force via spans represented as sets of binary words."""
    zero = frozenset([0])
    found = {zero}
    queue = [zero]
    for space in queue:
        for v in range(1, 1 << m):
            if v in space:
                continue
            bigger = space | frozenset(x ^ v for x in space)
            if bigger not in found:
                found.add(bigger)
                queue.append(bigger)
    return found


def brute_subdirect(a, b, spaces):
    counts = [0] * (a + 2 * b + 1)
    for space in spaces:
        if any({(v >> i) & 1 for v in space} != {0, 1} for i in range(a)):
            continue
        if any({(v >> (a + 2 * i)) & 3 for v in space} != {0, 1, 2, 3}
               for i in range(b)):
            continue
        counts[len(space).bit_length() - 1] += 1
    return tuple(counts)


def brute_elementary(n):
    """Enumerate elementary abelian subgroups as actual permutation sets."""
    identity = tuple(range(n))
    involutions = [p for p in permutations(range(n))
                   if p != identity and all(p[p[i]] == i for i in range(n))]
    def mul(p, q):
        return tuple(p[q[i]] for i in range(n))
    zero = frozenset([identity])
    seen = {zero}
    queue = [zero]
    for group in queue:
        for p in involutions:
            if p in group:
                continue
            if any(mul(p, q) != mul(q, p) for q in group):
                continue
            bigger = group | frozenset(mul(p, q) for q in group)
            if bigger not in seen:
                seen.add(bigger)
                queue.append(bigger)
    hist = Counter(len(g).bit_length() - 1 for g in seen)
    return [hist[k] for k in range(n // 2 + 1)]


def brute_family_from_two_subgroups(n):
    """Independent check: enumerate every 2-subgroup, then test F_n intrinsically.

    Used only through n=6. No Gaussian coefficients or quotient-space
    enumeration are used in this check.
    """
    identity = tuple(range(n))
    def mul(p, q):
        return tuple(p[q[i]] for i in range(n))
    def two_element(p):
        q = p
        for _ in range(n.bit_length()):
            if q == identity:
                return True
            q = mul(q, q)
        return q == identity
    candidates = [p for p in permutations(range(n))
                  if p != identity and two_element(p)]
    sylow_order = 1 << sum(n // (1 << j) for j in range(1, n.bit_length()))
    zero = frozenset([identity])
    seen = {zero}
    queue = [(zero, ())]
    for group, basis in queue:
        for p in candidates:
            if p in group:
                continue
            generators = basis + (p,)
            closure = {identity}
            pending = [identity]
            exceeded = False
            for q in pending:
                for g in generators:
                    product = mul(q, g)
                    if product not in closure:
                        closure.add(product)
                        pending.append(product)
                        if len(closure) > sylow_order:
                            exceeded = True
                            break
                if exceeded:
                    break
            if exceeded or len(closure) & (len(closure) - 1):
                continue
            closure = frozenset(closure)
            if closure not in seen:
                seen.add(closure)
                queue.append((closure, generators))
    hist = [0] * (n + 1)
    for group in seen:
        remaining = set(range(n))
        orbits = []
        while remaining:
            i = min(remaining)
            orbit = sorted({g[i] for g in group})
            orbits.append(orbit)
            remaining.difference_update(orbit)
        if sum(len(o) == 1 for o in orbits) != n % 2:
            continue
        accepted = True
        for orbit in orbits:
            if len(orbit) == 1:
                continue
            if len(orbit) not in [2, 4]:
                accepted = False
                break
            index = {x: j for j, x in enumerate(orbit)}
            projection = {tuple(index[g[x]] for x in orbit) for g in group}
            small_id = tuple(range(len(orbit)))
            if len(orbit) == 2:
                assert len(projection) == 2
            elif len(projection) == 4:
                if any(tuple(p[p[i]] for i in range(4)) != small_id for p in projection):
                    accepted = False  # cyclic order four, not regular V_4
                    break
            elif len(projection) == 8:
                nontrivial_squares = {tuple(p[p[i]] for i in range(4)) for p in projection}
                nontrivial_squares.discard(small_id)
                assert len(nontrivial_squares) == 1
                central = next(iter(nontrivial_squares))
                supported = list(identity)
                for i, x in enumerate(orbit):
                    supported[x] = orbit[central[i]]
                if tuple(supported) not in group:
                    accepted = False
                    break
            else:
                accepted = False
                break
        if accepted:
            hist[len(group).bit_length() - 1] += 1
    return len(seen), hist


def moments(hist):
    total = sum(hist)
    mean = sum(k * count for k, count in enumerate(hist)) / total
    second = sum(k * k * count for k, count in enumerate(hist)) / total
    return mean, second - mean * mean


def run():
    checks = []
    for m in range(7):
        spaces = all_binary_subspaces(m)
        assert len(spaces) == sum(gaussian(m, k) for k in range(m + 1))
        for b in range(m // 2 + 1):
            a = m - 2 * b
            assert brute_subdirect(a, b, spaces) == subdirect_counts(a, b)
        checks.append(f"All subdirect rank counts checked by enumerating F_2^{m} subspaces.")
    for n in range(1, 8):
        expected = elementary_counts(n)
        assert brute_elementary(n) == expected
        checks.append(f"S_{n}: actual elementary subgroup counts by rank = {expected}.")
    assert family_counts(4)[0] == [0, 3, 4, 3, 0]
    checks.append("F_4 order polynomial is 3 y + 4 y^2 + 3 y^3 (10 groups).")
    for n in [4, 5, 6]:
        two_count, expected = brute_family_from_two_subgroups(n)
        assert expected == family_counts(n)[0]
        checks.append(f"S_{n}: independently enumerated {two_count} 2-subgroups; "
                      f"intrinsic F_{n} order counts = {expected}.")
    rows = []
    for n in [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]:
        all_e = elementary_counts(n)
        f, e_good, c1, c4, pair_hist = family_counts(n)
        m = n // 2
        s = sum(gaussian(m, k) for k in range(m + 1))
        assert sum(e_good) <= sum(all_e)
        assert sum(f) <= c4 * s
        mean, variance = moments(f)
        row = {
            "n": n,
            "elementary_total_log2": log2(sum(all_e)),
            "family_total_log2": log2(sum(f)),
            "elementary_over_family_log2": log2(sum(all_e)) - log2(sum(f)),
            "elementary_good_fraction": sum(e_good) / sum(all_e),
            "elementary_asymptotic_ratio": sum(all_e) / (c1 * s),
            "family_asymptotic_ratio": sum(f) / (c4 * s),
            "family_mean_log2_order": mean,
            "family_variance_log2_order": variance,
            "family_mean_prediction": 7 * n / 16 - 3 / 8 * sqrt(3 * n / 8),
            "family_variance_over_n": variance / n,
            "expected_pair_orbits_over_sqrt_n": sum(a * c for a, c in pair_hist.items()) / sum(f) / sqrt(n),
        }
        rows.append(row)
    result = {"checks": checks, "rows": rows}
    out = Path(__file__).with_name("verification.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    for check in checks:
        print(check, flush=True)
    print("n   log2(E/F)   good_E     E/asympt  F/asympt   mean_F    variance/n")
    for row in rows:
        print(f"{row['n']:3d} {row['elementary_over_family_log2']:11.4f} "
              f"{row['elementary_good_fraction']:9.6f} "
              f"{row['elementary_asymptotic_ratio']:9.6f} "
              f"{row['family_asymptotic_ratio']:9.6f} "
              f"{row['family_mean_log2_order']:9.4f} "
              f"{row['family_variance_over_n']:10.6f}")
    print(f"Saved {out}")


if __name__ == "__main__":
    run()

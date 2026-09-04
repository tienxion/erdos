#!/usr/bin/env python3
"""Check the S_3-orbit construction and coefficient asymptotics."""
from itertools import permutations
from math import comb, factorial, log, exp, sqrt, pi, lgamma
from pathlib import Path
import json

from verify import subdirect_counts, family_counts


def odd_family_counts(n):
    assert n % 2 and n >= 3
    m = n // 2
    hist = [0] * (n + 1)
    for b in range((m - 1) // 2 + 1):
        a = m - 1 - 2 * b
        denom = 6 * 2 ** a * factorial(a) * 24 ** b * factorial(b)
        labelled = factorial(n) // denom
        assert factorial(n) % denom == 0
        for k, count in enumerate(subdirect_counts(a + 1, b)):
            for d in range(b + 1):
                hist[k + d] += labelled * count * comb(b, d) * 3 ** d
    return hist


def brute_all_and_odd(n):
    """Enumerate every subgroup of S_n; independently recognize G_n for n=3,5."""
    identity = tuple(range(n))
    elements = list(permutations(range(n)))
    def mul(p, q):
        return tuple(p[q[i]] for i in range(n))
    zero = frozenset([identity])
    seen = {zero}
    queue = [(zero, ())]
    for group, generators in queue:
        for p in elements:
            if p in group:
                continue
            gens = generators + (p,)
            closure = {identity}
            pending = [identity]
            for q in pending:
                for g in gens:
                    v = mul(q, g)
                    if v not in closure:
                        closure.add(v)
                        pending.append(v)
            closure = frozenset(closure)
            if closure not in seen:
                seen.add(closure)
                queue.append((closure, gens))
    hist = [0] * (n + 1)
    for group in seen:
        remaining = set(range(n))
        orbits = []
        while remaining:
            i = min(remaining)
            orbit = sorted({g[i] for g in group})
            remaining.difference_update(orbit)
            orbits.append(orbit)
        if sorted(map(len, orbits)) != ([3] if n == 3 else [2, 3]):
            continue
        triple = next(o for o in orbits if len(o) == 3)
        projection = {tuple(g[i] for i in triple) for g in group}
        if len(projection) != 6:
            continue
        three_cycle = list(identity)
        for i in range(3):
            three_cycle[triple[i]] = triple[(i + 1) % 3]
        if tuple(three_cycle) not in group:
            continue
        order = len(group)
        assert order % 3 == 0
        two_part = order // 3
        assert two_part & (two_part - 1) == 0
        hist[two_part.bit_length() - 1] += 1
    return len(seen), hist


def log_coefficient(N, w):
    assert N % 2 == 0
    m = N // 2
    terms = []
    for b in range(m // 2 + 1):
        a = m - 2 * b
        terms.append(b * log(w) - a * log(2) - lgamma(a + 1)
                     - b * log(24) - lgamma(b + 1))
    top = max(terms)
    return top + log(sum(exp(t - top) for t in terms))


def coefficient_asymptotic_log(N, w):
    return (-3 / (4 * w) - log(2 * pi * N) / 2
            + sqrt(3 * N / (2 * w)) + N / 4 * (1 + log(w) - log(6 * N)))


def run():
    checks = []
    for n, known_total in [(3, 6), (5, 156)]:
        total, hist = brute_all_and_odd(n)
        assert total == known_total
        assert hist == odd_family_counts(n)
        checks.append(f"Enumerated all {total} subgroups of S_{n}; G_{n} v_2-order histogram = {hist}.")
    rows = []
    for n in [5, 9, 17, 33, 65, 129, 257]:
        N = n - 1
        actual = sum(odd_family_counts(n)) / sum(family_counts(n)[0])
        prediction = sqrt(N / 24)
        rows.append({"n": n, "G_over_F": actual, "prediction": prediction,
                     "ratio_to_prediction": actual / prediction})
    coefficient_rows = []
    for N in [32, 64, 128, 256, 512, 1024]:
        for w in [1, 4]:
            ratio = exp(log_coefficient(N, w) - coefficient_asymptotic_log(N, w))
            coefficient_rows.append({"N": N, "w": w, "exact_over_asymptotic": ratio})
    out = Path(__file__).with_name("odd_family_verification.json")
    out.write_text(json.dumps({"checks": checks, "odd_ratios": rows,
                               "coefficient_ratios": coefficient_rows}, indent=2) + "\n")
    for line in checks:
        print(line)
    for row in rows:
        print(f"n={row['n']}: G/F={row['G_over_F']:.6f}; "
              f"sqrt((n-1)/24)={row['prediction']:.6f}; ratio={row['ratio_to_prediction']:.6f}")
    print(f"Saved {out}")


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""Exact checks for all_abelian.md; standard library only."""
from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from math import log2, sqrt
from pathlib import Path
import json
import random

from verify import elementary_counts


@lru_cache(None)
def partitions(n, cap=None):
    if not n:
        return ((),)
    if cap is None:
        cap = n
    return tuple((k,) + tail for k in range(min(n, cap), 0, -1)
                 for tail in partitions(n - k, k))


@lru_cache(None)
def gaussian(p, n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return gaussian(p, n - 1, k) + p ** (n - k) * gaussian(p, n - 1, k - 1)


def columns(lam):
    return tuple(sum(x >= j for x in lam) for j in range(1, max(lam, default=0) + 1))


def hall_hist(p, lam):
    r = columns(lam)
    def choices(j, previous):
        if j == len(r):
            yield ()
        else:
            for x in range(min(previous, r[j]) + 1):
                for tail in choices(j + 1, x):
                    yield (x,) + tail
    hist = Counter()
    for s in choices(0, r[0] if r else 0):
        count = 1
        for j, rank in enumerate(r):
            nxt = s[j + 1] if j + 1 < len(r) else 0
            count *= p ** (nxt * (rank - s[j])) * gaussian(p, rank - nxt, s[j] - nxt)
        hist[p ** sum(s)] += count
    return hist


def brute_additive(moduli):
    elements = list(product(*(range(q) for q in moduli)))
    zero = (0,) * len(moduli)
    def add(a, b):
        return tuple((x + y) % q for x, y, q in zip(a, b, moduli))
    identity = frozenset([zero])
    seen = {identity}
    queue = [identity]
    for group in queue:
        for x in elements:
            if x in group:
                continue
            result = set(group)
            y = x
            while y not in group:
                result.update(add(y, g) for g in group)
                y = add(y, x)
            result = frozenset(result)
            if result not in seen:
                seen.add(result)
                queue.append(result)
    return Counter(map(len, seen))


def brute_abelian_permutations(n):
    identity = tuple(range(n))
    elements = list(permutations(range(n)))
    def mul(p, q):
        return tuple(p[q[i]] for i in range(n))
    zero = frozenset([identity])
    seen = {zero}
    queue = [(zero, ())]
    for group, generators in queue:
        for x in elements:
            if x in group or any(mul(x, g) != mul(g, x) for g in generators):
                continue
            result = set(group)
            y = x
            while y not in group:
                result.update(mul(y, g) for g in group)
                y = mul(y, x)
            result = frozenset(result)
            if result not in seen:
                seen.add(result)
                queue.append((result, generators + (x,)))
    elementary = sum(all(mul(g, g) == identity for g in h) for h in seen)
    return len(seen), elementary, Counter(map(len, seen))


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        if a:
            out.append((p, a))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def local_types(max_order):
    result = []
    for order in range(2, max_order + 1):
        factors = factor(order)
        for types in product(*(partitions(e) for p, e in factors)):
            ranks = {(p, j): r for (p, e), lam in zip(factors, types)
                     for j, r in enumerate(columns(lam), 1)}
            optimal = order == 2 or (order == 4 and ranks.get((2, 1)) == 2)
            result.append((order, ranks, optimal))
    return result


def energy(ranks):
    return sum(log2(p) * r * r for (p, j), r in ranks.items())


def run():
    checks = []
    hall_cases = 0
    for p, top in [(2, 5), (3, 3), (5, 2)]:
        for exponent in range(1, top + 1):
            for lam in partitions(exponent):
                assert hall_hist(p, lam) == brute_additive([p ** a for a in lam])
                hall_cases += 1
    checks.append(f"Birkhoff formula checked by actual subgroup enumeration for {hall_cases} abelian p-group types.")
    small = []
    published = [1, 2, 5, 21, 87, 612]
    for n, known in enumerate(published, 1):
        total, elementary, hist = brute_abelian_permutations(n)
        assert total == known
        assert elementary == sum(elementary_counts(n))
        small.append({"n": n, "abelian": total, "elementary_2": elementary,
                      "by_order": dict(sorted(hist.items()))})
        checks.append(f"S_{n}: {total} actual abelian subgroups, of which {elementary} have exponent dividing two.")
    types = local_types(128)
    bad = [(q, r) for q, r, optimal in types if not optimal]
    for q, r in bad:
        assert r.get((2, 1), 0) <= 3 * q / 8
        assert sqrt(energy(r)) <= 15 * q / 32
    checks.append(f"Both local rank inequalities checked on {len(bad)} nonoptimal regular abelian types of orders at most 128.")
    rng = random.Random(1163)
    samples = 0
    for _ in range(3000):
        blocks = [rng.choice(bad) for _ in range(rng.randint(1, 15))]
        f = rng.randint(0, 30)
        good_pairs = rng.randint(400, 1200)
        n = f + sum(q for q, r in blocks) + 2 * good_pairs
        delta, m = n % 2, n // 2
        ranks = Counter({(2, 1): good_pairs})
        for q, r in blocks:
            ranks.update(r)
        D = m - ranks[(2, 1)]
        L = f - delta + sum(q for q, r in blocks)
        assert 1 <= D <= m and 2 * D <= L <= 8 * D
        assert energy(ranks) <= m * m - m * D / 32 + 1e-6
        samples += 1
    # Specifically test the odd-n case with no fixed point and a C_3 orbit.
    for m in [416, 500, 1000, 10000]:
        ranks = {(2, 1): m - 1, (3, 1): 1}
        assert energy(ranks) <= m * m - m / 32
    checks.append(f"Global defect inequalities checked on {samples} seeded mixed-order profiles and the odd-degree C_3 edge case.")
    out = Path(__file__).with_name("abelian_verification.json")
    out.write_text(json.dumps({"checks": checks, "small_degree_counts": small}, indent=2) + "\n")
    for line in checks:
        print(line)
    print(f"Saved {out}")


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""Exact local and finite checks for progress_v3.md; standard library only."""
from functools import lru_cache
from itertools import permutations
from math import factorial, comb, log, exp, sqrt, pi, lgamma
from pathlib import Path
import json

from verify import gaussian, convolve, all_binary_subspaces, family_counts


def multiply(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    ans = [0] * len(p)
    for i, v in enumerate(p):
        ans[v] = i
    return tuple(ans)


def local_group_check():
    def element(b, v):
        return tuple(2 * (i ^ v) + (e ^ ((b >> (i ^ v)) & 1))
                     for i in range(4) for e in range(2))
    group = {element(b, v) for b in range(16) if b.bit_count() % 2 == 0
             for v in range(4)}
    identity = tuple(range(8))
    z = tuple(i ^ 1 for i in range(8))
    assert len(group) == 32
    assert {g[0] for g in group} == set(range(8))
    assert all(multiply(g, h) in group for g in group for h in group)
    center = {g for g in group if all(multiply(g, h) == multiply(h, g) for h in group)}
    commutators = {multiply(multiply(g, h), multiply(inverse(g), inverse(h)))
                   for g in group for h in group}
    assert center == commutators == {identity, z}
    assert {multiply(g, g) for g in group} == center
    generators = [element(3, 0), element(5, 0), element(0, 1), element(0, 2)]
    closure = {identity}
    pending = [identity]
    for g in pending:
        for h in generators:
            q = multiply(g, h)
            if q not in closure:
                closure.add(q)
                pending.append(q)
    assert closure == group
    normalizer = []
    conjugate_centers = set()
    for p in permutations(range(8)):
        ip = inverse(p)
        zp = multiply(multiply(p, z), ip)
        conjugate_centers.add(zp)
        if all(multiply(multiply(p, g), ip) in group for g in generators):
            normalizer.append(p)
            assert zp == z
    assert len(normalizer) == 384
    assert len(conjugate_centers) == 105
    return {"group_order": 32, "center_order": 2, "derived_order": 2,
            "binary_quotient_rank": 4, "normalizer_order": 384,
            "conjugate_count": factorial(8) // 384}


@lru_cache(None)
def subdirect_counts_8(a, b, c):
    polynomial = [1]
    for count, factor in [(a, [1, -1]), (b, [1, -3, 2]),
                          (c, [1, -15, 70, -120, 64])]:
        for _ in range(count):
            polynomial = convolve(polynomial, factor)
    m = a + 2 * b + 4 * c
    values = tuple(sum(q * gaussian(m - t, k) for t, q in enumerate(polynomial))
                   for k in range(m + 1))
    assert all(v >= 0 for v in values)
    return values


def check_subdirect_8():
    checked = []
    for m in [4, 5, 6]:
        spaces = all_binary_subspaces(m)
        for b in range((m - 4) // 2 + 1):
            a = m - 4 - 2 * b
            hist = [0] * (m + 1)
            for space in spaces:
                shift = 0
                good = True
                for dim in [1] * a + [2] * b + [4]:
                    mask = (1 << dim) - 1
                    if len({(v >> shift) & mask for v in space}) != 1 << dim:
                        good = False
                        break
                    shift += dim
                if good:
                    hist[len(space).bit_length() - 1] += 1
            assert tuple(hist) == subdirect_counts_8(a, b, 1)
            checked.append({"a": a, "b": b, "c": 1, "rank_counts": hist})
    return checked


def exact_family_8(n):
    delta, m = n % 2, n // 2
    hist = [0] * (n + 1)
    ambient = 0
    for c in range(m // 4 + 1):
        for b in range((m - 4 * c) // 2 + 1):
            a = m - 4 * c - 2 * b
            denom = (factorial(delta) * 2 ** a * factorial(a)
                     * 24 ** b * factorial(b) * factorial(8) ** c * factorial(c))
            assert factorial(n) % denom == 0
            weight = factorial(n) // denom * 105 ** c
            ambient += weight * 4 ** b
            for k, count in enumerate(subdirect_counts_8(a, b, c)):
                for d in range(b + 1):
                    hist[k + d + c] += weight * count * comb(b, d) * 3 ** d
    return hist, ambient


def saddle_rho(N):
    m = N / 2
    low, high = 0.0, (48 * N) ** .25
    for _ in range(70):
        mid = (low + high) / 2
        if mid / 2 + mid ** 2 / 3 + mid ** 4 / 96 < m:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def coefficient_moments(N):
    """Exact finite coefficient sum in logs; moments under profile weights.

    Counts sum of weights to floating point accuracy. Conditional dihedral
    variance is included analytically, without sampling or asymptotics.
    """
    assert N > 0 and N % 2 == 0
    m = N // 2
    terms = []
    lf = [lgamma(j + 1) for j in range(m + 1)]
    for c in range(m // 4 + 1):
        for b in range((m - 4 * c) // 2 + 1):
            a = m - 4 * c - 2 * b
            weight = -a * log(2) - lf[a] - b * log(6) - lf[b] - c * log(384) - lf[c]
            terms.append((weight, a, b))
    top = max(x[0] for x in terms)
    norm = sum(exp(w - top) for w, a, b in terms)
    mean_a = sum(exp(w - top) * a for w, a, b in terms) / norm
    correction = sum(exp(w - top) * (b - a) / 4 for w, a, b in terms) / norm
    variance = sum(exp(w - top) * (((b - a) / 4 - correction) ** 2 + 3 * b / 16)
                   for w, a, b in terms) / norm
    return top + log(norm), 3 * N / 8 + correction, variance, mean_a


def run():
    results = {"local_group": local_group_check(),
               "subdirect_checks": check_subdirect_8()}
    hist8, _ = exact_family_8(8)
    expected = family_counts(8)[0]
    expected[5] += 105
    assert hist8 == expected
    exact_rows = []
    for n in [8, 16, 24, 32, 48, 64]:
        hist, ambient = exact_family_8(n)
        total = sum(hist)
        subspaces = sum(gaussian(n // 2, k) for k in range(n // 2 + 1))
        mean = sum(k * v for k, v in enumerate(hist)) / total
        variance = sum((k - mean) ** 2 * v for k, v in enumerate(hist)) / total
        exact_rows.append({"n": n, "total": total, "surjectivity_fraction": total / (ambient * subspaces),
                           "mean_log2_order": mean, "variance_log2_order": variance})
    results["exact_family"] = exact_rows
    asymptotic_rows = []
    for N in [64, 128, 256, 512, 1024, 2048, 4096]:
        rho = saddle_rho(N)
        V = rho / 2 + 2 * rho ** 2 / 3 + rho ** 4 / 24
        approx = rho / 2 + rho ** 2 / 6 + rho ** 4 / 384 - N / 2 * log(rho) - log(2 * pi * V) / 2
        exact, mean, variance, mean_a = coefficient_moments(N)
        center, scale = 3 * N / 8 + rho ** 2 / 24 - rho / 8, rho / sqrt(24)
        asymptotic_rows.append({"N": N, "coefficient_over_saddle": exp(exact - approx),
                                "mean_minus_center_over_scale": (mean - center) / scale,
                                "variance_over_scale_squared": variance / scale ** 2,
                                "odd_family_ratio": mean_a / 3,
                                "odd_family_ratio_over_prediction": 2 * mean_a / rho})
    results["asymptotic_checks"] = asymptotic_rows
    destination = Path(__file__).with_name("extraspecial_verification.json")
    destination.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results["local_group"]))
    print(f"Checked rank-4 surjectivity on {len(results['subdirect_checks'])} profiles, through dimension 6.")
    print("Q_8 order histogram equals F_8 plus 105 groups of order 32.")
    print(json.dumps(asymptotic_rows[-1]))
    print(f"Wrote {destination}")


if __name__ == "__main__":
    run()

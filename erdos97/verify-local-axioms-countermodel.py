#!/usr/bin/env python3
"""Exact abstract metric verification; no Euclidean realization is claimed."""

from itertools import combinations, product


def main():
    vectors = [
        v for v in product(range(3), repeat=3)
        if any(v) and next(x for x in v if x) == 1
    ]
    assert len(vectors) == 13
    n = 26
    out = [set() for _ in range(n)]
    for i, point in enumerate(vectors):
        for j, line in enumerate(vectors):
            if sum(x*y for x, y in zip(point, line)) % 3 == 0:
                out[i].add(13+j)
                out[13+j].add(i)
    assert all(len(row) == 4 for row in out)
    assert sum(map(len, out)) == 104

    distance = [[0]*n for _ in range(n)]
    for rank, (i, j) in enumerate(combinations(range(n), 2), 1):
        if j in out[i]:
            value = 200000
        elif (i < 13) == (j < 13):
            value = 300000 + rank
        else:
            value = 400000 + rank
        distance[i][j] = distance[j][i] = value

    for a, b, c in combinations(range(n), 3):
        x, y, z = distance[a][b], distance[a][c], distance[b][c]
        assert x+y > z and x+z > y and y+z > x
    for i in range(n):
        assert {j for j in range(n) if distance[i][j] == 200000} == out[i]
        other = [distance[i][j] for j in range(n) if j != i and j not in out[i]]
        assert len(other) == len(set(other))
    for i, j in combinations(range(n), 2):
        common = out[i] & out[j]
        assert len(common) <= 1
        equidistant = [
            k for k in range(n)
            if k not in (i, j) and distance[k][i] == distance[k][j]
        ]
        assert set(equidistant) == common
        assert len(equidistant) <= 1

    # P_0, P_1, L_1, L_4 occur in this cyclic order.
    a, b, c, d = 0, 1, 14, 17
    assert a < b < c < d
    diagonal_sum = distance[a][c] + distance[b][d]
    side_sum = distance[a][b] + distance[c][d]
    assert diagonal_sum < side_sum

    print("Verified an exact 26-vertex strict metric.")
    print("Every vertex has exactly four neighbors at favorite distance 200000.")
    print("Every pair has at most one equidistant third vertex; no four-cycles occur.")
    print("Double-intersection and equal-radius rhombus rules are vacuous.")
    print(f"Displayed Kalmanson violation: diagonal sum {diagonal_sum} < side sum {side_sum}.")
    print("This is an abstract metric countermodel to local axioms, not a convex Euclidean polygon.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify finite graph properties, not distances or a geometric realization."""

import json
from itertools import combinations
from pathlib import Path


def main():
    path = Path(__file__).with_name("nine-vertex-combinatorial-witness.json")
    data = json.loads(path.read_text())
    n = data["n"]
    assert data["cyclic_order"] == list(range(n))
    rows = data["out_neighbors"]
    assert len(rows) == n
    out = [set(row) for row in rows]
    classes = data["radius_classes"]
    assert len(classes) == n
    for i, row in enumerate(rows):
        assert len(row) == len(out[i]) == 4
        assert i not in out[i]
        assert all(0 <= j < n for j in row)

    def alternate(a, b, c, d):
        assert len({a, b, c, d}) == 4
        if a > b:
            a, b = b, a
        return (a < c < b) != (a < d < b)

    total = 0
    histogram = {0: 0, 1: 0, 2: 0}
    for a, b in combinations(range(n), 2):
        common_targets = sorted(out[a] & out[b])
        assert len(common_targets) <= 2
        if len(common_targets) == 2:
            assert alternate(a, b, *common_targets)

        predecessors = [i for i in range(n) if {a, b} <= out[i]]
        assert len(predecessors) <= 2
        if len(predecessors) == 2:
            assert alternate(a, b, *predecessors)
        if b == a + 1 or (a == 0 and b == n - 1):
            assert len(predecessors) <= 1
        total += len(predecessors)
        histogram[len(predecessors)] += 1

        ab = b in out[a]
        ba = a in out[b]
        if ab and ba:
            assert classes[a] == classes[b]
        elif ab or ba:
            assert classes[a] != classes[b]

    assert total == 6 * n
    assert total <= n * (n - 2)
    print(f"Verified {n} vertices, four outgoing neighbors per vertex.")
    print("Verified common-predecessor/target bounds and cyclic alternation.")
    print("Verified necessary radius-class consistency of reciprocal/one-way arcs.")
    print(f"Common-predecessor pair histogram: {histogram}")
    print("No geometric realization or counterexample to Erdős #97 is asserted.")


if __name__ == "__main__":
    main()

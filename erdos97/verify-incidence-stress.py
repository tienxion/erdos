"""Exact first/second stress-load check on a rational Pappus configuration.

Uses only Python's standard library. This checks the displayed example,
not existence or nonexistence of a geometric counterexample to problem 97.
"""

from fractions import Fraction as F


def pair(a, b):
    return F(a), F(b)


points = [
    pair(0, 0), pair(1, 0), pair(3, 0),
    pair(0, 2), pair(2, 2), pair(5, 2),
    (F(2, 3), F(2, 3)), (F(15, 8), F(3, 4)),
    (F(13, 5), F(4, 5)),
]
# Lines are (slope Y, intercept b).
lines = [
    pair(0, 0), pair(0, 2), pair(1, 0), pair(-2, 2),
    (F(2, 5), F(0)), (F(-2, 3), F(2)),
    (F(1, 2), F(-1, 2)), pair(-2, 6), (F(2, 29), F(18, 29)),
]
edges = [(i, j) for i, (y, b) in enumerate(lines)
         for j, (v, w) in enumerate(points) if w == b + y * v]
stress = list(map(F, [
    "12/29", "-18/29", "6/29", "18/145", "-6/29", "12/145",
    "8/29", "4/29", "-12/29", "18/145", "9/145", "-27/145",
    "-20/29", "-12/29", "32/29", "-9/29", "-27/145", "72/145",
    "72/145", "48/145", "-24/29", "3/29", "2/29", "-5/29",
    "3/5", "-8/5", "1",
]))
assert len(edges) == len(stress) == 27
for i in range(9):
    assert sum(w for w, (ii, j) in zip(stress, edges) if ii == i) == 0
    assert sum(w * points[j][0] for w, (ii, j) in zip(stress, edges)
               if ii == i) == 0
for j in range(9):
    assert sum(w for w, (i, jj) in zip(stress, edges) if jj == j) == 0
    assert sum(w * lines[i][0] for w, (i, jj) in zip(stress, edges)
               if jj == j) == 0

quartic = sum(w * (points[j][0] - lines[i][0]) ** 4
              for w, (i, j) in zip(stress, edges))
sixth = sum(w * (points[j][0] - lines[i][0]) ** 6
            for w, (i, j) in zip(stress, edges))
mixed = sum(w * (points[j][0] ** 4 * lines[i][0] ** 2
                 + points[j][0] ** 2 * lines[i][0] ** 4)
            for w, (i, j) in zip(stress, edges))
assert quartic == 0
assert sixth == F(66654, 841)
assert mixed * 15 == sixth
print(f"Exact stress check passed: quartic = {quartic}, sixth = {sixth}.")

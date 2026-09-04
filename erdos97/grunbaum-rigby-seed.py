#!/usr/bin/env python3
"""Reproduce the exact trigonometric GR(21_4) seed as numerical JSON.

Exact formulas are documented in grunbaum-rigby-seed.md.  This script is a
floating-point consistency check, not an interval or symbolic certificate.
"""
import cmath
import json
import math
from pathlib import Path


def make_seed():
    pi = math.pi
    original = {}
    for family, k in (("A", 1), ("D", 2), ("B", 3)):
        factor = math.cos(k*pi/7)/math.cos(pi/7)
        for j in range(7):
            z = factor*cmath.exp(1j*(2*j+k-1)*pi/7)
            original[f"{family}{j}"] = (z.real, z.imag)

    point_order = [f"{family}{j}" for family in ("A", "D", "B")
                   for j in range(7)]
    points = []
    for label in point_order:
        x, y = original[label]
        v, w = (x+2*y)/(1+x/10+y/13), (3*x+5*y)/(1+x/10+y/13)
        points.append(dict(label=label, original=[x, y], V=v, W=w,
                           U=w-v*v/2))

    lines = []
    for family, k, h in (
            ("L", 2, math.cos(2*pi/7)),
            ("M", 3, math.cos(3*pi/7)),
            ("N", 4, math.cos(2*pi/7)*math.cos(3*pi/7)/math.cos(pi/7))):
        for j in range(7):
            theta = (2*j+k)*pi/7
            a, b = math.cos(theta), math.sin(theta)
            beta = 2*a-b+8*h/65
            slope = (5*a-3*b+7*h/26)/beta
            intercept = h/beta
            if family == "L":
                adjacent = [f"A{j}", f"A{(j+2)%7}",
                            f"D{j}", f"D{(j+1)%7}"]
            elif family == "M":
                adjacent = [f"A{j}", f"A{(j+3)%7}",
                            f"B{j}", f"B{(j+1)%7}"]
            else:
                adjacent = [f"B{j}", f"B{(j+2)%7}",
                            f"D{j}", f"D{(j+3)%7}"]
            lines.append(dict(label=f"{family}{j}", normal=[a, b],
                              offset=h, Y=slope, C=intercept,
                              X=intercept+slope*slope/2,
                              points=adjacent))
    point_index = {p["label"]: i for i, p in enumerate(points)}
    incidence = [[i, point_index[label]] for i, line in enumerate(lines)
                 for label in line["points"]]
    return dict(
        scope="Real point-line incidence seed; not a convex unit-distance realization.",
        sources=["https://arxiv.org/html/2512.18872v1",
                 "https://arxiv.org/abs/2408.09203"],
        exact_chart="V=(x+2y)/(1+x/10+y/13); W=(3x+5y)/(1+x/10+y/13)",
        line_order=[line["label"] for line in lines],
        point_order=point_order, points=points, lines=lines,
        incidence=incidence)


def verify(seed):
    incidence = set(map(tuple, seed["incidence"]))
    assert len(incidence) == 84
    assert all(sum(i == a for a, b in incidence) == 4 for i in range(21))
    assert all(sum(j == b for a, b in incidence) == 4 for j in range(21))
    incident_error, nonincident_gap = 0., float("inf")
    for i, line in enumerate(seed["lines"]):
        for j, point in enumerate(seed["points"]):
            residual = abs(point["W"]-line["Y"]*point["V"]-line["C"])
            if (i, j) in incidence:
                incident_error = max(incident_error, residual)
            else:
                nonincident_gap = min(nonincident_gap, residual)
    def min_sep(xs):
        return min(abs(x-y) for i, x in enumerate(xs) for y in xs[i+1:])
    diagnostics = dict(
        maximum_incident_equation_error=incident_error,
        minimum_nonincident_equation_gap=nonincident_gap,
        minimum_point_abscissa_separation=min_sep([p["V"] for p in seed["points"]]),
        minimum_line_slope_separation=min_sep([l["Y"] for l in seed["lines"]]))
    assert incident_error < 1e-11
    assert min(nonincident_gap,
               diagnostics["minimum_point_abscissa_separation"],
               diagnostics["minimum_line_slope_separation"]) > 1e-5
    return diagnostics


if __name__ == "__main__":
    seed = make_seed()
    seed["numerical_checks"] = verify(seed)
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(seed, indent=2)+"\n")
    print(json.dumps(seed["numerical_checks"], indent=2))
    print(out)

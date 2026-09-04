#!/usr/bin/env python3
"""Finite affine-chart criterion and bounded projective search for the unit limit.

The divided-difference criterion is exact mathematically. The chart search and
all coordinates produced by this implementation are floating-point heuristics.
Failure of this search proves no projective impossibility.
"""
import argparse
import itertools
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution

HERE = Path(__file__).resolve().parent


def second_divided(x, f):
    order = np.argsort(x)
    x, f = np.asarray(x)[order], np.asarray(f)[order]
    gaps = np.diff(x)
    if gaps.min() <= 1e-9:
        raise ValueError("Nearly coincident abscissae or slopes")
    divided = np.diff(np.diff(f) / gaps) / (x[2:] - x[:-2])
    return divided, order


def criterion(points, lines):
    curvature, point_order = second_divided(points[:, 0], points[:, 1])
    dual_curvature, line_order = second_divided(lines[:, 0], lines[:, 1])
    C, D = float(curvature.max()), float(dual_curvature.min())
    lower = max(0., -2 * D)
    upper = .5 / C if C > 0 else np.inf
    feasible = lower < upper
    scale = np.sqrt(lower * upper) if lower > 0 and np.isfinite(upper) else (
        2 * lower + 1 if not np.isfinite(upper) else upper / 2)
    return {"C": C, "D": D, "minus_four_CD": -4 * C * D,
            "positive_scale_lower_bound": lower,
            "positive_scale_upper_bound": upper if np.isfinite(upper) else None,
            "affine_scale_feasible": bool(feasible),
            "suggested_scale_if_feasible": float(scale) if feasible else None,
            "point_order": point_order.tolist(), "line_order": line_order.tolist(),
            "point_second_divided_differences": curvature.tolist(),
            "line_second_divided_differences": dual_curvature.tolist()}


def transform(original_points, original_lines, parameters, orientation):
    angle, p, q = parameters
    c, s = np.cos(angle), np.sin(angle)
    matrix = np.array([[c, s, 0], [-orientation * s, orientation * c, 0],
                       [p, q, 1.]])
    transformed = original_points @ matrix.T
    if np.min(np.abs(transformed[:, 2])) < 1e-8:
        raise ValueError("Point too near chart infinity")
    points = transformed[:, :2] / transformed[:, 2, None]
    dual = original_lines @ np.linalg.inv(matrix)
    if np.min(np.abs(dual[:, 1])) < 1e-8:
        raise ValueError("Line too near vertical")
    lines = -dual[:, [0, 2]] / dual[:, 1, None]
    return points, lines, matrix


def incidence_triangles(seed):
    pair_to_line = {}
    adjacency = [[] for _ in seed["lines"]]
    for i, j in seed["incidence"]:
        adjacency[i].append(j)
    for i, row in enumerate(adjacency):
        for pair in itertools.combinations(sorted(row), 2):
            if pair in pair_to_line:
                raise ValueError("Repeated point pair on distinct selected lines")
            pair_to_line[pair] = i
    triangles = []
    for a, b, c in itertools.combinations(range(len(seed["points"])), 3):
        pairs = [(a, b), (a, c), (b, c)]
        if all(pair in pair_to_line for pair in pairs):
            lines = [pair_to_line[pair] for pair in pairs]
            if len(set(lines)) == 3:
                triangles.append((a, b, c))
    return triangles


def triangle_diagnostic(points, triangles):
    cups, caps = [], []
    for triple in triangles:
        subset = points[list(triple)]
        curvature, _ = second_divided(subset[:, 0], subset[:, 1])
        (cups if curvature[0] > 0 else caps).append(list(triple))
    return {"noncollinear_incidence_triangles": len(triangles),
            "cup_count": len(cups), "cap_count": len(caps),
            "first_cup_point_indices": cups[0] if cups else None}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default=str(HERE / "grunbaum-rigby-seed.json"))
    parser.add_argument("--seconds", type=float, default=45)
    parser.add_argument("--output", default=str(HERE / "parabolic-chart-results.json"))
    args = parser.parse_args()
    seed = json.loads(Path(args.seed).read_text())
    original_points = np.array([p["original"] + [1.] for p in seed["points"]])
    original_lines = np.array([line["normal"] + [-line["offset"]] for line in seed["lines"]])
    triangles = incidence_triangles(seed)
    initial_points = np.array([[p["V"], p["W"]] for p in seed["points"]])
    initial_lines = np.array([[line["Y"], line["C"]] for line in seed["lines"]])
    initial = criterion(initial_points, initial_lines)
    initial.update(triangle_diagnostic(initial_points, triangles))
    best = {"score": np.inf}
    calls = 0
    start = time.monotonic()
    per_case = args.seconds / 4
    for orientation in (1, -1):
        for extent in (2., 20.):
            deadline = time.monotonic() + per_case

            def objective(parameters):
                nonlocal calls
                if time.monotonic() > deadline:
                    raise TimeoutError
                calls += 1
                try:
                    points, lines, matrix = transform(original_points, original_lines,
                                                      parameters, orientation)
                    result = criterion(points, lines)
                except (ValueError, np.linalg.LinAlgError, FloatingPointError):
                    return 1e6
                # For an n_4 configuration both signs must be strict in exact
                # arithmetic. Unexpected signs are retained for later auditing.
                product = result["minus_four_CD"]
                score = float(np.log(max(product, 1e-100)))
                if score < best["score"]:
                    best.update(score=score, parameters=parameters.tolist(),
                                orientation=orientation, extent=extent,
                                criterion=result, matrix=matrix.tolist(),
                                points=points.tolist(), lines=lines.tolist())
                return score

            try:
                differential_evolution(objective, [(0, 2 * np.pi), (-extent, extent), (-extent, extent)],
                                       seed=97021 + orientation + int(extent), popsize=20,
                                       maxiter=20000, tol=1e-9, polish=False,
                                       updating="immediate")
                status = "Optimizer stopped"
            except TimeoutError:
                status = "Wall-clock bound reached"
            print(json.dumps({"orientation": orientation, "extent": extent,
                              "status": status, "calls": calls,
                              "best_minus_four_CD": best["criterion"]["minus_four_CD"]}), flush=True)
    best_points = np.asarray(best["points"])
    best_lines = np.asarray(best["lines"])
    best.update(triangle_diagnostic(best_points, triangles))
    best["maximum_incidence_error"] = max(abs(best_points[j, 1] - best_lines[i, 0] * best_points[j, 0]
                                                - best_lines[i, 1]) for i, j in seed["incidence"])
    output = {"status": "Bounded numerical search only; no universal projective impossibility established.",
              "criterion": "C=max second divided difference of W(V); D=min second divided difference of b(Y); feasible iff max(0,-2D)<1/(2C), with infinite upper bound when C<=0.",
              "initial_chart": initial, "best_chart": best, "objective_calls": calls,
              "elapsed_seconds": time.monotonic() - start}
    Path(args.output).write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"initial_minus_four_CD": initial["minus_four_CD"],
                      "best_minus_four_CD": best["criterion"]["minus_four_CD"],
                      "best_cups": best["cup_count"],
                      "triangles": best["noncollinear_incidence_triangles"],
                      "best_incidence_error": best["maximum_incidence_error"]}), flush=True)


if __name__ == "__main__":
    main()

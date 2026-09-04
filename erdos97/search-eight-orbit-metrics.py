#!/usr/bin/env python3
"""Heuristic search for convex realizations of abstract eight-orbit graphs.

Floating-point output is never a proof or a counterexample. The independent
diagnostics evaluate original distances and a convex hull, not just the
optimizer's phase equations. This script allows every radius order.
"""
import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares
from scipy.spatial import ConvexHull, QhullError


N = 8
OMEGA = np.exp(2j * np.pi / 3)


def unpack(x):
    logs = np.r_[0.0, x[:N - 1]]
    phases = np.r_[0.0, x[N - 1:]]
    z = np.exp(logs + 1j * phases / 3)
    return logs, phases, z


def residual(x, sources, targets):
    logs, phases, z = unpack(x)
    delta = phases[targets] - phases[sources]
    d = np.abs(np.arctan2(np.sin(delta), np.cos(delta)))
    # Two possible radius ratios for this directed incidence and the
    # circular phase separation. Select the closer branch, without
    # fixing a radius ordering or a rotation label.
    c_up = np.cos((2 * np.pi - d) / 3)
    c_down = np.cos((2 * np.pi + d) / 3)
    up = np.log(c_up + np.sqrt(c_up * c_up + 2))
    down = np.log(c_down + np.sqrt(c_down * c_down + 2))
    difference = logs[targets] - logs[sources]
    e_up, e_down = difference - up, difference - down
    metric = np.where(np.abs(e_up) <= np.abs(e_down), e_up, e_down)

    # Choose representatives with phases in [0,2pi), then order them
    # cyclically. The previous/next representatives at the seam rotate.
    p = np.mod(phases, 2 * np.pi)
    order = np.argsort(p)
    ordered = np.exp(logs[order] + 1j * p[order] / 3)
    previous = np.r_[ordered[-1] / OMEGA, ordered[:-1]]
    following = np.r_[ordered[1:], ordered[0] * OMEGA]
    a, b = ordered - previous, following - ordered
    sine = np.imag(np.conj(a) * b) / np.maximum(np.abs(a) * np.abs(b), 1e-14)
    convex = 0.5 * np.maximum(0.003 - sine, 0.0)

    i, j = np.triu_indices(N, 1)
    phase_delta = phases[j] - phases[i]
    minor = np.abs(np.arctan2(np.sin(phase_delta), np.cos(phase_delta))) / 3
    distances = np.sqrt(np.maximum(0.0, np.exp(2 * logs[i]) + np.exp(2 * logs[j])
                                   - 2 * np.exp(logs[i] + logs[j]) * np.cos(minor)))
    separation = 0.5 * np.maximum(0.03 - distances, 0.0)
    spread = np.array([max(0.0, float(np.ptp(logs)) - math.log(1.999))])
    return np.r_[metric, convex, separation, spread]


def diagnose(x, sources, targets):
    logs, phases, z = unpack(x)
    points = np.array([q * OMEGA ** k for q in z for k in range(3)])
    errors = [min(abs(abs(z[i] - z[j] * OMEGA ** k) ** 2 / abs(z[i]) ** 2 - 3)
                  for k in range(3)) for i, j in zip(sources, targets)]
    try:
        hull_count = len(ConvexHull(np.c_[points.real, points.imag]).vertices)
    except QhullError:
        hull_count = 0
    separation = min(abs(points[i] - points[j]) for i in range(24) for j in range(i))
    return {
        "original_squared_distance_max_error": float(max(errors)),
        "hull_vertices": hull_count,
        "minimum_point_separation": float(separation),
        "radius_ratio": float(np.exp(np.ptp(logs))),
        "log_radii": logs.tolist(),
        "cube_phases": phases.tolist(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--starts", type=int, default=2)
    parser.add_argument("--max-evaluations", type=int, default=250)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    classes = json.loads((here / "eight-orbit-isomorphism-classes.json").read_text())["classes"]
    end = min(args.start + args.count, len(classes))
    records = []
    start_time = time.time()
    for index in range(args.start, end):
        masks = classes[index]["out_masks"]
        pairs = [(i, j) for i in range(N) for j in range(N) if masks[i] & (1 << j)]
        sources = np.array([i for i, _ in pairs])
        targets = np.array([j for _, j in pairs])
        best = None
        for attempt in range(args.starts):
            rng = np.random.default_rng(970000 + index * 1000 + attempt)
            phases = 2 * np.pi * rng.permutation(np.arange(1, N)) / N
            logs = rng.normal(0, 0.015, N - 1)
            initial = np.r_[logs, phases]
            result = least_squares(residual, initial, args=(sources, targets),
                                   max_nfev=args.max_evaluations, ftol=1e-10,
                                   xtol=1e-10, gtol=1e-10)
            record = diagnose(result.x, sources, targets)
            record.update({"class_index": index, "attempt": attempt,
                           "optimizer_cost": float(result.cost), "evaluations": result.nfev,
                           "out_masks": masks})
            # Keep the optimizer's best compromise, while storing all
            # independent diagnostics that expose nonconvexity/collapse.
            if best is None or record["optimizer_cost"] < best["optimizer_cost"]:
                best = record
        records.append(best)
        if (index - args.start + 1) % 10 == 0:
            good = [r for r in records if r["hull_vertices"] == 24 and r["minimum_point_separation"] > 0.02]
            error = min((r["original_squared_distance_max_error"] for r in good), default=None)
            print(json.dumps({"classes_completed": len(records), "convex_nondegenerate": len(good),
                              "best_convex_original_error": error,
                              "seconds": round(time.time() - start_time, 2)}), flush=True)
    output = {"status": "Heuristic numerical search only; no exact counterexample is asserted.",
              "parameters": vars(args), "seconds": time.time() - start_time, "records": records}
    path = here / f"metric-search-{args.start:03d}-{end:03d}.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(f"Saved {path}", flush=True)


if __name__ == "__main__":
    main()

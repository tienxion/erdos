#!/usr/bin/env python3
"""Bounded HEURISTIC C3 search for Erdős #97 with arbitrary favorite radii.

No floating-point output from this program is a proof.  Four closest-to-equal
distances are selected afresh at every evaluation, so the objective is only
piecewise smooth.  Original distances and the full convex hull are checked
independently after each run.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares
from scipy.special import logsumexp, softmax
from scipy.spatial import ConvexHull, QhullError

TAU = 2 * np.pi / 3
OMEGA = np.exp(1j * TAU)
GAP_FLOOR_FRACTION = 0.002
TURN_FLOOR = 0.0002
EDGE_FLOOR = 0.004


def decode(x, m):
    logs = np.r_[0.0, x[:m - 1]]
    radii = np.exp(logs)
    radii /= np.sqrt(np.mean(radii * radii))
    weights = softmax(np.r_[0.0, x[m - 1:]])
    gaps = TAU * (GAP_FLOOR_FRACTION / m
                  + (1 - GAP_FLOOR_FRACTION) * weights)
    angles = np.r_[0.0, np.cumsum(gaps[:-1])]
    return radii * np.exp(1j * angles)


def encode(z):
    m = len(z)
    z = z * np.exp(-1j * np.angle(z[0]))
    angles = np.unwrap(np.angle(z))
    gaps = np.diff(np.r_[angles, TAU]) / TAU
    weights = np.maximum((gaps - GAP_FLOOR_FRACTION / m)
                         / (1 - GAP_FLOOR_FRACTION), 1e-7)
    return np.r_[np.log(np.abs(z[1:]) / abs(z[0])),
                 np.log(weights[1:] / weights[0])]


def all_points(z):
    return np.concatenate([z * OMEGA ** k for k in range(3)])


def selected_distances(z):
    m = len(z)
    p = all_points(z)
    distances = np.abs(z[:, None] - p[None, :])
    distances[np.arange(m), np.arange(m)] = np.inf
    order = np.argsort(distances, axis=1)[:, :-1]
    ordered = np.take_along_axis(distances, order, axis=1)
    windows = np.lib.stride_tricks.sliding_window_view(ordered, 4, axis=1)
    means = windows.mean(axis=2)
    deviations = (windows - means[:, :, None]) / means[:, :, None]
    best = np.argmin(np.mean(deviations * deviations, axis=2), axis=1)
    selected_indices = np.take_along_axis(order, best[:, None] + np.arange(4), axis=1)
    selected = np.take_along_axis(distances, selected_indices, axis=1)
    return selected, selected_indices


def geometry(z):
    previous = np.r_[z[-1] / OMEGA, z[:-1]]
    following = np.r_[z[1:], z[0] * OMEGA]
    a, b = z - previous, following - z
    turns = np.imag(np.conj(a) * b) / np.maximum(np.abs(a) * np.abs(b), 1e-20)
    return turns, np.abs(b)


def residual(x, m, weight, deadline):
    if time.monotonic() > deadline:
        raise TimeoutError("Per-run wall-clock bound reached")
    z = decode(x, m)
    selected, _ = selected_distances(z)
    average = selected.mean(axis=1, keepdims=True)
    distance_error = (selected - average) / average
    turns, edges = geometry(z)
    # Normalized edge directions avoid accepting inward corners merely because
    # neighboring points coalesce.  A separate edge floor discourages collapse.
    convex_error = weight * np.maximum(TURN_FLOOR - turns, 0)
    collapse_error = weight * np.maximum(EDGE_FLOOR - edges, 0) / EDGE_FLOOR
    return np.r_[distance_error.ravel(), convex_error, collapse_error]


def smooth_barany(normal_angles, beta=20.0, epsilon=0.025):
    seed = np.array([1 + 0j, .906 + .114j, .645 + .359j, -.498 + .871j])
    p = all_points(seed)
    u = np.exp(1j * normal_angles)
    support = np.real(p[None, :] * np.conj(u[:, None]))
    tangent_projection = np.imag(p[None, :] * np.conj(u[:, None]))
    logits = beta * support
    weights = softmax(logits, axis=1)
    h = logsumexp(logits, axis=1) / beta + epsilon
    derivative = np.sum(weights * tangent_projection, axis=1)
    return u * (h + 1j * derivative)


def seed_points(m, family, phase=0):
    if family == "regular":
        t = np.arange(m) * TAU / m
        return np.exp(1j * t)
    if family == "near_regular":
        t = np.arange(m) * TAU / m
        r = 1 + .017 * np.cos(3 * t + .71) + .004 * np.sin(6 * t + .27)
        return r * np.exp(1j * t)
    beta = 12 if family == "barany_normal" else 25
    if family == "barany_normal":
        angles = phase + np.arange(m) * TAU / m
    else:
        dense_angles = np.linspace(phase, phase + TAU, 4001)
        dense = smooth_barany(dense_angles, beta)
        length = np.r_[0.0, np.cumsum(np.abs(np.diff(dense)))]
        targets = np.arange(m) * length[-1] / m
        angles = np.interp(targets, length, dense_angles)
    return smooth_barany(angles, beta)


def diagnose(x, m):
    z = decode(x, m)
    p = all_points(z)
    selected, indices = selected_distances(z)
    squared = selected * selected
    mean_squared = squared.mean(axis=1)
    errors = np.ptp(squared, axis=1) / mean_squared
    turns, edges = geometry(z)
    try:
        hull_count = len(ConvexHull(np.c_[p.real, p.imag]).vertices)
    except QhullError:
        hull_count = 0
    pairwise = np.abs(p[:, None] - p[None, :])
    pairwise[np.diag_indices_from(pairwise)] = np.inf
    return {
        "vertices": 3 * m,
        "hull_vertices": hull_count,
        "all_vertices_on_hull": hull_count == 3 * m,
        "minimum_point_separation": float(pairwise.min()),
        "minimum_turn_sine": float(turns.min()),
        "minimum_edge": float(edges.min()),
        "max_relative_squared_distance_spread": float(errors.max()),
        "rms_relative_squared_distance_spread": float(np.sqrt(np.mean(errors ** 2))),
        "per_representative_relative_squared_distance_spread": errors.tolist(),
        "favorite_radii": np.sqrt(mean_squared).tolist(),
        "selected_target_indices": indices.tolist(),
        "selected_original_squared_distances": squared.tolist(),
        "representative_coordinates": np.c_[z.real, z.imag].tolist(),
        "all_point_coordinates": np.c_[p.real, p.imag].tolist(),
        "parameters": x.tolist(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds-per-run", type=float, default=11)
    parser.add_argument("--max-nfev", type=int, default=120)
    parser.add_argument("--output", default="erdos97/favorite-radius-results.json")
    args = parser.parse_args()
    output = Path(args.output)
    records = []
    start_time = time.monotonic()
    for m in (9, 12, 15, 20):
        for family in ("regular", "near_regular", "barany_normal", "barany_arc"):
            x0 = encode(seed_points(m, family))
            initial = diagnose(x0, m)
            best = {"x": x0.copy(), "cost": np.inf, "calls": 0}
            deadline = time.monotonic() + args.seconds_per_run

            def fun(x):
                value = residual(x, m, 8.0, deadline)
                cost = float(np.dot(value, value))
                best["calls"] += 1
                if cost < best["cost"]:
                    best.update(x=x.copy(), cost=cost)
                return value

            run_start = time.monotonic()
            try:
                result = least_squares(fun, x0, max_nfev=args.max_nfev,
                                       bounds=(-5.5, 5.5), ftol=1e-11,
                                       xtol=1e-11, gtol=1e-11, diff_step=2e-6)
                status = result.message
                nfev = result.nfev
            except TimeoutError as exc:
                status, nfev = str(exc), None
            final = diagnose(best["x"], m)
            record = {"orbits": m, "family": family, "status": status,
                      "elapsed_seconds": time.monotonic() - run_start,
                      "nfev": nfev, "residual_calls": best["calls"],
                      "objective_squared_norm": best["cost"],
                      "initial": initial, "final": final}
            records.append(record)
            payload = {
                "status": "HEURISTIC ONLY: no exact proof or counterexample",
                "description": "C3 symmetry, arbitrary inferred favorite radius at each representative; best four consecutive sorted distances.",
                "barany_seed_status": "Exact decimal 12-point primary construction; smooth support is evaluated numerically. No numerical A5 is assumed.",
                "convexity_weight": 8.0, "turn_floor": TURN_FLOOR,
                "edge_floor": EDGE_FLOOR, "gap_floor_fraction": GAP_FLOOR_FRACTION,
                "elapsed_seconds": time.monotonic() - start_time,
                "runs": records,
            }
            output.write_text(json.dumps(payload, indent=2) + "\n")
            print(json.dumps({"m": m, "seed": family,
                              "seconds": round(record["elapsed_seconds"], 2),
                              "hull": final["hull_vertices"], "n": 3 * m,
                              "spread": final["max_relative_squared_distance_spread"],
                              "turn": final["minimum_turn_sine"],
                              "separation": final["minimum_point_separation"]}), flush=True)


if __name__ == "__main__":
    main()

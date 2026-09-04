#!/usr/bin/env python3
"""Finite deterministic multistart follow-up; every result is heuristic only."""
import importlib.util
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("favorite_search", HERE / "favorite-radius-search.py")
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


def alternate_indices(z, rng):
    p = search.all_points(z)
    m = len(z)
    distances = np.abs(z[:, None] - p[None, :])
    distances[np.arange(m), np.arange(m)] = np.inf
    order = np.argsort(distances, axis=1)[:, :-1]
    ordered = np.take_along_axis(distances, order, axis=1)
    windows = np.lib.stride_tricks.sliding_window_view(ordered, 4, axis=1)
    means = windows.mean(axis=2)
    score = np.mean(((windows - means[:, :, None]) / means[:, :, None]) ** 2, axis=2)
    ranked = np.argsort(score, axis=1)
    # A transient alternate cluster can escape a locally preferred farthest
    # cluster. The final stage always uses the actual minimum-variance window.
    ranks = rng.integers(0, 4, size=m)
    chosen = ranked[np.arange(m), ranks]
    return np.take_along_axis(order, chosen[:, None] + np.arange(4), axis=1)


def main():
    rng = np.random.default_rng(970004)
    beginning = time.monotonic()
    global_deadline = beginning + 150
    records = []
    output = HERE / "favorite-radius-restart-results.json"
    for m in (9, 12, 15, 20):
        for restart in range(12):
            if time.monotonic() >= global_deadline:
                break
            family = ("near_regular", "barany_normal", "barany_arc")[restart % 3]
            phase = float(rng.uniform(0, search.TAU))
            z = search.seed_points(m, family, phase)
            x0 = search.encode(z)
            # Vary angular sampling and smooth radial deformation, maintaining
            # polar order through the parametrization. Hull validation is
            # still required: these perturbations need not preserve convexity.
            t = np.arange(m) * search.TAU / m
            radial = .008 * np.cos(3 * t + phase) + .003 * np.sin(6 * t + phase)
            x0[:m - 1] += radial[1:] - radial[0]
            x0[m - 1:] += rng.normal(0, .16, m - 1)
            deadline = min(global_deadline, time.monotonic() + 4)
            fixed = alternate_indices(search.decode(x0, m), rng) if restart >= 6 else None
            best = {"x": x0.copy(), "cost": np.inf}
            calls = 0

            def fun(x):
                nonlocal calls
                value = search.residual(x, m, 15.0, deadline)
                if fixed is not None:
                    representative = search.decode(x, m)
                    points = search.all_points(representative)
                    selected = np.abs(representative[:, None] - points[fixed])
                    mean = selected.mean(axis=1, keepdims=True)
                    value[:4 * m] = ((selected - mean) / mean).ravel()
                score = float(value @ value)
                calls += 1
                if score < best["cost"]:
                    best.update(x=x.copy(), cost=score)
                return value

            started = time.monotonic()
            stages = []
            try:
                result = least_squares(fun, x0, bounds=(-5.5, 5.5),
                                       max_nfev=350, ftol=1e-12, xtol=1e-12,
                                       gtol=1e-12, diff_step=2e-7)
                stages.append(result.message)
                if fixed is not None:
                    # Discard the fixed-stage score before final optimization.
                    x1 = best["x"].copy()
                    fixed = None
                    best = {"x": x1.copy(), "cost": np.inf}
                    result = least_squares(fun, x1, bounds=(-5.5, 5.5),
                                           max_nfev=200, ftol=1e-12, xtol=1e-12,
                                           gtol=1e-12, diff_step=2e-7)
                    stages.append(result.message)
            except TimeoutError:
                stages.append("Bounded wall-clock timeout")
            final = search.diagnose(best["x"], m)
            record = {"orbits": m, "restart": restart, "family": family,
                      "initial_phase": phase, "used_alternate_window_stage": restart >= 6,
                      "elapsed_seconds": time.monotonic() - started,
                      "statuses": stages, "residual_calls": calls,
                      "final": final}
            records.append(record)
            output.write_text(json.dumps({
                "status": "HEURISTIC ONLY. No exact solution or impossibility result.",
                "random_seed": 970004, "maximum_seconds": 150,
                "elapsed_seconds": time.monotonic() - beginning,
                "convexity_weight": 15.0, "runs": records}, indent=2) + "\n")
            print(json.dumps({"m": m, "restart": restart, "family": family,
                              "hull": final["hull_vertices"], "n": 3 * m,
                              "spread": final["max_relative_squared_distance_spread"],
                              "turn": final["minimum_turn_sine"],
                              "separation": final["minimum_point_separation"]}), flush=True)


if __name__ == "__main__":
    main()

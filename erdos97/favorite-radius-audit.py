#!/usr/bin/env python3
"""Independent coordinate audit and bounded removal-of-convexity diagnostic.

The relaxation is not a construction: nonconvex point sets do not answer #97.
"""
import importlib.util
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares
from scipy.spatial import ConvexHull

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("favorite_search", HERE / "favorite-radius-search.py")
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


def independent_check(data, m):
    points = np.asarray(data["all_point_coordinates"])
    targets = np.asarray(data["selected_target_indices"])
    # Recompute squared lengths from serialized Cartesian coordinates, without
    # using the search's distance-selection routine or saved residuals.
    squared = np.sum((points[targets] - points[:m, None, :]) ** 2, axis=2)
    spreads = np.ptp(squared, axis=1) / squared.mean(axis=1)
    differences = points[:, None, :] - points[None, :, :]
    distances_squared = np.sum(differences * differences, axis=2)
    distances_squared[np.diag_indices_from(distances_squared)] = np.inf
    edges = np.roll(points, -1, axis=0) - points
    following = np.roll(edges, -1, axis=0)
    crosses = edges[:, 0] * following[:, 1] - edges[:, 1] * following[:, 0]
    return {"hull_vertices": len(ConvexHull(points).vertices),
            "total_vertices": len(points),
            "max_relative_squared_distance_spread": float(spreads.max()),
            "minimum_raw_consecutive_cross_product": float(crosses.min()),
            "minimum_pair_distance": float(np.sqrt(distances_squared.min())),
            "selected_indices_are_distinct": all(len(set(row)) == 4 for row in targets),
            "no_selected_self_incidence": all(i not in row for i, row in enumerate(targets))}


def main():
    runs = []
    for filename in ("favorite-radius-results.json", "favorite-radius-restart-results.json"):
        for record in json.loads((HERE / filename).read_text())["runs"]:
            record = dict(record, source=filename)
            runs.append(record)
    audits = []
    for m in (9, 12, 15, 20):
        eligible = [r for r in runs if r["orbits"] == m
                    and r["final"]["all_vertices_on_hull"]]
        record = min(eligible, key=lambda r: r["final"]["max_relative_squared_distance_spread"])
        x0 = np.asarray(record["final"]["parameters"])
        indices = np.asarray(record["final"]["selected_target_indices"])
        deadline = time.monotonic() + 8
        best = {"x": x0.copy(), "cost": np.inf}

        def unconstrained(x):
            if time.monotonic() > deadline:
                raise TimeoutError
            z = search.decode(x, m)
            p = search.all_points(z)
            selected = np.abs(z[:, None] - p[indices])
            mean = selected.mean(axis=1, keepdims=True)
            deviations = (selected - mean) / mean
            _, edges = search.geometry(z)
            collapse = 10 * np.maximum(search.EDGE_FLOOR - edges, 0) / search.EDGE_FLOOR
            value = np.r_[deviations.ravel(), collapse]
            score = float(value @ value)
            if score < best["cost"]:
                best.update(x=x.copy(), cost=score)
            return value

        try:
            result = least_squares(unconstrained, x0, bounds=(-5.5, 5.5),
                                   max_nfev=1800, ftol=1e-13, xtol=1e-13,
                                   gtol=1e-13, diff_step=1e-7)
            status = result.message
        except TimeoutError:
            status = "Eight-second bound reached"
        relaxed = search.diagnose(best["x"], m)
        relaxed_z = search.decode(best["x"], m)
        relaxed_p = search.all_points(relaxed_z)
        fixed_squared = np.abs(relaxed_z[:, None] - relaxed_p[indices]) ** 2
        fixed_spread = float(np.max(np.ptp(fixed_squared, axis=1) / fixed_squared.mean(axis=1)))
        audit = {"orbits": m, "source": record["source"],
                 "restart": record.get("restart"), "family": record["family"],
                 "best_convex_independent_check": independent_check(record["final"], m),
                 "relaxation_status": status,
                 "relaxation_original_fixed_target_spread": fixed_spread,
                 "relaxation_independent_check": independent_check(relaxed, m),
                 "relaxation_final": relaxed}
        audits.append(audit)
        print(json.dumps({k: v for k, v in audit.items() if k != "relaxation_final"}), flush=True)
    (HERE / "favorite-radius-audit.json").write_text(json.dumps({
        "status": "HEURISTIC ONLY. Relaxations deliberately remove convexity and cannot solve #97.",
        "audits": audits}, indent=2) + "\n")


if __name__ == "__main__":
    main()

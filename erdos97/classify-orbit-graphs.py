#!/usr/bin/env python3
"""Group finite directed candidate graphs by exact directed isomorphism.

This is a search convenience, not a geometric feasibility certificate.
Radii are not fixed when using an unlabelled representative: different
radius orders must not be silently excluded in a later geometric search.
"""
import json
from collections import defaultdict
from pathlib import Path

import networkx as nx


def main():
    here = Path(__file__).resolve().parent
    buckets = defaultdict(list)
    representatives = []
    graphs = []
    count = 0
    for line in (here / "eight-orbit-graphs.jsonl").read_text().splitlines():
        masks = json.loads(line)
        n = len(masks)
        graph = nx.DiGraph()
        graph.add_nodes_from(range(n))
        graph.add_edges_from((i, j) for i in range(n) for j in range(n)
                             if masks[i] & (1 << j))
        assert all(graph.out_degree(i) == 2 for i in range(n))
        # A coarse invariant only narrows the comparisons. Every merge
        # below still uses a full directed-graph isomorphism check.
        key = tuple(sorted(graph.in_degree(i) for i in range(n)))
        found = None
        for index in buckets[key]:
            if nx.is_isomorphic(graph, graphs[index]):
                found = index
                break
        if found is None:
            found = len(graphs)
            graphs.append(graph)
            buckets[key].append(found)
            representatives.append({"out_masks": masks, "labeled_count": 0})
        representatives[found]["labeled_count"] += 1
        count += 1
    assert count == sum(r["labeled_count"] for r in representatives)
    output = {
        "scope": "Abstract graphs only; neither radii nor coordinates are certified.",
        "radius_order_warning": "Geometric use of representatives must allow every radius order.",
        "labeled_count": count,
        "isomorphism_class_count": len(representatives),
        "classes": representatives,
    }
    (here / "eight-orbit-isomorphism-classes.json").write_text(
        json.dumps(output, indent=2) + "\n")
    print(f"{count} labeled graphs; {len(representatives)} directed isomorphism classes.")
    print("No geometric realizability is asserted.")


if __name__ == "__main__":
    main()

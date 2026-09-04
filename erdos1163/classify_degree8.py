"""Compute degree-eight transitive 2-group data using installed Sage/GAP.

Run: sage -python erdos1163/classify_degree8.py
This finite table guides proofs; it is not an asymptotic argument.
"""
from sage.all import libgap
from pathlib import Path
import json


def info(G):
    order = int(G.Size())
    phi = G.FrattiniSubgroup()
    derived = G.DerivedSubgroup()
    series = list(G.LowerCentralSeries())
    return dict(order=order, structure=str(G.StructureDescription()),
                exponent=int(G.Exponent()), nilpotency_class=len(series)-1,
                generator_rank=(order//int(phi.Size())).bit_length()-1,
                frattini_order=int(phi.Size()), center_order=int(G.Center().Size()),
                derived_order=int(derived.Size()),
                abelian_invariants=[int(a) for a in G.AbelianInvariants()])


def run():
    rows = []
    for idx in range(1, int(libgap.NrTransitiveGroups(8))+1):
        G = libgap.TransitiveGroup(8, idx)
        order = int(G.Size())
        if order & (order-1):
            continue
        row = dict(transitive_id=idx, **info(G))
        row['generators'] = str(G.GeneratorsOfGroup())
        lower = list(G.LowerCentralSeries())
        gamma3 = lower[2] if len(lower) > 2 else libgap.TrivialSubgroup(G)
        powers = libgap.Subgroup(G, libgap([x**4 for x in G.Elements()]))
        kill = libgap.ClosureGroup(gamma3, powers)
        quotient = libgap.FactorGroup(G, kill)
        row['class2_exponent4_quotient'] = info(quotient)
        row['obstruction_kernel_order'] = int(kill.Size())
        normals = []
        for K in G.NormalSubgroups():
            if not libgap.IsSubgroup(K, kill):
                continue
            Q = libgap.FactorGroup(G, K)
            qinfo = info(Q)
            qinfo['kernel_order'] = int(K.Size())
            normals.append(qinfo)
        row['class2_exponent4_normal_quotients'] = normals
        rows.append(row)
        print(idx, row['structure'], 'order', order, 'rank',row['generator_rank'],
              'class',row['nilpotency_class'],'exp',row['exponent'],
              'c2e4',row['class2_exponent4_quotient']['structure'], flush=True)
    destination = Path(__file__).with_name('degree8_groups.json')
    destination.write_text(json.dumps(rows,indent=2)+'\n')
    print(f'Wrote {len(rows)} transitive 2-group types to {destination}')


if __name__ == '__main__':
    run()

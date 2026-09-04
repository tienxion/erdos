# Further partial results for review

4 September 2026. These results were developed **after** the user's review of the submitted version 1. The proofs below are linked in full and have been independently audited within this research task. They have not been added to the public manuscript. The full Erdős problem remains open, and priority of these additional results remains unconfirmed.

## Exact mixed two-edge-star forests

For all integers $s,t\ge1$ and $r\ge0$,
$$
\widehat r(sP_3\sqcup rK_2,\ tP_3)=3(s+t-1)+2r.
$$
Here $P_3=K_{1,2}$. The proof reduces high-degree hosts by vertex deletion and explicitly colours every remaining graph of maximum degree two, using the parity of its cycle components and a bound on the red matching number. It covers arbitrarily long repeated bad diagonals, which the submitted local-gap theorem does not handle. The uniform case $r=0$ and one-star case $t=1$ are already known.

Full proof, known overlaps, and a precisely stated unresolved extension: [mixed two-edge-star theorem](improvement_plateaus.md).

## Additional local gap conditions

At a bad diagonal with even maximum, a drop of two now suffices without a restriction on the following gap. A drop of one also suffices when the following drop is positive, with the stated final-index convention.

The key lemma proves that a graph of positive odd maximum degree has a matching meeting all its maximum-degree vertices whenever those vertices induce a graph with independence number at most two. Removing the matching leaves even degree capacities that can be split by a 2-factorization. The equality-host argument supplies the required structure.

For example, for every $h,u\ge1$, take
$$
A=(2h+2,2h,\ldots,4,3,1^u),\qquad B=(5,1).
$$
Then
$$
\widehat r(F(A),F(B))=h^2+7h+5u+8.
$$
The previous recursive estimate left one edge of uncertainty here; the new matching argument closes it.

Full lemma, proof, and further exact families: [additional gap conditions](improvement_gap.md).

## A universal recursive lower bound

The same induction can retain a deficit at an unresolved diagonal while using the degree information for that computed lower bound to recover deficits at earlier diagonals. It yields a computable lower bound for every pair of star forests, at least as strong as Ricky Cipollini's diagonal sum minus the bad-diagonal count. Exactness follows whenever all deficits are recovered.

The full recurrence, conditional equality statements, proof, and examples are in [recursive lower bound](improvement_recursive.md). Simultaneous tails, the good-diagonal definition, and the original deficit bound remain attributed to Cipollini.

## Review boundary

The version 1 claim is already awaiting moderation. These follow-up proofs are a separate review package. Mathematical correctness, priority, and suitability for a journal are distinct questions; the independent task audits address the first. The original Győri–Schelp paper and Cheng thesis are still missing from the full-text literature comparison.

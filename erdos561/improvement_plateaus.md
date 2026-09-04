# Mixed unions of two-edge stars and edges versus uniform two-edge stars

4 September 2026. This is a separate research note. The theorem and proof below have passed two independent mathematical audits. The novelty assessment remains qualified as stated at the end. This does not solve general Erdős problem 561.

## Theorem

For all integers $s,t\ge1$ and $r\ge0$,

\[
\widehat r(sP_3\sqcup rK_2,\ tP_3)
=3(s+t-1)+2r.
\tag{1}
\]

Here $P_3=K_{1,2}$ has two edges, all unions are vertex-disjoint, and the host graphs are finite and simple. Copies need not be induced.

The conjectured diagonal sequence is $s+t-1$ copies of 3 followed by $r$ copies of 2. Thus the theorem handles arbitrarily long repeated bad diagonals of value 3; when $r>0$ their transition to value 2 has a gap of only one.

## Upper bound

Take the disjoint union of $s+t-1$ copies of $K_{1,3}$ and $r$ copies of $P_3$. Suppose a red-blue colouring has no blue $tP_3$.

Let $k$ of the $r$ small host components be entirely blue. The remaining $r-k$ each have a red edge. At most $t-1-k$ large host components can contain a blue $P_3$, because these blue copies and the $k$ small blue components are disjoint. Therefore at least

\[
(s+t-1)-(t-1-k)=s+k
\]

large host components have no blue $P_3$. In a three-edge star this forces at least two red edges, so each such component contains a red $P_3$. Use $s$ of them for the required red $sP_3$, one red edge from each of another $k$, and one red edge from each of the $r-k$ small components that are not entirely blue. These copies form a red $sP_3\sqcup rK_2$. The host has the number of edges in (1).

## Base case: one blue two-edge star

Let $F=sP_3\sqcup rK_2$, and suppose $G\to(F,P_3)$. Every matching $M$ of $G$ can be coloured blue, with all remaining edges red. Since the blue graph then has no $P_3$, $G-M$ contains $F$. Take a maximum matching. Also $G$ itself contains $F$, by colouring all edges red, so

\[
\nu(G)\ge\nu(F)=s+r.
\]

Consequently

\[
e(G)\ge |M|+e(F)\ge(s+r)+(2s+r)=3s+2r.
\]

Together with the upper bound this proves (1) for $t=1$. This is the matching-deletion argument already used for one-star targets in DJKR; it is included here to make the proof self-contained.

## A colouring lemma for graphs of maximum degree two

**Lemma.** Let $s,t\ge1$, $r\ge0$, and let $G$ have maximum degree at most 2 and

\[
e(G)\le 3(s+t-1)+2r-1.
\]

Then $G$ has a red-blue colouring with neither a red $sP_3\sqcup rK_2$ nor a blue $tP_3$.

**Proof.** Remove isolated vertices. Every component is a path or a cycle. Let $q$ be the number of odd-cycle components.

First suppose $q\le s+t-2$. Properly alternate colours on all paths and even cycles. On an odd cycle, alternation around the cycle gives exactly one pair of adjacent edges of the same colour; all other edges of that colour are isolated in its monochromatic graph, and the other colour is a matching. Assign this exceptional pair red on at most $s-1$ odd cycles and blue on at most $t-1$ odd cycles. Such an assignment exists because $q\le(s-1)+(t-1)$. The red graph contains fewer than $s$ disjoint copies of $P_3$, and the blue graph fewer than $t$. This proves the assertion in this case.

Now suppose $q\ge s+t-1$. Select $t-1$ distinct odd cycles. Colour components as follows.

* On every path, properly alternate colours, choosing blue for both end edges if its edge count is odd. Its red graph is a matching of size $\lfloor e(C)/2\rfloor$, and its blue graph is a matching.
* Properly alternate colours on each even cycle. Its red matching number is $e(C)/2$, and its blue graph is a matching.
* On each odd cycle not selected, alternate colours with the exceptional adjacent pair red. If its length is $2\ell+1$, its red matching number is $\ell$, and its blue graph is a matching.
* A selected $C_3$ or $C_5$ is coloured entirely blue. It contains at most one vertex-disjoint blue $P_3$, and its red matching number is zero, at most $\ell-1$.
* On a selected odd cycle of length $2\ell+1\ge7$, colour four consecutive edges blue and all remaining edges red. The blue graph is a five-vertex path, so it contains at most one vertex-disjoint $P_3$. The red graph is a path with $2\ell-3$ edges and $2\ell-2$ vertices, so its matching number is $\ell-1$.

The blue graph contains at most $t-1$ disjoint copies of $P_3$, one from each selected cycle. Matching numbers add across components. Before the decrease of at least one on each selected cycle, the sum of the red matching bounds is at most

\[
\left\lfloor\frac{e(G)-q}{2}\right\rfloor.
\]

Hence, writing $R$ for the red graph,

\[
\begin{aligned}
\nu(R)
&\le \left\lfloor\frac{e(G)-q}{2}\right\rfloor-(t-1)\\
&\le \left\lfloor
\frac{3(s+t-1)+2r-1-(s+t-1)}2
\right\rfloor-(t-1)\\
&=s+r-1.
\end{aligned}
\]

But $sP_3\sqcup rK_2$ has a matching of size $s+r$. Thus the red graph does not contain this forest. The lemma follows. $\square$

## Lower bound for all $t$

Induct on $t$, using the base case proved above. Suppose $t\ge2$ and

\[
G\to(sP_3\sqcup rK_2,\ tP_3).
\]

If a vertex $v$ has degree at least 3, valid largest-component deletion gives

\[
G-v\to(sP_3\sqcup rK_2,\ (t-1)P_3).
\]

Indeed, an avoiding colouring of $G-v$ extended by colouring all edges at $v$ blue could acquire at most one component of a vertex-disjoint blue $tP_3$ through $v$; the remaining $t-1$ components would already lie in $G-v$. The inductive hypothesis therefore gives

\[
e(G)\ge3+3(s+t-2)+2r=3(s+t-1)+2r.
\]

If instead $\Delta(G)\le2$, the colouring lemma excludes every host with fewer than this many edges. These two cases prove the lower bound and complete the theorem. $\square$

## Relation to earlier work and current limitations

The case $r=0$ is the classical uniform-star theorem. The case $t=1$ is the familiar one-star matching-deletion argument. Alternating colours on paths and cycles and distributing odd-cycle defects already appears in DJKR's proof of Theorem 2.2; no novelty is claimed for the first case of our colouring lemma. The additional case here allows more odd cycles by changing the colouring on selected cycles and controlling the red matching number, thereby accommodating the extra isolated-edge components. The full published DJKR paper gives two equal stars against a star forest whose component sizes are at least 2 (Theorem 2.4), and an all-odd theorem (Theorem 2.5). Neither stated hypothesis includes $r>0$ here when the other side has two-edge stars. [DJKR, published record](https://repozitorij.upr.si/IzpisGradiva.php?id=21994&lang=eng&print=); [preprint](https://arxiv.org/html/2111.02065).

Fu–Luo–Ni's current paper concerns uniform forests within each colour; when $r>0$, the first target in (1) is not uniform. [Current v3](https://arxiv.org/html/2606.04439v3).

The numerical Győri–Schelp condition quoted in DJKR fails at the final diagonal 2 when $r>0$. Cheng's thesis abstract describes a single nontrivial star plus a matching on each side; $s\ge2$ and $t\ge2$ put (1) outside that stated scope. The complete original Győri–Schelp paper and Cheng thesis have not been retrieved, so no unqualified novelty claim follows.

Rickyc's [6 August 2026 forum comment](https://www.erdosproblems.com/forum/thread/561#post-8384) already gives the simultaneous-tail framework, good-diagonal criterion, and the lower bound subtracting one for bad diagonals. Those are prior work. The proof above uses a direct colouring lemma for maximum-degree-two graphs to handle repeated bad diagonals. Whether this lemma or the exact mixed-forest formula has appeared elsewhere remains to be checked.

## Unresolved extension: matching components on both sides

The preceding theorem has no matching components in its blue target. A natural extension, not proved here, is

\[
\widehat r(sP_3\sqcup rK_2,\ tP_3\sqcup uK_2)
\stackrel{?}{=}3(s+t-1)+2\max(r,u)+\min(r,u)
\tag{2}
\]

for $s,t\ge1$ and $r,u\ge0$. The diagonal sequence is exactly $s+t-1$ copies of 3, then $\max(r,u)$ copies of 2, then $\min(r,u)$ copies of 1. Thus (2) is precisely the original conjectured value in this subcase. The standard diagonal-star construction proves its upper bound.

The lower bound reduces to the following concrete assertion, which remains open in this note:

**Unproved degree-two assertion.** Every finite simple graph $G$ of maximum degree at most 2 with

\[
e(G)<3(s+t-1)+2\max(r,u)+\min(r,u)
\]

admits a red-blue colouring avoiding both forests in (2).

Here is a complete justification of the reduction. First, for integers $v\ge1,w\ge0$,

\[
\widehat r(vK_2,\ P_3\sqcup wK_2)=2v+w.
\tag{3}
\]

For the upper bound take $vP_3\sqcup wK_2$. If there is no red matching of size $v$, at most $v-1$ host components have red edges. Thus at least $w+1$ components are entirely blue. At least one entirely blue component is a $P_3$, since otherwise each of the $v$ host copies of $P_3$ would supply a disjoint red edge. Use this blue $P_3$ and one edge from $w$ other blue components.

For the lower bound in (3), induct on $v$. At $v=1$ a Ramsey host must itself contain $P_3\sqcup wK_2$ and hence at least $2+w$ edges. If $v\ge2$, a Ramsey host has a vertex of degree at least 2, since otherwise colouring it entirely blue avoids the blue $P_3$. Deleting such a vertex and putting all its incident edges in red shows that the remainder arrows $((v-1)K_2,P_3\sqcup wK_2)$. Induction then charges at least $2+2(v-1)+w=2v+w$ edges.

Now suppose the unproved degree-two assertion were available and induct on $s+t$ in (2). When $s\ge2$, deleting a vertex of degree at least 3 in red reduces $s$ by one; when $t\ge2$, blue deletion reduces $t$ by one. In either case the proposed lower bound decreases by exactly 3, so induction handles all hosts of maximum degree at least 3. At $s=t=1$, assume by symmetry $r\ge u$. If $r\ge1$, red deletion reduces to $(rK_2,P_3\sqcup uK_2)$, and (3) again charges the required $3+2r+u$ edges. If $r=u=0$, the usual single-star result gives the bound 3 directly. This proves the claimed reduction.

The proved colouring lemma above settles this assertion when $\min(r,u)=0$. It does not by itself settle positive matching tails on both sides. In its second case, the red matching-number estimate can lose up to the extra $\min(r,u)$ edge contribution in (2). Requiring both colours to have matching numbers below those of their respective targets is too restrictive: on $C_5$, colouring two consecutive edges red and the other three blue avoids a monochromatic $P_3\sqcup K_2$, although the blue matching number is two.

A more exact formulation uses the vertex orders of monochromatic path and cycle components. A component on $c$ vertices can contain a union of $x$ disjoint copies of $P_3$ and $y$ disjoint edges whenever $3x+2y\le c$, and only then. Thus testing either target after a proposed colouring becomes a small packing problem over these component orders. This reformulation is valid but has not yet supplied a colouring that works for every host in the unproved assertion. No general both-mixed theorem is claimed.

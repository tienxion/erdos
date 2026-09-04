# Erdős problem 561: research notes

Date: 4 September 2026. **This does not solve the full problem.** The theorem below concerns two stars on each side, allowing single-edge components. Its argument was independently checked by a second research agent, but its novelty has not been established. The finite computations are exploratory checks, not a formal proof certificate for the general conjecture.

## Statement and current source status

For a nonincreasing positive-integer sequence A=(a_1,...,a_s), write F(A) for the vertex-disjoint union of the stars K_(1,a_i). The size Ramsey number is the minimum edge count of a finite simple host graph G for which every red/blue edge-colouring contains a red F(A) or a blue F(B).

[Erdős problem 561](https://www.erdosproblems.com/561) asks whether

$$
\widehat r(F(A),F(B))=\sum_{k=2}^{s+t}\max_{i+j=k}(a_i+b_j-1).
$$

The catalogue available during this investigation lists it as open. Literature checking matters here: [Fu, Luo and Ni, arXiv:2606.04439v1](https://arxiv.org/html/2606.04439v1), dated 3 June 2026, claimed the general result. The next version removed that claim. The [current v3 record](https://arxiv.org/abs/2606.04439), revised 4 July 2026, concerns **uniform** star forests; v2 explicitly calls the general conjecture open. Search-engine abstracts were still returning the obsolete full-solution claim.

## A false lemma in the superseded version

Lemma 2.3 of Fu–Luo–Ni v1 claims, in particular, that deleting an arbitrary host vertex allows one to delete the *smallest* star from a target forest while preserving the Ramsey property. Here is a complete counterexample to that lemma, not to Erdős problem 561.

Let F_1=K_(1,2) disjoint union K_2, F_2=K_2, and G=F_1. Then G arrows (F_1,F_2): a blue edge is already a blue F_2, and if there are no blue edges, the whole graph is a red F_1. Delete the centre v of the K_(1,2). The remaining nonisolated graph is a single edge. Colouring that edge red gives neither a red K_(1,2) nor a blue K_2. Thus G−v does not arrow (K_(1,2),K_2), contrary to the lemma.

The valid deletion implication drops the **largest** star instead: colour every edge incident with the deleted vertex in the relevant colour. Any copy of the original forest uses the deleted vertex in at most one component, so its surviving components contain the forest consisting of the original smallest s−1 stars. This change removes the induction inequality used in v1.

## Audited partial theorem: two stars on each side

For all positive integers a≥b≥1 and c≥d≥1,

$$
\widehat r(K_{1,a}\sqcup K_{1,b},K_{1,c}\sqcup K_{1,d})
=(a+c-1)+\max(a+d-1,b+c-1)+(b+d-1).
$$

This is a full proof of a special case of problem 561, not a solution for arbitrary star forests. Its novelty has not been established. The argument, including the single-edge components and exceptional small cases, was independently checked by another research agent and reviewed by the coordinating agent.

The external theorem inputs are:

1. Vizing's theorem: a finite simple graph of maximum degree D admits a proper edge-colouring with at most D+1 colours.
2. Davoodi, Javadi, Kamranian and Raeisi, [Theorem 2.3](https://arxiv.org/html/2111.02065), proves the formula for one star against a star forest whose component sizes are all at least 2. Its equality classification gives disjoint stars, with a K_3 replacement allowed exactly for a component paired as K_(1,2) against K_(1,2). The paper appeared in *Ars Mathematica Contemporanea* 25(2), P2.09 (2025), [DOI](https://doi.org/10.26493/1855-3974.3081.d6c).
3. Their Theorem 2.4 covers two equal stars against a star forest with all component sizes at least 2. We use this only under those stated hypotheses.
4. Fournier's theorem: if the subgraph induced by the maximum-degree vertices is a forest, the graph has a proper edge-colouring with exactly D colours. See Hilton and Zhao, [*On the Edge-Colouring of Graphs whose Core has Maximum Degree Two*](https://combinatorialpress.com/article/jcmcc/Volume%20021/vol-21-paper%207.pdf), *JCMCC* 21 (1996), 97–108. We call that induced subgraph the maximum-degree core.

All hosts are finite simple graphs. Isolated vertices can be removed whenever convenient. Every target here has no isolated vertices.

### Two elementary deletion facts

If G arrows (K_(1,a) disjoint union K_(1,b), K_(1,c) disjoint union K_(1,d)), then, for any vertex v,

$$
G-v\longrightarrow(K_{1,a}\sqcup K_{1,b},K_{1,d}). \tag{1}
$$

To prove this, colour G−v avoiding the displayed pair and colour every edge incident with v blue. No red target is created. A blue copy of the original target would leave at least one whole component in G−v; either component contains K_(1,d), a contradiction. Interchanging colours gives the other deletion implication.

Likewise, if H arrows (K_(1,a) disjoint union K_2,K_(1,d)), then H−w arrows (K_2,K_(1,d)) for every vertex w. Thus H−w contains K_(1,d): this follows by colouring all its edges blue.

We will repeatedly use the following observation. If a graph of maximum degree at most p+q−3 has a proper edge-colouring with at most p+q−2 colours, merging at most p−1 matching colour classes into red and at most q−1 into blue avoids both a red K_(1,p) and a blue K_(1,q). Vizing therefore implies that every Ramsey host for targets containing those largest stars has maximum degree at least p+q−2. If a graph with maximum degree exactly p+q−2 has a forest as its maximum-degree core, Fournier gives the same avoiding colouring.

### Auxiliary one-star formula allowing every positive component size

For any positive integers a_1,...,a_s,d, let F be the disjoint union of K_(1,a_i). Then

$$
\widehat r(F,K_{1,d})=\sum_{i=1}^s a_i+s(d-1).
$$

This follows from the matching-deletion argument in DJKR; the size argument itself does not require a_i≥2, although their equality classification does.

For the upper bound, take disjoint stars of sizes a_i+d−1. Unless one contains a blue K_(1,d), their centres each see at most d−1 blue edges and therefore at least a_i red edges, giving a red F.

For the lower bound, induct on d. When d=1, colouring all edges red shows that a Ramsey host H must contain F and has at least the displayed number of edges. For d≥2, take a maximum matching M in a Ramsey host H. Since H contains F, we have |M|≥s. Moreover,

$$
H-M\longrightarrow(F,K_{1,d-1}).
$$

Otherwise extend an avoiding colouring of H−M by colouring M blue. No red F is created. Every blue K_(1,d) would lose at most one edge on removal of the matching and would leave a blue K_(1,d−1), a contradiction. The induction hypothesis now gives

$$
e(H)\ge |M|+e(H-M)
\ge s+\sum_i a_i+s(d-2)
=\sum_i a_i+s(d-1).
$$

In particular, for a,d≥1,

$$
\widehat r(K_{1,a}\sqcup K_2,K_{1,d})=a+2d-1. \tag{2}
$$

When d=1 an equality host for (F,K_2) is exactly F, apart from isolated vertices, because it contains F and has exactly e(F) edges.

### Upper bound for the theorem

Put L_1=a+c−1, L_2=max(a+d−1,b+c−1), L_3=b+d−1 and S=L_1+L_2+L_3. Take three disjoint host stars with these edge counts.

The first star contains a red K_(1,a) or a blue K_(1,c). In the first case, if either remaining star contains a red K_(1,b), the red target is complete. Otherwise their centres each see at most b−1 red edges; the second supplies a blue K_(1,c), and the third supplies a disjoint blue K_(1,d). In the second case, either a remaining star supplies blue K_(1,d), or the second and third supply disjoint red stars of sizes a and b. This proves the S-edge upper bound.

### A rigid reduction for a hypothetical counterexample

Interchange the colours if needed so that a−b≥c−d. Then

$$
S=2a+b+c+2d-3.
$$

Suppose G is a Ramsey host with e(G)<S. Let D=Δ(G), choose a vertex v of degree D, and put H=G−v. Vizing gives D≥a+c−2. Equation (1), the one-star formula from DJKR when b≥2, equation (2) when b=1 and d≥2, and the trivial d=1 case give

$$
e(H)\ge a+b+2d-2.
$$

Hence e(G)≥S−1. Integrality and the assumed strict inequality force

$$
e(G)=S-1,\quad D=a+c-2,\quad e(H)=a+b+2d-2. \tag{3}
$$

### Case 1: b,d≥2

If a=2 or c=2, one of the target forests consists of two equal stars, and DJKR Theorem 2.4 applies. Otherwise a,c≥3, so D≥4.

The equality classification in DJKR Theorem 2.3 applies to H. Its nonisolated part is a disjoint union of K_(1,a+d−1) and K_(1,b+d−1), with a triangle permitted in place of a star only when its original component size and d are both 2.

Every vertex of H other than a star centre has degree at most 2 in H, hence at most 3 in G. Thus every degree-D vertex of G is v or a star centre of H. Distinct star centres are nonadjacent, so the maximum-degree core is a forest. Fournier and merging a−1 matching colour classes into red and c−1 into blue contradict the Ramsey property.

### Case 2: d=1

Equation (3) and H arrows (K_(1,a) disjoint union K_(1,b),K_2) imply that H is exactly that red target plus isolated vertices.

If c=1, the centre of K_(1,a) in H already has degree a>D=a−1, impossible. Thus c≥2. The gap inequality implies a≥2, so D≥2. When D≥3, every vertex other than v and the star centres has degree at most 2 in G, and the same core-forest contradiction applies.

When D=2, we have a=c=2. The gap inequality forces b=1, so both targets are K_(1,2) disjoint union K_2. Equation (3) gives e(G)=5 and Δ(G)=2. If G has no odd cycle, properly 2-edge-colour it. If it has C_5, that uses all five edges; colour two consecutive edges red and the other three blue. Neither colour contains the five-vertex target. Otherwise it has a triangle, using three edges, and at most two other edges; colour the triangle red and all other edges blue. Again neither colour contains the target. All possibilities contradict the Ramsey property.

### Case 3: b=1 and d≥2

If a−1=c−d, interchange the colours so that the new d is 1 and Case 2 applies. Thus assume

$$
a-1>c-d,\qquad a\ge2.
$$

Now e(H)=a+2d−1 and H arrows (K_(1,a) disjoint union K_2,K_(1,d)). Put r=Δ(H) and take a maximum-degree vertex w. The deletion facts and Vizing give

$$
a+d-2\le r\le a+d-1.
$$

If r=a+d−2, the graph H−w consists of a copy of K_(1,d), one further edge, and isolated vertices. Every vertex except w and that star's centre has degree at most 3 in H. If r≥4, its maximum-degree core is a forest, which contradicts the Ramsey property of H. Therefore this smaller-degree case can occur only when (a,d) is (2,2), (2,3), or (3,2). Those exceptions are treated below.

Consider the larger-degree case r=a+d−1. Then H−w is exactly K_(1,d) plus isolated vertices; write x for its centre. The inequality r≤D=a+c−2 gives c≥d+1. The strict gap inequality then implies a≥3, and D≥4. In G, every vertex outside {v,w,x} has degree at most 3, so a cycle in the maximum-degree core could only be the triangle vwx.

If c=d+1, then r=D, so v cannot be adjacent to w. If c≥d+2, then

$$
d_G(x)\le d+2<a+c-2=D.
$$

In both situations the triangle is impossible. Fournier again contradicts the Ramsey property of G.

It remains to treat the three smaller-degree exceptions.

**Exception (a,d)=(3,2).** The strict gap inequality permits c=2 or c=3. In both cases H has six edges, maximum degree 3, and at least six nonisolated vertices because it contains K_(1,3) disjoint union K_2. If its maximum-degree core has no cycle, Fournier applies. Otherwise it has at least three cubic vertices. Four cubic vertices would use all twelve incidences, leaving no room for six nonisolated vertices. Hence the core cycle is a triangle of exactly three cubic vertices. Their three remaining incident edges must go to three distinct pendant neighbours, because six nonisolated vertices are required and all six edges are now used. Properly colour the triangle with three colours and give each pendant edge the colour missing at its triangle endpoint. This is a proper 3-edge-colouring of H, again an avoiding colouring after merging classes.

**Exception (a,d)=(2,2).** The strict gap inequality forces c=2. The original G has seven edges and maximum degree 2. If it has at most one odd cycle, alternate colours on paths and even cycles and colour any odd cycle alternately with a single blue pair of consecutive edges. Red is a matching and blue has at most one K_(1,2), so neither target occurs. If it has two odd cycles, both are triangles and at most one edge remains. Colour one triangle red and everything else blue. Red has no K_(1,2) disjoint from an edge, and blue has at most one K_(1,2). This also contradicts the Ramsey property.

**Exception (a,d)=(2,3).** Here c=3, G has ten edges and maximum degree 3, and H has seven edges and maximum degree 3. We show that the only relevant obstruction to a proper 3-edge-colouring of H is K_4 with one edge subdivided.

First ν(H)=2, where ν is maximum matching size. The lower bound is supplied by its copy of K_(1,2) disjoint union K_2. If M is a matching, removing M leaves a Ramsey host for (K_(1,2) disjoint union K_2,K_(1,2)): extend an avoiding colouring by colouring M blue; any blue K_(1,3) would lose at most one edge and leave blue K_(1,2). Equation (2) gives e(H−M)≥5, hence |M|≤2.

If the cubic-vertex core has no cycle, Fournier gives a proper 3-edge-colouring. Otherwise let q be the number of cubic vertices. We have 3≤q≤4, since the sum of all degrees is 14.

If q=3, those vertices form a triangle and each has one additional incident edge. If those three edges have distinct external endpoints they form a matching of size 3. If they all meet one external vertex, that vertex is also cubic. The remaining possibility is a triangle ABC with edges AX,BX,CY. These account for six edges. The seventh edge cannot touch A,B,C. If it brings a new vertex, a matching of size 3 results: use XZ,AB,CY or YZ,AC,BX, or a new disjoint edge together with AB,CY, as applicable. The only other possible edge is XY, which makes X a fourth cubic vertex. Thus q=3 is impossible.

If q=4, the total degree outside the cubic vertices is 2. Either the cubic core is K_4 and the remaining edge is disjoint, which gives a matching of size 3; or the core is K_4 minus an edge xy. Its two missing incidences either lead to distinct pendant vertices, again giving a matching of size 3, or to one vertex u of degree 2. The latter is precisely K_4 with xy replaced by xu,uy.

Thus assume H has vertices x,y,z,w,u and edges xz,xw,yz,yw,zw,xu,uy, with all other vertices isolated. The new vertex v cannot be adjacent to x,y,z,w, which already have degree 3. If v is not adjacent to u, its three neighbours are new leaves; colour its star red and H blue. The red star cannot contain K_(1,2) disjoint from an edge, and H has only five vertices, so blue cannot contain two disjoint K_(1,3). If v is adjacent to u, its other two neighbours are new leaves. Colour zw red and all other edges blue. Every blue K_(1,3) is centred at x,y,u, or v, and all of them contain u; two cannot be vertex-disjoint. Red is a single edge. Both colourings contradict the assumed Ramsey property.

This completes every case and proves the two-star theorem.

### What remains open in this investigation

Nothing above handles arbitrary numbers s,t of star components. The reduction exploited that, after deleting one host vertex, one target becomes a **single** star. For longer forests the extremal classification needed for the same argument is unavailable here. No proof or counterexample to the full statement of problem 561 was obtained.

## Finite search

`search.cpp` reads graph6 hosts, enumerates edge masks of all copies of the two target forests, and solves the exact avoidance-colouring clauses by unit propagation and backtracking. A red-copy mask contributes a clause requiring at least one blue edge, and a blue-copy mask requires at least one red edge.

For each listed pair with conjectured answer S, `run_search.py` uses nauty 2.9.3 `geng -d1` to enumerate every unlabelled graph with exactly S−1 edges and every possible number of nonisolated vertices (at most 2(S−1)). Testing exactly S−1 edges suffices to look for counterexamples below S: any smaller Ramsey host could be padded with disjoint edges without losing its Ramsey property.

No counterexample was found in the following searches. Counts are host tests per pair, so repeated host graphs in different rows are counted again.

| First forest sizes | Second forest sizes | S | Hosts enumerated |
|---|---|---:|---:|
| 2,1 | 2,1 | 6 | 26 |
| 3,1 | 2,1 | 8 | 177 |
| 3,2 | 2,1 | 9 | 497 |
| 4,1 | 2,1 | 10 | 1,476 |
| 4,2 | 2,1 | 11 | 4,613 |
| 3,2 | 3,2 | 12 | 15,216 |
| 4,2 | 3,1 | 12 | 15,216 |
| 4,2 | 3,2 | 14 | 193,367 |
| 4,3 | 2,1 | 12 | 15,216 |
| 4,2 | 4,2 | 15 | 740,226 |
| 2,1,1 | 2,1,1 | 9 | 497 |
| 2,2,1 | 2,1,1 | 11 | 4,613 |
| 3,2,1 | 2,2,1 | 14 | 193,367 |

`verify_checker.py` independently enumerates all red/blue colourings for 128 small tests, including explicit Ramsey hosts from the constructive upper bound. All comparisons with the C++ checker passed. This is implementation validation; it is not independent formal verification of nauty or the full search.

Files: `search.cpp`, `run_search.py`, `verify_checker.py`, `results.json`, and `search.log`. nauty was downloaded from its [official site](https://users.cecs.anu.edu.au/~bdm/nauty/) and built in `/tmp/nauty2_9_3`; the compiled checker is `/tmp/erdos561_search`.

# A matching extension at a drop of two

Research draft, 4 September 2026. This extends the local sufficient criterion in [the submitted manuscript](submitted/v1/manuscript.tex). The simultaneous suffix framework and the good-diagonal degree bound originate in [rickyc's 6 August 2026 forum comment](https://www.erdosproblems.com/forum/thread/561#post-8384). This note adds an elementary matching argument in the maximum-degree core; it does not solve the general conjecture.

## 1. An elementary matching lemma

**Lemma.** Let G be a finite simple graph of positive odd maximum degree D. If the vertices of degree D form a clique, then G has a matching meeting every vertex of degree D.

**Proof.** Let C be the clique of degree-D vertices. If |C| is even, a perfect matching of G[C] suffices. If |C| is odd, then |C| is at most D: a clique in a graph of maximum degree D has at most D+1 vertices, and D+1 is even. Thus a vertex x of C has a neighbor y outside C, since its internal degree |C|-1 is strictly less than D. Take xy together with a perfect matching of C minus x. These edges form the required matching. The case |C|=1 is included. □

**Degree-splitting consequence.** If positive integers p,q have opposite parity and satisfy p+q-2=D, then such a graph has a red/blue coloring avoiding red K_(1,p) and blue K_(1,q).

To prove this, interchange colors if necessary so that p is even and q is odd. Remove the matching M in the lemma. Then G-M has maximum degree at most D-1, and both p-2 and q-1 are nonnegative even integers summing to D-1. Complete G-M to a simple (D-1)-regular graph and decompose it into 2-factors. Assign (p-2)/2 factors to red and (q-1)/2 factors to blue, and restrict to G-M. The resulting maximum degrees are at most p-2 and q-1. Add M to red. The final maximum degrees are at most p-1 and q-1, as desired. The zero-degree case is immediate.

The original special case p=2 is especially direct: color M red and all remaining edges blue.

The parity assumption matters. For even D, the graph K_(D+1) has a complete maximum-degree core of odd order and no matching covering that core. It actually arrows (K_(1,2),K_(1,D)): an avoiding red graph would have to be a matching covering all vertices, which is impossible.

## 2. Why a drop of two forces a complete core

Use the notation ell_k, S_k and the simultaneous suffix requirements P_k from the manuscript. Assume that the next suffix problem has the established lower bound S_(k+1), and every equality host for it has maximum degree at most ell_(k+1).

Suppose ell_k-ell_(k+1)=2 and G satisfies P_k with fewer than S_k edges. The existing degree/deletion argument forces

$$
e(G)=S_k-1,\qquad D=\Delta(G)=\ell_k-1.
$$

For **every** maximum-degree vertex x, the graph G-x has exactly S_(k+1) edges and satisfies P_(k+1). Therefore

$$
\Delta(G-x)\le\ell_{k+1}=D-1.
$$

Every other degree-D vertex must consequently be adjacent to x. Since x was arbitrary, the degree-D vertices of G form a clique. This conclusion uses no condition at all on the drop after ell_(k+1).

## 3. Extended sufficient criterion

**Theorem.** In the local criterion of the manuscript, add the following third allowed alternative at a bad nonfinal diagonal k:

> ell_k-ell_(k+1)=2, and ell_k is even.

Then the exact size Ramsey formula still holds. The old alternatives (a drop at least three, or a drop of two with the specified following independence condition) remain unchanged. Good diagonals remain unrestricted.

**Proof.** Retain the same descending induction, including the equality maximum-degree and independence assertions. Only the new alternative requires an additional argument. A hypothetical deficient host has D=ell_k-1 odd, and the preceding section shows that its maximum-degree core is a clique. Every maximizing pair p=a_i,q=b_j has opposite parity, because p+q-1=ell_k is even. The degree-splitting consequence of the matching lemma supplies a coloring avoiding the two largest stars for this maximizing pair. This contradicts the corresponding suffix Ramsey requirement. All equality assertions and the upper construction are unchanged. □

Thus a bad drop of two from an even maximum can now be followed by either a plateau or a drop of one, without restricting the maximizing component sizes.

## 4. A newly covered infinite family

For every integer r at least 2, let

$$
F_r=K_{1,3}\sqcup rK_2,\qquad
H_r=K_{1,5}\sqcup(r+1)K_{1,2}.
$$

Their diagonal maxima are

$$
7,\quad\underbrace{5,\ldots,5}_{r\text{ copies}},\quad
4,\quad\underbrace{2,\ldots,2}_{r\text{ copies}}.
$$

The first diagonal is good because its maximizing pair is (3,5). The value-5 diagonals have a maximizing pair (1,5), and the value-2 diagonals have a maximizing pair (1,2), so they too are good. The unique bad diagonal has value 4, attained by (3,2). It drops by two into a plateau of twos, satisfying the new alternative. Therefore

$$
\boxed{\widehat r(F_r,H_r)=11+7r.}
$$

The old local criterion fails at the value 4 for every r at least 2. The good/bad deficit bound gives only 10+7r. The new matching argument recovers that one missing edge. This establishes a strict improvement over those two stated criteria; priority over other literature remains to be checked.

## 5. A false stronger shortcut

It is not valid to replace the matching argument by the assertion that a graph whose maximum-degree core is a clique of size three is class 1. The graph K_5 minus one edge has maximum degree 4 and maximum-degree core K_3, but it has 9 edges. Four matching classes can cover at most 4 floor(5/2)=8 edges, so its edge chromatic number exceeds 4. It can nevertheless be split into a matching and a graph of maximum degree 3. Avoiding the two target stars is strictly weaker than producing a proper maximum-degree edge coloring.

## 6. Compatibility with the recursive lower bound

The same improvement applies to [the recursive lower bound](improvement_recursive.md). Add an extra recovery test

$$
\ell_k-d_{k+1}=2
\quad\text{and }\ell_k\text{ is even}.
$$

When this test holds, set d_k=ell_k. The hypothetical deficient host has odd D=ell_k-1, and deletion at any maximum-degree vertex yields an equality host for the recursively computed next lower bound, with maximum degree at most d_(k+1)=D-1. The same complete-core, matching, and even-factor splitting argument applies. No attainability of the recursive lower bound is assumed.

The matching-plus-factorization strengthening was suggested by the parallel number-theory agent and independently checked here. The proof adds no external ingredient beyond the parity splitting already used for good diagonals.

## 7. A stronger matching lemma and recovery at a drop of one

**Review status.** The root agent has completed a second independent audit of the full independence-number-two matching lemma and its gap-one consequence, including the disconnected-core and odd-connected-core cases. The rule allowing a following drop of one is now within the checked mathematical result. Integration into public versions remains the root agent's responsibility.

**Lemma.** Let G have positive odd maximum degree D. If the graph C induced by its degree-D vertices has independence number at most two, then G has a matching meeting every vertex of C.

We first note that every connected graph of independence number at most two has a Hamiltonian path. Indeed, let P be a longest path. If a vertex z lies outside P, neither endpoint of P is adjacent to z, so the endpoints must be adjacent to each other. The path can therefore be closed into a cycle. Connectivity gives an edge from that cycle to an outside vertex, which extends it to a longer path, a contradiction. The cases of at most two vertices are immediate.

**Proof of the lemma.** If C has even order and is connected, take alternate edges of a Hamiltonian path.

If C is disconnected, it has exactly two components, and each is a clique; otherwise three independent vertices would exist. Cover every even component internally. An odd clique component has order c at most D, and it has at least two distinct neighbors outside C. To check the latter assertion, if all its external neighbors consisted of a single vertex y, every clique vertex would need D-c+1 at most one external edge. Hence c=D and y would itself have degree at least D and belong to C, a contradiction. For each odd clique choose one edge to an outside vertex, choosing different outside endpoints if both cliques are odd, and match the remaining clique vertices internally.

It remains to treat connected C of odd order. Call a vertex v exposable when C-v has a perfect matching. The observation about Hamiltonian paths shows that a nonexposable vertex v must separate C into two odd cliques X,Y: there are at most two components after deletion, each is a clique if there are two, and two even components would have perfect matchings.

If such a nonexposable v exists, every other vertex w is exposable. For w in X, deleting w either leaves a connected graph, or separates the even clique X-w from the connected even-order graph Y+v; either way a perfect matching exists. The argument for Y is identical. If none of these exposable vertices had a neighbor outside C, every vertex of X and Y would have internal degree D. Since |X| and |Y| are odd and D is odd, the degree equation forces |X|=|Y|=D and every vertex of X and Y to be adjacent to v. This gives degree at least 2D at v, impossible. Thus an exposable w has a neighbor z outside C; use wz and a perfect matching of C-w.

Finally, if every vertex of connected odd C is exposable, some vertex must have an outside neighbor: otherwise C would be an odd-order D-regular graph with odd D, contrary to the degree-sum parity. Again use one outside edge and a perfect matching after deleting its endpoint in C. □

Combining this matching lemma with the even-factor splitting from Section 1 shows that an odd-maximum-degree graph whose maximum-degree core has independence number at most two avoids every pair of stars with opposite parity and size sum D+2.

**Additional local recovery rule.** Suppose ell_k is even, ell_k-ell_(k+1)=1, and either

- k+1 is nonfinal and ell_(k+1)-ell_(k+2) is at least 1; or
- k+1 is final and ell_(k+1) is at least 2.

Then this bad diagonal may also be admitted in the local exact criterion.

**Proof.** A deficient host has odd maximum degree D=ell_k-1=ell_(k+1). Deleting any maximum-degree vertex gives an equality host for the next suffix problem. Whenever the next diagonal has a positive drop, its equality host's degree-ell_(k+1) vertices form a clique: if two were nonadjacent, deleting one would leave the other above the following equality degree bound. At the final diagonal of size at least two there is at most one such vertex.

If the original maximum-degree core contained three independent vertices, deleting one would leave two nonadjacent vertices of degree D in that next equality host, a contradiction. Hence its independence number is at most two. Apply the stronger matching lemma and then the even-factor splitting to obtain the star-avoiding coloring. □

This argument also applies to recursive budgets: require ell_k even, ell_k-d_(k+1)=1, and d_(k+1)-d_(k+2) at least 1, with the same final-index exception. The equality clique assertion requires only a positive drop of the computed d-values. Independence flags alone do not record this extra information, but the clique assertion follows directly from the existing next equality bounds.

For example, take h,u at least 1,

$$
A=(2h+2,2h,\ldots,4,3,1^u),\qquad B=(5,1).
$$

The maxima are (2h+6,2h+4,...,8,7,5^u,1). The last bad value 8 drops by one to 7, followed by a drop of two, so the new rule recovers it. Every preceding even bad value drops by two and is recovered by Section 3. Thus

$$
\widehat r(F(A),K_{1,5}\sqcup K_2)
=h^2+7h+5u+8.
$$

The previous recursive estimate for this family left one edge of uncertainty. This identity closes that gap when the component of size 3 occurs once.

## 8. A strict-decrease corollary with one odd forest

**Corollary.** Suppose the diagonal maxima decrease strictly, and every odd-valued nonfinal diagonal is good. Then the conjectured formula holds. In particular, it holds under strict decrease whenever all component sizes in either one of the two forests are odd.

**Proof.** Each bad nonfinal diagonal then has even value. A drop of at least three uses the original rule; a drop of two uses Section 3; a drop of one uses Section 7, because the following drop is positive unless the next diagonal is final. In that final case its value is at least two: a bad even diagonal has value at least four, so a drop of one leaves at least three. Thus every diagonal is recovered. If all components of B are odd, every maximizing pair at an odd-valued diagonal has its A component odd as well, so that diagonal is good. The case of all components of A odd is symmetric. □

As a concrete example requiring the following-drop-one strengthening, for r at least 1 take A=(7^r,4,3,2), B=(5,1). The maxima are 11^r,8,7,6,2. The value 8 drops by one to 7, which again drops by one. All other bad values satisfy an earlier checked rule. The resulting formula is

$$
\widehat r(rK_{1,7}\sqcup K_{1,4}\sqcup K_{1,3}\sqcup K_{1,2},
           K_{1,5}\sqcup K_2)=11r+23.
$$

This last displayed family has an initial plateau of good values, so it follows directly from the full local criterion rather than the strict-decrease corollary itself.

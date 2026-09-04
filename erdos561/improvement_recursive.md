# A recursive refinement of the diagonal deficit lower bound

Research draft, 4 September 2026. This is a universal lower bound, not a solution of the full star-forest conjecture. Its prior-work starting point is [rickyc's forum post of 6 August 2026](https://www.erdosproblems.com/forum/thread/561#post-8384): the simultaneous-tail deletion property, the good-diagonal definition used below, and the bound \(S-\#\{\text{bad nonfinal diagonals}\}\) are all explicitly present there. The proposed additional step is to recover some deficits using equality information for recursively computed lower bounds, Fournier's theorem, and matchings covering the vertices of maximum degree.

## 1. Definitions and algorithm

Let \(A=(a_1\ge\cdots\ge a_s\ge1)\), \(B=(b_1\ge\cdots\ge b_t\ge1)\), and let \(F(A)\), \(F(B)\) be their star forests. Put \(m=s+t\) and
\[
\ell_k=\max_{i+j=k}(a_i+b_j-1),\qquad
S=\sum_{k=2}^m\ell_k.
\]
A diagonal \(k\) is **good** if some maximizing pair has both entries odd or has one entry equal to one. Otherwise it is **bad**. All maxima and indices are restricted to \(1\le i\le s\), \(1\le j\le t\).

Calculate positive integers \(d_k\) and Boolean flags \(I_k,J_k\) from right to left as follows:
\[
d_m=\ell_m,\qquad I_m=[\ell_m\ge2],\qquad J_m=\mathrm{true}.
\]
For \(k=m-1,m-2,\ldots,2\), set
\[
d_k=
\begin{cases}
\ell_k,&\text{if diagonal }k\text{ is good},\\
\ell_k,&\text{if }\ell_k-d_{k+1}\ge3,\\
\ell_k,&\text{if }\ell_k-d_{k+1}=2\text{ and either }I_{k+1}\text{ holds or }\ell_k\text{ is even},\\
\ell_k,&\text{if }\ell_k-d_{k+1}=1,\ \ell_k\text{ is even, and }J_{k+1}\text{ holds},\\
\ell_k-1,&\text{otherwise},
\end{cases} \tag{1}
\]
and then set
\[
I_k=[d_k-d_{k+1}\ge2],\qquad J_k=[d_k>d_{k+1}]. \tag{2}
\]
Let \(M_k=\sum_{r=k}^m d_r\). The recurrence uses \(d_{k+1}\), not \(\ell_{k+1}\); a deficit which remains at one diagonal can help recover a preceding deficit.

**Theorem.** For every pair of star forests,
\[
\boxed{M_2\le\widehat r(F(A),F(B))\le S.} \tag{3}
\]
Computing all diagonal maxima and their good/bad flags takes \(O(st)\) elementary operations; the recurrence itself takes \(O(s+t)\).

## 2. Simultaneous-tail invariant

For \(2\le k\le m\), write \(G\to\mathcal Q_k\) if
\[
G\to\left(\bigsqcup_{u=i}^s K_{1,a_u},
           \bigsqcup_{v=j}^t K_{1,b_v}\right)
\quad\text{for every }i+j=k.
\]
The deletion argument from the cited forum post gives
\[
G\to\mathcal Q_k\ \Longrightarrow\ G-x\to\mathcal Q_{k+1}
\quad(k<m) \tag{4}
\]
for every vertex \(x\). The relevant valid deletion removes the largest target component. When deleting any one component of a sorted star forest, the remaining components dominate the forest obtained by deleting its largest component.

Vizing's theorem, with matching colour classes merged into two colours, gives
\[
G\to\mathcal Q_k\ \Longrightarrow\ \Delta(G)\ge\ell_k-1. \tag{5}
\]
At a good diagonal the stronger bound
\[
\Delta(G)\ge\ell_k \tag{6}
\]
holds. For an odd–odd maximizing pair, this follows by completing a graph of maximum degree \(a_i+b_j-2\) to an even regular multigraph, applying Petersen's 2-factorization theorem, and dividing the factors into \((a_i-1)/2\) red and \((b_j-1)/2\) blue factors. If one maximizing entry is one, colouring all edges in the other colour proves (6). These are precisely the splitting facts used in the cited post.

We also use Fournier's theorem: a finite simple graph whose maximum-degree vertices induce a forest has a proper edge-colouring with \(\Delta(G)\) colours. In particular, if \(\Delta(G)=p+q-2\) and its maximum-degree core is a forest, merging \(p-1\) classes into red and \(q-1\) into blue avoids \((K_{1,p},K_{1,q})\).

Here is an additional splitting fact used by the even-\(\ell_k\) clause of (1).

**Core matching lemma.** Let \(G\) be a finite simple graph of positive odd maximum degree \(D\). If the subgraph \(C\) induced by its vertices of degree \(D\) has independence number at most two, then \(G\) has a matching covering every vertex of \(C\).

First observe that a connected graph of independence number at most two has a Hamiltonian path. The cases of at most two vertices are immediate. Otherwise let \(P\) be a longest path, which has at least three vertices. If \(z\) lies outside \(P\), neither endpoint of \(P\) is adjacent to \(z\). The endpoints must therefore be adjacent to each other. This closes \(P\) into a cycle, and connectivity supplies an edge from the cycle to an outside vertex, producing a longer path. That is a contradiction.

If \(C\) is connected and has even order, alternate edges of a Hamiltonian path give a perfect matching in \(C\).

If \(C\) is disconnected, it consists of exactly two cliques: three components, or two nonadjacent vertices within one component and a vertex in the other, would give three independent vertices. Match each even clique internally. An odd clique has order \(c\le D\), and at least two distinct neighbours outside \(C\). Indeed, every clique vertex needs \(D-c+1\ge1\) outside neighbours. If the only outside neighbour available to the entire clique were \(y\), then \(D-c+1=1\), \(c=D\), and \(d_G(y)\ge D\); this would put \(y\) in \(C\), a contradiction. Thus for each odd clique one can select an edge to an outside vertex, using distinct outside endpoints if both cliques are odd, and then match its remaining vertices internally.

It remains to consider connected \(C\) of odd order. Call \(v\in C\) *exposable* if \(C-v\) has a perfect matching; the empty graph has a perfect matching. If a vertex \(v\) is not exposable, the Hamiltonian-path observation and the independence-number bound show that \(C-v\) consists of two odd cliques \(X,Y\). Every other vertex \(w\) is exposable. For example, for \(w\in X\), the graph \(C-w\) is either connected of even order, or it separates the even clique \(X-w\) from the connected even-order graph \(Y+v\). In either case each relevant connected even-order graph has a Hamiltonian path and hence a perfect matching. The argument for \(w\in Y\) is identical.

If none of these exposable vertices has an outside neighbour, every vertex of \(X\) and \(Y\) has degree \(D\) within \(C\). Since \(|X|,|Y|,D\) are odd, the degree equations force \(|X|=|Y|=D\) and every vertex of both cliques to be adjacent to \(v\). This would give \(d_G(v)\ge2D>D\), a contradiction. Thus some exposable vertex has an outside neighbour. If instead every vertex of \(C\) is exposable, an outside neighbour must again exist: otherwise \(C\) would be an odd-order graph regular of odd degree \(D\), contrary to the degree-sum parity. In either situation, choose an outside edge at an exposable vertex and a perfect matching of the rest of \(C\). This proves the lemma, including \(D=1\).

**Splitting consequence.** Suppose \(p,q\ge2\) have opposite parity, \(\Delta(G)=D=p+q-2\), and the maximum-degree core has independence number at most two. Then \(G\not\to(K_{1,p},K_{1,q})\).

The integer \(D\) is odd. Remove a matching \(N\) covering the maximum-degree core, as supplied by the lemma. The remaining graph has maximum degree at most the even integer \(D-1\). Suppose, after interchanging colours if needed, that \(p\) is even and \(q\) is odd. The nonnegative capacities \(p-2\) and \(q-1\) are even and sum to \(D-1\). Even-regular completion and 2-factorization therefore split \(G-N\) into red and blue parts of maximum degrees at most \(p-2\) and \(q-1\). Colour \(N\) red. The final maximum degrees are at most \(p-1,q-1\), respectively, proving the consequence.

## 3. Proof, including the equality statements

We prove by descending induction on \(k\) that:

1. Every \(G\to\mathcal Q_k\) has \(e(G)\ge M_k\).
2. If \(G\to\mathcal Q_k\) and \(e(G)=M_k\), then \(\Delta(G)\le d_k\).
3. If additionally \(I_k\) is true, there is at most one vertex of degree \(d_k\).
4. If additionally \(J_k\) is true, the vertices of degree \(d_k\) induce a clique (possibly empty).

The equality assertions are conditional: the proof does not assume that an \(M_k\)-edge host actually exists.

At \(k=m\), the target pair consists of the two stars \(K_{1,a_s},K_{1,b_t}\). Its size Ramsey number is \(a_s+b_t-1=\ell_m\): a star supplies the upper bound, and a graph with at most \(a_s+b_t-2\) edges can be coloured with at most \(a_s-1\) red and \(b_t-1\) blue edges. The first two assertions follow. For the third, if a simple graph has \(e(G)=d_m\ge2\), it cannot have two vertices each incident with all its edges, since at most one edge is incident with both specified vertices. This also proves the clique assertion for \(d_m\ge2\); if \(d_m=1\), the two degree-one vertices are the adjacent endpoints of its unique edge. Thus all four assertions hold at the base.

Suppose \(k<m\) and the assertions hold at all subsequent diagonals. Choose a maximum-degree vertex \(x\) of a graph \(G\to\mathcal Q_k\). By (4) and the next lower bound,
\[
e(G)\ge\Delta(G)+M_{k+1}. \tag{7}
\]
If \(d_k=\ell_k-1\), (5) and (7) give the required lower bound. If \(k\) is good, use (6) instead. It remains to consider a bad diagonal at which one of the gap tests in (1) sets \(d_k=\ell_k\).

Assume for contradiction that \(e(G)<M_{k+1}+\ell_k\). For every vertex \(v\), deletion gives
\[
d_G(v)\le e(G)-M_{k+1}\le\ell_k-1.
\]
Together with (5), (7), and integrality, this forces
\[
e(G)=M_{k+1}+\ell_k-1,\qquad
D:=\Delta(G)=\ell_k-1,
\]
and
\[
H:=G-x\to\mathcal Q_{k+1},\qquad e(H)=M_{k+1}.
\]
The next equality assertion gives \(\Delta(H)\le d_{k+1}\).

If \(\ell_k-d_{k+1}\ge3\), every vertex other than \(x\) has degree in \(G\) at most \(d_{k+1}+1\le D-1\). The maximum-degree core therefore has only the vertex \(x\).

If \(\ell_k-d_{k+1}=2\) and \(I_{k+1}\) holds, every degree-\(D\) vertex other than \(x\) must be adjacent to \(x\) and have degree exactly \(d_{k+1}\) in \(H\). The next equality assertion allows at most one such vertex. Consequently the maximum-degree core of \(G\) has at most two vertices and is a forest.

Choose a maximizing pair \((i,j)\) on diagonal \(k\). In either case the core is a forest and
\[
D=\ell_k-1=a_i+b_j-2.
\]
Fournier's theorem gives a colouring avoiding the two largest stars and hence the corresponding two tail forests, contradicting \(G\to\mathcal Q_k\).

Next suppose \(\ell_k-d_{k+1}=2\) with \(\ell_k\) even, without the flag \(I_{k+1}\). The preceding equality argument applies when deleting **any** maximum-degree vertex \(x\). Therefore, after deleting any such vertex, the remaining maximum degree is at most \(d_{k+1}=D-1\). Two maximum-degree vertices of \(G\) must be adjacent: otherwise deleting one would leave the other of degree \(D\). Thus the maximum-degree core is a clique.

Finally suppose \(\ell_k-d_{k+1}=1\), \(\ell_k\) is even, and \(J_{k+1}\) holds. Here \(d_{k+1}=D\). If the maximum-degree core of \(G\) contained three independent vertices \(x,y,z\), deleting \(x\) would produce an equality host at the next level in which \(y,z\) retain degree \(D\) and are nonadjacent. This contradicts the next clique assertion. Thus the core has independence number at most two.

In each of these last two cases, choose a maximizing pair \((i,j)\). The integer \(a_i+b_j-1=\ell_k\) is even, so \(a_i,b_j\) have opposite parity. Since the present diagonal is bad, neither entry is one. The splitting consequence of the core matching lemma supplies a colouring avoiding the corresponding two tail forests, a contradiction. This completes the lower-bound proof.

Now suppose \(G\to\mathcal Q_k\) and \(e(G)=M_k\). Deleting an arbitrary vertex gives
\[
d_G(x)\le M_k-M_{k+1}=d_k,
\]
which proves the second assertion. If \(I_k\) holds and \(x,y\) are two distinct vertices of degree \(d_k\), then \(G-x\) has exactly \(M_{k+1}\) edges and satisfies \(\mathcal Q_{k+1}\). Its vertex \(y\) has degree at least \(d_k-1>d_{k+1}\), whether or not \(x,y\) are adjacent, contradicting the next equality bound. This proves the uniqueness assertion. Finally, if \(J_k\) holds and two vertices \(x,y\) of degree \(d_k\) were nonadjacent, the same deletion would leave \(y\) of degree \(d_k>d_{k+1}\), again contradicting the next equality bound. The clique assertion follows, completing the induction.

At \(k=2\), \(\mathcal Q_2\) is the original Ramsey requirement, proving the lower bound in (3). The standard disjoint-star host with component sizes \(\ell_2,\ldots,\ell_m\) supplies the upper bound. \(\square\)

## 4. Comparison with the earlier lower bound and the exact criterion

Let \(b\) be the number of bad nonfinal diagonals. Every good diagonal contributes \(d_k=\ell_k\), every other nonfinal diagonal contributes at least \(\ell_k-1\), and the final one contributes \(\ell_m\). Hence
\[
M_2\ge S-b.
\]
More precisely, the gain over that bound equals the number of bad diagonals for which a gap test in (1) succeeds.

If every bad nonfinal diagonal drops by at least three in the original \(\ell\)-sequence, all deficits are recovered. More generally, the previously proved local exact criterion is a corollary: a bad gap of two is sufficient if the following gap is at least two, or if the next diagonal is final and \(\ell_m\ge2\). Descending induction gives \(d_k=\ell_k\) at every diagonal under those hypotheses, so (3) becomes equality. The even-\(\ell_k\) clauses further recover a bad gap of two without either of these following-gap assumptions, including when the next diagonal begins a plateau; they also recover a bad gap of one when the following computed gap is positive, or when the next diagonal is final.

The recursive form also applies when the exact criterion fails. A bad diagonal with an original gap of two can be recovered if the next diagonal still has a deficit: then
\[
\ell_k-d_{k+1}
=\ell_k-(\ell_{k+1}-1)=3.
\]
Thus a single remaining deficit may suffice for a whole preceding block; the preceding deficits need not all be charged separately.

## 5. An explicit infinite family with only one remaining edge of uncertainty

Let \(h,u\ge1\) and \(r\ge2\). Take
\[
A=(2h+2,2h,\ldots,4,
       \underbrace{3,\ldots,3}_{r},
       \underbrace{1,\ldots,1}_{u}),
\qquad B=(5,1).
\]
There are \(h\) even components, followed by \(r\) copies of three and \(u\) edges. All successive gaps in \(A\) are at most two. As in the exact-family calculation, every diagonal except the last is strictly maximized in the \(b_1=5\) column. The full diagonal sequence is
\[
(2h+6,2h+4,\ldots,8,
 \underbrace{7,\ldots,7}_{r},
 \underbrace{5,\ldots,5}_{u},1).
\]
Its first \(h\) diagonals are bad and the remaining diagonals are good. The value 8 is followed by a plateau containing at least two copies of 7, so its gap is one and the next clique flag is false. The recurrence leaves its contribution at 7, losing one edge. If \(h\ge2\), the preceding value 10 now sees a difference of three from that computed contribution, so it is recovered. Its uniqueness flag is true, and all preceding even diagonals, each with gap two, are recovered in turn. Consequently
\[
M_2=S-1,
\qquad
S=h^2+7h+7r+5u+1.
\]
We obtain the universal, fully proved two-sided estimate
\[
\boxed{
h^2+7h+7r+5u
\le\widehat r(F(A),K_{1,5}\sqcup K_2)
\le h^2+7h+7r+5u+1.
} \tag{8}
\]

The earlier diagonal lower bound gives \(S-h\), so (8) improves it by \(h-1\) edges, unbounded as \(h\) grows, despite the local exact criterion failing at the value 8. This example does **not** determine which of the two consecutive integers in (8) is the exact answer. It compares the recurrence with the cited diagonal deficit bound; no claim is made that other available theorems cannot yield the same estimate for this particular family.

If instead \(r=1\), the value 7 is followed by 5 and hence has both its uniqueness and clique flags set. The final gap-one rule recovers the value 8, and all preceding even diagonals are recovered as well. Thus for every \(h,u\ge1\),
\[
\boxed{\widehat r\left(F(2h+2,2h,\ldots,4,3,1^u),\ K_{1,5}\sqcup K_2\right)
=h^2+7h+5u+8.}
\tag{9}
\]

## 6. A gap-two recovery followed by an arbitrarily long plateau

For \(r\ge2\), let
\[
A=(3,1^r),\qquad B=(5,2^{r+1}).
\]
The diagonal sequence is
\[
(7,5^r,4,2^r).
\]
Every diagonal other than the value 4 is good. Indeed, the values 7 and 5 have odd–odd maximizing pairs, and a maximizing pair for each value 2 contains a one. The value 4 is maximized by the pair \((3,2)\), so it is bad and even. It is followed by a gap of two and a plateau of length \(r\); thus its recovery uses the even-value rule, rather than the following uniqueness flag. The recurrence gives
\[
\boxed{\widehat r(F(3,1^r),F(5,2^{r+1}))=11+7r.}
\tag{10}
\]
The simpler earlier local spacing criterion does not recover this diagonal when \(r\ge2\).


## 7. A recovery that uses a following gap of exactly one

Take \(A=(4,3,1)\) and \(B=(3,2)\). Their diagonal maxima are
\[
(6,5,4,2).
\]
The value 5 is good because \((3,3)\) is a maximizing pair, and the value 2 is good because its maximizing pair contains a one. The values 6 and 4 are bad. The even gap-two rule recovers 4; the good value 5 then has \(J=\mathrm{true}\) and \(I=\mathrm{false}\), since its computed drop is exactly one. The final rule of (1) therefore recovers 6, proving
\[
\boxed{\widehat r(F(4,3,1),F(3,2))=17.}
\]
Replacing the final rule's clique flag by the stronger uniqueness flag would leave a lower bound of 16 here. This example shows that recording the clique assertion improves the recursion strictly.

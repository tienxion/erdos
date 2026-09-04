# A diagonal criterion for the star-forest size Ramsey formula

Research draft, 4 September 2026. The proof below establishes a sufficient condition for the formula in Erdős problem 561, not the full conjecture. **Novelty requires a literature audit.** The odd–odd degree-splitting argument comes from Davoodi, Javadi, Kamranian and Raeisi, *On a Conjecture of Erdős on Size Ramsey Number of Star Forests*, [arXiv:2111.02065](https://arxiv.org/html/2111.02065). The other external ingredients are Vizing's theorem and Fournier's theorem about a forest of maximum-degree vertices. No computational assertion is used in the proof.

## 1. Notation and criterion

Let
$$
a_1\ge\cdots\ge a_s\ge1,\qquad
b_1\ge\cdots\ge b_t\ge1,
$$
and let $F(A)=\bigsqcup_{i=1}^s K_{1,a_i}$, and similarly for $F(B)$. Put $m=s+t$, and, for $2\le k\le m$, define
$$
\ell_k=\max_{\substack{1\le i\le s,\ 1\le j\le t\\i+j=k}}
(a_i+b_j-1),
\qquad T_k=\sum_{r=k}^m\ell_r.
$$
The sequence $(\ell_k)$ is nonincreasing: every pair on a diagonal other than the first has a valid predecessor on the preceding diagonal with at least as large a sum.

Call diagonal $k$ **good** if it has a maximizing pair $(i,j)$ for which either both $a_i,b_j$ are odd, or $\min(a_i,b_j)=1$.

**Theorem.** Suppose that every $k\in\{2,\ldots,m-1\}$ which is not good satisfies at least one of the following:

1. $\ell_k-\ell_{k+1}\ge3$;
2. $\ell_k-\ell_{k+1}=2$, and either
   - $k+1<m$ and $\ell_{k+1}-\ell_{k+2}\ge2$, or
   - $k+1=m$ and $\ell_m\ge2$.

Then
$$
\boxed{\widehat r(F(A),F(B))=T_2.}
$$
No condition is imposed on the final diagonal, and good diagonals may have gaps zero or one. In particular, the simpler condition “every non-final diagonal is good or drops by at least three” suffices.

## 2. Two degree facts

For positive integers $p,q$, write $L=p+q-1$.

**Degree fact A.** If $G\to(K_{1,p},K_{1,q})$, then $\Delta(G)\ge L-1$. If both $p,q$ are odd, or if $\min(p,q)=1$, then $\Delta(G)\ge L$.

For the first assertion, if $\Delta(G)\le p+q-3$, Vizing gives a proper edge-colouring with at most $p+q-2$ colours. Merge at most $p-1$ matching classes into red and at most $q-1$ into blue. Their maximum degrees are at most $p-1,q-1$, respectively.

For odd $p,q$, the stronger assertion is the degree-splitting lemma of Davoodi et al. A graph of maximum degree at most the even integer $p+q-2$ can be embedded into an even regular graph of that degree, whose edges decompose into 2-factors by Petersen's theorem. Give $(p-1)/2$ factors the red colour and $(q-1)/2$ factors the blue colour, then restrict the colouring to the original graph. For $p=q=1$, a graph of maximum degree zero has no edges and the assertion is immediate. If $p=1$, colour all edges blue: any graph of maximum degree less than $q=L$ avoids the two required stars. The case $q=1$ is symmetric.

**Degree fact B.** If $\Delta(G)=p+q-2$ and the graph induced by its maximum-degree vertices is a forest, then $G\not\to(K_{1,p},K_{1,q})$.

Indeed, Fournier's theorem gives a proper edge-colouring with $\Delta(G)$ colours. Merge $p-1$ classes into red and the remaining $q-1$ classes into blue.

## 3. Simultaneous tail problems

It is important to preserve all tails at a given diagonal, rather than choose one deletion path. For $2\le k\le m$, let $\mathcal Q_k$ be the collection of Ramsey requirements
$$
G\longrightarrow
\left(\bigsqcup_{u=i}^s K_{1,a_u},
      \bigsqcup_{v=j}^t K_{1,b_v}\right)
\quad\text{for every valid }(i,j)\text{ with }i+j=k.
$$
Write $G\to\mathcal Q_k$ when every requirement in this collection holds. The avoiding colouring for different requirements need not be the same; the definition is simply their conjunction.

**Deletion observation.** If $k<m$, $G\to\mathcal Q_k$, and $x$ is any vertex, then $G-x\to\mathcal Q_{k+1}$.

To see the underlying deletion implication, suppose a target has component sizes $a_i,\ldots,a_s$, with at least two components. An avoiding colouring for the pair with its largest component removed extends to the original graph by colouring every edge incident with $x$ red. A newly created red forest uses $x$ in at most one component. After discarding that component, the remaining components contain the forest of sizes $a_{i+1},\ldots,a_s$: deleting any component from a nonincreasing list leaves a list which dominates the list obtained by deleting its largest component. The blue target cannot be created by these red edges. The same argument applies to blue deletion. Every valid pair on diagonal $k+1$ has a valid predecessor on diagonal $k$, so these implications prove the observation.

Also, if $G\to\mathcal Q_k$, then
$$
\Delta(G)\ge\ell_k-1, \tag{1}
$$
and if diagonal $k$ is good, then
$$
\Delta(G)\ge\ell_k. \tag{2}
$$
Choose a maximizing pair and note that its Ramsey requirement implies the corresponding requirement for its two largest stars; then apply Degree fact A.

For every $k$, the union
$$
\bigsqcup_{r=k}^m K_{1,\ell_r} \tag{3}
$$
satisfies all requirements in $\mathcal Q_k$, so a host with $T_k$ edges exists. Here is a direct verification. For fixed tail indices $i,j$, process the host stars in order. Maintain the first unfilled red and blue target indices $u,v$. At the stage indexed by $r=u+v$, the available host star has $\ell_r\ge a_u+b_v-1$ edges. Its centre therefore has at least $a_u$ red edges or at least $b_v$ blue edges. Assign the corresponding target component and advance that index. The components assigned at distinct stages are disjoint. The process finishes one of the target forests by the final stage. Initially $u=i,v=j$, and $u+v=k$, as required.

## 4. Descending induction, including equality information

We prove the following assertions by descending induction on $k$:

* every graph $G\to\mathcal Q_k$ has at least $T_k$ edges;
* if $G\to\mathcal Q_k$ and $e(G)=T_k$, then $\Delta(G)\le\ell_k$;
* in an equality host, the vertices of degree $\ell_k$ are independent whenever $k<m$ and $\ell_k-\ell_{k+1}\ge2$. At $k=m$, they are independent whenever $\ell_m\ge2$.

At $k=m$, there is only the pair $(K_{1,a_s},K_{1,b_t})$. Its size Ramsey number is $a_s+b_t-1=\ell_m$: the star with that many edges is an upper bound, and any graph with at most $a_s+b_t-2$ edges can be coloured with at most $a_s-1$ red edges and at most $b_t-1$ blue edges. An equality host has maximum degree at most its edge count $\ell_m$. If $\ell_m\ge2$, two vertices of degree $\ell_m$ cannot be adjacent—or even coexist—because each would have to be incident with every edge, whereas in a simple graph at most one edge is incident with both of two specified vertices.

Now take $k<m$ and assume all three assertions for later diagonals. Suppose, for contradiction, that $G\to\mathcal Q_k$ and $e(G)<T_k$. For any vertex $x$, deletion and the induction hypothesis give
$$
e(G)-d_G(x)=e(G-x)\ge T_{k+1}.
$$
Consequently $\Delta(G)\le\ell_k-1$. If diagonal $k$ is good, this contradicts (2). Otherwise (1), integrality, and deletion at a maximum-degree vertex $x$ force
$$
e(G)=T_k-1,\qquad
D:=\Delta(G)=\ell_k-1,\qquad
e(H)=T_{k+1},\quad H:=G-x\to\mathcal Q_{k+1}. \tag{4}
$$
By the equality information at the next diagonal,
$$
\Delta(H)\le\ell_{k+1}. \tag{5}
$$

If $\ell_k-\ell_{k+1}\ge3$, then every vertex of $G$ other than $x$ has degree at most
$$
\ell_{k+1}+1\le\ell_k-2=D-1.
$$
Thus the maximum-degree core of $G$ consists only of $x$.

If the gap is two, every degree-$D$ vertex of $G$ other than $x$ must be adjacent to $x$ and have degree exactly $\ell_{k+1}$ in $H$. The stated condition on the next diagonal guarantees that these vertices are independent in $H$, by the third induction assertion. Hence the maximum-degree core of $G$ is a star with centre $x$.

In either case that core is a forest. Choose any maximizing pair $(i,j)$ on diagonal $k$; then $D=a_i+b_j-2$. Degree fact B gives a colouring avoiding red $K_{1,a_i}$ and blue $K_{1,b_j}$, which also avoids their entire tail forests. This contradicts $G\to\mathcal Q_k$ and proves the lower bound.

It remains to establish the equality information for the present diagonal. Suppose $G\to\mathcal Q_k$ and $e(G)=T_k$. Deleting any vertex and applying the next lower bound gives
$$
d_G(x)\le T_k-T_{k+1}=\ell_k,
$$
as required. If $x,y$ are adjacent vertices of degree $\ell_k$, then $G-x$ is an equality host for $\mathcal Q_{k+1}$. Its vertex $y$ has degree $\ell_k-1$, whereas the next equality bound is $\Delta(G-x)\le\ell_{k+1}$. These inequalities contradict $\ell_k-\ell_{k+1}\ge2$. The independence assertion follows, completing the induction and the theorem. $\square$

## 5. An explicit family with arbitrarily long plateaus

Let $r,u\ge1$ be arbitrary integers. Set
$$
F=K_{1,6}\sqcup rK_{1,3}\sqcup uK_2,
\qquad H=K_{1,5}\sqcup K_2.
$$
The diagonal sequence is
$$
(\ell_2,\ldots,\ell_{r+u+3})
=\left(10,
\underbrace{7,\ldots,7}_{r\text{ terms}},
\underbrace{5,\ldots,5}_{u\text{ terms}},1\right).
$$
Only the first diagonal fails the odd–odd criterion, and its gap is three. Every other diagonal has an odd–odd maximizing pair. Therefore
$$
\boxed{
\widehat r(K_{1,6}\sqcup rK_{1,3}\sqcup uK_2,
           K_{1,5}\sqcup K_2)
=11+7r+5u.
}
$$

This family is not an instance of the published all-odd theorem, because of $K_{1,6}$, and it is not a pair of uniform forests. The first target has at least three components and at least two nontrivial stars. The final diagonal is one, so it does not satisfy the Győri–Schelp requirement $\binom{\ell_k}{2}\ge\sum_{j=k}^{s+t}\ell_j$. When $r$ or $u$ is large, the diagonal sequence has long constant runs, so it also lies outside a criterion requiring every successive diagonal gap to be at least two. These comparisons do not themselves establish novelty against all other literature.

The criterion also permits more than one exceptional diagonal. For arbitrary $r,u,v\ge1$, take component lists
$$
A=(10,\underbrace{7,\ldots,7}_{r},6,
       \underbrace{3,\ldots,3}_{u},
       \underbrace{1,\ldots,1}_{v}),\qquad B=(5,1).
$$
Their diagonal sequence is
$$
(14,\underbrace{11,\ldots,11}_{r},10,
       \underbrace{7,\ldots,7}_{u},
       \underbrace{5,\ldots,5}_{v},1).
$$
The only non-good values are 14 and 10, each followed by a drop of three. Thus the exact answer is
$$
\widehat r(F(A),F(B))=25+11r+7u+5v.
$$

### Arbitrarily many exceptional diagonals and an unbounded improvement over odd rounding

Fix $h\ge1$, positive integers $r_1,\ldots,r_h$, and $u\ge1$. Let $B=(5,1)$. Form $A$ by concatenating, in descending order $j=h,h-1,\ldots,1$, the blocks
$$
\left(4j+2,\underbrace{4j-1,\ldots,4j-1}_{r_j\text{ terms}}\right),
$$
and then append $u$ copies of $1$. Thus $A$ has $h+\sum_jr_j+u$ components.

Every successive drop in $A$ is one of $0,1,2,3$. For a list $A=(a_1,\ldots,a_s)$ and $B=(5,1)$, the diagonal values are
$$
\ell_2=a_1+4,\qquad
\ell_{i+1}=\max(a_{i-1},a_i+4)\quad(2\le i\le s),
\qquad \ell_{s+2}=a_s.
$$
Since $a_{i-1}-a_i\le3$, the second expression is always $a_i+4$, and $a_s=1$. Consequently the full diagonal sequence is obtained by concatenating
$$
\left(4j+6,\underbrace{4j+3,\ldots,4j+3}_{r_j\text{ terms}}\right)
\quad\text{for }j=h,h-1,\ldots,1,
$$
then appending $u$ copies of $5$ and a final $1$.

There are exactly $h$ non-good diagonals, namely the values $4j+6$. Each is attained strictly by the pair $(4j+2,5)$, so neither parity nor a component of size one makes it good. Each is followed by $4j+3$, a drop of three. Every remaining diagonal is attained by an odd–odd pair. The theorem therefore proves
$$
\boxed{
\widehat r(F(A),K_{1,5}\sqcup K_2)
=2h^2+8h+\sum_{j=1}^h r_j(4j+3)+5u+1.
} \tag{6}
$$

For comparison, round each even component $4j+2$ of $A$ down to $4j+1$, leaving every other component unchanged, and call the resulting list $A^-$. All its components and those of $B$ are odd. Its successive gaps are at most two, so the same calculation gives diagonal values $a_i^-+4$, followed by one. Exactly $h$ values have decreased by one. The published all-odd theorem and monotonicity thus give the direct lower bound
$$
\widehat r(F(A),F(B))
\ge\widehat r(F(A^-),F(B))
=2h^2+8h+\sum_{j=1}^h r_j(4j+3)+5u+1-h.
$$
Equation (6) improves this direct odd-rounding lower bound by exactly $h$ edges. The improvement is unbounded as $h\to\infty$, while the repetition parameters permit arbitrarily long plateaus between exceptional diagonals. This comparison does not claim that odd rounding is the strongest consequence obtainable from every result in the literature.

## 6. Independent audit of the separated-gap argument

The parallel argument with
$$
\min_{i<s}(a_i-a_{i+1})\ge
\max_{j<t}(b_j-b_{j+1})\ge
\min_{j<t}(b_j-b_{j+1})\ge2
$$
is sound for $s,t\ge2$. The condition makes each diagonal maximum occur in the first row or last column, giving
$$
T_2=\sum_{j=1}^t(a_1+b_j-1)
    +\sum_{i=2}^s(a_i+b_t-1).
$$
Deleting the largest blue component subtracts exactly $a_1+b_1-1$ from this expression. The proposed induction on $t$, including its equality maximum-degree and independence properties, is valid. Its base at $t=1$ follows from the one-star formula and red deletion of the largest component. The gap assumptions force $a_1,b_1\ge3$, so no maximum-degree-one boundary exception occurs in that induction. The diagonal theorem above includes the same mechanism without requiring that the diagonal maxima follow a fixed row-column path.

# Extensions investigated from the two-star theorem

Date: 4 September 2026. These are partial results on problem 561. Novelty has not been established.

## A proved family with separated component sizes

Let A=(a_1,...,a_s), B=(b_1,...,b_t) be decreasing positive integer sequences, with s,t>=2. Suppose

$$
2\le b_j-b_{j+1}\le a_i-a_{i+1}
\qquad(1\le i<s,\ 1\le j<t).
$$

Then the conjectured size Ramsey formula holds, and its value is

$$
S(A,B)=\sum_{j=1}^t(a_1+b_j-1)+\sum_{i=2}^s(a_i+b_t-1).
$$

This allows either sequence to end in 1. In addition, every equality host E has maximum degree at most L=a_1+b_1-1, and its vertices of degree exactly L are independent.

### Proof

The gap inequality ensures that, on any anti-diagonal i+j=k, moving one step from (i,j) to (i-1,j+1) does not decrease a_i+b_j. Thus the anti-diagonal maximum occurs at the smallest feasible i, giving the displayed formula. In particular, if B'=(b_2,...,b_t), then

$$
S(A,B)-S(A,B')=a_1+b_1-1=L.
$$

Use the usual disjoint-star construction for the upper bound. We prove the lower bound and the asserted properties of equality hosts simultaneously by induction on t.

For t=1, the elementary one-star formula gives

$$
\widehat r(F(A),K_{1,b_1})=\sum_i(a_i+b_1-1).
$$

For an equality host E, delete any vertex w and drop the largest red star. The resulting graph remains Ramsey for F(a_2,...,a_s) versus K_(1,b_1). The same one-star formula implies d_E(w)<=a_1+b_1-1=L. If two degree-L vertices w,u were adjacent, deleting w would give an equality host for the smaller red forest, whose maximum degree is at most a_2+b_1-1 (the same deletion argument, or its edge count if the smaller forest has one star). But u would have degree L-1>a_2+b_1-1, because a_1-a_2>=2. This proves the base case and both equality properties.

For t>=2, suppose G is Ramsey with e(G)<S(A,B). Set D=Delta(G), choose a maximum-degree vertex v, and put H=G-v. Vizing's theorem, followed by merging matching colour classes into a_1-1 red and b_1-1 blue classes, gives D>=L-1. Valid largest-star deletion gives H -> (F(A),F(B')), so induction gives e(H)>=S(A,B'). Integrality now forces

$$
e(G)=S(A,B)-1,\qquad D=L-1,\qquad e(H)=S(A,B').
$$

By the inductive equality properties, Delta(H)<=a_1+b_2-1. If b_1-b_2>=3, every vertex of G other than v has degree at most D-1; hence the maximum-degree core consists only of v. If b_1-b_2=2, a degree-D vertex other than v must have degree exactly a_1+b_2-1 in H. All such vertices are independent by induction, so the maximum-degree core of G is a star or a subgraph of a star. Fournier's theorem gives a proper D-edge-colouring, whose matching classes can again be merged to avoid even the two largest stars. This contradiction establishes the lower bound.

Finally, let E be an equality host for (A,B). For any vertex w, largest-blue-star deletion and induction imply

$$
d_E(w)\le S(A,B)-S(A,B')=L.
$$

If degree-L vertices w,u were adjacent, E-w would be an equality host for (A,B'), and u would have degree L-1>a_1+b_2-1, contradicting its inductive degree bound. This establishes the equality properties and completes the induction.

### Scope and novelty caution

The proof uses only the elementary one-star formula, valid largest-star deletion, Vizing, and Fournier; it does not need the DJKR equality classification. However, its novelty may be modest: the anti-diagonal maxima decrease by at least 2, so the Gyori-Schelp numerical inequality is automatically satisfied once the current maximum is at least 5. The potentially uncovered part occurs near terminal values 1 through 4. The original Gyori-Schelp proof and subsequent literature should be checked before presenting this as a new theorem.

## Independent audit of the stronger local criterion

The argument in `extensions_combinatorics.md`, and its manuscript version in `manuscript.tex`, has been checked independently. The stronger local criterion subsumes the separated-gap theorem above. The following points were checked explicitly:

- Simultaneous suffix deletion is valid for every feasible index pair on the next diagonal. The predecessor on the deleted side always contains at least two components; the argument removes the largest target component, not the smallest.
- The common upper host works for each suffix requirement separately. Starting at diagonal k, each selected red or blue component increases the sum of the current indices by exactly one, and one target forest is complete after at most s+t-k+1 host components.
- The single-star base works for every positive component size and both parities. If the final diagonal equals 1, no independence assertion is needed there. Under the spacing corollary, its predecessor is automatically good because every feasible maximizing pair contains a component of size 1.
- The contradiction at a bad diagonal forces all three equalities: the host has S_k-1 edges, its maximum degree is ell_k-1, and deleting a maximum-degree vertex leaves an equality host for the next simultaneous suffix problem.
- A gap of at least three makes the maximum-degree core a singleton. A gap of two makes it a star whenever the equality information at the next diagonal supplies independence. These are exactly the cases in the stated hypothesis, so applying Fournier's theorem introduces no additional assumption.
- The even-largest-component corollary requires its explicit maximizing-pair clause when the second forest has more than two components. For two components that clause follows from the displayed strict comparison of gaps.

No mathematical gap was found. One editorial point was sent to the manuscript author: the conclusion involving ell_3 should explicitly require s+t>2 before stating the separate single-star case.

The family with arbitrarily many exceptional diagonals was also checked. For h,u,r_1,...,r_h at least 1, let B=(5,1), and construct A by concatenating the blocks (4j+2,(4j-1) repeated r_j times), for j=h,h-1,...,1, followed by u copies of 1. Its maxima are the blocks (4j+6,(4j+3) repeated r_j times), followed by u copies of 5 and one copy of 1. There are exactly h bad diagonals, each dropping by three. The exact value obtained is

$$
2h^2+8h+\sum_{j=1}^h r_j(4j+3)+5u+1.
$$

Taking every r_j=u=1 gives 4h^2+13h+6. Rounding all even component sizes down to odd ones gives a lower bound smaller by exactly h, so the local criterion improves that direct consequence of the known all-odd theorem by an unbounded amount. This comparison is a mathematical statement, not a claim of established priority over the full literature.

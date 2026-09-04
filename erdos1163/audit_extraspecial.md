# The degree-eight extraspecial orbit: count and uniqueness

Independent derivation, 4 September 2026.

**Result.** There are exactly **105** subgroups of \(S_8\) in the
transitive extraspecial class \(E\cong D_8\circ D_8\). Their normalizers
have order **384**. In particular the proposed coefficient is
\[
\exp(z^2/2+4z^4/24+105z^8/40320)
=\exp(z^2/2+z^4/6+z^8/384).
\]

The normalizer calculation below is entirely elementary and does not
depend on computational enumeration.

## 1. A model in the centralizer of a matching

Fix the involution
\[
z=(12)(34)(56)(78).
\]
Its four two-point orbits will be called fibers. A permutation centralizes
\(z\) if and only if it permutes these fibers and is free to interchange
the two points within each fiber. Consequently
\[
W=C_{S_8}(z)\cong\mathbb F_2^4\rtimes S_4,
\qquad |W|=2^4\cdot4!=384.
\]
Let \(B_0\) be the even-weight subspace of the base group
\(\mathbb F_2^4\), and let
\[
V=\{1,(12)(34),(13)(24),(14)(23)\}\triangleleft S_4
\]
act by permuting the four fibers. Define
\[
E=B_0\rtimes V.
\]
This group has order \(8\cdot4=32\). It is transitive on the eight
points: \(V\) is transitive on the fibers, and \(B_0\) can interchange
the two points of any specified fiber by also flipping one other fiber.

## 2. Derived subgroup, center, and extraspecial type

Both \(B_0\) and \(V\) are abelian. For every nonidentity \(g\in V\)
and every even-weight \(b\), the vector \(b+gb\) is either zero or
\(\mathbf1=(1,1,1,1)\). Indeed, \(g\) is the product of two disjoint
transpositions, and even weight says that the two pairwise coordinate
sums coincide. Both possibilities occur, so
\[
E'=\langle\mathbf1\rangle=\langle z\rangle.
\]
Every nonidentity element of \(V\) acts nontrivially on \(B_0\).
Thus an element centralizing \(B_0\) has trivial \(V\)-component.
The \(V\)-fixed vectors in \(B_0\) are exactly \(0,\mathbf1\), whence
\[
Z(E)=E'=\langle z\rangle.
\]
Also \((b,g)^2=(b+gb,1)\), so all squares lie in \(E'\), and
\[
\Phi(E)=E'=\langle z\rangle,\qquad E/E'\cong C_2^4.
\]

For an explicit identification of the type, use fiber coordinates
numbered \(1,2,3,4\), and put
\[
u_1=(1,0,1,0),\quad u_2=(1,1,0,0),\quad
g_1=(12)(34),\quad g_2=(13)(24).
\]
Each pair \((u_i,g_i)\) consists of involutions with commutator \(z\),
so each generates \(D_8\). The two generated dihedral groups centralize
each other and meet precisely in \(\langle z\rangle\). They generate
\(E\), since \(u_1,u_2,z\) span \(B_0\) and \(g_1,g_2\) generate \(V\).
This proves directly that \(E\cong D_8\circ D_8\), the plus-type
extraspecial group of order 32.

## 3. The normalizer and the count 105

Write \(\pi:W\to S_4\) for the action on fibers. The group just
constructed has the intrinsic description
\[
E=\ker(\operatorname{sgn}|_W)\cap\pi^{-1}(V).
\]
To verify this, a permutation of two-point fibers has even sign on the
eight points, and the sign of a base flip is its weight modulo two.
Both factors in this intersection are normal in \(W\), so
\(W\leq N_{S_8}(E)\).

Conversely, \(z\) is the unique nonidentity central element of \(E\).
Every element normalizing \(E\) must therefore fix \(z\) under
conjugation. Hence
\[
N_{S_8}(E)\leq C_{S_8}(z)=W.
\]
This proves
\[
\boxed{N_{S_8}(E)=C_{S_8}(z),\qquad |N_{S_8}(E)|=384.}
\]
The number of conjugates is consequently
\[
\boxed{\frac{8!}{384}=105.}
\]
More strongly, these 105 conjugates correspond bijectively to perfect
matchings of the eight labels, by taking the nonidentity central
element. The number of matchings is also \(8!/(2^4 4!)=105\).

## 4. Uniqueness of the efficient degree-eight action

The primary source is Kovács–Praeger, *Finite permutation groups with
large abelian quotients*, Pacific J. Math. 136 (1989), 283–292:
[paper](https://archives.maths.anu.edu.au/people/Kovacs/K070.pdf).
The theorem on printed p. 283 classifies equality in the bound for
abelian prime-power quotients. Section 2, statement (11), printed
p. 286, specifically identifies the extraspecial group as the unique
transitive subgroup of a Sylow 2-subgroup of \(S_8\) with abelian
quotient of order at least 16.

For the proposed application, the theorem gives the following slightly
stronger conclusion. If \(T\leq S_8\) is transitive and has a quotient
isomorphic to \(C_2^4\), then \(T\) belongs to the class just constructed;
the assumption that \(T\) is a 2-group is unnecessary.

Indeed, a Sylow 2-subgroup of a transitive degree-eight group fixes no
point: a point stabilizer has index eight and therefore has strictly
smaller 2-part than the group. In the notation of that theorem, its
moved-point count is consequently \(k_2=8\). The elementary quotient
of order 16 attains the upper bound \(2^{k_2/2}\). In the equality list,
the only transitive action of degree eight is \(E\).

**Caution.** The theorem controls quotients of the whole orbit
projection. It does not by itself classify all subdirect subgroups or
prove that their product's commutator subgroup is present.

## 5. Consequence for the exact family polynomial

For completeness, let \(a,b,c\) count orbits of lengths \(2,4,8\),
respectively, and let \(a+2b+4c=m\). Define \(s_{a,b,c,k}\) to count
the \(k\)-subspaces of
\[
\mathbb F_2^a\times(\mathbb F_2^2)^b
                     \times(\mathbb F_2^4)^c
\]
surjecting onto every displayed factor. Its inclusion-exclusion
polynomial is
\[
(1-x)^a(1-3x+2x^2)^b
(1-15x+70x^2-120x^3+64x^4)^c
=\sum_t d_t x^t,
\]
and
\[
s_{a,b,c,k}=\sum_t d_t{m-t\brack k}_2.
\]
For the family containing the entire product of the orbit projections'
derived groups, the exact order polynomial is
\[
\sum_{a+2b+4c=m}
\frac{n!}{\delta!\,2^a a!\,24^b b!\,40320^c c!}
(1+3y)^b(105y)^c\sum_k s_{a,b,c,k}y^k.
\]
Each extraspecial factor adds exactly one to the binary logarithm of
the derived kernel. The surjectivity failure bound now uses at most
\(a+3b+15c\leq2n\) hyperplanes, so the previous uniform relative
error \(O(n2^{-m/4})\) applies without an essential change.

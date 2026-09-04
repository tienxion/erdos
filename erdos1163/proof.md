# Subgroups of prescribed power-of-two order in symmetric groups

Submitted by tienxion. 4 September 2026. A partial result relevant to Erdős 1163. This note
counts actual subgroups, not conjugacy classes, and does not determine
the order distribution of a uniformly chosen unrestricted subgroup.
Developed with OpenAI GPT-6 assistance, including independent agent
proof audits. No claim of novelty or prior expert endorsement is made.

Let
$$
a_{n,j}=\#\{H\leq S_n:|H|=2^j\}.
$$
Uniformly for integers $\lfloor n/4\rfloor\leq j\leq\lfloor n/2\rfloor$,
$$
\log_2 a_{n,j}\geq\frac{n^2}{16}
+\left(\frac{7n}{8}-\left|j-\frac{3n}{8}\right|\right)\log_2 n-O(n).
\tag{1}
$$
The groups supplying this bound have nilpotency class at most two,
exponent dividing four, and orbits of size at most eight. Combining
(1) with the upper bound for **all** 2-subgroups in Roney-Dougal–Tracey,
[Theorem 2](https://arxiv.org/html/2503.05416v1), gives the uniform conclusion
$$
\log_2 a_{n,j}=\frac{n^2}{16}+O(n\log n).
\tag{2}
$$
Thus every prescribed order in this interval attains the full quadratic
counting exponent. The remaining error can still change relative
probabilities substantially; (2) does not imply equidistribution.

## An explicit eight-point group

On $\mathbb F_2^2\times\mathbb F_2$, let $B_0$ consist of the flips
$$
(i,e)\longmapsto(i,e+b_i),\qquad \sum_i b_i=0.
$$
Let $V=\mathbb F_2^2$ translate the first coordinate, and put
$E=B_0\rtimes V$. It has order 32 and acts transitively: translations
move between fibers, while even flips can interchange the two points
of any chosen fiber. A nonzero translation exchanges the four indices
in two pairs. For even-weight $b$, the two pair sums agree, so
$b+v(b)$ is zero or the all-one vector $\mathbf1$; both values occur.
Consequently
$$
E'=\langle\mathbf1\rangle\cong C_2,
\qquad E/E'\cong\mathbb F_2^4.
$$
The square formula $ (b,v)^2=(b+v(b),0) $ shows that all squares
lie in the central derived group, proving the
class and exponent assertions. This classical degree-eight factor
appears in Kovács–Praeger,
[*Finite permutation groups with large abelian quotients*, §2](https://archives.maths.anu.edu.au/people/Kovacs/K070.pdf).

## Construction at every prescribed order

Assume $n\geq16$, and write
$$
m=\lfloor n/2\rfloor,\quad f=\lfloor m/2\rfloor,
\quad a=m-2f\in\{0,1\},\quad\delta=n-2m\in\{0,1\}.
$$
Take $k=f$, except when $m=2f+1$ and $j=m$, in which case take
$k=f+1$. Then $k\geq4$, $k(m-k)=\lfloor m^2/4\rfloor$, and
$z=j-k$ lies between zero and $f$. Set
$$
c=\min(z,f-z),\quad b=f-2c,\quad d=z-c.
$$
These are nonnegative integers satisfying
$$
a+2b+4c=m,\qquad c+d=z,\qquad d\in\{0,b\}.
$$
Partition the labels into $\delta$ singletons, $a$ pairs, $b$
four-point blocks, and $c$ eight-point blocks. Use $C_2$ on each
pair and $E$ on each eight-point block. On every four-point block
use the regular Klein four-group if $d=0$, or the transitive
dihedral group of order eight if $d=b$. When $b=0$, this
distinction is immaterial. Transport one fixed model to each labelled
block using its increasing ordering.

Their direct product $P$ satisfies
$$
P/P'\cong\mathbb F_2^m,\qquad |P'|=2^z.
$$
Every quotient factor has dimension at most four. Choose a linear
surjection from $\mathbb F_2^4$ onto each factor. The image of their
combined map surjects onto every factor and has dimension at most four;
extend it to a four-dimensional subspace $W\leq\mathbb F_2^m$.

For each $k$-dimensional subspace $U$ containing $W$, take its
full preimage $H$ in $P$. This group contains $P'$ and projects
fully onto each quotient factor, so it projects fully onto each orbit
group. Its orbits are exactly the chosen blocks and
$|H|=2^{k+z}=2^j$. Distinct $U$'s give distinct subgroups; different
partitions give different orbit decompositions. Therefore
$$
a_{n,j}\geq
\frac{n!}{\delta!\,2^a a!\,(4!)^b b!\,(8!)^c c!}
{m-4\brack k-4}_2.
\tag{3}
$$
All counted groups inherit the class and exponent restrictions from $P$.

The Gaussian coefficient satisfies
$$
{R\brack s}_2
=\prod_{i=0}^{s-1}\frac{2^R-2^i}{2^s-2^i}
\geq 2^{s(R-s)}.
$$
Thus the logarithm of the last factor in (3) is at least
$(k-4)(m-k)=n^2/16-O(n)$, uniformly in $j$.
Stirling's formula gives
$$
\log_2\frac{n!}{\delta!\,2^a a!\,(4!)^b b!\,(8!)^c c!}
=(n-b-c)\log_2 n+O(n)
$$
uniformly even if $b$ or $c$ is zero: use
$b\log b+c\log c=(b+c)\log n+O(n)$, with $0\log0=0$.
Finally,
$$
b+c=f/2+|z-f/2|,
\qquad
n-b-c=7n/8-|j-3n/8|+O(1).
$$
Substitution proves (1). The cited published upper bound proves (2).

The upper bound and the eight-point group are prior results. The
contribution of this note is the explicit prescribed-order construction
and its uniform estimate; whether this refinement is already recorded
in the literature has not been established.

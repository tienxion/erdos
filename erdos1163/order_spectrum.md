# Many subgroups of every prescribed order in a linear interval

4 September 2026. This is an order-specific counting result relevant
to Erdős 1163, not a limiting law for an unrestricted random subgroup.
Its construction uses elementary binary subspace counting and the
classical eight-point extraspecial group described in [progress_v3.md](progress_v3.md).
No novelty claim is made.

Write

$$
 a_{n,j}=\#\{H\leq S_n:|H|=2^j\}.
$$

**Theorem.** Uniformly over all integers
`floor(n/4)<=j<=floor(n/2)`, as n tends to infinity,

$$
\boxed{
\log_2 a_{n,j}\geq
\frac{n^2}{16}
+\left(\frac{7n}{8}-\left|j-\frac{3n}{8}\right|\right)
\log_2n-O(n).
}                                                       \tag{1}
$$

All the subgroups counted in this lower bound have nilpotency class
at most two, exponent dividing four, and orbits of size at most eight.
Moreover, uniformly over the same interval,

$$
\boxed{\log_2 a_{n,j}=\frac{n^2}{16}+O(n\log n).}       \tag{2}
$$

In particular, for **every** sequence of integers j(n) in that interval,
`log_2(a_(n,j(n)))/n^2 -> 1/16`.

## Proof of the lower bound

For `n>=16`, put

$$
 m=\lfloor n/2\rfloor,\quad
 f=\lfloor m/2\rfloor=\lfloor n/4\rfloor,\quad
 a=m-2f\in\{0,1\},\quad\delta=n-2m\in\{0,1\}.
$$

Normally take `k=f`. The only exception is `m=2f+1` and `j=m`,
when take `k=f+1`. Thus `k>=4`, `k(m-k)=floor(m^2/4)`, and

$$
 z=j-k\in\{0,\ldots,f\}.
$$

Set

$$
 c=\min(z,f-z),\qquad b=f-2c,\qquad d=z-c.
$$

All these numbers are nonnegative integers. If `z<=f/2`, then
`d=0`; if `z>=f/2`, then `d=b`. Also

$$
 a+2b+4c=m,\qquad c+d=z.                              \tag{3}
$$

Partition the n labelled points into delta singletons, a pairs,
b four-point blocks, and c eight-point blocks. On each pair use
`C_2`; on each four-point block use regular `V_4` if `d=0`, and
`D_8` if `d=b`; on each eight-point block use the transitive plus
extraspecial group E of order 32. If `b=d=0` the convention is
immaterial. Fix one embedded model on each labelled block, for example
by transporting fixed models along its increasing ordering.

Their ambient direct product P has

$$
 P/P'\cong\mathbb F_2^m,\qquad |P'|=2^{c+d}=2^z.
$$

The displayed quotient factors have ranks one, two, or four.
There is a subspace of dimension at most four surjecting onto every
factor: choose surjective linear maps from `F_2^4` to the displayed
factors and take the image of their combined map. Extend this image,
if necessary, to a four-dimensional subspace W of `F_2^m`.

Every k-space U containing W is therefore subdirect onto these
factors. Its full preimage H in P has the prescribed orbit projections
(surjectivity modulo the Frattini subgroup suffices), and

$$
 |H|=2^{k+z}=2^j.
$$

There are exactly `[m-4 choose k-4]_2` choices for U. Distinct U give
distinct H. Different labelled partitions also give distinct H,
because the full orbit projections are transitive and hence H
recovers its orbit partition. Consequently the following explicit
finite lower bound holds:

$$
 a_{n,j}\geq
 \frac{n!}{\delta!\,2^aa!\,(4!)^bb!\,(8!)^cc!}
 {m-4\brack k-4}_2.                                  \tag{4}
$$

The Gaussian coefficient is at least

$$
 2^{(k-4)(m-k)}=2^{n^2/16-O(n)},                       \tag{5}
$$

with an absolute uniform error. Stirling's formula gives, also
uniformly when b or c is zero,

$$
 \log_2\frac{n!}{\delta!\,2^aa!\,(4!)^bb!\,(8!)^cc!}
   =(n-b-c)\log_2n+O(n).                             \tag{6}
$$

For example, the uniformity follows by writing
`b log b+c log c=(b+c)log n+O(n)`, using the boundedness of
`x log x` on `[0,1]` and its continuous value zero at zero.

Finally

$$
 b+c=f/2+|z-f/2|,
$$

and `f=n/4+O(1)`, `k=f+O(1)`. Therefore

$$
 n-b-c=7n/8-|j-3n/8|+O(1).                           \tag{7}
$$

Combining (4)–(7) proves (1), including both parity cases and both
ends of the j interval.

## Upper bound and interpretation

Every subgroup of order `2^j` is a 2-group. Theorem 2 of
[Roney-Dougal and Tracey, *Subgroups of symmetric groups: enumeration
and asymptotic properties*](https://arxiv.org/html/2503.05416v1)
gives

$$
 a_{n,j}\leq|\operatorname{Sub}_2(S_n)|
        \leq2^{n^2/16+O(n\log n)}.
$$

Together with (1), this proves (2). The order-specific lower bound is
derived here from the explicit construction; the upper bound is the
published theorem just cited.

This shows that many widely separated exact orders attain the full
quadratic counting exponent. It does not determine their relative
probabilities under uniform sampling from all subgroups: errors at
the `n log n` scale can still change those probabilities substantially.

The proof uses no finite transitive-group classification and none of
the harder dominance theorems in the other research notes. Only the
explicit transitive E action with `E/E'` of rank four and `|E'|=2`,
elementary subspace counting, and the cited upper bound are needed.

## A matching second term inside the saturated family

The sharper upper bound below is a restricted-class statement. Let
$Q_n$ consist of full preimages of subdirect binary subspaces in
products of $C_2$ on pairs, regular $V_4$ or $D_8$ on four-point
blocks, and the specified extraspecial $E$ on eight-point blocks,
with exactly $\delta=n\bmod2$ fixed points. Thus every subgroup in
$Q_n$ contains the entire product of the orbit groups' derived
subgroups. Put
$$
q_{n,j}=\#\{H\in Q_n:|H|=2^j\}.
$$
Uniformly for $\lfloor n/4\rfloor\leq j\leq\lfloor n/2\rfloor$,
$$
\boxed{\log_2 q_{n,j}
=\frac{n^2}{16}
 +\left(\frac{7n}{8}-\left|j-\frac{3n}{8}\right|\right)
   \log_2n+O(n).}                                    \tag{8}
$$

**Proof.** The construction proving (4) belongs to $Q_n$, so it
already proves the lower bound in (8).

For the upper bound, fix a profile with $a$ pairs, $b$ four-point
blocks, $c$ eight-point blocks, and $d\leq b$ dihedral factors.
Write
$$
m=\lfloor n/2\rfloor=a+2b+4c,\qquad
B=a+b+c,\qquad z=d+c,\qquad j=k+z,
$$
where $k$ is the quotient-subspace dimension. The two elementary
inequalities
$$
B-z=a+b-d\geq0,\qquad
B-(m/2-z)=a/2+d\geq0
$$
give
$$
B\geq m/4+|z-m/4|.                                  \tag{9}
$$

The number of labelled orbit partitions is at most
$2^{(n-B)\log_2 n+O(n)}$, uniformly in the profile, by the same
factorial estimate as (6), now including $a!$. All choices of
embedded local groups and of the $d$ dihedral positions contribute
at most another $2^{O(n)}$, since each block has a fixed finite
number of choices. The number of $k$-subspaces is at most
$$
C\,2^{k(m-k)}.
$$
This follows from the Gaussian product formula and the positivity
of $\prod_{i\geq1}(1-2^{-i})$. Discarding failed subdirectness
only increases the count.

Put $u=k-m/2$ and $A=j-3m/4$. By (9), the logarithm of this
profile's contribution is at most
$$
\frac{m^2}{4}+(n-m/4-|A-u|)\log_2n-u^2+O(n).
$$
Using $|A-u|\geq|A|-|u|$ and
$$
-u^2+|u|\log_2n\leq\frac14(\log_2n)^2,
$$
this is at most
$$
\frac{m^2}{4}+(n-m/4-|j-3m/4|)\log_2n+O(n).
$$
There are only polynomially many profiles; summing them changes the
logarithm by $O(\log n)$. Finally $m=n/2+O(1)$, and the
absolute-value function is Lipschitz, giving the upper bound in (8).

This $O(n)$-accurate second term has been proved for $Q_n$.
The upper bound for unrestricted $a_{n,j}$ remains (2).
An exponentially small total-variation comparison with a larger
class does not by itself transfer (8), because individual prescribed
orders can have much smaller probabilities.

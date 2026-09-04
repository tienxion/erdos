# A necessary condition for a bounded excess in Erdős problem 295

**Update, 4 September 2026:** this earlier argument is preserved for reference. The [consolidated note](quantitative_obstructions.md) proves stronger exponential-tail and polynomial-ceiling bounds, and the [primary-source audit](literature_audit.md) explains the classical antecedents and the stronger available upper bound from Vose's theorem. The bounds quoted below from the problem page are historical bounds, not a complete account of available consequences of the literature.

This note proves a partial result. It does **not** resolve Erdős problem 295, and no novelty is claimed for the argument.

The problem asks whether, if \(k(N)\) is the least number of distinct integers \(a\geq N\) whose reciprocals sum to one, then
\[
k(N)-(e-1)N\longrightarrow\infty.
\]
The [problem page](https://www.erdosproblems.com/295) and [discussion page](https://www.erdosproblems.com/forum/thread/295?order=newest), checked on 4 September 2026, list the problem as open, with zero comments and zero proof claims. The recorded bounds are \(-c<k(N)-(e-1)N\ll N/\log N\). The historical source is H. D. Ruderman, P. Erdős and E. Straus, [solution of E2232](https://doi.org/10.2307/2317539), *American Mathematical Monthly* **78** (1971), pp. 302–303. The journal contents confirm the bibliographic entry; the article's proof has not been checked for this note, and the argument below does not use it.

## Proposition

Fix a real constant \(C\geq0\). There is \(N_0(C)\) such that the following holds for every integer \(N\geq N_0(C)\). If \(A\subseteq\{N,N+1,\ldots\}\) is finite and
\[
\sum_{a\in A}\frac1a=1,
\qquad |A|\leq(e-1)N+C,
\]
then
\[
\boxed{\max A\geq\exp\!\left(\frac{N}{132(C+1)}\right).}
\]

In particular, along any sequence of such representations for which \(\log\max A=o(N)\), the excess \(|A|-(e-1)N\) tends to infinity. Otherwise a subsequence would have excess at most some fixed \(C\geq0\), contradicting the proposition. This includes denominators bounded by \(N^B\) for any fixed \(B>0\).

## Proof

Put \(k=|A|\), \(L=N+k-1\), and \(I=\{N,\ldots,L\}\). The \(i\)-th smallest member of \(A\) is at least \(N+i-1\), so
\[
S:=\sum_{j=N}^{L}\frac1j\geq1.
\]
Let \(\delta=S-1\geq0\). The integral comparison for the decreasing function \(1/x\) gives
\[
S\leq \frac1N+\log\frac LN.
\]
Since \(L\leq eN+C-1\leq eN+C\), and \(\log(1+u)\leq u\) for \(u\geq0\), it follows that
\[
0\leq\delta\leq\frac{1+C/e}{N}\leq\frac{C+1}{N}. \tag{1}
\]
Conversely, \(S\geq1\) and the same integral comparison imply
\[
L\geq Ne^{1-1/N}.
\]
Consequently, whenever \(N\geq\max\{20,100(C+1)\}\),
\[
\frac52N\leq L\leq\frac{11}{4}N. \tag{2}
\]

Define the missing and added denominators by
\[
H=I\setminus A,\qquad E=A\setminus I.
\]
Because \(|I|=|A|\), we have \(|H|=|E|\). Subtracting the two reciprocal sums and using this equality gives the exact identity
\[
\delta
=\sum_{h\in H}\left(\frac1h-\frac1L\right)
 +\sum_{a\in E}\left(\frac1L-\frac1a\right). \tag{3}
\]
Every summand in (3) is nonnegative. By (2), each missing \(h\leq2N\) contributes at least
\[
\frac1{2N}-\frac1{(5/2)N}=\frac1{10N}.
\]
Each selected \(a\geq3N\) belongs to \(E\), because \(L<3N\), and contributes at least
\[
\frac1{(11/4)N}-\frac1{3N}=\frac1{33N}.
\]
Together with (1), these inequalities prove
\[
|H\cap[N,2N]|\leq10(C+1),\qquad
|A\cap[3N,\infty)|\leq33(C+1). \tag{4}
\]

Now let \(p\in(3N/2,2N]\) be prime and suppose \(p\in A\). Some other member of \(A\) must be divisible by \(p\). Otherwise \(1-\sum_{a\in A\setminus\{p\}}1/a\) would be a rational number admitting a denominator coprime to \(p\), whereas it equals \(1/p\), an impossibility. Such another member is a positive multiple of \(p\) distinct from \(p\), and is therefore at least \(2p>3N\).

It follows that every selected prime in \((3N/2,2N]\) divides
\[
Q=\prod_{a\in A\cap[3N,\infty)}a.
\]
Here an empty product is interpreted as one. Distinct primes are relatively prime, so their product divides \(Q\). Write \(\vartheta(x)=\sum_{p\leq x}\log p\). At most \(10(C+1)\) primes in this interval are missing, by (4). Thus
\[
\log Q\geq
\vartheta(2N)-\vartheta(3N/2)-10(C+1)\log(2N). \tag{5}
\]
Writing \(M=\max A\), the second estimate in (4) also yields
\[
\log Q\leq33(C+1)\log M. \tag{6}
\]
Equations (5) and (6) give the explicit finite inequality
\[
\boxed{
33(C+1)\log M\geq
\vartheta(2N)-\vartheta(3N/2)-10(C+1)\log(2N).
} \tag{7}
\]

The prime number theorem states that \(\vartheta(x)=x+o(x)\). Therefore
\[
\vartheta(2N)-\vartheta(3N/2)=\frac N2+o(N).
\]
Since \(C\) is fixed, the right-hand side of (7) is at least \(N/4\) for all sufficiently large \(N\). Dividing by \(33(C+1)\) and exponentiating proves the proposition. \(\square\)

## What is still missing

The original problem permits arbitrarily large denominators. The proposition shows that a hypothetical sequence of representations with bounded excess must use exponentially large denominators; it does not rule out such representations.

In particular, counting the primes in the selected interval cannot by itself count distinct added denominators: one enormous added denominator can contain many of those primes. Replacing that step by a claim that each prime requires its own added denominator would be invalid.

The use of the prime number theorem is only needed to convert the exact inequality (7) into the displayed exponential bound. All estimates preceding (7) are elementary.

## Why a general upper bound on denominators does not finish the proof

There is also a compatible upper bound \(\log M=O_C(N)\) under the same bounded-excess hypothesis. Here is the argument, included to make the remaining gap precise.

Let \(r=|A\cap[3N,\infty)|\). For sufficiently large \(N\), (5) makes \(r\geq1\), while (4) gives \(r\leq33(C+1)\). The positive residual
\[
R=1-\sum_{\substack{a\in A\\a<3N}}\frac1a=\frac uv
\]
in lowest terms has denominator \(v\) dividing \(\operatorname{lcm}(1,\ldots,3N-1)\). Hence \(\log v=O(N)\), for example by the usual equivalent form of the prime number theorem for the logarithm of this least common multiple.

Write the remaining denominators as \(d_1<\cdots<d_r\). If a positive residual with reduced denominator \(v_j\) is represented by \(r-j+1\) remaining unit fractions, then
\[
\frac1{v_j}\leq R_j\leq\frac{r-j+1}{d_j},
\qquad d_j\leq(r-j+1)v_j.
\]
After subtracting \(1/d_j\), the next reduced denominator satisfies
\[
v_{j+1}\leq v_jd_j\leq r v_j^2.
\]
Starting with \(v_1=v\), induction gives
\[
\log d_r\leq2^{r-1}\log v+(2^{r-1}-1)\log r=O_C(N).
\]
Thus the available arguments constrain a hypothetical counterexample to exponential denominators, from both above and below. These bounds are consistent. A proof excluding that regime is still required for the original problem.

## Verification scope

The harmonic-loss and prime-divisibility arguments were derived and checked independently by separate agents, then reviewed together. The improved interval \((3N/2,2N]\) and constant 132 were checked against the same inequalities. This is an informal mathematical proof of the stated partial result, with the prime number theorem as a standard input; it has not been formalized in a proof assistant. No claim is made that this partial result is new.

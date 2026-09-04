# A new attempt at the unrestricted tail obstruction

Date: 4 September 2026.

**Outcome:** this attempt did not prove divergence, divergence for almost every integer \(N\), or a new unrestricted lower bound beyond the existing constant bound. It establishes a counting refinement for possible cores and makes the remaining numerator problem explicit. These observations have not been checked for novelty and are not presented as publishable progress.

The current [research record](README.md) and [quantitative note](quantitative_obstructions.md) were read before this attempt. The approach below studies the number and global arithmetic of the core sums; it does not strengthen the existing prime-incidence arguments.

## 1. A bound on the number of possible polynomial cores

Fix \(C\geq0\). Let \(\mathcal B_{N,C}\) be the collection of sets
\[
B=A\cap[N,N^2]
\]
that occur in a representation
\[
\sum_{a\in A}1/a=1,
\qquad |A|\leq(e-1)N+C.
\]
Then
\[
|\mathcal B_{N,C}|\leq\exp(O_C(\sqrt N)).
\tag{1}
\]
This is sharper than the immediate bound obtained by choosing \(O_C(\sqrt N)\) arbitrary edits from a polynomial-size universe.

**Proof.** Put \(k=|A|\), \(L=N+k-1\), \(I=[N,L]\cap\mathbb Z\), and
\[
H=I\setminus A,\qquad E=A\setminus I,
\qquad \delta=\sum_{n=N}^{L}1/n-1.
\]
The harmonic comparison bounds \(k-(e-1)N\) below by an absolute constant. Thus, for fixed \(N,C\), only \(O_C(1)\) integer values of \(k\) are possible. For sufficiently large \(N\), we have \(L\leq3N\) and \(0\leq\delta\leq(C+1)/N\). The harmonic-loss identity gives
\[
\delta=
\sum_{h\in H}\frac{L-h}{hL}
+\sum_{a\in E}\frac{a-L}{aL}.
\]
Consequently,
\[
\sum_{h\in H}(L-h)
+\sum_{a\in E,\ a\leq4N}(a-L)
\leq12(C+1)N.
\tag{2}
\]
Indeed, the respective denominator products are at most \(9N^2\) and \(12N^2\). Also each \(a>4N\) contributes at least \(1/(12N)\), so there are at most
\[
q=\lfloor12(C+1)\rfloor
\]
such denominators.

Let \(W=\lfloor12(C+1)N\rfloor\). Apart from the possible zero offset \(L-h=0\), the holes and the additions at most \(4N\) are encoded by two finite subsets of positive integers with combined sum at most \(W\). For \(t=W^{-1/2}\), their number is at most
\[
\begin{aligned}
\exp(tW)\prod_{j\geq1}(1+e^{-tj})^2
&\leq\exp\!\left(tW+2\sum_{j\geq1}e^{-tj}\right)\\
&\leq\exp(3\sqrt W).
\end{aligned}
\]
The optional zero offset gives a factor of at most 2. The at most \(q\) core denominators in \((4N,N^2]\) have at most \((q+1)N^{2q}\) choices. Together with the \(O_C(1)\) possibilities for \(k\), these bounds prove (1). The number and sizes of denominators above \(N^2\) are not enumerated here. \(\square\)

The argument also reproves the edit bound: if \(h=|H|\), then distinct nonnegative hole offsets have sum at least \(h(h-1)/2\), so \(h=O_C(\sqrt N)\).

## 2. The exact numerator problem in the first possible tail range

For any core \(B\), write
\[
R_B=1-\sum_{b\in B}\frac1b=\frac{u_B}{v_B}>0
\]
in lowest terms. If there is exactly one denominator \(M>N^2\), then
\[
u_B=1,\qquad M=v_B.
\tag{3}
\]
Conversely, a positive unit residual whose denominator exceeds \(N^2\) completes that core with exactly one further term. Thus the one-tail question is an exact numerator test, not an estimate of prime capacity.

Let \(b_0=(e-1)/2\). The existing tail-count theorem gives
\[
1\leq r:=|A\cap(N^2,\infty)|
\leq D+b_0+o(1),\qquad D=|A|-(e-1)N.
\]
Therefore, for any fixed
\[
C<2-b_0=\frac{5-e}{2},
\]
a hypothetical sequence with \(D\leq C\) has exactly one such tail for sufficiently large \(N\). The subrange \(C<1-b_0\) was already excluded. The first unresolved constant-width range therefore already requires uniformly excluding (3) for the sparse collection of near-consecutive cores.

There is a useful but compatible exact scale in this case. Let
\[
Q=\operatorname{lcm}(1,\ldots,L)
\prod_{a\in B\setminus I}a.
\]
Every core denominator divides \(Q\). Since there are \(O_C(\sqrt N)\) added core denominators, each at most \(N^2\),
\[
\log Q=\psi(L)+O_C(\sqrt N\log N)=(e+o(1))N.
\]
Equation (3) implies \(M\mid Q\). The existing exponential-tail theorem supplies the reverse bound \(\log M\geq(e-o(1))N\), so in the one-tail case
\[
\log M=(e+o(1))N.
\tag{4}
\]
Equivalently, the explicit positive integer
\[
U_B=Q-\sum_{b\in B}Q/b
\]
must divide \(Q\), and the completion is \(M=Q/U_B\). The number of candidate cores in (1) is small, but no argument here excludes that divisibility relation.

## 3. A spectral reformulation of the same missing gap

Let \(B=\{b_1,\ldots,b_m\}\) and form the integer symmetric matrix
\[
K_B=\operatorname{diag}(b_1,\ldots,b_m)-\mathbf1\mathbf1^{\mathsf T}.
\]
The matrix is positive definite exactly when \(R_B>0\). Indeed, it is congruent to \(I-zz^{\mathsf T}\), where \(z_i=b_i^{-1/2}\), whose exceptional eigenvalue is \(1-\sum_i1/b_i=R_B\). Also
\[
\det K_B=\left(\prod_i b_i\right)R_B.
\tag{5}
\]
For the cores under consideration, \(R_B=O_C(N^{-2})\), because only \(O_C(1)\) positive unit fractions above \(N^2\) remain. The \(O_C(\sqrt N)\) edit bound gives
\[
T_2:=\sum_{b\in B}b^{-2}
=\frac{1-e^{-1}+o(1)}N.
\]
The smallest eigenvalue \(\lambda_B\) is the unique root in \((0,\min B)\) of
\[
\sum_{b\in B}\frac1{b-\lambda_B}=1.
\]
For \(\lambda\geq0\) below \(\min B\), the increase on the left from its value at zero is at least \(\lambda T_2\). Hence \(\lambda_B\leq R_B/T_2=O_C(N^{-1})\). Expanding at this small root then gives
\[
\lambda_B=\frac{R_B}{T_2}(1+o(1))
=\left(\frac e{e-1}+o(1)\right)N R_B.
\tag{6}
\]
A hypothetical one-tail example therefore gives an integer matrix of this special diagonal-minus-rank-one form with
\[
\lambda_B=\exp(-(e+o(1))N).
\]
This reformulation does not prove an improved gap. The determinant integrality bound obtained from (5) is far too weak, and common-denominator refinement returns to the already compatible scale \(\exp(-(e+o(1))N)\). No spectral theorem excluding this behavior for the required near-consecutive diagonals was established.

## 4. Why the sparse family does not prove an almost-everywhere result

The tempting heuristic is that \(\exp(O_C(\sqrt N))\) candidate sums should rarely hit an interval of length \(\exp(-cN)\) around 1. The counting statement (1) gives no distribution information and does not justify that heuristic. In particular, an arbitrary one-element rational family can contain \(1-1/Q_N\) with \(Q_N\) exponential in \(N\). This example is not an admissible core construction; it demonstrates only the logical insufficiency of cardinality information alone.

A union-bound or Borel–Cantelli argument can control approximation to almost every **real target** from a sparse family. It does not control a fixed target such as 1 for almost every integer \(N\). These are different quantifiers. Moreover, exact finite unit-fraction representations already require rational targets, which form a measure-zero set.

For context, Bettin, Molteni and Sanna's primary paper [Small values of signed harmonic sums](https://sites.unimi.it/molteni/research/papers-pdf/43-molteni-Small_values_of_signed_harmonic_sums.pdf), *C. R. Math.* **356** (2018), 1062–1074, distinguishes this issue explicitly: its almost-everywhere lower bounds concern the real target parameter, whereas its fixed-target results concern a different approximation problem involving all sign patterns. Those statements do not supply the missing uniform estimate for the near-consecutive cores here.

## Final assessment

The counting lemma and the exact numerator/spectral formulations are valid internal deductions. They neither rule out a unit residual for every sufficiently large \(N\) nor show that such residuals occur for only a density-zero set of integers. Even the first one-tail range remains open in this attempt. Any claimed progress beyond these reductions would require a new uniform arithmetic separation result for the specially structured core sums; none was proved.

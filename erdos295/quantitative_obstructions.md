# Quantitative obstructions for nearly shortest Egyptian fractions

Research note, 4 September 2026. **This is not a solution of Erdős problem 295, and it is not a submission-ready manuscript.** The arguments below strengthen the previous local note, but novelty and publication-level significance have not been established. See [the primary-source audit](literature_audit.md), [the independent exponential-bound review](quantitative_review.md), [the polynomial-bound review](polynomial_cap_review.md), and [the subquadratic review](subquadratic_review.md).

Throughout, \(A\) is a finite set of distinct integers at least \(N\), and
\[
\sum_{a\in A}\frac1a=1,\qquad
k=|A|,\quad D=k-(e-1)N,\quad M=\max A,
\qquad b=\frac{e-1}{2}.
\]
All logarithms are natural. Asymptotic assertions concern sequences with \(N\to\infty\). The original problem asks whether the *unrestricted* minimum possible \(D\) tends to infinity.

## Results

**Theorem 1 (exponential tail).** If \(D=o(N/\log N)\), then
\[
\liminf_{N\to\infty}\frac1N
 \log\!\prod_{\substack{a\in A\\a>N^2}}a\ \ge e, \tag{1}
\]
and
\[
\liminf_{N\to\infty}\frac{(D+b)\log M}{N}\ge e. \tag{2}
\]
More precisely, with \(r=|A\cap(N^2,\infty)|\),
\[
1\le r\le D+b+O\!\left(\frac{(D+1)^2}{N}\right)
\tag{3}
\]
for sufficiently large \(N\); the lower inequality follows from (1).

**Corollary 1.1 (bounded excess).** Fix \(C\ge0\), and put
\[
q=\left\lfloor C+\frac{e-1}{2}\right\rfloor.
\]
If \(q=0\), representations with \(D\le C\) do not exist for sufficiently large \(N\). If \(q\ge1\), every sequence of such representations satisfies
\[
\liminf\frac{\log M}{N}\ge\frac e q. \tag{4}
\]
Thus a fixed additive excess forces a bounded number of denominators above \(N^2\), whose product has logarithm at least \((e-o(1))N\). This improves the coefficient in the earlier local bound \(\log M\ge N/[132(C+1)]\).

**Corollary 1.2 (a subexponential ceiling).** If \(F=F(N)\) satisfies
\[
\log N=o(\log F),\qquad \log F=o(N),
\]
then every representation with \(M\le F\) satisfies
\[
D\ge(e-o(1))\frac{N}{\log F}. \tag{5}
\]
For example, \(M\le\exp(N^\alpha)\), \(0<\alpha<1\), implies

\[
D\ge(e-o(1))N^{1-\alpha}.
\]

**Theorem 2 (a polynomial ceiling).** Fix \(B>1\). Every sequence of representations with \(M\le N^{B+o(1)}\) satisfies
\[
D\ge(\mathcal C(B-1)-o(1))\frac{N}{\log N}, \tag{6}
\]
where, for real \(h>0\),
\[
\mathcal C(h)=e\int_0^e\min\left\{w(x),\frac1{eh}\right\}\,dx,
\qquad
w(x)=\sum_{\substack{m\ge1\\1\le mx\le e}}
\left(\frac1{mx}-\frac1e\right).
\]
Writing \(c_t=\mathcal C(t)\) for positive integers \(t\),
\[
\begin{aligned}
c_1&=e\log2-2+\frac{5e}{6}\log\frac65+\frac e2\log3
       =1.79033944\ldots,\\
c_2&=e\log\frac32-\frac32+\frac e2\log3
       =1.09533735\ldots,\\
c_t&=e\log\left(1+\frac1t\right)\qquad(t\ge3).
\end{aligned} \tag{7}
\]
In particular, \(M\le N^{2+o(1)}\) gives the constant \(c_1\), \(M\le N^{3+o(1)}\) gives \(c_2\), and for \(B\ge4\) the constant is \(e\log(B/(B-1))\). The component argument below is stronger than simply counting at most \(\lfloor B\rfloor\) large primes per denominator.

**Theorem 3 (subquadratic multiplicity).** If \(1<B<2\) and \(M\le N^{B+o(1)}\), put \(s=\lceil1/(B-1)\rceil\). Then
\[
D\ge(d_s-o(1))\frac N{\log N},\qquad
d_s=\mathcal C(1/s)
=e\int_0^e\min\{w(x),s/e\}\,dx. \tag{7a}
\]
More generally, for each fixed integer \(s\ge2\), the same bound holds if
\[
M=o\!\left(N^{1+1/(s-1)}\right). \tag{7b}
\]
Thus \(M=o(N^2)\) yields \(d_2=2.59516741\ldots\), whereas Theorem 2 supplies \(c_1=1.79033944\ldots\) at \(N^{2+o(1)}\). Also \(d_s=\log s+O(1)\) as \(s\to\infty\). These are lower-bound constants, not claimed optimal constants. No matching construction under the same ceiling has been established here.

**Classical comparison.** The historical bound displayed on the problem page is not the strongest upper bound obtainable from established results. Vose's uniform Egyptian-fraction theorem implies
\[
k(N)\le(e-1)N+O(\sqrt N),
\]
with maximum denominator \(\exp(O(N))\) available simultaneously. This is a standard corollary, not a novelty claim. A proof and checked primary references are in the [literature audit](literature_audit.md). Croot's interval construction gives the available polynomial-ceiling upper excess \(O(N\log\log N/\log N)\); the constrained upper and lower bounds here still differ by a factor \(\log\log N\) for fixed \(B>1\).

## 1. The harmonic loss identity

Set
\[
L=N+k-1=eN+D-1,\quad I=[N,L]\cap\mathbb Z,
\quad H=I\setminus A,\quad E=A\setminus I.
\]
Since \(|H|=|E|\),
\[
\delta:=\sum_{j=N}^{L}\frac1j-1
=\sum_{h\in H}\left(\frac1h-\frac1L\right)
 +\sum_{a\in E}\left(\frac1L-\frac1a\right)\ge0. \tag{8}
\]
The nonnegativity also follows by ordering the elements of \(A\).

The elementary bound
\[
1\le\frac1N+\log\frac LN
\]
gives \(L\ge Ne^{1-1/N}\), hence \(D\) is bounded below by an absolute constant. When \(D=o(N)\), the expansion
\[
H_n=\log n+\gamma+\frac1{2n}+O(n^{-2})
\]
gives
\[
eN\delta=D+b+O\!\left(\frac{(|D|+1)^2}{N}\right).
\]
When \(D<0\), the already established absolute lower bound makes the error \(O(1/N)\), and \(\delta\ge0\) yields \(D\ge-b-O(1/N)\). When \(D\ge0\), no lower estimate is needed. Consequently \(D+1\) is bounded below by a positive constant for large \(N\), and \(|D|+1\ll D+1\). We may therefore use the form
\[
eN\delta=D+b+O\!\left(\frac{(D+1)^2}{N}\right). \tag{9}
\]
In particular, for \(D=o(N/\log N)\) or \(D=O(N/\log N)\), one has \(\delta=O((D+1)/N)\).

## 2. A bounded-cofactor prime lemma

**Lemma.** Fix positive \(\varepsilon,T\). For sufficiently large \(N\), if a prime \(p>\varepsilon N\) divides some element of \(A\cap[N,TN]\), then \(p\) divides some element of \(A\cap(TN,\infty)\).

**Proof.** Suppose there is no such latter element. Write the selected multiples of \(p\) as \(mp\), with \(m\) belonging to a nonempty subset \(J\subseteq\{1,\ldots,K\}\), where \(K=\lfloor T/\varepsilon\rfloor+1\) is fixed. Their reciprocal sum is
\[
\frac1p\sum_{m\in J}\frac1m=\frac{u}{pv}.
\]
We may take \(v=\operatorname{lcm}(1,\ldots,K)\) and \(1\le u\le vH_K\). For sufficiently large \(N\), \(p>\max(v,vH_K)\), so the sum has \(p\)-adic valuation \(-1\). The reciprocals of all other elements of \(A\), and the integer 1, have denominators coprime to \(p\). This contradicts the equality of their difference with \(u/(pv)\). \(\square\)

This is an elementary form of a classical prime-divisor obstruction, not a newly introduced mechanism. Croot and Martin use quantitatively stronger versions when the maximum denominator is near \(N\); see the literature audit.

## 3. Proof of Theorem 1

Fix \(0<\varepsilon<1\), \(0<\eta<e-2\), and \(T>e+1\). All three parameters stay fixed until after the limit in \(N\).

For every prime
\[
\varepsilon N<p\le(e-\eta)N,
\]
choose \(n_p=p\lceil N/p\rceil\). If \(p\le N\), then \(n_p< N+p\le2N\); if \(p>N\), then \(n_p=p\le(e-\eta)N\). Hence \(n_p\in I\), a positive proportion of \(N\) below \(L\), for sufficiently large \(N\).

If \(n_p\notin A\), its contribution to (8) is at least \(c_\eta/N\), for some \(c_\eta>0\). Also, distinct primes greater than \(\varepsilon N\) cannot divide the same \(n_p\le L\), since \(\varepsilon^2N^2>L\) eventually. Equations (8)–(9) therefore show that the number of these exceptional primes is \(O_\eta(D+1)\).

For every other prime in the displayed interval, the lemma forces a multiple in \(A\cap(TN,\infty)\). Thus
\[
\log\prod_{\substack{a\in A\\a>TN}}a
\ge \vartheta((e-\eta)N)-\vartheta(\varepsilon N)
      -O_\eta((D+1)\log N), \tag{10}
\]
where \(\vartheta(x)=\sum_{p\le x}\log p\).

By (8), every denominator above \(TN\) costs at least \(1/L-1/(TN)\gg_T1/N\). There are \(O_T(D+1)\) such denominators. Those at most \(N^2\) contribute altogether \(O_T((D+1)\log N)=o(N)\) to the logarithm in (10). The prime number theorem now gives
\[
\log\prod_{\substack{a\in A\\a>N^2}}a
\ge(e-\eta-\varepsilon-o(1))N.
\]
First taking the lower limit in \(N\), and then letting \(\varepsilon,\eta\downarrow0\), proves (1).

For \(a>N^2\), the cost in (8) is at least \(1/L-1/N^2\). Therefore
\[
r\le\frac{\delta}{1/L-1/N^2}
=D+b+O\!\left(\frac{(D+1)^2}{N}\right), \tag{11}
\]
which proves (3). Since \(r\ge1\), this also implies \(D+b\ge1-o(1)\) along bounded-\(D\) subsequences. In general the error in (11) is \(o(D+b)\): for unbounded positive \(D\), its relative size is \(O(D/N)\); for bounded \(D\), use the preceding lower bound.

Finally,
\[
r\log M\ge\log\prod_{a>N^2}a\ge(e-o(1))N.
\]
Divide using \(r\le(D+b)(1+o(1))\). This proves (2) without multiplying an uncontrolled additive error by \(\log M\).

For Corollary 1.1, (11) and integrality give \(r\le q\) eventually. Equation (1) gives (4). As a further elementary consequence, the unrestricted minimum satisfies
\[
\liminf_{N\to\infty}\bigl(k(N)-(e-1)N\bigr)\ge\frac{3-e}{2}.
\]
This is only a constant lower bound.

For Corollary 1.2, a sequence violating (5) by a fixed positive proportion would have \(D=O(N/\log F)=o(N/\log N)\). Applying (2) and \(\log M\le\log F\) contradicts that violation. Here the constant \(b\) is negligible because \(N/\log F\to\infty\).

## 4. A component bound for the number of supported primes

Fix \(\varepsilon,T>0\), with \(T>e+1\), and suppose \(M\le N^{B+\xi_N}\), where \(B>1\) is fixed and \(\xi_N\to0\). Consider all selected denominators above \(TN\). Form a hypergraph: its vertices are their prime divisors greater than \(\varepsilon N\), and each denominator with at least one such divisor contributes an edge consisting of those distinct prime divisors. Different denominators may give the same edge; keep them as distinct edges. Each edge has at most a fixed number \(J=J(B)\) of vertices for sufficiently large \(N\).

Take one connected component with \(q\) prime vertices and \(r\ge1\) edges, represented by denominators \(a_1,\ldots,a_r\). Write \(j_i\) for the number of distinct large prime factors of \(a_i\), and let \(b_i\) be the integer obtained from \(a_i\) by removing *all* prime-power factors whose primes exceed \(\varepsilon N\). Then
\[
b_i\le\frac{a_i}{(\varepsilon N)^{j_i}}. \tag{12a}
\]

Add the reciprocals of the component's tail denominators and of every selected denominator at most \(TN\) divisible by one of its primes. Call this positive sum \(S_0\). Every complementary selected denominator is coprime to all component primes. Since the entire sum is 1, the reduced denominator of \(S_0\) is also coprime to every component prime.

For large \(N\), a selected denominator at most \(TN\) contains at most one prime greater than \(\varepsilon N\), to the first power. It has form \(mp\), with \(m\le T/\varepsilon\). Set
\[
L_0=\operatorname{lcm}(1,\ldots,\lceil T/\varepsilon\rceil).
\]
After the component primes cancel, the reduced denominator of \(S_0\) therefore divides \(L_0\prod_i b_i\). Positivity implies
\[
S_0\ge\frac1{L_0\prod_i b_i}. \tag{12b}
\]

Each prime has at most \(\lceil T/\varepsilon\rceil\) incident low denominators. Their reciprocals are at most \(1/N\), while each tail reciprocal is less than \(1/(TN)\). As \(q\le Jr\),
\[
S_0\le C_{\varepsilon,T,B}\frac rN. \tag{12c}
\]
This upper bound is used quantitatively; no assumption that a component has bounded size is made.

The bipartite incidence graph of a connected component has \(q+r\) vertices, so
\[
\sum_i j_i\ge q+r-1.
\]
Combining this fact with (12a)–(12c), and using \(\log a_i\le(B+\xi_N)\log N\), gives
\[
\begin{aligned}
\log N-\log(C_{\varepsilon,T,B}L_0r)
&\le\sum_i\log b_i\\
&\le\bigl((B+\xi_N)r-q-r+1\bigr)\log N
     +O_{\varepsilon,B}(r).
\end{aligned}
\]
Cancel the \(\log N\) terms and rearrange:
\[
q\le(B-1+\xi_N)r
  +\frac{\log(C_{\varepsilon,T,B}L_0r)+O_{\varepsilon,B}(r)}{\log N}.
\tag{12d}
\]

Sum over components. Since their number is at most the total number of nonempty edges, and \(\log r\le r\) for \(r\ge1\), all errors sum to \(O_{\varepsilon,T,B}(r_T/\log N)\), where \(r_T=|A\cap(TN,\infty)|\). Empty edges can only increase \(r_T\). Thus the total number of prime vertices satisfies
\[
q_{\rm total}\le(B-1+o(1))r_T. \tag{12e}
\]
This is the required improvement over counting prime factors in each denominator separately. Removing all large prime *powers* in (12a) ensures that repeated factors cause no problem.

## 5. Proof of Theorem 2

It suffices to work along sequences with \(D=O(N/\log N)\): any sequence violating (6) has this property, by the absolute lower bound for \(D\). In this range, \(L/N\to e\), and (9) gives
\[
N\delta=\frac D e+o(N/\log N). \tag{12}
\]

Fix \(0<\varepsilon<1\) and \(T>e+1\). For primes \(\varepsilon N<p\le L\), define
\[
W_N(p)=\sum_{\substack{m\ge1\\N\le mp\le L}}
                  \left(\frac1{mp}-\frac1L\right).
\]
Partition these primes into two classes: \(U\) consists of those with no multiple in \(A\cap I\), and \(V\) consists of the others.

Every core multiple of a prime in \(U\) is a hole. Core multiples corresponding to distinct such primes are disjoint for sufficiently large \(N\), because the product of the primes exceeds \(L\). Their total cost in (8) is consequently at least \(\sum_{p\in U}W_N(p)\).

Every prime in \(V\) divides a denominator above \(TN\), by the lemma. Put \(h=B-1\). The component bound (12e) gives \(|V|\le(h+o(1))r_T\), where \(r_T=|A\cap(TN,\infty)|\). Write \(h_N=h+o(1)>0\) for a valid upper-bound coefficient. The tail's harmonic cost is at least \(r_T(1/L-1/(TN))\). Combining the two disjoint parts of (8),
\[
\begin{aligned}
\delta
&\ge\sum_{p\in U}W_N(p)
       +\frac{|V|}{h_N}\left(\frac1L-\frac1{TN}\right)\\
&\ge\sum_{\varepsilon N<p\le L}
 \min\left\{W_N(p),\frac1{h_N}\left(\frac1L-\frac1{TN}\right)\right\}.
\end{aligned} \tag{13}
\]
No prime is being assigned a distinct tail denominator: the component bound explicitly accounts for shared denominators.

Define, for \(0<x\le e\),
\[
w(x)=\sum_{\substack{m\ge1\\1\le mx\le e}}
                  \left(\frac1{mx}-\frac1e\right). \tag{14}
\]
On any fixed interval \([\varepsilon,e]\), this function has finitely many pieces and is bounded and Riemann integrable. Away from finitely many endpoints, \(NW_N(p)\) tends uniformly to \(w(p/N)\); moving endpoints arising from \(L/N-e=o(1)\) contribute \(o(N/\log N)\) to the relevant prime sums. This last statement follows by enclosing the finitely many endpoints in fixed intervals of total length at most an arbitrary \(\rho>0\), using the prime number theorem there, then letting \(\rho\downarrow0\).

The prime number theorem and (13) therefore give
\[
\liminf\frac{D\log N}{N}
\ge e\int_\varepsilon^e
 \min\left\{w(x),\frac1h\left(\frac1e-\frac1T\right)\right\}\,dx.
\]
Let \(T\to\infty\), then \(\varepsilon\downarrow0\). The integrand is bounded by \(1/(eh)\), so these limits are valid even though \(w(x)\) itself grows near zero. This proves (6) with
\[
\mathcal C(h)=e\int_0^e\min\left\{w(x),\frac1{eh}\right\}\,dx. \tag{15}
\]

## 6. Proof of Theorem 3

Again reduce to \(D=O(N/\log N)\) and fix \(\varepsilon,T\). First assume \(M\le N^{B+o(1)}\), \(1<B<2\), and let \(s=\lceil1/(B-1)\rceil\). Every denominator contains at most one prime greater than \(\varepsilon N\), and that prime occurs to the first power, for sufficiently large \(N\).

For a prime \(p\in V\), write the sum of all selected low multiples of \(p\) as \(U/(pV_0)\), where \(U,V_0\) are positive integers bounded uniformly in terms of \(\varepsilon,T\). Write all its tail multiples as \(px_1,\ldots,px_r\). If \(r\le s-1\), then
\[
x_i\le\frac M{\varepsilon N}\le N^{B-1+o(1)}.
\]
The numerator after combining these terms is the positive integer
\[
Z=U\prod_{i=1}^r x_i
 +V_0\sum_{i=1}^r\prod_{j\ne i}x_j.
\]
The denominator is \(pV_0\prod x_i\), with every factor other than \(p\) coprime to \(p\). The total reciprocal sum being 1 therefore requires \(p\mid Z\). But
\[
0<Z\le N^{r(B-1)+o(1)}=o(N)<p,
\]
since \((s-1)(B-1)<1\). For \(r=0\), interpret \(Z=U\); the same contradiction applies. Thus each prime in \(V\) has at least \(s\) tail multiples. Distinct such primes cannot share a denominator, so \(r_T\ge s|V|\).

Use this stronger count in (13). The prime sum now has limiting integrand \(\min\{w(x),s(1/e-1/T)\}\). The same limit argument proves (7a).

For (7b), the assumption also implies \(M=o(N^2)\), so the same disjointness and prime-power observations apply. For \(r\le s-1\),
\[
\left(\frac M{\varepsilon N}\right)^r=o(N).
\]
Consequently \(Z=o(N)\) again, including the case \(r=s-1\).

Finally, integral comparison in (14) gives
\[
w(x)=\frac1{ex}+O(1)\qquad(x\downarrow0).
\]
Since taking a minimum with a fixed constant is a Lipschitz operation, comparison of the integrands with \(\min(1/x,s)\) on \((0,e)\) gives
\[
d_s=\int_0^e\min(1/x,s)\,dx+O(1)=\log s+O(1).
\]

## 7. Evaluation of the constants

First, \(w(x)\ge1/e\) for \(0<x\le1/2\). To see this, \(w\) decreases on each interval \((1/(m+1),1/m)\): when a term disappears at \(x=e/j\), its value is zero. Its infimum there is the limit at \(1/m\) from below. For \(m=2\), this limit is
\[
2\left(\frac13+\frac14+\frac15\right)-\frac3e
=\frac{47}{30}-\frac3e>\frac1e.
\]
For \(m\ge3\), comparison with an integral gives the lower bound
\[
g(m):=\int_{m+1}^{em}\left(\frac m u-\frac1e\right)\,du
=\frac{m+1}{e}-m\log\left(1+\frac1m\right).
\]
The function \(g(y)\) is increasing for \(y\ge3\), since
\[
g'(y)=\frac1e-\log(1+1/y)+\frac1{y+1}
>\frac1e-\frac1{y(y+1)}>0.
\]
Also \(g(3)>1/e\), because \(e\log(4/3)<1\). Values at the jump points themselves are larger, so the stated bound follows.

On \([1/2,1)\), \(w\) is decreasing. Its limit at 1 from below is \(1/2-1/e\), which exceeds \(1/(3e)\), since \(e>8/3\). The relevant crossings are:

- \(w(x)=1/e\) at \(x=5e/18\); between this point and \(e/3\), \(w(x)=5/(6x)-2/e\).
- \(w(x)=1/(2e)\) at \(x=e/3\); between \(e/3\) and 1, \(w(x)=1/(2x)-1/e\).
- For \(t\ge3\), there is no crossing below 1.

On \([1,e]\), the crossing with \(1/(et)\) occurs at \(x=et/(t+1)\). Below it the minimum in (15) is \(1/(et)\); above it \(w(x)=1/x-1/e\). Thus
\[
e\int_1^e\min\{w(x),1/(et)\}\,dx
=e\log(1+1/t)-\frac1t. \tag{16}
\]
For \(t\ge3\), the interval \((0,1)\) contributes exactly \(1/t\). The same crossing and saturation calculation holds for every real \(h\ge3\), giving \(\mathcal C(h)=e\log(1+1/h)\) and hence the asserted formula for every real \(B\ge4\). For \(t=1,2\), integrating the two explicitly displayed formulas below 1 gives (7). The decimal values are only illustrations; the exact formulas and their proof establish the bounds.

For the headline subquadratic constant, exact integration gives
\[
\boxed{
d_2=e\left[
\frac{19}{20}\log\frac{20}{19}
+\frac{77}{60}\log3
+\frac{13}{12}\log\frac{15}{13}
+\frac73\log\frac43+\log2
\right]-\frac{11}{2}.
}
\]
The regions where \(w(x)<2/e\), apart from endpoints, are
\[
\left(\frac{19e}{120},\frac12\right),\qquad
\left(\frac{13e}{60},1\right),\qquad
\left(\frac{3e}{8},e\right).
\]
Split the first at \(e/6\), the second at \(e/4,e/3\), and the third at \(e/2\). The seven formulas for \(w(x)=A/x-n/e\) have respective pairs
\[
(A,n)=
(19/20,4),(47/60,3),(13/12,3),(5/6,2),
(1/2,1),(3/2,2),(1,1).
\]
Integrating these pieces gives the boxed expression. To verify that no interval near zero is omitted, \(w(x)>2/e\) for \(x\le1/3\): at the left limit of \(1/3\), use \(3\sum_{j=4}^8 1/j=743/280\) and \(e>8/3\); for the subsequent left limits use \(g(m)\ge g(4)>2/e\). This last inequality follows from \(\log(5/4)<1/4\) and \(e<3\). Monotonicity between jumps then supplies exactly the listed crossings. The [independent subquadratic audit](subquadratic_review.md) records the same calculation in detail.

## 8. What has and has not been achieved

Theorems 2 and 3 give quantitative obstructions for polynomial and subquadratic ceilings; Theorem 1 describes the arithmetic mass that must occur beyond every polynomial scale when the excess is bounded. These are rigorous restricted statements, independently checked as recorded in the review files. The expression “every polynomial scale” also follows directly from (10): for any fixed power \(N^A\), the discarded logarithmic mass is still \(O_A((D+1)\log N)=o(N)\).

They do not establish that the unrestricted excess diverges. If a bounded number of denominators are exponential in \(N\), their prime-factor capacity is itself of order \(N/\log N\), so the polynomial-cap argument loses its growing lower bound. The previous local note also gives a compatible upper bound \(\log M=O_C(N)\) under bounded excess.

The [tail investigation](tail_investigation.md) explains why imposing the simultaneous prime congruences alone does not repair this gap: a classical Chinese remainder construction can cancel a prescribed set of primes with one positive unit fraction. That construction does not complete a representation of 1, but it prevents treating these congruences alone as a contradiction.

The primary-source audit found classical antecedents of the prime-divisibility argument. The exact formulations and constants above were not located in the inspected sources. However, two directly relevant historical articles were not accessible in full, and absence from the sources inspected is not proof of novelty. No submission, external posting, or claim to have solved problem 295 is warranted by this note.

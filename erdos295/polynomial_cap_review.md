# Independent audit: a polynomial denominator cap

Internal mathematical review, 4 September 2026. The theorem and the proposed constants are correct. The proof below includes the limiting details and verifies the closed forms independently. This document does not establish novelty.

## Statement verified

Fix \(B>1\), and put \(t=\lfloor B\rfloor\). Suppose that \(A\) is a finite set of distinct integers such that
\[
N\le a\le N^B\quad(a\in A),
\qquad \sum_{a\in A}\frac1a=1.
\]
Write \(D=|A|-(e-1)N\). Then, uniformly over these representations,
\[
\boxed{D\ge(c_t-o(1))\frac N{\log N},} \tag{1}
\]
where
\[
c_t=e\int_0^e\min\left\{w(x),\frac1{et}\right\}\,dx,
\qquad
w(x)=\sum_{\substack{m\ge1\\1\le mx\le e}}
\left(\frac1{mx}-\frac1e\right).
\tag{2}
\]
The integral is an improper integral at zero; its integrand is bounded and nonnegative, so this poses no convergence problem.

The closed forms are
\[
\begin{aligned}
c_1&=e\log2-2+\frac{5e}{6}\log\frac65
       +\frac e2\log3
       =1.790339441409\ldots,\\
c_2&=e\log\frac32-\frac32+\frac e2\log3
       =1.095337345849\ldots,\\
c_t&=e\log\left(1+\frac1t\right)\qquad(t\ge3).
\end{aligned} \tag{3}
\]

## Harmonic budget and reduction

It is enough to consider \(D=O(N/\log N)\). Indeed, a sequence violating (1) by any fixed positive amount satisfies this upper bound. The elementary harmonic lower bound \(D\ge-O(1)\) makes it an absolute bound as well. Sequences with \(D\log N/N\) tending to infinity already satisfy the conclusion.

Put
\[
L=N+|A|-1=eN+D-1,
\quad I=[N,L]\cap\mathbb Z,
\quad H=I\setminus A,
\quad E=A\setminus I,
\quad
\delta=\sum_{j=N}^{L}\frac1j-1.
\]
Ordering the elements of \(A\) gives \(\delta\ge0\); moreover \(|H|=|E|\), so
\[
\delta=
\sum_{h\in H}\left(\frac1h-\frac1L\right)
+\sum_{a\in E}\left(\frac1L-\frac1a\right). \tag{4}
\]
Every summand is nonnegative. The harmonic expansion, with \(b=(e-1)/2\), gives
\[
eN\delta=D+b+O\!\left(\frac{(D+1)^2}{N}\right)
          =D+o\!\left(\frac N{\log N}\right). \tag{5}
\]
Also \(\lambda:=L/N=e+O(1/\log N)\).

## Exact prime charging inequality

Fix \(0<\varepsilon<1\) and \(T>e\), taking \(N\) sufficiently large that \(L<TN\). Let
\[
\mathcal P=\{p\text{ prime}:\varepsilon N<p\le L\},
\qquad
W_N(p)=\sum_{\substack{m\ge1\\N\le mp\le L}}
\left(\frac1{mp}-\frac1L\right),
\qquad
\alpha_N=\frac1L-\frac1{TN}>0.
\]
Partition \(\mathcal P\) into \(\mathcal O\), the primes for which no multiple in \(I\) belongs to \(A\), and \(\mathcal C=\mathcal P\setminus\mathcal O\).

If \(p\in\mathcal O\), all multiples of \(p\) in \(I\) are holes and incur the full charge \(W_N(p)\). These sets of holes are disjoint for different primes in \(\mathcal P\): a common hole would be at least \(pq>\varepsilon^2N^2>L\). Therefore
\[
\sum_{h\in H}\left(\frac1h-\frac1L\right)
\ge\sum_{p\in\mathcal O}W_N(p). \tag{6}
\]

If \(p\in\mathcal C\), then some member of \(A\) above \(TN\) is divisible by \(p\). Here is the arithmetic justification. All selected multiples of \(p\) at most \(TN\) have the form \(mp\), with \(m\le K=\lfloor T/\varepsilon\rfloor\); this family is nonempty. Their reciprocal sum is \(s/p\), where \(s\) is a positive rational number whose numerator and denominator are bounded in terms of \(K\) alone. For large \(N\), the reduced denominator of \(s/p\) is divisible by \(p\). If all remaining selected denominators were coprime to \(p\), their reciprocal sum would have denominator coprime to \(p\), contradicting the total sum one.

Let \(r=|A\cap(TN,\infty)|\). A denominator \(a\le N^B\) contains at most \(t\) distinct primes exceeding \(\varepsilon N\), since
\[
(\varepsilon N)^{t+1}>N^B
\]
for all sufficiently large \(N\), by \(t+1>B\). Thus
\[
|\mathcal C|\le tr. \tag{7}
\]
Every selected denominator above \(TN\) belongs to \(E\) and costs at least \(\alpha_N\) in (4). Combining (4), (6), and (7),
\[
\begin{aligned}
\delta
&\ge\sum_{p\in\mathcal O}W_N(p)+r\alpha_N\\
&\ge\sum_{p\in\mathcal O}W_N(p)
  +|\mathcal C|\frac{\alpha_N}{t}\\
&\ge\boxed{\sum_{\varepsilon N<p\le L}
        \min\left\{W_N(p),\frac{\alpha_N}{t}\right\}.}
\end{aligned} \tag{8}
\]
This step is valid even if a tail denominator contains an omitted prime as well as a covered prime. No allocation of separate denominators to separate primes is assumed. The only capacity bound is (7).

## Passage to the integral

Define
\[
w_\lambda(x)=\sum_{\substack{m\ge1\\1\le mx\le\lambda}}
\left(\frac1{mx}-\frac1\lambda\right).
\]
For \(p/N=x\),
\[
W_N(p)=N^{-1}w_\lambda(x),
\qquad
\alpha_N=N^{-1}(1/\lambda-1/T).
\]
On a fixed interval \([\varepsilon,e+1]\), there are only finitely many potentially contributing \(m\). More explicitly,
\[
w_\lambda(x)=\sum_m
\mathbf 1_{x\ge1/m}
\left(\frac1{mx}-\frac1\lambda\right)_+,
\]
where the sum may be truncated uniformly in \(N\). This expression proves uniform convergence \(w_\lambda\to w_e\) on that interval: the lower cutoffs \(1/m\) are fixed, and the positive-part function is Lipschitz. The moving upper cutoffs cause no discontinuity because their terms vanish at the cutoff.

The limiting function
\[
f_{\varepsilon,T}(x)=
\min\left\{w(x),\frac{1/e-1/T}{t}\right\}
\]
is bounded and Riemann integrable on \([\varepsilon,e+1]\), with finitely many jumps. It vanishes for \(x>e\). The prime number theorem and approximation by step functions give
\[
\sum_{\varepsilon N<p\le(e+1)N}f_{\varepsilon,T}(p/N)
=\frac N{\log N}\left(
\int_\varepsilon^e f_{\varepsilon,T}(x)\,dx+o(1)\right).
\]
Uniform convergence permits the same assertion with the \(N\)-dependent function in (8). Consequently, (5) and (8) imply
\[
\liminf\frac{D\log N}{N}
\ge e\int_\varepsilon^e
\min\left\{w(x),\frac{1/e-1/T}{t}\right\}\,dx.
\]
First let \(T\to\infty\), and then \(\varepsilon\downarrow0\). Bounded or monotone convergence proves (1)--(2). The arithmetic numerator bound is needed only for fixed \(\varepsilon,T\) before the limit in \(N\), so its dependence on these parameters is harmless.

## Independent verification of the closed forms

### The interval \(0<x\le1/2\)

On each interval \((1/(m+1),1/m)\), \(w\) decreases with \(x\). Breaks at \(e/j\) are continuous because the disappearing summand is zero there. At \(1/m\), the summand with index \(m\) enters with positive size \(1-1/e\), so the value at the endpoint exceeds the left limit. It suffices to bound those left limits:
\[
w(1/m^-)=\sum_{j=m+1}^{\lfloor em\rfloor}
\left(\frac m j-\frac1e\right).
\]
For \(m=2\), the value is \(47/30-3/e>1/e\). For \(m\ge3\), comparison with the integral of the positive decreasing function \(m/y-1/e\) gives
\[
w(1/m^-)\ge\int_{m+1}^{em}
\left(\frac m y-\frac1e\right)dy
=g(m):=\frac{m+1}{e}-m\log(1+1/m).
\]
The derivative satisfies
\[
g'(m)=\frac1e-\log(1+1/m)+\frac1{m+1}
\ge\frac1e-\frac1{m(m+1)}>0\quad(m\ge3).
\]
Furthermore,
\(g(3)>1/e\) follows from \(e\log(4/3)<1\), itself a consequence of \(\log(4/3)<1/3\) and \(e<3\). Hence
\[
w(x)>1/e\qquad(0<x\le1/2). \tag{9}
\]

### The interval \(1/2\le x<1\)

Here \(w\) is decreasing and continuous, apart from the already handled lower endpoint jump. Its limiting value at one is
\[
w(1^-)=\frac12-\frac1e>\frac1{3e},
\]
using \(e>8/3\). Consequently no cap \(1/(et)\), \(t\ge3\), is crossed here.

The level \(1/e\) is crossed at \(a_1=5e/18\), lying in \((e/4,e/3)\), where
\(w(x)=5/(6x)-2/e\). The level \(1/(2e)\) is crossed at \(a_2=e/3\), the transition to
\(w(x)=1/(2x)-1/e\).

### The interval \(1\le x\le e\)

The function decreases, and its crossing of \(1/(et)\) occurs at
\[
\alpha_t=\frac{et}{t+1}\ge e/2.
\]
For \(x\ge e/2\), \(w(x)=1/x-1/e\). If there were no interval below one where \(w\) falls below the cap, the integral in (2) would equal
\[
e\left[\frac{\alpha_t}{et}
  +\int_{\alpha_t}^{e}\left(\frac1x-\frac1e\right)dx\right]
=e\log(1+1/t). \tag{10}
\]
This applies directly for \(t\ge3\).

For \(t=2\), subtract from (10) the deficit
\[
e\int_{e/3}^{1}
\left(\frac{3}{2e}-\frac1{2x}\right)dx
=\frac32-\frac e2\log3.
\]
For \(t=1\), the deficit is
\[
\begin{aligned}
&e\int_{5e/18}^{e/3}
\left(\frac3e-\frac5{6x}\right)dx
+e\int_{e/3}^{1}
\left(\frac2e-\frac1{2x}\right)dx\\
&\hspace{2em}=2-\frac{5e}{6}\log\frac65-\frac e2\log3.
\end{aligned}
\]
These calculations prove all formulas in (3). Numerical evaluation was used only to check the displayed decimal values, not to justify any inequality or integral identity.

## Scope, possible sharpening, and novelty

This result establishes an explicit positive lower bound of order \(N/\log N\) for each fixed polynomial denominator cap. It is stronger in order than a bounded-excess obstruction under that cap. It still imposes a restriction absent from Erdős problem 295, and therefore does not settle the original question.

The proof uses only the capacity bound of \(t\) large primes per selected denominator. When \(B=t\) is an integer, additional restrictions hold: for example, \(t\) primes all exceeding \(N\) cannot share a denominator at most \(N^t\). Thus the constants are proved lower bounds, with no claim of optimality. Exploiting those extra packing constraints could strengthen the integer-cap cases.

No literature search was conducted in this independent arithmetic audit. Priority and submission suitability require the separate primary-literature review. The result should not be advertised as new solely because the present proof and constants are valid.

## Addendum: the stronger bound at integer exponents

The proposed component argument is valid and improves the exponent parameter. In fact, for every fixed \(K>0\) and \(B>1\), the hypothesis
\[
N\le a\le K N^B\quad(a\in A)
\]
implies
\[
\boxed{
D\ge\bigl(c_{\lceil B\rceil-1}-o(1)\bigr)\frac N{\log N}.
} \tag{11}
\]
Thus the coefficient is \(c_1\) throughout \(1<B\le2\), \(c_2\) throughout \(2<B\le3\), and so on. The constants \(c_t\) are exactly those in (3). Multiplication of the denominator cap by fixed \(K\) does not change the coefficient.

For noninteger \(B\), the existing capacity proof applies with \(t=\lfloor B\rfloor=\lceil B\rceil-1\), because \((\varepsilon N)^{t+1}>KN^B\) eventually. The improvement concerns integer \(B=m\ge2\), for which the effective capacity is \(m-1\) even though individual tail denominators may contain \(m\) large primes.

### The component lemma

Fix \(m\ge2\), \(K>0\), \(\varepsilon>0\), and \(T>0\). Consider representations satisfying
\[
\sum_{a\in A}\frac1a=1,
\qquad N\le a\le KN^m,
\qquad |A|=O(N).
\]
For each selected denominator \(a>TN\), form an edge consisting of all distinct primes \(p>\varepsilon N\) dividing \(a\); omit empty edges. Vertices are the primes appearing in at least one such edge. Denominators with identical supports are retained as separate edges, which is harmless for the following counting argument.

For sufficiently large \(N\), every edge has at most \(m\) vertices, since \((\varepsilon N)^{m+1}>KN^m\). We claim that every connected component of this hypergraph contains an edge with at most \(m-1\) vertices.

Suppose instead that some component \(\mathcal V\) has only edges of size \(m\). Every tail denominator incident to it has the form
\[
a=d\prod_{p\in F}p,
\qquad F\subseteq\mathcal V,
\quad |F|=m,
\quad 1\le d\le K\varepsilon^{-m}.
\tag{12}
\]
In particular, each vertex \(p\in\mathcal V\) satisfies
\[
p\le K\varepsilon^{-(m-1)}N=:C_0N.
\tag{13}
\]
For large \(N\), none of these large primes can divide \(d\), whose bound is fixed. Thus repeated factors of a large prime are also excluded in a full-size edge. Any edge with a repeated large-prime factor would already have fewer than \(m\) distinct large primes for large \(N\), and would be a permissible root edge.

Let \(S_{\mathcal V}\) be the reciprocal sum of **all** selected denominators divisible by at least one vertex in \(\mathcal V\). This includes every tail denominator belonging to the component and every selected denominator at most \(TN\) incident to one of its vertices. Every other selected denominator is coprime to every vertex of \(\mathcal V\).

A selected denominator at most \(TN\) incident to \(p\in\mathcal V\) has the form \(dp\), with \(d\le T/\varepsilon\). Such a denominator cannot contain two primes exceeding \(\varepsilon N\) for large \(N\), since their product would exceed \(TN\). Together with (12), this shows that all denominators contributing to \(S_{\mathcal V}\) divide
\[
Q_0\prod_{p\in\mathcal V}p,
\qquad
Q_0=\operatorname{lcm}(1,\ldots,H),
\qquad
H=\left\lceil\max\{1,K\varepsilon^{-m},T/\varepsilon\}\right\rceil.
\tag{14}
\]
Here \(Q_0\) is independent of \(N\) and of the component. Take \(N\) large enough that \(\varepsilon N>H\), so \(Q_0\) is coprime to all component vertices.

Because
\[
S_{\mathcal V}=1-
\sum_{\substack{a\in A\\p\nmid a\ \text{for every }p\in\mathcal V}}\frac1a,
\]
the reduced denominator of \(S_{\mathcal V}\) is coprime to every vertex of \(\mathcal V\). Combining this with (14), its reduced denominator divides \(Q_0\). The component has an edge, so \(S_{\mathcal V}>0\), and therefore
\[
S_{\mathcal V}\ge\frac1{Q_0}. \tag{15}
\]
This cancellation statement uses the entire incident sum. Applying it only to the component's tail denominators, while omitting its incident low denominators, would be unjustified.

On the other hand, (13) bounds the number of component vertices by \(\pi(C_0N)=O(N/\log N)\). For each vertex, at most \(\lfloor T/\varepsilon\rfloor\) selected low denominators can be incident to it, and each reciprocal is at most \(1/N\). Their total is \(O(1/\log N)\). Every tail denominator in the component is at least \((\varepsilon N)^m\), and there are at most \(|A|=O(N)\) of them. Consequently,
\[
S_{\mathcal V}
\le O\!\left(\frac1{\log N}\right)+O(N^{1-m})
\longrightarrow0. \tag{16}
\]
All implied constants depend only on the fixed parameters and the bound in \(|A|=O(N)\), not on the component. Equations (15)--(16) contradict one another for large \(N\). This proves the claim uniformly over all components.

### Counting vertices from a root edge

In each component, choose an edge of size at most \(m-1\) as a root. Because the component is connected, its remaining edges can be ordered so that each intersects the union of its predecessors. The root introduces at most \(m-1\) vertices, and every later edge introduces at most \(m-1\) new vertices, since it has size at most \(m\) and already shares at least one vertex.

Thus, if \(r_T\) is the total number of selected denominators above \(TN\),
\[
\#\{p>\varepsilon N:p\mid a\text{ for some }a\in A,\ a>TN\}
\le(m-1)r_T. \tag{17}
\]
Empty edges only increase the right side when included in \(r_T\). Repeated edges also cause no difficulty.

Every covered core prime from the proof of (8) is a vertex counted on the left of (17), by the same bounded-cofactor divisibility argument. Replacing (7) with (17) proves the exact charging inequality (8) with \(t=m-1\). The remainder of the integral proof is unchanged. The reduction \(D=O(N/\log N)\) guarantees \(|A|=O(N)\), as required by the component lemma. This completes the proof of (11).

### Audit verdict and limits

No gap was found in the support, cancellation, uniform smallness, or hypergraph counting steps. The order of limits remains essential: \(\varepsilon,T\), and hence the potentially very large integer \(Q_0\), are fixed before \(N\to\infty\). An explicit practical threshold is not provided, and is not required for the asymptotic statement.

This addendum supplies a structural refinement beyond the original per-denominator capacity count. It still requires a fixed polynomial bound on the largest denominator. It does not exclude the unrestricted exponential-denominator regime allowed in Erdős problem 295. Validity of the refinement does not establish its novelty, and this audit makes no priority claim.

## Further verified extension: a slowly growing cap factor

The component argument also proves the stronger assertion
\[
\boxed{
M=o(N^m\log\log N),\quad m\ge2\text{ fixed}
\quad\Longrightarrow\quad
D\ge\bigl(c_{m-1}-o(1)\bigr)\frac N{\log N}.
} \tag{18}
\]
All asymptotic hypotheses here are along the sequence of representations under consideration. Equivalently, one may impose a specified cap \(M\le N^m f(N)\), with \(f(N)\ge1\) and \(f(N)=o(\log\log N)\). Taking \(f(N)=\max\{1,M/N^m\}\) gives the displayed form.

Here is the additional uniformity check. Fix \(\varepsilon,T\) as before, and again reduce to \(|A|=O(N)\). Every tail edge still has size at most \(m\), since
\((\varepsilon N)^{m+1}>N^m f(N)\) eventually. In a hypothetical component with only edges of size \(m\), the cofactors in (12) now satisfy
\[
d\le f(N)\varepsilon^{-m}.
\]
Set
\[
H_N=\left\lceil\max\{1,f(N)\varepsilon^{-m},T/\varepsilon\}\right\rceil,
\qquad
Q_N=\operatorname{lcm}(1,\ldots,H_N).
\]
For fixed \(\varepsilon,T\), \(H_N=o(\log\log N)\), and hence \(H_N<\varepsilon N\) for large \(N\). This still excludes repeated component-prime factors in full-size edges and makes \(Q_N\) coprime to all component vertices. The same cancellation argument proves that the positive incident sum has reduced denominator dividing \(Q_N\), so
\[
S_{\mathcal V}\ge Q_N^{-1}.
\]
The standard bound
\(\log\operatorname{lcm}(1,\ldots,H)=\psi(H)=O(H)\)
gives
\[
\log Q_N=o(\log\log N),
\qquad
S_{\mathcal V}\ge(\log N)^{-o(1)}. \tag{19}
\]

To obtain an upper bound independent of \(f\), count low terms using only primes at most \(TN\), rather than the largest prime in the component. A selected denominator at most \(TN\) incident to a component vertex contains a prime \(\varepsilon N<p\le TN\), with at most \(\lfloor T/\varepsilon\rfloor\) possible cofactors. Thus there are at most
\[
\lfloor T/\varepsilon\rfloor\pi(TN)=O(N/\log N)
\]
such terms. Their reciprocal sum is \(O(1/\log N)\). Every full-size component tail is still at least \((\varepsilon N)^m\), so its total tail mass is \(O(N^{1-m})\). Hence
\[
S_{\mathcal V}\le O(1/\log N)+O(N^{1-m})
=O(1/\log N), \tag{20}
\]
uniformly over components. Equations (19) and (20) are incompatible: for example, (19) is eventually at least \((\log N)^{-1/2}\).

Therefore every component again has a root edge of size at most \(m-1\), and (17) and the integral argument remain valid. This proves (18). The extension establishes a denominator regime slightly beyond a fixed multiple of \(N^m\); it still leaves unrestricted denominators, and in particular the exponential regime, unresolved.

## Unifying quantitative component bound

The subsequently proposed quantitative component argument is valid and supersedes both preceding cap-factor restrictions. For every fixed real \(B>1\), it proves
\[
\boxed{
M\le N^{B+o(1)}
\quad\Longrightarrow\quad
D\ge\bigl(\mathcal C(B-1)-o(1)\bigr)\frac N{\log N},
} \tag{21}
\]
where, for every real \(h>0\),
\[
\mathcal C(h)=e\int_0^e
\min\left\{w(x),\frac1{eh}\right\}dx.
\tag{22}
\]
In particular, \(\mathcal C(t)=c_t\) for positive integers \(t\). The denominator bound \(N^{m+o(1)}\), with fixed integer \(m\ge2\), gives coefficient \(c_{m-1}\). This includes factors much larger than the \(o(\log\log N)\) factor in (18).

### Capacity lemma with a real exponent

Fix \(0<\varepsilon<1\) and \(T>e\). Write the denominator bound as
\[
a\le N^{B+\rho_N},\qquad \rho_N\ge0,\quad\rho_N\to0.
\]
Choose a fixed integer \(J>B\). For sufficiently large \(N\), every denominator contains at most \(J\) distinct primes greater than \(\varepsilon N\).

Form the same hypergraph from the large-prime supports of selected denominators above \(TN\), ignoring empty edges. Consider a component with \(q\) prime vertices and \(r\ge1\) denominator edges, and let \(j_i\) be the size of its \(i\)-th edge. Then
\[
q\le Jr,
\qquad
q+r-1\le s:=\sum_{i=1}^{r}j_i\le Jr. \tag{23}
\]
The middle inequality follows by considering the connected bipartite incidence graph: it has \(q+r\) vertices and \(s\) graph edges. It remains valid for repeated hyperedges, which correspond to distinct denominator vertices.

For each tail denominator in the component, remove **all powers** of every prime exceeding \(\varepsilon N\), and call the remaining integer \(b_i\). Thus
\[
b_i=\frac{a_i}{\prod_{p>\varepsilon N}p^{v_p(a_i)}},
\qquad
\log b_i\le\log a_i-j_i\log(\varepsilon N). \tag{24}
\]
The inequality uses only one copy of each support prime; repeated large-prime factors strengthen it. There is no bounded-cofactor assumption on \(b_i\).

Let \(S\) be the reciprocal sum of all selected denominators incident to at least one component prime, including those at most \(TN\). Put
\[
K_0=\lceil T/\varepsilon\rceil,
\qquad
L_0=\operatorname{lcm}(1,\ldots,K_0).
\]
For large \(N\), every incident low denominator has the form \(dp\), with \(d\le K_0<\varepsilon N\). Consequently its cofactor divides \(L_0\). Every incident tail denominator is an edge of this component, by the definition of connected components, and all its primes exceeding \(\varepsilon N\) belong to the component.

The complementary selected denominators are coprime to every component prime. Since the total reciprocal sum is one, the reduced denominator of \(S\) is also coprime to every component prime. Before that cancellation, its denominator divides a product of component-prime powers times \(L_0\prod_i b_i\). Therefore after cancellation it divides \(L_0\prod_i b_i\), and positivity gives
\[
S\ge\frac1{L_0\prod_i b_i}. \tag{25}
\]
This argument explicitly removes all large-prime powers. Removing only a single copy of a repeated prime would not identify the remaining small-prime factor correctly, although it would suffice for the upper inequality in (24).

There are at most \(K_0q\) incident low terms, each at most \(1/N\), and \(r\) incident tail terms, each at most \(1/(TN)\). By (23),
\[
S\le\frac{K_0q+r/T}{N}
\le\frac{C_0r}{N},
\qquad C_0=K_0J+1/T. \tag{26}
\]
All constants are independent of the component and the representation. Combining (25)--(26),
\[
\log N-\log(C_0L_0r)
\le\sum_i\log b_i.
\tag{27}
\]
On the other hand, (23)--(24) give
\[
\begin{aligned}
\sum_i\log b_i
&\le r(B+\rho_N)\log N-s\log(\varepsilon N)\\
&\le\bigl((B-1+\rho_N)r-q+1\bigr)\log N
     +Jr|\log\varepsilon|.
\end{aligned} \tag{28}
\]
Combining (27) and (28) cancels the one \(\log N\) contributed by each connected component. The resulting explicit inequality is
\[
\boxed{
q\le(B-1+\rho_N)r
 +\frac{J|\log\varepsilon|r+\log(C_0L_0r)}{\log N}.
} \tag{29}
\]
No assumption \(|A|=O(N)\) is needed for this component inequality. Even if the upper bound in (26) exceeds one, it is still a valid upper bound and (27)--(29) remain valid.

Sum (29) over all nonempty components. If \(R\) is their total number of denominator edges, their number of components is at most \(R\), and
\(\sum_{\text{components}}\log r\le\sum r=R\).
Since \(C_0L_0>1\), it follows that the total number \(Q\) of prime vertices satisfies
\[
Q\le h_N R\le h_N r_T,
\quad
h_N=B-1+\rho_N+
\frac{J|\log\varepsilon|+\log(C_0L_0)+1}{\log N},
\tag{30}
\]
where \(r_T=|A\cap(TN,\infty)|\), including empty-support denominators. Here \(h_N\to B-1>0\). If there are no nonempty components, (30) holds with \(Q=R=0\).

### From capacity to the excess bound

Every covered core prime in the proof of (8) occurs among the vertices counted by \(Q\), by the same bounded-cofactor argument applied below \(TN\). Equation (30) therefore gives
\[
|\mathcal C|\le h_N r_T.
\]
Exactly as in (8),
\[
\delta\ge
\sum_{\varepsilon N<p\le L}
\min\left\{W_N(p),\frac{1/L-1/(TN)}{h_N}\right\}. \tag{31}
\]
To prove (21), again reduce to \(D=O(N/\log N)\), so (5) and \(L/N\to e\) apply. For fixed \(\varepsilon,T\), the cap in the associated Riemann sum converges to
\((1/e-1/T)/(B-1)\). The same uniform convergence and prime number theorem argument used above applies, since \(B-1>0\) is fixed. First take \(N\to\infty\), then \(T\to\infty\), and then \(\varepsilon\downarrow0\). This proves (21)--(22).

The error is uniform for a specified upper exponent error \(\rho_N\to0\). The proof does not require a single uniform rate over all possible unspecified little-o functions.

### Closed forms for real \(h\ge1\)

The integer constants checked earlier are recovered from a useful continuous expression. Define
\[
g=1+1/h,
\qquad h_0=\frac2{e-2}.
\]
Then
\[
\mathcal C(h)=
\begin{cases}
e\log g-g+\dfrac{5e}{6}\log\!\left(\dfrac{4+2/h}{5}\right)
       +\dfrac e2\log3,
   &1\le h\le2,\\[4pt]
e\log g-g+\dfrac e2\log(2g),
   &2\le h\le h_0,\\[4pt]
e\log g,
   &h\ge h_0.
\end{cases} \tag{32}
\]
To verify this, the interval \((0,1/2]\) is always capped for \(h\ge1\), by (9). On \((1/2,1)\), the crossing of \(w(x)=1/(eh)\) is
\[
\frac{5eh}{6(2h+1)}\quad(1\le h\le2),
\qquad
\frac{eh}{2(h+1)}\quad(2\le h\le h_0).
\]
For \(h\ge h_0\), no crossing occurs before one, because
\(1/(eh)\le1/2-1/e\). Integrating the deficit below the cap, just as in the integer calculation, gives (32). The formulas agree at their common endpoints. In particular,
\[
\mathcal C(B-1)=e\log\frac B{B-1}
\qquad\text{when }B\ge1+\frac2{e-2},
\]
so the simpler stated sufficient range \(B\ge4\) is correct. For \(0<h<1\), the integral definition (22) remains valid without requiring a closed form.

### Final mathematical audit of this refinement

No gap was found in the quantitative component argument. The cancellation of the component-prime powers, the bound on the remaining denominator, the incidence-graph inequality, and the summation of the logarithmic component errors are all valid. The proof gives a real-exponent coefficient and supersedes the earlier integer-only refinements.

This remains a theorem under a denominator-growth restriction. Its validity does not demonstrate novelty, and the present document is an independent proof audit rather than a completed literature or publication assessment.

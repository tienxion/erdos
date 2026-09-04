# Investigation of the bounded tail in Erdős problem 295

Date: 4 September 2026.

**Status:** no argument here excludes a bounded number of exponentially large denominators. This is an audit of the remaining obstruction, not a claim of a new theorem suitable for submission. Only this file was edited by the tail investigator.

Let a finite set of distinct integers \(A\subseteq[N,\infty)\) satisfy
\[
\sum_{a\in A}a^{-1}=1,\qquad |A|\leq(e-1)N+C,
\]
where \(C\) is fixed. The existing harmonic-loss argument gives only \(O_C(1)\) denominators beyond \(3N\), and forces the largest denominator to be exponential in \(N\). This investigation asked whether positivity, simultaneous congruences, or fixed tail length forces a contradiction.

## 1. Simultaneous prime cancellation has an exact one-term solution

**Lemma.** Let \(S\) be rational, and let \(\mathcal P\) be a nonempty finite set of primes with
\[
v_p(S)=-1\qquad(p\in\mathcal P).
\]
Put \(P=\prod_{p\in\mathcal P}p\). There is an integer \(P\leq d<P^2\) such that \(v_p(d)=1\) and \(S+1/d\) has reduced denominator coprime to every \(p\in\mathcal P\).

**Proof.** The rational number \(pS\) has denominator coprime to \(p\), and its residue \(c_p=pS\pmod p\) is nonzero. Impose
\[
t\equiv-\bigl((P/p)c_p\bigr)^{-1}\pmod p
\qquad(p\mid P).
\]
The Chinese remainder theorem supplies a unique \(1\leq t<P\) satisfying these congruences, with \(\gcd(t,P)=1\). Set \(d=Pt\). Then
\[
p(S+1/d)=pS+\frac1{(P/p)t}\equiv0\pmod p.
\]
The expression on the left has denominator coprime to \(p\), so its valuation is at least one. Thus \(v_p(S+1/d)\geq0\). The size and valuation assertions follow from the choice of \(t\). \(\square\)

For \(S=\sum_{p\in\mathcal P}1/p\), the conditions become
\[
\frac d p\equiv-1\pmod p\qquad(p\in\mathcal P).
\]
Thus even the positive signs and all simultaneous cancellation congruences can be carried by one denominator of size less than \(P^2\). If \(\log P=\Theta(N)\), this lies in the exponential regime already left open.

The lemma does **not** finish the Egyptian-fraction representation. The factor \(t\) may introduce other denominator factors. If \(S<1\), the lemma alone does not always ensure \(S+1/d\leq1\), although the sufficient condition \(1-S\geq1/P\) ensures it. No bound on the number of terms needed for the remaining residual follows.

## 2. This cancellation mechanism is classical

For a reduced positive fraction \(u/v\) with \(u>1\) and \(v>1\), let \(1\leq t<v\) be the inverse of \(u\pmod v\), and put
\[
w=(ut-1)/v.
\]
Then \(w\) is a positive integer, \(w<u\), and
\[
\frac uv=\frac1{vt}+\frac wt.
\]
One unit fraction with denominator less than \(v^2\) leaves a residual with smaller denominator. For \(u=1\), take \(t=1,w=0\).

This is a basic instance of reverse-greedy Egyptian-fraction methods. David Eppstein describes the method, attributes its basic formulation to K. S. Brown, and discusses the limitations of available length bounds in his own [Reverse Greedy Methods notes](https://ics.uci.edu/~eppstein/numth/egypt/greed.html). The identity and preceding lemma are explanatory observations here; no novelty is claimed.

## 3. Fixed tail length isolates a numerator problem

Write the positive residual after choosing a core \(B\) as
\[
R=1-\sum_{b\in B}\frac1b=\frac uv
\]
in lowest terms.

* One remaining unit fraction exists exactly when \(u=1\); its denominator is \(v\).
* Two remaining positive unit fractions with denominators \(x,y\) exist exactly when positive integers \(s,t\) satisfy
  \[
  st=v^2,\qquad s\equiv t\equiv-v\pmod u,
  \]
  with \(x=(s+v)/u\) and \(y=(t+v)/u\). Distinctness and the required cutoff for \(x,y\) must also be imposed.

The second criterion is the elementary identity
\[
\frac uv=\frac1x+\frac1y
\quad\Longleftrightarrow\quad
(ux-v)(uy-v)=v^2.
\]
Both factors are positive because each unit fraction is strictly smaller than their sum.

Prime support gives information about \(v\). It does not prove \(u\ne1\), or exclude the divisor configuration above, uniformly over the allowed almost consecutive cores. That is a separate global arithmetic issue.

## 4. Elementary rational separation has the compatible exponential scale

For a polynomially bounded core of a bounded-excess representation, the harmonic-loss identity permits \(O_C(\sqrt N)\) changes from its consecutive comparison block. The product of the changed denominators has logarithm \(o(N)\), so the core differs from the block by a rational correction of height \(\exp(o(N))\).

The least common multiple of a block \([N,L]\) with \(L\sim eN\) is exactly \(\operatorname{lcm}(1,\ldots,L)\) for sufficiently large \(N\): every integer below \(N\) has a multiple in \([N,2N]\). The prime number theorem gives logarithm \((e+o(1))N\).

The elementary nonzero separation between rationals of denominators \(D\) and \(s\) is only \(1/(Ds)\). Here this gives the scale
\[
\exp(-(e+o(1))N),
\]
which is compatible with a positive exponential residual. A bound based only on common-denominator size therefore does not replace the missing numerator argument. This comparison of scales is not a counterexample construction.

## 5. A continued-fraction shortcut that must not be used

For an exactly consecutive core with harmonic residual \(o(N^{-2})\), midpoint Euler–Maclaurin gives, for \(P=2L+1,Q=2N-1\),
\[
Q^2(P/Q-e)\longrightarrow\frac{e-e^{-1}}6.
\]
It is tempting to apply Legendre's criterion and the explicit continued fraction of \(e\) to exclude this constant.

The flaw is that \(P,Q\) need not be coprime. With \(g=\gcd(P,Q)\), the approximation constant at the reduced denominator is smaller by \(g^2\), and \(g\) need not be bounded. Multiples of convergents can therefore have very different constants at the unreduced scale. The quick argument proves no exclusion, and no conclusion from it is used here.

## Outcome

A single positive exponential denominator can satisfy all the local cancellation congruences. One- and two-term residual tests turn the remaining question into uniform restrictions on the reduced numerator and divisor structure of almost consecutive harmonic sums. No such restriction was proved. This investigation supplies no full solution or independent publishable progress.

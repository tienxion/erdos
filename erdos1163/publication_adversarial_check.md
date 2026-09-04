# Fresh publication-facing check

4 September 2026. This is an additional adverse check after the
earlier independent audits.

## Mathematical conclusions

**All-abelian theorem:** no gap found on the fresh pass. I revisited
the potentially vulnerable points rather than relying on the finite
verification script:

- The Birkhoff exponent is exactly
  \(\sum_j s_j(r_j-s_j)\); the Sylow components multiply.
- The defect inequalities include odd degree with no fixed point.
  In that case the necessary odd orbit supplies the missing loss.
- The ambient product is recovered from the actual orbit projections.
  The profile count and coefficient ratio therefore do not omit
  embeddings or require an unjustified injectivity assumption.
- The final exceptional-profile bound is a geometric series with ratio
  \((Cn)^{34}2^{-\lfloor n/2\rfloor/128}\), which is exponentially
  small eventually. The unspecified absolute positive exponent
  constant is justified.
- The saddle evaluation retains the lattice factor and gives the
  stated constant \(e^{-3/4}\); the parity-dependent theta factor
  in the Gaussian sum is necessary and correctly included.

The resulting formula remains
\[
|\operatorname{Ab}_n|
=n![z^{n-\delta}]\exp(z^2/2+z^4/24)\,
S_{\lfloor n/2\rfloor}(1+O(2^{-cn})),
\qquad \delta=n\bmod2.
\]
Here \(\delta!=1\), so its omission in this display changes nothing.

**The \(7/8\) lower bound:** verified by a new, simpler proof that does
not depend on any saddle estimate, relative enumeration theorem,
normalizer count, or typical-saturation argument. This proof is in
website_note_draft.md.

In fact it proves the finite lower bound
\[
\#\{H\leq S_n:|H|=2^{j_n}\}
\geq
\frac{n!}{(8!)^t t!\,2^a a!\,\delta!}
{r-4\brack \lfloor(r-4)/2\rfloor}_2
\quad(n\geq8),
\]
where \(n=8t+2a+\delta\), \(0\leq a\leq3\),
\(r=\lfloor n/2\rfloor\), and
\(j_n=\lfloor n/8\rfloor+\lfloor n/4\rfloor+2\).
Every counted subgroup has exactly this order and is of class at most
two and exponent dividing four. This strengthens the stated lower
bound to an order-refined version at a single explicit order.

The arbitrary deterministic choice of one \(E\) on each labelled
eight-point block is sufficient. Since the resulting group recovers
its orbit partition, different partitions cannot produce duplicate
subgroups. There is no need to claim that 105 embeddings are counted.

Combining the abelian count with this elementary lower bound gives
\[
\Pr_{H\in\operatorname{Sub}(S_n)}(H\text{ abelian})
\leq2^{-(n/8)\log_2n+O(n)}.
\]
This is an unrestricted probability bound; the available order CLTs
remain restricted to their stated projection classes.

## Current-source check and its limits

The live [1162 discussion](https://www.erdosproblems.com/forum/thread/1162)
was inspected by the parent agent through CUA on 4 September 2026:
it had no comments or proof claims. The main entry mentioned the
leading logarithmic asymptotic from Roney-Dougal–Tracey. The live
[1163 discussion](https://www.erdosproblems.com/forum/thread/1163)
had two comments about interpretation, without proof claims. Direct
fetches through the web tool returned 403; this paragraph records
the parent's live-browser observation rather than a successful
independent web fetch.

I directly inspected the full proof of Proposition 7.3 in
[Roney-Dougal–Tracey, arXiv:2503.05416](https://arxiv.org/html/2503.05416v1).
Its lower-bound construction uses disjoint prime-order cycles and
middle-dimensional subdirect products. I did not find the
extraspecial construction or an explicit \(7/8\) coefficient in that
accessible text. This observation does not establish novelty.

A prior public note dated 11 August 2026,
[exact order counts in a prime-orbit slice](https://erdosproblemaday.com/day/1162-order-refined-p-orbit-slice),
gives order-refined counts and asymptotics for the simpler family with
all nontrivial orbits of one prime length. That overlaps the elementary
prime-cycle mechanism and should be acknowledged in any expanded
literature review. It does not treat the degree-eight factor in the
accessible note.

The degree-eight group and its quotient efficiency are classical:
[Kovács–Praeger (1989)](https://archives.maths.anu.edu.au/people/Kovacs/K070.pdf),
Section 2. The website draft attributes this ingredient explicitly.

This check supports the correctness of the stated partial claim.
It is not a comprehensive priority search or prior expert endorsement.
The short draft includes truthful AI-assistance and review disclosure.
No submission or communication to another party was performed by
this audit agent.

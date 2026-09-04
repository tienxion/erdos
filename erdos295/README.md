# Erdős problem 295 — research record

Updated 4 September 2026. **The full problem remains unresolved in this work. Publication-level novelty has not been established.** All work in this folder concerns problem 295 alone.

Let \(k(N)\) be the minimum number of distinct integers at least \(N\) whose reciprocals sum to 1. The question is whether
\[
k(N)-(e-1)N\longrightarrow\infty.
\]

The [consolidated research note](quantitative_obstructions.md) contains independently reviewed restricted theorems. Write \(D=|A|-(e-1)N\), \(M=\max A\), and \(b=(e-1)/2\).

- If \(D=o(N/\log N)\), then
  \[
  \log\prod_{a\in A,\ a>N^2}a\ge(e-o(1))N,
  \qquad
  \liminf\frac{(D+b)\log M}{N}\ge e.
  \]
- For each fixed \(B>1\), \(M\le N^{B+o(1)}\) forces
  \[
  D\ge(\mathcal C(B-1)-o(1))N/\log N,
  \]
  where the note gives an explicit integral and evaluated constants. In particular, \(M\le N^{2+o(1)}\) gives coefficient \(1.79033944\ldots\).
- The stronger assumption \(M=o(N^2)\) gives coefficient \(2.59516741\ldots\). More generally, a proved multiplicity bound strengthens the result for subquadratic powers.

The polynomial-ceiling proof uses connected components of the graph recording which large primes occur together in denominators, together with a quantitative bound on a positive rational sum's denominator. It accounts for multiple primes sharing one tail denominator. The subquadratic proof counts how many tail terms are needed to cancel each selected large prime.

The [literature audit](literature_audit.md) also corrects the baseline comparison: a routine corollary of Vose's classical theorem gives
\[
k(N)\le(e-1)N+O(\sqrt N),
\]
with exponential maximum denominator available simultaneously. This is established background, not new progress. Croot gives a polynomial-ceiling upper excess \(O(N\log\log N/\log N)\), so the constrained upper and lower bounds are not matched here.

The original problem permits unrestricted denominators. Boundedly many exponential denominators remain compatible with every result above. The [tail investigation](tail_investigation.md) explains why prime congruences alone do not exclude them.

Proof checks are recorded in [the exponential review](quantitative_review.md), [the polynomial review](polynomial_cap_review.md), and [the subquadratic review](subquadratic_review.md). These are independent informal mathematical reviews, not proof-assistant formalizations. The polynomial review retains earlier, weaker versions followed by the final continuous-exponent theorem; the consolidated note states the final results.

The [original prime obstruction](prime_obstruction.md) is preserved as the earlier research record and is superseded quantitatively by the consolidated note. Original source links are provided in the literature audits. Downloaded source PDFs and page scans are not included in this repository.

The exact new formulations were not found in inspected primary sources, but the original 1971 proof and a relevant 2005 paper remain unread because their full texts were inaccessible. The ingredients have classical antecedents. Accordingly, this is an internal research record, not a claim of a new solution or a submission-ready manuscript. No external posting, author contact, or submission has occurred.

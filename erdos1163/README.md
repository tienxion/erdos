# Problem 1163: orders of subgroups of symmetric groups

**Status: a partial result, not a solution of the unrestricted problem.**
The [submitted proof](proof.md) gives a uniform counting estimate for each
prescribed order in a linear interval. The other notes study specified
classes of subgroups and must be read with their stated sampling measures.

## The submitted result

Let $a_{n,j}=\#\{H\leq S_n:|H|=2^j\}$, counting actual subgroups.
Uniformly for integers $\lfloor n/4\rfloor\leq j\leq\lfloor n/2\rfloor$,

$$
\log_2 a_{n,j}\geq\frac{n^2}{16}
+\left(\frac{7n}{8}-\left|j-\frac{3n}{8}\right|\right)\log_2 n-O(n).
$$

Together with Roney-Dougal–Tracey's upper bound for all 2-subgroups, this gives

$$
\log_2 a_{n,j}=\frac{n^2}{16}+O(n\log n)
$$

uniformly throughout the interval. The lower bound uses groups of class at
most two and exponent dividing four, acting on blocks of two, four, and eight
points. It does not depend on the longer classification or dominance arguments
in the research notes.

This does **not** determine the relative probabilities of these orders for a
uniformly chosen unrestricted subgroup: the remaining error matters at that scale.

## Reading order

| Document | Purpose |
|---|---|
| [Submitted proof](proof.md) | Self-contained construction, exact finite bound, and asymptotic estimate |
| [Order spectrum](order_spectrum.md) | Additional matching second term inside the restricted family $Q_n$ |
| [Consolidated results](results.md) | Broader counts and limit laws, with precise domains and proof links |
| [Research notes](research_guide.md) | Detailed arguments and their development |
| [Audits](audit_guide.md) | Separate AI-agent checks, including the submitted proof's audit |
| [Verification](verification_guide.md) | Python/Sage scripts, finite data, and reproduction instructions |
| [References](references.md) | Prior results and sources |
| [Submission record](submission.md) | What was submitted and the observed moderation status |

The [Erdős website claim](https://www.erdosproblems.com/forum/thread/1163/proof-claims)
was submitted on **4 September 2026** under **tienxion** as a partial proof.
It was awaiting moderator approval when submitted; consult that page for later
status. The [typeset web version](https://erdos-1163-order-counts.groggorius-george.chatgpt.site)
remains the writeup linked from that submission.

## Verification and attribution

The submitted argument and the broader notes were developed with OpenAI GPT-6
assistance. [The submitted-proof audit](audit_order_spectrum.md) found
no gap in the construction, endpoint cases, or counting estimates. This is an
AI-agent audit, not a claim of independent human expert endorsement.
The Gaussian identities, the degree-eight group, and the cited upper bound
are prior mathematics. Whether the explicit refinement is already recorded
in the literature has not been established.

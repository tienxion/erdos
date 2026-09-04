# Submission record

- **Problem:** [Erdős 1163](https://www.erdosproblems.com/1163)
- **Submitted:** 4 September 2026, 21:53:59 UTC
- **Account:** tienxion
- **Type:** Partial proof
- **Status observed at submission:** Awaiting moderator approval
- **Claim page:** [Erdős website](https://www.erdosproblems.com/forum/thread/1163/proof-claims)
- **Submitted writeup:** [Typeset web version](https://erdos-1163-order-counts.groggorius-george.chatgpt.site)
- **Repository copy:** [proof.md](proof.md)

The website displayed the completed claim with its external proof link.
This records successful submission, not moderator acceptance or a mathematical
endorsement by the website. Consult the claim page for later status.

## Submitted summary

We count subgroups of $S_n$ having a prescribed order $2^j$. Uniformly for
$\lfloor n/4\rfloor\leq j\leq\lfloor n/2\rfloor$, we obtain
$\log_2 a_{n,j}=n^2/16+O(n\log n)$. The construction combines permutation
groups on two, four, and eight points with binary subspace counting; the
matching leading upper bound follows from Roney-Dougal–Tracey. This gives
a partial counting result, while the order distribution of a uniformly
chosen unrestricted subgroup remains unresolved as of now.

## Disclosures

The submission disclosed OpenAI GPT-6 assistance with proof development,
audits, and drafting the summary, which the submitter edited. It explained
that $a_{n,j}$ counts actual subgroups, that novelty has not been established,
and that neither a full solution nor independent human expert verification
is claimed. No Lean formalization was submitted.

Only the self-contained prescribed-order argument was submitted. The broader
research notes in this repository are separate supporting research.

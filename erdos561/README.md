# Erdős problem 561: current research package

This task now concerns **only problem 561**, the size Ramsey number of two star forests. The full conjecture has not been solved. The current candidate contribution is a general local criterion with complete proofs, not the earlier finite search.

## Current theorem

For nonincreasing positive sequences A and B, put

\[
\ell_k=\max_{i+j=k}(a_i+b_j-1).
\]

The conjectured sum is exact if every nonfinal diagonal either has a maximizing pair with both sizes odd or one size equal to 1, or has one of the local gaps specified in Theorem 1 of the manuscript. In particular, a drop of at least 3 suffices at each diagonal lacking such a maximizing pair. A drop of 2 also suffices when the next diagonal has the required separation. The final diagonal has no restriction.

The simultaneous-suffix framework and parity-based deficit bound were already posted by [rickyc on 6 August 2026](https://www.erdosproblems.com/forum/thread/561#post-8384), as discovered in the final live-forum audit. The candidate addition here establishes exact minimum edge counts under local gap conditions by controlling the maximum degree of equality hosts. If consecutive maxima differ by at least 2, an equality host has at most one vertex of the largest allowed degree. This rules out the maximum-degree configurations of a putative smaller Ramsey host using Fournier's edge-coloring theorem.

The method permits arbitrary numbers of components and long repeated runs of star sizes. One consequence is

\[
\widehat r(K_{1,6}\sqcup rK_{1,3}\sqcup mK_2,\ K_{1,5}\sqcup K_2)
=11+7r+5m\qquad(r,m\ge1).
\]

Corollary 8 gives families with any number h of even components. The exact value exceeds the direct lower bound from rounding those components down and applying the published all-odd theorem by h. This comparison is with that specific prior bound, not a claim to have computed the strongest consequence of every earlier paper.

## Files

- [Manuscript PDF](output/pdf/manuscript.pdf): complete theorem, proofs, explicit infinite families, references, and limitations.
- [LaTeX source](manuscript.tex): editable source; compile with `tectonic --outdir output/pdf manuscript.tex` from this directory.
- [Novelty audit](novelty_audit.md): primary papers checked, exact overlap, and remaining access gaps.
- [Underlying proof notes](extensions_combinatorics.md) and [independent audit](extensions_analysis.md).
- [Earlier two-star theorem and finite search](notes.md): complete special-case proof, but extensive overlap with known cases.

## What is established, and what is not

**Mathematical status:** the local theorem, its boundary cases, the strengthened equality-degree assertion, and its displayed corollaries have complete informal proofs. The general argument and the arbitrary-h family were checked independently by multiple research agents. The coordinating user has now reported mathematical review and found the argument accurate. The proof uses established theorems of Vizing, Petersen, and Fournier; it does not depend on computation. The PDF was compiled and visually checked.

**Novelty status:** the explicit families are outside the hypotheses of the theorem statements read in the original 1978/1981 papers, the published 2025 DJKR paper, Lortz–Mengersen 2021, and Fu–Luo–Ni v3. They also fail the numerical Győri–Schelp condition restated by DJKR and lie outside the stated scope of Cheng's thesis. This is a defensible noncoverage claim, not proof of priority.

**Submission:** the reviewed manuscript was submitted as a partial-proof claim by **tienxion** on 4 September 2026 and is awaiting moderator approval. See [the submission record](submission_record.md) for the exact text, public PDF link, and verified file hash. No author contact has been made. The general problem remains open.

**Remaining priority work:** obtain and compare the original Győri–Schelp 2002 paper and Cheng 2010 thesis, and obtain an independent specialist's assessment of whether the additional criterion follows from prior work. Submission does not resolve these questions.

## Follow-up research, separate from submitted version 1

- [Recursive lower bound](improvement_recursive.md): a universal refinement using equality-host degree information; all stated steps have received independent mathematical audits.
- [Matching extensions](improvement_gap.md): additional local recovery rules using a matching covering every maximum-degree vertex, followed by an even-degree factorization.
- [Mixed two-edge-star forests](improvement_plateaus.md): a complete proof that the size Ramsey number of sP3 plus r isolated edges versus tP3 is 3(s+t−1)+2r, for s,t≥1 and r≥0. This handles long repeated bad diagonals.

These follow-up results were developed after the user's review of version 1. They require their own human review before a further site submission. Their novelty remains qualified by the literature-access gaps described above.

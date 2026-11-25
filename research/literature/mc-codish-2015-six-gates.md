# Codish, Cruz-Filipe, Frank, Schneider-Kamp (2015): When six gates are not enough

| Field | Value |
|---|---|
| Title | When Six Gates are Not Enough |
| Authors | Michael Codish, Luís Cruz-Filipe, Michael Frank, Peter Schneider-Kamp |
| Year | 2015 (arXiv submission 24 August 2015) |
| Venue | arXiv preprint 1508.05737 (cs.CC). A refereed venue, if any, was **not confirmed** |
| Affiliations | Ben-Gurion University of the Negev; University of Southern Denmark (per search summary) |
| Group | MC: maximum MC for small n. Index: `index-multiplicative-complexity.md` |

## Attribution correction

The NP-FRONTIER task brief attributed arXiv 1508.05737 to Find, Smith-Tone and Sönmez Turan. Two independent WebSearch results show that the authors are **Codish, Cruz-Filipe, Frank and Schneider-Kamp**.

The Find–Smith-Tone–Sönmez Turan paper is a different one: "The number of Boolean functions with multiplicative complexity 2" (`mc-find-2015-mc-two.md`).

## Relevant theorem (abstract level)

**M(7) ≥ 7.** Using a pigeonhole (counting) argument, some Boolean function on 7 inputs has multiplicative complexity at least 7, so it cannot be computed with 6 multiplications over GF(2).
- The paper's table lists the previous bound as M(7) ≥ 6 (from the degree bound).
- The authors describe the result as raising the best known lower bound by 1.

## Why it matters for NP-FRONTIER

- The result is **non-constructive**: no explicit 7-variable function with MC 7 is given, as far as the snippets show.
- **Evidence on (a).** A fresh-variable lemma (index item (a)) would give M(n+1) ≥ M(n) + 1 with explicit witnesses. A dedicated counting argument was used here instead.
  - This is weak evidence that (a) was not known in 2015.
  - However, M(6) = 6 was only established in 2018 (`mc-calik-2018-six-variables.md`). In 2015 even (a) would have given only M(7) ≥ M(6) + 1 ≥ 6.
- **Explicit witness target.** An explicit 7-variable function with MC ≥ 7 remains a natural concrete target, for example g6·x_7 for an explicit MC-6 function g6 (index suggested check 2).

## Limitations

- The details of the counting argument were not seen.
- Publication status beyond arXiv was not confirmed.

## Retrieval

- Title, authors, arXiv ID, submission date, category and affiliations: from WebSearch summaries of the arXiv listing (web3.arxiv.org/abs/1508.05737, arxiv.org/pdf/1508.05737) and ar5iv.
- Main result ("some Boolean functions on 7 inputs need at least 7 AND gates", pigeonhole principle, previous table value M(7) ≥ 6): from WebSearch summaries of the abstract and introduction.
- Attribution correction: two separate WebSearch results (queries "When six gates are not enough …" and "arXiv 1508.05737 Codish …") agree.

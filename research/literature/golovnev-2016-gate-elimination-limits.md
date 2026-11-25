# Golovnev, Hirsch, Knop, Kulikov (2016/2018): On the limits of gate elimination

| Field | Value |
|---|---|
| Title | On the Limits of Gate Elimination |
| Authors | Alexander Golovnev, Edward A. Hirsch, Alexander Knop, Alexander S. Kulikov |
| Year | 2016 (conference); 2018 (journal) |
| Venues | 41st MFCS (2016), LIPIcs, DOI 10.4230/LIPIcs.MFCS.2016.46. Journal of Computer and System Sciences 96:107–119 (2018), DBLP key journals/jcss/GolovnevHKK18 |
| Preprint | ECCC TR16-119 (https://eccc.weizmann.ac.il/report/2016/119/) |
| Group | Circuit lower bound frontier (limitation of the main technique) |

## Context

All known linear lower bounds for explicit functions over general bases use **gate elimination**:
1. Take an optimal circuit for f.
2. Apply one or more substitutions to input variables (constants, or functions of other variables).
3. Show that several gates become redundant and can be eliminated.
4. Recurse on the restricted function, which stays in a class closed under such substitutions.

This covers Blum's 3n, FGHK's (3 + 1/86)n, Li–Yang's 3.1n, and presumably the 2026 3.5n claim.

## Relevant theorem

Abstract-level statement, confirmed. **Gate elimination cannot prove linear lower bounds cn beyond a certain constant c, where c depends only on the number of substitutions made in a single step of the induction.**

The ECCC revision adds:
- a limitation for gate elimination with **any subadditive complexity measure** that performs almost the maximal N/2 substitutions;
- a lower bound on decision-tree complexity;
- a note that the limitation also applies to average-case circuit lower bounds and to Circuit #SAT algorithms built on gate elimination.

Not checked: the exact formalization of "a gate elimination proof", the explicit dependence c(k) on the number k of substitutions per step, and the functions witnessing the limitation.

## What it rules out or limits

It rules out proving large-constant linear bounds over B2 (and a fortiori superlinear or superpolynomial bounds) with gate elimination that uses a bounded number of substitutions per inductive step. The strong version covers any subadditive measure with up to about N/2 substitutions.

For the program: **a P ≠ NP or NP ⊄ P/poly argument cannot be "gate elimination, done more cleverly"** unless it leaves the formal framework of this paper. The hypothesis must then say exactly how.

## Why it matters for NP-FRONTIER

Gate elimination is the only route that ever produced explicit lower bounds for unrestricted circuits, and this result caps it. Together with natural proofs (`razborov-1997-natural-proofs.md`) and locality (`chen-2020-locality-barrier.md`), it delimits the general-circuit frontier.

## Limitations

- The limitation is relative to a formal model of gate elimination. A proof that departs from that model, e.g. one using non-subadditive measures, unbounded substitution counts, or global arguments, is not covered.
- The constant is not recorded here.

## Check to apply to a hypothesis

If a lower-bound argument proceeds by "restrict variables, count eliminated gates, recurse", determine:
- the number of substitutions per step, and
- whether the progress measure is subadditive.

If both fall within this paper's framework, the argument cannot exceed c·n for the corresponding constant, so it cannot yield superlinear bounds.

## Retrieval

- Authors, MFCS 2016 venue and DOI, JCSS 96 (2018) pp. 107–119 (from DBLP) and ECCC TR16-119: confirmed by WebSearch (DBLP entry, Dagstuhl DOI page, IUCC CRIS record, ECCC page; result summaries).
- Main statement (no linear bound cn beyond a constant c depending only on substitutions per step): confirmed via WebSearch summaries of the abstract.
- Subadditive-measure / N/2-substitution strengthening, decision-tree bound, and average-case / #SAT remark: confirmed via WebSearch summary of the ECCC revision notes.
- Formal model details and constants: not checked.

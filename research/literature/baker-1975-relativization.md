# Baker, Gill, Solovay (1975): Relativizations of the P =? NP question

| Field | Value |
|---|---|
| Title | Relativizations of the P =? NP Question |
| Authors | Theodore Baker, John Gill, Robert Solovay |
| Year | 1975 |
| Venue | SIAM Journal on Computing 4(4):431–442 (December 1975) |
| DOI | 10.1137/0204037 |
| URLs | https://www.scilit.net/publications/465bd6e25769de9154ce750a4b3bb6ba ; PDF copy: https://cse.ucdenver.edu/~cscialtman/complexity/Relativizations%20of%20the%20P=NP%20Question%20(Original).pdf |
| Group | Barrier (relativization) |

## Relevant theorem

For a language O, P^O and NP^O are the classes decided by deterministic and nondeterministic polynomial-time oracle Turing machines with oracle O.

**Theorem (BGS 1975, standard two-oracle form).**
1. There is an oracle A with P^A = NP^A.
2. There is an oracle B with P^B ≠ NP^B.

Standard constructions (recalled from memory, not checked against the paper):
- A: any PSPACE-complete language, for example TQBF. Then NP^A ⊆ PSPACE ⊆ P^A.
- B: built by diagonalization against an enumeration M_1, M_2, ... of polynomial-time oracle machines, with L_B = {1^n : B contains a string of length n}. Then L_B ∈ NP^B. For each i, pick a fresh length n where M_i^B(1^n) makes fewer than 2^n queries. Add an unqueried length-n string to B exactly when M_i rejects, so M_i errs on 1^n and L_B ∉ P^B.

The paper also contains further relativized results (e.g. on NP versus coNP). These are not itemized here (unverified).

## What it rules out or limits

A proof technique **relativizes** if it stays valid when every machine in the argument gets oracle access to the same arbitrary language O.
- A relativizing proof of P ≠ NP would give P^A ≠ NP^A, contradicting (1).
- A relativizing proof of P = NP would give P^B = NP^B, contradicting (2).

So **any resolution of P vs NP, in either direction, must use a non-relativizing argument.** Approaches that are typically ruled out:
- Pure simulation and diagonalization arguments: time-hierarchy-style proofs, universal machines, padding, and closure-under-composition arguments that treat machines as black boxes.
- On the P = NP side, any "generic" witness-finding procedure that uses the NP verifier only as a black box. Oracle B is the standard example: black-box search over 2^n candidate witnesses needs exponentially many queries. A polynomial-time algorithm for SAT must exploit the internal structure of instances, such as the clause structure of a CNF.

## Why it matters for NP-FRONTIER

This is the first filter for every P ≠ NP proof attempt and every "universal" P = NP algorithm. A hypothesis must name the step that fails relative to some oracle. That step carries the real content and is where review should concentrate.

## Limitations

- "Relativizes" is not a formal property of a written proof until a formal framework is fixed. In practice, check each lemma for oracle machines with an arbitrary oracle.
- Non-relativizing techniques exist. Recalled examples, not checked here: arithmetization (IP = PSPACE, MIP = NEXP), the PCP theorem, and Williams's ACC0 lower bound (see `williams-2011-acc.md`). Arithmetization-based techniques are in turn limited by algebrization (`aaronson-2009-algebrization.md`).
- For non-uniform circuit lower bounds, "relativization" (circuits with oracle gates) is less canonical. The barrier is cleanest for uniform machine classes.
- The barrier says nothing about which answer is true.

## Check to apply to a hypothesis

1. Does every lemma hold verbatim when all machines get an arbitrary oracle O? If yes, the argument cannot settle P vs NP: reject.
2. Otherwise, identify the step that fails relative to A (PSPACE-complete) or to B (BGS diagonal oracle). Treat that step as the critical step and audit it first.

## Related results

- Charles H. Bennett and John Gill, "Relative to a random oracle A, P^A ≠ NP^A ≠ co-NP^A with probability 1", SIAM Journal on Computing 10 (1981), pp. 96–113. Bibliographic data confirmed from a WebSearch hit: the title of a Journal of Symbolic Logic review that covers both BGS and Bennett–Gill. The statement is in the title.
- The search also returned arXiv 2112.03677 ("On Baker-Gill-Solovay Oracle Turing Machines and Relativization Barrier") and arXiv 2601.09702 ("Diagonalization Without Relativization: A Closer Look at the Baker-Gill-Solovay Theorem"). **Not reviewed.** Do not rely on them as reinterpretations of BGS without an independent audit.

## Retrieval

- Title, authors, journal, volume/issue (4(4)), pages 431–442, December 1975 and DOI 10.1137/0204037: confirmed by WebSearch (result summary citing the scilit record and the UC Denver PDF copy).
- That the relativized question has a positive answer for some oracles and a negative answer for others: confirmed at abstract level by the same WebSearch summary.
- The standard two-oracle formulation and its interpretation (no relativizing technique settles P vs NP): confirmed from secondary sources (MIT OCW 18.405J notes, UMD lecture notes) surfaced by WebSearch.
- Constructions of A and B, and the list of non-relativizing techniques: recalled from memory, not checked against the paper.

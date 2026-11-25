# EXP-001: Exact multiplicative complexity of small Boolean functions

**Research question.** Compute MC exactly for small functions. Validate the tools against published values, and provide ground truth for PNE-001/OTH-001.

**Methods (two independent implementations).**
- `bfs4.py`: exact MC of all 2^16 four-variable functions with no SAT solver. It runs a breadth-first search over the spans W_k = W_{k−1} + span{a·b : a, b ∈ W_{k−1}}, starting from W_0 = affine functions. Every function computed by a k-AND circuit lies in some W_k, and every function in some W_k is computed by a k-AND circuit.
- `mc.py`: SAT encoding of "a k-AND XOR-AND circuit computes F". It uses PySAT 1.9.dev25 with CaDiCaL 1.5.3, Tseitin-encoded XOR chains, and non-degenerate gates (an assumption that loses nothing; see the docstring). Every circuit the solver returns is re-checked by an independent evaluator (`evaluate`). `encode()` exposes the CNF for proof logging.

**Results.**
- MC distribution over all 65,536 functions of 4 variables: MC 0: 32, MC 1: 1,120, MC 2: 31,616, MC 3: 32,768. The maximum is 3 = n − 1, matching the literature (Turan–Peralta; bibliographic data via WebSearch). MC = 3 holds exactly for the 32,768 functions of degree 4.
- SAT spot checks agree: MC(x1x2x3) = 2, MC(AND4) = 3 (k = 2 UNSAT in 0.3 s).
- Scaling limit: SAT UNSAT proofs on 5–6 variables with k ≥ 3 can take many minutes. The AND5 k = 3 probe did not finish in about 15 minutes, so UNSAT is used sparingly and certified separately (EXP-002/003).

**Reproduce.** `python3 bfs4.py` (about 1 minute; writes `mc4.json`). `scripts/setup_env.sh` installs PySAT.

**Limitations.** The BFS is exact but exponential, practical up to 4 variables in Python. SAT results without a proof certificate are not treated as proofs.

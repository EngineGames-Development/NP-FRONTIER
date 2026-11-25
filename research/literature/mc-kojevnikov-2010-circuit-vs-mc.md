# Kojevnikov, Kulikov (2010): Circuit complexity and multiplicative complexity of Boolean functions

| Field | Value |
|---|---|
| Title | Circuit Complexity and Multiplicative Complexity of Boolean Functions |
| Authors | Arist Kojevnikov, Alexander S. Kulikov |
| Year | 2010 |
| Venue | CiE 2010 (Computability in Europe), LNCS 6158, pp. 239–245 |
| DOI | 10.1007/978-3-642-13962-8_27 |
| DBLP | conf/cie/KojevnikovK10 |
| Group | MC ↔ circuit size; statement of the explicit-bound frontier. Index: `index-multiplicative-complexity.md` |

## Relevant statements (abstract level, relayed)

1. **Main result.** A very simple proof of a **7n/3 − c lower bound** on circuit complexity (full binary basis) for a large class of functions representable by high-degree polynomials over GF(2).
   - The proof uses lower bounds on MC.
   - It uses a circuit complexity measure that assigns different weights to XOR and AND gates.
   - The authors call it "as simple as Schnorr's proof of a 2n − c lower bound".
2. **Frontier statement** (relayed by a search summary): the best known lower bound on the MC of an explicit function is **n − 1**.

## Why it matters for NP-FRONTIER

- Item 2 is one of two independent "best known explicit MC lower bound is n − 1" statements (with `mc-demenkov-2011-affine-dispersers.md`), relevant to index item (c).
- Item 1 shows the standard way MC lower bounds feed circuit-size lower bounds: XOR gates are cheap but not free.
  - Any improvement of explicit MC bounds beyond n would interact with this method. Agent D has not worked out how.
  - Agent D notes, as standard, that C_{B2}(f) ≥ MC(f), because every binary gate is affine or AND-type.

## Limitations

- Abstract and slides only.
- The exact phrase and context of the "n − 1" statement were not seen.

## Retrieval

- Title, authors, venue, pages, DOI and DBLP key: from WebSearch summaries of doi.org, DBLP, the SPbU pure portal and Bohrium.
- Item 1: from WebSearch summaries quoting the abstract.
- Item 2: from a WebSearch summary ("A 2010 paper by Kojevnikov and Kulikov states that the best known lower bound is n − 1 for explicit functions' multiplicative complexity"); the original sentence was not seen.

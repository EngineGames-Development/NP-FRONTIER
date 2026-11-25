# Mishra, Santhanam (2026): An explicit 3.5n − o(n) size lower bound against general Boolean circuits (UNREFEREED CLAIM)

| Field | Value |
|---|---|
| Title | An Explicit 3.5n-o(n) Size Lower Bound against General Boolean Circuits |
| Authors | Om Swostik Mishra, Rahul Santhanam |
| Year | 2026 |
| Venue | ECCC Technical Report TR26-260, dated 19 October 2026. Not known to be peer-reviewed |
| URL | Expected at https://eccc.weizmann.ac.il/report/2026/260/ (constructed from the report number; the page itself was **not** retrieved) |
| Group | Circuit lower bound frontier (general circuits); added to the requested list because it changes the frontier statement |

## Claimed result (not verified)

**Claim.** A lower bound of **3.5n − o(n)** on the size of B2 (full binary basis) circuits computing an **explicit function in P**. This would improve the 3.1n − o(n) bound of Li–Yang (2022).

Not confirmed:
- which function is used (the listing excerpt does not say it is an affine disperser);
- the technique (presumably gate elimination; unverified);
- correctness.

## What it rules out or limits

Frontier calibration only, as for `li-2022-3.1n-lower-bound.md`. Even if correct, the bound is linear. It changes nothing about the gap to superpolynomial bounds, nor about the limits of gate elimination (`golovnev-2016-gate-elimination-limits.md`).

## How NP-FRONTIER should cite the frontier until this is checked

"Best refereed explicit lower bound for B2 circuits: 3.1n − o(n) (Li–Yang, STOC 2022). Claimed: 3.5n − o(n) (Mishra–Santhanam, ECCC TR26-260, Oct 2026; unrefereed, not verified here)."

## Next step

Retrieve the ECCC report directly if a fetch route is available. No direct fetch of ECCC was attempted in this session; only WebSearch was used. Then record the function, the technique and the main theorem statement.

## Retrieval

- Title, authors, report number TR26-260, date 19 Oct 2026 and the one-sentence claim (3.5n − o(n) for B2 circuits computing an explicit function in P, improving Li–Yang): from a single WebSearch result summary of an ECCC keyword listing page (eccc.weizmann.ac.il/keyword/19061). A second WebSearch for the report title did **not** return the report page.
- Independent corroboration: a WebSearch summary of arXiv 2610.27127 ("Short Point Lists for CNFs and Stronger Constant-Depth Circuit Hardness", 2026) reports that it cites "a recent preprint of Mishra and Santhanam [MS26]" as improving the explicit B2 bound to 3.5n − o(n). That citation does not give the ECCC number.
- Everything else: unverified.

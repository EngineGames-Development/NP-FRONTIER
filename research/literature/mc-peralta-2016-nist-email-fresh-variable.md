# Peralta (2016), internal NIST email: MC(uv·f) = 1 + MC(v·f)

| Field | Value |
|---|---|
| Title | Email "Re: MC of the Counting function (8,4) is 6." |
| Authors | René Peralta, to Çağdaş Çalık, cc Meltem Sönmez Turan (NIST) |
| Date | 15 September 2016 |
| URL | https://nist.pqcrypto.org/foia/20230815/ (FOIA release; file "Re_ MC of the Counting function (8,4) is 6.(1)-2.pdf") |
| Group | MC: fresh-variable statements (novelty of PNE-001) |

## Content (retrieved: PDF downloaded and read in cycle 002)

The relevant passage, verbatim: "I am attaching what I think is the proof we needed (I think what you wanted is that the multiplicative complexity of uv f (where u,v are variables and f is a function of variables other than u,v) is 1 + mult_comp(v f). That is a corollary of the claim in the attached."

The attachment (MultComp3.pdf) is **not** part of the release. The thread also reports a 6-AND circuit for the counting function E(8,4).

## Why it matters for NP-FRONTIER

- The statement is PNE-001 for every function of the form h = v·f, i.e. for h that already carries a fresh-variable factor.
- Peralta calls it a corollary of a claim in the attachment. That claim may be a general fresh-variable lemma. If so, PNE-001 (and our Theorems 17 and 25) would be known in unpublished form.
- **Novelty of PNE-001 is therefore unconfirmed.** No published statement of the general lemma was found.

## Limitations

- This is an informal, unreviewed email, and the proof is not visible.
- We do not know whether the attached claim covers general h.
- It is not cited as a theorem anywhere in our documents.

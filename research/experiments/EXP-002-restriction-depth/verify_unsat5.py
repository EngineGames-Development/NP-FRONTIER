"""Independently verify every sample5 'UNSAT at k=D' claim with the exhaustive SAT-free S_2 test (all have D = 2)."""
import json, sys
sys.path.insert(0, ".")
from verify_s2_5 import in_S2
d = json.load(open("sample5_results.json"))
claims = [o for o in d if o["status_at_D"] == "UNSAT"]
bad = [o["F"] for o in claims if not (o["D"] == 2 and in_S2(o["F"]) is None)]
print(f"{len(claims)} UNSAT claims (MC > D = 2); independently confirmed: {len(claims) - len(bad)}; contradicted: {bad}")

"""EXP-004b: exhaustive first-gate certificates for the 7 MC-3 functions with three cheap directions (EXP-005),
where Corollary 13 does not apply. Uses --distinct-x (justified by Lemma 12)."""
import json, os, subprocess, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); EXP2 = os.path.join(HERE, "..", "EXP-002-restriction-depth")
HARD = ['0x6e890b2', '0x10dce02c', '0x1383e575', '0x8130e859', '0xddfc6a78', '0xec974362', '0xecf49415']
def work(g):
    out = subprocess.run([sys.executable, "-u", "first_gate_general.py", g, "--distinct-x"], cwd=EXP2,
                         capture_output=True, text=True, timeout=6000).stdout.strip().splitlines()
    return {"g": g, "log": out}
if __name__ == "__main__":
    res = []
    with Pool(3) as pool:
        for r in pool.imap_unordered(work, HARD):
            res.append(r); print(r["g"], "|", r["log"][0] if r["log"] else "", "|", r["log"][-1] if r["log"] else "", flush=True)
            json.dump(res, open(os.path.join(HERE, "results_hard7.json"), "w"))

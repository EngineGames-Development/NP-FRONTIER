import NPFrontier.BoolFun
/-! Axiom audit: every build prints the axioms each headline theorem depends on.
Acceptable: none, or a subset of [propext, Classical.choice, Quot.sound]. Anything else must be recorded. -/
open NPFrontier NPFrontier.BF
#print axioms top_anf
#print axioms anf_xor
#print axioms degLE_xor
#print axioms degLE_node_of_restrict
#print axioms degLE_restrict
#print axioms degLE_pred_iff_even_weight
#print axioms gate_normalize
#print axioms mul_eval_one
#print axioms peval_anf
#print axioms same_direction_product

import NPFrontier.BoolFun
import NPFrontier.Circuit
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
-- XOR-AND circuits (NPFrontier/Circuit.lean); full names, since `eval` etc. also exist in `NPFrontier.BF`.
#print axioms NPFrontier.Circuit.vals_eq
#print axioms NPFrontier.Circuit.IsRun.unique
#print axioms NPFrontier.Circuit.eval_elim
#print axioms NPFrontier.Circuit.elim_affine
#print axioms NPFrontier.Circuit.elim_left
#print axioms NPFrontier.Circuit.elim_right
#print axioms NPFrontier.Circuit.elim_xor
#print axioms NPFrontier.Circuit.eval_comp
#print axioms NPFrontier.Circuit.exists_comp
#print axioms NPFrontier.Circuit.eval_addOut
#print axioms NPFrontier.Circuit.exists_xor_affine
#print axioms NPFrontier.Circuit.eval_addDummy
#print axioms NPFrontier.MCle.mono
#print axioms NPFrontier.MCleOn.mono
#print axioms NPFrontier.MCle_zero_iff
#print axioms NPFrontier.MCleOn.of_elim_left
#print axioms NPFrontier.MCleOn.of_elim_right
#print axioms NPFrontier.MCleOn.of_elim_xor
#print axioms NPFrontier.MCle_xor_affine_iff
#print axioms NPFrontier.MCle.comp_affine
#print axioms NPFrontier.MCleOn.comp_affine
#print axioms NPFrontier.MCleOn.comp_affine_of_maps_to
#print axioms NPFrontier.MCle_comp_section_iff
#print axioms NPFrontier.MCle_and2
#print axioms NPFrontier.not_MCle_and2_zero
#print axioms NPFrontier.MCle_and3

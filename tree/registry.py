# tree/registry.py

from tree.nodes import q0_welcome
from tree.nodes import q1_binary_refstd
from tree.nodes import q2_binary_output
from tree.nodes import q3_multi_refstd
from tree.nodes import q4_multi_output
from tree.nodes import q5_multi_labels
from tree.nodes import q6_multi_measurement
from tree.nodes import n01_binary_truth_var
from tree.nodes import n02_binary_2x2
from tree.nodes import n03_binary_curve
from tree.nodes import n11_multi_truth_var
from tree.nodes import n12_multi_score
from tree.nodes import n13_multi_topn
from tree.nodes import n14_multi_kbyk
from tree.nodes import n15_multi_ordinal

_ALL_NODES = [
    q0_welcome,
    q1_binary_refstd,
    q2_binary_output,
    q3_multi_refstd,
    q4_multi_output,
    q5_multi_labels,
    q6_multi_measurement,
    n01_binary_truth_var,
    n02_binary_2x2,
    n03_binary_curve,
    n11_multi_truth_var,
    n12_multi_score,
    n13_multi_topn,
    n14_multi_kbyk,
    n15_multi_ordinal,
]

QA_TREE: dict = {mod.NODE["id"]: mod.NODE for mod in _ALL_NODES}

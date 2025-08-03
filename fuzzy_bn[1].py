
# fuzzy_bn.py
# Author: Khujasta Basiri
# CYSE 630 Final Exam Project
# This script builds a Fuzzy Bayesian Network (FBN) from STIX data and models uncertainty using fuzzy logic.

import json
from pysmile import Network
import numpy as np

class FuzzyBayesianNetwork:
    def __init__(self):
        self.net = Network()
        self.fuzzy_sets = {
            "low": lambda x: max(0, min(1, (0.5 - x) / 0.5)),
            "moderate": lambda x: max(0, 1 - abs(x - 0.5) / 0.5),
            "high": lambda x: max(0, min(1, (x - 0.5) / 0.5))
        }

    def add_node(self, node_id, name):
        self.net.add_node(Network.NODE_TYPE_CPT, node_id)
        self.net.set_node_name(node_id, name)
        self.net.set_outcome_id(node_id, 0, "False")
        self.net.set_outcome_id(node_id, 1, "True")

    def set_noisy_or_definition(self, node_id, parents, base_prob=0.01, influence=0.6):
        if not parents:
            self.net.set_node_definition(node_id, [1-base_prob, base_prob])
            return

        table_size = 2 ** len(parents)
        definition = []
        for i in range(table_size):
            bits = [(i >> j) & 1 for j in range(len(parents))]
            p_true = 1 - np.prod([1 - influence if b else 1 for b in bits])
            definition.extend([1-p_true, p_true])
        self.net.set_node_definition(node_id, definition)

    def build_from_stix(self, stix_file):
        with open(stix_file) as f:
            stix_data = json.load(f)

        ttps, relationships = {}, []
        for obj in stix_data.get("objects", []):
            if obj["type"] == "attack-pattern":
                ttps[obj["id"]] = {
                    "id": obj["id"],
                    "name": obj.get("name", ""),
                    "technique_id": obj.get("external_references", [{}])[0].get("external_id", ""),
                    "tactic": obj.get("kill_chain_phases", [{}])[0].get("phase_name", "")
                }
            elif obj["type"] == "relationship":
                relationships.append((obj["source_ref"], obj["target_ref"], obj.get("relationship_type", "")))

        id_map = {}
        for stix_id, info in ttps.items():
            if info["technique_id"]:
                self.add_node(info["technique_id"], info["name"])
                id_map[stix_id] = info["technique_id"]

        for src, tgt, rel_type in relationships:
            if src in id_map and tgt in id_map:
                self.net.add_arc(id_map[src], id_map[tgt])

        for stix_id, node_id in id_map.items():
            parents = [p for p in self.net.get_parents(node_id)]
            self.set_noisy_or_definition(node_id, parents)

    def save(self, filename="attack_flow.xdsl"):
        self.net.write_file(filename)


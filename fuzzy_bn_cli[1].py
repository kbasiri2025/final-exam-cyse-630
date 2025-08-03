
# fuzzy_bn_cli.py
# Author: Khujasta Basiri
# CYSE 630 Final Exam (Undergraduate Version)
# Command-line interface for the Fuzzy Bayesian Network system.

from fuzzy_bn import FuzzyBayesianNetwork
import json

def fuzzy_label(prob):
    if prob < 0.33:
        return "Low"
    elif prob < 0.66:
        return "Moderate"
    return "High"

def main():
    print("=== Fuzzy Bayesian Network CLI ===")
    print("Building FBN from example_stix.json...")

    fbn = FuzzyBayesianNetwork()
    fbn.build_from_stix("example_stix.json")
    fbn.save("attack_flow.xdsl")
    print("FBN built successfully!\n")

    print("Enter fuzzy evidence for techniques (low, moderate, high). Leave blank to skip.")
    evidence = {}
    for node_id in fbn.net.get_all_node_ids():
        user_input = input(f"Evidence for {node_id} ({'/'.join(['low','moderate','high'])}): ").strip().lower()
        if user_input in ["low", "moderate", "high"]:
            if user_input != "low":
                fbn.net.set_evidence(node_id, "True")

    fbn.net.update_beliefs()

    print("\n=== Inference Results ===")
    for node_id in fbn.net.get_all_node_ids():
        beliefs = fbn.net.get_node_value(node_id)
        prob_true = beliefs[1] if len(beliefs) > 1 else 0
        print(f"{node_id}: Probability={prob_true:.3f}, Fuzzy Label={fuzzy_label(prob_true)}")

if __name__ == "__main__":
    main()

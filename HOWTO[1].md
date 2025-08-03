
# HOWTO: Using the Fuzzy Bayesian Network System
### Author: Khujasta Basiri

This guide explains how to set up and run the **Fuzzy Bayesian Network (FBN)** for cyber situational awareness.

---

## 🔹 1. Install Requirements
```bash
pip install flask prometheus_client
```
Install **PySMILE** separately (requires license).

---

## 🔹 2. Build the FBN
```bash
python fuzzy_bn.py
```
This generates `attack_flow.xdsl` from `example_stix.json`.

---

## 🔹 3. Run the Web Service
```bash
python bn_ws.py
```

---

## 🔹 4. Submit Evidence
Use the `/report` endpoint with linguistic input:
```bash
curl -X POST http://localhost:5000/report -H "Content-Type: application/json" -d '{"T1059":"high","T1566":"moderate"}'
```

---

## 🔹 5. Get Inference Results
```bash
curl http://localhost:5000/inference
```

---

## 🔹 6. Prometheus & Grafana
1. Start Prometheus with `prometheus.yml`.  
2. Add Prometheus as a data source in Grafana.  
3. Create dashboard panels to visualize `belief_<node>` metrics.  

---

## 🔹 7. Screenshots
- Include **Grafana dashboard images** showing how belief values update after evidence submission.



# Fuzzy Bayesian Network for Cyber Situational Awareness
### Author: Khujasta Basiri
### CYSE 630 Final Exam Project

This project extends my midterm submission into a **Fuzzy Bayesian Network (FBN)**-based cyber situational awareness system. It combines **fuzzy logic** with **Bayesian inference** to model uncertainty and provide adaptive cyber risk assessment.

---

## 🔹 Features
✅ Converts STIX attack flows into a **Fuzzy Bayesian Network (FBN)**  
✅ Supports **linguistic evidence input** (e.g., "low", "moderate", "high")  
✅ Implements **Noisy-OR CPT logic** for conditional probabilities  
✅ Provides **real-time inference results** through a web API  
✅ Exposes metrics for **Prometheus + Grafana dashboards**  

---

## 🔹 Files in this Project
- `fuzzy_bn.py` – Builds the FBN from STIX data  
- `bn_ws.py` – Flask web service with `/report` and `/inference` endpoints  
- `example_stix.json` – Realistic APT attack flow input  
- `attack_flow.xdsl` – BN file generated from STIX  
- `prometheus.yml` – Configuration for Prometheus metrics scraping  
- `HOWTO.md` – Detailed setup guide with examples and screenshots  

---

## 🔹 How It Works
1. **Convert STIX to FBN**
```bash
python fuzzy_bn.py
```

2. **Run the Web Service**
```bash
python bn_ws.py
```

3. **Submit a Linguistic Report**
```bash
curl -X POST http://localhost:5000/report -H "Content-Type: application/json" -d '{"T1059":"high","T1566":"moderate"}'
```

4. **Check Inference Results**
```bash
curl http://localhost:5000/inference
```

5. **Visualize in Grafana**
- Import Prometheus metrics into Grafana dashboard.

---

## 🔹 System Architecture
Flask API → Fuzzy Bayesian Network → Prometheus → Grafana Dashboard

---

## 🔹 Author
This project was created by **Khujasta Basiri** as part of the **CYSE 630 Final Exam** at George Mason University.

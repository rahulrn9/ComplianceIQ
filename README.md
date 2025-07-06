# ComplianceIQ – Data Quality & Contract Enforcement Framework

**Tech Stack:** Apache NiFi · Apache Kafka · Apache Airflow · Snowflake · Python · JSON Schema · Kubernetes

---

## 📌 Overview

**ComplianceIQ** is an end-to-end data quality and SLA enforcement framework built for financial compliance teams. It automates the validation of inbound data streams against predefined data contracts (JSON Schema), ensures regulatory SLAs are met, and provides real-time visibility into pipeline health and contract adherence.

---

## 🚀 Features

- 🔄 **Apache NiFi Flow** for validating incoming data against defined JSON schemas
- ✅ **JSON Schema Validation** to enforce strict data contract rules
- ⏰ **Apache Airflow DAG** to perform periodic SLA checks and flag stale or incomplete datasets
- 📈 **Snowflake Dashboards** (pluggable) to visualize compliance metrics
- 🛠 **Kubernetes Deployment** for scalable execution in cloud-native environments
- 🧠 Auto-remediation hooks for failed data ingestion or schema mismatch

---

## 🧱 Project Structure

ComplianceIQ/
├── src/
│ ├── nifi_flows/ # NiFi JSON flow definition
│ └── airflow_dags/ # Airflow DAG for validation
├── configs/
│ └── compliance-schema.json # JSON Schema for validation
├── k8s/
│ └── deployment.yaml # Kubernetes deployment manifest
├── scripts/ # Optional helper scripts
└── README.md # You're here!

yaml
Copy
Edit

---

## 🛠 Setup Instructions

### 📥 1. Clone the Repository

```bash
git clone https://github.com/rahulrn9/ComplianceIQ.git
cd ComplianceIQ
⚙️ 2. Set Up Apache NiFi
Import src/nifi_flows/validation_flow.json into NiFi

Configure NiFi to read from your source stream or files

Connect it with your Kafka topic if using streaming validation

📋 3. Define JSON Schema
Edit configs/compliance-schema.json to reflect your incoming data format and required fields.

⏱ 4. Run Airflow DAG
Copy src/airflow_dags/data_validation_dag.py to your Airflow dags/ directory

Ensure your compliance_data.json is available in /tmp/ or adjust the path

Start Airflow Scheduler and Webserver:

bash
Copy
Edit
airflow scheduler
airflow webserver
☁️ 5. Kubernetes Deployment (Optional)
bash
Copy
Edit
kubectl apply -f k8s/deployment.yaml
Ensure that:

Your container image is set correctly

Mounted volumes contain the necessary code/config

✅ Sample JSON Schema
json
Copy
Edit
{
  "type": "object",
  "properties": {
    "record_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "status": { "type": "string" }
  },
  "required": ["record_id", "timestamp"]
}
📊 Future Enhancements
Snowflake or BigQuery-based dashboard for SLA/contract tracking

Alerting via Slack/Email when violations occur

Integration with Open Policy Agent (OPA) for dynamic contract enforcement

Grafana dashboards with Prometheus metrics

🤝 Contributing
Pull requests and feedback are welcome. For major changes, please open an issue first to discuss your idea.

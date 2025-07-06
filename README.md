# ComplianceIQ – Data Quality & Contract Enforcement Framework

## Components
- Apache NiFi flow config for validating compliance data against JSON schemas.
- Airflow DAG to check data contract and SLA violations.
- JSON Schema sample and Kubernetes deployment file.

## Usage
1. Use NiFi flow (`validation_flow.json`) to validate incoming data.
2. Deploy Airflow DAG (`data_validation_dag.py`) for scheduled SLA checks.
3. Use Kubernetes manifest to deploy validator service.

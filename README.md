# ❄️ Project Snowflake — End‑to‑End ETL Pipeline with Airflow, Snowflake, and Terraform

A production‑grade, modular data pipeline that automates the ingestion, transformation, and loading of retailer data into Snowflake using **Python**, **Airflow**, **Terraform**, and **Docker**. Ideal for data engineers, DevOps engineers, and DataOps workflows.

---

## 📸 Overview

**Project Snowflake** automates the entire data lifecycle:

1. 🧼 **Transform** raw CSV data
2. ✂️ **Split** transformed data into logical tables
3. ☁️ **Upload** tables to Amazon S3
4. 🏔️ **Load** the final data into **Snowflake** using SQL scripts
5. ⚙️ All orchestrated by **Airflow DAGs**
6. 🏗️ Infrastructure managed via **Terraform**
7. 🐳 Runs in a self‑contained **Docker Compose** environment

---

## 🚀 Architecture

```text
📁 CSV → 🐍 Python (Transform) → 📁 Table CSVs → ☁️ S3 → 🧊 Snowflake
                │                      │             │
                │                      │             └─── via SQL in Airflow DAG
                │                      └─── upload_data_to_s3_bucket.py
                └─── transform_data_script.py ➜ split_data_into_tables.py

            ┌──────────────┐
            │   Airflow    │ ◀── Orchestrates pipeline
            └──────────────┘
```

### 🧰 Tech Stack

| Tool      | Purpose                                     |
| --------- | ------------------------------------------- |
| Python    | ETL scripts                                 |
| Airflow   | DAG orchestration                           |
| Docker    | Containerisation and environment isolation  |
| Snowflake | Data warehouse                              |
| Terraform | Infrastructure provisioning (Snowflake IaC) |
| S3        | Cloud storage (intermediate staging)        |

### 🗂️ Folder Structure

```text
Project-Snowflake/
│
├── airflow/
│   ├── dags/
│   │   ├── etl_snowflake_pipeline.py     ◀── Main DAG
│   │   └── sql_scripts/load_data.sql     ◀── SQL for Snowflake loading
│   ├── logs/
│   └── plugins/
│
├── assets/datasets/
│   ├── Original_file/                    ◀── Raw CSVs
│   ├── Transformed_full/                 ◀── Cleaned CSVs
│   └── Transformed_tables/               ◀── Split tables
│
├── python_scripts/
│   ├── transform_data_script.py          ◀── Cleans and transforms data
│   ├── split_data_into_tables.py         ◀── Splits data into logical tables
│   ├── upload_data_to_s3_bucket.py       ◀── Uploads to S3
│   └── run_sql_script.py                 ◀── Executes SQL (now used in DAG)
│
├── terraform/
│   ├── main.tf / variables.tf / modules/ ◀── IaC: schema, warehouse, tables, stage, integration
│
├── docker-compose.yaml                   ◀── Runs Airflow + Postgres
├── Makefile                              ◀── CLI for common tasks
├── .env                                  ◀── Env vars (used by Docker/Airflow)
└── README.md
```

---

## ⚙️ How It Works

### 🔄 DAG: `snowflake_etl_pipeline`

| Task ID               | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `transform_data`      | Cleans raw CSV using Pandas                            |
| `split_into_tables`   | Splits cleaned data by entity (e.g. orders, products)  |
| `upload_to_s3`        | Uploads split CSVs to the S3 bucket                    |
| `load_into_snowflake` | Executes SQL script to load staged data into Snowflake |

Airflow handles retries, logging, and task chaining automatically.

---

## 🏁 Setup Instructions

### ✅ 1. Clone & Environment Setup

```bash
git clone https://github.com/yourusername/project-snowflake.git
cd project-snowflake
cp .env.example .env  # Edit AWS keys and other secrets
```

### 🐳 2. Start Airflow with Docker Compose

```bash
make start
```

Runs Airflow, Postgres, and all required services.

### 🛠️ 3. Provision Snowflake Infrastructure with Terraform

```bash
cd terraform
terraform init
terraform apply
```

Creates:

* Warehouse
* Database
* Schema
* Tables
* External Stage
* Integration

### 🌐 4. Configure Airflow Connection in the UI

Open **Admin → Connections** in the Airflow web UI (`http://localhost:8080`):

* **Connection ID**: `snowflake_default`
* **Connection Type**: `Snowflake`

Fill in credentials & **Extra** like:

```json
{
  "account": "your_account",
  "warehouse": "your_warehouse",
  "database": "your_database",
  "role": "your_role"
}
```

---

## 🧪 Running the Pipeline

1. Place your raw CSV files into `assets/datasets/Original_file/`.
2. Trigger the **`snowflake_etl_pipeline`** DAG in the Airflow UI.
3. Monitor tasks as they progress: **transform ➝ split ➝ upload ➝ load**.
4. View the final data in Snowflake.

---

## 📈 Future Enhancements

* 🧪 Add data validation with **Great Expectations**
* 🔁 Enable scheduling (daily/weekly)
* 📁 Archive old processed files
* 🔐 Add secret manager integration (AWS Secrets Manager or HashiCorp Vault)
* 📊 Connect **Power BI** or **Streamlit** for reporting
* 📦 Convert this into a reusable **cookiecutter** template

---

## 👨‍💻 Author

**Abdirahman I.** — DataOps/DevOps Engineer
“I believe pipelines should be *reproducible, testable, and secure by design*.”

---

## 📜 Licence

MIT Licence — free to use, modify, and learn from.

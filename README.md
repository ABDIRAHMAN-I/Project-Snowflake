# ❄️ Project Snowflake – Scalable Data Pipeline with Airflow, Snowflake, S3, and Terraform

This project sets up an end-to-end data pipeline that transforms raw CSV data, splits it into domain-specific tables, uploads it to Amazon S3, and loads it into Snowflake — all automated through Apache Airflow and deployed using Terraform.

The pipeline is modular, production-ready, and built with repeatability and clarity in mind.

---

## 💡 Architecture Diagram

![Architecture](./images/snowflake_pipeline_architecture.png)

> A visual overview of the pipeline from data ingestion to Snowflake loading.

---

## 🚀 Overview

This project includes:

* Python scripts for data transformation, splitting and loading
* Airflow DAG to orchestrate the ETL flow
* Terraform code to provision snowflake warehouse, database, tables, etc
* Environment-managed secrets for security
* Docker-Compose to run airflow

---

## 💻 Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/project-snowflake.git
   cd project-snowflake
   ```

2. Spin up Airflow using Docker Compose:

   ```bash
   docker-compose up -d
   ```

3. Upload a CSV to:

   ```
   ./assets/datasets/Original_file/
   ```

4. Open Airflow UI:

   ```
   http://localhost:8080
   ```

5. Trigger the DAG:

   ```
   snowflake_etl_pipeline
   ```

---

## 🧱 Key Components

| Tool               | Role                                                                  |
| ------------------ | --------------------------------------------------------------------- |
| **Apache Airflow** | Orchestrates the ETL flow in DAG steps                                |
| **Snowflake**      | Data warehouse used for final storage and analysis                    |
| **S3**             | Temporary staging layer for processed CSVs                            |
| **Terraform**      | Provisions infrastructure like S3, IAM roles, and Snowflake resources |
| **Docker**         | Containerises Airflow and its components                              |
| **GitHub Actions** | Automates Docker builds, Terraform applies (optional)                 |

---

## 📁 Directory Structure

```
project-snowflake/
│
├── dags/                         # Airflow DAG definitions
├── python_scripts/              # Python ETL scripts
├── assets/
│   └── datasets/
│       ├── Original_file/       # Raw uploaded files
│       ├── Transformed_full/    # Cleaned and normalised output
│       └── Split_files/         # Domain-specific split tables
├── terraform/                   # Infrastructure as Code
├── docker-compose.yml           # Airflow local setup
├── .env                         # Snowflake and AWS credentials
└── README.md                    # This file
```

---

## 🔐 Environment Configuration

Your `.env` should include:

```env
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
SNOWFLAKE_ROLE=
```

---

## 🧺 Step-by-Step Guide

### 1. 🛠️ Configure Snowflake

Create the following manually or via Terraform:

* Database
* Schema
* Role with appropriate privileges
* Warehouse

> Optional: Use Terraform modules to automate this setup.

---

### 2. 📄 Upload a CSV to `Original_file`

Put your raw CSV in:

```
assets/datasets/Original_file/
```

---

### 3. 🥪 Run the Airflow Pipeline

* Open Airflow: `http://localhost:8080`
* Trigger DAG: `snowflake_etl_pipeline`

Pipeline Steps:

1. **transform\_data** – Cleans and normalises the data
2. **split\_into\_tables** – Splits it by domain (e.g., Customers, Orders, etc.)
3. **upload\_to\_s3** – Uploads files to your specified S3 bucket
4. **load\_into\_snowflake** – Loads files from S3 into Snowflake using `COPY INTO`

---

### 4. 📒 SQL File (load\_data.sql)

Ensure this file exists at:

```
/opt/airflow/dags/sql/load_data.sql
```

Example SQL snippet:

```sql
COPY INTO SALES_DATA
FROM @my_s3_stage
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"')
PATTERN = '.*sales.*.csv';
```

---

## ⚙️ Terraform Setup (Optional)

To provision S3, IAM, and Snowflake resources:

```bash
cd terraform
terraform init
terraform apply -var-file="terraform.tfvars"
```

---

## ✅ Result

Once everything is working, you should be able to query your cleaned and structured data directly in Snowflake!

Example:

```sql
SELECT * FROM CLEANED_SALES LIMIT 10;
```

---


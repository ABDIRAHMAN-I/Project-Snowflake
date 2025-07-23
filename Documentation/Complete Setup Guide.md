# 🏔️ Snowflake ETL Pipeline - Complete Setup Guide

A step-by-step guide to set up and run the end-to-end ETL pipeline with Airflow, Snowflake, and Terraform.

## 📋 Prerequisites

Before you begin, ensure you have the following installed and configured:

### Required Software
- **Docker Desktop** (latest version)
- **Docker Compose** (comes with Docker Desktop)
- **Terraform** (v1.0+)
- **Git**
- **Make** (for using Makefile commands)

### Required Accounts
- **AWS Account** with S3 access
- **Snowflake Account** (free trial available)

---

## 🚀 Step-by-Step Setup

### Step 1: Clone and Prepare the Project

```bash
# Clone the repository
git clone https://github.com/yourusername/project-snowflake.git
cd project-snowflake

# Create environment file from template
cp .env.example .env
```

### Step 2: Configure Environment Variables

Open the `.env` file and fill in your credentials:

```bash
# AWS Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=us-east-1
S3_BUCKET_NAME=your-snowflake-data-bucket

# Snowflake Configuration
SNOWFLAKE_ACCOUNT=your_account.region
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
SNOWFLAKE_ROLE=your_role

# Airflow Configuration
AIRFLOW_UID=50000
```

### Step 3: Create AWS S3 Bucket

1. Log into AWS Console
2. Navigate to S3 service
3. Create a new bucket with the name you specified in `S3_BUCKET_NAME`
4. Note the bucket name for later use

### Step 4: Start the Airflow Environment

```bash
# Initialize and start all services
make start

# Alternative: Use docker-compose directly
docker-compose up -d
```

This will start:
- Airflow Webserver (http://localhost:8080)
- Airflow Scheduler
- PostgreSQL database
- Redis (for task queuing)

**Wait 2-3 minutes** for all services to fully initialize.

### Step 5: Access Airflow Web UI

1. Open your browser and go to `http://localhost:8080`
2. Default login credentials:
   - Username: `airflow`
   - Password: `airflow`

### Step 6: Provision Snowflake Infrastructure with Terraform

```bash
# Navigate to terraform directory
cd terraform

# Initialize Terraform
terraform init

# Review the planned changes
terraform plan

# Apply the infrastructure
terraform apply
```

When prompted, type `yes` to confirm.

This creates:
- Snowflake warehouse
- Database and schema
- Data tables
- External stage for S3 integration
- Storage integration

### Step 7: Configure Snowflake Connection in Airflow

1. In Airflow UI, go to **Admin → Connections**
2. Click the **+** button to add a new connection
3. Fill in the following details:

```
Connection Id: snowflake_default
Connection Type: Snowflake
Host: your_account.region.snowflakecomputing.com
Schema: your_schema
Login: your_username
Password: your_password
Extra: {
  "account": "your_account.region",
  "warehouse": "your_warehouse", 
  "database": "your_database",
  "role": "your_role"
}
```

4. Click **Test** to verify the connection
5. Save the connection

### Step 8: Configure AWS Connection in Airflow

1. In Airflow UI, go to **Admin → Connections**
2. Add another connection:

```
Connection Id: aws_default
Connection Type: Amazon Web Services
Login: your_aws_access_key_id
Password: your_aws_secret_access_key
Extra: {
  "region_name": "us-east-1"
}
```

### Step 9: Prepare Your Data

1. Place your raw CSV files in the `assets/datasets/Original_file/` directory
2. Ensure your CSV files have proper headers and are well-formatted

### Step 10: Run the ETL Pipeline

1. In Airflow UI, navigate to **DAGs**
2. Find the `snowflake_etl_pipeline` DAG
3. Toggle it **ON** (if not already enabled)
4. Click on the DAG name to view details
5. Click **Trigger DAG** to start the pipeline

### Step 11: Monitor Pipeline Execution

1. Watch the DAG graph view as tasks complete:
   - **transform_data**: Cleans and transforms raw CSV
   - **split_into_tables**: Splits data into logical tables
   - **upload_to_s3**: Uploads processed files to S3
   - **load_into_snowflake**: Loads data into Snowflake tables

2. Click on individual tasks to view logs and troubleshoot any issues

### Step 12: Verify Data in Snowflake

1. Log into your Snowflake account
2. Navigate to your database and schema
3. Query your tables to verify data was loaded correctly:

```sql
-- Example queries
SELECT COUNT(*) FROM your_table_name;
SELECT * FROM your_table_name LIMIT 10;
```

---

## 🛠️ Useful Commands

### Docker Management
```bash
# Start all services
make start

# Stop all services
make stop

# View logs
docker-compose logs -f

# Restart a specific service
docker-compose restart airflow-webserver
```

### Terraform Management
```bash
# View current state
terraform show

# Destroy infrastructure (cleanup)
terraform destroy
```

### Troubleshooting
```bash
# Check Airflow scheduler logs
docker-compose logs airflow-scheduler

# Check webserver logs
docker-compose logs airflow-webserver

# Access Airflow container
docker-compose exec airflow-webserver bash
```

---

## 📊 Pipeline Overview

The ETL pipeline follows this flow:

1. **Raw Data** → CSV files in `Original_file/`
2. **Transform** → Clean and standardize data using Python/Pandas
3. **Split** → Separate into logical tables (orders, products, customers, etc.)
4. **Stage** → Upload to S3 as intermediate storage
5. **Load** → Copy from S3 into Snowflake tables using COPY commands
6. **Validate** → Verify data integrity and completeness

---

## 🔧 Configuration Tips

### Scaling Considerations
- Adjust Airflow worker count in `docker-compose.yaml`
- Configure Snowflake warehouse size based on data volume
- Set appropriate retry policies in DAG configuration

### Security Best Practices
- Use AWS IAM roles instead of access keys when possible
- Enable Snowflake MFA
- Rotate credentials regularly
- Use Airflow Variables for sensitive configuration

### Performance Optimization
- Use file compression for S3 uploads
- Configure Snowflake clustering keys for large tables
- Implement incremental loading for large datasets

---

## 🚨 Common Issues and Solutions

### Issue: Airflow won't start
**Solution**: 
```bash
# Check if ports are available
netstat -tulpn | grep :8080

# Reset Docker environment
docker-compose down -v
docker-compose up -d
```

### Issue: Snowflake connection fails
**Solution**:
- Verify account identifier format: `account.region`
- Check network connectivity and firewall settings
- Validate credentials in Snowflake console

### Issue: S3 upload fails
**Solution**:
- Verify AWS credentials and permissions
- Check S3 bucket exists and is accessible
- Ensure bucket region matches configuration

### Issue: DAG import errors
**Solution**:
```bash
# Check DAG syntax
docker-compose exec airflow-webserver python -m py_compile /opt/airflow/dags/etl_snowflake_pipeline.py

# Restart scheduler
docker-compose restart airflow-scheduler
```

---

## 📝 Project Structure Reference

```
Project-Snowflake/
├── airflow/
│   ├── dags/etl_snowflake_pipeline.py    # Main orchestration DAG
│   └── sql_scripts/load_data.sql         # Snowflake loading SQL
├── assets/datasets/
│   ├── Original_file/                    # Place raw CSV files here
│   ├── Transformed_full/                 # Cleaned data output
│   └── Transformed_tables/               # Split tables output
├── python_scripts/                       # ETL processing scripts
├── terraform/                            # Infrastructure as Code
├── docker-compose.yaml                   # Service orchestration
├── .env                                  # Environment configuration
└── Makefile                              # Convenience commands
```
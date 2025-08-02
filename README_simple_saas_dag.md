# Simple SaaS Sales Data Pipeline

## Overview

This Airflow DAG (`simple_saas_dag.py`) is a beginner-friendly data pipeline that demonstrates how to integrate Apache Airflow with PostgreSQL for processing SaaS sales data. The pipeline extracts data from a CSV file, loads it into PostgreSQL, and performs basic analytics.

## 📊 What This Pipeline Does

1. **Creates Database Table**: Sets up a PostgreSQL table structure for SaaS sales data
2. **Loads CSV Data**: Reads the SaaS-Sales.csv file and imports ~10,000 records into PostgreSQL
3. **Creates Analysis Views**: Generates pre-built SQL views for common business questions
4. **Runs Custom Analytics**: Executes Python-based analysis and prints insights
5. **Linear Workflow**: Follows a simple start → create → load → analyze → end pattern

## 🏗️ Pipeline Architecture



## 📁 Data Schema

The pipeline creates a `saas_sales` table with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| row_id | INTEGER | Unique row identifier |
| order_id | VARCHAR(50) | Order reference number |
| order_date | DATE | When the order was placed |
| contact_name | VARCHAR(100) | Customer contact person |
| country | VARCHAR(50) | Customer country |
| city | VARCHAR(50) | Customer city |
| customer | VARCHAR(100) | Company name |
| customer_id | INTEGER | Unique customer identifier |
| industry | VARCHAR(50) | Customer industry sector |
| segment | VARCHAR(50) | Business segment (SMB, Enterprise, etc.) |
| product | VARCHAR(100) | Product/service purchased |
| sales | DECIMAL(10,2) | Sales amount in dollars |
| quantity | INTEGER | Number of items ordered |
| discount | DECIMAL(5,2) | Discount percentage applied |
| profit | DECIMAL(10,2) | Profit amount in dollars |

## 🔧 Tasks Breakdown

### Task 1: `create_saas_table`
- **Type**: PostgresOperator
- **Purpose**: Creates the `saas_sales` table if it doesn't exist
- **SQL**: DDL statement with proper data types and constraints

### Task 2: `load_csv_data`
- **Type**: PythonOperator
- **Purpose**: Loads CSV data into PostgreSQL
- **Features**:
  - Reads SaaS-Sales.csv using pandas
  - Cleans and transforms column names
  - Converts date formats
  - Inserts data in 1000-record chunks for efficiency
  - Truncates existing data before loading (full refresh)

### Task 3: `run_simple_analysis`
- **Type**: PostgresOperator
- **Purpose**: Creates analytical views for business insights
- **Views Created**:
  - `sales_by_country`: Country-level sales performance
  - `top_products`: Best-selling products by revenue
  - `industry_performance`: Industry-wise customer and sales metrics

### Task 4: `analyze_data`
- **Type**: PythonOperator
- **Purpose**: Runs custom analysis and prints results
- **Analytics**:
  - Top 5 countries by sales
  - Monthly sales trends
  - Customer segment analysis
  - Returns summary metrics via XCom

## 🚀 Setup Instructions

### Prerequisites

1. **Apache Airflow** installed and running
2. **PostgreSQL** database server
3. **Python packages**: pandas, psycopg2-binary

```bash
pip install pandas psycopg2-binary
```

### Database Setup

1. Create a PostgreSQL database:
```sql
CREATE DATABASE airflow_practice;
```

2. Configure Airflow connection in the UI:
   - Go to Admin > Connections
   - Create new connection:
     - **Conn Id**: `postgres_default`
     - **Conn Type**: `Postgres`
     - **Host**: `localhost`
     - **Schema**: `airflow_practice`
     - **Login**: `your_username`
     - **Password**: `your_password`
     - **Port**: `5432`

### File Setup

1. Ensure the CSV file exists at the specified path:
   ```
   /Users/johankarim/Desktop/coding_project/python.daily/airflow/SaaS-Sales.csv
   ```

2. Place the DAG file in your Airflow DAGs folder:
   ```
   $AIRFLOW_HOME/dags/simple_saas_dag.py
   ```

## ⚙️ Configuration

### DAG Settings
- **Schedule**: Daily (`@daily`)
- **Start Date**: Yesterday (`days_ago(1)`)
- **Catchup**: Disabled
- **Retries**: 1 attempt with 5-minute delay
- **Owner**: data_engineer

### Customization Options

1. **Change CSV Path**: Update the `csv_file` variable in `load_csv_to_postgres()`
2. **Modify Chunk Size**: Adjust `chunk_size = 1000` for different batch sizes
3. **Add More Views**: Extend the SQL in `run_simple_analysis` task
4. **Custom Analytics**: Modify the `custom_analysis()` function

## 📈 Expected Output

When the pipeline runs successfully, you'll see:

1. **Database Table**: `saas_sales` with ~9,995 records
2. **Analysis Views**: 3 pre-built views for business intelligence
3. **Console Output**: Formatted analysis results in Airflow logs
4. **XCom Data**: Summary metrics available for downstream tasks

### Sample Analysis Output

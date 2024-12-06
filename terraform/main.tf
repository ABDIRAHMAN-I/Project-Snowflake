terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
      version = "0.99.0"
    }
  }
}


# resources 
resource "snowflake_warehouse" "warehouse" {
  name           = "WAREHOUSE DEMO_WH"
  warehouse_size = "XSMALL"
  auto_suspend = 300
  auto_resume = true
}

resource "snowflake_database" "database" {
  name = "GLOBAL_RETAIL_DB"
}

resource "snowflake_schema" "schema" {
  name     = "TRANSACTIONS_DATA"
  database = "GLOBAL_RETAIL_DB"
}



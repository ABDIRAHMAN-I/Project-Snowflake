terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
    }
  }
}


resource "snowflake_schema" "main" {
  name     = var.schema_name
  database = var.database_name
}

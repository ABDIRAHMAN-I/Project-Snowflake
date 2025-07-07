terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
    }
  }
}


resource "snowflake_database" "main" {
  name = var.database_name
}

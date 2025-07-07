terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
    }
  }
}


resource "snowflake_warehouse" "warehouse" {
  name           = var.warehouse_name
  warehouse_size = var.warehouse_size
  auto_suspend   = var.auto_suspend
  auto_resume    = var.auto_resume
}
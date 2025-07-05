terraform {
  required_providers {
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
      version = "~> 0.76"
    }
  }
}

provider "snowflake" {
  user              = var.snowflake_user
  password          = var.snowflake_password
  account_name      = var.snowflake_account
  organization_name = var.snowflake_org
  role              = var.snowflake_role
}



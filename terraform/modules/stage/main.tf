terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
    }
  }
}




resource "snowflake_stage" "s3_stage" {
  name                = "S3_STAGE"
  database            = var.database_name
  schema              = var.schema_name
  url                 = var.s3_bucket_url
  storage_integration = var.storage_integration_name
  comment             = "Stage to access S3 transformed data"
}

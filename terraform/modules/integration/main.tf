terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
    }
  }
}




resource "snowflake_storage_integration" "s3_integration" {
  name                      = "S3_INT"
  storage_provider          = "S3"
  enabled                   = true
  storage_aws_role_arn      = var.s3_snowflake_iam_role_arn
  storage_allowed_locations = [var.s3_bucket_url]
  comment                   = "Integration with S3 for external stage access"
}

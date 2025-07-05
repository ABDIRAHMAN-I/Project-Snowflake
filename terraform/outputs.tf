output "database_name" {
  value = snowflake_database.main.name
}

output "schema_name" {
  value = snowflake_schema.main.name
}

output "snowflake_s3_trust_policy" {
  value       = snowflake_storage_integration.s3_integration.storage_aws_external_id
  description = "Use this external ID when creating the IAM trust relationship for Snowflake."
}
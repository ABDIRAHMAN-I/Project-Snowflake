output "storage_integration_name" {
  value = snowflake_storage_integration.s3_integration.name
}

output "external_id" {
  value = snowflake_storage_integration.s3_integration.storage_aws_external_id
}

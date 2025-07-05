variable "snowflake_account" {
  description = "Snowflake account name (without .snowflakecomputing.com)"
  type        = string
}

variable "snowflake_org" {
  type = string
}

variable "snowflake_user" {
  description = "Snowflake login name"
  type        = string
}

variable "snowflake_password" {
  description = "Snowflake user password"
  type        = string
  sensitive   = true
}

variable "snowflake_role" {
  description = "Snowflake role to assume"
  type        = string
}

variable "snowflake_region" {
  description = "Region identifier for your Snowflake account"
  type        = string
}

variable "database_name" {
  default = "GLOBAL_RETAIL_DB"
}

variable "schema_name" {
  default = "SALES"
}

variable "warehouse_name" {
  description = "Name of the Snowflake warehouse"
  type        = string
  default     = "WAREHOUSE DEMO_WH"
}

variable "warehouse_size" {
  description = "Size of the Snowflake warehouse (e.g. XSMALL, SMALL, etc.)"
  type        = string
  default     = "XSMALL"
}

variable "auto_suspend" {
  description = "Time in seconds before auto-suspending the warehouse"
  type        = number
  default     = 300
}

variable "auto_resume" {
  description = "Whether the warehouse should auto-resume"
  type        = bool
  default     = true
}


variable "s3_snowflake_iam_role_arn" {
  description = "The ARN of the IAM role Snowflake will assume."
  type        = string
  default     = "arn:aws:iam::977098994448:role/SnowflakeS3AccessRole"
}

variable "s3_bucket_url" {
  description = "S3 bucket path Snowflake will read from"
  type        = string
  default     = "s3://my-snowflake-project-bucket0/transformed_data/"
}
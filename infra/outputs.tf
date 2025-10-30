output "vpc_id" {
  description = "ID of the VPC"
  value       = module.vpc.vpc_id
}

output "rds_endpoint" {
  description = "RDS instance endpoint"
  value       = module.rds.db_instance_endpoint
  sensitive   = true
}

output "rds_port" {
  description = "RDS instance port"
  value       = module.rds.db_instance_port
}

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = module.lambda.lambda_function_name
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket for CSV uploads"
  value       = module.lambda.s3_bucket_id
}

output "database_connection_info" {
  description = "Database connection information"
  value = {
    endpoint = module.rds.db_instance_endpoint
    port     = module.rds.db_instance_port
    database = var.db_name
    username = var.db_username
  }
  sensitive = true
}
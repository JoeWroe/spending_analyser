variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "eu-west-2"
}

variable "aws_profile" {
  description = "AWS profile to use"
  type        = string
  default     = "banking_apps_dev"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "spending-analyser"
}

variable "environment" {
  description = "Environment (dev, prod)"
  type        = string
  default     = "dev"
}

variable "csv_upload_bucket_name" {
  description = "S3 bucket name for CSV uploads"
  type        = string
  default     = "statement-csv-upload-bucket"
}

variable "lambda_timeout" {
  description = "Lambda function timeout in seconds"
  type        = number
  default     = 30
}

variable "lambda_runtime" {
  description = "Lambda runtime version"
  type        = string
  default     = "python3.11"
}

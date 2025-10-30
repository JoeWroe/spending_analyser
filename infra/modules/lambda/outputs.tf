output "lambda_function_arn" {
  description = "ARN of the Lambda function"
  value       = aws_lambda_function.statement_ingestor.arn
}

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.statement_ingestor.function_name
}

output "s3_bucket_id" {
  description = "ID of the S3 bucket"
  value       = aws_s3_bucket.statement_csv_bucket.id
}

output "s3_bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.statement_csv_bucket.arn
}
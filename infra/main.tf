provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

resource "aws_s3_bucket" "statement_csv_bucket" {
  bucket = "${var.environment}-statement-csv-upload-bucket"
}

resource "aws_iam_role" "statement_ingestor_execution_role" {
  name = "${var.environment}-statement-ingestor-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Effect = "Allow",
      Sid = ""
    }]
  })
}

resource "aws_iam_role_policy_attachment" "statement_ingestor_execution" {
  role       = aws_iam_role.statement_ingestor_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "statement_ingestor" {
  function_name = "${var.environment}-statement-ingestor"
  role          = aws_iam_role.statement_ingestor_execution_role.arn
  handler       = "statement_ingestor.ingest_statement"
  runtime       = var.lambda_runtime
  filename      = "${path.module}/lambda/statement_ingestor.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda/statement_ingestor.zip")
  timeout       = var.lambda_timeout
}

resource "aws_s3_bucket_notification" "statement_bucket_notification" {
  bucket = aws_s3_bucket.statement_csv_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.statement_ingestor.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = ""
    filter_suffix       = ".csv"
  }

  depends_on = [aws_lambda_permission.allow_s3]
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.statement_ingestor.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.statement_csv_bucket.arn
}

resource "aws_iam_role" "database_setup_execution_role" {
  name = "${var.environment}-database-setup-role"
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

  tags = {
    Name = "${var.environment}-${var.project_name}-database-setup-lambda-role"
  }
}

resource "aws_iam_role_policy_attachment" "database_setup_execution" {
  role       = aws_iam_role.database_setup_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

data "archive_file" "database_setup_zip" {
  type        = "zip"
  output_path = "${path.module}/../lambda/database_setup.zip"
  source_dir  = "/tmp/db_lambda_package"
}

resource "aws_lambda_function" "database_setup" {
  function_name = "${var.environment}-database-setup"
  role          = aws_iam_role.database_setup_execution_role.arn
  handler       = "database_setup.setup_database"
  runtime       = var.lambda_runtime
  filename      = data.archive_file.database_setup_zip.output_path
  source_code_hash = data.archive_file.database_setup_zip.output_base64sha256
  timeout       = var.lambda_timeout


  environment {
    variables = {
      DATABASE_URL = "postgresql://${var.db_username}:${var.db_password}@${var.db_endpoint}/${var.db_name}"
    }
  }

  tags = {
    Name = "${var.environment}-${var.project_name}-database-setup-lambda"
  }
}
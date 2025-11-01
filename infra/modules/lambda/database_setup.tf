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

resource "aws_iam_role_policy_attachment" "database_setup_vpc_execution" {
  role       = aws_iam_role.database_setup_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
}

resource "aws_security_group" "database_setup_lambda" {
  name_prefix = "${var.environment}-database-setup-lambda-"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.environment}-${var.project_name}-database-setup-lambda-sg"
  }
}

resource "aws_lambda_function" "database_setup" {
  function_name = "${var.environment}-database-setup"
  role          = aws_iam_role.database_setup_execution_role.arn
  handler       = "database_setup.setup_database"
  runtime       = var.lambda_runtime
  filename      = "${path.module}/../lambda/database_setup.zip"
  source_code_hash = filebase64sha256("${path.module}/../lambda/database_setup.zip")
  timeout       = var.lambda_timeout
  architectures = ["arm64"]

  vpc_config {
    subnet_ids         = var.private_subnet_ids
    security_group_ids = [aws_security_group.database_setup_lambda.id]
  }

  environment {
    variables = {
      DATABASE_URL = "postgresql://${var.db_username}:${var.db_password}@${var.db_endpoint}/${var.db_name}"
    }
  }

  tags = {
    Name = "${var.environment}-${var.project_name}-database-setup-lambda"
  }
}
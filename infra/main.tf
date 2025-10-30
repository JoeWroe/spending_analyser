provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

module "vpc" {
  source = "./modules/vpc"

  environment  = var.environment
  project_name = var.project_name
  aws_region   = var.aws_region
}

module "rds" {
  source = "./modules/rds"

  environment        = var.environment
  project_name       = var.project_name
  vpc_id             = module.vpc.vpc_id
  vpc_cidr_block     = module.vpc.vpc_cidr_block
  private_subnet_ids = module.vpc.private_subnet_ids

  db_instance_class          = var.db_instance_class
  db_engine_version          = var.db_engine_version
  db_allocated_storage       = var.db_allocated_storage
  db_max_allocated_storage   = var.db_max_allocated_storage
  db_name                    = var.db_name
  db_username                = var.db_username
  db_password                = var.db_password
  db_backup_retention_period = var.db_backup_retention_period
  db_backup_window           = var.db_backup_window
  db_maintenance_window      = var.db_maintenance_window
}

module "lambda" {
  source = "./modules/lambda"

  environment     = var.environment
  project_name    = var.project_name
  lambda_runtime  = var.lambda_runtime
  lambda_timeout  = var.lambda_timeout
  lambda_zip_path = "${path.module}/lambda/statement_ingestor.zip"

  db_endpoint = module.rds.db_instance_endpoint
  db_port     = module.rds.db_instance_port
  db_name     = var.db_name
  db_username = var.db_username
  db_password = var.db_password
}


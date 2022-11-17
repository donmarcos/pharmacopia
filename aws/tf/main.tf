provider "aws" {
    region = "us-west-2"
}

locals {
  bucket = aws_s3_bucket.pharmacopia_source_bucket.id
  account_id    = data.aws_caller_identity.current.account_id
  function = aws_lambda_function.processImage
  region = data.aws_region.current.name
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "pharmacopia_source_bucket" {
    bucket_prefix = "pharmacopia-source-"
    tags = {
        "About" = "Input bucket for pharmacopia"
    }
}

resource "aws_s3_bucket_public_access_block" "pharmacopia_source_bucket_private" {
  bucket = aws_s3_bucket.pharmacopia_source_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

output "pharmacopia_source_bucket" {
    value = aws_s3_bucket.pharmacopia_source_bucket.id
}

resource "aws_iam_policy" "processImage_policy" {
  name = "processImage_policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid = "AccessAll"
        Action = [
            "s3-object-lambda:List*",
            "s3-object-lambda:Get*",
            "comprehendmedical:*",
            "textract:*",
            "s3:Get*",
            "s3:List*"
        ]
        Effect = "Allow"
        Resource = "*"
      },
      {
        Sid = "AccessLogs"
        Action = ["logs:CreateLogStream", "logs:PutLogEvents", "logs:CreateLogGroup"]
        Effect = "Allow"
        Resource = [
          "arn:aws:logs:${local.region}:${local.account_id}:*",
        ]
      },
    ]
  })
}

resource "aws_iam_role" "processImage_role" {
  name = "processImage_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "sts:AssumeRole"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "test-attach" {
  role       = aws_iam_role.processImage_role.name
  policy_arn = aws_iam_policy.processImage_policy.arn
}

resource "aws_lambda_function" "processImage" {
  filename      = "${path.module}/processImage.zip"
  function_name = "processImage"
  handler       = "lambda_function.lambda_handler"
  role          = aws_iam_role.processImage_role.arn
  runtime       = "python3.9"
  environment {
    variables = {
        BUCKET = "${local.bucket}",
        REGION = "${local.region}"
    }
  }
  timeout = 60
}

resource "aws_lambda_function_url" "test_latest" {
  function_name      = aws_lambda_function.processImage.function_name
  authorization_type = "NONE"
}

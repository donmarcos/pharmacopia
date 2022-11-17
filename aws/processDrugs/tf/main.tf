provider "aws" {
    region = "us-east-1"
}

locals {
  account_id    = data.aws_caller_identity.current.account_id
  function = aws_lambda_function.processDrugs
  region = data.aws_region.current.name
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

resource "aws_iam_policy" "processDrugs_policy" {
  name = "processDrugs_policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid = "CloudWatchAccess"
        Action = [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ]
        Effect = "Allow"
        Resource = [
          "arn:aws:logs:${local.region}:${local.account_id}:*",
        ]
      },
      {
        Sid = "AccessLogs"
        Action = ["dataexchange:*"]
        Effect = "Allow"
        Resource = ["*"]
      },
    ]
  })
}

resource "aws_iam_role" "processDrugs_role" {
  name = "processDrugs_role"
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
  role       = aws_iam_role.processDrugs_role.name
  policy_arn = aws_iam_policy.processDrugs_policy.arn
}

resource "aws_lambda_function" "processDrugs" {
  filename      = "${path.module}/processDrugs.zip"
  function_name = "processDrugs"
  handler       = "lambda_function.lambda_handler"
  role          = aws_iam_role.processDrugs_role.arn
  runtime       = "python3.9"
  environment {
    variables = {
        REGION = "${local.region}",
        DATA_SET_ID = "b5c571b26671fc8b73a1146b140f0d75",
        REVISION_ID = "9ae2799c1227cc58002a946e27410dd3",
        ASSET_ID = "245ba9ec692792d750753ab605f388d2"
    }
  }
  timeout = 240
}
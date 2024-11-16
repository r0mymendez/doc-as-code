terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Configuración del bucket S3
resource "aws_s3_bucket" "s3_mkdocs" {
  bucket = "doc-as-code-mkdocs"

  tags = {
    Name        = "s3-doc-as-code-mkdocs"
    Environment = "documentation"
    Tool        = "MkDocs"
  }

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

# Configuración del sitio web estático para el bucket
resource "aws_s3_bucket_website_configuration" "s3_mkdocs_website" {
  bucket = aws_s3_bucket.s3_mkdocs.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

# Deshabilitar el bloqueo de políticas públicas en el bucket
resource "aws_s3_bucket_public_access_block" "s3_mkdocs_public_access" {
  bucket = aws_s3_bucket.s3_mkdocs.id

  block_public_acls       = false  # Permite ACLs públicas (por ejemplo, lectura pública)
  block_public_policy     = false  # Permite políticas públicas en el bucket
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Política para permitir el acceso público de solo lectura
resource "aws_s3_bucket_policy" "s3_mkdocs_policy" {
  bucket = aws_s3_bucket.s3_mkdocs.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.s3_mkdocs.arn}/*"
      }
    ]
  })
}


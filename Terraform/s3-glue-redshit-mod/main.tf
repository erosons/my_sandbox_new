# Define AWS provider
provider "aws" {
  region = "us-west-2"
}

# S3 bucket for staging raw data
resource "aws_s3_bucket" "etl_bucket" {
  bucket = "my-etl-data-bucket"
  
  tags = {
    Name        = "ETL Data Bucket"
    CostCenter  = "7894"
    Environment = "Production"
    Owner       = "Data Engineering Team"
  }
}

# Upload ETL script from local to S3
resource "aws_s3_object" "upload_etl_script" {
  bucket = aws_s3_bucket.etl_bucket.bucket
  key    = "scripts/etl_script.py"     # Path where the script will be stored in the bucket
  source = "${path.module}/scripts/etl_script.py"  # Local path to the ETL script
}

# IAM role for AWS Glue
resource "aws_iam_role" "glue_role" {
  name = "glue-etl-role"
  
  assume_role_policy = <<EOF
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "glue.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  }
  EOF

  tags = {
    Name        = "ETL Data Glue"
    CostCenter  = "7894"
    Environment = "Production"
    Owner       = "Data Engineering Team"
  }
}

# Glue ETL job definition
# Option: Use AWS Step Functions or Lambda to Manage Job Execution:
# To ensure that your Glue job runs after the Redshift cluster is fully available, you can set up an AWS Step Function or an AWS Lambda function that listens for CloudWatch events, waits for the Redshift cluster to become available, and then triggers the Glue job.
# Would you like an example of how to automate the Glue job execution using Step Functions or Lambda?
resource "aws_glue_job" "etl_job" {
  name        = "my-etl-job"
  role_arn    = aws_iam_role.glue_role.arn

  
  
  command {
    name            = "glueetl"
    script_location = "s3://my-etl-data-bucket/scripts/etl_script.py"
  }

  glue_version = "3.0"
  
  # Explicit dependency: Glue ETL job will only run once the Redshift cluster is provisioned
   # Combine all dependencies into one list
  depends_on = [
    aws_iam_role.glue_role,
    aws_redshift_cluster.etl_cluster
  ]

  tags = {
    Name        = "ETL Data Job"
    CostCenter  = "7894"
    Environment = "Production"
    Owner       = "Data Engineering Team"
  }
}

# Redshift cluster to store processed data
resource "aws_redshift_cluster" "etl_cluster" {
  cluster_identifier = "my-etl-cluster"
  node_type          = "dc2.large"  # Smallest node type
  master_username    = "admin"
  master_password    = "password123"
  cluster_type       = "single-node"

  tags = {
    Name        = "ETL Redshift Cluster"
    Environment = "Production"
    Owner       = "Data Engineering Team"
  }
}

Step 1 => pip install Boto3 which is the SDK for communicating with S3
Step 2 => Go to you AWS account => IAM => User=> Create a User with whatevername
Step 3 => Enable programmatic Access , for the permissions (Attach existing policies)
Step 4 => Search for AmazonS3FullAccess
Step 5 => Download the access details which is download.csv
Step 6 => Put the csv in your pwd
Step 7 => Install aws CLI , this will create a root .aws folder in your root dir
Step9 => Use CLI command see One note to setup your credential file and config file as shown below

Create a credential file with this setup

[default]
aws_access_key_id = **\*\***\*\*\*\***\*\***
aws_secret_access_key = **\*\*\*\***\*\*\*\***\*\*\*\***
aws_session_token = \***\*\*\*\*\***\*\*\*\*\***\*\*\*\*\***
Create a config file
[default]
region = ""
output = json (optional)
aws_access_key_id = **\*\***\*\*\*\***\*\***(optional)
aws_secret_access_key = **\*\***\***\*\***(optional)

Step 10 => Boto3 makes an API to S3 buckets in two main way

- Client which gives a low level access
- Resouces => object oriented way of accessing

AWS Glue

AWS Glue is a serverless and fully-managed Extract Transform and Load (ETL) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams. AWS Glue consists of a central metadata repository known as the AWS Glue Data Catalog, an ETL engine that automatically generates Python or Scala code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries. In this article, we’ll cover how to use AWS SDK for Python (Boto3 library) to interact with AWS Glue to start automating ETL jobs, crawlers and defining the Metadata Catalogs.

Crawler

AWS Glue allows you to use crawlers to populate the AWS Glue Data Catalog tables. Upon completion, the crawler creates or updates one or more tables in your Data Catalog. Extract, transform, and load (ETL) jobs that you define in AWS Glue use these Data Catalog tables as sources and targets. The ETL job reads from and writes to the data stores that are specified in the source and target Data Catalog tables.

Developing AWS Glue ETL jobs locally using a container before deploying to the cloud
https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/

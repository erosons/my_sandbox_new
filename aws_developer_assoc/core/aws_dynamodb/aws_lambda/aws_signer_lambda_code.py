"""
Set Up AWS Signer:

Create a signing profile in AWS Signer.
Ensure you have an S3 bucket to store the signed code.
Prepare Your Lambda Deployment Package:

Package your Lambda function code into a ZIP file.
Sign the Lambda Code Using AWS Signer:

Use the AWS Signer to create a signed version of your Lambda deployment package.
Below is an example code to demonstrate these steps using Boto3, the AWS SDK for Python:

Step 1: Set Up AWS Signer and Create a Signing Profile
Ensure you have already created a signing profile in the AWS Signer console. You can create a profile named MyLambdaSigningProfile.

Step 2: Prepare Your Lambda Deployment Package
Create a ZIP file of your Lambda function code. For example, assume the file is named lambda_function.zip


onfigure AWS Resources:

s3_bucket: Your S3 bucket name where the Lambda deployment package will be stored.
s3_key: The key (file name) of the Lambda deployment package in S3.
signed_s3_key: The key (file name) for the signed Lambda deployment package.
signing_profile_name: The name of the signing profile you created in AWS Signer.
region_name: The AWS region where your resources are located.
Upload the Lambda Deployment Package to S3:

Use the upload_file method to upload your Lambda deployment package (lambda_function.zip) to your S3 bucket.
Start the Signing Job:

Use the start_signing_job method to start a signing job with AWS Signer. This requires the source S3 bucket and key, the destination S3 bucket, and the signing profile name.
Wait for the Signing Job to Complete:

Use a loop to periodically check the status of the signing job until it either succeeds or fails.
Download the Signed Lambda Deployment Package:

Once the signing job succeeds, download the signed deployment package from the destination S3 bucket.
Clean Up:

Optionally, delete the uploaded and signed files from S3 to clean up.

"""

import boto3
import time
import os

# Configure AWS resources
s3_bucket = 'your-s3-bucket-name'
s3_key = 'lambda_function.zip'
signed_s3_key = 'signed_lambda_function.zip'
signing_profile_name = 'MyLambdaSigningProfile'
region_name = 'us-east-1'

# Initialize AWS clients
s3_client = boto3.client('s3')
signer_client = boto3.client('signer', region_name=region_name)

# Upload the Lambda deployment package to S3
s3_client.upload_file('lambda_function.zip', s3_bucket, s3_key)

# Start the signing job
signing_job_response = signer_client.start_signing_job(
    source={
        's3': {
            'bucketName': s3_bucket,
            'key': s3_key,
            'version': 'latest'
        }
    },
    destination={
        's3': {
            'bucketName': s3_bucket,
            'prefix': ''
        }
    },
    profileName=signing_profile_name
)

# Get the signing job ID
signing_job_id = signing_job_response['jobId']
print(f"Signing job started with Job ID: {signing_job_id}")

# Wait for the signing job to complete
def wait_for_signing_job(signing_job_id):
    while True:
        response = signer_client.describe_signing_job(jobId=signing_job_id)
        status = response['status']
        if status == 'Succeeded':
            print("Signing job succeeded.")
            return response['signedObject']['s3']
        elif status == 'Failed':
            raise Exception("Signing job failed.")
        else:
            print(f"Signing job status: {status}. Waiting...")
            time.sleep(10)

signed_object = wait_for_signing_job(signing_job_id)

# Download the signed Lambda deployment package from S3
signed_s3_key = signed_object['key']
s3_client.download_file(s3_bucket, signed_s3_key, 'signed_lambda_function.zip')
print(f"Signed Lambda deployment package downloaded as 'signed_lambda_function.zip'")

# Clean up: Remove the uploaded and signed files from S3 (optional)
s3_client.delete_object(Bucket=s3_bucket, Key=s3_key)
s3_client.delete_object(Bucket=s3_bucket, Key=signed_s3_key)
print("Cleaned up S3 bucket.")


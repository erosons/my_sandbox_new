import boto3
import json

def lambda_handler(event, context):
    # Initialize SageMaker client
    sagemaker = boto3.client('sagemaker')

    # Specify the training job parameters
    training_job_name = "sagemaker-training-job"
    training_image = "763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-training:2.3-cpu-py37-ubuntu18.04"  # TensorFlow CPU image
    role_arn = "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_SAGEMAKER_ROLE"
    input_data = "s3://your-bucket/path-to-your-training-data/"
    
    # Create the training job configuration
    create_training_params = {
        "TrainingJobName": training_job_name,
        "AlgorithmSpecification": {
            "TrainingImage": training_image,
            "TrainingInputMode": "File"
        },
        "RoleArn": role_arn,
        "InputDataConfig": [
            {
                "ChannelName": "train",
                "DataSource": {
                    "S3DataSource": {
                        "S3DataType": "S3Prefix",
                        "S3Uri": input_data,
                        "S3DataDistributionType": "FullyReplicated"
                    }
                }
            }
        ],
        "OutputDataConfig": {
            "S3OutputPath": "s3://your-bucket/path-to-your-output-data/"
        },
        "ResourceConfig": {
            "InstanceType": "ml.m5.large",
            "InstanceCount": 1,
            "VolumeSizeInGB": 50
        },
        "StoppingCondition": {
            "MaxRuntimeInSeconds": 3600
        }
    }
    
    # Create SageMaker training job
    response = sagemaker.create_training_job(**create_training_params)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Training job started successfully')
    }

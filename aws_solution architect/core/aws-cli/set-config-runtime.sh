#!/bin/bash
#chmod +x aws_setup.sh
# ./aws_setup.sh <AWS_ACCESS_KEY_ID> <AWS_SECRET_ACCESS_KEY> [AWS_DEFAULT_REGION]

# Assign passed variables or use default values
AWS_ACCESS_KEY_ID=$1
AWS_SECRET_ACCESS_KEY=$2
AWS_DEFAULT_REGION=${3:-us-east-1} # Default to us-east-1 if not provided

# Validate that the necessary variables are provided
if [ -z "$AWS_ACCESS_KEY_ID" ] || [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
    echo "Usage: $0 <AWS_ACCESS_KEY_ID> <AWS_SECRET_ACCESS_KEY> [AWS_DEFAULT_REGION]"
    exit 1
fi

# Configure AWS CLI using the provided credentials
aws configure set aws_access_key_id "$AWS_ACCESS_KEY_ID"
aws configure set aws_secret_access_key "$AWS_SECRET_ACCESS_KEY"
aws configure set default.region "$AWS_DEFAULT_REGION"

# Confirm configuration
echo "AWS CLI configured successfully!"
echo "Current configuration:"
aws configure list

# Optional: Display the generated credentials file
echo "Your AWS credentials have been saved to ~/.aws/credentials and ~/.aws/config"

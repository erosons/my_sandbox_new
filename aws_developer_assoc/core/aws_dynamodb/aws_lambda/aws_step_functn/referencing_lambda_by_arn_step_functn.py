import boto3
import json

# Initialize clients
lambda_client = boto3.client('lambda')
stepfunctions_client = boto3.client('stepfunctions')

# Lambda function ARNs
step1_arn = 'arn:aws:lambda:REGION:ACCOUNT_ID:function:Step1'
step2_arn = 'arn:aws:lambda:REGION:ACCOUNT_ID:function:Step2'
step3_arn = 'arn:aws:lambda:REGION:ACCOUNT_ID:function:Step3'

# State machine definition
state_machine_definition = {
    "Comment": "A simple state machine to trigger downstream steps",
    "StartAt": "Step1",
    "States": {
        "Step1": {
            "Type": "Task",
            "Resource": step1_arn,
            "Next": "Step2"
        },
        "Step2": {
            "Type": "Task",
            "Resource": step2_arn,
            "Next": "Step3"
        },
        "Step3": {
            "Type": "Task",
            "Resource": step3_arn,
            "End": True
        }
    }
}

# Create the state machine
response = stepfunctions_client.create_state_machine(
    name='SimpleStateMachine',
    definition=json.dumps(state_machine_definition),
    roleArn='arn:aws:iam::ACCOUNT_ID:role/service-role/StepFunctions-ExecutionRole'  # Replace with your IAM role ARN
)

print(f"State machine created with ARN: {response['stateMachineArn']}")

import json

"""Lambda Function: Step1"""
def lambda_handler(event, context):
    print("Step1 executed")
    return {
        'statusCode': 200,
        'body': json.dumps('Step1 completed1'),
        'nextStep': 'Step2'
    }

"""Lambda Function: Step2"""
def lambda_handler(event, context):
    print("Step1 executed")
    return {
        'statusCode': 200,
        'body': json.dumps('Step1 completed2'),
        'nextStep': 'Step2'
    }

"""Lambda Function: Step3"""
def lambda_handler(event, context):
    print("Step1 executed")
    return {
        'statusCode': 200,
        'body': json.dumps('Step1 completed3'),
        'nextStep': 'Step2'
    }

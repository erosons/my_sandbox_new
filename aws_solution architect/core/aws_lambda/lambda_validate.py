from lambda_function import lambda_handler

## We are basically retrying to simulate the deployment environment AWS
# By test if the lambda works locally

res = lambda_handler(None ,None)

print(res)
 # Deploying a Lambda function 
  means packaging your code, dependencies, setting the necessary configuration, and uploading everything to AWS Lambda to make it ready for execution. Here’s a breakdown of what this process typically entails:

   # Write Your Code: 
    First, you write the code for the task you want the Lambda function to perform. This could be in supported languages like Python, Node.js, Java, C#, Go, or PowerShell.

# Create a Deployment Package: 
   Your code and any dependencies need to be zipped into a deployment package. For some runtime environments, you can also use container images to package your Lambda function.
   
# Package Dependencies: 
   If your code relies on external libraries or modules, you need to include these in your deployment package.
    Create a package folder and install the required libraries needed in lambda function
    >> mkdir packlib
    >> pip install requests -t packlib

# Upload the Deployment Package: 
 Upload your zipped file or container image to Lambda, either through the AWS Management Console, AWS CLI, or using SDKs.

  # use case example
  To create new zip file >>>  zip -r aws_lambda.zip lamda_function_prac_one.py
  To update and exists zip file >>>  zip -g aws_lambda.zip lamda_function_prac_one.py

  # use case example two with external libraries
  To create the zip file along with the package dependences 
    - cd into the packlib folder >> cd packlib
        >> zip -r ../aws_lambda.zip .   Not it important the zip is created from inside package file and written to current directory
                                    Because we only want the external library packages only
        >> zip -g  aws_lambda.zip  lambda.py download.py  -> Update the zip file with codes
    - Upload to the AWS console lambda function      

   # use case example three define s3 permissions  for lambda to Integrate with AWS services
   - Update the role with the right policies and attached to the lambda function  
   - Update configuratiom
       - time out 
       - Memory 
       - Storage requirement             


   # Define Configuration Settings:
    You need to set various configuration options for your Lambda function:
        Runtime: The programming language and version.
        Handler: The function within your code that Lambda calls to begin execution.
        Memory and Timeout(Memory 128MB - 10GB): Set the amount of memory and the maximum execution time allowed for your function.
        Storage requirment: Storage required in the course of teh project  Storage 512MB -10GB 
        Environment Variables: Key-value pairs that your function can access as part of its execution environment.
        Roles and Permissions: IAM roles that grant your Lambda function permission to access AWS resources.

     Proceed to AWS console lambda with all set runtime config in place, Goto action and upload the .zip file

        Set Triggers (Optional): Configure what will trigger your Lambda function. This could be events from other AWS services like S3 buckets, DynamoDB tables, SNS topics, API Gateway, etc.

        Testing: After deployment, you typically test the Lambda function to ensure it operates as expected. This can be done through the AWS Management Console or programmatically.

        Monitor and Manage: Once deployed, you can monitor your function with AWS CloudWatch, configure alarms, and view logs to manage its performance and health.

        Versioning and Aliases: Manage different versions of your Lambda functions and use aliases to route traffic between versions.
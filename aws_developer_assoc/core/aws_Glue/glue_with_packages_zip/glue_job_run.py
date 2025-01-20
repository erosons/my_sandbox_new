import boto3

glue = boto3.client('glue')

response = glue.create_job(
    Name='my-glue-job',
    Role='your-glue-role',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://your-bucket/path-to-your-repo/glue_job_script.py',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--extra-py-files': 's3://your-bucket/path-to-packages/requests_package.zip',
    },
    GlueVersion='2.0'
)

# Start the job
glue.start_job_run(JobName='my-glue-job')

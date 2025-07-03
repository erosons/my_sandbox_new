import boto3

glue = boto3.client('glue')

response = glue.create_job(
    Name='your-glue-job',
    Role='your-glue-role',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://your-bucket/path-to-your-script.py',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--extra-py-files': 's3://your-bucket/path-to-your-repo/your-library.zip',
    },
    GlueVersion='2.0'
)

# Run the job
glue.start_job_run(JobName='your-glue-job')


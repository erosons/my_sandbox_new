# glue_job_script.py
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Add the S3 path to your custom module to the system path
sys.path.insert(0, 's3://your-bucket/path-to-your-repo/src/')

# Import your custom class
from my_class import MyClass

# Initialize Glue context and job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Instantiate and use your custom class
my_instance = MyClass("Hello, AWS Glue!")
my_instance.print_message()

job.commit()

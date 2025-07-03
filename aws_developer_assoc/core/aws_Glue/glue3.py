# glue_job_script.py
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Add the S3 path to your custom modules to the system path
sys.path.insert(0, 's3://your-bucket/path-to-your-repo/src/')

# Import your custom functions
from my_functions import function_one, function_two
from utils import helper_function

# Initialize Glue context and job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Call your custom functions
function_one()
function_two()
helper_function()

job.commit()

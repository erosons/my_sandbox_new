import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1764033762816 = glueContext.create_dynamic_frame.from_options(
    format_options={}, 
    connection_type="s3", 
    format="parquet", 
    connection_options={"paths": ["s3://amzn-s3-glue-poc/raw_data/orders.parquet"]}, 
    transformation_ctx="AmazonS3_node1764033762816"
    )

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(
    frame=AmazonS3_node1764033762816, 
    ruleset=DEFAULT_DATA_QUALITY_RULESET, 
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQuality_node1764033260100", 
        "enableDataQualityResultsPublishing": True}, 
        additional_options={
            "dataQualityResultsPublishing.strategy": "BEST_EFFORT", 
            "observations.scope": "ALL"}
            )
additional_options = {}

# Check if the Iceberg table exists
tables_collection = spark.catalog.listTables("samplesuperstor-db")
table_names_in_db = [table.name for table in tables_collection]
table_exists = "test2" in table_names_in_db

if table_exists:
    AmazonS3_node1764034059582_df = AmazonS3_node1764033762816.toDF()
    AmazonS3_node1764034059582_df.writeTo("glue_catalog.samplesuperstor-db.test2") \
        .tableProperty("format-version", "2") \
        .tableProperty("location", "s3://amzn-s3-glue-poc/iceberg/samplesuperstor-db/test2") \
        .tableProperty("write.parquet.compression-codec", "gzip") \
        .options(**additional_options) \
.append()
else:
    AmazonS3_node1764034059582_df = AmazonS3_node1764033762816.toDF()
    AmazonS3_node1764034059582_df        .writeTo("glue_catalog.samplesuperstor-db.test2") \
        .tableProperty("format-version", "2") \
        .tableProperty("location", "s3://amzn-s3-glue-poc/iceberg/samplesuperstor-db/test2") \
        .tableProperty("write.parquet.compression-codec", "gzip") \
        .options(**additional_options) \
.create()

job.commit()
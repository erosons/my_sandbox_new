import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkConf, SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark
from delta import *

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Delta Lake configurations
builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

# Custom log4j configuration
conf = SparkConf()
log4j_properties = """
log4j.rootCategory=INFO, console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.target=System.err
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n

# Set the logging level for various components
log4j.logger.org.apache.spark=INFO
log4j.logger.org.apache.hadoop=INFO
log4j.logger.io.delta=INFO
log4j.logger.org.apache.http=INFO
"""

# Apply the log4j properties
sc = SparkContext(conf=conf)
sc._jvm.org.apache.log4j.PropertyConfigurator.configure(log4j_properties)

spark = configure_spark_with_delta_pip(builder).getOrCreate()
glue_context = GlueContext(sc)
job = Job(glue_context)
job.init(args['JOB_NAME'], args)

# Read data from JDBC source
df = spark.read \
        .format('jdbc')\
        .option('url','jdbc:dremio:direct=dremio-cloud.com:443')\
        .option("encrypt", "true") \
        .option("dbtable", "schema.tablename")\
        .option("user", "?")\
        .option("password", "?")\
        .option("table", """ ? """)\
        .load()

df.createOrReplaceTempView("temp_table")

df2 = spark.sql("select * from temp_table")
df2.show(3) # Show data in temp_table

# Define Delta Lake table path
delta_table_path = "s3://your-bucket/path-to-delta-lake-table"

# Create new table and insert data from temp_table if it does not exist
if not spark.catalog.tableExists('spark_catalog.default.SMT_customer15'):
    df2.write.format("delta").saveAsTable("spark_catalog.default.SMT_customer15", path=delta_table_path)
else:   
    # Upsert (merge) data into the Delta Lake table
    deltaTable = DeltaTable.forPath(spark, delta_table_path)
    deltaTable.alias("target").merge(
        df2.alias("source"),
        "target.Account_No = source.Account_No AND target.ID = source.ID AND target.UsageDate = source.UsageDate AND target.filetrackid = source.filetrackid"
    ).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()

job.commit()

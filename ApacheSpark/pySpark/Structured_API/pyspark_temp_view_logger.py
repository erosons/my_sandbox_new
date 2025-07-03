from pyspark.sql import SparkSession
import os
from pyspark.sql.types import (
    StructField,
    StructType,
    ShortType,
    IntegerType,
    StringType,
    FloatType,
    BooleanType,
)

spark = SparkSession\
        .builder \
        .appName("Basics")\
        .getOrCreate() \

#################################################        
# Access the underlying log4j logging from Spark
#################################################

log4jLogger = spark._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)
http_logger = log4jLogger.LogManager.getLogger("org.apache.http")
http_logger.setLevel(log4jLogger.Level.DEBUG)  # Set to DEBUG to capture detailed logs

#####################
# Set the log levels
#####################
logger.setLevel(log4jLogger.Level.INFO)
logger.info("This is an informational message.")

# format 1
df = spark.read.csv(
    os.environ.get("SANDBOX_FILE"), header=True
)

# #Format 2
# df = spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(os.environ.get("SANDBOX_FILE"))


df.createOrReplaceTempView("SuperStoreData")
SQL="""
    SELECT *
    FROM SuperStoreData
    WHERE REGION = "East" OR  REGION = "West"
    Order by State asc
"""

spark.sql(SQL).show()

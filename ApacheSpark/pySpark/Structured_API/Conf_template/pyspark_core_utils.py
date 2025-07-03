from  pyspark.sql import SparkSession
import os

"""
Suppose you have a cluster with 10 nodes, each with 16 cores and 64 GB of RAM. Here's a way you could configure it:
Executors: 10 executors (one per node)
Cores per Executor: 5 cores per executor
Executor Memory: Calculate based on remaining system RAM, reserving about 10 GB per node for overhead, 
which leaves about 54 GB. Allocating around 20-24 GB per executor could be safe, ensuring there's 
enough memory for the operating system and other processes.
"""
def get_spark_session(env,appname):
    if env == "DEV":
        spark = (
        SparkSession.builder
            .master("local")
            #.master("spark://<remote_host>:7077") \
            .config("spark.executor.instances", "2")  # 2 executors per node x 5 nodes = 10 executors
            .config("spark.executor.cores", "5")      # 8 cores per executor
            .config("spark.executor.memory", "100g")   # 30 GB per executor
            .appName(appname)
            .getOrCreate()
        )
        
        return spark
    else:
        pass

def file_reader(Integration_runtime,format,file_src):
    
    #Format 1
    
    # df = spark.read \
    #     .option("header", True)\
    #     .option("inferSchema", "true")\
    #     .csv(os.environ.get("SANDBOX_FILE"))
    
    #Format 2
    df = Integration_runtime \
            .read \
            .format(format)\
            .option("header", True)\
            .option("inferSchema", "true")\
            .load(file_src)
    return df
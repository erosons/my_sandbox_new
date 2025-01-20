from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings
from pyflink.table.window import Tumble
from pyflink.table.expressions import col, lit
from pyflink.datastream.connectors import FileSink, OutputFileConfig
from pyflink.table.descriptors import Schema, OldCsv, FileSystem
from pyflink.common.typeinfo import Types
from pyflink.common.serialization import SimpleStringEncoder


""""
>>> pip install apache-flink pyarrow
Create a Python script for the Flink job. This script will:

    Read from a source (e.g., a socket or Kafka; this example will use a socket for simplicity).
    Apply a time window of 3 minutes.
    Write the aggregated results to S3 in Parquet format.

pip install apache-flink pyarrow

Kafka or Other Sources: Replace the socket source with a Kafka source or any other source as per your actual data ingestion requirements.
S3 Configuration: Ensure your Flink environment is configured to access Amazon S3. This typically involves setting the appropriate Hadoop configurations for S3 access, such as fs.s3a.access.key, fs.s3a.secret.key, and others in the flink-conf.yaml or through environment variables.
Environment Settings: If running this job on a cluster or with specific performance configurations, adjust the parallelism, memory configurations, and other operational parameters as needed.

Step 4: Execution

Run your Python script on your local machine or a Flink cluster configured to handle Python jobs. Ensure that the network settings allow connections to your data source and S3.

This script outlines how to create a Flink job in Python with time-windowed processing and output to S3. Adjust the details according to your specific infrastructure and data schema requirements.

"""

# Initialize the StreamExecutionEnvironment
env = StreamExecutionEnvironment.get_execution_environment()
env_settings = EnvironmentSettings.in_streaming_mode()
t_env = StreamTableEnvironment.create(env, environment_settings=env_settings)

# Define the source, here using a socket for simplicity
# In practice, replace this with a Kafka source or another appropriate source
hostname = "localhost"
port = 9999
t_env.connect(FileSystem().path(f'socket://{hostname}:{port}')) \
    .with_format(OldCsv()) \
    .with_schema(Schema().field("data", Types.STRING())) \
    .create_temporary_table("source_table")

# Convert table to a datastream for windowing and watermarking
table = t_env.from_path("source_table")
windowed_table = table.window(Tumble.over(lit(3).minutes).on(col("proctime")).alias("w")) \
    .group_by(col("w")) \
    .select(col("data").count)

# Define the sink - output to S3 as Parquet files
output_path = "s3://your-bucket-name/your-output-path/"
t_env.connect(FileSystem().path(output_path)) \
    .with_format(OldCsv()) \
    .with_schema(Schema().field("count", Types.LONG())) \
    .create_temporary_table("sink_table")

windowed_table.execute_insert("sink_table").wait()

# Execute the job
env.execute("Python Flink S3 Parquet Sink")

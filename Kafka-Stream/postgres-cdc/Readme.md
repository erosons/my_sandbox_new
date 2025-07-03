## Setup your PostgresDB for CDC

SELECT * FROM pg_settings where name ='wal_level' -> the currents of on the postgres Server
Update the Postgres.conf file 
  -> WRITE AHEAD LOG
  
# Change wal_level from replica to logical

In PostgreSQL, the wal_level parameter determines the amount of information to be written to the Write-Ahead Logging (WAL). This setting is crucial for data replication and recovery processes. It's particularly important when you are implementing Change Data Capture (CDC) mechanisms, as these often rely on WAL to propagate changes.
Understanding wal_level

The wal_level setting in PostgreSQL can be configured to several different levels, affecting the volume of information recorded in the WAL and thus influencing the system’s ability to support certain features like point-in-time recovery and logical replication:

    Minimal: This level causes the minimal amount of data to be logged, sufficient for crash recovery or physical replication only. It is not suitable for point-in-time recovery or logical replication.

    Replica (formerly archive): At this level, enough data is logged to support WAL archiving and replication, including running read replicas. It supports point-in-time recovery but not logical replication.

    Logical: This is the highest level of WAL logging. It supports logical replication and decoding, which are required for sophisticated CDC mechanisms. At this level, all changes that could potentially be visible to any logical replication subscriber are logged.

# Configuring wal_level for CDC

To enable logical replication for CDC, you need to set the wal_level to logical. This setting ensures that all necessary information for logical decoding is available in the WAL logs, which is essential for capturing changes in the database state.

Here’s how you can configure this setting:

    Via postgresql.conf:
        Locate your PostgreSQL configuration file (postgresql.conf), which is usually found in the PostgreSQL data directory.
        Change the wal_level parameter:

        conf

    wal_level = logical

    Save the file and restart your PostgreSQL server for the change to take effect.

# Using SQL command:

    You can also change this setting on the fly using SQL if your system allows for reloading configuration parameters:

    sql

       SELECT * FROM pg_settings where name ='wal_level'
        ALTER SYSTEM SET wal_level = 'logical';
        SELECT pg_reload_conf();

        This method changes the setting and reloads the configuration without needing to restart the database, but the change will only take effect at the next database restart.

# Considerations

    Performance Impact: Increasing the wal_level from minimal to logical can have a performance impact on your system due to the additional logging overhead. Monitor your system's performance after making this change, especially if it is a high-traffic database.

    Disk Usage: Higher levels of WAL logging increase disk usage. Ensure that your system has adequate disk space to accommodate the increased WAL volume, and consider implementing appropriate WAL archiving strategies.

    Replication and Recovery: If you are using logical replication or require point-in-time recovery, setting wal_level to logical is necessary. This setup supports various advanced use cases, including bidirectional replication and streaming changes to external systems for real-time updates or audits.

Adjusting the wal_level parameter is a critical step in configuring PostgreSQL for CDC, enabling detailed tracking of changes and facilitating advanced replication features. Make sure to assess the impacts carefully and adjust your database maintenance routines accordingly to handle the increased workload and storage requirements.


## DEBEZIUM CONNECTOR USER PERMISSION (create user with highest level of permission)

- User must have Replication privileges in the database to add the Table to to a publication
- User must have Create priviledes on the database to add publications.
- User must have SELECT privileges on the tables to copy the initial table data

# A publication for postgres
    Is essential a group of tables whoses data changes are intendeed to be replicated through logical

#  Deploy your Kafka Environment with - Docker compose

- /home/samson/Desktop/my_sandbox_new/Kafka-Stream/postgres-cdc

# Launch your Kafka Manager : localhost:9000

# Setup Custom Producer and Consumer:
 - pip install kafka-python


# Sink and Source setup -> Targeting schema Registry

Launch an extension in Vscode called Thunder Client ->  works like Postman
- # Pass in Debezium URL for testing -> localhost:8083
    -> send a get request to ensure response is 200K -> should return kafka config
- # Post source and Sink connector configuration json payload for the target postgres
- # Write Glue, Python script  

# Note if all goes, since have enabled CDC on the server, as soon as we connect the debezium, a topic ,should autmatically show up
  in Kafka topic list
  >> consumer.topics()


{
  "name": "s3-sales-sink",
  "config": {
    "connector.class": "io.confluent.connect.s3.S3SinkConnector",
    "tasks.max": "1",
    "topics": "src.public.factinternetsales_streaming",
    "s3.bucket.name": "kafka-bucket",
    "s3.part.size": "5242880",
    "flush.size": "3",
    "aws.secret.access.key": "${env:AWS_SECRET_ACCESS_KEY}",
    "aws.access.key.id": "${env:AWS_ACCESS_KEY_ID}",
    "store.url": "http://minio:9000",
    "key.converter": "io.confluent.connect.avro.AvroConverter",
    "value.converter": "io.confluent.connect.avro.AvroConverter",
    "key.converter.schemas.enable": true,
    "value.converter.schemas.enable": true,
    "key.converter.schema.registry.url": "http://your-schema-registry-url:8081",
    "value.converter.schema.registry.url": "http://your-schema-registry-url:8081",
    "format.class": "io.confluent.connect.s3.format.parquet.ParquetFormat",
    "storage.class": "io.confluent.connect.s3.storage.S3Storage",
    "schema.compatibility": "NONE"
  }
}


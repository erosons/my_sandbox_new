# Create a directory to store the JAR files
mkdir delta-lake-jars
cd delta-lake-jars

# Download Delta Core JAR (version 1.0.0 as an example)
wget https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.0/delta-core_2.12-1.0.0.jar

# Download Delta Storage S3 JAR (version 1.0.0 as an example)
wget https://repo1.maven.org/maven2/io/delta/delta-storage-s3_2.12/1.0.0/delta-storage-s3_2.12-1.0.0.jar

wget https://repo1.maven.org/maven2/io/delta/delta-storage-s3-dynamodb/4.0.0rc1/delta-storage-s3-dynamodb-4.0.0rc1.jar

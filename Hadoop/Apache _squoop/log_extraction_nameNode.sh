
#!/bin/bash

# Configuration Variables
LOG_FILE="/var/log/hadoop-hdfs/hdfs-namenode.log"
OUTPUT_FILE="namenode_logs.csv"
DB_NAME="hadoop_logs"
DB_USER="your_username"
DB_PASS="your_password"
DB_TABLE="NameNodeLogs"

# Ensure the output file does not already exist
rm -f $OUTPUT_FILE

# Extract relevant log parts (customize the awk command according to your log format)
awk '{print $1","$2","substr($0, index($0,$5))}' $LOG_FILE > $OUTPUT_FILE

# Load data into MySQL
# -u: username, -p: password (prompt if not provided here for security reasons), -D: database
mysql -u $DB_USER -p$DB_PASS -D $DB_NAME -e "
    LOAD DATA LOCAL INFILE '"$OUTPUT_FILE"'
    INTO TABLE $DB_TABLE
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    (log_date, log_time, log_message);
"

# Clean up if necessary
rm -f $OUTPUT_FILE

echo "Logs have been loaded into the database."

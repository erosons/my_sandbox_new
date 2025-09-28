"""
Extracting high volume data ingestion or Streaming data ingestion -> Using Binary log replication can be an efficient way.
the bin log file capture, or keeps record of every ops on db  depending on how its configured
CDC that happens in on DB such insert Update, create.
Commercial Open source tools- Apache Kafka,Debezium can be used
"""
import configparser
from pymysqlreplication import BinLogStreamReader, event, row_event
import pymysqlreplication
import pandas as pd
from ingesting_to_S3 import upload_file, bucket_name


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")


# get connection of mysql
mysql_conn = {
    "host": hostname,
    "port": int(port),
    "user": username,
    "passwd": password

}

"""
Reading bin log
"""
server_id = 1
log_file = "/var/lib/mysql/mysql-bin.000005"
log_pos = 4
tables = "Orders"
"""
stream = BinLogStreamReader(connection_settings=mysql_conn, server_id=server_id, only_events=[
                            row_event.DeleteRowsEvent, row_event.WriteRowsEvent, row_event.UpdateRowsEvent], log_file=log_file, log_pos=log_pos, resume_stream=True, blocking=True, only_tables=tables, slave_heartbeat=10)
"""
stream = BinLogStreamReader(connection_settings=mysql_conn, server_id=server_id, only_events=[
                            row_event.DeleteRowsEvent, row_event.WriteRowsEvent, row_event.UpdateRowsEvent],
                            resume_stream=True, log_pos=4, log_file=log_file)

"""
Writing the output of logfile into a csv
"""

order_events = []
for bin_logevent in stream:
    for rows in bin_logevent.rows:
        if bin_logevent.table == tables:
            event = {}
            if isinstance(bin_logevent, row_event.DeleteRowsEvent):
                event['actions'] = "Delete"
                event.update(rows['values'].items())
            elif isinstance(bin_logevent, row_event.UpdateRowsEvent):
                event['actions'] = "Update"
                event.update(rows['values'].items())
            elif isinstance(bin_logevent, row_event.WriteRowsEvent):
                event['actions'] = "Insert"
                event.update(rows['values'].items())
            order_events.append(event)
stream.close()

"""
Load the data into a csv file and upload into an S3 bucket
"""
filename = 'bin_log.csv'
bin_log_extract = pd.DataFrame(order_events)

"""
To output a commpressed file instead of csv

compression =dict(method='zip',archive_name='out.csv')
bin_log_csv.iloc[:,1:].to_csv('out.zip',index=False,compression=compression)
"""

# remove the first column of the dataFrame and write to csv file
bin_log_extract.iloc[:, 1:].to_csv(filename, index=False, header=None, sep='|')

"""
This is were we upload the file to S3 BUCKET
"""
upload_file(filename, bucket_name, object_Name=filename)

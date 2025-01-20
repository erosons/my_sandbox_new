from kafka import kafkaPoducer
import psycopg2
import json
from time import sleep


prod-client = KafkaConsumer('awskafkatopic1',bootstrap_servers=[''])
for msg in consumer:
    rec_data = msg.value.decode('utf-8')
    r = rec_data.replace('"','')
    record = r.strip('\\n')
    print(records)
    record_list:list = record.split(',')
    
# Establish the connection to the database
with psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
) as conn:
    # Create a cursor object
    with conn.cursor() as cur:
        cur.execute(sql)
        conn.commit()

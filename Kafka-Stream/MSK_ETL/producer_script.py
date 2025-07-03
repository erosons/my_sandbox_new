from kafka import KafkaProducer
import json
import pandas as pd
from time import sleep

v={
    "key1": "value1",
    "key2": 1234,
    "key3": True
}

prodclient = KafkaProducer(bootstrap_servers=['b-3.democluster1.vfyg6o.c18.kafka.us-east-1.amazonaws.com:9098'], api_version=(0,11,5)
                           )
prodclient.send('awskafkatopic1',json.dumps(v).encode('utf-8'))
sleep(2)
prodclient.flush()
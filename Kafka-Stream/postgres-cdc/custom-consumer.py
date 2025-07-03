# import kafka producer from the kafka library
from kafka import KafkaConsumer
import json

# Define server with
boostrap_server = ['localhost:29092']

# topic Nmae where the message will publish
topicName = 'source.public.order_details'

#initilize consumer
consumer = KafkaConsumer(topicName,bootstrap_servers = boostrap_server,auto_offset_reset='earliest',group_id = 'orders-group')

#read and print mesage from topic by consumer
for msg in consumer:
    # Print message
    #print("Topic Name {}, Mesage {}".format(msg.topic,msg.value))
     print(json.load(msg.value))
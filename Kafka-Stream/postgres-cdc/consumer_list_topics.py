# import kafka producer from the kafka library
from kafka import KafkaConsumer

# Define server with
boostrap_server = ['localhost:29092']

# topic Nmae where the message will publish
topicName = 'source-order_details-connector'

#initilize consumer
consumer = KafkaConsumer(topicName,bootstrap_servers = boostrap_server,auto_offset_reset='earliest')

# #read and print mesage from topic by consumer
# for msg in consumer:
#     # Print message
#     print("Topic Name {}, Mesage {}".format(msg.topic,msg.value))
consumer.topics()
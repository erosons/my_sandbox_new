# import kafka producer from the kafka library
from kafka import KafkaProducer

# Define server with
boostrap_server = ['localhost:29092']

# topic Nmae where the message will publish
topicName = 'test'

#initilize producer
producer = KafkaProducer(bootstrap_servers = boostrap_server)

#Publish text in define topic

producer.send(topicName, b'Second ,message')

# Print message
print('Message sent')
from confluent_kafka import Consumer, KafkaException

# Kafka Consumer configuration
conf = {
    'bootstrap.servers': 'your-msk-broker-endpoint:9092',  # MSK broker endpoint
    'group.id': 'your-consumer-group',  # Consumer group ID
    'auto.offset.reset': 'earliest',  # Start reading at the earliest message
    'security.protocol': 'SASL_SSL',  # Depending on your configuration
    'sasl.mechanism': 'AWS_MSK_IAM',  # If using IAM for authentication
    'sasl.username': 'your-access-key-id',
    'sasl.password': 'your-secret-access-key',
    'ssl.ca.location': '/path/to/your/ca-cert.pem',  # Path to CA certificate if required
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to the topic
topic = 'your_topic_name'
consumer.subscribe([topic])

try:
    while True:
        # Poll for a message
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            # Properly received a message
            print(f'Received message: {msg.value().decode("utf-8")}')

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    pass

finally:
    # Close down consumer to commit final offsets.
    consumer.close()

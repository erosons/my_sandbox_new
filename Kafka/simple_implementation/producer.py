from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Simulate sending noisy data
for _ in range(100):
    data = {'value': random.gauss(50, 10)}  # Normal data with some noise
    producer.send('raw-data', data)
    time.sleep(1)

producer.flush()

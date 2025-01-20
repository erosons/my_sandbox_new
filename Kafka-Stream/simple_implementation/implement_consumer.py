from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'raw-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

mean = 50
std_dev = 10

for message in consumer:
    data = message.value
    if mean - std_dev <= data['value'] <= mean + std_dev:
        print("Filtered Data:", data)
    else:
        print("Noisy Data Detected, Ignored:", data)

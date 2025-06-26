from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ['501', '502', '503']
users = ['101', '102', '103']

for _ in range(10):
    message = {
        "user_id": random.choice(users),
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
        "event": "view",
        "product_id": random.choice(products)
    }
    producer.send('clickstream', message)
    print(f"Produced: {message}")
    time.sleep(1)

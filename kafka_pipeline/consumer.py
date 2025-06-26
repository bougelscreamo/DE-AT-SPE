from kafka import KafkaConsumer
import json
import psycopg2
from collections import defaultdict

consumer = KafkaConsumer(
    'clickstream',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

conn = psycopg2.connect(
    dbname='kafka_db', user='kafkauser', password='kafkapass', host='localhost'
)
cur = conn.cursor()

view_counts = defaultdict(int)

try:
    for msg in consumer:
        data = msg.value
        if data["event"] == "view":
            product_id = data["product_id"]
            view_counts[product_id] += 1

            cur.execute("""
                INSERT INTO product_views (product_id, view_count)
                VALUES (%s, %s)
                ON CONFLICT (product_id) DO UPDATE
                SET view_count = product_views.view_count + 1;
            """, (product_id, 1))
            conn.commit()
            print(f"Stored view for product {product_id}")
except Exception as e:
    print("Error processing message:", e)
finally:
    consumer.close()
    conn.close()

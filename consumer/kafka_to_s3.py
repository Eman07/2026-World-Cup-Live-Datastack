import json
import os
import boto3
from kafka import KafkaConsumer
from datetime import datetime, timezone

# AWS S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name=os.environ['AWS_DEFAULT_REGION']
)

BUCKET = os.environ['AWS_BUCKET_NAME']

# Topic → S3 prefix and key field mapping
TOPIC_CONFIG = {
    "match-events":  {"prefix": "match_events",  "key_field": "match_id"},
    "player-scores": {"prefix": "player_scores", "key_field": "player_id"},
}

# Kafka consumer — reads from all topics
consumer = KafkaConsumer(
    *TOPIC_CONFIG.keys(),
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=10000,
    group_id='wc2026-s3-consumer-v3'
)

print("Connected to Kafka — reading messages...")

for message in consumer:
    topic  = message.topic
    record = message.value
    config = TOPIC_CONFIG[topic]
    key_value = record[config["key_field"]]
    ts = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f')
    key = f"{config['prefix']}/{key_value}/{ts}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(record).encode('utf-8')
    )
    print(f"Written: {key}")

consumer.close()
print("Done — check your S3 bucket")
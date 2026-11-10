from kafka import kafkaConsumer
import json
from database import  create_database, save_customer

create_database()
consumer=kafkaConsumer(
"customer_topic",
bootstrap_servers="localhost:9092",
auto_offset_rests="earliest",
enable_auto_commit =True,
group_id="customer_consumer_group",
value_deserializer=lamda v: json.loads(v.decode())
)

print("waiting for consumer events....")
for message in consumer:
    customer =message.value

    print("\n===EVENT RECEIVED FROM KAFKA===")
    print ("Original:",customer)

    transformed=[
    "CUSTOMER_NO":customer["customer_id"],
    "CUSTOMER_NAME":customer["name"],
    "EMAIL_ADRESS":customer["email"],
        "LOCATION":customer["city"],
    ]

print("Transfomed:",transfomed)

save_customer(transfomed)
print("Customer saved to SQLite database.")
            
        

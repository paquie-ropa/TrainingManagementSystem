from fastapi import FastAPI
from kafka import KafkaProducer
import json

app=FastAPI(title="Enterprise Intergration API")

producer=KafkaProducer(
    bootstrap_servers="Localhost:9092",
    value_serializer=lambda v:json.dumps(v).encode("utf-8")
)

@app.get("/")
def home():
    return {"message":"Enterprise Intergration API is running"}

@app.post("/customer")
def create_customer(customer:dict):
    print("/n===FASTAPI GATEWAY==")
    print( "Customer received:",customer)

    producer.send ("customer_topic",customer )
    producer.flush

    print("Event published to kafka")

    return{"message":"Customer event published successfully",
    "customer":customer}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("api:app", reload=True)
    
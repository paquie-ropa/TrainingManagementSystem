import requests

customers=[
    {"customer_id":1001, "name":"John Smith","emal":"john@gmail.com","city":"Johannesburg"},
    {"customer_id":1002, "name":"Mary Jones","emal":"mary@gmail.com","city":"Pretoria"},
        {"customer_id":1003, "name":"David Brown","emal":"david@gmail.com","city":"Cape Town"},
            {"customer_id":1004, "name":"Sarah Williams","emal":"sarah@gmail.com","city":"Durban"}

                
]
for customer in customer:
    print("\nSending customer:",customer)
    response=requests.post(
        "http:\\127.0.0.1.8000\customer"
        json=customer
    )
    print("Response:",response.json())


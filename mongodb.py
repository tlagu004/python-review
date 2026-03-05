from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
MONGO_URL = os.environ.get("MONGO_URL")
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASS")
MONGO_CLUSTER_URL = os.environ.get("MONGO_CLUSTER_URL")
client=MongoClient(MONGO_URL)
db = client["netlify"]
collection = db["users"]
user1 = {
    "firstName":"john",
    "lastName":"doe",
    "email":"jdoe305@gmail.com"
}
result1=collection.insert_one(user1)
print(client)
print(collection)
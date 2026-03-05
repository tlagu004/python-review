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
users = [
    {
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jsmith_dev@outlook.com",
        # "username": "janey_codes"
    },
    {
        "firstName": "Carlos",
        "lastName": "Rodriguez",
        "email": "c.rodriguez@miami.edu",
        # "username": "crod_305"
    },
    {
        "firstName": "Aisha",
        "lastName": "Khan",
        "email": "aisha.k@techcorp.io",
        # "username": "ak_cloud"
    },
    {
        "firstName": "Liam",
        "lastName": "O'Connor",
        "email": "liam.oconnor@protonmail.com",
        # "username": "luckyliam"
    },
    {
        "firstName": "Yuki",
        "lastName": "Tanaka",
        "email": "y.tanaka@global.jp",
        # "username": "yuki_t"
    }
]
result1=collection.insert_many(users)
findJane = collection.find({"firstName":"john"})
print(findJane)
# print(client)
# print(collection)
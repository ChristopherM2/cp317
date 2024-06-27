import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

mongo = os.getenv("MONGO")
client = pymongo.MongoClient(mongo)
db = client["Home"]
users = db["Users"]
groups = db["Groups"]

print(db.list_collection_names())

user = {
    "Name": "Shayan Dhillon",
    "ID": 2
}

group = {"Users": [1,2]}
users.insert_one(user)
groups.insert_one(group)

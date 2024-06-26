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
    "Name": "Christopher Matheson",
    "ID": 1
}
users.insert_one(user)

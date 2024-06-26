import pymongo
from dotenv import load_dotenv
import os
load_dotenv()
print("meow")
mongo = os.getenv("MONGO")
client = pymongo.MongoClient()
db = client["Home"]
users = db["Users"]
groups = db["Groups"]


print(db.list_collection_names())
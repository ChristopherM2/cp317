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


def create_user(name):
    id = users.count_documents({}) + 1
    users.insert_one({
        "name": name,
        "id": id,
    })
    return id


def create_group(name):
    gid = groups.count_documents({}) + 1
    groups.insert_one({
        "name": name,
        "users": [],
        "gid": gid,
    })
    return gid


def add_user_to_group(uid, gid):
    user = users.find_one({"id": uid})
    group = groups.find_one({"gid": gid})
    if user is None or group is None:
        return False
    group["users"].append(uid)
    groups.update_one({"gid": gid}, {"$set": group})
    return True

def get_user(uid):
    return users.find_one({"id": uid})
def get_group(gid):
    return groups.find_one({"gid": gid})


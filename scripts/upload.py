import pandas as pd
import os, json
from pymongo import MongoClient
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--path")
    args = parser.parse_args()

    url = os.environ["MONGO_URL"]
    user = os.environ["MONGO_USER"]
    pw = os.environ["MONGO_PASS"]
    db = os.environ["MONGO_DB"]
    collection = os.environ["USERS_COLLECTION"]

    client = MongoClient(url.format(user, pw))

    dab = client[db]
    col = dab[collection]

    with open(args.path) as f:
        data = json.load(f)

    name = args.path.split("/")[-1].split(".")[0]
    data["name"] = name

    col.insert_one(data)

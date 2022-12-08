import os
from pymongo import MongoClient
from logger import logger

MONGO_URI = os.getenv("MONGO_URI")

mg_client = MongoClient(
    host=MONGO_URI
)

def retrieve_docs_from_mongo(database:str, collection:str, query:dict={}):
    # Retrieve documents from a collection in MongoDB
    db = mg_client[database]
    col = db[collection]

    records = []
    for rec in col.find(query):
        rec["_id"] = str(rec["_id"])
        records.append(rec)

    logger.info("Total number of data: {}".format(len(records)))
    
    return records        
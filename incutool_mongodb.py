import pymongo
import os


def initdb():
    MONGO_DB_HOST = os.getenv('MONGO_DB_HOST', '')
    MONGO_DB_USER = os.getenv('MONGO_DB_USER', '')
    MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', '')
    MONGO_DB   = os.getenv('MONGO_DB','')
    MONGO_COLL = os.getenv('MONGO_COLL','')

    mongodb_uri = f'mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}/{MONGO_DB}?retryWrites=true&w=majority'

    # connect to MongoDB
    client = pymongo.MongoClient(mongodb_uri)

   

    mydb = client[MONGO_DB]
    mycoll = mydb[MONGO_COLL]  # change this to point to the proper collection

    collist = mydb.list_collection_names()

    if not ( MONGO_COLL in collist): 
        
        mydb.command("create", MONGO_COLL, timeseries={ 'timeField': 'timestamp', 'metaField': 'name', 'granularity': 'seconds' })

    return mycoll




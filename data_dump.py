# This file is to dump the data in mongodb database
import pymongo
import pandas as pd
import json

#from sensor.config import mongo_client   # to be used when loading the prog from docker or web server
mongo_client=pymongo.MongoClient("mongodb+srv://ksen01:Ks$9433118063@cluster0.coiraav.mongodb.net/?retryWrites=true&w=majority") # for running locally

DATA_FILE_PATH="aps_failure_training_set1.csv" # location of the dataset
#/config/workspace/   (Add this if you are using sensor.config)
DATABASE_NAME="aps"
COLLECTION_NAME="sensor" # data is stored in form of collections 

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH) # Read the dataset
    print(f"Rows and columns: {df.shape}") # Print the shape of dataset

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    #mongodb accepts dataframe in json format
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    # insert_many inserts all records inside mongodb








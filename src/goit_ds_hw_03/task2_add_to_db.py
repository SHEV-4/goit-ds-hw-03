from pymongo import MongoClient,errors 
from pymongo.server_api import ServerApi 
import json

def connection():
    try:
        client = MongoClient(os.environ["MONGODB_URI"],server_api=ServerApi('1'))
        return client
    except errors.ServerSelectionTimeoutError as err:
        print(err)
    except errors.PyMongoError as err:
        print(err)
        
def add_data_to_collection(file_path,collection_name):
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    try:
        with open(file_path,'r',encoding="utf-8") as file:
            data=json.load(file)
        db = client.famous_quote
        collection = db[collection_name]
        result = collection.insert_many(data)
        return result
    except json.JSONDecodeError as err:
        print(err)
    except FileNotFoundError as err:
        print(err)
    except errors.PyMongoError as err:
        print(err)


if __name__ == "__main__":
    print(add_data_to_collection("authors.json",'authors'))
    print(add_data_to_collection("quote.json",'quote'))

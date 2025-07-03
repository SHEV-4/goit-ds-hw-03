from pymongo import MongoClient,errors 
from pymongo.server_api import ServerApi 

def connection():
    try:
        client = MongoClient("mongodb+srv://shev:ShEv4UK@clusterstarted.5xwbbpm.mongodb.net/?retryWrites=true&w=majority&appName=ClusterStarted",server_api=ServerApi('1'))
        return client
    except errors.ServerSelectionTimeoutError as err:
        print(err)
    except errors.PyMongoError as err:
        print(err)

def add_info_to_collection():
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    db = client.pet_info
    db.cats.insert_many([
        {"name": "Barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]},
        {"name": "Riki",
        "age": 2,
        "features": ["дає себе гладити", "сірий","любе гратися"]},
        {"name": "Snow",
        "age": 4,
        "features": ["чорний"]},
        {"name": "Felix",
        "age": 1,
        "features": [ "білий"]},
        {"name": "Richi",
        "age": 5,
        "features": ["ходить в капці", "чорно-білий"]},
        {"name": "Marcus",
        "age": 6,
        "features": ["любе гратися", "дає себе гладити", "коричневий"]},
        {"name": "Mars",
        "age": 2,
        "features": [ "сіро-білий"]},
        {"name": "Luna",
        "age": 1,
        "features": ["ходить в капці", "дає себе гладити", "біло-коричневий"]},
        {"name": "Bella",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудо-чорний"]}
    ])
    


def get_all_record_from_collection():
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    db = client.pet_info
    try:
        record = db.cats.find({})
        for el in record:
            print(el)
    finally:
        client.close()


def get_info_by_name(name):
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    db = client.pet_info
    try:
        record = db.cats.find_one({"name":name})
        print(record)
    finally:
        client.close()
    
def update_age_by_name(age,name):
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    db = client.pet_info
    try:
        db.cats.update_one({"name":name},{"$set":{"age":age}})
    except errors.PyMongoError as err:
        print(err)
    finally:
        client.close()
        

def update_features_by_name(features,name):
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    db = client.pet_info
    try:
        db.cats.update_one({"name":name},{'$push':{'features':{"$each":features}}})
    except errors.PyMongoError as err:
        print(err)
    finally:
        client.close()

def delete_record_by_name(name):
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    db = client.pet_info
    try:
        db.cats.delete_one({'name':name})
    except errors.PyMongoError as err:
        print(err)
    finally:
        client.close()

def delete_all_record():
    client = connection()
    if client is None:
        print("Проблема з підключенням")
        return
    db = client.pet_info
    db.cats.delete_many({})

if __name__ =="__main__":
    update_features_by_name(["test","test"],"Mars")
    
# Joshua Udrea nano ~/Downloads/crud.py  Pwd SNHU1234
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

class AnimalShelter:
    def __init__(self, user, password, host='nv-desktop-services.apporto.com', port=32828, db_name='AAC', collection='animals'):
        try:
            self.client = MongoClient(
                f"mongodb://{user}:{password}@{host}:{port}/"
            )
            self.db = self.client[db_name]
            self.collection = self.db[collection]
        except ConnectionFailure as e:
            print("Could not connect to MongoDB:", e)

    def create(self, data):
        if data:
            result = self.collection.insert_one(data)
            return result.acknowledged
        else:
            raise Exception("Nothing to save, data parameter is empty")


    def read(self, query):
        return list(self.collection.find(query))


    def update(self, query, new_values):
        if query and new_values:
            result = self.collection.update_many(query,{'$set': new_values})
            return result.modified_count
        else:
            raise Exception("Update failed: missing query or new values")

    def delete(self, query):
        if query:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Delete failed: missing query")

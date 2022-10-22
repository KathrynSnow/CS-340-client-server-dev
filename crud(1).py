import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import pprint

class AnimalShelter(object):
    
    def __init__(self, username, password):
        #initialize MongoClient
        self.client = MongoClient('mongodb://%s:%s@localhost:42806' % (username, password))
        self.database = self.client['AAC']
        
    #create, C in CRUD method
    def create(self, data):
        if data is not None:
            data_create = self.database.animals.insert(data)   #data should be dictionary
            return data_create
        else:
            raise Exception("Parameter is empty, nothing to save")
            
    
    #read, R in CRUD method
    def read(self, data):
        if data is not None:
            data_read = self.database.animals.find_one(data,)
            return data_read
        else:
            raise Exception("Parameter is empty, nothing to read")
            
    def readAll(self, data):
        data_read = self.database.animals.find(data,{"_id":False})
        return read_data
    
    
    
    #update, U in CRUD method
    def update(self, query, data):
        if data is not None:
            data_update = self.database.animals.update_one(query, data)
            return data_update
        else:
            raise Exception("Parameter is empty, nothing to update)
                            
                            
                            
    #delete, D in CRUD method
     def delete(self, data):
         if data is not None:
             data_delete = self.database.animals.delete_one(data)
             return data_delete
         else:
             raise Exception("Parameter is empty, nothing to delete")
                            
       
        
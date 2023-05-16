# from pymongo import MongoClient

# cluster = "mongodb+srv://freddykk20:NBXkwlueiqfgfp2F@cluster0.zjvwmxw.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(cluster)

# print(client.list_database_names())

# db = client.carDatabase

# print(db.list_collection_names())

import os
import pprint
from pymongo import MongoClient

# fetch password from .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://freddykk20:{password}@cluster0.zjvwmxw.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

db = client.list_database_names()
test_db = client.carDatabase
collections = test_db.list_collection_names()

carDatabase = client.carDatabase
cars = carDatabase.cars

printer = pprint.PrettyPrinter()

# function to read all cars in collection
def find_all_cars():
    cars_list = cars.find()
     
    for car in cars_list:
        printer.pprint(car)

# find_all_cars()

#function to find a specific car by name

def find_car_by_name():
    car_name = cars.find_one({"name": "HONDA FIT"})
    printer.pprint(car_name)  

# find_car_by_name()

#FUNCTION TO COUNT ALL CARS AVAILABLE   

def count_cars():
    cars_count = cars.count_documents(filter={})
    # count = cars.find().count()
    print("Number of cars is", cars_count)

# count_cars()

# function to get car by id

def get_car_by_id(car_id):
    from bson.objectid import ObjectId

    _id = ObjectId(car_id)
    car = cars.find_one({"_id": _id})
    printer.pprint(car)

# get_car_by_id("642e8e189de5cf4e680bd83e")


# function to filter car prices

def filter_car_prices(min_price, max_price):
    query = {"$and": [
        {"price": {"$gte": min_price}},
        {"price": {"$lte": max_price}}
    ]}
    cars_list = cars.find(query).sort("price")
    for car in cars_list:
        printer.pprint(car)

# filter_car_prices(2000, 3600)


def specific_columns():
    columns = {"_id": 0, "image_urls": 0, "name": 1, "price": 1,  "url": 0}
    cars_list= cars.find({}, columns)
    for car in cars_list:
        printer.pprint(car)

# specific_columns()    
# 
# 
# function to update records
def update_car_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)  

    all_updates = {
        "$set": {"desc": "HONDA FIT"},
        # "$inc": {"price": 1000},
        "$rename": {"name": "car_name"}
    }

    cars.update_one({"_id": _id}, all_updates)

update_car_by_id("642e8e189de5cf4e680bd83e")
    
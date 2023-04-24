from pymongo import MongoClient
import os 

# fetch password from .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://freddykk20:{password}@cluster0.zjvwmxw.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

db = client["carDatabase"]
test_db = client.carDatabase
collections = test_db.list_collection_names()

carDatabase = client.carDatabase
cars = db["cars"]
#logic 

from fastapi import APIRouter

from models.car_model import CarModel
from config.db import carDatabase
from schemas.car_schema import carEntity, carsEntity
from bson import ObjectId

car_route = APIRouter()

@car_route.get('/')
async def get_all_cars():
    print(carDatabase.cars.find())
    print(carsEntity(carDatabase.cars.find()))
    return carsEntity(carDatabase.cars.find())


#POST

@car_route.post('/')
async def add_car(car_item: CarModel):
    carDatabase.cars.insert_one(dict(car_item))
    return carsEntity(carDatabase.cars.find())

#PUT
@car_route.put('/')
async def update_car(id, car_item: CarModel):
    (carDatabase.cars.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(car_item)}))
    return carEntity(carDatabase.cars.find_one({"_id": ObjectId(id)}))

#DELETE

@car_route.delete('/')
async def delete_car(id, car_item: CarModel):
    return carEntity(carDatabase.cars.find_one_and_delete({"_id": ObjectId(id)}))
    # carDatabase.cars.find({"_id": ObjectId(id)})

#GET by ID
@car_route.get('/{id}')

async def find_one_car(id):
    return carEntity(carDatabase.cars.find_one({"_id": ObjectId(id)}))

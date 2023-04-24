from fastapi import FastAPI
# from pymongo import MongoClient
# import os
import uvicorn
from routes.car_route import car_route







app = FastAPI()
app.include_router(car_route)

#endpoints

# @app.get("/cars")

# def get_all_cars():
#     car_list = []
#     for car in cars.find():
#         car_list.append(car)
#     return {"cars": car_list}



# if __name__ == "__RESTAPI__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)


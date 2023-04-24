from pydantic import BaseModel

class CarModel(BaseModel):
    name: str
    price: str
    image_urls: str
    url: str
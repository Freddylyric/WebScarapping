#serializer

def carEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "price": item["price"],
        "image_urls": item["image_urls"],
        "url": item["url"],
    }

# def carEntity(item: dict) -> dict:
#     result = {}
#     if 'name' in item:
#         result['name'] = item['name']
#     # add other keys as needed
#     return result

#for arrays
def carsEntity(entity) -> list:
    return [carEntity(item) for item in entity]
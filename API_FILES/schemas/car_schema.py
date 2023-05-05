#serializer

def carEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "price": item["price"],
        "image_urls": item["image_urls"],
        "url": item["url"],
    }
# checks to ensure the values exist

# def carEntity(item: dict) -> dict:
#     result = {}
#     if 'id' in item:
#         result['id'] = str(item['id'])
#     if 'name' in item:
#         result['name'] = item['name']
#     if 'price' in item:
#         result['price'] = item['price']
#     if 'image_urls' in item:
#         result['image_urls'] = item['image_urls']
#     if 'url' in item:
#         result['url'] = item['url']
#     return result

#for arrays
def carsEntity(entity) -> list:
    return [carEntity(item) for item in entity]



#functions to serialize.. similar functions as above but eliminate the need to serialize each model seperately
#single dictionary: convert model to dict


# def serializeDict (a) -> dict:
#     return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i!= '_id'}}

# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]

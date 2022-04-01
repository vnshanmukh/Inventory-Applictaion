from redis_om import HashModel
from db import inventory
class Product(HashModel):
    name : str
    price : int
    quantity : int
    class Meta:
        database = inventory
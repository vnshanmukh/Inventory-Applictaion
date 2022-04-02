from redis_om import HashModel
from db import inventory
class Product(HashModel):
    name : str
    price : int
    quantity : int
    class Meta:
        database = inventory
class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, completed, refunded

    class Meta:
        database = inventory
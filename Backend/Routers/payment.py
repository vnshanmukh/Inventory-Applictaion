from fastapi import APIRouter
from starlette.requests import Request
import requests, time
from fastapi.background import BackgroundTasks
from db import inventory
from schemas import Order
router = APIRouter(tags=['Payment'],
                    prefix='/payment'
                    )
@router.get('/orders/{pk}')
def get(pk: str):
    return Order.get(pk)


@router.post('/orders')
async def create(request: Request, background_tasks: BackgroundTasks):  # id, quantity
    body = await request.json()

    req = requests.get('http://localhost:8000/inventory/products/%s' % body['id'])
    product = req.json()

    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2 * product['price'],
        total=1.2 * product['price'],
        quantity=body['quantity'],
        status='pending'
    )
    order.save()

    background_tasks.add_task(order_completed, order)

    return order


def order_completed(order: Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
    inventory.xadd('order_completed', order.dict(), '*')
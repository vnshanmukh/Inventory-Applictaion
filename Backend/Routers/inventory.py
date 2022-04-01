from fastapi import APIRouter
from schemas import Product

router = APIRouter(tags=['Inventory'],
                    prefix="/inventory"
)
@router.get('/products')
async def products():
    return [format(pk) for pk in Product.all_pks()]

def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }

@router.post('/products')
def create(product: Product):
    return product.save()


@router.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@router.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)
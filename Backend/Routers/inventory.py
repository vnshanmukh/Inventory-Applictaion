from fastapi import APIRouter
from schemas import Product

router = APIRouter(tags=['Inventory'],
                    prefix="/inventory"
)
@router.get('/products')
async def products():
    return Product.all_pks()

@router.post('/products')
def create(product: Product):
    return product.save()


@router.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@router.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)
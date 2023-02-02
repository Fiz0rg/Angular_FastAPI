from typing import List, Dict

from cloudipsp import Api, Checkout

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from db.product import Product

from pydantic import parse_obj_as

from db.product import Product
from repository.basket_repository import get_basket_goods, get_test
from schemas.product import BaseProduct

from repository.redis import redis_instanse


router = APIRouter()


@router.get("/get_my_basket", response_model=List[BaseProduct])
async def get_my_basket(my_goods: List[BaseProduct] = Depends(get_basket_goods)) -> List[BaseProduct]:

    return parse_obj_as(List[BaseProduct], my_goods)


@router.post("/purchase/{product_id}", response_class=RedirectResponse)
async def purchase(product_id: int):
    take_product = await Product.objects.get(id=product_id)

    product_price = take_product.price
    api = Api(merchant_id=1396424,
            secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": product_price
    }
    url = checkout.url(data).get('checkout_url')
    
    return url


@router.get("/as")
async def fasasd():
    return await get_test()


@router.get("/postreq")
async def asdakdknsofn(name: str):

    value = await Product.objects.all()

    return await redis_instanse.set_lpush_redis(
        key=name,
        list_of_values=value
    )

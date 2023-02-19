from typing import List

from cloudipsp import Api, Checkout

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from fastapi_jwt_auth import AuthJWT

from product.model import Product
from cache_redis.repository import redis_instanse as redis
from product.product_schemas import BaseProduct

from .repository import get_basket_goods


router = APIRouter()


@router.get("/get_my_basket", response_model=List[BaseProduct])
async def get_my_basket(Authorize: AuthJWT = Depends()) -> List[BaseProduct]:

    Authorize.jwt_required()

    username = Authorize.get_jwt_subject()
    exist_user = redis.exists_redis(username)

    if not exist_user:
        """ Adding goods to Redis. """

        list_of_products = await get_basket_goods(username)
        redis.hset_redis(username, list_of_products)

    return redis.hgetall(username) 

        

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


@router.get("/redis")
def test():
    return redis.set_redis("key", "value")
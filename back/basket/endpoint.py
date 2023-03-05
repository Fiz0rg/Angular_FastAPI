from typing import List

from cloudipsp import Api, Checkout

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from fastapi_jwt_auth import AuthJWT

from product.model import Product
from cache_redis.repository import redis_instanse as redis
from product.product_schemas import BaseProduct

from .repository import get_basket_goods, dict_for_redis


router = APIRouter()


@router.get("/get_my_basket", response_model=List[BaseProduct])
async def get_my_basket(Authorize: AuthJWT = Depends()) -> List[BaseProduct]:

    Authorize.jwt_required()

    username: str = Authorize.get_jwt_subject()
    exist_user: bool = redis.exists_redis(username)

    key_prefix: str = f'{username}_basket_'    

    if not exist_user:
        """ Adding goods to Redis. """

        list_of_products: List[Product] = await get_basket_goods(username)
        list_to_dict = await dict_for_redis(key_prefix, list_of_products)
        redis.new_hmset_redis(list_to_dict)

    basket_products: List[BaseProduct] = redis.hgetall(username) 

    return basket_products

        

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
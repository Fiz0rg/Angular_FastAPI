from typing import List

from cloudipsp import Api, Checkout

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from fastapi_jwt_auth import AuthJWT

from ..db.product import Product

from ..repository.basket_repository import get_basket_goods
from ..repository.redis import redis_instanse as redis

from ..schemas.product import BaseProduct


router = APIRouter()


@router.get("/get_my_basket", response_model=List[BaseProduct])
async def get_my_basket(Authorize: AuthJWT = Depends()) -> List[BaseProduct]:

    Authorize.jwt_required()

    username = Authorize.get_jwt_subject()
    exist_user = await redis.exists_redis(username)

    if not exist_user:
        """ Adding goods to Redis. """

        list_of_products = await get_basket_goods(username)
        await redis.hset_redis(username, list_of_products)

    return await redis.hgetall(username) 

        

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
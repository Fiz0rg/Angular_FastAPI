from cloudipsp import Api, Checkout
from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from fastapi_jwt_auth import AuthJWT

from db.product import Product
from repository.basket_repository import BasketRepository as basket_class


router = APIRouter()


@router.get("/get_my_basket")
async def get_my_basket(Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()

    return await basket_class.get_basket_goods(username)



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

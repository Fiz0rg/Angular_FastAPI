from cloudipsp import Api, Checkout

from typing import List
from fastapi import APIRouter, Security
from fastapi.responses import RedirectResponse

from db.product import Product
from db.user import Buyer

from security.user import get_current_user

from repository.basket_repository import BasketRepository as basket_class


router = APIRouter()


@router.get("/get_my_basket")
async def get_my_basket(user_basket: Buyer = Security(get_current_user, scopes=['buyer'])):
    return await basket_class.get_basket_goods(user_basket.id)



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

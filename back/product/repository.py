from typing import List

from fastapi import HTTPException, Depends

from ..db.category import Category
from .model import Product
from ..db.basket import Basket
from ..user.model import Buyer

from .product_schemas import ProductCreate

from ..user.auth import check_access_token


async def create_product(user_input: ProductCreate) -> Product:
    find_category = await Category.objects.get(id=user_input.category)
    if not find_category:
        raise HTTPException(status_code=404, detail="Category not found")

    await Product(**user_input.dict()).save()

    response_product = await Product.objects.select_related("category").get(name=user_input.name)

    return response_product


async def get_product_by_name(product_name: str) -> Product:
    return await Product.objects.select_related("category").get(name=product_name)


async def add_product_in_basket(product_name: str, Authorize: check_access_token = Depends()) -> Basket:

    username = Authorize.get_jwt_subject()
    user = await Buyer.objects.get(username=username)

    product = await Product.objects.get(name=product_name)
    user_basket = await Basket.objects.get(user_id=user.id)
    await user_basket.products.add(product)

    """ Increase purchases => we can traffic most popular goods"""
    product.purchases+=1
    await product.update(_columns=['purchases'])

    """ We check amount of product. And if amount > 5, price of this product is reduced by 10% """
    if product.amount:
        product.amount -= 1
        await product.update(_columns=['amount'])

        if product.amount <= 5:
            product.price *= 0.9
            await product.update(_columns=['price'])

    return user_basket


async def get_all_products() -> List[Product]:

    return await Product.objects.select_related('category').filter(amount__gt=0).all()

        
async def ordered_products() -> List[Product]:
    
    return await Product.objects.order_by("-purchases").all()





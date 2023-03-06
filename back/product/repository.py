from typing import List

from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from starlette.responses import Response 

from .model import Product
from .product_schemas import ProductCreate

from product_category.model import Category
from basket.model import Basket
from user.model import Buyer
from user.auth import check_access_token


async def create_product(user_input: ProductCreate) -> Product:
    find_category: Category = await Category.objects.get(id=user_input.category)

    if not find_category:
        raise HTTPException(status_code=404, detail="Category not found")

    await Product(**user_input.dict()).save()
    response_product: Product = await Product.objects.select_related("category").get(name=user_input.name)
    return response_product


async def get_product_by_name(product_name: str) -> Product:
    one_product: Product = await Product.objects.select_related("category").get(name=product_name)
    if not one_product:
        raise HTTPException(status_code=404, detail="Not found this product")
    return one_product


async def add_product_in_basket(product_name: str, Authorize: check_access_token = Depends()) -> Response:

    username: str = Authorize.get_jwt_subject()
    user: Buyer = await Buyer.objects.get(username=username)

    product: Product = await Product.objects.get(name=product_name)
    user_basket: Basket = await Basket.objects.get(user_id=user.id)

    """
    Check if product already in basket
    """

    all_products: List[Basket] = await Product.objects.select_related(['baskets']).filter(
        baskets__user_id=user.id
            ).values()
            
    for item in all_products:
        if product.name == item['name']:
            raise HTTPException(status_code=304)
        
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

    return JSONResponse(status_code=200, content="Ok")


async def get_all_products() -> List[Product]:
    products = await Product.objects.select_related('category').filter(amount__gt=0).all()
    if not products:
        raise HTTPException(status_code=404, detail="Not found any products")
    return products

        
async def ordered_products() -> List[Product]:
    return await Product.objects.order_by("-purchases").all()





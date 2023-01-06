from fastapi import HTTPException

from db.category import Category
from db.product import Product
from db.basket import Basket

from schemas.product import ProductCreate

class ProductRepository:

    async def create_product(user_input: ProductCreate):
        find_category = await Category.objects.get(id=user_input.category)
        if not find_category:
            raise HTTPException(status_code=404, detail="Category not found")

        new_product = await Product(**user_input.dict()).save()

        response_product = await Product.objects.select_related("category").get(name=user_input.name)

        return response_product


    async def get_product_by_name(product_name: str):
        return await Product.objects.select_related("category").get(name=product_name)


    async def add_product_in_basket(product_name: str, user_id: int):

        product = await Product.objects.get(name=product_name)
        user_basket = await Basket.objects.get(user_id=user_id)
        await user_basket.products.add(product)

        product.purchases+=1
        await product.update(_columns=['purchases'])

        return user_basket
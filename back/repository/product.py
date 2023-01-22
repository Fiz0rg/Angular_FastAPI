from fastapi import HTTPException

from db.category import Category
from db.product import Product
from db.basket import Basket
from db.user import Buyer

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


    async def add_product_in_basket(product_name: str, username: str):

        user = await Buyer.objects.get(username=username)

        product = await Product.objects.get(name=product_name)
        user_basket = await Basket.objects.get(user_id=user.id)
        await user_basket.products.add(product)

        """ Increase purchases => we can traffic most popular goods"""
        product.purchases+=1
        await product.update(_columns=['purchases'])

        """ We check amount of product. And if amount > 5, price of this product is reduced by 10% """
        product.amount -= 1
        await product.update(_columns=['amount'])

        if product.amount <= 5:
            product.price *= 0.9
            await product.update(_columns=['price'])

        return user_basket


    async def get_all_products():
        a = await Product.objects.select_related('category').filter(amount__gt=0).all()
        return a

        
    async def ordered_products():
        return await Product.objects.order_by("-purchases").all()


    async def get_product_by_name(product_name):
        return await Product.objects.select_related(['category']).get(name=product_name)
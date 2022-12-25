from typing import List

from schemas.product import ProductCreate

from db.basket import Basket
from db.product import Product


class BasketRepository:
    
    async def get_basket_goods(user_id: int) :
        
        
        user_basket = await Product.objects.select_related(['baskets', 'category']).values()
        return user_basket
from typing import List

from user.model import Buyer
from product.model import Product  

from cache_redis.repository import redis_instanse


from product.product_schemas import BaseProduct


async def get_basket_goods(username: str) -> List[BaseProduct]:
                
    user: Buyer = await Buyer.objects.get(username=username)
    user_basket: List[BaseProduct] = await Product.objects.select_related(['baskets']).filter(
        baskets__user_id=user.id
            ).values()

    return user_basket


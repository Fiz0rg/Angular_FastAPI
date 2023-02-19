from typing import List

from ..user.model import Buyer
from ..db.product import Product  

from .redis import redis_instanse

from ..schemas.product import BaseProduct


async def get_basket_goods(username: str) -> List[BaseProduct]:
                
    user = await Buyer.objects.get(username=username)
    user_basket = await Product.objects.select_related(['baskets']).filter(
        baskets__user_id=user.id
            ).values()

    return user_basket


async def get_test():
    return await redis_instanse.get_redis_by_key("a")
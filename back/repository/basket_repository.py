from typing import List

from fastapi import Depends

from db.product import Product
from db.user import Buyer

from security.auth import username_from_jwt

from schemas.product import BaseProduct

from repository.redis import redis_cache, add_products_in_redis, convert_str_from_redis


async def get_basket_goods(username: str = Depends(username_from_jwt)) -> List[BaseProduct]:
                
    user = await Buyer.objects.get(username=username)

    if await redis_cache.lrange(user.username):
        return await convert_str_from_redis(user.username)
    
    else:
        user_basket = await Product.objects.select_related(['baskets']).filter(
        baskets__user_id=user.id
    ).all()

        await add_products_in_redis(user.username, user_basket)

    return await convert_str_from_redis(user.username)
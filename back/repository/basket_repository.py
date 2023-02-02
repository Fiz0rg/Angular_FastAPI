from fastapi import Depends

from db.user import Buyer

from security.auth import username_from_jwt

from .redis import redis_instanse


async def get_basket_goods(username: str = Depends(username_from_jwt)):
                
    user = await Buyer.objects.get(username=username)

    return 


async def get_test():
    return await redis_instanse.get_redis_by_key("a")
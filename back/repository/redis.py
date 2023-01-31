import json

from typing import Optional, List

from aioredis import Redis, create_redis_pool

from schemas.product import BaseProduct

#Create a RedisCache instance
class RedisCache:
    
    def __init__(self):
        self.redis_cache: Optional[Redis] = None
        
    async def init_cache(self):
        self.redis_cache = await create_redis_pool("redis://localhost:6379/0?encoding=utf-8") #Connecting to database

    async def keys(self, pattern):
        return await self.redis_cache.keys(pattern)

    async def set(self, key, value):
        return await self.redis_cache.set(key, value)

    async def hset(self, key, field, value):
        return await self.redis_cache.hset(key, field, value)
    
    async def get(self, key):
        return await self.redis_cache.get(key)

    async def lpush(self, key, value):
        return await self.redis_cache.lpush(key, value)

    async def lrange(self, username: str) -> List[BaseProduct]:
        return await self.redis_cache.lrange(username, 0, -1)
    
    async def close(self):
        self.redis_cache.close()
        await self.redis_cache.wait_closed()


redis_cache = RedisCache()


async def add_products_in_redis(username_key: str, product_list: List[BaseProduct]) -> bool:
 
    for product in product_list:
        
        one = BaseProduct(**product.dict())
        await redis_cache.lpush(username_key, one.json())

    return 


async def convert_str_from_redis(username_key: str) -> List[BaseProduct]:

    redis_string_response = await redis_cache.lrange(username_key)
    result: List[BaseProduct] = []

    for product in redis_string_response:
        parsed_produst = json.loads(product)
        pydantic_product = BaseProduct(**parsed_produst)
        result.append(pydantic_product)  

    return result  


import json
from redis import Redis

from typing import Optional, List

from ..product.product_schemas import BaseProduct


class RebiuldedRedis:

    _default_ex_time: Optional[int] = 604800

    def __init__(
        self,
        expire_time: Optional[int] = None,
        host: str = "aio",
        port: int = 6379,
        db: int = 0,
        encoding: str = "utf-8"
    ):
        self.redis = Redis(host=host, port=port, db=db)
        self._expire_time = expire_time or self._default_ex_time


    @property
    def expire_time(self):
        return self._expire_time


    async def get_redis_by_key(self, key: str) -> any:
        response = await self.redis.get(key)

        if not response:
            return None
        result = json.loads(response)
        return result


    def set_redis(self, key: str, value: any, keepttl: Optional[bool] = False) -> Optional[bool]:
        
        dumbs_value = json.dumps(value)
        request = self.redis.set(
            name=key,
            value=dumbs_value
        )
        return request


    async def set_lpush_redis(self, list_of_values, username: str) -> Optional[bool]:
        result = [await self.redis.lpush(username+str(value.id), value.json()) for value in list_of_values]
        return result

    
    async def get_keys(self, key):
        return await self.redis.keys(key)


    async def get_all_lrange(self, keys) -> List[BaseProduct]:
        my_list = [await self.redis.lrange(key, 0, -1) for key in keys]
        return my_list


    async def hset_redis(self, username: str, list_of_value: List[BaseProduct]):

        for value in list_of_value:
            key_value = f'{username+str(value["id"])}'
            await self.redis.hset(username, key_value, json.dumps(value))


    async def hgetall(self, key: str) -> List[any]:
        request = await self.redis.hgetall(key)
        converted_result = [json.loads(request[value]) for value in request]
        
        return converted_result


    async def exists_redis(self, key: str) -> bool:
        res = await self.redis.exists(key)  
        return bool(res)


redis_instanse = RebiuldedRedis()





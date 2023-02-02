import json

from typing import Optional, List, Dict
from aioredis import from_url


class RebiuldedRedis:

    _default_ex_time: Optional[int] = 604800

    def __init__(
        self,
        expire_time: Optional[int] = None,
        host: str = "redis://127.0.0.1",
        port: int = 6379,
        encoding: str = "utf-8"
    ):
        self.redis = from_url(f'{host}:{port}', encoding=encoding, decode_responses=True)
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

    async def set_redis(self, key: str, value: any, keepttl: Optional[bool] = False) -> Optional[bool]:
        
        dumbs_value = json.dumps(value)

        request = await self.redis.set(
            name=key,
            value=dumbs_value,
            ex=self.expire_time,
            keepttl=keepttl
        )
        
        return request


    async def set_lpush_redis(self, key: str, list_of_values) -> Optional[bool]:

        result = [await self.redis.lpush(key, value.json()) for value in list_of_values]
        return result





redis_instanse = RebiuldedRedis()





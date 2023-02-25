import json
from redis import Redis

from typing import Optional, List

from product.product_schemas import BaseProduct


class RebiuldedRedis:

    _default_ex_time: Optional[int] = 604800

    def __init__(
        self,
        expire_time: Optional[int] = None,
        host: str = "127.0.0.1",
        port: int = 6379,
        db: int = 0,
        encoding: str = "utf-8"
    ):
        self.redis = Redis(host=host, port=port)
        self._expire_time = expire_time or self._default_ex_time


    @property
    def expire_time(self):
        return self._expire_time


    def get_redis_by_key(self, key: str) -> any:
        response = self.redis.get(key)

        if response:
            return json.loads(response)


    def set_redis(self, key: str, value: any, keepttl: Optional[bool] = False) -> Optional[bool]:
        
        dumbs_value = json.dumps(value)
        request = self.redis.set(
            name=key,
            value=dumbs_value
        )
        return request


    def set_lpush_redis(self, list_of_values, username: str) -> Optional[bool]:
        result = [self.redis.lpush(username+str(value.id), value.json()) for value in list_of_values]
        return result

    
    def get_keys(self, key):
        return self.redis.keys(key)


    def get_all_lrange(self, keys) -> List[BaseProduct]:
        my_list = [self.redis.lrange(key, 0, -1) for key in keys]
        return my_list


    def hset_redis(self, username: str, list_of_value: List[BaseProduct]):

        for value in list_of_value:
            key_value = f'{username+str(value["id"])}'
            self.redis.hset(username, key_value, json.dumps(value))


    def hgetall(self, key: str) -> List[any]:
        request = self.redis.hgetall(key)
        converted_result = [json.loads(request[value]) for value in request]
        
        return converted_result


    def exists_redis(self, key: str) -> bool:
        res = self.redis.exists(key)  
        return bool(res)


redis_instanse = RebiuldedRedis()





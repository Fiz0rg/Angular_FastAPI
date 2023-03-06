import json
from fastapi import HTTPException

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
        self.encoding = encoding
        self.redis = Redis(host=host, port=port)
        self._expire_time = expire_time or self._default_ex_time


    @property
    def expire_time(self):
        return self._expire_time


    def get_redis_by_key(self, key: str) -> any:
        response = self.redis.get(key)

        if not response:
            raise HTTPException(status_code=404, detail="Not found")

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

        if key:
            return self.redis.keys(key)
        else:
            return self.redis.keys("*")


    def get_all_lrange(self, keys) -> List[BaseProduct]:
        my_list = [self.redis.lrange(key, 0, -1) for key in keys]

        if not my_list:
            raise HTTPException(status_code=404, detail="There is not any values")

        return my_list


    def hmset_redis(self, items: dict[str, dict[str, str]]):
        """
        Pipiline alow us to add many items in a row and after this send request to Redis with all items.
        Without it we'll just make many-many request by one item.
        """
        with self.redis.pipeline() as pipe:
            for key, value in items.items():
                pipe.hmset(key,value)
            pipe.execute()


    def hgetall(self, key_prefix: str) -> List[any]:
        """ 
        I don't know how to format fetched values from redis from bytes to native types. 
        So I just came up with this way. 
        """

        all_user_keys = self.redis.keys(key_prefix + "*")
        my_list = []
        for i in all_user_keys:
            item = self.redis.hgetall(i)

            for key, value in item.items():
                item.pop(key, None)
                item[key.decode(self.encoding)] = value.decode(self.encoding)

            my_list.append(BaseProduct(**item))
                    
        return my_list


    def exists_redis(self, key: str) -> bool:
        res = self.redis.exists(key)  
        return bool(res)


redis_instanse = RebiuldedRedis()





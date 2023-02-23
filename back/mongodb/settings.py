from typing import List

from bson import ObjectId
from motor import motor_asyncio

from .schemas import MongoDBSchemas


class MongoDB:
    
    def __init__(
        self,
        port: int = 27017,
        host: str = "localhost"
        ):

        self.client = motor_asyncio.AsyncIOMotorClient(host, port)
        self.database = self.client.rock
        self.collection = self.database.get_collection("rock_playlist")


    async def find_one(self, object_id: str) -> MongoDBSchemas:

        one_record = await self.collection.find_one({ "_id": ObjectId(object_id)})
        if one_record:
            result: MongoDBSchemas = MongoDBSchemas(**one_record)
            return result


    async def insert_one(self ,object: dict) -> MongoDBSchemas:

        action = await self.collection.insert_one(object)
        if action:
            one = await self.collection.find_one({ "_id": action.inserted_id})
            return MongoDBSchemas(**one)
    

mongo_instance = MongoDB()
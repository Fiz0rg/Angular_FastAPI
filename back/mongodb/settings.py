from typing import List

from bson import ObjectId
from motor import motor_asyncio

from .schemas import MongoDBSchemas


class MongoDB:
    
    def __init__(
        self,
        collection: str,
        database: str = "rock",
        port: int = 27017,
        host: str = "localhost",
        ):

        self.client = motor_asyncio.AsyncIOMotorClient(host, port)
        self.database = self.client[database]
        self.collection = self.database[collection]


    async def find_one(self, object_id: str) -> MongoDBSchemas:

        one_record = await self.collection.find_one({ "_id": ObjectId(object_id)})
        if one_record:
            result: MongoDBSchemas = MongoDBSchemas(**one_record)
            return result

    
    async def get_items(self) -> List[MongoDBSchemas]:
        result_list = []
        async for item in self.collection.find({}):
            result_list.append(MongoDBSchemas(**item))

        return result_list


    async def insert_one(self ,object: dict) -> MongoDBSchemas:

        action = await self.collection.insert_one(object)
        if action:
            one = await self.collection.find_one({ "_id": action.inserted_id})
            return MongoDBSchemas(**one)


    async def insert_many(self, items: List[dict]) -> List[MongoDBSchemas]:
        
        await self.collection.insert_many(items)
        result = await self.get_items()
        return result
    

    async def delete_student(self, object_id: str) -> bool:
        student = await self.collection.find_one({"_id": ObjectId(id)})
        if student:
            await self.collection.delete_one({"_id": ObjectId(id)})
            return True


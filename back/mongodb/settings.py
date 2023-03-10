from typing import List

from bson import ObjectId
from fastapi import HTTPException
from motor import motor_asyncio

from .schemas import MongoDBSchemas


class MongoDB:
    
    def __init__(
        self,
        collection_string: str,
        database_string: str = "rock",
        port: int = 27017,
        host: str = "localhost",
        ):
        self.collection_string = collection_string
        self.database_string = database_string
        self.client = motor_asyncio.AsyncIOMotorClient(host, port)
        self.database = self.client[database_string]
        self.collection = self.database[collection_string]


    def __repr__(self):
        return repr(f'Custom MongoDB object with {self.collection_string} collection and {self.database_string} database')


    async def find_one(self, object_id: str) -> MongoDBSchemas:
        one_record: MongoDBSchemas = await self.collection.find_one({ "_id": ObjectId(object_id)})
        if not one_record:
            raise HTTPException(status_code=404, detail="Not found this item")
            
        result: MongoDBSchemas = MongoDBSchemas(**one_record)
        return result

    
    async def get_items(self) -> List[MongoDBSchemas]:
        result_list: List[MongoDBSchemas] = [MongoDBSchemas(**item) async for item in self.collection.find({})]
        if not result_list:
            raise HTTPException(status_code=404, detail="Not found these items")
        return result_list


    async def insert_one(self ,object: dict) -> MongoDBSchemas:
        action = await self.collection.insert_one(object)
        if action:
            one = await self.collection.find_one({ "_id": action.inserted_id})
            return MongoDBSchemas(**one)


    async def insert_many(self, items: List[dict]) -> List[MongoDBSchemas]:
        await self.collection.insert_many(items)
        result: List[MongoDBSchemas] = await self.get_items()
        return result
    

    async def delete_one(self, object_id: str) -> bool:
        delete_item: MongoDBSchemas = await self.collection.find_one({"_id": ObjectId(id)})
        if delete_item:
            await self.collection.delete_one({"_id": ObjectId(id)})
            return True
        else: 
            raise HTTPException(status_code=304)


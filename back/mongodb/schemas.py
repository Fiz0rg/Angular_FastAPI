from pydantic import BaseModel


class MongoDBSchemas(BaseModel):
    _id: str
    rock: str
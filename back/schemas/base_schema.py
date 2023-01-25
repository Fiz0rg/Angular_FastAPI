from pydantic import BaseModel


class BaseSchemaModel(BaseModel):
    class Config:
        orm_mode = True
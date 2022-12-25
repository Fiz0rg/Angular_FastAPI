from pydantic import BaseModel


class CategoryName(BaseModel):
    name: str
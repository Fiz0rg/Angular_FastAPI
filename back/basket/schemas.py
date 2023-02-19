from pydantic import BaseModel


class BaseSchemaModel(BaseModel):
    class Config:
        orm_mode=True

class BasketProduct(BaseSchemaModel):
    name: str = None
    price: int
    category__name: str
    amount: float = None
    
from pydantic import BaseModel

from ..schemas.base_schema import BaseSchemaModel


class BaseProduct(BaseSchemaModel):
    name: str
    price: int
    amount: int = None


class ProductCreate(BaseProduct):
    category: int


class Category(BaseModel):
    name: str = None


class FullProductSchema(ProductCreate):
    id: int
    category: Category

    
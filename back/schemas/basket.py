from .base_schema import BaseSchemaModel


class BasketProduct(BaseSchemaModel):
    name: str = None
    price: int
    category__name: str
    amount: float = None
    
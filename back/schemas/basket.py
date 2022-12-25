from pydantic import BaseModel


class ProductInBasket(BaseModel):
    name: str
    price: int
    category__name: str
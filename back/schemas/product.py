from typing import List

from db.product import Product

from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: int
    category: int
    amount: int


class Category(BaseModel):
    id: int
    name: str


class Products(BaseModel):
    id: int
    name: str
    price: int
    amount: int
    category: Category
    




class ListOfProducts(BaseModel):
    list_of_products: List[Products] = []
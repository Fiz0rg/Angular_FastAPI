from typing import Optional
from ormar import ForeignKey, String, Integer, Model

from product_category.model import Category
from db import database, metadata_obj

class Product(Model):
    class Meta:
        database = database
        metadata = metadata_obj

    id: int = Integer(primary_key=True)
    name: str = String(max_length=30, unique=True, index=True)
    price: Optional[int] = Integer()
    purchases: int = Integer(default=0)
    amount: str = Integer(default=0)

    category: Optional["Category"] = ForeignKey(Category, skip_reverse=True)







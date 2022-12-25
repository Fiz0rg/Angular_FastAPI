from typing import Optional
from ormar import ForeignKey, String, Integer, Model

from db.category import Category

from .base_class import MetaClass

class Product(Model):
    class Meta(MetaClass):
        tablename = "product"

    id: int = Integer(primary_key=True)
    name: str = String(max_length=30, unique=True, index=True)
    price: Optional[int] = Integer()

    category: Optional["Category"] = ForeignKey(Category, skip_reverse=True)







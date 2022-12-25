from typing import Optional
from ormar import String, ForeignKey, Integer, Model

from .base_class import MetaClass
from .product import Product

class ProductPhoto(Model):
    class Meta(MetaClass):
        tablename = "productphoto"

    id: int = Integer(primary_key=True)
    url: str = String(max_length=1000)
    product: Optional[Product] = ForeignKey(Product, skip_reverse=True)
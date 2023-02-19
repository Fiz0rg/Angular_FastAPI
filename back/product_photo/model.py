from typing import Optional
from ormar import String, ForeignKey, Integer, Model

from ..db import database, metadata_obj
from ..product.model import Product

class ProductPhoto(Model):
    class Meta:
        tablename = "productphoto"
        database = database
        metadata = metadata_obj

    id: int = Integer(primary_key=True)
    url: str = String(max_length=1000)
    product: Optional[Product] = ForeignKey(Product, skip_reverse=True)
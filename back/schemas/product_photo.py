from typing import Optional

from pydantic import BaseModel

from db.product import Product


class ProductPhotoSchemas(BaseModel):
    url: str
    product: Optional[Product] = None
from typing import Optional

from pydantic import BaseModel

from product.model import Product


class ProductPhotoSchemas(BaseModel):
    url: str
    product: Optional[Product] = None
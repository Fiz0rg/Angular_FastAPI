from typing import Optional, List
from ormar import ForeignKey, Model, Integer, ManyToMany

from product.model import Product
from user.model import Buyer
from db import database, metadata_obj

class Basket(Model):
    class Meta:
        database = database
        metadata = metadata_obj

    id: int = Integer(primary_key=True)
    user_id: Optional[Buyer] = ForeignKey(Buyer, skip_reverse=True)
    products: Optional[List[Product]] = ManyToMany(Product)



    
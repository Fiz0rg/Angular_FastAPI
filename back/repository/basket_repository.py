from typing import List

from fastapi import Depends

from db.product import Product
from db.user import Buyer

from security.auth import username_from_jwt

from schemas.product import FullProductSchema


async def get_basket_goods(username: str = Depends(username_from_jwt)) -> List[FullProductSchema]:
                
    user = await Buyer.objects.get(username=username)

    user_basket = await Product.objects.select_related(['baskets']).filter(
        baskets__user_id=user.id
    ).all()

    return user_basket
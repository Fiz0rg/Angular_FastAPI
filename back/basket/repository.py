from typing import List

from user.model import Buyer
from product.model import Product  

from product.product_schemas import BaseProduct


async def get_basket_goods(username: str) -> List[BaseProduct]:
                
    user: Buyer = await Buyer.objects.get(username=username)
    user_basket: List[BaseProduct] = await Product.objects.select_related(['baskets']).filter(
        baskets__user_id=user.id
            ).values()

    return user_basket


async def dict_for_redis(key_prefix: str, list_of_items: List[any]):

    new_dict = dict()
    for item in list_of_items:
        dict_key: str = key_prefix + item['name']
        new_dict[dict_key] = item
    
    return new_dict
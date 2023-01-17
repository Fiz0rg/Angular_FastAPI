from db.product import Product
from db.user import Buyer


class BasketRepository:
    
    async def get_basket_goods(username: str):
                
        user = await Buyer.objects.get(username=username)

        user_basket = await Product.objects.select_related(['baskets']).filter(
            baskets__user_id=user.id
        ).values()
        return user_basket
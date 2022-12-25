from security.user import hash_password
from .base_repository import BaseRepository
from db.basket import Basket

class UserRepository:
    

    async def create(new_user, db_model):
        """  When created user, will be create a basket for this new user with same id. """

        new_user.password = hash_password(new_user.password)
        add = await BaseRepository.create_object(new_object=new_user, db_model=db_model)
        await Basket.objects.create(user_id=add)

        return add
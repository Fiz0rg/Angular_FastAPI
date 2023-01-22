from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from schemas.user import Admin
from security.user import hash_password
from .base_repository import BaseRepository
from db.basket import Basket

from db.user import Buyer

class UserRepository:
    

    async def create(new_user, db_model):
        """  When created user, will be create a basket for this new user with same id. """

        new_user.password = hash_password(new_user.password)
        add = await BaseRepository.create_object(new_object=new_user, db_model=db_model)
        await Basket.objects.create(user_id=add)

        return add

    
    async def get_all_users():
        return await Buyer.objects.all()


    async def create_admin():
        
        admin = Admin(username="Admin", password='123', is_admin=True)
        create_admin = await UserRepository.create(admin, Buyer)
        return create_admin


    async def checking(username: str):
        return await Buyer.objects.get(username=username)


    async def get_username_by_jwt(Authorize: AuthJWT = Depends()):
        Authorize.jwt_required()

        username = Authorize.get_jwt_subject()
        user = await Buyer.objects.get(username=username)
        return user

from typing import List

from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from ..schemas.user import UserAdminSchema, UserCreate

from ..security.user import Settings, hash_password

from .base_repository import BaseRepository

from ..db.basket import Basket
from ..db.user import Buyer


@AuthJWT.load_config
def get_config():
    return Settings()


async def create_user(new_user, db_model) -> UserAdminSchema:
    """  When created user, will be create a basket for this new user with same id. """

    new_user.password = hash_password(new_user.password)
    add = await BaseRepository.create_object(new_object=new_user, db_model=db_model)
    await Basket.objects.create(user_id=add)

    return add

    
async def get_all_users() -> List[UserAdminSchema]:
    return await Buyer.objects.all()


async def create_admin() -> UserAdminSchema:
        
    admin = UserAdminSchema(username="Admin", password='123', is_admin=True)
    create_admin = await create_user(admin, Buyer)
    return create_admin

    
async def registration(new_user: UserCreate):
    return await create_user(new_user, Buyer)


async def checking(username: str) -> UserAdminSchema:
    return await Buyer.objects.get(username=username)


async def get_username_by_jwt(Authorize: AuthJWT = Depends()) -> str:
    Authorize.jwt_required()

    username = Authorize.get_jwt_subject()
    return username



async def get_user_by_name(username: str = Depends(get_username_by_jwt)) -> Buyer:
    return await Buyer.objects.get(username=username)
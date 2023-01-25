from typing import List

import datetime
from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from schemas.user import UserAdminSchema, UserCreate, UserForm
from schemas.token import Token

from security.user import Settings, authenticate_user, hash_password

from .base_repository import BaseRepository
from .auth_repository import check_access_token

from db.basket import Basket
from db.user import Buyer


@AuthJWT.load_config
def get_config():
    return Settings()


async def username_from_jwt(auth: AuthJWT = Depends(check_access_token)) -> str:
    return auth.get_jwt_subject()


async def create_tokens(user: UserForm, Authorize: AuthJWT = Depends()) -> Token:
    user = await authenticate_user(username=user.username, password=user.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
        
    exp_time_acc_token = datetime.timedelta(minutes=12)
    exp_time_refresh_token = datetime.timedelta(minutes=28)

    access_token = Authorize.create_access_token(subject=user.username, expires_time=exp_time_acc_token)
    refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=exp_time_refresh_token)

    token_info = {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
    return Token(**token_info)
    

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


async def new_token(Authorize: AuthJWT = Depends()) -> str:
        
    try:
        Authorize.jwt_refresh_token_required()
    except:
        raise HTTPException(status_code=422, detail="Some shit")

    expire_access_token_time = datetime.timedelta(minutes=10)

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user, expires_time=expire_access_token_time)

    return new_access_token


async def get_user_by_name(username: str = Depends(get_username_by_jwt)):
    return await Buyer.objects.get(username=username)
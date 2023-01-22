import datetime
from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from schemas.user import Admin, UserCreate, UserForm
from schemas.token import Token

from security.user import Settings, authenticate_user, hash_password
from .base_repository import BaseRepository
from db.basket import Basket

from db.user import Buyer


@AuthJWT.load_config
def get_config():
    return Settings()


class UserRepository:

    async def create_tokens(user: UserForm, Authorize: AuthJWT = Depends()) -> Token:
        user = await authenticate_user(username=user.username, password=user.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        exp_time_acc_token = datetime.timedelta(minutes=12)
        exp_time_refresh_token = datetime.timedelta(minutes=28)

        access_token = Authorize.create_access_token(subject=user.username, expires_time=exp_time_acc_token)
        refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=exp_time_refresh_token)
        return {"access_token": access_token, "refresh_token": refresh_token , "token_type": "bearer"}
    

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

    
    async def registration(new_user: UserCreate):
        return await UserRepository.create(new_user, Buyer)


    async def checking(username: str):
        return await Buyer.objects.get(username=username)


    async def get_username_by_jwt(Authorize: AuthJWT = Depends()):
        Authorize.jwt_required()

        username = Authorize.get_jwt_subject()
        user = await Buyer.objects.get(username=username)
        return user


    async def new_token(Authorize: AuthJWT = Depends()):
        
        try:
            Authorize.jwt_refresh_token_required()
        except:
            raise HTTPException(status_code=422, detail="Some shit")

        expire_access_token_time = datetime.timedelta(minutes=10)

        current_user = Authorize.get_jwt_subject()
        new_access_token = Authorize.create_access_token(subject=current_user, expires_time=expire_access_token_time)

        return new_access_token
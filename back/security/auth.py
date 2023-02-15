import datetime

from fastapi_jwt_auth import AuthJWT
from fastapi import Depends, HTTPException 

from ..schemas.token import Token
from ..schemas.user import UserForm

from .user import authenticate_user


async def check_access_token(Authorize: AuthJWT = Depends()) -> AuthJWT:
    Authorize.jwt_required()

    return Authorize


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
    

async def new_token(Authorize: AuthJWT = Depends()) -> str:
        
    try:
        Authorize.jwt_refresh_token_required()
    except:
        raise HTTPException(status_code=422, detail="Some shit")

    expire_access_token_time = datetime.timedelta(minutes=10)

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user, expires_time=expire_access_token_time)

    return new_access_token


async def username_from_jwt(auth: AuthJWT = Depends(check_access_token)) -> str:
    return auth.get_jwt_subject()
import os
import datetime

from typing import Union
from jose import jwt, JWTError

from fastapi_jwt_auth import AuthJWT

from dotenv import load_dotenv
from fastapi import Depends
from fastapi.security import SecurityScopes, OAuth2PasswordBearer
from passlib.context import CryptContext

from pydantic import BaseModel, ValidationError
from db.user import Buyer
from schemas.token import TokenData
from .exeptions import exceptions

load_dotenv('.env')

ACCESS_TOKEN_EXPIRE_MINUNES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='user/token', scopes={"buyer": "just casual user"})

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(planed_password: str, hash_password: str):
    return pwd_context.verify(planed_password, hash_password)



async def authenticate_user(username: str, password: str):
    user = await Buyer.objects.get(username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[datetime.timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ['SECRET_KEY'], algorithm=os.environ['ALGHORITHM'])
    return encoded_jwt


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = exceptions(headers={"WWW-Authenticate": authenticate_value})
    try:
        payload = jwt.decode(token, os.environ['SECRET_KEY'], algorithm=os.environ['ALGHORITHM'])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])

        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = await Buyer.objects.get(username=token_data.username)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise credentials_exception(detail="Not enough permissions")
    return user

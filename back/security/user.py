import datetime
from typing import Union

from jose import jwt, JWTError

from fastapi import Depends
from fastapi.security import SecurityScopes, OAuth2PasswordBearer

from passlib.context import CryptContext

from pydantic import ValidationError

from db.user import Buyer

from schemas.token import TokenData

from .exeptions import exceptions

SECRET_KEY = "7f18111e48f8b0f243bc48a2faa87e17541ceea805f094f11e07db807fccf337"
ALGORITHM = "HS256"
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
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
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
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
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





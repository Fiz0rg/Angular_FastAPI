import os

from dotenv import load_dotenv
from passlib.context import CryptContext

from pydantic import BaseModel

from .model import Buyer

load_dotenv('.env')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Settings(BaseModel):
    authjwt_secret_key: str = "7f18111e48f8b0f243bc48a2faa87e17541ceea805f094f11e07db807fccf337"


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(planed_password: str, hash_password: str):
    return pwd_context.verify(planed_password, hash_password)



async def authenticate_user(username: str, password: str):
    user = await Buyer.objects.get(username=username)
    if any([user, verify_password(password, user.password)]):
        return user
    return user


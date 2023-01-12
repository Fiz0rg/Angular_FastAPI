import os

from dotenv import load_dotenv
from fastapi import Depends
from passlib.context import CryptContext

from pydantic import BaseModel

from db.user import Buyer

load_dotenv('.env')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Settings(BaseModel):
    authjwt_secret_key: str = os.environ['SECRET_KEY']


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


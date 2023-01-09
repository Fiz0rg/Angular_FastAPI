import os

from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from fastapi import APIRouter, HTTPException, Request, Depends, Form, Security
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from dotenv import load_dotenv


from repository.user import UserRepository
from security.user import ACCESS_TOKEN_EXPIRE_MINUNES, authenticate_user, create_access_token, get_current_user

from schemas.user import UserCreate, UserName, Admin
from schemas.token import Token

from db.user import Buyer

load_dotenv('.env')

router = APIRouter()

class Settings(BaseModel):
    authjwt_secret_key: str = os.environ['SECRET_KEY']


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post("/create_admin", response_model=Buyer)
async def create_admin():
    """ Create default admin. """

    admin = Admin(username="Admin", password='123', is_admin=True)
    create_admin = await UserRepository.create(admin, Buyer)
    return create_admin


@router.post("/registration", response_model=UserName)
async def create_user(new_user: UserCreate):

    return await UserRepository.create(new_user, Buyer)


@router.post("/token", response_model=Token)
async def login(username: str = Form(), password: str = Form(), Authorize: AuthJWT = Depends()):
    user = await authenticate_user(username=username, password=password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = Authorize.create_access_token(subject=user.username)
    refresh_token = Authorize.create_refresh_token(subject=user.username)

    return {"access_token": access_token, "refresh_token": refresh_token , "token_type": "bearer"}


@router.get("/refresh_token", response_model=str)
async def refresh_token(Authorize: AuthJWT = Depends(), current_user: Buyer = Security(get_current_user, scopes=["buyer"])):
    try:
        Authorize.jwt_refresh_token_required()
    except:
        raise HTTPException("You have no refresh_token")
    
    new_access_token = Authorize.create_access_token(subject=current_user.username)
    return {"access_token": new_access_token}

import datetime
from typing import List
from dotenv import load_dotenv

from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException, Header, Request

from repository.user import UserRepository
from db.user import Buyer
from schemas.user import Admin, UserCreate, UserName, UserForm
from schemas.token import Token
from security.user import authenticate_user, Settings

load_dotenv('.env')

router = APIRouter()


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
async def login(user: UserForm, Authorize: AuthJWT = Depends()):
    user = await authenticate_user(username=user.username, password=user.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    exp_time_acc_token = datetime.timedelta(seconds=12)
    exp_time_refresh_token = datetime.timedelta(minutes=28)


    access_token = Authorize.create_access_token(subject=user.username, expires_time=exp_time_acc_token)
    refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=exp_time_refresh_token)
    return {"access_token": access_token, "refresh_token": refresh_token , "token_type": "bearer"}


@router.post("/refresh_token", response_model=str)
async def refresh_token(
    request: Request,
    Authorize: AuthJWT = Depends()
):

    request = request.headers['authorization']

    if Authorize:
        Authorize.jwt_refresh_token_required(token=request)

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user.username)
    return {"access_token": new_access_token}


@router.get("/get_all", response_model=List[UserCreate], response_model_exclude={"password"})
async def get_all():
    return await Buyer.objects.all()
    

@router.get('/me')
async def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    username = Authorize.get_jwt_subject()
    user = await Buyer.objects.get(username=username)
    return user


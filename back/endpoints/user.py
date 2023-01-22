from typing import List, Set
from dotenv import load_dotenv

from fastapi import APIRouter, Depends

from repository.user import UserRepository
from db.user import Buyer
from schemas.user import Admin, UserCreate, UserName
from schemas.token import Token


load_dotenv('.env')

router = APIRouter()


@router.post("/create_admin", response_model=Buyer)
async def create_admin(admin: Admin = Depends(UserRepository.create_admin)):
    """ Create default admin. """

    return admin


@router.post("/registration", response_model=UserName)
async def create_user(new_user: UserCreate = Depends(UserRepository.registration)):
    return new_user


@router.post("/token", response_model=Token)
async def login(refresh_access_types_tokens: Token = Depends(UserRepository.create_tokens)):
    return refresh_access_types_tokens


@router.post("/refresh_token")
async def refresh_token(new_access_token: str = Depends(UserRepository.new_token)):
    return {"access_token": new_access_token}


@router.get("/get_all", response_model=List[UserCreate], response_model_exclude={"password"})
async def get_all(users: Set[UserCreate] = Depends(UserRepository.get_all_users)):
    return users
    

@router.get("/me")
def get_user_by_jwt(username: str = Depends(UserRepository.get_username_by_jwt)):
    return username
from typing import List, Dict
from dotenv import load_dotenv

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import parse_obj_as

from repository.user import UserRepository
from db.user import Buyer
from schemas.user import Admin, UserCreate, UserName
from schemas.token import Token


load_dotenv('.env')

router = APIRouter()


@router.post("/create_admin", response_model=Admin)
async def create_admin(admin: Admin = Depends(UserRepository.create_admin)) -> Admin:
    """ Create default admin. """

    return admin


@router.post("/registration", response_model=Buyer)
async def create_user(new_user: Buyer = Depends(UserRepository.registration)) -> Buyer:

    return new_user


@router.post("/token", response_model=Token)
async def login(refresh_access_types_tokens: Token = Depends(UserRepository.create_tokens)) -> Token:

    return Token.from_orm(refresh_access_types_tokens)


@router.post("/refresh_token", response_model=Dict[str, str])
async def refresh_token(new_access_token: str = Depends(UserRepository.new_token)) -> JSONResponse:

    return JSONResponse(content={"access_token": new_access_token})


@router.get("/get_all", response_model=List[UserCreate], response_model_exclude={"password"})
async def get_all(users: List[UserCreate] = Depends(UserRepository.get_all_users)) -> List[UserCreate]:
    return parse_obj_as(List[UserCreate], users)
    

@router.get("/me", response_model=str)
def get_user_by_jwt(username: str = Depends(UserRepository.get_username_by_jwt)) -> str:
    return UserName(username=username)
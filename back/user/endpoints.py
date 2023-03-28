from typing import List, Dict
from dotenv import load_dotenv

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from starlette.requests import Request

from pydantic import parse_obj_as

from .user_schemas import UserAdminSchema, UserCreate, RegistrationForm
from .token_schemas import Token
from .model import Buyer

from .repository import (
    create_admin,
    active_user,
    get_all_users,
    get_user_by_name,
    pre_registration
)

from .auth import (
    create_tokens,
    new_token,
)


load_dotenv('.env')

router = APIRouter()

@router.get("/aaa")
async def aaa():
    result = await Buyer.objects.get(id=1)
    return result


@router.post("/create_admin", response_model=UserAdminSchema)
async def create_admin(admin: UserAdminSchema = Depends(create_admin)) -> UserAdminSchema:
    """ Create default admin. """

    return UserAdminSchema.from_orm(admin)


@router.post("/registration", response_model=Dict[str, str])
async def create_user(new_user: RegistrationForm) -> JSONResponse:

    await pre_registration(new_user)

    return JSONResponse(content={"response": "Follow the link in your gmail"}, status_code=200)


@router.post("/token", response_model=Token)
async def login(refresh_access_types_tokens: Token = Depends(create_tokens)) -> Token:

    return Token.from_orm(refresh_access_types_tokens)


@router.post("/refresh_token", response_model=Dict[str, str])
async def refresh_token(new_access_token: str = Depends(new_token)) -> JSONResponse:

    return JSONResponse(content={"access_token": new_access_token})


@router.get("/get_all", response_model=List[UserCreate], response_model_exclude={"password"})
async def get_all(users: List[UserCreate] = Depends(get_all_users)) -> List[UserCreate]:
    return parse_obj_as(List[UserCreate], users)
    

@router.get("/me", response_model=UserAdminSchema)
def get_user_by_jwt(user: UserAdminSchema = Depends(get_user_by_name)) -> UserAdminSchema:
    return UserAdminSchema.from_orm(user)


@router.get("/user_id={encrypted_user_id}", response_model=Dict[str, str])
async def final_registration_stage(request: Request) -> JSONResponse:

    encrypted_user = request.url.path
    result = await active_user(encrypted_user)

    if not result:
        raise HTTPException(status_code=304)
        
    return JSONResponse (status_code=200, content={"congrats": "You have beed registrated!"})

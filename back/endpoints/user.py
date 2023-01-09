from typing import List

from fastapi import APIRouter, Security

from db.user import Buyer
from schemas.user import UserCreate
from security.user import get_current_user


router = APIRouter()


@router.get("/get_all", response_model=List[UserCreate], response_model_exclude={"password"})
async def get_all():
    return await Buyer.objects.all()
    

@router.get("/users/me/", response_model=Buyer, response_model_exclude={"id", "password"})
async def read_users_me(current_user: Buyer = Security(get_current_user, scopes=["buyer"])):
    return current_user





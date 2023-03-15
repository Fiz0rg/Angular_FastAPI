from typing import List

from jose import jwe

from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT

from config import SMTP_SECRET_KEY

from .user_schemas import UserAdminSchema, UserCreate
from .security import Settings, hash_password
from .model import Buyer

from basket.model import Basket
from tasks.tasks import auth_gmail_letter
from cache_redis.repository import RebiuldedRedis


redis_instanse = RebiuldedRedis(expire_time=30, db=3)


@AuthJWT.load_config
def get_config():
    return Settings()


async def create_user(new_user: UserAdminSchema) -> UserAdminSchema:
    """  When created user, will be create a basket for this new user with same id. """

    new_user.password = hash_password(new_user.password)
    add = await Buyer.objects.create(**new_user.dict())
    await Basket.objects.create(user_id=add)

    return add

    
async def get_all_users() -> List[UserAdminSchema]:
    return await Buyer.objects.all()


async def create_admin() -> UserAdminSchema:
    admin_info = UserAdminSchema(username="Admin", password='123', is_admin=True)
    create_admin = await create_user(admin_info)
    return create_admin

    
async def registration(new_user: UserCreate) -> Buyer:
    return await create_user(new_user, Buyer)


async def pre_registration(user_id: int, user_gmail: str) -> JSONResponse:
    check_existing_user: Buyer = Buyer.objects.get(id=user_id)

    if not check_existing_user:
        raise HTTPException(status_code=403, detail="user already exist")

    encrypted_user_id: str = jwe.encrypt(str(user_id), SMTP_SECRET_KEY, algorithm="dir", encryption="A256GCM")

    redis_instanse.set_redis(user_id, encrypted_user_id)
    redis_instanse.set_expire_time(user_id, expire_time=1800)

    confirmation_link: str = f"http://127.0.0.1:8000/user_id={encrypted_user_id}"

    auth_gmail_letter.delay(
        confirmation_link=confirmation_link,
        user_gmail=user_gmail
    )

    return JSONResponse(content="Пройдите на вашу почту, пройдите по ссылке подтверждения")
    

async def checking(username: str) -> UserAdminSchema:
    return await Buyer.objects.get(username=username)


async def get_username_by_jwt(Authorize: AuthJWT = Depends()) -> str:
    Authorize.jwt_required()

    username: str = Authorize.get_jwt_subject()
    return username



async def get_user_by_name(username: str = Depends(get_username_by_jwt)) -> Buyer:
    return await Buyer.objects.get(username=username)
from typing import List
from datetime import datetime

from jose import jwt

from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT

from config import SMTP_SECRET_KEY

from .user_schemas import UserAdminSchema, RegistrationForm
from .security import Settings, hash_password
from .model import Buyer

from basket.model import Basket
from tasks.tasks import auth_gmail_letter
from cache_redis.repository import RebiuldedRedis


redis_instanse = RebiuldedRedis(expire_time=30)


@AuthJWT.load_config
def get_config():
    return Settings()


async def create_user(new_user: UserAdminSchema) -> UserAdminSchema:
    """  When created user, will be create a basket for this new user with same id. """

    new_user.password = hash_password(new_user.password)
    pre_registration(new_user)
    add = await Buyer.objects.create(**new_user.dict())
    await Basket.objects.create(user_id=add)

    return add

    
async def get_all_users() -> List[UserAdminSchema]:
    return await Buyer.objects.all()


async def create_admin() -> UserAdminSchema:
    admin_info = UserAdminSchema(username="Admin", gmail="123@gmail.com", password='123', is_admin=True)
    create_admin = await create_user(admin_info)
    return create_admin

    
async def active_user(encrypted_user_id: str) -> bool:

    splitting_url_path: str = encrypted_user_id.split("=")[1]
    decode_user_info: dict = jwt.decode(splitting_url_path, key=SMTP_SECRET_KEY, algorithms="HS256")    

    user_id, user_gmail = next(iter(decode_user_info.items()))

    get_value_from_redis: str = redis_instanse.get_redis_by_key(user_id)

    if not get_value_from_redis:
        raise HTTPException(status_code=404, detail="Your link was expire. Please, repeat auth process")

    get_value_from_redis = get_value_from_redis.replace('"', '')
    
    if splitting_url_path != get_value_from_redis:
        raise HTTPException(status_code=406, detail="Your encrypted value don't match with currently existing. Repeat auth process if you're not hacker")
    
    activate_user = await Buyer.objects.get(id=int(user_id))
    activate_user.is_activate = True
    activate_user.creation_datetime = datetime.now()

    await activate_user.update(_columns=["is_activate", "creation_datetime"])
    await activate_user.load()
    
    return True


async def pre_registration(user: RegistrationForm) -> JSONResponse:
    """ Create user but with False flag is_active. False until user don't follow registration link. """

    check_existing_user: Buyer = await Buyer.objects.get_or_none(gmail=user.gmail, username=user.username)

    if check_existing_user:
        raise HTTPException(status_code=403, detail="user already exist")
    
    create_not_active_user: Buyer = await create_user(user)

    if not create_not_active_user:
        raise HTTPException(status_code=401, detail="Something went wrong")

    

    # encrypted_user_id: bytes = jwe.encrypt(str(create_not_active_user.id), SMTP_SECRET_KEY, algorithm="dir", encryption="A256GCM")

    encode_user_info: str = jwt.encode({str(create_not_active_user.id): create_not_active_user.gmail}, key=SMTP_SECRET_KEY, algorithm="HS256")

    redis_instanse.set_redis(create_not_active_user.id, encode_user_info)
    redis_instanse.set_expire_time(create_not_active_user.id, expire_time=1800)

    confirmation_link: str = f"http://127.0.0.1:8000/user/user_id={encode_user_info}"

    auth_gmail_letter.delay(
        confirmation_link=confirmation_link,
        user_gmail=user.gmail
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
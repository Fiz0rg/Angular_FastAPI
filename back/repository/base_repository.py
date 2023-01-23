from fastapi import Depends
from fastapi_jwt_auth import AuthJWT


class BaseRepository:

    async def create_object(new_object, db_model):
        return await db_model.objects.create(**new_object.dict())


async def check_access_token_exist(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
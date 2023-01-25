from fastapi_jwt_auth import AuthJWT
from fastapi import Depends 


async def check_access_token(Authorize: AuthJWT = Depends()) -> AuthJWT:
    Authorize.jwt_required()

    return Authorize

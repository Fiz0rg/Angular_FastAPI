from typing import List

from .user_schemas import BaseSchemaModel


class TokenData(BaseSchemaModel):
    username: str | None = None
    scopes: List[str] = []


class Token(BaseSchemaModel):
    access_token: str
    refresh_token: str
    token_type: str 
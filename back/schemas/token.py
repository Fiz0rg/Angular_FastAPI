from typing import List

from pydantic import BaseModel

from .base_schema import BaseSchemaModel


class TokenData(BaseModel):
    username: str | None = None
    scopes: List[str] = []


class Token(BaseSchemaModel):
    access_token: str
    refresh_token: str
    token_type: str 
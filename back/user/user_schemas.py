from fastapi import Form
from pydantic import BaseModel


class BaseSchemaModel(BaseModel):
    class Config:
        orm_mode=True


class UserName(BaseSchemaModel):
    username: str


class PasswordUser(BaseSchemaModel):
    password: str


class UserCreate(UserName, PasswordUser):
    pass


class UserAdminSchema(UserCreate):
    is_admin: bool


class UserForm(BaseSchemaModel):
    username: str = Form(...)
    password: str = Form(...)



        
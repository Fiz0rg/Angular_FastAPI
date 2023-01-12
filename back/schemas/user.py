from fastapi import Form
from pydantic import BaseModel

class UserName(BaseModel):
    username: str


class PasswordUser(BaseModel):
    password: str


class UserCreate(UserName, PasswordUser):
    pass


class Admin(UserCreate):
    is_admin: bool


class UserForm(BaseModel):
    username: str = Form(...)
    password: str = Form(...)



        
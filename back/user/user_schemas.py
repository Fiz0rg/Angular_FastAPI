from fastapi import Form
from pydantic import EmailStr


from basket.schemas import BaseSchemaModel


class UserName(BaseSchemaModel):
    username: str


class PasswordUser(BaseSchemaModel):
    password: str


class UserCreate(UserName, PasswordUser):
    pass


class UserAdminSchema(UserCreate):
    is_admin: bool


class RegistrationForm(BaseSchemaModel):
    username: str 
    gmail: EmailStr
    password: str



        
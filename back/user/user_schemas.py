from fastapi import Form
from pydantic import EmailStr


from basket.schemas import BaseSchemaModel


class UserName(BaseSchemaModel):
    username: str


class PasswordUser(BaseSchemaModel):
    password: str


class GmailUser(BaseSchemaModel):
    gmail: EmailStr


class UserCreate(UserName, PasswordUser):
    pass


class UserAdminSchema(UserCreate, GmailUser):
    is_admin: bool


class UserForm(UserName, PasswordUser):
    pass


class RegistrationForm(BaseSchemaModel):
    username: str 
    gmail: EmailStr
    password: str



        
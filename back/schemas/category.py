from fastapi import Form
from pydantic import BaseModel

from .base_schema import BaseSchemaModel


class FormCategoryName(BaseModel):
    category_name: str = Form(...)


class CategoryName(BaseSchemaModel):
    category_name: str 


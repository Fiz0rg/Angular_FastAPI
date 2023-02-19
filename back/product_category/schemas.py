from fastapi import Form
from pydantic import BaseModel

from ..schemas.base_schema import BaseSchemaModel


class FormCategoryName(BaseModel):
    category_name: str = Form(...)


class CategoryName(BaseSchemaModel):
    name: str 


class FullCategorySchema(CategoryName):
    id: int

from fastapi import Form
from pydantic import BaseModel


class CategoryName(BaseModel):
    category_name: str = Form(...)
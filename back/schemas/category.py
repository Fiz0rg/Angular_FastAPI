from typing import List

from fastapi import Form
from pydantic import BaseModel

from db.category import Category


class CategoryName(BaseModel):
    category_name: str = Form(...)


class ListCategories(BaseModel):
    list_of_cat: List[Category] = []

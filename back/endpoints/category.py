from typing import List

from fastapi import APIRouter

from db.category import Category
from schemas.category import CategoryName

router = APIRouter()


@router.post("/create_category", response_model=Category, response_model_exclude={"id"})
async def create_category(category_name: CategoryName):
    new_category = await Category.objects.create(name=category_name.name)
    return new_category


@router.get("/get_all", response_model=List[Category], response_model_exclude={"id"})
async def get_all_categories():
    return await Category.objects.all()

    
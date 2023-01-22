from typing import Set

from fastapi import APIRouter, Depends

from db.category import Category
from db.product import Product

from repository.category_repository import RepositoryClass

from schemas.category import CategoryName


router = APIRouter()


@router.post("/create_category", response_model=Category, response_model_exclude={"id"})
async def create_category(category_name: CategoryName):
    new_category = await Category.objects.create(name=category_name.category_name)
    return new_category


@router.get("/get_all", response_model=Set[Category])
async def get_all_categories(categories: Set[Category] = Depends(RepositoryClass.get_all_caregories)):
    return categories


@router.get("/one")
async def get_category_by_name(name: str):
    return await Category.objects.get(name=name)


@router.get("/{category_name}")
async def sorted_category(category_name: str):
    category = await Category.objects.get(name=category_name)

    return await Product.objects.filter(category__name=category.name).all()
    

@router.post("/dsad")
async def test(test: str = Depends(RepositoryClass.test)):
    return test
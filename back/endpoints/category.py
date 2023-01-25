from typing import List

from fastapi import APIRouter, Depends
from pydantic import parse_obj_as

from db.category import Category
from db.product import Product

from repository.category_repository import (
    get_all_caregories,
    get_category_by_name, 
    create_category,
    sorted_products_by_category_name,
)

from schemas.category import CategoryName


router = APIRouter()


@router.post("/create_category", response_model=Category, response_model_exclude={"id"})
async def create_category(new_category: CategoryName = Depends(create_category)) -> Category:
    
    return CategoryName.from_orm(new_category)


@router.get("/get_all", response_model=List[Category])
async def get_all_categories(categories: List[Category] = Depends(get_all_caregories)) -> List[Category]:

    return parse_obj_as(List[Category], categories)


@router.get("/one", response_model=Category)
async def get_category_by_name(category: Category = Depends(get_category_by_name)) -> Category:

    return Category.from_orm(category)


@router.get("/{category_name}", response_model=List[Product])
async def sorted_category(products: List[Product] = Depends(sorted_products_by_category_name)) -> List[Product]:

    return parse_obj_as(List[Product], products)

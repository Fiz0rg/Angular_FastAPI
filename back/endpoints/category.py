from typing import Set, List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from db.category import Category
from db.product import Product

from repository.category_repository import (
    get_all_caregories,
    get_category_by_name, 
    create_category_dependency,
    sorted_products_by_category_name,
)

from schemas.category import CategoryName, ListCategories


router = APIRouter()


@router.post("/create_category", response_model=Category, response_model_exclude={"id"})
async def create_category(new_category: CategoryName = Depends(create_category_dependency)):
    
    return Category(**new_category.dict())


@router.get("/get_all")
async def get_all_categories(categories: Set[Category] = Depends(get_all_caregories)):

    return ListCategories(list_of_cat=categories)


@router.get("/one")
async def get_category_by_name(category: Category = Depends(get_category_by_name)):

    return Category(**category.dict())


@router.get("/{category_name}")
async def sorted_category(products: Set[Product] = Depends(sorted_products_by_category_name)):

    return JSONResponse(content=products, status_code=200) 

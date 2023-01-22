from typing import Set

from fastapi import APIRouter, Depends

from db.category import Category
from db.product import Product

from repository.category_repository import RepositoryClass

from schemas.category import CategoryName


router = APIRouter()


@router.post("/create_category", response_model=Category, response_model_exclude={"id"})
async def create_category(new_category: CategoryName = Depends(RepositoryClass.create_category)):
    return new_category


@router.get("/get_all")
async def get_all_categories(categories: Set[Category] = Depends(RepositoryClass.get_all_caregories)):
    return categories


@router.get("/one")
async def get_category_by_name(category_name: Category = Depends(RepositoryClass.get_category_by_name)):
    return category_name


@router.get("/{category_name}")
async def sorted_category(products: Set[Product] = Depends(RepositoryClass.sorted_products_by_category_name)):

    return products

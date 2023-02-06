from typing import List

from fastapi import APIRouter, Depends

from fastapi_jwt_auth import AuthJWT

from pydantic import parse_obj_as
from repository.basket_repository import get_basket_goods

from repository.category_repository import (
    get_all_caregories,
    get_category_by_name, 
    create_category,
    sorted_products_by_category_name,
)

from schemas.product import FullProductSchema
from schemas.category import FullCategorySchema


router = APIRouter()


@router.post("/create_category", response_model=FullCategorySchema, response_model_exclude={"id"})
async def create_category(new_category: FullCategorySchema = Depends(create_category)) -> FullCategorySchema:

    return FullCategorySchema.from_orm(new_category)


@router.get("/get_all", response_model=List[FullCategorySchema])
async def get_all_categories(categories: List[FullCategorySchema] = Depends(get_all_caregories)) -> List[FullCategorySchema]:

    return parse_obj_as(List[FullCategorySchema], categories)


@router.get("/one", response_model=FullCategorySchema)
async def get_category_by_name(category: FullCategorySchema = Depends(get_category_by_name)) -> FullCategorySchema:

    return FullCategorySchema.from_orm(category)


@router.get("/{category_name}", response_model=List[FullProductSchema])
async def sorted_category(products: List[FullProductSchema] = Depends(sorted_products_by_category_name)) -> List[FullProductSchema]:

    return parse_obj_as(List[FullProductSchema], products)

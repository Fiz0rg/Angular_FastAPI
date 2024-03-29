import datetime

from typing import List

from fastapi import APIRouter, Depends, Request

from pydantic import parse_obj_as

from .schemas import FullCategorySchema

from cache_redis.repository import redis_instanse
from product.product_schemas import FullProductSchema
from mongodb.settings import MongoDB

from .repository import (
    get_all_caregories,
    get_category_by_name, 
    create_category,
    sorted_products_by_category_name,
)


router = APIRouter()


@router.get('/a')
def test(request: Request):
    return redis_instanse.checking_ips_addresses(request.client.host)


@router.get("/aa_mongo")
async def test_mongo():

    fake_data = [
        {"rap": "shit"},
        {'rock': 'awesome'}
    ]

    mongo_instance = MongoDB("rock_playlist")
    mb = await mongo_instance.insert_many(fake_data)
    return mb


@router.get('a_test')
def redis_test():
    return redis_instanse.set_redis("key", "value")



@router.post("/create_category", response_model=FullCategorySchema, response_model_exclude={"id"})
async def create_category(new_category: FullCategorySchema = Depends(create_category)) -> FullCategorySchema:

    return FullCategorySchema.from_orm(new_category)


@router.get("/get_all", response_model=List[FullCategorySchema])
async def get_all_categories(request: Request, categories: List[FullCategorySchema] = Depends(get_all_caregories)) -> List[FullCategorySchema]:

    return parse_obj_as(List[FullCategorySchema], categories)



@router.get("/one", response_model=FullCategorySchema)
async def get_category_by_name(category: FullCategorySchema = Depends(get_category_by_name)) -> FullCategorySchema:
    
    return FullCategorySchema.from_orm(category)


@router.get("/{category_name}", response_model=List[FullProductSchema])
async def sorted_category(products: List[FullProductSchema] = Depends(sorted_products_by_category_name)) -> List[FullProductSchema]:

    return parse_obj_as(List[FullProductSchema], products)

from typing import List, Dict, Any

from pydantic import parse_obj_as

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from starlette.responses import Response

from .product_schemas import FullProductSchema

from .repository import (
    create_product,
    get_all_products,
    add_product_in_basket,
    ordered_products,
    get_product_by_name
)


router = APIRouter()    


@router.post(
    "/create_product",
    response_model=FullProductSchema,
    response_model_exclude={"id", "baskets", "category__id"}
    )
async def create_product(product: FullProductSchema = Depends(create_product)) -> FullProductSchema:
    return FullProductSchema.from_orm(product)


@router.get(
    "/get_all_products",
    response_model=List[FullProductSchema],
    response_model_exclude={"id", "baskets", "category__id"}
    )
async def get_all(products: List[FullProductSchema] = Depends(get_all_products)) -> List[FullProductSchema]:
    return parse_obj_as(List[FullProductSchema], products)


@router.post("/add_product_in_basket")
async def add_product_in_basket(adding_response: Response = Depends(add_product_in_basket)) -> JSONResponse:
    return adding_response


@router.get("/get_ten_goods", response_model=List[FullProductSchema])
async def get_ten_goods(products: List[FullProductSchema] = Depends(ordered_products)) -> List[FullProductSchema]:
    return parse_obj_as(List[FullProductSchema], products)
    

@router.get("/{product_name}", response_model=FullProductSchema)
async def get_product_by_name(one_product: FullProductSchema = Depends(get_product_by_name)) -> FullProductSchema:
    return FullProductSchema.from_orm(one_product)

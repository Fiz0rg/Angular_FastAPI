from typing import Set, List, Dict

from pydantic import parse_obj_as

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from repository.product import (
    create_product,
    get_all_products,
    add_product_in_basket,
    ordered_products,
    get_product_by_name
)

from db.product import Product

router = APIRouter()    


@router.post(
    "/create_product",
    response_model=Product,
    response_model_exclude={"id", "baskets", "category__id"}
    )
async def create_product(product: Product = Depends(create_product)) -> Product:
    
    return Product.from_orm(product)


@router.get(
    "/get_all_products",
    response_model=List[Product],
    response_model_exclude={"id", "baskets", "category__id"}
    )
async def get_all(products: List[Product] = Depends(get_all_products)) -> List[Product]:
    
    return parse_obj_as(List[Product], products)


@router.post(
    "/add_product_in_basket",
    response_model=Dict[str, str],
    dependencies=[Depends(add_product_in_basket)]
    )
async def add_product_in_basket() -> JSONResponse:
    
    return JSONResponse(content={"done": "Product has been added into our basket"}, status_code=200) 


@router.get("/get_ten_goods", response_model=List[Product])
async def get_ten_goods(products: List[Product] = Depends(ordered_products)) -> List[Product]:
    return parse_obj_as(List[Product], products)


@router.get("/{product_name}", response_model=Product)
async def get_product_by_name(one_product: Product = Depends(get_product_by_name)) -> Product:
    return Product.from_orm(one_product)
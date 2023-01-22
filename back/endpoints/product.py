from typing import Set, List

from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from repository.product import ProductRepository

from db.product import Product

router = APIRouter()    

@router.post("/create_product", response_model=Product, response_model_exclude={"id", "baskets", "category__id"})
async def create_product(product: Product = Depends(ProductRepository.create_product)):
    
    return product


@router.get(
    "/get_all_products",
    response_model=List[Product],
    response_model_exclude={"id", "baskets", "category__id"}
    )
async def get_all(products: List[Product] = Depends(ProductRepository.get_all_products)):
    
    return products


@router.post("/add_product_in_basket")
async def add_product_in_basket(adding_product: dict = Depends(ProductRepository.add_product_in_basket)):

    return {"status_response": "200"}


@router.get("/get_ten_goods")
async def get_ten_goods(products: Set[Product] = Depends(ProductRepository.ordered_products)):
    return products


@router.get("/{product_name}")
async def get_product_by_name(product_name: str):
    return await Product.objects.select_related(['category']).get(name=product_name)
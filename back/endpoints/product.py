from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT

from repository.product import ProductRepository
from db.product import Product
from schemas.product import ProductCreate

router = APIRouter()    

@router.post("/create_product", response_model=Product, response_model_exclude={"id", "baskets", "category__id"})
async def create_product(product: ProductCreate):
    
    return await ProductRepository.create_product(product)


@router.get("/get_all_products", response_model=List[Product], response_model_exclude={"id", "baskets", "category__id"})
async def get_all():
    return await Product.objects.select_related('category').filter(amount__gt=0).all()


@router.post("/add_product_in_basket")
async def add_product_in_basket(product_name: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    username = Authorize.get_jwt_subject()

    await ProductRepository.add_product_in_basket(product_name=product_name, username=username)
    return {"status_response": "200"}


@router.get("/get_ten_goods")
async def get_ten_goods():
    a = await Product.objects.order_by("-purchases").all()
    return a[:2]


@router.get("/{product_name}")
async def get_product_by_name(product_name: str):
    return await Product.objects.select_related(['category']).get(name=product_name)
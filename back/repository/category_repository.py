from typing import List

from fastapi import Depends

from db.category import Category
from db.product import Product

from .base_repository import check_access_token_exist

from schemas.category import CategoryName



async def sorted_products_by_category_name(category_name: str) -> List[Product]:

    category = await Category.objects.get(name=category_name)

    return await Product.objects.filter(category__id=category.id).all()


async def get_all_caregories() -> List[Category]:
    return await Category.objects.all()


async def create_category(
    category_name: CategoryName,
    
    ) -> Category:
    return await Category.objects.create(name=category_name.category_name)


async def get_category_by_name(category_name: str) -> Category:
    return await Category.objects.get(name=category_name)
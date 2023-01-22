from db.category import Category
from db.product import Product

from schemas.category import CategoryName


class RepositoryClass:

    async def sorted_products_by_category_name(category_name: str):
        category = await Category.objects.get(name=category_name)

        return await Product.objects.filter(category__name=category.name).all()


    async def get_all_caregories():
        return await Category.objects.all()


    async def create_category(category_name: CategoryName):
        new_category = await Category.objects.create(name=category_name.category_name)
        return new_category


    async def get_category_by_name(category_name: str):
        return await Category.objects.get(name=category_name)
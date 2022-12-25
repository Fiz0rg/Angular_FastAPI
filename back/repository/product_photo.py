import os

from unittest.mock import patch
import aiofiles

from fastapi import UploadFile, HTTPException

from db.product_photo import ProductPhoto

from .product import ProductRepository


class ProductPhotoRepository:
    async def add_product_photo(file: UploadFile, product_name: str):
        """ File processing. 
        Cheking existance of directory (/static/name_category/file_name)
        """

        product = await ProductRepository.get_product_by_name(product_name=product_name)
        category_name = product.category.name
        path = (os.getcwd()) + "/static" + f"/{category_name}"

        if not os.path.exists(path):
            os.mkdir(path)

        category_name = product.category.name
        url_for_phoro = f'{path}/{product.name}.jpeg'

        if file.content_type == "image/jpeg":
            await write_photo(url_for_phoro, file)
        else:
            raise HTTPException(status_code=404, detail="This isn't a photo")
        
        """ Adding record in database. """

        return await ProductPhoto.objects.create(url=url_for_phoro, product=product)


async def write_photo(url: str, file: UploadFile):
    async with aiofiles.open(url, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)
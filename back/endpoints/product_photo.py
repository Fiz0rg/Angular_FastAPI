from fastapi import APIRouter, UploadFile

from db.product_photo import ProductPhoto

from repository.product_photo import ProductPhotoRepository

router = APIRouter()


@router.post("/add_photo", response_model=ProductPhoto)
async def add_photo(product_name: str, file: UploadFile):
    execution = ProductPhotoRepository.add_product_photo(file, product_name=product_name)
    return await execution








from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from fastapi_jwt_auth .exceptions import AuthJWTException

from tasks.settings import cel

# from .product_photo.endpoint import router as product_photo_router

from basket.endpoint import router as basket_router
from product_category.endpoint import router as category_router
from user.endpoints import router as user_router
from product.endpoint import router as product_router

from db import database

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://127.0.0.1:4200/login"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database

    if not database_.is_connected:
        print("Connecting to database")
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database

    if database_.is_connected:
        print("Disconnecting from  database")
        await database_.disconnect()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
        

app.include_router(category_router, tags=["category router"], prefix="/category")
app.include_router(user_router, tags=["user router"], prefix="/user")
app.include_router(basket_router, tags=["basket router"], prefix="/basket")
app.include_router(product_router, tags=["product router"], prefix="/product")
# app.include_router(product_photo_router, tags=["photo"], prefix="/photo")

# app.mount("/static", StaticFiles(directory="static"), name="static")

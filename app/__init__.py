from app.instances.db_config import database
from fastapi import FastAPI
from app.routers.user import user_router
from app.routers.auth import auth_router
from app.routers.upload import upload_router
from app.routers.store import store_router
from app.routers.product import product_router
from app.routers.order import order_router
from app.routers.rating import rating_router
from app.routers.review import review_router
from app.settings import settings
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


async def startup():
    await database.connect()

async def shutdown():
    await database.disconnect()

def create_app():

    @asynccontextmanager
    async def lifespan(app:FastAPI):
        await startup()
        yield
        await shutdown()

    app = FastAPI(title="Farmmerce", lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"], 
        allow_headers=["*"],  
    )

    app.include_router(user_router)
    app.include_router(auth_router)
    app.include_router(upload_router)
    app.include_router(store_router)
    app.include_router(product_router)
    app.include_router(order_router)
    app.include_router(rating_router)
    app.include_router(review_router)

    return app

app = create_app()
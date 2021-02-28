import aioredis
from fastapi import APIRouter

from app.resources.stock import router as router_stock
from app.config import REDIS_URI
from app.db import Redis


router = APIRouter()


@router.on_event('startup')
async def startup():
    Redis(await aioredis.create_redis_pool(REDIS_URI, encoding='utf8'))


router.include_router(router_stock, tags=['stock'], prefix='/stock')

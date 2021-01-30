
from fastapi import APIRouter

from app.resources.stock import router as router_stock

router = APIRouter()

router.include_router(router_stock, tags=['stock'], prefix='/stock')

import pandas as pd
import os

from fastapi import APIRouter
from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.config import STOCK_DAILY_PATH
from app.utils.exc import FileNotFoundException


router = APIRouter()


class Daily(BaseModel):
    ts_code: str
    trade_date: datetime
    open: float
    close: float
    high: float
    low: float


@router.get('/daily/{code}', response_model=List[Daily])
async def stock_daily(code: str):
    fp = os.path.join(STOCK_DAILY_PATH, code)
    if not os.path.isfile(fp):
       raise FileNotFoundException(fp)
    columns = ['ts_code', 'trade_date', 'open',
               'close', 'high', 'low']
    data = pd.read_csv(fp, parse_dates=['trade_date'])[columns].to_dict('records')
    return data


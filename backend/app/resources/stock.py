import pandas as pd
import numpy as np
import os

from fastapi import APIRouter
from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.config import STOCK_DAILY_PATH
from app.utils.exc import FileNotFoundException
from app.utils import cache


router = APIRouter()


class KLine(BaseModel):
    symbol: str
    name: str = None
    data: List[list] = []
    count: int


@router.get('/kline/{code}', response_model=KLine)
@cache(3600)
async def stock_daily(code: str):
    fp = os.path.join(STOCK_DAILY_PATH, code)
    if not os.path.isfile(fp):
       raise FileNotFoundException(fp)
    columns = ['trade_date', 'pre_close', 'open','high',
               'low', 'close', 'vol', 'amount']
    df = pd.read_csv(fp)[columns]
    data = np.array(df[::-1]).tolist()
    return {'symbol': code, 'name': code,
            'data': data, 'count': df.shape[0]}

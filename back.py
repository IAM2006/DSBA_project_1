import model
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

class HouseData(BaseModel):
    beds: float
    baths: float
    sqft: float
    nb: int

app = FastAPI()

@app.post('/price')
async def price_prediction(data: HouseData):
    dt = dict(data)
    res = model.predict(dt['beds'], dt['baths'], dt['sqft'], dt['nb'])
    return {
        'result': res
    }
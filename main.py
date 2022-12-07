from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    id: int


class Data(BaseModel):
    feature_1: float
    feature_2: str


app = FastAPI(
    name="ShinyApp",
    description="Small web application",
    version="0.0.1"
)


# Should be placed on top so "items" does not become a category
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}


@app.post("/{category}")
async def create_item(category: str, amount: int, item: Item):
    return {"category": category, "amount": amount, "item": item}


@app.post("/")
async def ingest_data(data: Data):
    if data.feature_1 < 0.:
        raise HTTPException(status_code=404, detail=f"feature 1 is negative: {data.feature_1}")

    if len(data.feature_2) > 280:
        raise HTTPException(status_code=404, detail=f"feature 2 string length is too big: {len(data.feature_2)}")
    return data

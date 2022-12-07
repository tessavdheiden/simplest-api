from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    id: int


app = FastAPI()


@app.get("/")
async def welcome():
    return {"Hello": "Master"}


# Should be placed on top so "items" does not become a category
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}


@app.post("/{category}")
async def create_item(category: str, amount: int, item: Item):
    return {"category": category, "amount": amount, "item": item}

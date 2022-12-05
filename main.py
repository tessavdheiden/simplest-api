from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    id: int


app = FastAPI()


@app.post("/{category}")
async def create_item(category: str, amount: int, item: Item):
    return {"category": category, "amount": amount, "item": item}

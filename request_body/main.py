"""Request body"""
from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    """Item data model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
app = FastAPI()

@app.get("/items")
async def get_items(item: Item):
    """get items"""
    return item

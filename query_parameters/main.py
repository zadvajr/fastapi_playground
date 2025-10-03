"""Query Parameters"""
from fastapi import FastAPI

app = FastAPI()

items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    """Read Items"""
    return items_db[skip : skip + limit]

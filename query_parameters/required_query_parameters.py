"""Required Query Parameters"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str):
    """Read Item"""
    item = {"item_id": item_id, "needy": needy}
    return item

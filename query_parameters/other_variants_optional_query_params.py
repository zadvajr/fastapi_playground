"""Other variants with typing"""
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """Read Item by ID"""
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

"""Type Parameters with types"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Read Item with ID"""
    return {"item_id": item_id}

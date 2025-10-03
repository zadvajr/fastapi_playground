"""Optional Query Parameters"""
#You can declare optional query parameters by setting their default values to None"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    """Read item"""
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
